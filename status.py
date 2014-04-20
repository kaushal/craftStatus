from flask import Flask, render_template
from minecraft_query import MinecraftQuery

app = Flask(__name__)

@app.route('/')
def getStatus():
    query = MinecraftQuery("dev.eddiezane.com", 25565)

    rules = query.get_rules()

    print rules
    print rules['players']
    retVal = ''
    for name in rules['players']:
        retVal = retVal + name + ', '
    return render_template('results.html', names=rules['players'], rule=rules['motd'], number=rules['numplayers'])

if __name__ == '__main__':
    app.run(host='0.0.0.0')
