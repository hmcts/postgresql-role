postgresql
=========

Used for installing postgresql

Example Playbook
----------------

install.yml
```yaml
- hosts: all
  become: yes
  roles:
    - devops.postgresql
```

vars.yml:

See [vars.yml](tests/vars.yml)

Tests
---------------

Tests are run using [molecule](https://github.com/metacloud/molecule) and [docker](https://www.docker.com/)

```bash
$ molecule test
```

Tests are also run on jenkins, they are split out into individual stages to make it easier to
 see what step failed.


License
-------

MIT

Author Information
------------------

HMCTS Reform Programme
