"""
만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어가라
"""
m= int(input('돈이 얼마나 있니?'))

print("내가 가진 돈", m, '원입니다.', sep='')

if m >= 3000:
    print('택시로 가는게 좋겠군!!!')
else:
    print('쭈쭈바 먹으면서 걸어가는게 좋겠군!!!')

# 년도를 입력받아 윤/평년을 판단하는 프로그램을 만드시오
# if문으로도 해보고, 삼항 연산자로도 해보자