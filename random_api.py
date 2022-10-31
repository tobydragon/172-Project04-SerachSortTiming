import requests
import json

from user import User


def download_random_user_data(num_data_points):
    """
    gets a number of data points from the random-data-api
    :returns : a list of dictionaries (json objects) containing data about random fake users
    """
    all_responses = []
    print("Downloading:")
    for count in range(num_data_points//100):
        response = requests.get("https://random-data-api.com/api/v2/users?size=100")
        all_responses.append(response.json())
        print("\tround", count+1, "of", num_data_points//100)
    if num_data_points % 100 != 0:
        final_response = requests.get("https://random-data-api.com/api/v2/users?size=" + str(num_data_points % 100))
        all_responses.append(final_response.json())
    final_list = []
    for response_list in all_responses:
        for user in response_list:
            final_list.append(user)
    return final_list


def create_users_from_json(all_user_json):
    """
    :param all_user_json: a list of dictionaries (json objects) containing data about random fake users
    :return: a list of User objects as defined in user.py
    """
    all_users = []
    for user_json in all_user_json:
        all_users.append(User(user_json))
    return all_users


def download_and_write_our_objects_to_file(num_data_points, filename):
    """
    :param num_data_points: number of random user data you want written to file
    :param filename: the filename to write to
    :post: a file is written with containing a list of User objects as defined in user.py
    """
    data_list = download_random_user_data(num_data_points)
    our_data_list = create_users_from_json(data_list)
    write_data_to_file(our_data_list, filename)


def write_data_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4, default=vars)


def read_users_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    all_users = []
    for user_json in json_data:
        all_users.append(User(user_json))
    return all_users


def download_and_write_raw_data_to_file(num_data_points, filename):
    """
    :param num_data_points: number of random user data you want written to file
    :param filename: the filename to write to
    :post: a file is written with json data directly from the api
    """
    data_list = download_random_user_data(num_data_points)
    write_data_to_file(data_list, filename)


def visual_test():
    users = download_random_user_data(5)
    print(json.dumps(users, indent=4))


if __name__ == "__main__":
    download_and_write_raw_data_to_file(1005, "data/test-theirObjects.json")
    download_and_write_our_objects_to_file(1005, "data/test-ourObjects.json")
    lots_of_objects = read_users_from_file("data/test-ourObjects.json")
    print(len(lots_of_objects))
    print(lots_of_objects[2])
