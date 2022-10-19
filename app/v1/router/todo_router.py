from fastapi import APIRouter, Depends, Body
from fastapi import status

from app.v1.schema import todo_schema
from app.v1.service import todo_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix="/api/v1/to-do", tags=["to-do"])


@router.post("/",
             status_code=status.HTTP_201_CREATED,
             response_model=todo_schema.Todo,
             dependencies=[Depends(get_db)],
             summary="Create a new to-do"
             )
def create_todo(todo: todo_schema.TodoCreate = Body(...),
                current_user: User = Depends(get_current_user)):
    """
    # Crear a new to-do

    ## Args
    The app can recive next fields into a JSON
    - title: A description for todo

    ## Return
    - todo: Todo info
    """
    return todo_service.create_task(todo, current_user)
