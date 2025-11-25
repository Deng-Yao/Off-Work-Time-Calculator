import tkinter as tk
from tkinter import ttk  # 引入ttk模块，让UI更好看
from datetime import datetime, timedelta

def calculate_off_duty_time():
    """
    核心计算函数，根据上班时间计算下班时间。
    """
    try:
        # 1. 获取用户选择的小时和分钟
        hour_str = hour_var.get()
        minute_str = minute_var.get()

        if not hour_str or not minute_str:
            result_var.set("错误：请选择完整的时间！")
            return

        hour = int(hour_str)
        minute = int(minute_str)

        # 2. 将输入时间转换为datetime对象
        clock_in_time = datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)

        # 3. 定义标准上班和下班时间
        standard_clock_in = clock_in_time.replace(hour=8, minute=30, second=0, microsecond=0)
        standard_off_duty = clock_in_time.replace(hour=17, minute=45, second=0, microsecond=0)
        
        # 4. 定义弹性打卡最晚时间
        latest_flexible_in = clock_in_time.replace(hour=9, minute=30, second=0, microsecond=0)

        # 输入校验：打卡时间不能晚于弹性时间上限
        if clock_in_time > latest_flexible_in:
            result_var.set("警告：打卡时间已超过9:30！")
            return

        # 5. 计算逻辑
        # 总工作时长为9小时15分钟
        work_duration = timedelta(hours=9, minutes=15)
        
        # 计划下班时间 = 打卡时间 + 工作时长
        calculated_off_duty = clock_in_time + work_duration

        # 最终下班时间取“计算下班时间”和“标准下班时间”中较晚的那个
        final_off_duty_time = max(calculated_off_duty, standard_off_duty)

        # 6. 格式化并显示结果
        result_var.set(f"计算结果：\n您的下班时间应为 {final_off_duty_time.strftime('%H:%M')} 后")

    except ValueError:
        result_var.set("错误：请输入有效的时间！")
    except Exception as e:
        result_var.set(f"发生未知错误: {e}")

# --- GUI 界面设置 ---

# 创建主窗口
root = tk.Tk()
root.title("下班时间计算器 @DENG Yao")
root.geometry("400x300") # 设置窗口大小
root.resizable(False, False) # 禁止调整窗口大小

# 使用ttk美化样式
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12, "bold"))
style.configure("TCombobox", font=("Helvetica", 12))

# 创建一个主框架
main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(expand=True, fill=tk.BOTH)

# 提示标签
prompt_label = ttk.Label(main_frame, text="请选择您的上班打卡时间：")
prompt_label.pack(pady=10)

# 时间选择框架
time_selection_frame = ttk.Frame(main_frame)
time_selection_frame.pack(pady=5)

# 小时选择
hour_var = tk.StringVar()
hour_options = [f"{h:02d}" for h in range(8, 10)] # 弹性时间为8点和9点
hour_combobox = ttk.Combobox(time_selection_frame, textvariable=hour_var, values=hour_options, width=5, state="readonly")
hour_combobox.pack(side=tk.LEFT, padx=5)
hour_combobox.set("08") # 默认值

# 时间分隔符
time_separator_label = ttk.Label(time_selection_frame, text=":")
time_separator_label.pack(side=tk.LEFT)

# 分钟选择
minute_var = tk.StringVar()
minute_options = [f"{m:02d}" for m in range(0, 60)]
minute_combobox = ttk.Combobox(time_selection_frame, textvariable=minute_var, values=minute_options, width=5, state="readonly")
minute_combobox.pack(side=tk.LEFT, padx=5)
minute_combobox.set("30") # 默认值

# 计算按钮
calculate_button = ttk.Button(main_frame, text="计算下班时间", command=calculate_off_duty_time)
calculate_button.pack(pady=20)

# 结果显示标签
result_var = tk.StringVar()
result_label = ttk.Label(main_frame, textvariable=result_var, font=("Helvetica", 14, "bold"), justify=tk.CENTER)
result_label.pack(pady=10)

# 启动主事件循环
root.mainloop()