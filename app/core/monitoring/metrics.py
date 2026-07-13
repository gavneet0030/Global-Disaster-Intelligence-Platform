import psutil

import platform


class SystemMetrics:

    @staticmethod
    def report():

        print("=" * 60)

        print("SYSTEM METRICS")

        print("=" * 60)

        print()

        print("CPU Usage :", psutil.cpu_percent(), "%")

        print("RAM Usage :", psutil.virtual_memory().percent, "%")

        print("Python :", platform.python_version())

        print("OS :", platform.system())