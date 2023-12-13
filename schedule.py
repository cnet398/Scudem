def scheduleMaker(sleep, work, relax, exercise, step):
    s = [0] * int(24 / step)
    r = [0] * int(24 / step)
    w = [0] * int(24 / step)
    e = [0] * int(24 / step)

    s1 = 0
    r1 = 0
    w1 = 0
    e1 = 0

    for i in range(len(s)):
        if i < sleep / step:
            if i < .2 * (sleep / step):
                s1 += 1 * step

            if s1 > .91:
                s1 = .91

            if i > .8 * (sleep / step):
                s1 -= 1 * step

            if s1 < 0:
                s1 = 0
            s[i] = round(s1, 3)

        if i >= sleep / step and i < (sleep + work) / step:
            if i < ((sleep + .2 * work) / step):
                w1 += 250 * step

            if w1 > 250:
                w1 = 250

            if i > ((sleep + .8 * work) / step):
                w1 -= 250 * step

            if w1 < 0:
                w1 = 0
            w[i] = round(w1, 3)

        if i >= (sleep + work) / step and i < (sleep + work + relax) / step:
            if i < ((sleep + work + .2 * relax) / step):
                r1 += 5 * step

            if r1 > 5:
                r1 = 5

            if i > ((sleep + work + .8 * relax) / step):
                r1 -= 5 * step

            if r1 < 0:
                r1 = 0
            r[i] = round(r1, 3)

        if i > (sleep + work + relax) / step:
            if i < ((sleep + work + relax + .2 * exercise) / step):
                e1 += .8 * step

            if e1 > .8:
                e1 = .8

            if i > ((sleep + work + relax + .8 * exercise) / step):
                e1 -= .8 * step

            if e1 < 0:
                e1 = 0
            e[i] = round(e1, 3)

    return [s, w, r, e]
