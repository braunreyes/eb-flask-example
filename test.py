
def puzzle_answer(text):
    text = 'Please solve this puzzle: ABCD A---> B--<- C--=- D-->-'
    clean_prefix = text.replace('Please solve this puzzle: ABCD ','')
    item_list = clean_prefix.split()
    for i,item in enumerate(item_list):
        if '->' in item:
            item_list[i] = item.replace('->','>>')
        if '<-' in item:
            item_list[i] = item.replace('<-','<<')
    for i,item in enumerate(item_list):
        if item[1] == '-':
            item = item[:1] + '<' + item[2:]
        if item[2] == '-':
            item = item[:2] + '>' + item[3:]
        if item[3] == '-':
            item = item[:3] + '<' + item[4:]
        if item[4] == '-':
            item = item[:4] + '>'
        item_list[i] = item
    item_list[0] = item_list[0][:1] + '=' + item_list[0][2:]
    item_list[1] = item_list[1][:2] + '=' + item_list[1][3:]
    item_list[2] = item_list[2][:3] + '=' + item_list[2][4:]
    item_list[3] = item_list[3][:4] + '='
    answer = ''' ABCD
    {0}
    {1}
    {2}
    {3}'''.format(*item_list)
    return answer
