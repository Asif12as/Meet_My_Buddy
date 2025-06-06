# Your Buddy

A fun web application where users can chat with their virtual "buddy" - a friendly AI companion that speaks in casual slang and knows personal details about you, but is hilariously clueless about general knowledge.

## Features

- Chat interface with a friendly AI buddy
- Buddy responds in casual, slang-heavy language
- Buddy knows personal details about the developer
- Buddy intentionally fails at general knowledge questions
- Responsive design that works on desktop and mobile

## Tech Stack

- **Frontend**: React
- **Backend**: Python with FastAPI
- **AI**: Groq API (using Llama 3 model)

## Project Structure

```
Your_Buddy/
├── frontend/           # React frontend
│   ├── public/         # Public assets
│   └── src/            # React source code
│       ├── components/ # React components
│       └── ...         # Other frontend files
└── backend/            # FastAPI backend
    ├── main.py         # Main API code
    └── requirements.txt # Python dependencies
```

## Setup Instructions

### Prerequisites

- Node.js and npm
- Python 3.8 or higher
- Groq API key (sign up at https://console.groq.com)

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Create a `.env` file based on `.env.example` and add your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

6. Start the backend server:
   ```
   python main.py
   ```
   The API will be available at http://localhost:8000

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm start
   ```
   The frontend will be available at http://localhost:3000

## Customization

To personalize your buddy, edit the `DEVELOPER_INFO` variable in `backend/main.py` with your own personal details.

## License

MIT