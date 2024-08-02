// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title HyperNovaIntent
 * @notice Core intent declaration and settlement contract for cross-chain infrastructure.
 * @dev Users declare intents, solvers compete to fulfill them. Supports Robinhood Chain, EVM chains, and Virtuals.
 */
contract HyperNovaIntent {
    enum IntentStatus { Pending, Active, Fulfilled, Expired, Cancelled, Disputed }
    enum ChainType { Robinhood, Ethereum, Base, Arbitrum, Optimism, Polygon, Virtuals }
    
    struct Intent {
        bytes32 id; address user; ChainType sourceChain; ChainType targetChain;
        bytes sourceCalldata; bytes targetCalldata; uint256 deadline; uint256 reward;
        address tokenIn; address tokenOut; uint256 amountIn; uint256 minAmountOut;
        IntentStatus status; address solver; uint256 timestamp;
    }
    
    struct Solver { address addr; string name; uint256 stake; uint256 totalFulfilled; uint256 successRate; bool active; }
    
    mapping(bytes32 => Intent) public intents;
    mapping(address => Solver) public solvers;
    address public owner;
    uint256 public intentCount;
    bytes32[] public intentIds;
    
    event IntentCreated(bytes32 indexed id, address indexed user, ChainType source, ChainType target, uint256 amount, uint256 reward);
    event IntentFulfilled(bytes32 indexed id, address indexed solver, uint256 amountOut);
    event IntentCancelled(bytes32 indexed id);
    event SolverRegistered(address indexed solver, string name, uint256 stake);
    event CrossChainSettlement(bytes32 indexed intentId, bytes32 targetTxHash, ChainType targetChain);
    
    constructor() { owner = msg.sender; }
    
    function createIntent(ChainType src, ChainType tgt, bytes calldata sc, bytes calldata tc, uint256 dl, uint256 rw, address ti, address to, uint256 amt, uint256 minOut) external payable returns (bytes32) {
        bytes32 id = keccak256(abi.encodePacked(msg.sender, block.timestamp, intentCount));
        Intent storage intent = intents[id];
        intent.id = id; intent.user = msg.sender; intent.sourceChain = src; intent.targetChain = tgt;
        intent.sourceCalldata = sc; intent.targetCalldata = tc; intent.deadline = dl; intent.reward = rw;
        intent.tokenIn = ti; intent.tokenOut = to; intent.amountIn = amt; intent.minAmountOut = minOut;
        intent.status = IntentStatus.Pending; intent.timestamp = block.timestamp;
        intentIds.push(id); intentCount++;
        emit IntentCreated(id, msg.sender, src, tgt, amt, rw);
        return id;
    }
    
    function registerSolver(string calldata name, uint256 stake) external {
        solvers[msg.sender] = Solver(msg.sender, name, stake, 0, 1000, true);
        emit SolverRegistered(msg.sender, name, stake);
    }
    
    function fulfillIntent(bytes32 id, uint256 amountOut, bytes32 txHash) external {
        Intent storage intent = intents[id];
        require(intent.status == IntentStatus.Pending || intent.status == IntentStatus.Active, "Invalid");
        require(amountOut >= intent.minAmountOut, "Slippage");
        intent.status = IntentStatus.Fulfilled; intent.solver = msg.sender;
        solvers[msg.sender].totalFulfilled++;
        emit IntentFulfilled(id, msg.sender, amountOut);
        emit CrossChainSettlement(id, txHash, intent.targetChain);
    }
    
    function cancelIntent(bytes32 id) external {
        require(msg.sender == intents[id].user, "Not owner");
        intents[id].status = IntentStatus.Cancelled;
        emit IntentCancelled(id);
    }
}