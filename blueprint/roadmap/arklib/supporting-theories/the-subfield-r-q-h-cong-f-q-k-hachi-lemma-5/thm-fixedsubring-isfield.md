---
declaration: theorem
origin: cited
lean: ArkLib.Lattices.CyclotomicModulus.fixedSubring_isField
statement: formalized
proof: formalized
---

# $R_q^H$ is a field

For $q$ prime, $q \equiv 5 \pmod 8$, $2k \mid d$, the ring $R_q^H$ is a field.

## Depends on

- [$R_q^{\sigma_{-1}}$ is a field](thm-conjfixedsubring-isfield.md)
- [$R_q^H \le R_q^{\sigma_{-1}}$](lem-fixedsubring-le-conjfixedsubring.md)

## Proof

$R_q^H \subseteq R_q^{\sigma_{-1}}$ (Lemma [$R_q^H \le R_q^{\sigma_{-1}}$](lem-fixedsubring-le-conjfixedsubring.md)), and $R_q^{\sigma_{-1}}$ is a field (Theorem [$R_q^{\sigma_{-1}}$ is a field](thm-conjfixedsubring-isfield.md)). A subring of a field is an integral domain (Lemma [Subring of a domain is a domain](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/lattices/hachi_subfield.tex#L70)); $R_q^H$ is finite (`fixedSubring.fintype`) and nontrivial, hence a field (Lemma [Finite domain is a field](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/lattices/hachi_subfield.tex#L76)).

## Lean

Formalized as [`ArkLib.Lattices.CyclotomicModulus.fixedSubring_isField`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ArkLib.Lattices.CyclotomicModulus.fixedSubring_isField).

## Sources

- [ArkLib blueprint: lattices/hachi_subfield.tex, line 81](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/lattices/hachi_subfield.tex#L81)
