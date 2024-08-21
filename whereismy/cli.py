import argparse


def main():
    parser = argparse.ArgumentParser(description="Locate my stuff")
    parser.add_argument("--version", action="store_true", help="Show version")
    parser.add_argument("--list", help="List all items", action="store_true")
    parser.add_argument("category", help="Category to search", nargs="?", default="*")
    parser.add_argument("item", help="Item to locate", nargs="?", default="*")

    args = parser.parse_args()

    if args.version:
        print("v1.0.0")
        exit(0)
    if args.list:
        print("Listing all items")
        exit(0)
    print(f"Locating {args.item} in {args.category}")
