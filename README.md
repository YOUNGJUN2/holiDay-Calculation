# 휴일 계산 프로그램

밥을 먹다가 부모님이 한 달 뒤 약속을 잡으시는데 달력을 보며 '하나 둘 셋 ---' 쉬는 날인지 확인하기 위해 달력의 날짜를 세고 계시는 모습을 봤다. 따로 근무하는 날이 표시되는 근무표가 안나오기 때문이다.

- 부모님의 근무 패턴은 1 2 3 **4** 5 6 7 **8** 9 이렇게 3일 일하고 쉬는 날이 돌아오게 되는데 여기서 변수는 쉬는 날임과 동시에 '토요일'일 경우에는 그 다음 날인 일요일까지 이틀을 연달아 쉬고 나서 이틀만을 근무한 뒤 다시 위의 패턴으로 돌아온다.

- 결국, 4일 마다 쉬는 날은 고정이고, 쉬는 날이 '토요일'(1)일 경우에는 **1 2** 3 4 **5** 와 같이 조금 바뀐 패턴으로 반복된다.

따라서 약속 계획을 잡으실 때는 달력을 보며 하나하나 숫자를 세셨기 때문에 번거로워하셨고, 약속일이 멀수록 버거워하시는 모습을 종종 봤다.

부모님의 번거로움을 덜어주고자 날짜만 지정하면 그 날이 일하는 날인지, 쉬는 날인지 직접 계산하여 알려주는 프로그램을 개발했다.
<hr>

**<http://yjpi.iptime.org:4003/HoliDay>**

