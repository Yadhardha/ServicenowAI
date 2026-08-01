import google.generativeai as genai


API_KEY = "GEMINI_API_KEY"

genai.configure(api_key=API_KEY)


model = genai.GenerativeModel("gemini-2.5-flash")


