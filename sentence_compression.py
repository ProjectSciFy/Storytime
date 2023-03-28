from sumy.summarizers.luhn import LuhnSummarizer
import spacy
from spacy import displacy
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')
from nltk.tokenize import TreebankWordTokenizer as twt
from spacy import displacy
from pathlib import Path

text =  "Once upon a time, in a magical forest, there lived a small white mouse named Pip." # "Once upon a time, in a far-off land, there was a castle ruled by a brave and kind princess named Lily. She loved her people and spent her days making sure they were happy and safe."

# text = "Once upon a time, in a magical forest, there lived a small white mouse named Pip. Pip was a curious and adventurous mouse who loved to explore the forest and its many wonders.",
#     "One day, while Pip was scurrying through the forest, she stumbled upon a large black dog named Max. Max was a friendly dog who loved to chase after squirrels and play fetch with his owner.",
#     "At first, Pip was frightened of Max. She had heard stories of dogs chasing and killing mice. But as she watched Max, she noticed something different about him. He didn't seem interested in chasing or hurting her. Instead, he wagged his tail and looked at her with kind eyes.",   
#     "Pip cautiously approached Max, and to her surprise, he welcomed her with a wag of his tail. From that moment on, Pip and Max became the best of friends. They would play together in the forest, with Max always careful not to hurt Pip with his big paws.",
#     "As they explored the forest together, Pip and Max encountered many adventures. They discovered hidden caves, climbed tall trees, and swam in the crystal clear streams. Pip was always amazed at how fearless Max was, and Max loved having Pip by his side to share in his adventures.",
#     "Even though they were different species, Pip and Max had a bond that was unbreakable. They were the best of friends, and nothing could ever come between them.",
#     "And so, Pip and Max continued to explore the magical forest together, living out their days in the purest form of friendship that could ever exist."

#stop_words = ['once', 'upon', 'a','time','lived','name']


stop_words = []
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)


def visualize_pos(text):
    pos_tags = ["PRON", "VERB", "NOUN", "ADJ", "ADP",
                "ADV", "CONJ", "DET", "NUM", "PRT"]
    
    # Tokenize text and pos tag each token
    tokens = twt().tokenize(text)
    tags = nltk.pos_tag(tokens, tagset = "universal")

    # Get start and end index (span) for each token
    span_generator = twt().span_tokenize(text)
    spans = [span for span in span_generator]

    # Create dictionary with start index, end index, 
    # pos_tag for each token
    ents = []
    for tag, span in zip(tags, spans):
        if tag[1] in pos_tags:
            ents.append({"start" : span[0], 
                         "end" : span[1], 
                         "label" : tag[1] })

    doc = {"text" : text, "ents" : ents}

    colors = {"PRON": "blueviolet",
              "VERB": "lightpink",
              "NOUN": "turquoise",
              "ADJ" : "lime",
              "ADP" : "khaki",
              "ADV" : "orange",
              "CONJ" : "cornflowerblue",
              "DET" : "forestgreen",
              "NUM" : "salmon",
              "PRT" : "yellow"}
    
    options = {"ents" : pos_tags, "colors" : colors}
    
    svg = displacy.render(doc, 
                    style = "ent", 
                    options = options, 
                    manual = True,
                   )
    

svg = "abc cde"

visualize_pos(text)

output_path = Path("butterfly2.svg")
output_path.open('w', encoding='utf-8').write(svg)


pos_tags = ["PRON", "VERB", "NOUN", "ADJ", "ADP", "ADV", "CONJ", "DET", "NUM", "PRT"]
colors = {"PRON": "blueviolet",
          "VERB": "lightpink",
          "NOUN": "turquoise",
          "ADJ" : "lime",
          "ADP" : "khaki",
          "ADV" : "orange",
          "CONJ" : "cornflowerblue",
          "DET" : "forestgreen",
          "NUM" : "salmon",
          "PRT" : "yellow"}
options = {"ents": pos_tags, "colors": colors}

svg = displacy.render(doc, 
                style = "ent", options = options)

output_path = Path("butterfly2.svg")
output_path.open('w', encoding='utf-8').write(svg)

nouns = []
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)
    if token.lemma_ not in stop_words and not token.is_stop:
        print(token.text, token.lemma_, token.pos_,[child for child in token.children])

    if (token.lemma_ not in stop_words) and (not token.is_stop) and (str(token.pos_) == "NOUN" or str(token.pos_) == "ADJ" or str(token.pos_) == "VERB" or str(token.pos_) == "ADV"):
        nouns.append(token.lemma_)


out = ""
for token in doc:
    if token.lemma_ in nouns:
        if token.lemma_ not in out:
            out = out + token.lemma_ + " "

out = out + "cartoon"

print(out)