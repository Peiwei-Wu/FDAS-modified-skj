"""复用原预训练掩码，从原始FLARE CT生成截断、标准化后的浮点图像。"""

import argparse
from pathlib import Path
import shutil

import cv2
import h5py
import numpy as np
import SimpleITK as sitk
from tqdm import tqdm


def process_images(source_dir, raw_root, output_dir):
    names = (source_dir / "train_slices.list").read_text().splitlines()
    cases = {}
    for name in names:
        case, index = Path(name).stem.rsplit("_slice", 1)
        cases.setdefault(case, []).append((name, int(index)))
    raw_paths = {f"{p.parent.name}_{p.name.removesuffix('_0000.nii.gz')}": p
                 for p in raw_root.rglob("*_0000.nii.gz")}
    data_dir = output_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    for case, slices in tqdm(cases.items(), desc="FLARE CT standardization"):
        volume = sitk.GetArrayFromImage(sitk.ReadImage(str(raw_paths[case])))
        for name, index in slices:
            image = volume[index].astype(np.float32)
            np.clip(image, -928.0, 692.0, out=image)
            image -= -3.34828877
            image /= 173.19928077357244
            image = cv2.resize(image, (256, 256), interpolation=cv2.INTER_LINEAR)
            with h5py.File(source_dir / "data" / name, "r") as source:
                masks = source["masks"][:]
            with h5py.File(data_dir / name, "w") as output:
                output.create_dataset("image", data=image, compression="gzip")
                output.create_dataset("masks", data=masks, compression="gzip")
        del volume
    shutil.copyfile(source_dir / "train_slices.list", output_dir / "train_slices.list")
    print(f"Saved {len(names)} slices to {output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source_dir", type=Path, default=Path("outputs/FLARE_pre_processed_masks"))
    parser.add_argument("--raw_root", type=Path, default=Path("/mnt/e/PeiweiWu/datasets/FLARE"))
    parser.add_argument("--output_dir", type=Path, default=Path("outputs/FLARE_pre_processed_masks_v2"))
    args = parser.parse_args()
    process_images(args.source_dir, args.raw_root, args.output_dir)
