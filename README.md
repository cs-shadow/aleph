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
