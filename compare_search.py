import timeit


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def boyer_moore_search(text, pattern):
  shift_table = build_shift_table(pattern)
  i = 0 

  while i <= len(text) - len(pattern):
    j = len(pattern) - 1

    while j >= 0 and text[i + j] == pattern[j]:
      j -= 1

    if j < 0:
      return i

    i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

  return -1


def build_shift_table(pattern):
    table = {}
    length = len(pattern)

    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1

    table.setdefault(pattern[-1], length)

    return table

def rabin_karp_search(main_string, substring):
    substring_length = len(substring)
    main_string_length = len(main_string)
    
    base = 256 
    modulus = 101  
    
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    
    h_multiplier = pow(base, substring_length - 1) % modulus
    
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1

def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0

    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus

    return hash_value


art_1 = read_file("article_1.txt")
existed_sub_str_1 = " Вони прості "

art_2 = read_file("article_2.txt")
existed_sub_str_2 = "максимальна кількість"

not_existed_sub_str = "Спробуй знайти це"

kmp_t_1  = timeit.timeit(lambda: kmp_search(art_1, existed_sub_str_1), number=1)
bm_t_1  = timeit.timeit(lambda: boyer_moore_search(art_1, existed_sub_str_1), number=1)
rk_t_1  = timeit.timeit(lambda: rabin_karp_search(art_1, existed_sub_str_1), number=1)

kmp_t_1_n  = timeit.timeit(lambda: kmp_search(art_1, not_existed_sub_str), number=1)
bm_t_1_n  = timeit.timeit(lambda: boyer_moore_search(art_1, not_existed_sub_str), number=1)
rk_t_1_n  = timeit.timeit(lambda: rabin_karp_search(art_1, not_existed_sub_str), number=1)

kmp_t_2  = timeit.timeit(lambda: kmp_search(art_2, existed_sub_str_2), number=1)
bm_t_2  = timeit.timeit(lambda: boyer_moore_search(art_2, existed_sub_str_2), number=1)
rk_t_2  = timeit.timeit(lambda: rabin_karp_search(art_2, existed_sub_str_2), number=1)

kmp_t_2_n  = timeit.timeit(lambda: kmp_search(art_2, not_existed_sub_str), number=1)
bm_t_2_n  = timeit.timeit(lambda: boyer_moore_search(art_2, not_existed_sub_str), number=1)
rk_t_2_n  = timeit.timeit(lambda: rabin_karp_search(art_2, not_existed_sub_str), number=1)

print(f'Time for seaching existed substring in article #1: kmp_time: {kmp_t_1:.6f} | bm_time: {bm_t_1:.6f} | rk_time: {rk_t_1:.6f}')
print(f'Time for seaching not existed substring in article #1: kmp_time: {kmp_t_1_n:.6f} | bm_time: {bm_t_1_n:.6f} | rk_time: {rk_t_1_n:.6f}')
print('-' * 100)
print(f'Time for seaching existed substring in article #2: kmp_time: {kmp_t_2:.6f} | bm_time: {bm_t_2:.6f} | rk_time: {rk_t_2:.6f}')
print(f'Time for seaching not existed substring in article #2: kmp_time: {kmp_t_2_n:.6f} | bm_time: {bm_t_2_n:.6f} | rk_time: {rk_t_2_n:.6f}')
