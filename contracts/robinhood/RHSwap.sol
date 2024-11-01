// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
contract RHSwap {
    struct Order { address maker; address tokenIn; address tokenOut; uint256 amountIn; uint256 amountOut; uint256 deadline; bool filled; }
    mapping(bytes32 => Order) public orders;
    uint256 public orderCount;
    event OrderCreated(bytes32 indexed id, address indexed maker, address ti, address to, uint256 amtIn, uint256 amtOut);
    event OrderFilled(bytes32 indexed id, address indexed taker);
    function createOrder(address ti, address to, uint256 amtIn, uint256 amtOut, uint256 dl) external returns (bytes32) {
        bytes32 id = keccak256(abi.encodePacked(msg.sender, orderCount++, block.timestamp));
        orders[id] = Order(msg.sender, ti, to, amtIn, amtOut, dl, false);
        emit OrderCreated(id, msg.sender, ti, to, amtIn, amtOut); return id;
    }
    function fillOrder(bytes32 id) external {
        require(!orders[id].filled, "Filled"); orders[id].filled = true;
        emit OrderFilled(id, msg.sender);
    }
}