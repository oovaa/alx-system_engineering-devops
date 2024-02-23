# install_flask
# install_flask_and_werkzeug
package { 'Flask':
  ensure => '2.1.0',
}

package { 'Werkzeug':
  ensure => '2.1.1',
}
