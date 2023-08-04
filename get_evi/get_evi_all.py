from tqdm import tqdm
import os
import shutil
import json
from importlib import import_module


def main():
    # target_dir = "evi"

    # shutil.rmtree(target_dir)
    # os.mkdir(target_dir)

    with open("evi_name_list.json") as evi_name_list_file:
        evi_name_list = json.load(evi_name_list_file)
        pbar = tqdm(range(len(evi_name_list)), desc="get_evi", ncols=80)

        for evi_name in evi_name_list:
            module = import_module("app." + evi_name)
            module.main()
            pbar.update(1)

    pbar.close()


if __name__ == "__main__":
    main()
