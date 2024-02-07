class Settings():
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_NAME: str
    
    @property
    def DATABASE_URL_asyncpg(self):
        return f"sqlite+aiosqlite:///db.sqlite3"

    @property
    def DATABASE_URL_psycopg(self):
        return f"sqlite+pysqlite:///db.sqlite3"
    
settings = Settings()