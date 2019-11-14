while True:                                 #while大循环进行多次模拟楼层试验
    Floor=input("请输入你想到达的楼层:")
    try:                                    #避免字符/非正整数/超出实际楼层等无效输入导致程序无法运行
        floor=int(Floor)
        if 18<floor<=30:                    #设定楼层上限为30层
            actualFloor=floor-2 
        elif floor>14 and floor<18:
            actualFloor=floor-1
        elif 0<floor<14:
            actualFloor=floor
        else:                               #考虑边界条件14、18楼,及其他整数类型的非法输入
            actualFloor='输入的楼层不存在'
        print("实际楼层", actualFloor)        #print函数在条件外，避免重复代码
    except:
        print('无效输入,请输输入1-30除14、18楼层整数') #提示用户规范输入

    while True:
        flag=input('是否继续输入？请输入yes/no')  #询问用户是否再次模拟试验
        if flag.lower() not in('yes','no'):  #考虑yes/no大小写问题,转成小写判断
                print('请注意，只能输入yes/no') #规范输入
        else:
            break
    if flag.lower()=='no':                   #退出系统，避免死循环
        print('试验完毕，退出系统')
        break
                
