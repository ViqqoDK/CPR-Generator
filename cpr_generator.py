birtday = input("Fødselsdag: ")
print()
values = [4,3,2,7,6,5,4,3,2,1]

def checksum(cpr_number):
    SUM = 0
    for idx in range(len(values)):
        SUM += int(cpr_number[idx]) * values[idx]
        
    if SUM % 11 == 0:
        print(f"{cpr_number}")


for control in range(0,9999):
    control = f"{control:04d}"
    checksum(birtday+control)
    
