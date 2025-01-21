from app.db import get_db_connection

def insert_image(name: str, embedding: list):
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO ai_project.images (name, embedding) VALUES (%s, %s)",
            (name, embedding)
        )
    conn.close()

def search_similar_images(embedding: list, limit: int = 5):
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT id, name, embedding <-> %s::vector AS similarity
            FROM ai_project.images
            ORDER BY similarity ASC
            LIMIT %s;
            """,
            (embedding, limit) 
        )
        results = cur.fetchall()
    conn.close()
    return results