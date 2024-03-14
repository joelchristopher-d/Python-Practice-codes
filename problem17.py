

# Hackerrank assesment


def reverse_words_order_and_swap_cases(sentence):

    temp = sentence.split()
    
    reverse = temp[::-1]
    final = " ".join(reverse)
    return final.swapcase()

if __name__ == '__main__':
    sentence = "BarKs dOGs"
    print(reverse_words_order_and_swap_cases(sentence))


