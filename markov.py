from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # file_doc = open("green-eggs.txt")
    # file_doc = file_doc.read()
    # same as below
    file_doc = open("green-eggs.txt").read()

    # print file_doc #(checkpoint)
    return file_doc  
    # "This should be a variable that contains your file text as one long string"


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita hi there hi")
        {('hi', 'there'): ['mary', 'juanita', 'hi'], 
        ('there', 'mary'): ['hi'], 
        ('mary', 'hi': ['there']
        ('there', 'juanita'): ['hi']
        ('juanita', 'hi'): ['there']
        }
    """

    chains = {}

    # splits the white spaces and line characters in text_string 
    text_words = text_string.split()
    # print text_string #(checkpoint)

    # for every word in the length of the text_string give us the range
    # minus the last word in the text_string
    for index in range(len(text_words)-2):
        # shortens the range of our list so we don't exceed the key:value pairs
        # print index #(checkpoint)

        # Binds the first index at index[0] in the text_string to key 
        # plus, binds the second index at index[1] to key 
        # to create a tuple of the two windex
        key = (text_words[index], text_words[index + 1])
        # print text_string[index], text_string[index + 1] #(checkpoint)

        # Bind the third index at index[2] in the text_string to the variable new_value (is the value)
        new_value = text_words[index + 2]  
        # print key, new_value   #(checkpoint)

        if key not in chains:
            # add the new_value 'AS THE' value in the chains dictionary
            chains[key] = [new_value]  #also puts the new_value in a list
        else:
            # chains[key] is equal to the value, not the key
            # if the key is IN the chains dictionary, append the new_value 
            chains[key].append(new_value)            

    # print chains #(checkpoint)
    return make_chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    # text = ""

    new_key = chains.keys[], random.choice[chains[key]]
    print new_key

    # return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
