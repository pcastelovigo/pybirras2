from wordpress_xmlrpc import *
from wordpress_xmlrpc.methods.posts import *
from wordpress_xmlrpc.methods.users import *
from wordpress_xmlrpc.compat import *

wordpress = Client('http://dominio.url/xmlrpc.php', 'usuario', 'contraseña')

post = WordPressPost()
post.title = "pyBirras Test 1"
post.content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
post.post_status = "publish"
wordpress.call(NewPost(post))
