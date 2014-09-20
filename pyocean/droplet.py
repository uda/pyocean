from .base import Resource, ResourceIterator
from .exceptions import *
import time


class Droplet(Resource):

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
        return self.__do_action('password_reset')

    def resize(self, size):
        pass

    def restore(self, image):
        pass

    def rebuild(self, image):
        pass

    def rename(self, name):
        pass

    def change_kernel(self):
        pass

    def enable_ipv6(self):
        """Enable IPv6 for current droplet."""
        return self.__do_action('enable_ipv6')

    def disable_backups(self):
        """Disable backups for current droplet."""
        return self.__do_action('disable_backups')

    def disable_backups(self):
        """Enable private networking for current droplet."""
        return self.__do_action('enable_private_networking')

    def snapshot(self, name):
        """Snapshot current droplet."""
        return self.__do_action("snapshot", name=name)

    def __do_action(self, type_, name=None):
        """Perform action on droplet."""
        if not self.id:
            raise ValueError('Droplet not loaded.')
        path = "droplets/%s/actions" % self.id
        params = {'type': type_}
        if name:
            params['name'] = name
        res = self.call_api(path, method='post', params=params)
        try:
            while res['action']['status'] == 'in-progress':
                time.sleep(1)
                res = self.call_api('%s/%s' % (path, res['action']['id']))
                if res['action']['status'] == 'errored':
                    raise DropletActionError("Action '%s' on dropled failed." % \
                                             res['action']['type'])
        except KeyError:
            raise InvalidResponse('Retrieved invalid response from DigitalOcean API.')


class DropletIterator(ResourceIterator):

    def __init__(self):
        super(DropletIterator, self).__init__()
