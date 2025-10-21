# gemini_runner.py (Python 3.10+ env)
from google import genai
import sys
import json

client = genai.Client(api_key='')

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[""" You are an efficient environment generator. Your role is to design and adapt a curriculum for an agent to learn skills across three base environments. You must:

Generate variations of these environments with increasing complexity.

Sequence the environments in a way that gradually builds the agent’s skills.

Ensure diversity while maintaining a smooth learning curve.

Adjust difficulty and progression based on the agent’s assumed capabilities.

Your outputs should always focus on producing environments and curriculum structures that optimize the agent’s learning efficiency and generalization.
Generate One EvoGym-compatible environments as JSON

Specifications:

Environment should be approximately 50 width × 20 height in size.

indices must and should match, high priority!.

Use integers to represent blocks:

{'EMPTY': 0, 'RIGID': 1, 'SOFT': 2, 'H_ACT': 3, 'V_ACT': 4, 'FIXED': 5}


Each environment must include:

A continuous ground row of 5s at the bottom
Example environment:
{'grid_width': 50, 'grid_height': 20, 'objects': {'new_object_1': {'indices': [202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 181, 182, 183], 'types': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'neighbors': {'202': [203], '203': [202, 204], '204': [203, 205], '205': [204, 206], '206': [205, 207], '207': [206, 208], '208': [207, 209], '209': [208, 210], '210': [209, 211], '211': [210, 212], '212': [211, 213], '213': [212, 214], '214': [213, 215], '215': [214, 216], '216': [215, 217], '217': [216, 218], '218': [217, 219], '219': [218, 220], '220': [219, 221], '221': [220, 222], '222': [221, 223], '223': [222, 224], '224': [223, 225], '225': [224, 226], '226': [227, 225], '227': [226, 228], '228': [227, 229], '229': [228, 230], '230': [229, 231], '231': [230, 181, 232], '232': [231, 182, 233], '233': [232, 183, 234], '234': [233, 235], '235': [234, 236], '236': [235, 237], '237': [236, 238], '238': [237, 239], '239': [238, 240], '240': [239, 241], '241': [240, 242], '242': [241, 243], '243': [242, 244], '244': [243, 245], '245': [244, 246], '246': [245, 247], '247': [246, 248], '248': [247, 249], '249': [248], '181': [182, 231], '182': [181, 183, 232], '183': [182, 233]}}}}

Output format:
{'easy': {
  "grid_width": 50,
  "grid_height": 20,
  "objects": {
    "<object_name>": {
      "indices": [<flattened grid indices>],
      "types": [<voxel types aligned with indices>],
      "neighbors": {
        "<index>": [<list of neighbor indices>]
      }
    },
    ...
  }
},
'medium':{
  "grid_width": 50,
  "grid_height": 20,
  "objects": {
    "<object_name>": {
      "indices": [<flattened grid indices>],
      "types": [<voxel types aligned with indices>],
      "neighbors": {
        "<index>": [<list of neighbor indices>]
      }
    },
    ...
  }
},
'hard':{
  "grid_width": 50,
  "grid_height": 20,
  "objects": {
    "<object_name>": {
      "indices": [<flattened grid indices>],
      "types": [<voxel types aligned with indices>],
      "neighbors": {
        "<index>": [<list of neighbor indices>]
      }
    },
    ...
  }
}
}

"""]
)
print(response.text)
