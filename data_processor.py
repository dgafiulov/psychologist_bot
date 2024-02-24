import texts


def edit_data(data):
    edited = [texts.STANDARD_START]
    data = sorted(data, key=lambda x: x[0])
    for i in data:
        edited.append({
            'role': i[2],
            'content': i[1]
        })

    edited[len(edited) - 1]['content'] = texts.ROLE_CONTROL + edited[len(edited) - 1]['content']

    return edited
