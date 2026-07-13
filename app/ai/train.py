from app.ai.train_model import ModelTrainer


def main():

    print("=" * 60)
    print("Global Disaster Intelligence Platform")
    print("Machine Learning Training")
    print("=" * 60)

    ModelTrainer.train()

    print("\nTraining Completed Successfully!")


if __name__ == "__main__":
    main()