"""
 Below code convert line text to  this form : {'a1': [
                                ['bb1', '6'],
                               ['bb2', '7'],
                                ['bb3', '8']
                            ],
                            'a2': [
                                   ['b2', '2'],
                                   ['b2', '3'],
                                   ['b2', '4']
                                   ]
                     }
"""

from tqdm import tqdm
import time

def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item +"  "
    return str

def class_str_tuple(mydat_dict):
    str = ""
    for my_tuple in mydat_dict:
        str += convertTuple(my_tuple)+'\n'
    return str

def write_specific_file(file_name, mydat_dict):
    with open(file_name, 'w', encoding='utf-8') as toWrite:
        toWrite.write(class_str_tuple(mydat_dict))
        toWrite.close()

def write_to_file(conf_token, sus_token, del_token):
    write_specific_file("confirmed.txt", conf_token)
    write_specific_file("suspicious.txt", sus_token)
    write_specific_file("deletion.txt", del_token)

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().splitlines()

def convert_file_to_dict(file_lines):
    my_dict = {}
    for line in file_lines:
        temp = line.split()
        if len(temp) != 3:
            continue
        my_dict.setdefault(temp[0], []).append([temp[1],temp[2]])
    return my_dict

    for line in lines_read_file:
        my_list.append(line)
    return my_list

def process(data_dict):
    conf_token_list = []
    sus_token_list = []
    del_token_list = []
    threshold_one = 20
    temp = list(data_dict)
    for key_master, values in tqdm(data_dict.items()):  # num key list
        first_key_max = values[0][0]
        first_freq_max = values[0][1]

        # append to confirm list
        conf_token_list.append((key_master , first_key_max , first_freq_max))

        # prepare second threshold
        threshold_two = int( first_freq_max ) * 0.1

        for mid_word , line_freq in values:  # num lists of master_loop_row key
            if int(line_freq) < threshold_one:
                # threshold one direct deletion
                del_token_list.append((key_master , mid_word , line_freq) )  # deleiton list
                # traverse 2nd not normalized form word
            else:
            # compare master_loop_row normalized with loop_for_list_in_row of max woard
            # if ( second_num_other_list > max_num_first_list * 0.10 )
                if int(line_freq) < threshold_two:
                    del_token_list.append((key_master , mid_word , line_freq)) # deleiton list
                else:
             # direct add as confirmation list condition satisfied
                    if  first_key_max == mid_word:
                        conf_token_list.append((key_master , mid_word , line_freq)) # confirmation list
            # mid state not del not conf add to suspicious  list condition satisfied
                    else:
                        sus_token_list.append((key_master , mid_word , line_freq)) # deleiton list
    write_to_file(sus_token_list, conf_token_list, del_token_list)

def driver(file_path):
    print(f"start hanlding file..")
    file_line_as_str = read_file(file_path)
    data_dict = convert_file_to_dict(file_line_as_str)
    process(data_dict)

if __name__ == "__main__":
    # record start time
    start_time = time.time()
    driver('test1.txt')
    # record end time
    print("Total Run Time =  %s seconds " % (time.time() - start_time))



