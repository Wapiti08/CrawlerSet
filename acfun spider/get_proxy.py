import random


def get_head():
    lst = ['Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
           'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
           'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
           'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',
           'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
           'Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3',
           'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19',
           'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
           'Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1']

    i = random.randint(0, len(lst) - 1)
    # print(i)
    head = {'User-Agent': lst[i]}
    return head


def get_ip():
    f = open('ip.csv', 'rb')
    ips = []
    while True:
        ip = f.readline().decode()
        if not ip:

            break
        elif ip == '\r\n':
            continue
        else:
            new_ip = ''
            for i in ip:
                if i == '\r':
                    break
                elif i == ',':
                    i = ':'
                    new_ip += i
                else:
                    new_ip += i

            if new_ip in ips:
                # print('重复!')
                # num += 1
                pass
            else:
                ips.append(new_ip)

    use_ip = random.choice(ips)
    return use_ip


if __name__ == '__main__':
    print(get_ip())
    print(get_head())
