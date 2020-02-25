from slack import RTMClient
from octorest import OctoRest
import wget

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

        # pr int(data['user'])
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

        if command == "!start":
            print("Inside of start command")
            print(printer_client)
            printer_client.start(location="/home/pi/OctoPrint/venv/bin/uploads", filename="small_boat.gcode")

        # Status / number of jobs queued.
        if command == '!status':
            status(web_client, channel_event, thread)

        # Please don't ddos the printer with uploads.
        if command == '!upload':
            print("File Upload:")
            try:
                # file_info[0] accesses the first and assumed only file per upload.
                file_info = data['files']
                # print(file_info)

                filename = file_info[0]['title']
                # test.java
                words = filename.split(".")
                print("Words = {}".format(words))
                extension = words[-1]
                print("Extension = {}".format(extension))
                # DEBUG:

                if extension != 'gcode':
                    # Prints a message to channel saying the file isnt gcode.
                    print("Nah, chief. You can't do that. That ain't a gcode. ¯\_(ツ)_/")
                    return

                # url_private_download
                print(file_info[0]['url_private_download'])
                url = file_info[0]['url_public_download']

                file = wget.download(url, out="/home/pi/OctoPrint/venv/bin/uploads")
                print(file)
                print(printer_client)
                try:
                    printer_client.upload(file)
                except:
                    return
            except:
                return

            print("Uploaded file {}".format(file_info[0]['filetype']))

    except:
        return

printer_client = OctoRest(url="", apikey="API_KEY")
rtm_client = RTMClient(token='TOKEN')
rtm_client.start()
