from .base import Resource, ResourceIterator
from .dropletaction import DropletAction
from .exceptions import *


class Droplet(Resource):

    __last_action_id = None

    def __init__(self, attrs={}):
        super(Droplet, self).__init__(attrs)

    def reboot(self):
        """Reboot current droplet."""
        return self.__do_action('reboot')

    def power_cycle(self):
        """Power off current droplet and then back on."""
        return self.__do_action('power_cycle')

    def shutdown(self):
        """Shutdown current droplet."""
        return self.__do_action('shutdown')

    def power_off(self):
        """Power off current droplet."""
        return self.__do_action('power_off')

    def power_on(self):
        """Power on current droplet."""
        return self.__do_action('power_on')

    def password_reset(self):
        """Password reset current droplet. New password will be emailed to you."""
        return self.__do_action(type_='password_reset')

    def enable_ipv6(self):
        """Enable IPv6 for current droplet."""
        return self.__do_action(type_='enable_ipv6')

    def disable_backups(self):
        """Disable backups for current droplet."""
        return self.__do_action(type_='disable_backups')

    def disable_backups(self):
        """Enable private networking for current droplet."""
        return self.__do_action(type_='enable_private_networking')

    def create_snapshot(self, name):
        """Snapshot current droplet."""
        return self.__do_action(type_="snapshot", name=name)

    def __do_action(self, type_, name=None):
        """Perform action on droplet."""
        if not self.id:
            raise ValueError('Droplet not loaded.')
        params = {'type': type_}
        if name:
            params['name'] = name
        data = self.call_api('droplets/%s/actions' % self.id, method='post', params=params)
        try:
            self.__last_action_id = data['action']['id']
            return DropletAction(self.id, data['action'])
        except KeyError:
            raise InvalidResponse('Retrieved invalid response from DigitalOcean API.')


class DropletIterator(ResourceIterator):

    def __init__(self):
        super(DropletIterator, self).__init__()
