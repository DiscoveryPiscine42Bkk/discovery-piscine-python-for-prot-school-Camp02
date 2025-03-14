def average(scores_dict):

    total_score = 0
    count = 0
    students = list(scores_dict.keys())
    i = 0
    
    while i < len(students):
        total_score += scores_dict[students[i]]
        count += 1
        i += 1

    return total_score / count if count > 0 else 0

if __name__ == "__main__":
    class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
input()