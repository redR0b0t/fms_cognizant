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

# Backend Service
Generating responses from the finetune model and uploading to firestore:  <br>
<br>
Steps to run the backend service:<br>

```bash
git clone https://github.com/redR0b0t/fms_cognizant.git
cd fms_cognizant/cms_backend
python ./run_service.py
```
---------------Work In Progress----------------------------------------


# WebApp
<br>
Steps to run the webapp:<br>

```bash
git clone https://github.com/redR0b0t/fms_cognizant.git
cd fms_cognizant/cms_interface
flutter run -d web-server
```


<br>
Web UI for submitting feedback:  <br> 

![sc_ui_init](https://github.com/redR0b0t/fms_cognizant/assets/143605527/7c8fa90a-2102-46ba-9bfc-98239946eaf8)


<br>
The feedback being processed by the python backend service:  <br>

![sc_ui_processing](https://github.com/redR0b0t/fms_cognizant/assets/143605527/8b1fd639-747b-4b2e-945b-e89dca21fc46)


<br>
Data stored in Firestore Document uploaded by Web App:<br>

![image](https://github.com/redR0b0t/fms_cognizant/assets/143605527/467c6679-64f5-49a2-a59d-3c0b1e8114be)

