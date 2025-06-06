work_profile = dict(
    name = "John",
    surname = "Doe",
    age = 30,
    city = "New York",
    skills = ["Python", "JavaScript"])

def add_skills(work_profile, new_skill):
    work_profile["skills"].append(new_skill)
    return work_profile

def generate_min_cv(work_profile):
    cv = f"""
    Name: {work_profile['name']} {work_profile['surname']}
    Age: {work_profile['age']}
    City: {work_profile['city']}
    Skills: {', '.join(work_profile['skills'])}
    """
    return print(cv)

def main():
    add_skills(work_profile, "C++")
    add_skills(work_profile, "SQL")
    generate_min_cv(work_profile)

if __name__ == "__main__":
    main()