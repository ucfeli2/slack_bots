from slack import RTMClient
from time import sleep

@RTMClient.run_on(event="message")
def print_message(**payload):

    data = payload['data']
    web_client = payload['web_client']

    try:
        # Debug information
        print(data['user'])
        print(data['text'])
        print(data['channel'])

        command = data['text'].split(" ")[0]

        channel_event = data['channel']
        received_message = data['text']
        thread = data['ts'] # Lets the bot reply to the message.

        # Help / Ussage command.
        if command == '!help':
            web_client.chat_postMessage(
                channel=channel_event,
                text="Possible Commands: ... WIP",
                thread_ts=thread
            )

        # Status / number of jobs queued.
        if command == '!status':
            web_client.chat_postMessage(
                channel=channel_event,
                text="WIP: There are currently __ of jobs in queue.",
                thread_ts=thread
            ) 
            
        # Status of the current job. 
        # Completed? Registers that the most recent job was finished
        # Backend : alert the user when its turn to print.
        # Upload command.
        # Snapshot. Sends a picture of the current print as a reply 
        # Stream? Pulls up live stream of the print as a reply.

        # TO DO: 
        return
    except:
        return

rtm_client = RTMClient(token='xoxb-892027031253-892068907621-7gdRvcMM2X8VEKIcuqYui7GS')
rtm_client.start()
