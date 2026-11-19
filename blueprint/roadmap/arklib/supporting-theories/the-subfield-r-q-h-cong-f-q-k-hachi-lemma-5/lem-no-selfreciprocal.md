---
declaration: lemma
origin: cited
lean: ArkLib.Lattices.CyclotomicModulus.no_selfReciprocal_factor
statement: formalized
---

# No self-reciprocal factor

For $q \equiv 5 \pmod 8$, reversal swaps the two factors: if $X^{2^\alpha}+1 = p_1 p_2$ with $p_1, p_2$ irreducible, then $p_1^{\mathrm{rev}}$ is associated to $p_2$. This is the step carrying the $-1 \notin \langle q\rangle$ root-orbit content. The root set of $p_1$ is a single Frobenius orbit $=$ a coset of $\langle q\rangle$; were $p_1^{\mathrm{rev}} \sim p_1$ it would be closed under $\zeta \mapsto \zeta^{-1}$, i.e. $-1 \in \langle q\rangle$, contradicting Lemma [$-1 \notin \langle q\rangle$](lem-neg-one-notmem.md); as reversal permutes the two factors of the self-reciprocal $X^{2^\alpha}+1$, it sends $p_1$ to $p_2$.

## Depends on

- [Order of $q$ modulo the conductor](lem-order-q.md)
- [$-1 \notin \langle q\rangle$](lem-neg-one-notmem.md)

## Lean

Stated as [`ArkLib.Lattices.CyclotomicModulus.no_selfReciprocal_factor`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ArkLib.Lattices.CyclotomicModulus.no_selfReciprocal_factor); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: lattices/hachi_subfield.tex, line 176](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/lattices/hachi_subfield.tex#L176)
