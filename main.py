# Import Libraries
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.toast import toast


# Create a random name class that should inherit from App
class MyToastMessageApp(MDApp):
    # Create build method
    def build(self):
        # Create a Button
        btn=MDRaisedButton(text="Show toast message",
                           font_size=32,
                           pos_hint={"center_x":0.5, "center_y":0.5})

        # Bind the button when the button clicked will run showToast method
        btn.bind(on_release=self.showToast)
        # Return the button
        return btn

    def showToast(self, instance):
        # show toast message
        toast(text="This is a toast message")



# Create class object
MyToastMessageApp().run()
