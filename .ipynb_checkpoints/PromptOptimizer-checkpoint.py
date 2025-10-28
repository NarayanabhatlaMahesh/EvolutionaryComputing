import sys
import json
from google import genai

# Initialize Gemini
client = genai.Client(api_key="AIzaSyCoSIzQjBTsRZ4y3GJdCeFPDGsIupLd3Hg")

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
        contents=["""Encourage variety by adjusting:

Terrain shape (ramps, pits, stairs)

Task objectives

Material composition (mix of rigid, soft, actuator voxels)

Maintain realism by grounding the design in plausible soft-body mechanics — e.g., robots should crawl, jump, or deform naturally.

Avoid "fantasy" objects or abstract floating mazes that violate 2D voxel physics.""",prompt]
    )

    # --- Print clean Gemini output ---
    print(json.dumps(response.text, ensure_ascii=False))

if __name__ == "__main__":
    main()
