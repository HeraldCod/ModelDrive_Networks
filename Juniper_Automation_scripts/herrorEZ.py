from jnpr.junos import device
from jnpr.junos.utils.config import Config

switch = {'host' : '10.10.10.150', 'user' : 'root' , 'pw' : '' }

device  = Device (host = switch['host'], user = switch['user'], password = switch['pw'])

try:
    device.open()

    config = Config(device)

    payload = """vlans{
        vlan101{
            vlan-id 101;
            }
        }
        """

    config.lock()
    config.load(payload, format='text')
    config.pdiff()

    # checking commit success

    if config.commit_check() == True:
        config.commit()
    else:
        config.rollback()

    config.unlock()

except ConnectAuthError as error:
    print('Authentication error occorred. Check your creds')
    print(str(error))
except ConfigLoadError as error:
    print(f'Config Load error : {str(error)}')
finally:
    device.close()





