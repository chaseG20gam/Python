
def manage_information(personal_data=("Ana", 30, "Madrid")):
   
    name, age, location = personal_data
    birth = 2025 - age
    modified_data = (name, birth, location)
    name, birth, location = modified_data

    return print(f"Tupla original: {personal_data}\n" f"Tupla modificada: {modified_data}\n")

if __name__ == "__main__":
    manage_information()
