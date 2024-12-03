# 计时记录
import time
import os
time_start=time.time()
start_time_str = time.strftime("%Y%m%d_%H%M%S", time.localtime(time_start))

time.sleep(3)
time_stop=time.time()

print(f"Time used: {time_stop-time_start} seconds.")#输出时间到本地文件
script_name = os.path.basename(__file__).split('.')[0]
file_name = f"{start_time_str}_{script_name}.txt"

duration = time_stop - time_start

with open(file_name, 'w') as f:
    f.write(f"开始时间: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_start))}\n")
    f.write(f"停止时间: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_stop))}\n")
    f.write(f"运行时长: {duration:.2f} 秒\n")

print(f"Time used: {time_stop-time_start} seconds.")
