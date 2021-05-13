import statistics

def find_first(sums,name,ascii_list,gender):
    '''find first trait given name and gender
    '''
    # sums = 0
    # ascii_list = []
    # if name:
    #     for i in name:
    #         if i:
    #             ascii_list.append(ord(i))
    #         sums += ord(i)

    first_trait = sums/len(name)/statistics.median_low(ascii_list)
    first = {'f':{'low':'1','high':'2'},'m':{'low':'3','high':'4'}}

    key = ''
    if first_trait >= 0.98:
        key = 'high'
    else:
        key = 'low'
    return first[gender][key]

def find_second(ascii_list,first):
    '''find second trait given name and first trait
    '''

    second = {'1':['5','6'],'2':['7','8'],'3':['9','10'], '4':['11','12']}

    # ascii_list = [ord(i) for i in name]
    # print(len(name))
    # print(name)
    half = round(len(ascii_list)/2)
    character = sum(ascii_list[:half])/sum(ascii_list[half:])


    if character >= 0.90:
        return second[first][1]
    else:
        return second[first][0]
    return character

def find_third(ascii_list, second):
    
    third = {'5':['13','14'],'6':['15','16'],'7':['17','18'],
                '8':['19','20'],'9':['21','22'],'10':['24','23'],
                '11':['26','25'],'12':['28','27']}

    # ascii_list = []
    # for i in name:
    #     i = i.strip().lower()
    #     if i:
    #         ascii_list.append(ord(i))
    # print(ascii_list)
    difference = max(ascii_list) - min(ascii_list)
    if difference > 17:
        return third[second][1]
    else:
        return third[second][0]
 
def find_fourth(third,constellation):
    fourth = {'13': ['29', '30'], '14': ['31', '32'], '15': ['33', '34'], '16': ['35', '36'],
              '17': ['37', '38'], '18': ['39', '40'], '19': ['41', '42'], '20': ['43', '44'],
              '21': ['45', '46'], '22': ['47', '48'], '23': ['49', '50'], '24': ['51', '52'],
              '25': ['53', '54'], '26': ['55', '56'], '27': ['57', '58'], '28': ['59', '60']}
    if int(constellation) <= 6:
        return fourth[third][0]
    else:
        return fourth[third][1]


import json
f = open('output.json')
dictionary = json.load(f)
f.close()

