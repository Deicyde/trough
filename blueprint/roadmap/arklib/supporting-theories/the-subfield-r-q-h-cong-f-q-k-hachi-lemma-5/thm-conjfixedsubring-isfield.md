---
declaration: theorem
origin: cited
lean: ArkLib.Lattices.CyclotomicModulus.conjFixedSubring_isField
statement: formalized
proof: formalized
---

# $R_q^{\sigma_{-1}}$ is a field

For $q$ prime with $q \equiv 5 \pmod 8$ and $\alpha \ge 1$, $R_q^{\sigma_{-1}}$ is a field.

## Depends on

- [Core unit lemma](thm-core-unit.md)

## Proof

Transport along $R_q \cong S$ (`Rq.equivQuotient`), under which $\sigma_{-1}$ becomes $\texttt{galoisAutₛ}$ (`galoisAut_toQuotient`). A nonzero $\sigma_{-1}$-fixed element of $R_q^{\sigma_{-1}}$ maps to a nonzero fixed element of $S$, a unit by Theorem [Core unit lemma](thm-core-unit.md); its inverse is again $\sigma_{-1}$-fixed (apply $\sigma_{-1}$ to $a a^{-1} = 1$ and cancel the unit), so it lies in $R_q^{\sigma_{-1}}$.

## Lean

Formalized as [`ArkLib.Lattices.CyclotomicModulus.conjFixedSubring_isField`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ArkLib.Lattices.CyclotomicModulus.conjFixedSubring_isField).

## Sources

- [ArkLib blueprint: lattices/hachi_subfield.tex, line 212](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/lattices/hachi_subfield.tex#L212)
