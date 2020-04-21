from app.api.models import NoteSchema
from app.db import notes, database


async def post(payload: NoteSchema):
    """Create new note with values from payload

    Arguments:
        payload {NoteSchema} -- Note data

    Returns:
        int -- note id of the created note
    """
    query = notes.insert().values(title=payload.title, description=payload.description)
    return await database.execute(query=query)


async def get(id: int):
    """select data from database

    Arguments:
        id {str} -- note id

    Returns:
        note -- A note object
    """
    query = notes.select().where(id == notes.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    """Returns all note records currently in database

    Returns:
        list -- List of Note dictionaries
    """
    query = notes.select()
    return await database.fetch_all(query=query)


async def put(id: int, payload: NoteSchema):
    query = (
        notes
        .update()
        .where(id == notes.c.id)
        .values(title=payload.title, description=payload.description)
        .returning(notes.c.id)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = notes.delete().where(id == notes.c.id)
    return await database.execute(query=query)
