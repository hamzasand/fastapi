from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

def varify_token(token: str = Header(None)):
    if token!= "mysecrettoken":
        raise HTTPException(
            status_code= 401,
            detail ="Unauthorized"
        )
    return {
        "user":"Authorized"
    }

@app.get("/secure-data")
def secure_data(user= Depends(varify_token)):
    return {
        "message": "secure data acess",
        "user": user
    }

@app.get("/dashboar")
def user_dashboard(user=Depends(varify_token)):
    return {
        "message": "User dashboard data available",
        "data": user
    }