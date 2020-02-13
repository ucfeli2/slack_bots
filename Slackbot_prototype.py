from slack import RTMClient
from time import sleep

# Driver methods for each command.
# Proper usage instructions
def helpMe(client, c_e, txt, t_ts):
    print(client, c_e, txt, t_ts)
    client.chat_postMessage(
    channel=c_e,
    text=txt,
    thread_ts=t_ts
    )
    return

# Time duration of the print.
def status(w_c, c_e, th):
    w_c.chat_postMessage(
    channel=c_e,
    text="Work In Progress" ,
    thread_ts=th
    )
    return

# File I/O for what they want to print.
def upload():
    return

# Sent by user after current print has finished -- updates queue
def finished():
    return

# List of people currently waiting to print.
def queue():
    return

# Returns snapshot of current print progress
def snapshot():
    return

# Begins livestream of current print progress
def stream():
    return

@RTMClient.run_on(event="message")
def print_message(**payload):
    print("Message reveived:")
    data = payload['data']
    web_client = payload['web_client']

    try:
        # Debug information
        # print(data)

        # print(data['user'])
        # print(data['text'])
        # print(data['channel'])

        command = data['text'].split(" ")[0]

        channel_event = data['channel']
        received_message = data['text']
        thread = data['ts'] # Lets the bot reply to the message as a thread

        # Help / Usage command.
        if command == '!help':
            web_client.chat_postMessage(
            channel=channel_event,
            text="Here's what I can do...",
            thread_ts=thread
            )
            # prompt = "WIP: Proper usage:"
            # helpMe(client, channel_event, prompt, thread)

        # Status / number of jobs queued.
        if command == '!status':
            status(web_client, channel_event, thread)

        # Please don't ddos the printer with uploads.
        if command == '!upload':
            print("File Upload:")
            try:
                # file_info[0] accesses the first and assumed only file per upload.
                file_info = data['files']
                if (file_info[0]['filetype'] != 'java'):
                    # Error message saying this ain't g. code.
                    return
            except:
                return

            print("Uploaded file {}".format(file_info[0]['filetype']))

        return
    except:
        return

rtm_client = RTMClient(token='INSERT_TOKEN')
rtm_client.start()
