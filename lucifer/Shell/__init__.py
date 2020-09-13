"""The Shell package contains the class for the Shell."""
import lucifer.Indexing as Indexing
from lucifer.Help import help_menu


class Shell:
    from ._In import parseShellIn, getIn
    from ._Info import display_help, print_name, print_id, print_auto_vars
    from ._Spawn import spawn_shell, spawn
    from ._Options import show, show_options, command_set, change_auto_set_vars
    from ._Module import describe_module, run_module, use_module, set_vars, use
    from ._Shell import open_shell, show_shells, set_name, set_name_id, clear_shell, background_shell

    def __init__(self, ID, lucifer_manager):
        """Per Shell Setup."""
        self.id = ID
        self.is_main = True if self.id == 0 else False
        self.luciferManager = lucifer_manager
        self.gui = False
        self.module = ""
        self.module_obj = None
        self.loaded_modules = {}
        self.program_name = "lucifer"
        self.shell_in = ""
        self.vars = {}
        self.auto_vars = lucifer_manager.auto_vars
        self.help_menu = help_menu
        self.name = "Shell " if not self.is_main else "Main Shell"
        self.alias = {
            "help": self.display_help,
            "set": self.command_set,
            "show": self.show,
            "quit": self.luciferManager.end,
            "exit": self.luciferManager.end,
            "id": self.print_id,
            "spawn_shell": self.spawn_shell,
            "open_shell": self.open_shell,
            "close": self.background_shell,
            "show_shells": self.show_shells,
            "name": self.print_name,
            "set_name": self.set_name,
            "set_name_id": self.set_name_id,
            "clear": self.clear_shell,
            "use": self.use,
            "run": self.run_module,
            "exploit": self.run_module,
            "set_vars": self.set_vars,
            "options": self.show_options,
            "description": self.describe_module,
            "describe": self.describe_module,
            "auto_vars": self.print_auto_vars,
            "change_auto_vars": self.change_auto_set_vars,
            "auto_var": self.print_auto_vars,
            "change_auto_var": self.change_auto_set_vars
        }
        self.module_cache = None
        self.luciferManager.shell_recur += 1
        self.index_modules()

    def index_modules(self):
        print("Indexing Modules...")
        self.module_cache = Indexing.index_modules()
        print(f"Indexing Complete, Found {len(self.module_cache[1].keys())} Modules")
