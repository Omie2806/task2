import spacy
from wordfreq import word_frequency

nlp = spacy.load("en_core_web_sm")

text = "Project X is an exclusive elub at Veermata Jijabai Technological Institute, Mumbai, mcant to 5erve as a healthy environment for 5tudents to learn from each other and grow together.Through the guidance of their mcntors these 5tudents are able to complete daunting tasks in a relatively short time frame, gaining significant exposure and knowledge in their domain of choice."


def is_valid(word):
    return word_frequency(word.lower(), 'en') > 0

def try_corrections(word):
    if is_valid(word):
        return word

    if 'c' in word:
        alt = word.replace('c', 'e')
        if is_valid(alt):
            return alt

    if 'e' in word:
        alt = word.replace('e', 'c', 1)
        if is_valid(alt):
            return alt

    if '5' in word:
        alt = word.replace('5', 's')
        if is_valid(alt):
            return alt

    return word

corrected_words = [try_corrections(w) for w in text.split()]

if corrected_words and corrected_words[0].lower() == "however":
    corrected_words[0] += ','

corrected_text = " ".join(corrected_words)

if not corrected_text.endswith(('.', '!', '?')):
    corrected_text += '.'

doc = nlp(corrected_text)

proper_noun_phrases = []
phrase = []

for token in doc:
    if token.pos_ == "PROPN":
        phrase.append(token.text)
    elif phrase:
        proper_noun_phrases.append(" ".join(phrase))
        phrase = []
if phrase:
    proper_noun_phrases.append(" ".join(phrase))

print(corrected_text)
print(proper_noun_phrases)