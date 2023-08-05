def solution(hp):
    G_ant = 5   # 장군 개미의 공격력
    S_ant = 3   # 병정 개미의 공격력
    N_ant = 1   # 일 개미의 공격력
    
    count_g = 0 # 장군 개미가 투입된 수
    count_s = 0 # 병정 개미가 투입된 수
    count_n = 0 # 일 개미가 투입된 수
    
    # 해당 문제는 장군 개미를 먼저 투입하여
    # hp를 깎는 것이 제일 효율적
    # 투입된 장군 개미의 수를 출력
    count_g = hp // G_ant
    
    # 이 후 남은 체력으로 병정개미 or 일개미 투입 판단
    hp = hp % G_ant
    
    if hp == 4 :
        count_s += 1
        count_n += 1
    elif hp == 3 :
        count_s += 1
    elif hp == 2 :
        count_n += 2
    elif hp == 1:
        count_n += 1
        
    answer = count_g + count_s + count_n # 전체 개미가 투입된 수
    
    return answer

print(solution(23))
print(solution(24))
print(solution(999))