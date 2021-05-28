def print_log(each_line=False):
    content_list = get_log()

    if each_line:
        for line in content_list:
            print(line)
    else:
        print(content_list)


def clean_log():
    file = open('log/posts.txt', 'w')
    file.write('')
    file.close()


def write_to_log(content: str):
    file = open('log/posts.txt', 'a')
    file.write(content)
    file.close()


def get_log():
    file = open('log/posts.txt', 'r')
    content = file.read()
    content_list = content.split('\n')
    file.close()
    return content_list
