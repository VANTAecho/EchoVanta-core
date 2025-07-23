import os
import subprocess
import time
import speech_recognition as sr


def run_module(module_name):
    try:
        print(f"[~] Running module: {module_name}")
        subprocess.run(["python", module_name])
    except Exception as e:
        print(f"[!] Error running {module_name}: {e}")


def mic_test():
    try:
        mic_names = sr.Microphone.list_microphone_names()
        if not mic_names:
            print("[!] No microphones found.")
            return False
        print("[✓] Microphones detected:", mic_names)
        return True
    except Exception as e:
        print(f"[!] Microphone error: {e}")
        return False


def listen_and_trigger():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("\n[Echo] Awaiting voice command... Say 'activate echo' to proceed.")

    while True:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("🎙 Listening...")
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"[Voice] Heard: {command}")

            if "activate echo" in command:
                print("[✓] Activation command recognized.")
                run_module("trigger_evc.py")

            elif "mic check" in command:
                run_module("mic_check.py")

            elif "exit" in command or "shutdown" in command:
                print("[Echo] Shutting down.")
                break

        except sr.UnknownValueError:
            print("[Voice] Unclear audio, try again.")
        except sr.RequestError as e:
            print(f"[!] Voice recognition service error: {e}")
            break


if __name__ == "__main__":
    print("=== Echo Runner Activated ===")
    if mic_test():
        listen_and_trigger()
    else:
        print("[x] System cannot proceed. No mic available.")
