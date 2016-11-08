s = "fadfaq3e324efq432432412124ewtaf31243546764523489892380809589809342809089342"
letters = []
numbers = "123456789"

for sym in s:
    if not sym in numbers:
        letters.append(sym)

print(letters)
