import numpy as np
import pickle

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# -------------------- YOUR FAQS --------------------
faqs = """
PASTE YOUR COMPLETE FAQS STRING HERE
"""
# ---------------------------------------------------

tokenizer = Tokenizer()
tokenizer.fit_on_texts([faqs])

vocab_size = len(tokenizer.word_index) + 1

input_sequences = []

for sentence in faqs.split("\n"):
    tokenized_sentence = tokenizer.texts_to_sequences([sentence])[0]

    for i in range(1, len(tokenized_sentence)):
        input_sequences.append(tokenized_sentence[:i + 1])

max_len = max(len(x) for x in input_sequences)

padded_input_sequences = pad_sequences(
    input_sequences,
    maxlen=max_len,
    padding="pre"
)

x = padded_input_sequences[:, :-1]
y = padded_input_sequences[:, -1]

y = to_categorical(y, num_classes=vocab_size)

model = Sequential()

model.add(
    Embedding(
        input_dim=vocab_size,
        output_dim=100,
        input_length=max_len - 1
    )
)

model.add(LSTM(150))

model.add(Dense(vocab_size, activation="softmax"))

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(x, y, epochs=10)

# Save model
model.save("next_word_model.keras")

# Save tokenizer
with open("tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

# Save max length
with open("max_len.pkl", "wb") as f:
    pickle.dump(max_len, f)

print("Model Saved Successfully")