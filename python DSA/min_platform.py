def find_platforms_req(arrival_time,dep_time):
    arrival_time.sort()
    dep_time.sort()
    
    platform_needed = 1
    max_platform = 1
    
    i = 1
    j = 0
    
    while(i < len(arrival_time) and j < len(arrival_time)):
        if (arrival_time[i] <= dep_time[j]):
            platform_needed += 1
            i += 1
        elif (arrival_time[i] > dep_time[j]):
            platform_needed -= 1
            j += 1
        if platform_needed > max_platform:
            max_platform = platform_needed
    return max_platform

def main():
    arrival_time = list(map(int,input("Enter the arrival times: ").split()))
    dep_time = list(map(int,input("Enter the departure times: ").split()))
    output = find_platforms_req(arrival_time,dep_time)
    print("The maximum platforms required are: ",output)
    
main()