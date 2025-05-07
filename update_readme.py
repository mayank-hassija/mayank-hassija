import random

# Load all quotes
with open("quotes.txt", "r", encoding="utf-8") as f:
    quotes = [q.strip() for q in f if q.strip()]

# Pick a random quote
quote = random.choice(quotes)

# Read the README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the placeholder <><> with the quote
updated_content = content.replace("<><>", f"> {quote}")

# Write the updated README
with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_content)
