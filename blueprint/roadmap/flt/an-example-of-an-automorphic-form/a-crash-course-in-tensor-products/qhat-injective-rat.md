---
declaration: lemma
origin: cited
lean: QHat.injective_rat
statement: formalized
proof: formalized
---

# QHat.injective_rat

The ring homomorphism $\mathbb{Q}\to\widehat{\mathbb{Q}}$ sending $q$ to $q\otimes_t 1$ is injective.

## Depends on

- [QHat](../widehat-q-and-tensor-products/qhat.md)
- [ZHat.commRing](../widehat-z/zhat-commring.md)

## Proof

We have seen that the map from $\mathbb{Z}$ to $\widehat{\mathbb{Z}}$ is injective. Now $\mathbb{Q}$ is a flat $\mathbb{Z}$-module, because it's torsion-free, so tensoring up we deduce that the map from $\mathbb{Q}=\mathbb{Q}\otimes\mathbb{Z}$ to $\widehat{\mathbb{Q}}=\mathbb{Q}\otimes\widehat{\mathbb{Z}}$ is also injective. There is no doubt a more elementary proof of this fact.

## Lean

Formalized as [`QHat.injective_rat`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/QHat.injective_rat).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch05automorphicformexample.tex, line 404](https://github.com/ImperialCollegeLondon/FLT/blob/019805815d7da565ed1e9f427b6fbd0cbc9d00d3/blueprint/src/chapter/ch05automorphicformexample.tex#L404)
