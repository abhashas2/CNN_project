from pathlib import Path

DATA_DIR = Path("data/raw/archive (1)/PetImages")

cat_dir = DATA_DIR / "Cat"
dog_dir = DATA_DIR / "Dog"

print("Dataset path:", DATA_DIR)
print("Cat folder exists:", cat_dir.exists())
print("Dog folder exists:", dog_dir.exists())

cat_images = list(cat_dir.glob("*.jpg"))
dog_images = list(dog_dir.glob("*.jpg"))

print("Number of Cat images:", len(cat_images))
print("Number of Dog images:", len(dog_images))