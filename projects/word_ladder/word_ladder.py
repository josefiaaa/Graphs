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

from util import Stack, Queue

class Word_Ladder:
    def __init__(self):
        self.words = []

    def add_word(self, word):
        """
        Add a word as a 'vert' of the graph
        """
        if word not in self.words:
        # If the word doesn't exist already
            self.words[word] = set()
        else:
            print("Error: This word has already been added!")

    def check_letter_difference(self, word1, word2):
        count = 0
        length = len(word1)

        for i in range(length): 
            # Going through all letters in the first word
            if word1[i] != word2[i]:
                # If the letter(i) of the word is different, the count is increased
                count += 1
            elif count == 1:
                # If the count ends up being a letter difference of 1, True is returned
                return True
            elif count > 1:
                # If more than one letter is different, function breaks
                break
        return False

    def shortest_ladder(self, starting_word, destination_word):

        q = Queue()
        visited = set()
        q.enqueue([starting_word])

        while q.size() > 0:
            path = q.dequeue()
            current = path[-1]

            if current not in visited:
                if current == destination_word:
                    return path
                visited.add(current)

                for next_letter in self.words[current]:
                    path_copy = list(path)
                    path_copy.append(next_letter)
                    q.enqueue(path_copy)

        return None



if __name__ == '__main__':
    graph = Word_Ladder()

