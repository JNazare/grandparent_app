from flask import Flask, redirect, url_for, session, request, render_template
from flask_oauth import OAuth


SECRET_KEY = 'development key'
DEBUG = True
FACEBOOK_APP_ID = 'process.env.FACEBOOK_APP_ID'
FACEBOOK_APP_SECRET = 'process.env.FACEBOOK_APP_SECRET'


app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'email,user_photos'}
)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True))


@app.route('/home')
@facebook.authorized_handler
def facebook_authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['oauth_token'] = (resp['access_token'], '')
    me = facebook.get('/me')
    my_photos = facebook.get('/me/photos/uploaded').data['data']
    viewable_photos = []
    for photo in my_photos:
    	viewable_photos = viewable_photos + [str(photo['source'])]
    return render_template('index.html', viewable_photos=viewable_photos)
    # return 'Logged in as id=%s name=%s redirect=%s' % \
    #     (me.data['id'], me.data['name'], request.args.get('next'))

@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')

if __name__ == '__main__':
    app.run()