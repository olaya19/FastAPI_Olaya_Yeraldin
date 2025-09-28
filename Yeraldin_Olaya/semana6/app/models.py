from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, DateTime
from sqlalchemy.sql import func
from database import Base  # ✅ Base único

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="user")
    is_active = Column(Boolean, default=True)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer)  # En centavos
    created_by = Column(Integer, ForeignKey("users.id"))

class Favorite(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

class Pedido(Base):
    __tablename__ = "laundry_pedidos"
    id = Column(Integer, primary_key=True, index=True)
    cliente = Column(String(200), nullable=False)
    prendas = Column(Integer, nullable=False)
    tipo_servicio = Column(String(100), nullable=False)
    fecha_recepcion = Column(Date, nullable=False)
    fecha_entrega = Column(Date, nullable=False)
    estado = Column(String(50), nullable=False, default="pendiente")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
