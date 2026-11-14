---
declaration: lemma
origin: cited
lean: ArkLib.Lattices.CyclotomicModulus.orderOf_q_eq
statement: formalized
proof: formalized
---

# Order of $q$ modulo the conductor

For $q \equiv 5 \pmod 8$ and $\alpha \ge 1$, the multiplicative order of $q$ in $(\mathbb{Z}/2^{\alpha+1})^\times$ is $2^{\alpha-1}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

$(\mathbb{Z}/2^{\alpha+1})^\times \cong \langle -1\rangle \times \langle 5\rangle$ with $|\langle 5\rangle| = 2^{\alpha-1}$. Writing $q \equiv (-1)^a 5^b$, the congruence $q \equiv 5 \pmod 8$ forces $a = 0$ and $b$ odd; since $b$ is odd it is a unit mod $2^{\alpha-1}$, so $q$ generates $\langle 5\rangle$ and $\operatorname{ord}(q) = 2^{\alpha-1}$. The $2$-adic computation is the same lifting-the-exponent toolkit already used in `Galois/Order.lean` (`two_pow_dvd_four_pow_sub_one_iff`).

## Lean

Formalized as [`ArkLib.Lattices.CyclotomicModulus.orderOf_q_eq`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ArkLib.Lattices.CyclotomicModulus.orderOf_q_eq).

## Sources

- [ArkLib blueprint: lattices/hachi_subfield.tex, line 115](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/lattices/hachi_subfield.tex#L115)
