#mouse library
class BadMouses:
    def __init__(self, kb, mouse):
        self.mouse = mouse
        #button masks: L=1, R=2, M=4
        self.buttons = {"left": 0x01, "right": 0x02, "middle": 0x04}

    def move_rel(self, args):
        try:
            parts = args.split()
            dx, dy = int(parts[0]), int(parts[1])
            # put_mouse_event(dx, dy, dz, dw, buttons)
            self.mouse.put_mouse_event(dx, dy, 0, 0, 0)
        except (IndexError, ValueError):
            print("BadMouses:illegal instruction,skipping")

    def move_abs(self, args):
        try:
            parts = args.split()
            x, y = int(parts[0]), int(parts[1])
            # virtualbox give up to 65565 pixel move bit all use 1080x1920 so we use it as a corner move
            self.mouse.put_mouse_event_abs(x, y, 0, 0, 0)
        except (IndexError, ValueError):
            print("BadMouses:Invalid settings,skipping")

    def click(self, args):
        mask = self.buttons.get("left")
        
        # just firmly pressing
        self.mouse.put_mouse_event(0, 0, 0, 0, mask)
        self.mouse.put_mouse_event(0, 0, 0, 0, 0)

    def scroll(self, args):
        try:
            dz = int(args)
            self.mouse.put_mouse_event(0, 0, dz, 0, 0)
        except ValueError:
            pass

