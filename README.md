# Aleph

## Getting Started

Make sure you have the following tools installed and set up.

* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Python](https://www.python.org/)
* [VSCode](https://code.visualstudio.com/)
* [Jupyter](https://jupyter-notebook.readthedocs.io/en/latest)

Now we'll look into how to install each of them. If you have them installed
already - great! However we still recommend to continue reading below to ensure
that your setup matches what the rest of this exercise will expect.

### Mac

1. Install [Homebrew](https://brew.sh/) - this will give us a package manager
   that we can use to install other things.
1. Install Git and Python using Homebrew:

    ```
    brew install git python3
    ```

1. Download and install VSCode from [its
   homepage](https://code.visualstudio.com/).


### Windows

1. Install [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) - you
   shouldn't need to veer away from the defaults (unless you know what you're
   doing, in which case - customize away).

1. Download and install VSCode from [its
   homepage](https://code.visualstudio.com/).

1. Set up VSCode with WSL using [this guide](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode).

1. Install Python and Git Inside WSL:

    ```
    sudo apt-get update && sudo apt-get install -y python3 git
    ```

### Next steps (for both Mac and Windows)

1. Create a [virtual environment](https://docs.python.org/3/library/venv.html)
   (also called "venv") for our exercise:

    ```
    python3 -m venv ~/.aleph
    ```

1. Now you can "activate" this environment whenever you want using:

    ```
    source ~/.aleph/bin/activate
    ```

1. Install Jupyter inside this environment using:

    ```
    pip install jupyter
    ```

1. Test that it's working correctly using [this guide](https://docs.jupyter.org/en/latest/running.html).

1. And after you're done, you can deactivate the virtual environment using the `deactivate` command

1. For some quality-of-life improvement, install `Python` extension in VSCode (optional).


## Setting up Git & GitHub

1. Create an account at: https://github.com/signup (if you haven't got one already).

1. Regardless of whether you have an existing account or have just created a
   new one, now would be a good time to enable [2-Factor
   authentication](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa)
   for your account.

   > **NOTE**: The username and password used above will only be valid for
   > signing in to the website. For use elsewhere, you will need to use an
   > access token - more on that below.

1. Once you're signed into your GitHub.com account, create a new access token
   like so:

   1. https://github.com/settings/tokens -> "Generate new token" ->
   "Generate new token (classic)"
   1. Enter a "note" that reminds you what you're going to use this token for,
      something like "general purpose token for personal macbook m3"
   1. "Expiration" -> "No expiration" (this is not ideal but one step at a time)
   1. "Scopes" -> Select "repo"
   1. "Generate token"
   1. GitHub will now display the token - make note of this token as it will
      only be shown to you once. I recommend storing this in a safe place such
      as a password manager.

1. Now, whenever the `git` command-line or VSCode or some such asks you for
   your "password", you can instead use this token.
