# Contrato Inteligente: Ejemplo

## Descripción
Este contrato almacena un valor en la blockchain.

## Código
```solidity
pragma solidity ^0.8.0;

contract ExampleContract {
    uint256 public value;

    function setValue(uint256 _value) public {
        value = _value;
    }
}