---
declaration: section
origin: cited
lean: MathlibExt.Algebra.CompleteLocalRingReconstructionWanted.conjecture, MathlibExt.Algebra.CompleteLocalRingReconstructionWanted.conjecture_refuted
statement: formalized
---

# Reconstructing complete local rings from quotients

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/reconstructing-complete-local-rings-from-quotien/index.html).

## Complete local ring reconstruction conjecture

The statement that any two commutative
Noetherian local rings $A$ and $B$, with maximal ideals $\mathfrak m_A$ and $\mathfrak m_B$, that
are complete and Hausdorff for the $\mathfrak m_A$-adic and $\mathfrak m_B$-adic topologies are
isomorphic as rings whenever $A/\mathfrak m_A^r$ and $B/\mathfrak m_B^r$ are isomorphic as rings
for every natural number $r$.

## Sources

- OWR-1453-004.

Formalized by `MathlibExt.Algebra.CompleteLocalRingReconstructionWanted.conjecture`, a definition declared in [WantedExt/Algebra/CompleteLocalRingReconstructionWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/CompleteLocalRingReconstructionWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/reconstructing-complete-local-rings-from-quotien/index.html#conjecture).

## The complete local ring reconstruction conjecture is false

There exist commutative
Noetherian local rings $A$ and $B$, with maximal ideals $\mathfrak m_A$ and $\mathfrak m_B$, that
are complete and Hausdorff for the $\mathfrak m_A$-adic and $\mathfrak m_B$-adic topologies, such
that $A/\mathfrak m_A^r$ and $B/\mathfrak m_B^r$ are isomorphic as rings for every natural number
$r$, but $A$ and $B$ are not isomorphic as rings.

Van den Dries proves that such rings are isomorphic when the residue field is algebraic over its
prime field, and reports examples by Gabber showing that the answer is no in general.

## Sources

- Lou van den Dries, Isomorphism of complete local noetherian rings and strong approximation, Proc. Amer. Math. Soc. 136 (2008), 3435-3448, https://doi.org/10.1090/S0002-9939-08-09401-X.

Stated but not proved: `MathlibExt.Algebra.CompleteLocalRingReconstructionWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Algebra/CompleteLocalRingReconstructionWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/CompleteLocalRingReconstructionWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/reconstructing-complete-local-rings-from-quotien/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reconstructing complete local rings from quotients](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/reconstructing-complete-local-rings-from-quotien/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/local-rings/reconstructing-complete-local-rings-from-quotien)
