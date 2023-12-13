import numpy as np
import math
import matplotlib.pyplot as plt
from schedule import scheduleMaker


def main():
    daily_ave_p = []
    total_p = []
    ts = []
    c_ss = []
    c_gs = []
    p_ts = []
    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    urgencylist = [0.96, 1.30, 0.88, 0.58, 0.85, 1.00, 0.71, 0.59, 1.25, 0.65, 0.72, 0.69, 0.95, 0.44, 1.10, 0.48, 1.22,
                   1.29, 0.45, 1.03, 0.99, 0.68, 0.55, 0.94, 0.75, 0.57, 0.69, 1.06, 0.63, 0.93, 1.17, 0.70, 0.75, 0.53,
                   1.01, 1.44, 0.67, 0.54, 1.07, 0.91, 1.24, 1.33, 1.15, 1.03, 1.21, 1.13, 0.44, 1.45, 0.45, 0.82, 1.16,
                   0.86, 0.85, 1.11, 0.71, 0.61, 1.50, 1.30, 0.95, 0.52, 0.93, 1.34, 1.11, 0.83, 1.49, 0.95, 0.94, 0.54,
                   0.47, 0.91, 1.33, 0.79, 1.50, 1.22, 1.45, 0.44, 1.14, 0.67, 0.61, 0.57, 1.24, 0.62, 0.75, 1.49, 0.59,
                   0.86, 1.44, 0.42, 0.74, 1.05, 1.50, 0.53, 0.67, 0.41, 0.43, 0.77, 1.02, 0.46, 0.95, 0.73, 1.21, 1.23,
                   0.98, 0.88, 0.66, 1.17, 1.42, 1.15, 1.48, 0.91, 0.86, 1.18, 1.12, 0.90, 1.37, 1.21, 1.04, 1.39, 0.47,
                   0.77, 0.56, 0.73, 0.61, 0.42, 0.90, 0.81, 0.48, 1.27, 0.95, 0.57, 1.12, 1.02, 0.97, 1.13, 1.10, 1.50,
                   0.74, 1.46, 0.80, 0.58, 0.82, 0.50, 0.68, 1.02, 1.47, 1.31, 0.95, 1.41, 0.86, 1.22, 0.49, 1.24, 0.91,
                   0.40, 0.58, 0.69, 1.37, 1.38, 1.24, 0.98, 0.62, 0.51, 0.73, 0.85, 0.56, 1.10, 0.91, 1.30, 0.68, 1.47,
                   0.76, 1.05, 1.15, 0.73, 0.56, 0.52, 0.41, 0.41, 0.85, 1.20, 1.21, 1.39, 0.76, 1.10, 0.55, 1.17, 0.76,
                   1.30, 0.98, 1.45, 0.60, 1.35, 1.15, 0.50, 1.47, 1.00, 0.67, 1.02, 1.05, 1.07, 1.17, 0.46, 1.12, 0.59,
                   0.63, 0.76, 0.53, 1.05, 0.74, 0.76, 0.79, 0.89, 1.01, 0.97, 1.08, 1.01, 1.18, 0.41, 0.90, 0.51, 0.60,
                   1.36, 1.05, 0.65, 0.68, 1.44, 1.34, 1.05, 0.41, 1.15, 1.26, 0.65, 1.46, 1.47, 1.23, 0.60, 1.01, 1.28,
                   0.41, 0.56, 0.84, 1.21, 0.81, 0.71, 1.31, 1.48, 0.60, 0.67, 1.40, 0.44, 0.59, 1.03, 1.28, 1.01, 0.78,
                   1.09, 1.35, 0.51, 0.63, 0.91, 1.39, 1.44, 0.70, 0.57, 0.77, 0.97, 1.41, 1.37, 0.92, 0.44, 0.99, 1.34,
                   0.97, 0.87, 1.03, 0.59, 1.00, 0.63, 1.13, 1.41, 0.88, 1.12, 0.45, 0.95, 0.53, 1.42, 1.26, 1.44, 1.07,
                   0.45, 0.90, 0.78, 1.05, 0.60, 0.51, 1.27, 1.24, 0.58, 0.92, 1.34, 1.25, 0.54, 0.74, 0.49, 1.30, 0.85,
                   0.46, 0.53, 0.68, 0.86, 0.81, 0.88, 1.04, 0.74, 0.83, 0.70, 0.71, 1.13, 0.61, 0.76, 1.50, 0.73, 0.83,
                   0.50, 0.62, 1.09, 0.74, 0.56, 1.05, 0.63, 1.33, 1.20, 1.21, 1.18, 0.55, 0.60]
    # Start Time (in hours)
    t = t_start = 0
    # End Time (in hours)
    t_end = 336
    # Step Size
    step = 0.01
    # Number of Steps
    n = int(round(t_end - t_start) / step)

    ###Initial Conditions###
    # Space Crew
    c_s = 20.39
    # Ground Crew
    c_g = 20.39
    # Productivity
    p_t = 1

    c_ss.append(c_s)
    c_gs.append(c_g)
    p_ts.append(p_t)
    ts.append(t)

    # Schedule Creation
    sleep = 12
    work2 = 5
    relax = 4
    exercise = 3
    schedule = scheduleMaker(sleep, work2, relax, exercise, step)
    sleep = schedule[0]
    work = schedule[1]
    relax = schedule[2]
    exercise = schedule[3]

    m = 0

    switch_list = []
    sw = 0
    for i in range(int(work2 / step)):
        switch_list.append(round(sw, 4))
        if i < .5 * (work2 / step):
            sw += 1 * step
            if sw > 1:
                sw = 1
        if i > .5 * (work2 / step):
            sw -= .1 * step
            if sw < 0:
                sw = 0

    # Team Building On/Off Switch
    teamwork = False

    # Population
    p = 7
    ul = 0
    sw = 0
    for i in range(n):
        if (i + 1) % (1 / step) == 0:
            ul += 1
        if sw >= len(switch_list):
            sw = 0
        # Magnitude
        limiter = 100
        # Urgency
        u = urgencylist[ul - 1]
        # Sleep
        s = sleep[m]
        print(s)
        # Relaxation
        r = relax[m]
        # Exercise
        e = exercise[m]
        # Stress Reduction Caused by Brain
        z = 1 / limiter
        # Work
        w = w_g = work[m]
        # Crew Interaction
        b = 0
        # Flight
        d = 0
        # Training
        tr = 0
        # 24 Hour Time
        t_module = t % 24
        # Natural Return to Average
        weight = .3
        # Productivity On/Off Switch
        switch = 0
        m += 1
        if m > 2399:
            m = 0

    # Interaction Change
    if t > 39 and not teamwork:
        b = .25 / limiter
        b = b - 17.5 / limiter * step
    if b < -1 / limiter:
        b = -1 / limiter
    if t > 39 and teamwork:
        b = .25 / limiter
        b = b - 20 / limiter * step
    if b < -1 / limiter:
        b = -1 / limiter
    if t > 39 and t < 168:
        tr = .1 / limiter

    # Initial Flight
    if t <= 39:
        d = 2.16 / limiter
        w_g = 0

    # Population Change
    if t > 39:
        w_g = w
        p = p + 1.1 * step
    if p > 14:
        p = 14
    ##########################

    ### Equations ###
    dc_s_dt = b * (c_s * c_g) + u * (w / p) + (-s - r + e - z + tr) * c_s - ((c_s - 20.39) / 7.74) * weight
    dc_g_dt = b * (c_s * c_g) + u * (w_g / p) + (-s - r + e + d - z) * c_g - ((c_g - 20.39) / 7.74) * weight
    p_t = math.exp(-(((((c_s + c_g) / 2) - 20.39) ** 2) / (2 * 7.74 ** 2))) * switch
    #################

    ### Euler's Method ###
    c_s = c_s + step * dc_s_dt
    c_g = c_g + step * dc_g_dt
    ######################

    # Crew Stress Convergence
    if t > 168 and np.abs(c_g - c_s) < .001:
        c_g = c_s

    t = step * (i + 1)
    total_p.append(p_t)
    if t % 24 == 0:
        daily_ave_p.append(sum(total_p) / len(total_p))
        total_p = []
    c_ss.append(c_s)
    c_gs.append(c_g)
    p_ts.append(p_t)
    ts.append(t)
    print(c_s)

    ave_stress = (sum(c_ss) + sum(c_gs)) / (2 * len(c_ss))
    ave_productivity = (sum(p_ts)) / (len(p_ts))
    # print(f"\t Schedule\n Sleep: {sleep}\n Work: {work}\n Relaxation: {relax}\n Exercise: {exercise}\n")
    # print(f"\t Averages\n Average Stress: {ave_stress}\n Average Productivity: {ave_productivity} \n")
    # print()
    # print("####################################################################################### \n")
    # print()
    x = [sleep, work, relax, exercise, ave_stress, ave_productivity]

    plt.style.use('seaborn-v0_8-darkgrid')
    # plt.subplot(1,2,1)
    plt.plot(ts, c_gs, label="Ground Crew")
    plt.plot(ts, c_ss, label="Space Crew")

    plt.title("Stress Level")
    plt.xlabel('Time (hours)')
    plt.ylabel('Cortisol (nmol/L)')
    plt.legend()

    plt.show()

    return x


if __name__ == "__main__":
    main()