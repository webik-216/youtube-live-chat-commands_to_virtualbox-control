import time

class ForegroundStub:
    def __init__(self, kb, mouse):
        self.kb = kb
        self.mouse = mouse

    def focus(self, args=None):
        print("Attempting to bring VM to front")
        try:
            # 0,0 relative move with no buttons tells VBox to 'wake up' the window
            self.mouse.put_mouse_event(0, 0, 0, 0, 0)
        except Exception as e:
            print(f"Focus Error: {e}")

    def refresh(self, args=None):
        print("Refreshing session lock")
        self.focus()
        
    def fullscreen(self, args=None):
        print("Toggling Fullscreen Mode")
        self.kb.put_keys("{rctrl}f")

    def keep_alive(self, args=None):
        print("Anti-sleep trapped")
        self.kb.put_keys("{shift}")

