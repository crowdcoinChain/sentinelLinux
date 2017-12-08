# Crowdcoin Sentinel

An all-powerful toolset for Crowdcoin.

[![Build Status](https://travis-ci.org/crowdcoinpay/sentinel.svg?branch=master)](https://travis-ci.org/crowdcoinpay/sentinel)

Sentinel is an autonomous agent for persisting, processing and automating Crowdcoin V12.1 governance objects and tasks, and for expanded functions in the upcoming Crowdcoin V13 release (Evolution).

Sentinel is implemented as a Python application that binds to a local version 12.1 crowdcoind instance on each Crowdcoin V12.1 Masternode.

This guide covers installing Sentinel onto an existing 12.1 Masternode in Ubuntu 14.04 / 16.04.

## Installation

### 1. Install Prerequisites

Make sure Python version 2.7.x or above is installed:

    python --version

Update system packages and ensure virtualenv is installed:

    $ sudo apt-get update
    $ sudo apt-get -y install python-virtualenv

Make sure the local Crowdcoin daemon running is at least version 12.1 (120100)

    $ crowdcoin-cli getinfo | grep version

### 2. Install Sentinel

Clone the Sentinel repo and install Python dependencies.

    $ git clone https://github.com/crowdcoinChain/sentinelLinux.git && cd sentinelLinux
    $ export LC_ALL=C
    $ virtualenv ./venv
    $ ./venv/bin/pip install -r requirements.txt
    

### 2.a. Check crowdcoin.conf

Change the configuration checking, and appending if missing the following
parameters rpcuser and rpcpassword needs to be replaced

    rpcuser=<ADD A RANDOM STRING HERE>
    rpcpassword=<ADD A RANDOM STRING HERE>
    listen=1
    server=1
    discover=1
    rpcport=19470
    rpcthreads=8
    rpcallowip=127.0.0.1
    daemon=1
    listen=1
    server=1
    staking=0
    discover=1

   addnode=84.17.23.43:12875
   addnode=18.220.138.90:12875
   addnode=86.57.164.166:12875
   addnode=86.57.164.146:12875
   addnode=18.217.78.145:12875
   addnode=23.92.30.230:12875
   addnode=35.190.182.68:12875
   addnode=80.209.236.4:12875
   addnode=91.201.40.89:12875

                          

Clone the Sentinel repo and install Python dependencies.    


### 2.b. remove old files
Enter the wallet folder and stop the wallet

    ./crowdcoin-cli stop 
    
Enter the crowdcoin config folder mentioned during the installation
    
    rm mncache.dat
    rm mnpayments.dat
    
Enter the wallet folder and restart the wallet 

    ./crowdcoind -daemon -reindex
    
Check the sync status

    watch ./crowdcoin-cli mnsync status

As soon as you see the following response press CTRL+C

    ./crowdcoin-cli mnsync status
    {
    "AssetID": 999,
    "AssetName": "MASTERNODE_SYNC_FINISHED",
    "Attempt": 0,
    "IsBlockchainSynced": true,
    "IsMasternodeListSynced": true,
    "IsWinnersListSynced": true,
    "IsSynced": true,
    "IsFailed": false
    }

Finally start the masternode

    ./crowdcoin-cli masternode start


### 3. Set up Cron

Set up a crontab entry to call Sentinel every minute:

    $ crontab -e

In the crontab editor, add the lines below, replacing '/home/YOURUSERNAME/sentinel' to the path where you cloned sentinel to:

    * * * * * cd /home/YOURUSERNAME/sentinelLinux && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1

### 4. Test the Configuration

Test the config by runnings all tests from the sentinel folder you cloned into

    $ ./venv/bin/py.test ./test

With all tests passing and crontab setup, Sentinel will stay in sync with crowdcoind and the installation is complete

## Configuration

An alternative (non-default) path to the `crowdcoin.conf` file can be specified in `sentinel.conf`:

    crowdcoin_conf=/path/to/crowdcoin.conf

## Troubleshooting

To view debug output, set the `SENTINEL_DEBUG` environment variable to anything non-zero, then run the script manually:

    $ SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py

## Contributing

Please follow the [CrowdcoinCore guidelines for contributing](https://github.com/crowdcoinpay/crowdcoin/blob/v0.12.1.x/CONTRIBUTING.md).

Specifically:

* [Contributor Workflow](https://github.com/crowdcoinpay/crowdcoin/blob/v0.12.1.x/CONTRIBUTING.md#contributor-workflow)

    To contribute a patch, the workflow is as follows:

    * Fork repository
    * Create topic branch
    * Commit patches

    In general commits should be atomic and diffs should be easy to read. For this reason do not mix any formatting fixes or code moves with actual code changes.

    Commit messages should be verbose by default, consisting of a short subject line (50 chars max), a blank line and detailed explanatory text as separate paragraph(s); unless the title alone is self-explanatory (like "Corrected typo in main.cpp") then a single title line is sufficient. Commit messages should be helpful to people reading your code in the future, so explain the reasoning for your decisions. Further explanation [here](http://chris.beams.io/posts/git-commit/).

### License

Released under the MIT license, under the same terms as CrowdcoinCore itself. See [LICENSE](LICENSE) for more info.
