from app import create_app
import uvicorn

# ====================
# Note: replace "app:create_app" with app and 
# remove reload=True to remove hot reloading
# ====================
if __name__ == '__main__':
    app = create_app()
    uvicorn.run("app:create_app", host='0.0.0.0', port=9000, reload=True, factory=True)