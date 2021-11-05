# 선형회귀식을 이용한 키 예측하기
import pandas as pd
from sklearn.linear_model import LinearRegression
import turtle

# 숫자입력용함수
def input_only_num(msg):
    num = ''
    while True :
        num = turtle.textinput(title=msg, prompt='숫자만 입력')
        if(not isNumber(num)):
            print("숫자만 입력해주세요...")
        else :
            break
    return float(num)

# 성별입력 함수
def input_gender(g):
    if(g == '남'):
        return 0
    elif(g == '여'):
        return 1
    else:
        return input_gender(turtle.textinput(title="성별 입력", prompt='남, 여 중에 입력'))

# 숫자형 문자열인가?
def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

def show_height(t, msg):
    t.clear()
    t.up()
    t.goto(-200,0)
    t.write(f"예상되는 당신의 키\n >> {msg:.2f}cm", font=("", 30))


lr=LinearRegression()

df=pd.read_csv("Galtons Height Data.csv")

# 인치 단위이기 때문에 cm단위로 변경
df['Father']=df['Father']*2.54
df['Mother']=df['Mother']*2.54
df['Height']=df['Height']*2.54

# Gender 데이터를 활용하기위해서 숫자로된 열을 추가
df.loc[df['Gender']=='M', 'Gender_num']=0
df.loc[df['Gender']=='F', 'Gender_num']=1

input_data=df[['Father','Mother','Gender_num']]
target_data=df['Height']

lr.fit(input_data, target_data)

t = turtle.Turtle()

while True:
    father_height = input_only_num("아버지의 키는?")
    mother_height = input_only_num("어머니의 키는?")
    gender_num = input_gender(turtle.textinput(title="성별 입력", prompt='남, 여 중에 입력'))

    pred_height = lr.predict([[father_height, mother_height, gender_num]])

    print(pred_height)
    show_height(t, pred_height[0])
    # 여기서 터틀로 키 보여주고 계속 반복적으로 입력받기

