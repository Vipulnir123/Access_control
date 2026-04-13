# Access Request Approval Engine (Split Access Version)

requests = [
    {"user": "Asha", "role": "Engineer", "access": "GitHub"},
    {"user": "Ravi", "role": "HR", "access": "Jira"},
    {"user": "Neha", "role": "Engineer", "access": "Slack"},
    {"user": "Kiran", "role": "Finance", "access": "GitHub"},
    {"user": "Arjun", "role": "HR", "access": "Slack"},
    {"user": "Maya", "role": "Engineer", "access": "Jira"},
    {"user": "Test", "role": "Engineer", "access": ["GitHub", "Slack","lll"]},
    {"user": "Bad", "role": "", "access": "GitHub"},
    {"user": "MultiFail", "role": "HR", "access": ["Jira", " "]}
]

ACCESS_RULES = {
    "Engineer": {"GitHub", "Slack"},
    "HR": {"Jira"},
    "Finance": set()
}

ALL_PLATFORMS = {"GitHub", "Slack", "Jira"}


def validate_request(req):
    required_fields = ["user", "role", "access"]

    for field in required_fields:
        if field not in req or req[field] in [None, "", []]:
            return False

    return True


def normalize_access(access):
    if isinstance(access, list):
        return access
    return [access]


def evaluate_single_access(role, access):
    """Evaluate one access item"""
    
    if access is None or str(access).strip() == "":
        return "Invalid"
    
    if role not in ACCESS_RULES:
        return "Rejected"

    if access not in ALL_PLATFORMS:
        return "Rejected"

    if access not in ACCESS_RULES[role]:
        return "Rejected"

    return "Approved"


def process_requests(requests):
    results = []

    summary = {
        "total": 0,
        "approved": 0,
        "rejected": 0,
        "invalid": 0
    }

    for req in requests:

        # If invalid → single invalid entry
        if not validate_request(req):
            result = {
                "user": req.get("user"),
                "role": req.get("role"),
                "access": req.get("access"),
                "status": "Invalid"
            }
            results.append(result)

            summary["total"] += 1
            summary["invalid"] += 1
            continue

        user = req["user"]
        role = req["role"]
        access_list = normalize_access(req["access"])

        # Process each access separately
        for access in access_list:
            status = evaluate_single_access(role, access)

            result = {
                "user": user,
                "role": role,
                "access": access,
                "status": status
            }

            results.append(result)

            summary["total"] += 1
            summary[status.lower()] += 1

    return results, summary


# Run
results, summary = process_requests(requests)

# Output
print("Processed Requests:")
for r in results:
    print(r)

print("\nSummary:")
print(summary)
