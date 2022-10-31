import time
import random_api


def linear_search_for_user(user_list, username_to_find):
    """:returns: the index of a user object with where username_to_find is located, or -1 if not present"""
    pass


def system_sort_by_username(user_list):
    """:post: the user_list is sorted in alphabetical order by username"""
    pass


def my_sort_by_username(user_list):
    """:post: the user_list is sorted in alphabetical order by username"""
    pass


def binary_search_for_user(user_list, username_to_find):
    """:pre: the user_list must be sorted by user_name
        :returns: the index of a user object with where username_to_find is located, or -1 if not present
    """
    return -1


def print_big_o_data(function_to_time, data):
    """
    :param: function_to_time - a function you would like to time, which takes only a single parameter,
        the data to time it on
    :param: data -   a large dataset (length >50,000) that can be used to run your function on
    :post: function_to_time will be run on various subsets of the data, growing in size, and the timing info for each
        run will be printed out
    """
    for i in range(1000, 500000, 10000):
        data_to_test = data[:i]
        total = 0
        start = time.perf_counter()
        function_to_time(data_to_test)
        stop = time.perf_counter()
        total += stop-start
        print(i, stop-start, sep="\t")


def print_comparison_of_linear_search_vs_sort_plus_binary_search():
    """
    :post: print data that will make a graph to show how many times searches must be done to justify running a sort
        and then using binary search
    """
    # get two copies of the same, large, unsorted list of data
    # keep two totals: total time for linear search, total time for sort + binary search
    # sort data and track time, add it to the sort+binsearch total
    # Run a loop: while total linear search time is less than total sort+binsearch time
    #   Search the unsorted data for a value, add that time to linear search time
    #   Search the sorted data for the same value, add that time to sort+binsearch time
    #   print the two data points (number of searches, time for each)
    # When the loop finishes, print the total number of searches
    pass


def check_binary_search_for_user():
    test_data = random_api.read_users_from_file("data/test-ourObjects.json")
    system_sort_by_username(test_data)
    for i in range(len(test_data)):
        answer = binary_search_for_user(test_data, test_data[i].username)
        if test_data[answer].username != test_data[i].username:
            print("failed, reported", answer, "for :", test_data[i].username)
    for username in ["a", "", "b", "something long that shouldn't be found"]:
        answer = binary_search_for_user(test_data, username)
        if answer != -1:
            print("found username when shouldn't:", username, test_data[answer])


def main():
    unsorted_data = random_api.read_users_from_file("data/500000.json")


if __name__ == "__main__":
    main()

