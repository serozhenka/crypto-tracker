from channels.generic.websocket import AsyncJsonWebsocketConsumer

from .constants import TrackerMsgType


class TrackerConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add('crypto', self.channel_name)

    async def tracker_send_data(self, event):
        await self.send_json({
            'msg_type': TrackerMsgType.NEW_MESSAGE,
            'data': event.get('data'),
        })

    async def disconnect(self, code):
        await self.close(code)
