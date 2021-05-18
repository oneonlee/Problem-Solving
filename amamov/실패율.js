function solution(N, stages) {
    let result = {}
    const stageNums = [];
    
    for (let i=1; i < N+1; i++) {
        stageNums.push(i);
    }
    
    stageNums.forEach(curStage => {
        let loser = 0
        const all = stages.filter(s => {
            if (s === curStage) {
                loser ++;
            }
            return s >= curStage
        }).length;
        const failRatio = loser / all
        result[curStage] = failRatio
    })
    
    result = Object.keys(result).map((key) => {
        return [key, result[key]];
    });
    
    result.sort((first, second) => {
        return second[1] - first[1];
    });
    
    const answer = []
       
    return result.map(r => Number(r[0]));
}
