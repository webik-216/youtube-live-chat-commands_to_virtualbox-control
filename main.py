import json
import os
import virtualbox
import pytchat
from supplies.BadKeyboards import BadKeyboards
from supplies.BadMouses import BadMouses
from supplies.ForegroundStub import ForegroundStub

class Youtube2Box:
    def __init__(self):
        config_path = os.path.join(os.getcwd(), "config.json")
        with open(config_path, "r") as f:
            self.config = json.load(f)
            
                self.vbox = virtualbox.VirtualBox()
        self.vm = self.vbox.find_machine(self.config["vm_name"])
        self.session = self.vm.create_session()
        
        #Modules
        kb = self.session.console.keyboard
        mouse = self.session.console.mouse
        self.modules = {
            "BadKeyboards": BadKeyboards(kb),
            "BadMouses": BadMouses(mouse),
            "ForegroundStub": ForegroundStub(kb, mouse)
        }
        self.cmd_map = self.config["Cust_plgs"]

    def run(self):
        chat = pytchat.create(video_id=self.config["video_id"])
        print(f"started on VM: {self.config['vm_name']}")

        while chat.is_alive():
            for c in chat.get().sync_items():
                parts = c.message.split(" ", 1)
                cmd = parts[0].lower()
                args = parts[1] if len(parts) > 1 else ""

                if cmd in self.cmd_map:
                    mod_name, method_name = self.cmd_map[cmd]
                    module = self.modules.get(mod_name)
                    if module:
                        func = getattr(module, method_name, None)
                        if func:
                            func(args)

if __name__ == "__main__":
    Youtube2Box().run()


