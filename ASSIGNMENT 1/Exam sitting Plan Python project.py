# NAMES: IZERE JOYEUX FILS     REG NUMBER: 224004106
# Project 48: Exam Seating Plan


# Integers
import array

marks = [85, 90, 78, 92, 88]  
total = sum(marks)
average = total / len(marks)
minimum = min(marks)
maximum = max(marks)
print("Total marks:", total)
print("Average mark:", average)
print("Minimum mark:", minimum)
print("Maximum mark:", maximum)

# Strings
report1 = f"Total marks summary: {total}"
report2 = f"Average mark summary: {average:.2f}"
print("\nReport:")
print(report1)
print(report2)

# Booleans
threshold = 85
if average > threshold and maximum > 90: 
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

# Lists
seating_plan = ["Row1_Seat1", "Row1_Seat2", "Row2_Seat1", "Row2_Seat2"]
print("\nOriginal Seating Plan:", seating_plan)
seating_plan.append("Row2_Seat3")  
seating_plan.remove("Row1_Seat2") 
seating_plan.sort()  
print("Updated Seating Plan:", seating_plan)

# Arrays
from array import array
seating_scores = array('i', [85, 90, 78]) 
array_sum = sum(seating_scores)
print("\nArray Sum:", array_sum)
print("List Sum for comparison:", sum(marks[:3])) 

# Dictionaries
seating_records = [
    {"id": 1, "name": "Alice", "value": 85},
    {"id": 2, "name": "Bob", "value": 90},
    {"id": 3, "name": "Charlie", "value": 78}
]
print("\nOriginal Records:")
for record in seating_records:
    print(record) 

# Update one record
seating_records[0]["value"] = 88 
# Delete record
del seating_records[1]  
# total of 'value' field
total_value = sum(record["value"] for record in seating_records)
print("Updated Records:")
for record in seating_records:
    print(record)
print("Total of values:", total_value)
