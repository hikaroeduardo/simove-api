from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, DateTime, ForeignKey, Date, Time, Enum, CHAR
from datetime import datetime, date, time
from typing import List, Optional
from enum import Enum as EnumPython

class RequestsStatus(EnumPython):
    ABERTO = "aberto"
    ACEITO = "aceito"
    RECUSADO = "recusado"
    FINALIZADO = "finalizado"

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
    requests: Mapped[List["Request"]] = relationship(back_populates="user", cascade="all, delete-orphan")

class Superitendence(Base):
    __tablename__ = "superitendences"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    acronym: Mapped[str] = mapped_column(String(10), unique=True)
    status: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    users: Mapped[List["User"]] = relationship(back_populates="superitendence", cascade="all, delete-orphan")
    requests: Mapped[List["Request"]] = relationship(back_populates="superitendence", cascade="all, delete-orphan")

class Request(Base):
    __tablename__ = "requests"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    id_user: Mapped[int] = mapped_column(ForeignKey("users.id"))
    id_superitendence: Mapped[int] = mapped_column(ForeignKey("superitendences.id"))
    departure_location: Mapped[str] = mapped_column(String(50))
    destination_location: Mapped[str] = mapped_column(String(50))
    date_request: Mapped[date] = mapped_column(Date, default=datetime.today)
    time_request: Mapped[time] = mapped_column(Time, default=lambda: datetime.now().time())
    number_peoples: Mapped[int] = mapped_column(default=1)
    status: Mapped[RequestsStatus] = mapped_column(Enum(RequestsStatus), default=RequestsStatus.ABERTO)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    superitendence: Mapped["Superitendence"] = relationship(back_populates="requests")
    user: Mapped["User"] = relationship(back_populates="requests")

class Driver(Base):
    __tablename__ = "drivers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    cpf: Mapped[str] = mapped_column(String(14))
    registration: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    phone: Mapped[str] = mapped_column(String(15), nullable=True)
    status: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

class Vehicle(Base):
    __tablename__ = "vehicles"

    id: Mapped[int] = mapped_column(primary_key=True)
    model: Mapped[str] = mapped_column(String(20))
    brand: Mapped[str] = mapped_column(String(20))
    plate: Mapped[str] = mapped_column(String(10))
    year: Mapped[str] = mapped_column(String(10))
    color: Mapped[str] = mapped_column(String(20))
    id_fuel: Mapped[int] = mapped_column(ForeignKey("fuels.id"))
    renavam: Mapped[str] = mapped_column(CHAR(11))
    status: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    fuel: Mapped["Fuel"] = relationship(back_populates="vehicles")

class Fuel(Base):
    __tablename__ = "fuels"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(10))

    vehicles: Mapped[List["Vehicle"]] = relationship(back_populates="fuel", cascade="all, delete-orphan")