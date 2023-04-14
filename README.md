# crossword_generator
 
This project is an automatic crossword generator, using artificial intelligence and machine learning to select words and clues that match a user-specified theme. The user is asked to input 3 words that belong to a theme of their choosing (e.g., “Ireland”, “France”, and “Italy” could be interpreted as a “Countries of Europe” theme), and their words are then processed in order to generate a much larger list of words that the project thinks is semantically and thematically similar to the user-inputted words. Words are chosen based on their similarity to the user-inputted words and whether or not they fit in the current crossword grid, interleaved with the rest of the words. When this is done, a fully completed crossword with corresponding clues is presented to the user. The end product is targeted for school teachers supplying their class with a crossword themed on topics covered in class, clubs and college societies that want to provide a fun activity for members, magazines, or for simple recreational use.

### How it works

This project uses the machine learning algorithm "Gensim" and its subsidiary "Word2Vec" to take a pre-trained word model and vectorize the information into numeric representations of words and their similarities to eachother. The similarity between these word vectors directly corresponds to the similarity between the words they represent. Once this is done, an algorithm I wrote from scratch in Python inserts a list of returned similar words into a predetermined grid, based on word length and overlapping words, and generates clues from a specific CSV dataset of clues.

This is the main repository of the project, with the other two repositiories being:
 - https://github.com/shterybai/crossword_generator_website
 - https://github.com/shterybai/CrosswordAPI
