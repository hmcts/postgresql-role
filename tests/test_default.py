import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('postgresql-role')


def test_hosts_file(File):
    f = File('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_pg_hba_templating(File):
    pg_hba = File("/var/lib/pgsql/9.6/data/pg_hba.conf").content_string

    expected_pg_hba = open("tests/expected_pg_hba.conf", "r").read()

    assert pg_hba == expected_pg_hba
