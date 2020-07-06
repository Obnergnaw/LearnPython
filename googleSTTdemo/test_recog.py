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
            confidence = best_alternative.confidence

            sys.stdout.write('===========================================\n')
            print(f'Transcript : {transcript}')
            print(f'Confidence : {confidence:.1%}')
            print_word_offsets(best_alternative)


            if re.search(r'\b(exit|quit)\b', transcript, re.I):
                print('\nDetecting keywords quit or exit ..\r')
                print('Exiting..')
                break


def print_word_offsets(alternatives):
    for word in alternatives.words:
        start_ms = word.start_time.ToMilliseconds()
        end_ms = word.end_time.ToMilliseconds()
        word = word.word
        print(f'{start_ms/1000:>7.2f}',
              f'{end_ms/1000:>7.2f}',
              f'{word}',
              sep=' | ')

def main(language_code):
    #language_code = 'cmn-CN'   # cmn-CN / en-US

    client = speech_v1.SpeechClient()
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code,
        enable_word_time_offsets=True,
        max_alternatives=1)
    streaming_config = types.StreamingRecognitionConfig(
        config=config,
        interim_results=False,
        single_utterance=False
    )

    sys.stdout.write('Listening, say "Quit" or "Exit" to stop.\n\n')
    sys.stdout.write('There will show the following information ..\n')
    sys.stdout.write('- Transcript\n')
    sys.stdout.write('- Confidence\n')
    sys.stdout.write('- Start(s) | End(s) | word\n')
    sys.stdout.write('===========================================\n\n')


    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (types.StreamingRecognizeRequest(audio_content=content)
                    for content in audio_generator)

        responses = client.streaming_recognize(streaming_config, requests)

        listen_print_loop(responses)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='language-code')
    parser.add_argument('language_code', type=str, help="set the language-code which will be recognized")
    args = parser.parse_args()
    main(args.language_code)