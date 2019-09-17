"""
Helper script that converts assigner (https://github.com/redkyn/assigner)
rosters into grader (https://github.com/redkyn/grader) compliant rosters.
"""
import yaml

with open("_config.yml") as file_handle:
    roster = yaml.safe_load(file_handle)["roster"]
    grader_roster = []

    for person in roster:
        firstName, lastName = person["name"].split(", ")
        grader_roster.append({
            "id": person["username"],
            "name": "{} {}".format(firstName, lastName)
        })
    out = open("test.yml", "w")
    yaml.dump(grader_roster, out)
    # yaml.dump(
    # print()
