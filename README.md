## HIBERNATE ORM
자바 언어를 위한 객체 관계 매핑 프레임워크
관계형 디비 테이블을 자바 객체로 매칭시키겠다는 것.

> 연결 시 jdbc url >> jdbc:h2:mem:testdb 로 해야 됨

장점
1. 재사용성이 좋다
2. 쿼리 많이 몰라도 된다.
3. 객체로 쿼리가 자동 매핑 되므로 편하다.
4. DB종류가 바뀌어도 대응이 쉽다.
http://hibernate.org/orm/documentation/getting-started/
출처 : https://bcho.tistory.com/906

## JPA 식별자 자동생성
##### @Generated 어노테이션 사용 == @GeneratedValue(strategy = GenerationType.AUTO)

## @RestController
@Controller + @ResponseBody
##### @autowired 각 상황의 타입에 맞는 IoC컨테이너 안의 Bean 주입하는 것

##JpaRepository
인터페이스에 미리 검색 메소드를 정의해두는 것.
> public interface 이름 extends JpaRepository<엔티티, ID유형>

@Repository 어노테이션 붙여야됨

## HTTP 패킷
클라이언트가 서버로 요청할때 보내는 데이터를 http 프로토콜을 사용하여 보낼때, 
http 패킷이라 한다. 
헤더에는 7가지 http 메서드 방식, 
클라이언트 정보, 브라우저 정보, 접속할 url 정보가 있으며
바디에 특정 데이터를 담아 서버에게 특정 요청을 보낼수 있다.


## get, post 방식 차이
### get 
* 클라이언트 데이터를 url 뒤에 붙여 보낸다. 
* ?마크 뒤에 key와 value 쌍으로, & 구분한다.
* url에 보내는 것이므로 헤더에 정보를 포함하여 요청하는 것
* body는 비어 있으므로 Content-Type 헤드필드 안들어간다. 
* get방식 요청은 캐싱때문에 post 보다 빠르다.
### post
* body에 정보 넣어 보낸다.
* Content-Type 헤더필드 필요, 어떤타입 쓸지 넣어야 된다.

### 400 에러
https://ko.go-travels.com/87082-how-to-fix-a-400-bad-request-error-2617988-7962899

### 405 에러

https://docs.microsoft.com/ko-kr/aspnet/web-api/overview/testing-and-debugging/troubleshooting-http-405-errors-after-publishing-web-api-applications
 