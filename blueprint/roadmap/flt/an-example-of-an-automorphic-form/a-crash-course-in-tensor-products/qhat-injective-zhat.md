---
declaration: lemma
origin: cited
lean: QHat.injective_zHat
statement: formalized
proof: formalized
---

# QHat.injective\_zHat

The ring homomorphism $\widehat{\mathbb{Z}}\to\widehat{\mathbb{Q}}$ sending $z$ to $1\otimes_t z$ is injective.

## Depends on

- [QHat](../widehat-q-and-tensor-products/qhat.md)
- [ZHat.torsionfree](../widehat-z/zhat-torsionfree.md)

## Proof

The map from $\mathbb{Z}$ to $\mathbb{Q}$ is injective, and we have seen that $\widehat{\mathbb{Z}}$ is a torsion-free and thus flat $\mathbb{Z}$-module, so the map from $\widehat{\mathbb{Z}}$ to $\widehat{\mathbb{Q}}$ is also injective.

## Lean

Formalized as [`QHat.injective_zHat`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/QHat.injective_zHat).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch05automorphicformexample.tex, line 420](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch05automorphicformexample.tex#L420)
