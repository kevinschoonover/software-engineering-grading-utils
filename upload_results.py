"""
Utility script for tasking a results.json from grading and uploading it to each
student's repo
"""
import os
import shutil

import git

result_path = "assignments/hw00/results/"
repos_dir = "test/hw00"


for result in os.listdir(result_path):
    full_path = os.path.join(result_path, result)
    username = result.split(".")[0]
    output_repo = os.path.join(repos_dir, username)

    shutil.copyfile(full_path, os.path.join(output_repo, "results.json"))

    repo = git.Repo(output_repo)
    print(repo)
    repo.index.add(["results.json"])
    repo.index.commit("adding results")
    repo.remotes.origin.push()
