import speedtest
import math

print("Generating your results...\n")

speedtest = speedtest.Speedtest(secure=True)  # Force HTTPS connection
speedtest.get_best_server()

# Converting speeds from bits to Mbps and rounding down
download_speed = math.floor(speedtest.download() / 1000000)
upload_speed = math.floor(speedtest.upload() / 1000000)


def test_failed():
    print("TEST FAILED :(\n")
    print("Cambly Requirements:")
    print(" - Download Speed: 10 Mbps")
    print(" - Upload Speed: 3 Mbps ")
    print("\nYour Results:")
    print(" - Download Speed: " + str(download_speed) + " Mbps")
    print(" - Upload Speed: " + str(upload_speed) + " Mbps")


def test_passed():
    print("TEST PASSED :)\n")
    print("Your Results:")
    print(" - Download Speed: " + str(download_speed) + " Mbps")
    print(" - Upload Speed: " + str(upload_speed) + " Mbps")


def main():

    # If speed is too slow
    if download_speed < 10 or upload_speed < 3:
        test_failed()

    # If speed is fast enough
    test_passed()


if __name__ == "__main__":
    main()
