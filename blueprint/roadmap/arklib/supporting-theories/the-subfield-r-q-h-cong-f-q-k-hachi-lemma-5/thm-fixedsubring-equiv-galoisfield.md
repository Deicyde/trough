---
declaration: theorem
origin: cited
lean: ArkLib.Lattices.CyclotomicModulus.fixedSubringEquivGaloisField
statement: formalized
proof: formalized
---

# Lemma 5: field isomorphism

Let $q$ be prime with $q \equiv 5 \pmod 8$ and $2 \cdot 2^\kappa \mid 2^\alpha$. Then there is a ring isomorphism

$$
R_q^{H} \;\cong\; \mathbb{F}_{q^{2^\kappa}} \quad\bigl(\texttt{GaloisField } q\ (2^\kappa)\bigr).
$$

## Depends on

- [$R_q^H$ is a field](thm-fixedsubring-isfield.md)
- [Cardinality, Eq. 7](thm-card-fixedsubring.md)

## Proof

By Theorem [$R_q^H$ is a field](thm-fixedsubring-isfield.md) $R_q^H$ is a finite field, and by Theorem [Cardinality, Eq. 7](thm-card-fixedsubring.md) it has cardinality $q^{2^\kappa}$. Any finite field of cardinality $q^{2^\kappa}$ is isomorphic to $\texttt{GaloisField } q\ (2^\kappa)$ (Lemma [Finite field by cardinality](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/lattices/hachi_subfield.tex#L64)).

## Lean

Formalized as [`ArkLib.Lattices.CyclotomicModulus.fixedSubringEquivGaloisField`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ArkLib.Lattices.CyclotomicModulus.fixedSubringEquivGaloisField).

## Sources

- [ArkLib blueprint: lattices/hachi_subfield.tex, line 36](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/lattices/hachi_subfield.tex#L36)
