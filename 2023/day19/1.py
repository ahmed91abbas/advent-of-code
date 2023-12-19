import re

with open("data.in", "r") as f:
    lines = f.read()

chunks = lines.split("\n\n")


def process_workflow(workflow, part):
    for rule in workflow:
        if ":" not in rule:
            return rule
        condition, next_workflow = rule.split(":")
        pattern = r"(\w+)([<>])(\d+)"
        match = re.match(pattern, condition)
        name, operator, value = match.groups()
        value = int(value)
        if operator == "<":
            if part[name] < value:
                return next_workflow
        elif operator == ">":
            if part[name] > value:
                return next_workflow
    assert False


workflows = {}
for line in chunks[0].splitlines():
    pattern = r"(\w+)\{(.*)\}"
    match = re.match(pattern, line)
    name, workflow = match.groups()
    workflow = workflow.split(",")
    workflows[name] = workflow

parts = []
for line in chunks[1].splitlines():
    pattern = r"\{(.*)\}"
    match = re.match(pattern, line)
    part = match.groups()[0]
    part = part.split(",")
    part = [p.split("=") for p in part]
    part = {k: int(v) for k, v in part}
    parts.append(part)


current_workflow = "in"
rejected = []
accepted = []
for part in parts:
    while current_workflow != "R" and current_workflow != "A":
        current_workflow = process_workflow(workflows[current_workflow], part)
        if current_workflow == "R":
            rejected.append(part)
        elif current_workflow == "A":
            accepted.append(part)
    current_workflow = "in"

result = 0
for part in accepted:
    result += sum(part.values())

print(result)
