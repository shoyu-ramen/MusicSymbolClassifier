import argparse
import os

from datasets.Dataset import Dataset


class MuscimaPlusPlusDatasetDownloader(Dataset):
    """ Downloads the Muscima++ dataset """

    def __init__(self, destination_directory: str):
        """
        Create and initializes a new dataset.
        :param destination_directory: The root directory, into which the data will be copied.
        """
        super().__init__(destination_directory)

    def get_dataset_download_url(self) -> str:
        return "https://ufal.mff.cuni.cz/~hajicj/2017/docs/MUSCIMA-pp_v0.9.zip"

    def get_dataset_filename(self) -> str:
        return "MUSCIMA-pp_v0.9.zip"

    def download_and_extract_dataset(self):
        if not os.path.exists(self.get_dataset_filename()):
            print("Downloading MUSCIMA++ Dataset...")
            self.download_file(self.get_dataset_download_url(), self.get_dataset_filename())

        print("Extracting MUSCIMA++ Dataset...")
        self.extract_dataset(self.destination_directory)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dataset_directory",
        type=str,
        default="../data/muscima_pp_raw",
        help="The directory, where the extracted dataset will be copied to")

    flags, unparsed = parser.parse_known_args()

    dataset = MuscimaPlusPlusDatasetDownloader(flags.dataset_directory)
    dataset.download_and_extract_dataset()
