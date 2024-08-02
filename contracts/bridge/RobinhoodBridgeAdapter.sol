// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
contract RobinhoodBridgeAdapter {
    address public immutable relayDepository;
    address public immutable hypernovaIntent;
    mapping(bytes32 => bool) public processedDeposits;
    event DepositInitiated(bytes32 indexed id, address indexed user, uint256 amount, bytes targetData);
    event DepositConfirmed(bytes32 indexed id, bytes32 targetTxHash);
    constructor(address _rd, address _hi) { relayDepository = _rd; hypernovaIntent = _hi; }
    function depositNative(bytes calldata data) external payable {
        bytes32 id = keccak256(abi.encodePacked(msg.sender, block.timestamp, msg.value));
        processedDeposits[id] = true;
        (bool s,) = relayDepository.call{value: msg.value}(data);
        require(s, "Deposit failed");
        emit DepositInitiated(id, msg.sender, msg.value, data);
    }
    function confirmDeposit(bytes32 id, bytes32 txHash) external {
        require(processedDeposits[id], "Not found");
        emit DepositConfirmed(id, txHash);
    }
}