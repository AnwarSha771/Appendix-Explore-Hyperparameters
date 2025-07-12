# List of words with their likelihood of being the next word, sorted by likelihood.
words_and_likelihoods_of_being_next_sorted = [
    ('apple', 0.4),
    ('dragonfruit', 0.2),
    ('marita', 0.1)
]
  def get_next_word_combined(words_sorted_by_likelihood_of_being_next, top_k, p, temperature):
    # Apply top_k to limit the choices.
    words_available_to_be_next = words_sorted_by_likelihood_of_being_next[:top_k]
    
    # Initialize the cumulative probability.
    cumulative = 0
    # List to hold words and probabilities after applying top_p.
    top_p_words = []
    # Add words to the list based on top_p criteria.
    for word, likelihood in words_available_to_be_next:
        cumulative += likelihood
        top_p_words.append((word, likelihood))
        if cumulative >= p:
            break
            
    # Separate the words and their probabilities after applying top_p.
    words, probabilities = zip(*top_p_words)
    # Adjust the probabilities by applying temperature.
    adjusted_probabilities = apply_temperature(probabilities, temperature)
    
    # Choose one word based on the adjusted probabilities as weights.
    return random.choices(words, weights=adjusted_probabilities, k=1)[0]
  top_ks = [2, 3]
top_ps = [0.6, 1]
temperatures = [0.1, 1]

for top_k in top_ks:
    for top_p in top_ps:
        for temperature in temperatures:
            print(f'Setting top_k to {top_k}, top_p to {top_p}, temperature to {temperature}.')
            for _ in range(10):
                next_word = get_next_word_combined(
                    words_and_likelihoods_of_being_next_sorted, 
                    top_k, 
                    top_p, 
                    temperature
                )
                print(next_word)
            print()
