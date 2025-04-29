from db.models import UserChitmil
from db.base import async_session
from sqlalchemy import select

async def save_chitmil_data(telegram_id: int, data: dict):
    async with async_session() as session:
        chitmil = UserChitmil(
            telegram_id=telegram_id,
            what_allow=data["what_allow"],
            day_name=data["day_name"],
            period=data["period"],
            increase=data["increase"]
        )
        session.add(chitmil)
        await session.commit()

async def get_user_chitmils(telegram_id: int):
    async with async_session() as session:
        result = await session.execute(
            select(UserChitmil).where(UserChitmil.telegram_id == telegram_id)
        )
        return result.scalars().all()
