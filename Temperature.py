# List of words with their likelihood of being the next word, sorted by likelihood.
words_and_likelihoods_of_being_next_sorted = [
    ('apple', 0.4),
    ('dragonfruit', 0.2),
    ('marita', 0.1)
def apply_temperature(probabilities, temperature):
    # Ensure temperature is within the valid range for your model
    if temperature <= 0 or temperature > 1:
        raise ValueError("Temperature must be greater than 0 and less than or equal to 1")
    # Apply temperature to probabilities
    adjusted_probabilities = [pow(p, 1 / temperature) for p in probabilities]
    return adjusted_probabilities
def get_next_word_temperature(words_sorted_by_likelihood_of_being_next, temperature):
    # Separate the words and their original probabilities.
    words, probabilities = zip(*words_sorted_by_likelihood_of_being_next)
    # Adjust the probabilities by applying temperature.
    adjusted_probabilities = apply_temperature(probabilities, temperature)
    # Choose one word based on the adjusted probabilities as weights.
    return random.choices(words, weights=adjusted_probabilities, k=1)[0]
temperatures = [0.01, 0.5, 1.0]

for temperature in temperatures:
    print(f'Setting temperature to {temperature}.')
    for _ in range(10):
        next_word = get_next_word_temperature(words_and_likelihoods_of_being_next_sorted, temperature)
        print(next_word)
    print()
