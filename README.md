# Access Request Approval Engine

A Python script that processes employee access requests and determines whether each should be **Approved**, **Rejected**, or **Invalid** based on predefined role-access rules.

---

## How to Run

### Prerequisites
- Python 3.6 or above
- No external libraries required (uses only Python built-ins)

### Steps

1. Clone or download the script file:
   ```
   access_approval.py
   ```

2. Run it directly using Python:
   ```bash
   python access_approval.py
   ```

3. Expected output:

   ```
   Processed Requests:
   {'user': 'Asha', 'role': 'Engineer', 'access': 'GitHub', 'status': 'Approved'}
   {'user': 'Ravi', 'role': 'HR', 'access': 'Jira', 'status': 'Approved'}
   {'user': 'Neha', 'role': 'Engineer', 'access': 'Slack', 'status': 'Approved'}
   {'user': 'Kiran', 'role': 'Finance', 'access': 'GitHub', 'status': 'Rejected'}
   {'user': 'Arjun', 'role': 'HR', 'access': 'Slack', 'status': 'Rejected'}
   {'user': 'Maya', 'role': 'Engineer', 'access': 'Jira', 'status': 'Rejected'}
   ...

   Summary:
   {'total': ..., 'approved': ..., 'rejected': ..., 'invalid': ...}
   ```

---

## Assumptions

### 1. Validation
- A request is marked **Invalid** if any of the three required fields — `user`, `role`, or `access` — is missing, `None`, an empty string `""`, or an empty list `[]`.
- Whitespace-only strings (e.g., `" "`) inside an access list are also treated as **Invalid** entries for that specific access item.

### 2. Access as a List (Extension Beyond Base Requirements)
- The base problem defines `access` as a single string per request.
- This solution also supports `access` as a **list of strings** to handle real-world scenarios where a user requests multiple tools at once.
- Each access item in the list is evaluated **independently** and produces its own output row with its own status.
- Example: `{"user": "Test", "role": "Engineer", "access": ["GitHub", "Slack", "lll"]}` → produces 3 rows.

### 3. Unknown Roles
- If a role is not one of `Engineer`, `HR`, or `Finance`, the request is marked **Rejected** (not Invalid), since the fields are technically present and valid — the role just has no permissions defined.

### 4. Unknown Platforms
- If the requested platform is not in the known set (`GitHub`, `Slack`, `Jira`), it is marked **Rejected**.
- Known platforms are defined in `ALL_PLATFORMS` and can be extended easily.

### 5. Finance Role
- Finance employees are not permitted any access. Any access request from a Finance role is automatically **Rejected**.

### 6. Summary Counting
- The summary counts **rows**, not original requests. So a single request with 3 access items contributes 3 to the total.
- Invalid requests (missing fields) are counted as 1 entry in the summary.

### 7. No External Dependencies
- The script uses only Python standard features — no pip installs needed.
