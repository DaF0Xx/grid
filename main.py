from functions import build_matrix
from functions import render

height = 5 # Height of the grid
matrix = build_matrix(height) # Our matrix of positions

character = {"position":[0,0]} # Character attributes

print(render(matrix, character["position"]))
# running = True
# while running:
#     try:
#         move = input("w, a, s, d: ").lower()
#         if move == 'a':
#             character["position"][0] -= 1
#         elif move == 'd':
#             character["position"][0] += 1
#         elif move == 'w':
#             character["position"][1] += 1
#         elif move == 's':
#             character["position"][1] -= 1
#         else:
#             # print("Invalid move! try again.")
#             # continue
#             break
#     except KeyboardInterrupt:
#         print("\nExiting...")
#         break

#     print(f"position: {character["position"]}")