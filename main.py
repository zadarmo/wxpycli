import os
import argparse
import shutil

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='wx-cli',
        description='description',
    )
    parser.add_argument('starter')  # starter name
    parser.add_argument('-o', '--output', default='./')  # output path

    args = parser.parse_args()
    src = f'./starter/{args.starter}'
    dst = f'{args.output}/{args.starter}'
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
