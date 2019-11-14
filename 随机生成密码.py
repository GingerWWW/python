import random

def pwLetters(length):                            #定义生成字母部分的函数
    password_letters=str()
    num_letters=length-2                          #字母部分位数应是密码位数-2
    for i in range(num_letters):
        letter=chr(random.randrange(97, 123))     #为了简便，采取小写字母a~z的ASCII码值97-122
        password_letters+=letter                  #随机生成字母串
    return password_letters

def insertAtrandom(password_letters,length):      #定义随机插入后完整密码的函数
    password_number=str(random.randint(0,9))      #随机生成一位数字
    password_symbol=str(random.choice(['+','-','*','/','?','!','@','#','$','%','&']))  #随机生成一位特殊字符
    pw_list=list(password_letters)
    r1=random.randint(0,length)                    #插入到随机位置
    pw_list.insert(r1,password_number)
    r2=random.randint(0,length) 
    pw_list.insert(r2,password_symbol)
    password=''.join(pw_list)
    return password

def main():
    while True:
        Num=input('请输出需要生成多少个随机密码')       #协助随机生成多个密码
        try:
            num=int(Num)                           #避免无效输入导致程序无法运行
            if num>0:
                break
            else:
                print('不是合法输入，请输入大于0的整数') #提示用户输入规范
        except:
            print('不是合法输入，请输入大于0的整数')
    for i in range(num):
        n=random.randint(8,16)                     #随机密码位数为8-16位，放在小循环中每次位数可以不同
        print(insertAtrandom(pwLetters(n),n))      #调用函数


if __name__=='__main__':
    main() 
