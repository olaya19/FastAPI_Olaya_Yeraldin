from auth import (create_access_token, get_current_user, get_password_hash,
                  require_admin, verify_password)
from database import Base, engine, get_db
from fastapi import Depends, FastAPI, HTTPException, status
from models import Favorite, Pedido, Product, User
from schemas import (FavoriteResponse, PedidoCreate, PedidoResponse,
                     ProductCreate, ProductResponse, Token, UserLogin,
                     UserRegister, UserResponse)
from sqlalchemy.orm import Session

app = FastAPI(title="Laundry API")


@app.on_event("startup")
def on_startup():
    # SOLO para desarrollo. En producción usa Alembic.
    Base.metadata.create_all(bind=engine)


# ---------------------- Usuarios ---------------------- #
@app.post("/register", response_model=UserResponse)
def register_user(user_data: UserRegister, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == user_data.username).first():
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user_data.password)
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_password,
        role=getattr(user_data, "role", "cliente_lavanderia"),
        is_active=True,  # ✅ si tu modelo lo tiene
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.post("/login", response_model=Token)
def login_for_access_token(user_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_data.username).first()
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@app.get("/protected")
def protected_endpoint(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello {current_user.username}, you are authenticated."}


@app.get("/admin-only")
def admin_only_endpoint(current_user: User = Depends(require_admin)):
    return {"message": "Welcome, Admin. This is a restricted area."}


# Aquí luego agregas los endpoints de Products y Favorites.


# CREATE
@app.post(
    "/laundry_pedidos/",
    response_model=PedidoResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_pedido(
    pedido: PedidoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Regla simple de duplicado: mismo cliente + fecha_recepcion + tipo_servicio
    dup = (
        db.query(Pedido)
        .filter(
            Pedido.cliente == pedido.cliente,
            Pedido.fecha_recepcion == pedido.fecha_recepcion,
            Pedido.tipo_servicio == pedido.tipo_servicio,
        )
        .first()
    )
    if dup:
        raise HTTPException(status_code=400, detail="Pedido ya existe")

    new = Pedido(
        cliente=pedido.cliente,
        prendas=pedido.prendas,
        tipo_servicio=pedido.tipo_servicio,
        fecha_recepcion=pedido.fecha_recepcion,
        fecha_entrega=pedido.fecha_entrega,
        estado=pedido.estado,
    )
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


# READ by id
@app.get("/laundry_pedidos/{pedido_id}", response_model=PedidoResponse)
def get_pedido(
    pedido_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        # Mensaje exacto que esperan los tests (lowercase)
        raise HTTPException(status_code=404, detail="pedido no encontrado")
    return pedido


# READ all
@app.get("/laundry_pedidos/", response_model=list[PedidoResponse])
def get_all_pedidos(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    return db.query(Pedido).all()


# UPDATE (full)
@app.put("/laundry_pedidos/{pedido_id}", response_model=PedidoResponse)
def update_pedido(
    pedido_id: int,
    update: PedidoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="pedido no encontrado")
    # Validaciones extras (por seguridad)
    if update.prendas <= 0:
        raise HTTPException(status_code=422, detail="prendas debe ser mayor que 0")
    if update.fecha_entrega < update.fecha_recepcion:
        raise HTTPException(
            status_code=422, detail="fecha_entrega debe ser >= fecha_recepcion"
        )

    pedido.cliente = update.cliente
    pedido.prendas = update.prendas
    pedido.tipo_servicio = update.tipo_servicio
    pedido.fecha_recepcion = update.fecha_recepcion
    pedido.fecha_entrega = update.fecha_entrega
    pedido.estado = update.estado

    db.commit()
    db.refresh(pedido)
    return pedido


# DELETE protegido por admin
@app.delete("/laundry_pedidos/{pedido_id}", status_code=status.HTTP_200_OK)
def delete_pedido(
    pedido_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):  # <-- require_admin
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="pedido no encontrado")
    db.delete(pedido)
    db.commit()
    return {"detail": "pedido eliminado"}
