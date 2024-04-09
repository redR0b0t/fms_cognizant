pip install torch==2.1.2
pip install torchaudio==2.1.2
pip install pyctcdecode
pip install git+https://github.com/huggingface/transformers
pip install tqdm
pip install peft==0.9.0

# for kenlm bindings
pip install https://github.com/kpu/kenlm/archive/master.zip

# for indicTransTokenizer //restart kernel after this...
git clone https://github.com/VarunGumma/IndicTransTokenizer
pip install --editable ./IndicTransTokenizer/
pip install sacrebleu

# for listener
pip install firebase-admin

# for asr
pip install soundfile