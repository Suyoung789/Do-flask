Flask
============
##### Let's flask
## With(with as)?
`with as`구문은 파이썬 2.5에서 도입된 기능이다.
또한 `with as` 구문은 `try-finally` 구문을 대신하여 더 쉽고 간편하게 나타낼 수 있게한다.   
일단 파일 처리를 위해서는 다음과 같은 과정이 필요하다
- 파일을 연다 
- 열은 파일로 필요한 처리를 한다
- 열었던 파일을 닫는다  
 
 이를 `try-finally` 구문을 이용하여 구현하면
```
 f=open('test.txt','w')     #파일을 연다.
 try: 
     f.write('hello python')    #열었던 파일로 필요한 처리를 한다.
 finally:
    f.close()                  #파일을 닫는다.
```

`with as`구문 으로 이러한 코드를
```
with open('test.txt', 'w') as f:
    f.write('hello python)
```
이렇게 짧게 바꾸어 구현할 수 있다.

`with as`구문은 `context manager`를 따라 실행되는데, with 블럭을 사용하여 파일을 열고 필요한 처리를 수행하다 with 블럭을 빠져나가면 파일이 자동으로 닫히게 된다. 이때, `with문`이 실행되면 `__enter__()`가 실행되면서 파일이 열리게 되고 `with` 블럭을 빠져나가게 되면 `__exit__()`이 실행되며 파일이 닫힌다.  
내가 이해한 바로는, `__enter__()`에는 파일을 여는 것과 관련된 함수가 있을 것이고, `__exit__()`에는 파일을 닫는 것과 관련된 함수가 있을 것이다.  
또한, `컨텍스트 매니저(context manager)`는 `__enter__()`와 `__exit__()`메소드들을 정의하는 객체로써 이해했다.