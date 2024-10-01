// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
contract RHStaking {
    struct Staker { uint256 amount; uint256 startTime; uint256 lockPeriod; uint256 rewards; }
    mapping(address => Staker) public stakers;
    uint256 public rewardRate = 100;
    event Staked(address indexed user, uint256 amount, uint256 lock);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);
    function stake(uint256 amt, uint256 lock) external {
        stakers[msg.sender] = Staker(amt, block.timestamp, lock, 0);
        emit Staked(msg.sender, amt, lock);
    }
    function calcRewards(address user) public view returns (uint256) {
        Staker memory s = stakers[user]; if (s.amount == 0) return 0;
        return (s.amount * rewardRate * (block.timestamp - s.startTime)) / (365 days * 10000);
    }
    function unstake() external {
        Staker storage s = stakers[msg.sender]; require(s.amount > 0, "None");
        uint256 r = calcRewards(msg.sender); s.amount = 0;
        emit Unstaked(msg.sender, s.amount, r);
    }
}