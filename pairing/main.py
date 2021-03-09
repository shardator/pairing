import math


def improved_i_sqrt(n):
    assert n >= 0
    if n == 0:
        return 0
    i = n.bit_length() >> 1    # i = floor( (1 + floor(log_2(n))) / 2 )
    m = 1 << i    # m = 2^i
    #
    # Fact: (2^(i + 1))^2 > n, so m has at least as many bits
    # as the floor of the square root of n.
    #
    # Proof: (2^(i+1))^2 = 2^(2i + 2) >= 2^(floor(log_2(n)) + 2)
    # >= 2^(ceil(log_2(n) + 1) >= 2^(log_2(n) + 1) > 2^(log_2(n)) = n. QED.
    #
    while (m << i) > n: # (m<<i) = m*(2^i) = m*m
        m >>= 1
        i -= 1
    d = n - (m << i) # d = n-m^2
    for k in range(i-1, -1, -1):
        j = 1 << k
        new_diff = d - (((m<<1) | j) << k) # n-(m+2^k)^2 = n-m^2-2*m*2^k-2^(2k)
        if new_diff >= 0:
            d = new_diff
            m |= j
    return m


def pair(k1, k2, safe=True):
    """
    Cantor pairing function
    http://en.wikipedia.org/wiki/Pairing_function#Cantor_pairing_function
    """
    z = (k1 + k2) * (k1 + k2 + 1) // 2 + k2
    if safe and (k1, k2) != depair(z):
        raise ValueError("{} and {} cannot be paired".format(k1, k2))
    return z


def depair(z):
    """
    Inverse of Cantor pairing function
    http://en.wikipedia.org/wiki/Pairing_function#Inverting_the_Cantor_pairing_function
    """
    w = (improved_i_sqrt(8 * z + 1) - 1)//2
    t = (w**2 + w) // 2
    y = z - t
    x = w - y
    # assert z != pair(x, y, safe=False):
    return x, y
