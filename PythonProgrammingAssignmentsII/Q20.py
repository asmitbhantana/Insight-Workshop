"""
20. Write a Python class to find the three elements that sum to zero
from a list of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
"""
if __name__ == '__main__':
    usr_list = [-25, -10, -7, -3, 2, 4, 8, 10]
    required_result = 0
    usr_list.sort()
    required_result_num_list = []
    for i in range(len(usr_list)):
        if usr_list[i] >= required_result:
            break
        for j in range(i + 1, len(usr_list)):
            if usr_list[i]+usr_list[j] >= required_result:
                break
            for k in range(j + 1, len(usr_list)):
                c_sum = usr_list[i] + usr_list[j] + usr_list[k]
                if c_sum > required_result:
                    break
                elif c_sum == required_result:
                    required_result_num_list.append([usr_list[i], usr_list[j], usr_list[k]])
                    break

    print(required_result_num_list)