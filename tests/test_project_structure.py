from app.core.monitoring.metrics import SystemMetrics

from app.core.monitoring.timer import Timer


def main():

    with Timer():

        SystemMetrics.report()


if __name__ == "__main__":

    main()