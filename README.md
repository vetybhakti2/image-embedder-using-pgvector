# Image Similarity Search with FastAPI and PGVector

## Running the Project

Follow these steps to run the project:

1. **Set Up PostgreSQL with PGVector**
   - Ensure PostgreSQL is running.
   - Add the `pgvector` extension by running the following SQL command:
     ```sql
     CREATE EXTENSION IF NOT EXISTS vector;
     ```

2. **Build and Run the Application Using Docker**
   - Build the Docker image:
     ```bash
     docker build -t image-to-vector .
     ```
   - Run the Docker container:
     ```bash
     docker run -p 8000:8000 --env-file .env image-to-vector
     ```

3. **Access the API Endpoints**
   - **Upload Image**
     - Endpoint: `POST /upload/`
     - Description: Upload an image to generate and store its embedding.
   
   - **Search for Similar Images**
     - Endpoint: `POST /search/`
     - Description: Search for images similar to the provided embedding.