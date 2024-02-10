from openai import OpenAI

client = OpenAI(api_key="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")




def sum_gen(audio_path):
    audio_file = open(audio_path, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="json",  # only json supported by Python
        language="en",
    )
    return meeting_minutes(transcription)

def abstract_summary_extraction(transcription):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content":  "this is the transcript of the conversation between a patient and doctor and i want to extract the specific data from it and the specific data has to include the reason for the patient to visit , Blood pressure of the patient , Body temp of the patient and the medical advice given by a doctor to the patient."

            },
            {
                "role": "user",
                "content": transcription.dict()['text']
            }
        ]
    )
    return response.choices[0].message.content

def bp_extraction(transcription):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content":  "this is the transcript of the conversation between a patient and doctor and i want  you to extract the  Blood pressure of the patient be as brief as possible"

            },
            {
                "role": "user",
                "content": transcription.dict()['text']
            }
        ]
    )
    return response.choices[0].message.content

def reason_extraction(transcription):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content":  "this is the transcript of the conversation between a patient and doctor and i want  you to extract the  reason for the patient visit be as brief as possible"

            },
            {
                "role": "user",
                "content": transcription.dict()['text']
            }
        ]
    )
    return response.choices[0].message.content

def temp_extraction(transcription):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content":  "this is the transcript of the conversation between a patient and doctor and i want  you to extract the  body temperature of the patient be as brief as possible"

            },
            {
                "role": "user",
                "content": transcription.dict()['text']
            }
        ]
    )
    return response.choices[0].message.content

def advice_extraction(transcription):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content":  "this is the transcript of the conversation between a patient and doctor and i want  you to extract the  medical advice given by the doctor"

            },
            {
                "role": "user",
                "content": transcription.dict()['text']
            }
        ]
    )
    return response.choices[0].message.content

def medicine_extraction(transcription):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content":  "this is the transcript of the conversation between a patient and doctor and i want  you to extract the  medicines given by the doctor, be as brief as possible"

            },
            {
                "role": "user",
                "content": transcription.dict()['text']
            }
        ]
    )
    return response.choices[0].message.content

def meeting_minutes(transcription):
    abstract_summary = abstract_summary_extraction(transcription)
    bp = bp_extraction(transcription)
    reason = reason_extraction(transcription)
    temp = temp_extraction(transcription)
    advice = advice_extraction(transcription)
    medicine = medicine_extraction(transcription)

    return {
        'bp' : bp,
        'reason' : reason,
        'temp' : temp,
        'advice' : advice,
        'medicine' : medicine
    }

