def access_info(key, place):
    try:
        with open(place, "r") as f:
            if f.read() == key:
                return
    except:
        return 0

def destroy_info(place):
    try:
        with open(place, "w") as f:
            f.write("file.txt")
    except:
        return "unable to delete"


def decrypt(cypher, input_key, true_key):
    if input_key == true_key:
        return access_info(cypher)
    else:
        destroy_info(cypher)
        return 0