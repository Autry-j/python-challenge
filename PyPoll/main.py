def print_output(candidates):
    total_votes = 0
    max_votes = 0
    winner = ""
    
    for key in candidates:
        total_votes += candidates[key]

    print(f'Election Results')
    print(f'{"-" * 25}')
    print(f'Total Votes: {total_votes}')
    print(f'{"-" * 25}')

    for key in candidates:
        if candidates[key] > max_votes:
            max_votes = candidates[key]
            winner = key
        print(f'{key} {candidates[key]*100.0/total_votes: .2f}% ({candidates[key]})')
    
    print(f'{"-" * 25}')
    print(f'\nWinner: {winner}\n')
    print(f'{"-" * 25}')

def process(file_name):

    candidates = {}
    line_number = 0
	
    with open(file_name, "r") as f:
        while True: 
            line = f.readline()
            if not line:
                break
            fields = line.split(",")

            if line_number > 0:
                key = fields[2].strip()
                candidate = candidates.get(key)
                if candidate == None:
                    candidates[key] = 0
                candidates[key] += 1
            line_number += 1

        print_output(candidates)

file_name = "Resources/election_data.csv"
process(file_name)