// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
contract VirtualsBridgeAdapter {
    address public immutable virtualsHub;
    address public immutable hypernovaIntent;
    struct AgentExec { bytes32 intentId; address agent; bytes params; bool completed; uint256 ts; }
    mapping(bytes32 => AgentExec) public executions;
    event AgentDispatched(bytes32 indexed id, address indexed agent, bytes32 intentId);
    event AgentCompleted(bytes32 indexed id, bytes32 indexed intentId, bytes result);
    constructor(address _vh, address _hi) { virtualsHub = _vh; hypernovaIntent = _hi; }
    function dispatchAgent(bytes32 intentId, address agent, bytes calldata params) external returns (bytes32) {
        bytes32 eid = keccak256(abi.encodePacked(intentId, agent, block.timestamp));
        executions[eid] = AgentExec(intentId, agent, params, false, block.timestamp);
        emit AgentDispatched(eid, agent, intentId); return eid;
    }
    function completeExecution(bytes32 eid, bytes calldata result) external {
        require(!executions[eid].completed, "Done"); executions[eid].completed = true;
        emit AgentCompleted(eid, executions[eid].intentId, result);
    }
}