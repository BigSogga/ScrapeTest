import requests
import json


def get_composers():
    index = 0
    while True:
        original_api_link = requests.get(f'https://imslp.org/imslpscripts/API.ISCR.php?account=worklist/disclaimer=accepted/sort=id/type=1/start={index}/retformat=json')
        data = json.loads(original_api_link.content)

        for key, value in data.items():
            if key != 'metadata':
                yield value
        more_data = value['moreresultsavailable']
        if more_data == False:
            break

        number_retrieved = value['limit']
        index += number_retrieved
    return


if __name__ == '__main__':
    composers = get_composers()
    for composer in composers:
        print(composer)
