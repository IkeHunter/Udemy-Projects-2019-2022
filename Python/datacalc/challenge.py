import time

print("For time(): {}".format(time.get_clock_info('time')))
print("For perf_counter(): {}".format(time.get_clock_info('perf_counter')))
print("For monotonic(): {}".format(time.get_clock_info('monotonic')))
print("For process_time(): {}".format(time.get_clock_info('process_time')))




