import os
import sys
from flask import Flask, render_template, redirect, url_for, request
from logic.task_manager import TaskManager

app = Flask(__name__, template_folder="views")
manager = TaskManager()


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.jinja2",
                                script_template=get_script_template(),
                                tasks=manager.get_tasks()
                               )
    else:
        return handle_new_script()


@app.route('/delete/<id_value>', methods=["GET", "DELETE"])
def delete_task(id_value):
    manager.delete_task(id_value)
    return redirect(url_for("index"))


def handle_new_script():
    name = request.form.get("name")
    script = request.form.get("script")
    manager.add_task(name, script)

    return redirect(url_for("index"))


def get_script_template() -> str:
    cwd = os.path.dirname(sys.modules['__main__'].__file__)
    path = os.path.join(cwd, "script_template.py")

    with open(path, 'r') as script_template_file:
        return script_template_file.read()


if __name__ == '__main__':
    app.run()
