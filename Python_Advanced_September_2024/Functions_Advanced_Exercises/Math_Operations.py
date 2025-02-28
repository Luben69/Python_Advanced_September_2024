def math_operations(*args, **kwargs):
    for i in range(len(args)):
        if i % 4 == 0:
            kwargs["a"] += args[i]
        elif i % 4 == 1:
            kwargs["s"] -= args[i]
        elif i % 4 == 2:
            if args[i] != 0:
                kwargs["d"] /= args[i]
        elif i % 4 == 3:
            kwargs["m"] *= args[i]

    result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    return "\n".join(f"{key}: {value:.1f}"for key, value in result)
