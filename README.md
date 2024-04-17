# fms_cognizant_skill_safari
feedback management system


sample data, that will be used for model training
<img width="700"  alt="image" src="https://github.com/redR0b0t/fms_cognizant/assets/143605527/9a7d9330-299c-4226-863e-3af32d834cc4">


finetuning flan-t5-xl model to learn from the sample data:
```python3
python "./itp/finetune_seq2seq.py" \
        --model_name_or_path $model_path \
        --resume_from_checkpoint $checkpoint_path \
        --bf16 True \
        --train_file $train_file \
        --per_device_train_batch_size 2 \
        --per_device_eval_batch_size 2 \
        --gradient_accumulation_steps 1 \
        --do_train \
        --learning_rate 1.0e-6 \
        --warmup_ratio 0.03 \
        --weight_decay 0.0 \
        --num_train_epochs 1 \
        --logging_steps 10 \
        --save_steps 100 \
        --save_total_limit 2 \
        --overwrite_output_dir \
        --output_dir $output_dir \
        --peft lora
```

Generating responses from the finetune model and uploading to firestore:
...
