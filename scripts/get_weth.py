from brownie import interface, config, network, accounts
from scripts.helpful_scripts import get_account


def main():
    get_weth()


def get_weth():
    """
    Mints WETH by depositing ETH.
    """
    account = get_account()  # add your keystore ID as an argument to this call
    weth = interface.WethInterface(
        config["networks"][network.show_active()]["weth_token"]
    )
    tx = weth.deposit({"from": account, "value": 0.1 * 1e18})
    tx.wait(1)
    print("Received 0.1 WETH")
