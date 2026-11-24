from collections import Counter

cards = []
cardsNum = []
cardsAlpha = []
ans = 0

for i in range(5):
    color, number = input().split()
    cards.append({color.lower(): int(number)})

for card in cards:
    cardsNum.extend(card.values())
    cardsAlpha.extend(card.keys())

counts = Counter(cardsNum)
cardsCount = list(counts.values())

sameColor = len(set(cardsAlpha)) == 1
consecutive = len(set(cardsNum)) == 5 and max(cardsNum) - min(cardsNum) == 4

if sameColor and consecutive:
    ans = max(cardsNum) + 900

elif cardsCount.count(4) == 1:
    nums = [number for number, count in counts.items() if count == 4]
    ans = nums[0] + 800

elif cardsCount.count(2) == 1 and cardsCount.count(3) == 1:
    nums1 = [number for number, count in counts.items() if count == 2]
    nums2 = [number for number, count in counts.items() if count == 3]
    ans = nums1[0] + nums2[0] * 10 + 700

elif sameColor:
    ans = max(cardsNum) + 600

elif consecutive:
    ans = max(cardsNum) + 500

elif cardsCount.count(3) == 1:
    nums = [number for number, count in counts.items() if count == 3]
    ans = nums[0] + 400

elif cardsCount.count(2) == 2:
    nums = [number for number, count in counts.items() if count == 2]
    ans = max(nums) * 10 + min(nums) + 300

elif cardsCount.count(2) == 1:
    nums = [number for number, count in counts.items() if count == 2]
    ans = nums[0] + 200

else:
    ans = max(cardsNum) + 100

print(ans)