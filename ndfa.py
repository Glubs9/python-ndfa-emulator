import sys

states = ["0"] #states is an array of the different states (by number) the ndfa is in

def next_state_file_handler(state_num, alpha_char):
        file_obj = open(state_num + ".txt", "r")
        test = open(state_num + ".txt", "r").readline()
        if test[:6] == "ACCEPT":
                return True
        return next_state(file_obj, alpha_char)

def next_state(state_file_obj, alpha_char):
        ret_states = []
        for line in state_file_obj:
                if line[0] == alpha_char:
                        ret_states.append(line[1:-1])
                elif line[0] == "-" and line[1] != alpha_char:
                        ret_states.append(line[2:-1])
        return ret_states

alpha_str = open("alphabet.txt", "r").read()
for char in alpha_str:
        next_states = []
        for state in states:
                tmp = next_state_file_handler(state, char)
                if tmp == True:
                        print("ACCEPTED")
                        quit()
                if tmp != []:
                        next_states += tmp
        states = list(set(next_states))

        if len(sys.argv) == 2 and sys.argv[1] == "d":
                print(char + ": " + states)

for state in states:
        tmp = next_state_file_handler(state, None)
        if tmp == True:
                print("ACCEPTED")
                quit()

print("NOT ACCEPTED")
