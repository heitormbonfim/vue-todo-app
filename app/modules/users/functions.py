from fastapi import APIRouter

user_router = APIRouter()


@user_router.post("/create/todo", status_code=201)
async def create_todo():
    return


@user_router.get("/todos")
async def get_todos():
    return
