import re, sys

def is_palindrome_recursive(sequence_to_test,beginning=0,end=-1):
    if len(sequence_to_test) <= beginning - end:
        return True
    elif sequence_to_test[beginning] == sequence_to_test[end]:
        return is_palindrome_recursive(sequence_to_test,beginning+1,end-1)
    else:
        return False

def is_palindrome_iterative(sequence_to_test):
    for index in range(len(sequence_to_test)//2):
        if sequence_to_test[index] != sequence_to_test[-1-index]:
            return  False
    return True

def is_palindrome(sequence_to_test,recurse = True,rules = "alpha_nocase"):
    if rules =="alpha_nocase":
        sequence_to_test = remove_non_alphas(sequence_to_test).lower()
    if recurse:
        return is_palindrome_recursive(sequence_to_test)
    else:
        return is_palindrome_iterative(sequence_to_test)

def remove_non_alphas(mixed_string):
    return re.sub(r'[^A-Za-z]','',mixed_string)

def find_palindromes(sequence_of_words):
    palindromes = []
    for length in range(1,1+len(sequence_of_words)):
        for start in range(0,len(sequence_of_words)-length+1):
            test_sequence = sequence_of_words[start:start+length]
            joined_sequence = ''.join(test_sequence)
            if is_palindrome(joined_sequence):
                palindromes.append(' '.join(test_sequence))
    return palindromes

def get_word_list(sentence):
    fixed_sentence = re.sub(r'[^A-Za-z ]','',sentence).lower()
    words = fixed_sentence.split()
    return words

def work_from_prompt():
            input_string = input("> ")
            if is_palindrome(input_string):
                print("It's a palindrome.")
            else:
                print("It's NOT a palindrome.")
                palindromes = find_palindromes(get_word_list(input_string))
                if len(palindromes) > 0:
                    print("But these are:")
                    for palindrome in palindromes:
                        print(palindrome)

def work_from_file(filename):
    with open(filename,'r') as in_file:
        for each_line in in_file:
            if is_palindrome(each_line):
                print(each_line+"That's a palindrome.\n")
            else:
                print(each_line+"That's NOT a palindrome.\n")

def main():
    if len(sys.argv) == 1:
        work_from_prompt()
    elif len(sys.argv) == 2:
        work_from_file(sys.argv[1])
    else:
        raise ValueError("Expected 1 argument got {}.".format(len(sys.argv)-1))

if __name__ == '__main__':
    main()
