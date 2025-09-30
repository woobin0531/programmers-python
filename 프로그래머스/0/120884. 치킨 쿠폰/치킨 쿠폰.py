def solution(chicken):
    answer = 0
    coupons = chicken

    while coupons >= 10:
        # 현재 쿠폰으로 받을 수 있는 서비스 치킨의 수
        new_service_chicken = coupons // 10
        answer += new_service_chicken
        
        # 남은 쿠폰 + 서비스 치킨으로 새로 받은 쿠폰
        coupons = (coupons % 10) + new_service_chicken
        
    return answer