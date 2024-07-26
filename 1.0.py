import tkinter as tk

class ElectricFanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("電風扇遊戲")

        self.temperature = 25  # 初始溫度
        self.fan_speed = "低速"  # 初始風速

        self.create_widgets()

    def create_widgets(self):
        # 溫度標籤
        self.temperature_label = tk.Label(self.root, text=f"當前溫度：{self.temperature}°C", font=('Helvetica', 14))
        self.temperature_label.pack(pady=10)

        # 風速標籤
        self.speed_label = tk.Label(self.root, text=f"電風扇風速：{self.fan_speed}", font=('Helvetica', 14))
        self.speed_label.pack()

        # 升高溫度按鈕
        self.increase_button = tk.Button(self.root, text="升高溫度", command=self.increase_temperature, font=('Helvetica', 12))
        self.increase_button.pack(pady=20)

        # 降低溫度按鈕
        self.decrease_button = tk.Button(self.root, text="降低溫度", command=self.decrease_temperature, font=('Helvetica', 12))
        self.decrease_button.pack()

    def increase_temperature(self):
        self.temperature += 1
        self.adjust_fan_speed()
        self.update_display()

    def decrease_temperature(self):
        self.temperature -= 1
        self.adjust_fan_speed()
        self.update_display()

    def adjust_fan_speed(self):
        if self.temperature >= 30:
            self.fan_speed = "高速"
        elif self.temperature >= 25:
            self.fan_speed = "中速"
        else:
            self.fan_speed = "低速"

    def update_display(self):
        self.temperature_label.config(text=f"當前溫度：{self.temperature}°C")
        self.speed_label.config(text=f"電風扇風速：{self.fan_speed}")

def main():
    root = tk.Tk()
    app = ElectricFanGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
