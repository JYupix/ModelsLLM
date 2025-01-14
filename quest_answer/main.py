from transformers import pipeline

model_name = "deepset/roberta-base-squad2"
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

def get_answer(question, context):
    QA_input = {
        'question': question,
        'context': context
    }
    result = nlp(QA_input)
    return result['answer']