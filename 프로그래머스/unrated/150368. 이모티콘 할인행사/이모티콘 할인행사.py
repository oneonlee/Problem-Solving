import itertools
def solution(users, emoticons):
    discounts_list = list(itertools.product([10, 20, 30, 40], repeat=len(emoticons)))
    
    final_subscribers = 0
    final_sales_amount = 0
    for discounts in discounts_list:
        subscribers = 0
        sales_amount = 0
        
        for user_idx in range(len(users)):
            ratio_threshold = users[user_idx][0]
            price_threshold = users[user_idx][1]

            purchase_list = []
            total_price = 0
            for emo_idx in range(len(emoticons)):
                percentage = discounts[emo_idx]
                price = emoticons[emo_idx]*(1-percentage/100)
                
                if percentage>=ratio_threshold:
                    purchase_list.append(emo_idx)
                    total_price+=price
            
            if total_price>=price_threshold:
                # purchase_list = [] # 생략 가능 (?)
                total_price = 0
                subscribers += 1
            
            sales_amount += total_price
            
        if subscribers > final_subscribers:
            final_subscribers = subscribers
            final_sales_amount = sales_amount
            # final_case = discounts
        elif subscribers == final_subscribers:
            if sales_amount > final_sales_amount:
                final_sales_amount = sales_amount
                # final_case = discounts
                
    # print(final_case)
        
    answer = [final_subscribers, final_sales_amount]
    return answer