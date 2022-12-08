import time
import logging
logging.basicConfig(level=logging.INFO)

def construct_suffix_tree_using_ukkonen(formatted_string):
    '''
    Responsiblity: Main Method to build Ukkonen
        Based Suffix Tree
    Input: formatted_string = input_string + "$"
    Ouput: Newly Contructed Suffix Tree Based on
        Ukkonen Algorithm
    '''
    # ukkonen_suffix_tree = UkkonenSuffixTree(formatted_string)
    # ukkonen_suffix_tree.construct_suffix_tree()
    return 1

def user_input_flow():
    '''
    Responsiblity: Mainly involved in taking
        user input and then formatting the
        same. Then we will invoke the main
        funcation in order to construct the
        Tree based on Ukkonen Algorithm.
        Post that Traversing the Newly
        Constructed Suffix Tree.
    Input: User Entered Input String
    Output: Constructed Tree Based on
        Ukkonen Algorithm
    '''
    input_string = input("Enter the input string : ")
    formatted_string = input_string + "$"
    logging.info("Your fomatted string will be : {}\n".format(formatted_string))
    logging.info("----------Started Constructing Suffix Tree-------------")
    start_time = time.time()
    ukkonen_suffix_tree = construct_suffix_tree_using_ukkonen(formatted_string)
    print(ukkonen_suffix_tree)
    end_time = time.time()
    logging.info("----------Suffix Tree Construction Completed-------------")
    logging.info("Construction of Suffix Tree using Ukkonen Algorithm took around : {} seconds".format(end_time - start_time))
    logging.info("----------Traversing the Newly Constructed Suffix Tree-------------")
    # ukkonen_suffix_tree.traverse_tree()

user_input_flow()
'''
Responsiblilty: Main Method to invoke
    the entire process.
'''