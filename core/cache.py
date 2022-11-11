from django.core.cache import caches
from redis import Redis


class BaseCacheService:
    PREFIX = ''
    KEYS = {

    }
    EX = 60 * 30

    @staticmethod
    def _get_redis_client() -> Redis:
        return caches['default'].client.get_client()


class CacheService(BaseCacheService):
    PREFIX = 'E'
    KEYS = {
        'user_id' : f'{PREFIX}:''{UUID}'
    }
    EX = 60 * 30

    def cache_user_id(self, uuid, user_id):
        client = self._get_redis_client()
        client.set(name=self.KEYS['user_id'].format(UUID=uuid), value=user_id, ex=self.EX)

    def get_user_id(self, uuid) -> int:
        client = self._get_redis_client()
        return int(client.get(name=self.KEYS['user_id'].format(UUID=uuid)) or b'-1')




