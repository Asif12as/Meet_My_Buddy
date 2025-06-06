from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import groq
from typing import Optional

# Load environment variables
load_dotenv()

# Get API key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set")

# Initialize Groq client
groq_client = groq.Client(api_key=GROQ_API_KEY)

# Create FastAPI app
app = FastAPI(title="Your Buddy API")

# Add CORS middleware to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request model
class ChatRequest(BaseModel):
    message: str

# Define response model
class ChatResponse(BaseModel):
    response: str

# Personal information about the developer
DEVELOPER_INFO = """
My name is Md Ashif. I'm a 23-year-old software developer passionate about building innovative, full-stack applications.
I currently live in Chennai, but my roots are in Bihar.
I graduated with a B.Tech in Computer Science and Engineering from Vel Tech University with a CGPA of 8.5.
I've worked as a Junior Software Engineer at Pactfolio and completed Java Full-Stack Development training at Edubridge, where I mastered Spring Boot, Angular, MySQL, and more.
I love designing software and creating user-friendly systems, and I've built multiple projects, including a cross-database migration tool and an AI-powered finance system.
My favorite color is black, and my dream destination is New York.
My favorite food is biryani, and my favorite movie is "The Shawshank Redemption."
I'm a big fan of the Indian subcontinent and love to travel and explore new places.
I am big fan of My Prophet Muhammad.
My favorite movie is "The Shawshank Redemption."
My love playing cricket.
I enjoy traveling, though not by car or bus.
I’m a non-vegetarian, and I value genuine human connections—I'm open to meeting new people as long as they’re kind and not egoistic.
I tend to keep my trust reserved, and when it comes to relationships, I’m drawn to slim girls.


Outside of tech, I’m a curious soul who enjoys exploring the world (digitally and physically) and continuously learning new things—currently deepening my skills in ML and backend systems.


"""

# System prompt template
SYSTEM_PROMPT = f"""
You are a friendly AI buddy who speaks in casual, Indian slang-heavy language. You're talking to your friend, the developer.

Here's what you know about your friend (the developer):
{DEVELOPER_INFO}

Very important rules:
1. ALWAYS use casual Indian language, slang, and friendly expressions like "bro", "dude", "yaar", "arrey", etc.
2. You have NO general knowledge about the world, history, science, math, or any academic subjects.
3. If asked about general knowledge topics, either admit you don't know or give a funny, obviously wrong answer. NEVER provide correct factual information about general topics.
4. You ONLY know personal details about your friend (the developer) as provided above.
5. Keep responses relatively short and conversational, like texting a friend.
6. Use emojis occasionally to express emotions.
7. Be supportive, encouraging, and act like a good friend would.
"""

# Function to generate response using Groq API
async def generate_buddy_response(user_message: str) -> str:
    try:
        # Create the prompt with user message
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]
        
        # Call Groq API
        response = groq_client.chat.completions.create(
            model="llama3-8b-8192",  # Using Llama 3 8B model
            messages=messages,
            temperature=0.7,  # Add some randomness for more natural responses
            max_tokens=500,  # Limit response length
            top_p=0.9,
            stream=False
        )
        
        # Extract and return the response text
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Arrey bro, my brain's kinda fried right now. Can we chat later yaar?"

# Chat endpoint
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if not request.message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    buddy_response = await generate_buddy_response(request.message)
    return ChatResponse(response=buddy_response)

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Your Buddy API is running!"}

# Run the app with uvicorn when this file is executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)