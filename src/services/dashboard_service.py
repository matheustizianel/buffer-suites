from src.db.session import SessionLocal

from src.models.guest_model import GuestModel
from src.models.room_model import RoomModel
from src.models.reservation_model import ReservationModel

from src.enums.room_status import RoomStatus
from src.enums.reservation_status import ReservationStatus

class DashboardService:
    @staticmethod
    def get_dashboard_stats():
        session = SessionLocal()
        try:
            stats = {}

            stats["guests_total"] = session.query(GuestModel).count()

            stats["guests_occupied"] = session.query(ReservationModel).filter(
                ReservationModel.status == ReservationStatus.CHECKED_IN
            ).count()

            stats["reservations_active"] = session.query(ReservationModel).filter(
                ReservationModel.status.in_([ReservationStatus.ACTIVE, ReservationStatus.CHECKED_IN])
            ).count()

            stats["rooms_available"] = session.query(RoomModel).filter(
                RoomModel.status == RoomStatus.AVAILABLE
            ).count()

            stats["rooms_occupied"] = session.query(RoomModel).filter(
                RoomModel.status == RoomStatus.OCCUPIED
            ).count()

            stats["reservations_cancelled"] = session.query(ReservationModel).filter(
                ReservationModel.status == ReservationStatus.CANCELLED
            ).count()

            return stats

        finally:
            session.close()
