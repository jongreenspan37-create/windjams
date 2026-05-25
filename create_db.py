
from database import engine, Base
import models 

def init_database():
    print("Connecting to the database and creating tables...")
    
    
    Base.metadata.create_all(bind=engine)
    
    print("Tables created successfully!")

if __name__ == "__main__":
    init_database()
