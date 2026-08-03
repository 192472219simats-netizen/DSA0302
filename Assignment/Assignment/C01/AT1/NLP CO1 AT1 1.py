import re

# Sample Resume
resume = """
Name: HEMANTH REDDY

Email: hemanthreddy@gmail.com
Alternate Email: hemanth.reddy123@outlook.com

Mobile: +91-9876543210

Skills:
Python, SQL, Machine Learning, NLP

Experience: 4 years
"""

# Extract Name
name = re.search(r"Name\s*:\s*([A-Za-z ]+)", resume)
candidate_name = name.group(1) if name else "Not Found"

# Extract Emails
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume)

# Extract Mobile Number
mobile = re.findall(r"(?:\+91[- ]?)?[6-9]\d{9}", resume)

# Technical Skills
skill_list = ["Python", "Java", "SQL", "Machine Learning", "NLP"]

skills_found = []

for skill in skill_list:
    if re.search(r"\b" + re.escape(skill) + r"\b", resume, re.IGNORECASE):
        skills_found.append(skill)

# Extract Experience
experience = re.search(r"(\d+)\s+years?", resume, re.IGNORECASE)

exp_years = int(experience.group(1)) if experience else 0

# Structured Summary
print("========== Candidate Profile ==========")
print("Name :", candidate_name)
print("Emails :", emails)
print("Mobile :", mobile)
print("Skills :", skills_found)
print("Experience :", exp_years, "Years")

# Eligibility Check
print("\n========== Eligibility ==========")

if exp_years >= 2 and "Python" in skills_found:
    print(candidate_name, "is ELIGIBLE for shortlisting.")
else:
    print(candidate_name, "is NOT ELIGIBLE.")