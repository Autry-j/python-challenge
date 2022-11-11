def process(file_name):

    months = {}
    total = 0
    changes = 0
    last = None
    count = 0 
    max_increase = 0
    max_increase_date = ""
    max_decrease = 0
    max_decrease_date = ""

    with open(file_name, "r") as f:
        while True: 
            line = f.readline()
            if not line:
                break
            fields = line.split(",")
            if '-' in fields[0]:
                parts = fields[0].split("-")
                months [parts[0]+"_"+parts[1]] = 1
                p_and_l = int(fields[1].strip())
                total += p_and_l
                if last is not None:
                    changes += p_and_l - last
                    if p_and_l >= last and (p_and_l - last) > max_increase:
                        max_increase = p_and_l - last
                        max_increase_date = fields[0]
                    elif p_and_l < last and (last - p_and_l) > max_decrease:
                        max_decrease = last - p_and_l
                        max_decrease_date = fields[0]
                else:
                    max_increase = 0
                    max_decrease = 0
                last = p_and_l
                count += 1

        print("Financial Analysis")
        print(f"{'-' * 30}")
        print(f'Total: ${total}')
        print(f"Total Months: {len(months)}")
        print(f"Average Change: ${round(changes*1.0/count, 2): .2f}")
        print(f"Greatest Increase in Profits: {max_increase_date} ${max_increase}")
        print(f"Greatest Decrease in Profits: {max_decrease_date} ${max_decrease}")

file_name = "Resources/budget_data.csv"
process(file_name)