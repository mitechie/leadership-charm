import charms.leadership

from charms.reactive import when, when_not, set_flag
from charmhelpers.core.hookenv import config, status_set


@when_not('leadership-flex.installed')
def install_leadership_flex():
    set_flag('leadership-flex.installed')
    status_set('active', 'ready to go')


@when('config.changed.name')
def config_changed_name():
    pass
#    name = config().get('name')
#    if not name:
#        name = '-- not set --'
#    status_set('active', 'my name is ' + name)


@when('leadership.is_leader')
def increment_counter():
    count = charms.leadership.leader_get('counter')

    if not count:
        count = 0
    count = int(count)
    count += 1
    
    charms.leadership.leader_set(counter=count)
