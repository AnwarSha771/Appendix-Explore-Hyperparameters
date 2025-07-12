# List of words with their likelihood of being the next word, sorted by likelihood.
words_and_likelihoods_of_being_next_sorted = [
    ('apple', 0.4),
    ('dragonfruit', 0.2),
    ('marita', 0.1)
]
def get_next_word_top_p(words_sorted_by_likelihood_of_being_next, p):
    # Initialize the cumulative probability.
    cumulative = 0
    # List to hold words and probabilities up to the cumulative probability p.
    words_available_to_be_next = []
    # Add words and their probabilities to the list until the cumulative probability reaches p.
    for word, likelihood in words_sorted_by_likelihood_of_being_next:
        cumulative += likelihood
        words_available_to_be_next.append((word, likelihood))
        if cumulative >= p:
            break
    # Separate the words and their probabilities.
    words, probabilities = zip(*words_available_to_be_next)
    # Choose one word based on the probabilities as weights.
    return random.choices(words, weights=probabilities, k=1)[0]
top_ps = [0.1, 0.6, 1.0]

for top_p in top_ps:
    print(f'Setting top_p to {top_p}.')
    for _ in range(10):
        next_word = get_next_word_top_p(words_and_likelihoods_of_being_next_sorted, top_p)
        print(next_word)
    print()
