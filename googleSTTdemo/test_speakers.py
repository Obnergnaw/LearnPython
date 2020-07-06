import re
import sys
from Mp.microphone import MicrophoneStream
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
from google.cloud.speech_v1 import types
import argparse

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

def listen_print_loop(responses):

    for response in responses:
        if not response.results:
            continue

        result = response.results[0]
        if not result.alternatives:
            continue

        if result.is_final:
            best_alternative = result.alternatives[0]
            transcript = best_alternative.transcript

            print(f'Transcript : {transcript}')
            print_word_tags(best_alternative)
            sys.stdout.write('===========================================\n')


            if re.search(r'\b(exit|quit)\b', transcript, re.I):
                print('\nDetecting keywords quit or exit ..\r')
                print('Exiting..')
                break

def print_word_tags(alternatives):
    for word in alternatives.words:
        print(u"Word: {}".format(word.word))
        print(u"Speaker tag: {}".format(word.speaker_tag))

def parse_arg():
    parser = argparse.ArgumentParser(description='configuration')
    parser.add_argument('--language_code', '-lc', type=str, help="set the language-code which will be recognized")
    args = parser.parse_args()
    return args.language_code


if __name__ == '__main__':
    language_code = parse_arg()
    client = speech_v1.SpeechClient()
    diarization_config = types.SpeakerDiarizationConfig(
        enable_speaker_diarization=True
    )
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code,
        enable_word_time_offsets=False,
        max_alternatives=1,
        diarization_config=diarization_config
    )
    streaming_config = types.StreamingRecognitionConfig(
        config=config,
        interim_results=False,
        single_utterance=False
    )

    sys.stdout.write('Listening, say "Quit" or "Exit" to stop.\n\n')
    sys.stdout.write('There will show the following information ..\n')
    sys.stdout.write('- Transcript\n')
    sys.stdout.write('- Speaker_tag\n')
    sys.stdout.write('===========================================\n\n')

    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (types.StreamingRecognizeRequest(audio_content=content)
                    for content in audio_generator)

        responses = client.streaming_recognize(streaming_config, requests)

        listen_print_loop(responses)