#!/usr/bin/env python3
"""Add missing word definitions to data.js Lesson 1."""
import re, json

with open("/mnt/d/hermes/deepeng/web/data.js") as f:
    content = f.read()

# Define missing words to add (aligned with NGSL 2809)
missing_defs = {
    "Tom":      {"word": "Tom", "def": "汤姆（人名）", "ipa": "/tɒm/", "eng_def": "a name for a boy"},
    "his":      {"word": "his", "def": "他的", "ipa": "/hɪz/", "eng_def": "belonging to him"},
    "he":       {"word": "he", "def": "他", "ipa": "/hiː/", "eng_def": "the male person previously mentioned"},
    "it":       {"word": "it", "def": "它", "ipa": "/ɪt/", "eng_def": "used to refer to a thing or animal"},
    "is":       {"word": "is", "def": "是", "ipa": "/ɪz/", "eng_def": "third person singular of 'be'"},
    "and":      {"word": "and", "def": "和；并且", "ipa": "/ænd/", "eng_def": "used to connect words or phrases"},
    "bread":    {"word": "bread", "def": "面包", "ipa": "/bred/", "eng_def": "a food made from flour and water"},
    "milk":     {"word": "milk", "def": "牛奶", "ipa": "/mɪlk/", "eng_def": "a white liquid from cows, used as food"},
    "then":     {"word": "then", "def": "然后", "ipa": "/ðen/", "eng_def": "at that time; next"},
    "to":       {"word": "to", "def": "到；去；给", "ipa": "/tuː/", "eng_def": "used to show direction or purpose"},
    "friend":   {"word": "friend", "def": "朋友", "ipa": "/frend/", "eng_def": "a person you like and know well"},
    "Ann":      {"word": "Ann", "def": "安（人名）", "ipa": "/æn/", "eng_def": "a name for a girl"},
    "they":     {"word": "they", "def": "他们；她们；它们", "ipa": "/ðeɪ/", "eng_def": "used to refer to two or more people"},
    "go":       {"word": "go", "def": "去", "ipa": "/ɡəʊ/", "eng_def": "to move or travel somewhere"},
    "together": {"word": "together", "def": "一起", "ipa": "/təˈɡeðə(r)/", "eng_def": "with each other"},
    "like":     {"word": "like", "def": "喜欢", "ipa": "/laɪk/", "eng_def": "to find pleasant or enjoyable"},
    "feel":     {"word": "feel", "def": "感觉", "ipa": "/fiːl/", "eng_def": "to experience an emotion or sensation"},
    "happy":    {"word": "happy", "def": "快乐的；开心的", "ipa": "/ˈhæpi/", "eng_def": "feeling pleasure or contentment"},
    "up":       {"word": "up", "def": "向上；起床", "ipa": "/ʌp/", "eng_def": "towards a higher position"},
}

# Each sentence index → list of word keys to add
add_to_sentences = {
    0: ["Tom", "his"],                      # Tom opens his eyes.
    # opens→open (already in dict), eyes→eye (already in dict)
    1: ["it", "is"],                         # It is morning.
    2: ["he"],                               # He gets up.
    # gets→get, up→up (added)
    3: ["he", "and"],                        # He eats bread and drinks milk.
    # eats→eat, bread→bread, drinks→drink, milk→milk
    4: ["then", "he", "to"],                # Then he walks to school.
    # walks→walk
    5: ["he", "friend", "Ann"],             # He sees his friend Ann.
    # sees→see, his→his
    6: ["they", "go", "to", "together"],    # They go to class together.
    7: ["Tom", "like"],                     # Tom likes school.
    # likes→like
    8: ["he", "feel", "happy"],             # He feels happy.
    # feels→feel
}

# Parse the JS to JSON for manipulation
js_text = content.replace("const LESSONS = ", "", 1).rstrip(";").rstrip()
data = json.loads(js_text)

lesson1 = data[0]
for sent_idx, word_keys in add_to_sentences.items():
    existing_words = {w["word"].lower() for w in lesson1["sentences"][sent_idx]["words"]}
    for key in word_keys:
        if key.lower() not in existing_words:
            lesson1["sentences"][sent_idx]["words"].append(missing_defs[key])

# Write back
output = "const LESSONS = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n"
with open("/mnt/d/hermes/deepeng/web/data.js", "w", encoding="utf-8") as f:
    f.write(output)

# Verify
import re as re2
new_all_words = set()
for s in lesson1["sentences"]:
    text_words = re2.findall(r"[a-zA-Z']+", s["en"])
    for w in text_words:
        new_all_words.add(w.lower())

new_dict_words = set()
for s in lesson1["sentences"]:
    for w in s["words"]:
        new_dict_words.add(w["word"].lower())

still_missing = sorted(new_all_words - new_dict_words)
print(f"Total words in text: {len(new_all_words)}")
print(f"Words with definitions: {len(new_dict_words)}")
print(f"Still missing: {len(still_missing)} → {still_missing}")
