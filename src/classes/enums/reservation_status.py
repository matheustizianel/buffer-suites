from enum import Enum

class ReservationStatus(Enum):
    ACTIVE = "active"
    CHECKED_IN = "checked_in"
    COMPLETED = "completed"
    CANCELLED = "cancelled"