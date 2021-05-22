from flask import Flask, render_template
app = Flask(__name__,template_folder='template')


@app.route("/")
def template_test():
    return render_template('index.html')

@app.route("/project/<project_id>")
def show_tasks(project_id):
    return render_template("project.html",project_id=project_id)

if __name__ == '__main__':
    app.run(debug=True)