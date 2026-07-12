from app.pipelines.etl_pipeline import ETLPipeline


def main():

    result = ETLPipeline.run()

    print("=" * 50)

    print("NASA Events        :", len(result["nasa"]))

    print("Earthquake Events  :", len(result["earthquakes"]))

    print("Unique Events      :", len(result["unique_events"]))

    print("=" * 50)

    print("\nFirst Five Events\n")

    for event in result["unique_events"][:5]:

        print(event)


if __name__ == "__main__":

    main()