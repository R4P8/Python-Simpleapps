from app import create_app
import app.tracing
from app.database import get_connection

app = create_app()


def check_database_connection():
    try:
        connection = get_connection()

        if connection:
            print("✅ PostgreSQL Connected Successfully")

        connection.close()

    except Exception as error:
        print("❌ Database Connection Failed")
        print(f"Error: {error}")


if __name__ == "__main__":
    check_database_connection()

    print("🚀 Flask API Running On Port 5005")

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5005
    )