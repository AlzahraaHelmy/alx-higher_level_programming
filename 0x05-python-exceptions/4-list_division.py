#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            per = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            per = 0
        except ZeroDivisionError:
            print("division by 0")
            per = 0
        except IndexError:
            print("out of range")
            per = 0
        finally:
            new_list.append(per)
    return new_list
