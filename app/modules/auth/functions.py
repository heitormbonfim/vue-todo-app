from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.database.connection import db_pool


def get_db_conn():
    with db_pool.connection() as conn:
        yield conn


auth_router = APIRouter()


class User(BaseModel):
    name: str
    email: str
    password: str
    role: str = "user"  # Default role as 'user'


@auth_router.post("/register", status_code=201)
async def register(body: User, conn=Depends(get_db_conn)):
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                --begin-sql
                INSERT INTO users (name, email, password, role)
                VALUES (%s, %s, %s, %s)
                RETURNING id;
                """,
                (body.name, body.email, body.password, body.role),
            )
            user_id = cur.fetchone()[0]
            conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        "error": False,
        "message": "User successfully registered",
        "data": {"user_id": user_id},
    }


@auth_router.post("/login")
async def login(conn=Depends(get_db_conn)):
    # Use conn to perform login operations
    return


@auth_router.get("/login")
async def login_with_token(conn=Depends(get_db_conn)):
    # Use conn to perform token-based login operations
    return


@auth_router.post("/change/password")
async def change_password(conn=Depends(get_db_conn)):
    # Use conn to perform password change operations
    return
