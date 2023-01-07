import random
import os
import git

# Generate 340 random codes
codes = {}
for i in range(1, 341):
  code = ''.join(random.choices(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], k=10))
  codes[f"code{i}"] = code

# Write codes to file
with open("codes.txt", "w") as f:
    for key, code in codes.items():
        f.write(f"{key}: {code}\n")

# Initialize repository
repo = git.Repo.init(".")

# Add and commit changes
repo.index.add(["codes.txt"])
repo.index.commit("Added codes.txt")

# Push changes to remote repository
origin = repo.remote(name="origin")
origin.push()
