import matplotlib.pyplot as plt

g0 = 9.81
R = 6371000


def gravitational_acc(h):
    return g0 * (R / (R + h)) ** 2


def euler_method(m, h0, v0=0, dt=0.01, t_max=100, k=0.1):
    """
       Simulates the motion of a falling body under the influence of gravity and drag.

       Parameters:
       m: Mass of the falling body (kg)
       h0: Initial height (m)
       v0: Initial velocity (m/s)
       dt: Time step for integration (s)
       t_max: Maximum time to simulate (s)
       k: Damping coefficient (kg/m)

       Returns:
       time_list (list): List of time values
       height_list (list): List of height values
       velocity_list (list): List of velocity values
    """
    t = 0
    h = h0
    v = v0

    time_list = [t]
    height_list = [h]
    velocity_list = [v]

    while t < t_max and h > 0:
        g = gravitational_acc(h)
        a = g - (k / m * v ** 2)

        print(f"Time: {t:.2f} s")
        print(f"Gravitational acceleration: {g:.4f} m/s^2")
        print(f"Acceleration: {a:.4f} m/s^2")
        print(f"Height: {h:.2f} m")
        print(f"Velocity (using v): {v:.4f} m/s")
        velocity_from_height = (h - height_list[-1]) / dt
        print(f"Velocity (using dh/dt): {velocity_from_height:.4f} m/s\n")

        v = v + a * dt
        h = h + v * dt

        if h < 0:
            h = 0

        t += dt
        time_list.append(t)
        height_list.append(h)
        velocity_list.append(v)

    return time_list, height_list, velocity_list


def euler_richardson(m, h0, v0=0, dt=0.01, t_max=100, k=0.1):
    """
       Euler-Richardson method for constant acceleration and without drag.
    """
    t = 0
    h = h0
    v = v0

    time_list = [t]
    height_list = [h]
    velocity_list = [v]

    while t < t_max and h > 0:
        g = gravitational_acc(h)
        a = g - (k / m * v ** 2)

        v_half = v + 0.5 * a * dt
        h_half = h + 0.5 * v * dt

        g_half = gravitational_acc(h_half)
        a_half = g_half - (k / m * v_half ** 2)

        v = v + a_half * dt
        h = h + v_half * dt
        t += dt

        time_list.append(t)
        height_list.append(h)
        velocity_list.append(v)

    return time_list, height_list, velocity_list


h0 = float(input("Input Height (m): "))
k = float(input("Input Damping Coeff (kg/s): "))
m = float(input("Input Mass (kg): "))

time_list, height_list, velocity_list = euler_method(m, h0, k=k)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(time_list, height_list, label="Height (m)", color="blue")
plt.title('Height vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(time_list, velocity_list, label="Velocity (m/s)", color="red")
plt.title('Velocity vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.grid(True)

plt.tight_layout()
plt.show()
