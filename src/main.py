from fastapi import FastAPI, HTTPException

app = FastAPI()

# Beispiel-Datenbank
database = {
    "1234567890123": {"name": "Produkt A", "price": 10.99, "stock": 100, "gewicht": 350},
    "9876543210987": {"name": "Produkt B", "price": 15.49, "stock": 50, "gewicht": 100},
}

@app.get("/ean")
async def get_attribute(ean: str, attribute: str):
    if ean in database:
        if attribute in database[ean]:
            return database[ean][attribute]
        else:
            raise HTTPException(status_code=404, detail="Attribut nicht gefunden")
    else:
        raise HTTPException(status_code=404, detail="EAN nicht gefunden")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)