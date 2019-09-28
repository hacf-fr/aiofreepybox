class Vpn:

    def __init__(self, access):
        self._access = access

    open_vpn_config_schema = {
        'configFile': '',
        'password': '',
        'username': ''
    }

    allowed_auth_schema = {
        'chap': bool,
        'eap': bool,
        'mschap': bool,
        'mschapv2': True,
        'pap': bool
    }

    mppe = [
        'disable',
        'require',
        'require_128'
    ]

    pptp_config_schema = {
        'allowedAuth': allowed_auth_schema,
        'mppe': mppe[2],
        'password': '',
        'remoteHost': '',
        'username': ''
    }

    vpn_client_configuration_schema = {
        'active': bool,
        'confOpenvpn': open_vpn_config_schema,
        'confPptp': pptp_config_schema,
        'description': '',
        'id': '',
        'type': 'openvpn',
    }

    vpn_user_data_schema = {
        'ipReservation': '',
        'login': '',
        'password': ''
    }

    async def create_vpn_client_configurations(self, vpn_client_configuration=vpn_client_configuration_schema):
        '''
        Create vpn client configurations
        '''
        return await self._access.post('vpn_client/config/', vpn_client_configuration)

    async def create_vpn_user(self, vpn_user_data=vpn_user_data_schema):
        '''
        Create vpn user
        '''
        return await self._access.post('vpn/user/', vpn_user_data)

    async def delete_vpn_client_configurations(self, config_id):
        '''
        Delete vpn client configurations
        '''
        return await self._access.delete(f'vpn_client/config/{config_id}')

    async def delete_vpn_server_connection(self, connection_id):
        '''
        Delete vpn server connection
        '''
        return await self._access.delete(f'vpn/connection/{connection_id}')

    async def delete_vpn_user(self, user_login):
        '''
        Delete vpn user
        '''
        await self._access.delete(f'vpn/user/{user_login}')

    async def download_vpn_user_configuration(self, server_name, user_login):
        '''
        Download vpn user configuration
        '''
        return await self._access.get(f'vpn/download_config/{server_name}/{user_login}')

    async def edit_vpn_client_configurations(self, config_id, vpn_client_configuration):
        '''
        Edit vpn client configurations
        '''
        return await self._access.put(f'vpn_client/config/{config_id}', vpn_client_configuration)

    async def edit_vpn_server_configuration(self, vpn_server_id, vpn_server_configuration):
        '''
        Edit vpn server configurations
        '''
        return await self._access.put(f'vpn/{vpn_server_id}/config/', vpn_server_configuration)

    async def get_vpn_client_applications(self):
        '''
        Get vpn client applications
        '''
        return await self._access.get('vpn_client/apps/')

    async def get_vpn_client_configurations(self):
        '''
        Get vpn client configurations
        '''
        return await self._access.get('vpn_client/config/')

    async def get_vpn_client_status(self):
        '''
        Get vpn client status
        '''
        return await self._access.get('vpn_client/status/')

    async def get_vpn_ip_reservations(self):
        '''
        Get vpn ip reservations
        '''
        return await self._access.get('vpn/ip_pool/')

    async def get_vpn_server_configuration(self, vpn_server_id):
        '''
        Get vpn server configuration
        '''
        return await self._access.get(f'vpn/{vpn_server_id}/config/')

    async def get_vpn_server_connections(self):
        '''
        Get vpn server connections
        '''
        return await self._access.get('vpn/connection/')

    async def get_vpn_servers(self):
        '''
        Get vpn servers
        '''
        return await self._access.get('vpn/')

    async def get_vpn_users(self):
        '''
        Get vpn users
        '''
        return await self._access.get('vpn/user/')
