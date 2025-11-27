from ..db.session import SessionLocal
from ..models.room_model import RoomModel
from ..enums.room_status import RoomStatus


class RoomController:
    def create_room(self, room_number, room_type, status = RoomStatus.AVAILABLE):
        session = SessionLocal()
        try:
            room = RoomModel(
                room_number=room_number,
                room_type=room_type,
                status=status
            )
            session.add(room)
            session.commit()
            session.refresh(room)
            return room
        finally:
            session.close()

    def get_room_by_id(self, room_id):
        session = SessionLocal()
        try:
            return session.get(RoomModel, room_id)
        finally:
            session.close()

    def list_rooms(self):
        session = SessionLocal()
        try:
            return session.query(RoomModel).all()
        finally:
            session.close()

    def delete_room(self, room_id):
        session = SessionLocal()
        try:
            room = session.get(RoomModel, room_id)
            if not room:
                return False
            session.delete(room)
            session.commit()
            return True
        finally:
            session.close()
