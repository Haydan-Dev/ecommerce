from fastapi import FastAPI 

# abb idhar ojbect ko variable me store kiya hai 
app = FastAPI()

# idhar uss variable ke help se FastAPI() object ke get fucntion yaa method ko call kiya hai
@app.get("/")
def Home():
    return{"Message":"main.py is working and now running on FastAPI perfectly fine"}


