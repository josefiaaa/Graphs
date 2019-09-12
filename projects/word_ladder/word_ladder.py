# Given two words (beginWord and endWord), and a dictionary's word list, return the shortest transformation sequence from beginWord to endWord, such that:

#   - Only one letter can be changed at a time.
#   - Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

### Note:

#   - Return None if there is no such transformation sequence.
#   - All words have the same length.
#   - All words contain only lowercase alphabetic characters.
#   - You may assume no duplicates in the word list.
#   - You may assume beginWord and endWord are non-empty and are not the same.

# Breakdown
    # - Shortest: BFS
    # - One letter at a time - EDGES
    # - Word list/words - VERTS
    # - Return None - Path Not Found
    # - beginWord & endWord - Starting / Ending Vertices
    # - No duplicates
    # - Same length - Different length words are N/A
    # -         ^^Connected Components ^^
    # - Transformation Sequence - Path

    # If we organize the word list in a graph with words as verices and 
    # #edges between two words that are one letter different, 
    # then  if we do a BFS from the beginning word to the end word, 
    # then the resulting path will be the transformation sequence

f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())

# Instead of converting the world list into a graph
# I'm going to make a helper function that looks up
# What neighbors or edges a word would have in the graph


# Calculate a small part of the graph to find edges and vertices relevant to 
# our current problem
def get_neighbors(word):
    neighbors = []
    word_list = list(word)
    # represents our word as [w, o, r, d]
    for i in range(len(word_list)):
        for letter in list('abcdefghijklmnopqrstuvwxyz'):
            temp_word = list(word_list)
            temp_word[i] = letter
            w = "".join(temp_word) # Join the list version of the world back into a string
            if w != word and w in word_set:
                neighbors.append(w)
    
    return neighbors


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


# Use a BFS variant to find our answer
def find_word_ladder(begin_word, end_word):
    visited = set()
    q = Queue()
    q.enqueue([begin_word])
    while q.size() > 0:
        path = q.dequeue()
        current = path[-1]
        if current not in visited:
            visited.add(current)
            if current == end_word:
                return path
            for new_word in get_neighbors(current):
                new_path = list(path)
                new_path.append(new_word)
                q.enqueue(new_path)


print(find_word_ladder("sail", "boat"))






# from util import Stack, Queue

# class Word_Ladder:
#     def __init__(self):
#         self.words = []

#     def add_word(self, word):
#         """
#         Add a word as a 'vert' of the graph
#         """
#         if word not in self.words:
#         # If the word doesn't exist already
#             self.words[word] = set()
#         else:
#             print("Error: This word has already been added!")

#     def check_letter_difference(self, word1, word2):
#         count = 0
#         length = len(word1)

#         for i in range(length): 
#             # Going through all letters in the first word
#             if word1[i] != word2[i]:
#                 # If the letter(i) of the word is different, the count is increased
#                 count += 1
#             elif count == 1:
#                 # If the count ends up being a letter difference of 1, True is returned
#                 return True
#             elif count > 1:
#                 # If more than one letter is different, function breaks
#                 break
#         return False

#     def shortest_ladder(self, starting_word, destination_word):

#         q = Queue()
#         visited = set()
#         q.enqueue([starting_word])

#         while q.size() > 0:
#             path = q.dequeue()
#             current = path[-1]

#             if current not in visited:
#                 if current == destination_word:
#                     return path
#                 visited.add(current)

#                 for next_letter in self.words[current]:
#                     path_copy = list(path)
#                     path_copy.append(next_letter)
#                     q.enqueue(path_copy)

#         return None



# if __name__ == '__main__':
#     graph = Word_Ladder()

