from flask import Flask, request, jsonify
application = Flask(__name__)

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
    answer = ''' ABCD\n{0}\n{1}\n{2}\n{3}'''.format(*item_list)
    return answer


@application.route("/", methods=['GET'])
def root():
    q = request.args.get('q')
    if q == 'Ping':
        return 'OK'
    if q == 'Position':
        return 'Data Engineer'
    if q == 'Resume':
        return 'https://www.linkedin.com/in/braun-reyes-60360656/'
    if q == 'Name':
        return 'Braun Reyes'
    if q == 'Years':
        return '5'
    if q == 'Status':
        return 'Yes'
    if q == 'Phone':
        return '7735121285'
    if q == 'Referrer':
        return 'Linkedin Message from Internal Recruiter'
    if q == 'Degree':
        return 'Bachelors in Marketing and Masters in Education are not relevant to Data Engineering'
    if q == 'Puzzle':
        d = request.args.get('d')
        result = puzzle_answer(d)
        return result
    if q == 'Email':
        return 'braunr00@gmail.com'
    if q == 'Source':
        return 'https://github.com/braunreyes/eb-flask-example'
    else:
        return 'OK'

if __name__ == '__main__':
    application.run(debug=True)

# examples from access logs
# 172.31.30.91 (50.17.218.234) - - [02/May/2018:04:12:31 +0000] "GET /?q=Ping&d=Please+return+OK+so+that+I+know+your+service+works. HTTP/1.1" 200 2 "-" "-"
# 172.31.86.55 (50.17.218.234) - - [02/May/2018:04:12:31 +0000] "GET /?q=Position&d=Which+position+are+you+applying+for%3F HTTP/1.1" 200 2 "-" "-"
# 172.31.30.91 (50.17.218.234) - - [02/May/2018:04:12:31 +0000] "GET /?q=Resume&d=Please+provide+a+URL+where+we+can+download+your+resume+and+cover+letter. HTTP/1.1" 200 2 "-" "-"
# 172.31.86.55 (50.17.218.234) - - [02/May/2018:04:12:31 +0000] "GET /?q=Name&d=What+is+your+full+name%3F HTTP/1.1" 200 2 "-" "-"
# 172.31.30.91 (50.17.218.234) - - [02/May/2018:04:12:31 +0000] "GET /?q=Years&d=How+many+years+of+software+development+experience+do+you+have%3F HTTP/1.1" 200 2 "-" "-"
# 172.31.86.55 (50.17.218.234) - - [02/May/2018:04:12:31 +0000] "GET /?q=Status&d=Can+you+provide+proof+of+eligibility+to+work+in+the+US%3F HTTP/1.1" 200 2 "-" "-"
# 172.31.30.91 (50.17.218.234) - - [02/May/2018:04:12:31 +0000] "GET /?q=Phone&d=Please+provide+a+phone+number+we+can+use+to+reach+you. HTTP/1.1" 200 2 "-" "-"
# 172.31.86.55 (50.17.218.234) - - [02/May/2018:04:12:31 +0000] "GET /?q=Referrer&d=How+did+you+hear+about+this+position%3F HTTP/1.1" 200 2 "-" "-"
# 172.31.30.91 (50.17.218.234) - - [02/May/2018:04:12:31 +0000] "GET /?q=Degree&d=Please+list+your+relevant+university+degree%28s%29. HTTP/1.1" 200 2 "-" "-"
# 172.31.86.55 (50.17.218.234) - - [02/May/2018:04:12:31 +0000] "GET /?q=Puzzle&d=Please+solve+this+puzzle%3A%0A+ABCD%0AA-%3E--%0AB--%3E-%0AC--%3D-%0AD--%3C-%0A HTTP/1.1" 200 2 "-" "-"
# 172.31.30.91 (50.17.218.234) - - [02/May/2018:04:12:31 +0000] "GET /?q=Email+Address&d=What+is+your+email+address%3F HTTP/1.1" 200 2 "-" "-"
# 172.31.86.55 (50.17.218.234) - - [02/May/2018:04:12:31 +0000] "GET /?q=Source&d=Please+provide+a+URL+where+we+can+download+the+source+code+of+your+resume+submission+web+service.
