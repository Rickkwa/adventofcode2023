# def split_segment(a_start, a_duration, b_start, b_duration):
#     result = {"before": [], "after": []}
#     a_end = a_start + a_duration - 1
#     b_end = b_start + b_duration - 1
#     # print(a_start, a_end, b_start, b_end)

#     if a_start < b_start:
#         before_segment = (a_start, b_start - a_start)
#         result["before"].append(before_segment)
#     elif a_start < b_start + b_duration - 1:
#         after_segment = (b_start + b_duration - 1, )
#         result["after"].append(after_segment)
#     return result



# print("===========  Test 1 =========== ")
# print(split_segment(5, 10, 8, 10))
# print("===========  Test 1 reverse =========== ")
# print(split_segment(8, 10, 5, 10))
# print("===========  Test 2 =========== ")
# print(split_segment(5, 10, 7, 4))
# print("===========  Test 2 reverse =========== ")
# print(split_segment(7, 4, 5, 10))

def check_overlap(a_start, a_duration, b_start, b_duration):
    """ Return tuple (overlap_start, overlap_duration) or False if no overlap """
    if a_start > b_start:
        a_start, b_start = b_start, a_start
        a_duration, b_duration = b_duration, a_duration
    a_end = a_start + a_duration - 1
    b_end = b_start + b_duration - 1
    # print(a_start, a_end, b_start, b_end)
    if b_start <= a_end and b_end >= a_end and a_start <= b_start:
        # print("Case A")
        return (b_start, a_end - b_start + 1)
    elif b_start >= a_start and b_end <= a_end:
        # print("Case B")
        return (b_start, b_duration)
    return False


def split_segment(a_start, a_duration, overlap_start, overlap_duration):
    result = {"before": [], "after": []}
    a_end = a_start + a_duration - 1
    overlap_end = overlap_start + overlap_duration - 1

    if a_start < overlap_start:
        result["before"].append((a_start, overlap_start - a_start))
    if a_end > overlap_end:
        result["after"].append((overlap_end + 1, a_end - overlap_end))
    return result

print("=============================== Overlap ===============================")
print("===========  Test 1 =========== ")
print(check_overlap(5, 10, 8, 10))

print("===========  Test 2 =========== ")
print(check_overlap(5, 10, 7, 4))

print("===========  Test 3 =========== ")
print(check_overlap(9, 11, 8, 10))

print("=============================== Split ===============================")
print("===========  Test 1 =========== ")
print(split_segment(5, 10, 8, 7))

print("===========  Test 2 =========== ")
print(split_segment(5, 10, 7, 4))

print("===========  Test 3 =========== ")
print(split_segment(9, 11, 9, 9))


print ("================================= Other ==============================")
print("Overlap", check_overlap(8, 6, 8, 12))
print("Split", split_segment(8, 6, 8, 6))


"""
LEGEND:
    -----  Ranges
    $$$$$  Overlapping area of the 2 ranges




          01234567890
012345678911111111112
     ----------         # range start at 5; length of 10
        ----------      # range starts at 8; length of 10
        $$$$$$$         # overlapping area starts at 8; length of 7
012345678911111111112
          01234567890

check_overlap(5, 10, 8, 10)
    returns (8, 7)




          01234567890
012345678911111111112
     ----------
       ----    
       $$$$    
012345678911111111112
          01234567890

check_overlap(5, 10, 7, 4)
    returns (7, 4)



          01234567890
012345678911111111112
         -----------
        ----------
         $$$$$$$$$
012345678911111111112
          01234567890

check_overlap(9, 11, 8, 10)
    returns (9, 9)


False
check_overlap(5, 10, 20, 4)
"""
