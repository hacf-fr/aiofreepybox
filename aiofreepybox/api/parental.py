class Parental:

    def __init__(self, access):
        self._access = access

    async def create_parental_filter(self, parental_filter):
        '''
        Create parental filter
        '''
        return await self._access.post('parental/filter/', parental_filter)

    async def delete_parental_filter(self, filter_id):
        '''
        Delete parental filter
        '''
        return await self._access.delete('parental/filter/{0}'.format(filter_id))

    async def edit_parental_filter(self, filter_id, parental_filter):
        '''
        Edit parental filter
        '''
        return await self._access.put('parental/filter/{0}'.format(filter_id), parental_filter)

    async def edit_parental_filter_planning(self, filter_id, parental_filter_planning):
        '''
        Edit parental filter planning
        '''
        return await self._access.put('parental/filter/{0}/planning/'.format(filter_id), parental_filter_planning)

    async def get_parental_config(self):
        '''
        Get parental config
        '''
        return await self._access.get('parental/config/')

    async def get_parental_filter_planning(self, filter_id):
        '''
        Get parental filter planning
        '''
        return await self._access.get('parental/filter/{0}/planning/'.format(filter_id))

    async def get_parental_filters(self):
        '''
        Get parental filters
        '''
        return await self._access.get('parental/filter/')

    async def set_parental_control_configuration(self, parental_control_configuration):
        '''
        Set parental control configuration
        '''
        return await self._access.put('parental/config/', parental_control_configuration)