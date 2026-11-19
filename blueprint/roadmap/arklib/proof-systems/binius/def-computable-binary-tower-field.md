---
declaration: definition
origin: cited
lean: ConcreteBinaryTower.instFieldConcrete
statement: formalized
---

# Computable Binary Tower Fields

Building upon the abstract definition of binary tower fields, we define a concrete, computable representation of binary tower fields. This construction, which underpins our formalization, represents each element of the field $\mathcal{T}_\iota$ as a bit vector of length $2^\iota$ corresponding to the coefficients of the multilinear $\mathbb{F}_2$-basis.

The arithmetic operations on these bit-vector representations are defined as follows:

- **Addition**: The sum of two elements is defined as the bitwise XOR of their corresponding bit-vector representations.
- **Multiplication (in $\mathcal{T}_\iota$)**: The product of two elements within the same field $\mathcal{T}_\iota$ is defined via a recursive Karatsuba-based algorithm ([Fan and Paar 1997](https://doi.org/10.1109/ISIT.1997.612935)). The complexity of this operation is $\Theta(2^{\log_2(3) \cdot \iota})$.
- **Cross-Level Multiplication**: The product of an element $\alpha \in \mathcal{T}_{\iota+\kappa}$ by a scalar $b \in \mathcal{T}_\iota$ is defined by representing $\alpha$ via its $2^\kappa$ coefficients $(a_u)_{u \in \{0,1\}^\kappa}$ in the $\mathcal{T}_\iota$-basis and performing the multiplication component-wise on those coefficients in the subfield $\mathcal{T}_\iota$. The total complexity is $2^\kappa \cdot \Theta(2^{\log_2(3) \cdot \iota})$.

## Depends on

- [Binary Tower Field](def-binary-tower-field.md)
- [Binary Tower Fields are fields](thm-binary-tower-fields-are-fields.md)

## Lean

Formalized as [`ConcreteBinaryTower.instFieldConcrete`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ConcreteBinaryTower.instFieldConcrete).

## Sources

- [ArkLib blueprint: proof_systems/binius.tex, line 52](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/binius.tex#L52)
