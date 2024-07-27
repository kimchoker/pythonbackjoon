def calculate_outfit_cases(test_cases):
    results = []
    
    for case in test_cases:
        n = case[0]
        clothes = case[1]
        
        if n == 0:
            results.append(0)
            continue
        
        cloth_dict = {}
        
        for cloth, category in clothes:
            if category in cloth_dict:
                cloth_dict[category] += 1
            else:
                cloth_dict[category] = 1
        
        outfit_combinations = 1
        
        for category in cloth_dict:
            outfit_combinations *= (cloth_dict[category] + 1)
        
        results.append(outfit_combinations - 1)
    
    return results

# 입력받는 부분
def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    test_cases = []
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        clothes = []
        for _ in range(n):
            cloth, category = data[idx].split()
            clothes.append((cloth, category))
            idx += 1
        test_cases.append((n, clothes))
    
    results = calculate_outfit_cases(test_cases)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
