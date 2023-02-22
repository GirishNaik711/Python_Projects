import string
import random
from graph import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path, "r") as f:
        text = f.read()
        text = ' '.join(text.split())
        text = text.lower
        text = text.translate(str.maketrans('','',string.punctuation))
    words = text.split()    

    return words 

def make_graph(words):
    g = Graph()
    previous_word = None

    for word in words:
        word_vertex = g.get_vertex(word)
        if previous_word:
            g.add_vertex(word_vertex)
        previous_word = word_vertex
    g.generate_probability_mappings()

    return g

def composition(g, words, length= 50):
    compostion = []
    word = g.get_vertex(random.choices(words))

    for _ in range(length):
        composition.append(word.value)
        g.get_next_word(word)

    return compostion

def main():
    words = get_words_from_text("text_path")
    g = make_graph(words)
    compose = composition(g, get_words_from_text, 100)

    return ' '.join(compose)

if __name__ == '__main__':
    print(main())   

