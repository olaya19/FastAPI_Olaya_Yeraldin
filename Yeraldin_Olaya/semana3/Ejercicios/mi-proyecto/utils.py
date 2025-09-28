import logging
from datetime import datetime
from typing import Any, Dict, Optional


def create_response(
    success: bool,
    data: Any = None,
    message: str = "Operation completed successfully",
    error_code: Optional[str] = None,
) -> Dict[str, Any]:
    response = {"success": success, "timestamp": datetime.now().isoformat()}
    if success:
        response["data"] = data
        response["message"] = message
    else:
        response["error_code"] = error_code
        response["message"] = message
    return response


def get_total_borrowed_books() -> int:
    # Lógica de ejemplo, podría ser una base de datos real
    return 5
