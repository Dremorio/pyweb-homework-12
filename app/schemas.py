from pydantic import BaseModel, EmailStr, Field
from datetime import date


class ContactBase(BaseModel):
    first_name: str = Field(..., max_length=100)
    last_name: str = Field(..., max_length=100)
    email: EmailStr
    phone_number: str
    birthday: date


class ContactCreate(ContactBase):
    pass


class ContactUpdate(ContactBase):
    pass


class Contact(ContactBase):
    id: int
    additional_data: str | None = None

    class Config:
        orm_mode = True
