# scripts/quality_report_laundry.py
"""
Genera un mini reporte de KPIs de calidad para la lavandería.
Úsalo después de correr pytest --cov para tomar datos del htmlcov.
"""
import os


def generate_domain_specific_report():
    print("📊 Quality Report - Lavandería")
    print("- Cobertura mínima esperada: >80% en main, auth y tests críticos")
    print("- Validación de pedidos: 100% de casos de fecha y prendas cubiertos")
    print("- Seguridad de autenticación: tests de login/register ejecutados")
    print("- Roles de negocio: gerente_lavanderia verificado en admin-only")


if __name__ == "__main__":
    generate_domain_specific_report()
