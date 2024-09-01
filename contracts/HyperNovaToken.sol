// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
contract HyperNovaToken is ERC20, Ownable {
    uint256 public constant MAX_SUPPLY = 1_000_000_000 ether;
    constructor() ERC20("HyperNova", "NOVA") Ownable(msg.sender) {
        _mint(msg.sender, 100_000_000 ether);
    }
    function mint(address to, uint256 amt) external onlyOwner {
        require(totalSupply() + amt <= MAX_SUPPLY, "Exceeds");
        _mint(to, amt);
    }
    function burn(uint256 amt) external { _burn(msg.sender, amt); }
}