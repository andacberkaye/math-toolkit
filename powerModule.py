def power(base, exponent):
    result = 1
    count = 0
    while count < int(exponent):
        result = result * base
        count = count + 1
    if exponent != int(exponent):
        frac = exponent - int(exponent)
        step = 0.0001
        while power_approx(result, base, step) < frac:
            result *= base ** step
        return result
    return result


def power_approx(result, base, step):
    count = 0.0
    temp = result
    while temp < result * base:
        temp *= base ** step
        count += step
    return count