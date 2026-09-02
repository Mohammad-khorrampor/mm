def get_info(keys_list, info_dict):
    if not keys_list:
        return info_dict
    
    key = keys_list[0]
    value = input(key + ": ")
    info_dict[key] = value
    print(f"{key}: {value}")
    
    return get_info(keys_list[1:], info_dict)

keys = ["name", "age", "reshte", "city", "uni", "score"]
info = get_info(keys, {})

if int(info["score"]) >= 17:
    print("eali")
elif int(info["score"]) >= 14:
    print("khob")
elif int(info["score"]) >= 10:
    print("gabol")
else:
    print("mardod")