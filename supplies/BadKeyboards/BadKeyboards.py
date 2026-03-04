import time

class BadKeyboards:
    def __init__(self, kb, mouse):
        self.kb = kb

    def press(self, args):
        key = args.strip().lower()
        if not key: return
        
        # VBox format: {enter} for special keys, 'a' for chars
        vbox_key = f"{{{key}}}" if len(key) > 1 else key
        try:
            self.kb.put_keys(vbox_key)
        except Exception as e:
            print(f"BadKeyboards Error: {e}")

    def type(self, args):
        #raw strings handle
        if not args: return
        self.kb.put_keys(args)

    def combo(self, args):
        # hotkey like "ctrl+alt+del" to "{ctrl}{alt}{del}"
        parts = args.split("+")
        formatted_combo = ""
        for p in parts:
            p = p.strip().lower()
            formatted_combo += f"{{{p}}}" if len(p) > 1 else p
            
        self.kb.put_keys(formatted_combo)

    def hold(self, args):
        print(f"BadKeyboards: Hold requested for {args} simulated")
        self.press(args)

