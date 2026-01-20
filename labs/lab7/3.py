personnel = [
    {"name": "Dr. Klein", "clearance": 2},
    {"name": "Agent Brooks", "clearance": 4},
    {"name": "Technician Reed", "clearance": 1}
]
a = list(map(lambda x: {
    "category": (
        "Restricted" if x["clearance"] == 1 else
        "Confidential" if 2 <= x["clearance"] <= 3 else
        "Top Secret"
    )
}, personnel))
print(a)