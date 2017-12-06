#!/bin/bash
set -evx

mkdir ~/.crowdcoincore

# safety check
if [ ! -f ~/.crowdcoincore/.crowdcoin.conf ]; then
  cp share/crowdcoin.conf.example ~/.crowdcoincore/crowdcoin.conf
fi
