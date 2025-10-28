import sys
import json
from google import genai

# Initialize Gemini
client = genai.Client(api_key="")

def main():
    args = sys.argv[1:]

    if not args:
        print("No prompt provided.")
        return

    prompt = " ".join(args)

    # print(f"[DEBUG] Received prompt: {prompt}", flush=True)

    # --- Call Gemini ---
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=["""You are a json file parser, u check for missing syntax and fill the gaps in any given json file. give no spaces, give in single    line""",prompt,'just give only json format, nothing extra. output:{...,...,...}'])

    # --- Print clean Gemini output ---
    print(json.dumps(response.text, ensure_ascii=False))

if __name__ == "__main__":
    main()
