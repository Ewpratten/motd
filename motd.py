import argparse
import requests
import getpass
import datetime
import socket
import re
import time

today = datetime.datetime.now()

# Features
# - Time and date
# - Number of open issues'

## Arguments ##
ap = argparse.ArgumentParser()
ap.add_argument("-g", "--github-username", default="ewpratten")
ap.add_argument("-o", "--github-org", default="frc5024")
args = ap.parse_args()

## Helpers and Functions ##


class Timer(object):
    tm = 0

    def start(self):
        self.tm = time.time()

    def stop(self):
        return time.time() - self.tm


tm_i = Timer()


def getUsername() -> str:
    return getpass.getuser()


def getTimeStr() -> str:
    return today.strftime("%-I:%-M on %a %B %d, %Y")


def getGHIssues():
    data = requests.get(
        f"https://api.github.com/search/issues?q=user:{args.github_username}&sort=updated&order=desc").json()

    issues = [item for item in data["items"]]
    open_count = 0

    for issue in issues:
        if issue["state"] == "open":
            open_count += 1

    # Build a lynk for the open issues list
    long_url = f"https://github.com/issues?q=is%3Aissue+archived%3Afalse+user%3A{args.github_username}+user%3A{args.github_org}+is%3Aopen"

    lynk_data = requests.post("https://new.lynkz.me",
                              data={"action": "new", "url": long_url}).text

    lynk = re.findall(
        r"<td><a href=\"https:\/\/lynkz\.me\/.*\">(.*)<\/a><\/td>", lynk_data)[0]

    return (open_count, lynk)


def hasInetAccess(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        return False


class ConsoleBuffer(object):
    buffer = ""

    def getBuffer(self):
        return self.buffer.strip()

    def writeLine(self, line):
        self.buffer += line + "\n"

## Main script ##


def main():
    # Create a ConsoleBuffer
    cb = ConsoleBuffer()

    # Get system username
    username = getUsername()
    dt = getTimeStr()
    open_issues, issues_lynk = getGHIssues()

    # Skip everything else if no inet access
    if not hasInetAccess():
        print("Internet Disconnected. MOTD hidden.")
        return

    # Write to buffer
    cb.writeLine(f"Welcome {username}!")
    cb.writeLine(f"It is currently {dt}.")

    if open_issues > 0:
        cb.writeLine(
            f"You have {open_issues} issues open on GitHub. View them here: {issues_lynk}")

    # Lastly, print out the message
    print(cb.getBuffer())


if __name__ == "__main__":
    main()
