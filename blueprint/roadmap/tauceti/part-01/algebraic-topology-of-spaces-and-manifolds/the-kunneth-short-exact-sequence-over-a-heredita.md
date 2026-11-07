---
declaration: def
origin: cited
lean: TopCat.singularHomologyKunnethUnitSplitting
statement: formalized
---

# The Künneth short exact sequence over a hereditary commutative ring splits

, so that
`Hₘ₊₁(X × Y; k)` is the direct sum of `⨁_{p + q = m + 1} Hₚ(X; k) ⊗ H_q(Y; k)` and
`⨁_{p + q = m} Tor₁(Hₚ(X; k), H_q(Y; k))`
(`CategoryTheory.ShortComplex.Splitting.isoBinaryBiproduct`).
The splitting depends on chosen splittings of the cycles of the singular chain complexes, and need
not be natural in `X` and `Y`.

```lean
TopCat.singularHomologyKunnethUnitSplitting.{w} (k : Type w) [CommRing k]
  [∀ (V : ModuleCat k), CategoryTheory.HasProjectiveDimensionLE V 1] (X Y : TopCat) (m : ℕ) :
  (TopCat.singularHomologyKunnethUnitShortComplex k X Y m).Splitting
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TopCat.singularHomologyKunnethUnitSplitting`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Kunneth/Sequence.html#TopCat.singularHomologyKunnethUnitSplitting).

## Sources

- [Tau Ceti documentation: `TopCat.singularHomologyKunnethUnitSplitting`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Kunneth/Sequence.html#TopCat.singularHomologyKunnethUnitSplitting)
- [Source of `TopCat.singularHomologyKunnethUnitSplitting` in TauCeti/AlgebraicTopology/Singular/Kunneth/Sequence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Singular/Kunneth/Sequence.lean#L410)
- [Tau Ceti roadmap status: Algebraic topology of spaces and manifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicTopology/STATUS.md)
