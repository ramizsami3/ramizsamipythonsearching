from collections import Counter
import sys

def frequency_calculation(original_string_list):
    # Combine all strings in the list into a single string
    combined_string = ''.join(original_string_list)
    # Use Counter to count the frequency of each character in the combined string
    frequency_dictionary = dict(Counter(combined_string))
    return frequency_dictionary

def sort_by_frequency(original_string_list, frequency_dictionary):
    # Sort characters primarily by frequency (descending) and then alphabetically
    sorted_characters = sorted(frequency_dictionary.keys(), key=lambda x: (-frequency_dictionary[x], x))
    # Build a sorted string based on the sorted characters and their frequencies
    sorted_string = ''.join(char * frequency_dictionary[char] for char in sorted_characters)
    return sorted_string

def remove_duplicates(sorted_string):
    # Initialize an empty set to keep track of seen characters
    seen = set()
    # Build a string with duplicates removed, preserving the order of first occurrence
    unique_sorted_string = ''.join(seen.add(char) or char for char in sorted_string if char not in seen)
    return unique_sorted_string

def main():
    # Check if at least one string is provided as input
    if len(sys.argv) < 2:
        print("Error: Please enter the list of strings separated by spaces.")
        return
    
    try:
        # Collect the list of strings from command line arguments
        original_string_list = sys.argv[1:]
        
        # Validate that all elements in the list are strings
        if not all(isinstance(s, str) for s in original_string_list):
            raise ValueError("All elements must be strings.")
        
        # Print the original list of strings
        print(f"Original String List: {original_string_list}")
        
        # Calculate the frequency of each character in the list
        frequency_dictionary = frequency_calculation(original_string_list)
        # Sort the characters by frequency and then alphabetically
        sorted_string = sort_by_frequency(original_string_list, frequency_dictionary)
        
        # Print the sorted string with duplicates
        print(f"Sorted String by Frequency (with Duplicates): {sorted_string}")
        
        # Remove duplicates from the sorted string
        final_string = remove_duplicates(sorted_string)
        
        # Print the final string with duplicates removed
        print(f"String with Duplicates Removed: {final_string}")
        
    except ValueError as e:
        # Handle any invalid input errors
        print(f"Invalid input: {e}")
        print("Please provide a list of strings.")

# Entry point of the script
if __name__ == "__main__":
    main()
