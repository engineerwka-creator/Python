import os
import time

FIRMWARE_FILE = "firmware.py"
UPDATE_FILE = "update.py"


def check_for_update():
    """Sprawdza, czy dostępny jest plik z aktualizacją."""
    return os.path.exists(UPDATE_FILE)


def install_update():
    """Zastępuje stary program nowym."""
    print("🔄 Instaluję aktualizację oprogramowania...")
    os.replace(UPDATE_FILE, FIRMWARE_FILE)
    print("✅ Aktualizacja zakończona!")


def run_firmware():
    """Uruchamia główny program użytkownika."""
    print("🚀 Uruchamiam program użytkownika...")
    time.sleep(1)
    os.system(f"python {FIRMWARE_FILE}")


def main():
    print("🧠 Bootloader startuje...")
    time.sleep(1)

    if check_for_update():
        print("📦 Wykryto nową wersję oprogramowania!")
        install_update()
    else:
        print("✅ Brak aktualizacji, uruchamiam istniejący program.")

    run_firmware()


if __name__ == "__main__":
    main()
