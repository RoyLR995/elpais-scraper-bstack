from utils.title_store import TitleStore
from utils.translation_util import translate_text
import re
from collections import Counter

def test_translate_titles_and_count():
    titles = TitleStore.get_titles()
    assert titles, "No titles found. Run opinion scraping test first."

    translated = []
    print("\n Translated Titles:")
    for title in titles:
        english = translate_text(title)
        print(f"• {english}")
        translated.append(english)

    # Frequency analysis
    word_list = []
    for title in translated:
        words = re.findall(r'\b\w+\b', title.lower())
        word_list.extend(words)

    counts = Counter(word_list)
    print("\n Words that appear more than twice:")
    found = False
    for word, count in counts.items():
        if count > 2:
            print(f"'{word}' appears {count} times")
            found = True

    if not found:
        print("No repeated words found.")
