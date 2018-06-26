"""
****
bit and byte
+ 컴퓨터 데이터의 크기를 나타내는 단위
+ 1bit : 0과 1 2가지 데이터를 표현 가능
+ 1byte : 8bit , 256(2**8)가지 데이터를 표현가능


character Encoding(문자 인코딩)
+ 문자나 기호들의 집합을 부호화(인코딩) 하는 방법
+ 인코딩의 2가지 의미
 -> 변환하는 방법  : ascii, cp949, utg8, utf16, utf32 등
 -> 변환하는 행위

+ 하나의 동영상을 avi, mp4, mkv 등으로 변환(인코딩) 할 수 있듯이, 하나의 문자열도 다양한 인코딩으로 변환 할 수 있습니다.
+ 각 인코딩마다 표현 가능한 글자와 범위가 다릅니다.

Encoding & Decoding
+ 일반적인 인코딩의 의미 : 어떠한 값을 특정 룰에 맞춰 다른 형식으로 변환
 -> 디코딩 : 역변환
+ 파이썬 유니코드 문자열(str)에서의 인코딩 의미
 -> 하나의 문자를 하나의 숫자로서 표현하는 다양한 Mapping Rule (인코딩에 따라서 Rule이 다름)
 -> 해당 Mapping Rule에 맞춰 변환 하는 것

str 인코딩 -> byte
byte 디코딩 -> str

유니코드
기존 인코딩의 한계를 극복하고, 전 셰계의 모든 문자를 일관되게 표현할 수 있도록 설게된 산업 표준
UTF-8
 모든 유니코드 문자 표현 가능
 가변 길이 문자 인코딩 방식 : 1byte ~ 4byte



유니코드 문자열(str타입)>인코딩>bytes탑입 문자열

문자열.encode('utf-8')
문자열.decode('utf-8')

+++++++++++++모든지!! 유니코드(str타입)을 한 번 거친 후에 인코딩해라


** 참고: 바이너리 데이터를 파이썬으로 읽어들이면, bytes 타입 (이미지-디코트 수행하면안된다)


"""
