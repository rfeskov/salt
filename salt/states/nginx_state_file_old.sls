{% set package_name = 'nginx' %}

copy_package:
  file.managed:
    - name: /srv/salt/nginx.deb
    - source: salt://nginx_package/nginx.deb

install_package:
  pkg.installed:
      - sources:
        - nginx: salt://nginx_package/nginx.deb
