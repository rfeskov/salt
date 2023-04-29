
{% set package_name = 'nginx' %}

copy_package:
  file.managed:
    - name: /srv/salt/nginx.deb
    - source: salt://nginx_package/nginx.deb
    - makedirs: True
    - user: root
    - group: root
    - mode: 755

install_package:
  pkg.installed:
    - sources:
      - nginx: salt://nginx_package/nginx.deb
