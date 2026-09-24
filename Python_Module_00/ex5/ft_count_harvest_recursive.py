def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def helper(day_1, days):
        if day_1 > days:
            return
        print("Day", day_1)
        helper(day_1 + 1, days)
    helper(1, days)
    print("Harvest time!")
