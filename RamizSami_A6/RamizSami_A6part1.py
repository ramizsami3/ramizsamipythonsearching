import sys

def separate_numbers(original):
    #Separate the original list into non-negative and negative lists
    # List comprehension to filter non-negative numbers
    non_negatives = [num for num in original if num >= 0]
    # List comprehension to filter negative numbers
    negatives = [num for num in original if num < 0]
    return non_negatives, negatives

def bubble_sort(alist, ascending=True):
    #Sort the list using the bubble sort algorithm
    n = len(alist)
    # Outer loop for each element in the list
    for i in range(n):
        # Inner loop for comparing adjacent elements
        for j in range(0, n-i-1):
            # If ascending is True, check if current element is greater than next
            # If ascending is False, check if current element is less than next
            if (ascending and alist[j] >alist[j+1]) or (not ascending and alist[j] <alist[j+1]):
                # Swap the elements if they are in the wrong order
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist

def main():
    # Ensure the correct usage of command-line arguments
    if len(sys.argv) < 2:
        # Print error message if no arguments are provided
        print("Error: Please enter the list of integers separated by spaces.")
        return
    
    # Convert command-line arguments to integers for thealist
    try:
        original = list(map(int, sys.argv[1:]))
    except ValueError:
        # Print error message if the arguments are not valid integer
        print("Error: Please provide a valid list of integers separated by spaces.")
        return

    # Print the original list
    print("Original list:", original)

    # Separate the original list into non-negative and negative lists
    non_negatives, negatives = separate_numbers(original)

    # Sort the non-negative list in ascending order
    sorted_non_negatives = bubble_sort(non_negatives, ascending=True)
    # Sort the negative list in descending order
    sorted_negatives = bubble_sort(negatives, ascending=False)

    # Combine the sorted lists
    sorted_list = sorted_non_negatives + sorted_negatives

    # Print the sorted list
    print("Sorted list:", sorted_list)

if __name__ == "__main__":
    main()

