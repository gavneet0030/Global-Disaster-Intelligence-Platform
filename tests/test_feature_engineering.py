from app.pipelines.etl_pipeline import ETLPipeline
from app.ai.feature_engineering import FeatureEngineering


pipeline = ETLPipeline.run()

events = pipeline["unique_events"]

features = FeatureEngineering.transform(events)

print("=" * 60)

print("Total Events :", len(features))

print("=" * 60)

for event in features[:10]:

    print(event)