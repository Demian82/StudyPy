def find_median(a):
    sorted_a = sorted(a)
    median_num = (len(sorted_a) // 2)
    return sorted_a[median_num]