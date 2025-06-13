from typing import List
from fastapi import(
    FastAPI,
    APIRouter,
    status,
    HTTPException
)
from sqlalchemy import select

from ..schemas import ItemSchema
from ..db import Session, Item


items_router = APIRouter(prefix='/items', tags=['Item'])


async def get_item(item_id: int, session):
    item = session.scalar(select(Item).where(Item.id == item_id))
    if not item:
        raise HTTPException(
            detail=f'Айтем з айді #{item_id} не знайдено',
            status_code=status.HTTP_404_NOT_FOUND
        )
    return item


@items_router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_item(data: ItemSchema):
    with Session.begin() as session:
        item = Item(**data.model_dump())
        session.add(item)

    return 'Created!'


@items_router.get('/all', response_model=List[ItemSchema])
async def get_all_items():
    with Session.begin() as session:
        items = session.scalars(select(Item))
        return [ItemSchema.model_validate(item) for item in items]


@items_router.get('/{item_id}', response_model=ItemSchema)
async def item_info(item_id: int):
    with Session.begin() as session:
        item = await get_item(item_id=item_id, session=session)
        return ItemSchema.model_validate(item)
    

@items_router.put('/update/{item_id}', response_model=ItemSchema)
async def update_item(item_id: int, data: ItemSchema):
    with Session.begin() as session:
        item = await get_item(item_id, session)
        for key, value in data.model_dump().items():
            setattr(item, key, value)
        return ItemSchema.model_validate(item)



@items_router.delete('/delete/{item_id}')
async def delete_item(item_id: int):
    with Session.begin() as session:
        item = await get_item(item_id, session)
        if item:
            session.delete(item)
            return 'Deleted!'
        
