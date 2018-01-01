import argparse

def get_options():
    parser = argparse.ArgumentParser("BR's Web Playground")
    parser.add_argument('--test', action='store_true', default=False)
    parser.add_argument('--test-static', action='store_true', default=False)
    parser.add_argument('--export', action='store_true', default=False)
    parser.add_argument('--host', type=str)

    return parser.parse_args()
