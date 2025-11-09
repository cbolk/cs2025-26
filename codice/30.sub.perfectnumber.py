SEP = ","

def is_perfect(n):
    if n >= 2:
      aliquot_sum = 1

      halfplus1 = n // 2 + 1
      for i in range(2, halfplus1):
          if n % i == 0:
              aliquot_sum += i
      return aliquot_sum == n

    # this is the anomaly, handled at the end
    return False


# MAIN FLOW
in_seq = input("input: ")
in_values = in_seq.split(SEP)
perfect_nums = []
tot = 0
size = 0
for x in in_values:
    int_x = int(x)
    if is_perfect(int_x):
        perfect_nums.append(int_x)
        tot += int_x
        size += 1

avg = tot / size
print("Average:", avg)
