#21BCT0345
#Rakeem Shaikh
from web3 import Web3

# Connect to the Ethereum network
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# Set up the contract
abi = [
    {
        "constant": False,
        "inputs": [
            {
                "name": "_air_quality_pm25",
                "type": "uint256"
            },
            {
                "name": "_air_quality_pm10",
                "type": "uint256"
            },
            {
                "name": "_light_intensity",
                "type": "uint256"
            },
            {
                "name": "_pressure",
                "type": "uint256"
            },
            {
                "name": "_co2_levels",
                "type": "uint256"
            },
            {
                "name": "_noise_levels",
                "type": "uint256"
            },
            {
                "name": "_motion_detected",
                "type": "bool"
            },
            {
                "name": "_latitude",
                "type": "uint256"
            },
            {
                "name": "_longitude",
                "type": "uint256"
            },
            {
                "name": "_battery_level",
                "type": "uint256"
            }
        ],
        "name": "storeData",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
  # ABI of your updated contract
bytecode = "0x608060405234801561001057600080fd5b5060405161010038038061010083398101604081905261002f91610033565b60208061003e6000396000f3fe608060405260043610603f5760003560e01c80632f745c590146044575b600080fd5b605d6004803603810190604a9190606a565b606f565b005b604051605e919060a4565b60405180910390f35b600060728282606f565b9050919050565b600081359050607f8160b2565b92915050565b600060208284031215609457609360b7565b5b600060a084828501606f565b91505092915050565b60a58160bd565b82525050565b600060208201905060be6000830184609a565b92915050565b600081905091905056fea2646970667358221220d9e42d827ed0d88866d1fa640056021ad175fdb60c65b9a1df93d9e2a82fc46464736f6c634300080b0033"
  # Bytecode of your updated contract
contract = w3.eth.contract(abi=abi, bytecode=bytecode)

# Deploy the updated contract
def deploy_contract():
    tx_hash = contract.constructor().transact()
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt.contractAddress

contract_address = deploy_contract()
contract_instance = w3.eth.contract(address=contract_address, abi=abi)

def store_data(sensor_data):
    """
    Stores various IoT sensor data in the blockchain.
    sensor_data is a dictionary containing the sensor data.
    """
    tx_hash = contract_instance.functions.storeData(
        sensor_data['air_quality_pm25'],
        sensor_data['air_quality_pm10'],
        sensor_data['light_intensity'],
        sensor_data['pressure'],
        sensor_data['co2_levels'],
        sensor_data['noise_levels'],
        sensor_data['motion_detected'],
        int(sensor_data['gps_coordinates'][0] * 1e6),  # Convert latitude to integer
        int(sensor_data['gps_coordinates'][1] * 1e6),  # Convert longitude to integer
        sensor_data['battery_level']
    ).transact()
    w3.eth.wait_for_transaction_receipt(tx_hash)

if __name__ == "__main__":
    while True:
        data = generate_sensor_data()
        store_data(data)
        time.sleep(5)
