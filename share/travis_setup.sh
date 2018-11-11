#!/bin/bash
set -evx

mkdir ~/.crowdcoinbrain

# safety check
if [ ! -f ~/.crowdcoinbrain/.crowdcoin.conf ]; then
  cp share/crowdcoin.conf.example ~/.crowdcoinbrain/crowdcoin.conf
fi
