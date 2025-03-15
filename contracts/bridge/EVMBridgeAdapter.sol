// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
contract EVMBridgeAdapter {
    address public immutable ccipRouter;
    address public immutable hypernovaIntent;
    mapping(uint64 => bytes32) public chainSelectors;
    event MessageSent(uint64 indexed chain, bytes32 indexed msgId, bytes payload);
    event MessageReceived(uint64 indexed chain, bytes32 indexed msgId, bytes payload);
    constructor(address _router, address _hi) { ccipRouter = _router; hypernovaIntent = _hi; }
    function setChainSelector(uint64 chainId, bytes32 sel) external { chainSelectors[chainId] = sel; }
    function sendMessage(uint64 chain, bytes calldata payload) external returns (bytes32) {
        bytes32 mid = keccak256(abi.encodePacked(block.timestamp, msg.sender, payload));
        emit MessageSent(chain, mid, payload); return mid;
    }
    function receiveMessage(uint64 chain, bytes32 mid, bytes calldata payload) external {
        emit MessageReceived(chain, mid, payload);
    }
}