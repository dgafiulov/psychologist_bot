import texts


def edit_data(data):
    edited = [texts.STANDARD_START]
    data = sorted(data, key=lambda x: x[0])
    for i in data:
        edited.append({
            'role': i[2],
            'content': i[1]
        })

    return edited
