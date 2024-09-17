

fruits = {'apple':100,'grapes':200, 'orange':300,'peach':400}
print("fruits:",fruits)
print("fruits.keys:",fruits.keys())
print("fruits.values:",fruits.values())

# dictionary 는 순서대로 출력되지 않는다. 
# 반복문을 이용한 딕셔너리 출력 
print('for문을 이용한 출력')

# 딕셔너리에 저장된 원소의 갯수만큼 반복하여 key를 인출한다. 
for iyyy in fruits: 
  # 인출한 key를 통하여 value 에 접근하여 출력한다. 
  val = fruits[iyyy]
  print("%s:%d" % (iyyy,val))
# key 는 문자열이므로 %s, value는 정수이므로 %d 를 사용한다. 
# %s string 문자열 첫번째 key apple
# %d decimal 정수 두번째 value 100
# %f float 실수
# yyyyMMdd hi:mi:ss year month day hour minutes seconds
