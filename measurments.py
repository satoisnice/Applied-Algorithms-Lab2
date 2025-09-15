import time
import random
import statistics

# Microsecond = 10^-6 seconds

def write_to_txt(results, filename="results.txt"):
    with open(filename, "w") as file:
        for val in results:
            file.write(f"{val}\n")

def time_manip_list(data: list, option: str, index: int, unit=1):
    """
    data (list): list of data
    option (str): list manipulation option. Either "add" or "remove"
    index (int): index pos of where to manip list
    unit (str): what to multiply seconds by either "ms", "micro" or "nano"
    """
    match unit:
        case "ms":
            multiplier = 1000
        case "micro":
            multiplier = 1e6
        case "nano":
            multiplier = 1e9
        case _:
            raise ValueError("WRONG YOU ENTEREDE THE WRONG UNIT WE ONLY ACCEPT:\nms\nmicro\nnano")

    rand_int = random.randint(0,100)

    if option == "add":
        start_time = time.perf_counter()
        data.insert(index, rand_int)
        end_time = time.perf_counter()
        return ((end_time - start_time) * multiplier)
    
    elif option == "remove":
        start_time = time.perf_counter()
        data.pop(index)
        end_time = time.perf_counter()
        return ((end_time - start_time) * multiplier)

    else:
        raise (ValueError("You or I messed up big time"))

def run_trials_and_get_statistics(test, num_trials=1000):
    deltas = [] 
    for i in range(num_trials):
        delta = test()
        deltas.append(delta)
    
    return statistics.mean(deltas)

def binary_search(needle, data: list):
    start = 0
    end = len(data) -1
    while start <= end:
        middle_index = (start + end) // 2
        middle_value = data[middle_index]

        if middle_value == needle:
            return True, middle_index
        
        elif middle_value > needle:
            end = middle_index - 1
        
        elif middle_value < needle:
            start = middle_index + 1
            
    return None

def generate_data(amount):
    """
    Generates an array of random numbers from 0-100
    seems pointless as of test 3

    Variables:
    amount: the number of random numbers, aka length of the list
    """
    return [random.randint(0,100) for i in range(amount)]


def test_1():
    data = generate_data(10)
    return time_manip_list(data, "add", 0, "micro")

def test_2():
    data = generate_data(1000000)
    return time_manip_list(data, "add", 0, "micro")

def test_3():
    data = generate_data(10)
    return time_manip_list(data, "add", -1, "micro")

def test_4():
    data = generate_data(1000000)
    return time_manip_list(data, "add", -1, "micro")

def test_5():
    data = generate_data(10)
    return time_manip_list(data, "remove", 0, "micro")

def test_6():
    data = generate_data(1000000)
    return time_manip_list(data, "remove", 0, "micro")

def test_7():
    data = generate_data(10)
    return time_manip_list(data, "remove", -1, "micro")

def test_8():
    data = generate_data(1000000)
    return time_manip_list(data, "remove", -1, "micro")

def generate_data_v2(amount, present: bool, val = None):
    if present:
        amount -= 1
        data = generate_data(amount)
        data.insert(random.randrange(amount), val)
        return data, val
    else:
        data = generate_data(amount)
        val = 101
        return data, val

def time_search(data, needle, inside: bool):
    start_time = time.perf_counter()
    found = needle in data
    end_time = time.perf_counter()
    if inside and found or (not inside and not found):
        return ((end_time - start_time)* 1e6)
    else:
        return ((end_time - start_time)*1e6)

def test_9(needle: int):
    data = generate_data_v2(10, True, needle)
    return time_search(data, needle, True)

def test_10(needle: int):
    data = generate_data_v2(1000000, True, needle)
    return time_search(data, needle, True)

def test_11():
    data, needle = generate_data_v2(10, False)
    return time_search(data, needle, False)

def test_12():
    data, needle = generate_data_v2(1000000, False)
    return time_search(data, needle, False)

def create_dict_data(amount, needle = None):
    dict = {}
    if needle != None:
        for i in range(amount-1):
            dict[random.randint(0,100)] = None
        dict[needle] = None
    
    else:
        for i in range(amount-1):
            dict[random.randint(0,100)] = None

    return dict        

def test_13(needle: int):
    dict = create_dict_data(10, needle)
    start_time = time.perf_counter()
    if needle in dict:
        end_time = time.perf_counter()
        return ((end_time-start_time)*1e6)

def test_14(needle: int):
    dict = create_dict_data(1000000, needle)
    start_time = time.perf_counter()
    if needle in dict:
        end_time = time.perf_counter()
        return ((end_time-start_time)*1e6)

def test_15(needle: int): #errors
    dict = create_dict_data(10)
    start_time = time.perf_counter()
    _ =  needle not in dict
    end_time = time.perf_counter()
    return ((end_time-start_time)*1e6)
    
def test_16(needle: int): #errors
    dict = create_dict_data(1000000)
    start_time = time.perf_counter()
    _ = needle not in dict
    end_time = time.perf_counter()
    return ((end_time-start_time)*1e6)


def run_all_tests(val=4):
    results = []

    results.append(run_trials_and_get_statistics(test_1, 1000))
    results.append(run_trials_and_get_statistics(test_2, 1))
    results.append(run_trials_and_get_statistics(test_3, 1000))
    results.append(run_trials_and_get_statistics(test_4, 1))
    results.append(run_trials_and_get_statistics(test_5, 1000))
    results.append(run_trials_and_get_statistics(test_6, 1))
    results.append(run_trials_and_get_statistics(test_7, 1000))
    results.append(run_trials_and_get_statistics(test_8, 1))
    results.append(run_trials_and_get_statistics(lambda: test_9(val), 1))
    results.append(run_trials_and_get_statistics(lambda: test_10(val), 1))
    results.append(run_trials_and_get_statistics(test_11, 1000))
    results.append(run_trials_and_get_statistics(test_12, 1))
    results.append(run_trials_and_get_statistics(lambda: test_13(val), 1000))
    results.append(run_trials_and_get_statistics(lambda: test_14(val), 1))
    results.append(run_trials_and_get_statistics(lambda: test_15(val), 1000))
    results.append(run_trials_and_get_statistics(lambda: test_16(val), 1))

    return results


if __name__ == "__main__":
    # print(1, run_trials_and_get_statistics(test_1, 1000))
    # print(2, run_trials_and_get_statistics(test_2, 1))
    # print(3, run_trials_and_get_statistics(test_3, 1000))
    # print(4, run_trials_and_get_statistics(test_4, 1))
    # print(5, run_trials_and_get_statistics(test_5, 1000))
    # print(6, run_trials_and_get_statistics(test_6, 1))
    # print(7, run_trials_and_get_statistics(test_7, 1000))
    # print(8, run_trials_and_get_statistics(test_8, 1))
    # print(9, run_trials_and_get_statistics(lambda: test_9(4), 1))
    # print(10, run_trials_and_get_statistics(lambda: test_10(4), 1))
    # print(11, run_trials_and_get_statistics(test_11, 1000))
    # print(12, run_trials_and_get_statistics(test_12, 1))
    # print(13, run_trials_and_get_statistics(lambda: test_13(4), 1000))
    # print(14, run_trials_and_get_statistics(lambda: test_14(4), 1))
    # print(15, run_trials_and_get_statistics(lambda: test_15(4), 1000))
    # print(16, run_trials_and_get_statistics(lambda: test_16(4), 1))
    # print(run_trials_and_get_statistics(test_(4), 1000))

    results = run_all_tests(4)
    for i, res in enumerate(results, start=1):
        print(i, res)

    write_to_txt(results, "./lab2_results.txt")
