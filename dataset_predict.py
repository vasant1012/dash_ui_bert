import config
import torch
import transformers


class Dataset:
    def __init__(self, texts):
        self.texts = texts
        self.tokenizer = transformers.BertTokenizer.from_pretrained(config.BASE_MODEL_PATH, do_lower_case=True)
        self.max_len = config.MAX_LEN

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, item):
        texts = str(self.texts[item])
        texts = " ".join(texts.split())
        inputs = self.tokenizer.encode_plus(
            texts,
            None,
            add_special_tokens=True,
            max_length=self.max_len,
            pad_to_max_length=True,
            truncation=True
        )

        ids = inputs["input_ids"]
        mask = inputs["attention_mask"]
        token_type_ids = inputs["token_type_ids"]
        return {
            "ids": torch.tensor(ids, dtype=torch.long),
            "mask": torch.tensor(mask, dtype=torch.long),
            "token_type_ids": torch.tensor(token_type_ids, dtype=torch.long)}