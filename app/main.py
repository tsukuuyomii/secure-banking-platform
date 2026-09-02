from fastapi import FastAPI

app = FastAPI( 
    title="Secure Banking Platform",
    description="A security-focused cloud banking platform",
    version="1.0.0",
)

@app.get("/health")
def health_check():
    return {"status": "healthy"}