import pandas as pd
import librosa


class AudioDataLoader:
    def load_from_df(self, df: pd.DataFrame):
        for i in range(len(df)):
            print(df.iloc[i]["slice_file_name"])
