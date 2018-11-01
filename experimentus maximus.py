def month_name(num):
    num = num - 1
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months[num]

print(month_name(12))