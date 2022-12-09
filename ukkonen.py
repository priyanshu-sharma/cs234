import time
import logging

logging.basicConfig(level=logging.INFO)
from operator import attrgetter as at

leaf_end_value = -1


class UkkonenSuffixTree:
    def __init__(self, formatted_string):
        """
        Responsiblity: Main Method to build Ukkonen
            Based Suffix Tree
        Input: formatted_string = input_string + "$"
        Ouput: Newly Contructed Suffix Tree Based on
            Ukkonen Algorithm
        """
        self.formatted_string = formatted_string
        self.size = -1
        self.root_node = None
        self.latest_node = None
        self.act_node = None
        self.act_edge = -1
        self.act_len = 0
        self.remainder = 0
        self.root_end = None
        self.split_end = None
    
    def check_for_rule_three_extension(self, index):
        if ((self.act_node == self.root_node) and (self.act_len > 0)):
            self.act_len -= 1
            self.act_edge = index - self.remainder + 1
        elif (self.act_node != self.root_node):
            self.act_node = self.act_node.s_link

    def initializing_the_value_and_add_root_node(self):
        self.size = len(self.formatted_string)
        self.root_end = -1
        new_root_node = UkkonenSuffixNode(False)
        new_root_node.s_link = self.root_node
        new_root_node.starting_value = -1
        new_root_node.ending_value = self.root_end
        new_root_node.s_index = -1
        self.root_node = new_root_node
        self.act_node = self.root_node

    def iterate_char_by_char(self):
        for index in range(self.size):
            global leaf_end_value
            leaf_end_value = index
            self.remainder += 1
            self.latest_node = None
            self.insert_char_in_suffix_tree(index)

    def traverse_tree(self):
        """
        Responsiblity: To output the newly
            constructed suffix tree based on
            the values given by tree_traversal()
            function
        Input: UkkonenSuffixTree Class Funcation
        Ouput: Print the children of the tree in
            Depth First Search Way. One can also
            replicate the same for Breadth First
            Search way.
        """
        for child in self.tree_traversal(self.root_node):
            print(child)

    def set_act_edge_to_current_index(self, index):
        if (self.act_len == 0):
            self.act_edge = index

    def construct_suffix_tree(self):
        """
        Responsiblity: Main Method to build Ukkonen
            Based Suffix Tree
        Input: formatted_string = input_string + "$"
        Ouput: Newly Contructed Suffix Tree Based on
            Ukkonen Algorithm
        """
        self.initializing_the_value_and_add_root_node()
        self.iterate_char_by_char()

    def tree_traversal(self, current_node):
        """
        Responsiblity: Starting from root_node
            it will first fetch all the child_no
            de of root_node and then for each
            child_node of root_node it will again
            fetch their all the child_nodes.
        Input: UkkonenSuffixTree Class Funcation
            + Accept the Current Node. Initially
            it will be root node.
        Ouput: Print the child_node of each node
            in Depth-First Search Way.
        """
        starting_value, ending_value = (
            current_node.starting_value,
            current_node.ending_value,
        )
        yield self.formatted_string[starting_value : ending_value + 1]

        for child_node in current_node.children_node.values():
            if child_node:
                yield from self.tree_traversal(child_node)

    def insert_char_in_suffix_tree(self, index):
        while(self.remainder > 0):
            self.set_act_edge_to_current_index(index)
            self.check_for_rule_three_extension(index)

class UkkonenSuffixNode:
    def __init__(self, leaf_node):
        self.children_node = {}
        self.leaf_node = leaf_node
        self.s_index = None
        self.starting_value = None
        self.ending_value = None
        self.s_link = None

    def __eq__(self, ukkonen_suffix_node):
        atg = at("starting_value", "ending_value", "s_index")
        if atg(self) == atg(ukkonen_suffix_node):
            return True
        return False

    def __ne__(self, ukkonen_suffix_node):
        atg = at("starting_value", "ending_value", "s_index")
        if atg(self) != atg(ukkonen_suffix_node):
            return True
        return False

    def __getattribute__(self, attribute_name):
        if attribute_name == "ending_value":
            if self.leaf_node:
                return leaf_end_value
        return super(UkkonenSuffixNode, self).__getattribute__(attribute_name)


def construct_suffix_tree_using_ukkonen(formatted_string):
    """
    Responsiblity: Main Method to build Ukkonen
        Based Suffix Tree
    Input: formatted_string = input_string + "$"
    Ouput: Newly Contructed Suffix Tree Based on
        Ukkonen Algorithm
    """
    ukkonen_suffix_tree = UkkonenSuffixTree(formatted_string)
    ukkonen_suffix_tree.construct_suffix_tree()
    return ukkonen_suffix_tree


def user_input_flow():
    """
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
    """
    input_string = input("Enter the input string : ")
    formatted_string = input_string + "$"
    logging.info("Your fomatted string will be : {}\n".format(formatted_string))
    logging.info("----------Started Constructing Suffix Tree-------------")
    start_time = time.time()
    ukkonen_suffix_tree = construct_suffix_tree_using_ukkonen(formatted_string)
    print(ukkonen_suffix_tree)
    end_time = time.time()
    logging.info("----------Suffix Tree Construction Completed-------------")
    logging.info(
        "Construction of Suffix Tree using Ukkonen Algorithm took around : {} seconds".format(
            end_time - start_time
        )
    )
    logging.info("----------Traversing the Newly Constructed Suffix Tree-------------")
    ukkonen_suffix_tree.traverse_tree()


user_input_flow()
"""
Responsiblilty: Main Method to invoke
    the entire process.
"""
