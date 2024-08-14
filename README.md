# Run this server

## Activate Virtual Environment (Windows git bash)

- To activate

```bash
source .venv/Scripts/activate
```

- To deactivate

```bash
deactivate
```

## Using Powershell

- To allow scripts

```bash
  Set-ExecutionPolicy Unrestricted -Scope Process
```

- To activate

```bash
.\.venv\Scripts\Activate.ps1
```

- To deactivate

```bash
.\.venv\Scripts\deactivate.bat
```

## Using Linux

- To activate

```bash
source .venv/bin/actiave
```

- To deactivate

```bash
deactivate
```

## Python Version

- Python 3.12.5
- Pip 24.2

## Install packages

```bash
pip install -r requirements.txt
```

### **1. Development Environment**

For development, you typically use `uvicorn` with the `--reload` option. This enables automatic reloading when code changes, which is useful for iterative development.

**Steps to run FastAPI in development:**

1. **Activate the Virtual Environment** (if not already activated):

   ```bash
   source .venv/Scripts/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Run Uvicorn with Reload**:

   ```bash
   uvicorn app.main:app --reload
   ```

   - `--reload` enables automatic reloading.
   - `app.main:app` specifies the module and the FastAPI app instance.

### **2. Production Environment**

For production, you should use a robust ASGI server like `uvicorn` or `gunicorn` with `uvicorn` workers, and ideally, place it behind a reverse proxy like Nginx.

**Steps to run FastAPI in production:**

1. **Set Up Uvicorn for Production**:

   Run Uvicorn with more workers and without the reload option:

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
   ```

   - `--host 0.0.0.0`: Makes the server accessible externally.
   - `--port 8000`: Specifies the port.
   - `--workers 4`: Specifies the number of worker processes (adjust based on your server’s CPU).

2. **Using Gunicorn with Uvicorn Workers**:

   For more advanced setups, especially on Unix-based systems, use `gunicorn` with `uvicorn` workers:

   **Install Gunicorn:**

   ```bash
   pip install gunicorn
   ```

   **Run Gunicorn with Uvicorn Workers:**

   ```bash
   gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
   ```

   - `-w 4`: Specifies the number of worker processes (adjust based on your server’s CPU).
   - `-k uvicorn.workers.UvicornWorker`: Uses Uvicorn as the worker class.

3. **Reverse Proxy with Nginx** (Optional but recommended):

   Set up Nginx to proxy requests to your FastAPI server. This handles HTTPS, load balancing, and serves static files efficiently.

   **Basic Nginx Configuration:**

   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

   - Save this configuration in `/etc/nginx/sites-available/yourproject` and create a symbolic link to `/etc/nginx/sites-enabled/`.
   - Restart Nginx with `sudo systemctl restart nginx`.
