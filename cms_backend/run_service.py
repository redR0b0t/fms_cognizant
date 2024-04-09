from cms_backend.utils.listener import listen_msgs


global uname
uname="uc4ddc6536e59d9d8f8f5069efdb4e25"



if __name__ == '__main__':
    try:
        listen_msgs()
    except Exception as e:
        print(f'error occured:\n\n\n {e}')  