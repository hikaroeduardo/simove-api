from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, DateTime, ForeignKey
from datetime import datetime
from typing import List

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str]
    phone: Mapped[str] = mapped_column(String(15), nullable=True)
    id_superitendence: Mapped[int] = mapped_column(ForeignKey("superitendences.id"))
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    status: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    superitendence: Mapped["Superitendence"] = relationship(back_populates="users")

class Superitendence(Base):
    __tablename__ = "superitendences"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    acronym: Mapped[str] = mapped_column(String(10), unique=True)
    status: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    users: Mapped[List["User"]] = relationship(back_populates="superitendence", cascade="all, delete-orphan")