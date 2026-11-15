from linked_list import LinkedList

if __name__ == "__main__":
    employee_ids = LinkedList()

    employee_ids.insert_at_end(10)
    employee_ids.insert_at_end(20)
    employee_ids.insert_at_end(30)

    print("Original employee IDs:")
    employee_ids.display()

    print(f"Sum of IDs: {employee_ids.recursive_sum()}")

    target = 20
    print(f"ID {target} found: {employee_ids.recursive_search(target)}")

    target = 99
    print(f"ID {target} found: {employee_ids.recursive_search(target)}")

    employee_ids.recursive_reverse()
    print("Reversed employee IDs:")
    employee_ids.display()