import sys

def separate_numbers(original): #define fucntion seperate_numbers
    
    #Separate the original list into non-negative and negative lists.
    
    #Args: original (list): The original list of integers.
    
    #Returns: tuple: Two lists, one with non-negative numbers and one with negative numbers.
    
    non_negatives = [num for num in original if num >= 0] #define variable non_negatvies
    negatives = [num for num in original if num < 0] #define negatvies
    return non_negatives, negatives #return both

def binary_search_insert_position(alist, number, ascending=True): #define fucntion binary_search_insert_postion
    
    #Find the correct position to insert a number in a sorted list using binary search.
    
    #Args: alist (list): The sorted list where the number should be inserted. number (int): The number to insert. ascending (bool): If True, the list is sorted in ascending order; otherwise, in descending order.
    
    #Returns: int: The index position where the number should be inserted.
    
    low = 0 #set low to 0
    high = len(alist) - 1 #set hgih to len of alist minus 1
    while low <= high: #check if low less or equal to high
        mid = (low + high) // 2 #if so set mid euqal to low plus high
        if (ascending and alist[mid] < number) or (not ascending and alist[mid] > number): 
            low = mid + 1
        else:
            high = mid - 1
    return low

def insertion_sort_binary(alist, ascending=True):
    
    #Sort the list using insertion sort with binary search for finding the insert position.
    
    #Args: alist (list): The list to be sorted. ascending (bool): If True, the list is sorted in ascending order; otherwise, in descending order.
    
    #Returns: list: The sorted list.
    
    sorted_list = [] #creare empty list sorted_list
    for number in alist: #create for loop 
        pos = binary_search_insert_position(sorted_list, number, ascending) #store call to previous fucntion in pos
        sorted_list.insert(pos, number) #insert pos and current loop value 
    return sorted_list #return list

def main(): #define main function 
    # Ensure the correct usage of command-line arguments
    if len(sys.argv) < 2: #check if less than 2
        print("Error: Please enter the list of integers separated by spaces.")
        return
    
    # Convert command-line arguments to integers for the list
    try:
        original = list(map(int, sys.argv[1:]))
    except ValueError:
        print("Error: Please provide a valid list of integers separated by spaces.")
        return

    print("Original list:", original)

    # Separate the original list into non-negative and negative lists
    non_negatives, negatives = separate_numbers(original)

    # Sort the non-negative list in ascending order
    sorted_non_negatives = insertion_sort_binary(non_negatives, ascending=True)
    # Sort the negative list in descending order
    sorted_negatives = insertion_sort_binary(negatives, ascending=False)

    # Combine the sorted lists
    sorted_list = sorted_non_negatives + sorted_negatives

    # Print the sorted list
    print("Sorted list:", sorted_list)

if __name__ == "__main__":
    main()
