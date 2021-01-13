import json
from asgiref.sync import async_to_sync
from apiEndi.easy import *
from channels.generic.websocket import JsonWebsocketConsumer 
from door.models import Chat as ChatModel
from door.serializers import FullUserSerializer

def hasTokenSession(cookies):
    
    if cookies.get('token'):
        try:
            token = Token.objects.get(key=cookies.get('token'))
            return token.user
        except Token.DoesNotExist:
            pass    
    return AnonymousUser()

class Chat(JsonWebsocketConsumer):
    def connect(self):
        
        self.scope['user'] =  hasTokenSession(self.scope['cookies'])
        if self.scope.get('user'):
            async_to_sync(self.channel_layer.group_add)(
                "public",
                self.channel_name
            )
            async_to_sync(self.channel_layer.group_add)(
                self.scope['user'].username,
                self.channel_name
            )
            self.accept()
        else: self.close()

    def disconnect(self, close_code):
        
        if self.scope['user']:
            async_to_sync(self.channel_layer.group_discard)(
                "public",
                self.channel_name
            )
            async_to_sync(self.channel_layer.group_discard)(
                self.scope['user'].username,
                self.channel_name
            )

    def receive_json(self, content):

        if content['reqType'] == "getPrevChat":
            async_to_sync(self.channel_layer.group_send)(
                self.scope['user'].username,{'type':'sendHistory'}
            )
        elif content['reqType'] == "message":
            ChatModel(message=content['message'],fromUser=self.scope['user']).save()
            user = FullUserSerializer(self.scope['user']).data
            async_to_sync(self.channel_layer.group_send)(
                'public',{
                    'type':'broadcast',
                    'message':content['message'],
                    'fromUser':user                    
                    }
            )    

    def sendHistory(self, event):
        history = []
        chats = ChatModel.objects.all()

        for i in chats:
            history.append({
                'message':i.message,
                'fromUser':FullUserSerializer(i.fromUser).data
            })
            
        self.send_json({
            'do': 'history',
            'chats': history
        })

    def broadcast(self, event):
        self.send_json({
            'do': 'message',
            'message': event['message'],
            'fromUser':event['fromUser']
        })