import pytest
import sys
import os
import re
os.environ['SENTINEL_ENV'] = 'test'
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import config

from crowdcoind import CrowdcoinDaemon
from crowdcoin_config import CrowdcoinConfig


def test_crowdcoind():
    config_text = CrowdcoinConfig.slurp_config_file(config.crowdcoin_conf)
    network = 'mainnet'
    is_testnet = False
    genesis_hash = u'0000006f3f7f60bf9fac87e30384c52f7cf7a65bf468f018cab8507e380af8c7'
    for line in config_text.split("\n"):
        if line.startswith('testnet=1'):
            network = 'testnet'
            is_testnet = True
            genesis_hash = u'000000be89e7ceb515258698012f4d0ac7846980969515fdf2771cda7e0eae68'

    creds = CrowdcoinConfig.get_rpc_creds(config_text, network)
    crowdcoind = CrowdcoinDaemon(**creds)
    assert crowdcoind.rpc_command is not None

    assert hasattr(crowdcoind, 'rpc_connection')

    # Crowdcoin testnet block 0 hash == 00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c
    # test commands without arguments
    info = crowdcoind.rpc_command('getinfo')
    info_keys = [
        'blocks',
        'connections',
        'difficulty',
        'errors',
        'protocolversion',
        'proxy',
        'testnet',
        'timeoffset',
        'version',
    ]
    for key in info_keys:
        assert key in info
    assert info['testnet'] is is_testnet

    # test commands with args
    assert crowdcoind.rpc_command('getblockhash', 0) == genesis_hash
