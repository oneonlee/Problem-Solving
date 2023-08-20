def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))] # 총 id의 개수만큼 0으로 초기화
    
    report = list(set(report)) # set 함수를 통해 중복신고 제거
    
    report_freq_dict={} # key: 신고당한 id, value : 신고받은 횟수
    killer_dict = {} # key: 신고당한 id, value : 그 사람을 신고한 id들 (띄어쓰기로 구분)
    
    # report_freq_dict와 killer_dict 초기화
    for id in id_list:
        report_freq_dict[id] = 0 # 모든 id에 대해 신고횟수를 0으로 초기화
        killer_dict[id] = "" # 모든 id에 대해 신고한 사람을 공백("")으로 초기화
    
    # report_freq_dict와 killer_dict 채우는 작업
    for r in report: 
        reported_id = r.split()[-1] # 신고당한 id
        report_freq_dict[reported_id] += 1 # freq 1 추가
        killer_dict[reported_id] += f"{r.split()[0]} " # 그 사람을 신고한 목록에 추가 (공백으로 구분)
            
    # report_freq_dict에서 k보다 신고횟수가 적은 id는 지워버림
    report_freq_dict_copy = report_freq_dict.copy()
    for key in report_freq_dict_copy:
        if report_freq_dict[key] < k:
            del report_freq_dict[key]
    # 이제 report_freq_dict에서 남은 id는 정지될 운명의 id들임...

    # killer_dict애 있는 정보를 이용해 정지될 id를 신고한 사용자에게 메일 발송
    for stop_id in report_freq_dict:
        # killer 리스트는 stop_id를 신고한 사람들의 리스트
        killer = killer_dict[stop_id].split()
        
        # killer 리스트를 돌면서 메일 발송 (발송 시 count)
        for id in killer:
            idx = id_list.index(id)
            answer[id_list.index(id)] += 1 # 메일 발송 시 count
    
    return answer