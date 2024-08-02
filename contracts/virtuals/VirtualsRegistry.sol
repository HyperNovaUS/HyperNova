// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
contract VirtualsRegistry {
    struct Agent { address id; string name; string desc; address creator; uint256 stake; uint256 executions; bool active; uint256 regAt; }
    mapping(address => Agent) public agents;
    address[] public agentList;
    event AgentRegistered(address indexed id, string name, address indexed creator);
    function registerAgent(string calldata name, string calldata desc) external returns (address) {
        address aid = address(uint160(uint256(keccak256(abi.encodePacked(msg.sender, name, block.timestamp)))));
        agents[aid] = Agent(aid, name, desc, msg.sender, 0, 0, true, block.timestamp);
        agentList.push(aid); emit AgentRegistered(aid, name, msg.sender); return aid;
    }
    function getAllAgents() external view returns (Agent[] memory) {
        Agent[] memory r = new Agent[](agentList.length);
        for (uint i = 0; i < agentList.length; i++) r[i] = agents[agentList[i]];
        return r;
    }
}