'''user_list = [
    "pass,FAIL, error, PASS,skipped"
]
user_list_new = user_list[0].split(", ")


contador_pass = 0
contador_fail = 0
contador_skipped = 0
contador_error = 0

def validate_user_list(user_list_new, contador_pass, contador_fail, contador_skipped, contador_error):
    for valor_list in user_list_new:
        if valor_list == "pass":
            print("pass")
            contador_pass += 1
        elif valor_list == "fail":
            print("fail")       
            contador_fail += 1
        elif valor_list == "skipped":
            print("skipped")
            contador_skipped += 1
        elif valor_list == "error":
            print("error")
            contador_error += 1
        else:
            print("Invalid value:", valor_list)
print('user list:', user_list_new)
print("Validating user list...")
print("Pass count:", contador_pass)
print("Fail count:", contador_fail)
print("Skipped count:", contador_skipped)
print("Error count:", contador_error)
'''

user_list = [
    "pass,FAIL, error, PASS,skipped"
]

user_list_new = user_list[0].split(",")

def validate_user_list(user_list_new):
    contador_pass = 0
    contador_fail = 0
    contador_skipped = 0
    contador_error = 0
    contador_invalid = 0

    for valor_list in user_list_new:
        valor_list = valor_list.strip().lower()

        if valor_list == "pass":
            contador_pass += 1

        elif valor_list == "fail":
            contador_fail += 1

        elif valor_list == "skipped":
            contador_skipped += 1

        elif valor_list == "error":
            contador_error += 1

        else:
            print("Invalid value:", valor_list)
            contador_invalid += 1

    return (
        contador_pass,
        contador_fail,
        contador_skipped,
        contador_error,
        contador_invalid
    )


print("User list:", user_list_new)
print("Validating user list...")

(
    contador_pass,
    contador_fail,
    contador_skipped,
    contador_error,
    contador_invalid
) = validate_user_list(user_list_new)

print("Pass count:", contador_pass)
print("Fail count:", contador_fail)
print("Skipped count:", contador_skipped)
print("Error count:", contador_error)
print("Invalid count:", contador_invalid)
print("Total tests:", len(user_list_new))