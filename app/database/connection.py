import psycopg_pool

# Create a global connection pool
db_pool = psycopg_pool.ConnectionPool(
    "dbname=postgres user=postgres password=6794 host=127.0.0.1 port=5432"
)


def get_db_conn():
    # Function to get a connection from the pool
    return db_pool.connection()


def create_tables():
    try:
        print("creating databases (if they don't exist)")

        with get_db_conn() as conn:
            with conn.cursor() as cur:
                # Enable the pgcrypto extension for UUID generation
                cur.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto;")

                # Create tables
                cur.execute(
                    """
                    --begin-sql
                    CREATE TABLE IF NOT EXISTS users (
                        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                        name VARCHAR(255),
                        email VARCHAR(255) UNIQUE,
                        password TEXT,
                        role VARCHAR(50)
                    );
                    """
                )

                cur.execute(
                    """
                    --begin-sql
                    CREATE TABLE IF NOT EXISTS todos (
                        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                        user_id UUID REFERENCES users(id) ON DELETE CASCADE,
                        task TEXT NOT NULL,
                        completed BOOLEAN DEFAULT FALSE
                    );
                    """
                )

            conn.commit()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    create_tables()
