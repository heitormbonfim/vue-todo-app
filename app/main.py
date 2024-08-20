from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

# from app.modules.utils.mock_router import mock_router
# from app.modules.auth.functions import auth_router
# from app.modules.users.functions import user_router
# from app.database.connection import create_tables

app = FastAPI()


@app.get("/api/alive", status_code=200)
async def example():
    return {"error": False, "message": "API up and running"}


# app.include_router(mock_router, prefix="/mock")
# app.include_router(user_router, prefix="/api")
# app.include_router(auth_router, prefix="/api/auth")

# Serve static files
app.mount("/static", StaticFiles(directory="public"), name="static")


@app.get("/{path_name:path}")
async def serve_vue_app(path_name: str):
    if path_name in ["favicon.ico", "robots.txt", "sitemap.xml"]:
        return FileResponse(Path("public") / path_name)
    file_path = Path("public") / path_name
    if file_path.is_file():
        return FileResponse(file_path)
    return FileResponse(Path("public") / "index.html")


if __name__ == "__main__":
    import uvicorn

    # Start dev server
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
