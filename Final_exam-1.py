#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20201831 이름 : 김태섭

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_string, target): #앞에 있는 매개변수가 my_strung 으로 잘못되어있어 my_string으로 수정함
    
    if target in my_string: #target 문자열이 my_string에 부분적으로 일치하면
        answer = 1        #answer 값이 1
    else:                   #부분적으로 일치하지 않는다면
        answer = 0        #answer 값이 2
    return answer

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter): # letter 매개변수에 모스부호를 넣어줌
    
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}   #딕셔너리 형의 변수를 선언하고 모스부호를 key로 영문자를 value값으로 만들어준다
    
    split_word = letter.split()     #letter 문자열을 공백을 구분자로 split_word에 저장
    
    answer = ''.join(morse[word] for word in split_word ) #split_word에 저장된 항목들을 공백없이 하나의 문자열로 합쳐 answer에 저장

    return answer 

# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    # 딕셔너리를 사용하여 숫자를 key 알파벳을 value
    number_to_alphabet = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j'}

    age_str = str(age) #age를 문자열로 변환
    answer = ''.join(number_to_alphabet[char] for char in age_str) #age_str의 첫 번째 문자부터 key에 대응되는 value값을 반환받아 answer에 문자열을 합쳐 저장

    return answer #최종적으로 PROGEAMMER-857식 나이 값을 반환

# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000


import math  #math 모듈을 import 시킴

def solution(r1, r2):
    answer = 0  #answer의 초기값을 0 으로 초기화
    # x의값의 범위를 1부터 r2까지
    for i in range(1, r2 + 1): 
        if i < r1:                                  #i가 내부 원의 경계에 닿을 때까지
            start_x = math.ceil(math.sqrt(r1**2 - i**2))  #x=i 일때 r1원의 y좌표값을 올림하여 점의 갯수를 셈
        else:
             start_x = 0   #i가 r1값을 벗어난경우

        end_x = int(math.sqrt(r2**2 - i**2)) #x=i 일때 r2원의 y좌표값을 내림하여 점의 갯수를 셈
        answer += 4 * (end_x - start_x + 1)        #한 사분면의 두 원사이의 점의 갯수를 구한후 4배 해주어 answer에 더해줌

    return answer #두 원사이의 전체 점의 갯수를 반환


# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution(numbers):
    # 각 숫자를 문자열로 변환하여 비교 기준을 설정
    numbers = list(map(str, numbers)) # 리스트를 이용하여 변수를 선언
    
    # 두 숫자를 이어 붙였을 때 큰 순서대로 정렬
    numbers.sort(key=lambda x: x*3, reverse=True) #내림차순으로 정리하며 같은수를 세번 반복하여 우선순위를 설정함
    
    # 모든 숫자가 0일 경우 예외 처리
    if numbers[0] == '0': #numbers의 첫 요소가 0인경우
        return '0'  # 0을 함수에 반환함
    
    # 정렬된 숫자를 이어 붙여 문자열로 반환
    answer = ''.join(numbers) #위에서 정렬된 nubers의 요소들을 join을 이용해 answer 문자열로 저장
    return answer #정렬된 값을 반환