
import argparse

def main():
    parser = argparse.ArgumentParser(description='Locate my stuff')
    parser.add_argument('category', help='Category to search')
    parser.add_argument('item', help='Item to locate')

