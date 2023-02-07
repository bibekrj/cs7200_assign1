import sys
import re

def parse_input(input_file):
    '''
    @param: inputfile name
    takes inputfile as a parameter
    returns number of men/woman, preferences of men and women and matching pairs provided in the file
    '''
    with open(input_file, 'r') as f:
        n = int(f.readline().strip())  # no of men and women
        men_prefs = {}
        women_prefs = {}
        for i in range(n):  # men preferences
            line = f.readline().strip().split()
            man = line[0]
            men_prefs[man] = line[1:]
        for i in range(n):  # women preferences
            line = f.readline().strip().split()
            woman = line[0]
            women_prefs[woman] = line[1:]
        matching = {}
        for i in range(n):  # matching pairs
            line = f.readline().strip().split()
            man = line[0]
            woman = line[1]
            matching[man] = woman
    return (n, men_prefs, women_prefs, matching)


def is_stable_matching(women_prefs, men_prefs, matching):
    '''
     function to check for the  stablity of provided pairs.
     '''
    checked = 0
    unstable_pair = []
    checked_pair = []
    # men_list = [manm for manm in men_prefs.keys()]
    # women_list = [womanw for womanw in women_prefs.keys()]
    # print(men_list, women_list)
    better_men_options = {}
    better_women_options = {}
    for man, woman in matching.items():
        current_position_man = women_prefs[woman].index(man)
        # print(man, current_position_man)

        current_position_woman = men_prefs[man].index(woman)
        # print(woman, current_position_woman)

        better_men = [man for man in women_prefs[woman][:current_position_man]]
        # print('men', better_men)

        better_women = [woman for woman in men_prefs[man]
                        [:current_position_woman]]
        # print('women', better_women)

        better_men_options[man] = better_women
        better_women_options[woman] = better_men

    # print("better men options",better_men_options)
    # print("better woman options", better_women_options)
    # print('\n')
    # print('\n')

    for m, w in better_men_options.items():
        print(m)
        for i in w:
            print(i, "i")
            checked += 1
            checked_pair.append([m,i])
            if m in better_women_options[i]:
                print("Better man found %s for %s" % (m, i))
                unstable_pair.append([m, i])
                break
                # checked += 1

    # print("checkedpair", checked_pair)
    # print("unstable pair",unstable_pair)
    if (len(unstable_pair) > 0):
        return False, unstable_pair, checked_pair
    else:
        return True, [], checked_pair


def write_output(output_file, result, matching):
    '''
    write the program output to a text file
    @param output_file, results
    return None
    '''
    checked, unstable, checked_pair = result
    with open(output_file, 'w') as f:
        if checked:
            f.write("100\n")
        else:
            f.write("200\n")
        f.write(str(len(checked_pair)) + '\n')
        # if len(unstable) > 0:
        for pair in checked_pair:
            f.write(str(pair) + '\n')


def create_output_filename(input_filename):
    '''
    function to create output file name
    '''
    base, number, ext = re.findall(r"(\D+)(\d*)(\.\w+)", input_filename)[0] 
    return f"output{number}{ext}"

def main(input_file, output_file):
    '''
    @param: inputfile name and output file name
    main function that runs the program
    calls on is_stable_matching to check for stability in the provided pairs
    writes the output to the given file name
    '''
    n, men_prefs, women_prefs, matching = parse_input(input_file)
    result = is_stable_matching(women_prefs, men_prefs, matching)
    write_output(output_file, result, matching)


if __name__ == '__main__':
    inputFileName = sys.argv[1]
    outputFilename = create_output_filename(inputFileName)
    main(inputFileName, outputFilename)  # calling the main function
