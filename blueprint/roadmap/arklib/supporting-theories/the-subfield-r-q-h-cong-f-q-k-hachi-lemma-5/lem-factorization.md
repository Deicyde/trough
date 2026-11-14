---
declaration: lemma
origin: cited
lean: ArkLib.Lattices.CyclotomicModulus.exists_irreducible_factorization
statement: formalized
---

# Factor existence

For $q \equiv 5 \pmod 8$, $X^{2^\alpha}+1 = p_1 \cdot p_2$ over $\mathbb{F}_q$ with $p_1, p_2$ coprime and irreducible. (Extracted from the two normalized factors; coprimality of the distinct monic irreducibles via `Irreducible.coprime_iff_not_dvd`.)

## Depends on

- [Two irreducible factors](lem-two-factors.md)

## Lean

Stated as [`ArkLib.Lattices.CyclotomicModulus.exists_irreducible_factorization`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ArkLib.Lattices.CyclotomicModulus.exists_irreducible_factorization); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: lattices/hachi_subfield.tex, line 150](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/lattices/hachi_subfield.tex#L150)
