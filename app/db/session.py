import logging
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
from app.core.config import Settings
from fastapi import HTTPException, status


logger = logging.getLogger("uvicorn.error")
engine = create_engine(Settings.DATABASE_URL, echo=False)
LocalSession = sessionmaker(autocommit = False, autoflush= False, bing = engine)

def get_deb():
    try: 
        db = LocalSession()
        yield db
    except OperationalError as es: 
        logger.error(f"Error en la conexión a la base de datos: {e}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            datail= "Error en la base de datos"
        )
    finally:
        if db is not None:
            db.close()



