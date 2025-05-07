import random

# Load quotes
with open("quotes.txt", "r", encoding="utf-8") as f:
    quotes = [line.strip() for line in f if line.strip()]

new_quote = f"> {random.choice(quotes)}"

# Load README
with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Replace quote between markers
start_marker = "<!-- quote-start -->"
end_marker = "<!-- quote-end -->"
in_quote = False
updated_lines = []

for line in lines:
    if start_marker in line:
        in_quote = True
        updated_lines.append(line)
        updated_lines.append(new_quote + "\n")
        continue
    if end_marker in line:
        in_quote = False
        updated_lines.append(line)
        continue
    if not in_quote:
        updated_lines.append(line)

# Save updated README
with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(updated_lines)
