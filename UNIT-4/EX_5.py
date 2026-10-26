# 5. Write a program to implement single multilevel and multiple inheritance. 
class Device:
    def __init__(self, brand):
        self.brand = brand

    def power_on(self):
        print(self.brand,"device is powering on.")


class Smartphone(Device):
    def browse_internet(self):
        print("Browsing the web on this",self.brand,"smartphone.")


class SmartWatch(Smartphone):
    def track_steps(self):
        print("Tracking daily step count.")


class Camera:
    def take_photo(self):
        print("Capturing a high-resolution photo.")


class MusicPlayer:
    def play_music(self):
        print("Playing my favorite playlist.")


class MultimediaDevice(Camera, MusicPlayer):
    def share_media(self):
        print("Sharing photos and music online.")


print("--- 1.Single Inheritance ---")
phone = Smartphone("Apple")
phone.power_on()
phone.browse_internet()
print()

print("--- 2.Multilevel Inheritance ---")
watch = SmartWatch("Samsung")
watch.power_on()
watch.browse_internet()
watch.track_steps()
print()

print("--- 3.Multiple Inheritance ---")
device = MultimediaDevice()
device.take_photo()
device.play_music()
device.share_media()
