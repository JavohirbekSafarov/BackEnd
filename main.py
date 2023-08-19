from fastapi import FastAPI, HTTPException, Form

app = FastAPI()

# Simulated user database
fake_users_db = {}


@app.post("/register")
async def register(username: str = Form(...), password: str = Form(...)):
    if username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already exists")

    # In a real application, you should hash the password before storing it.
    fake_users_db[username] = {"username": username, "password": password}

    return {"message": "Registration successful"}
