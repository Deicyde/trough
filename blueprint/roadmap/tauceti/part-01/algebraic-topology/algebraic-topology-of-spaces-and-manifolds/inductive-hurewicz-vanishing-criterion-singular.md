---
declaration: theorem
origin: cited
lean: TauCeti.subsingleton_homotopyGroup_of_isZero_homology_singularChains, TauCeti.subsingleton_homotopyGroup_of_isZero_homology_normalizedCubicalChainComplex
statement: formalized
proof: formalized
---

# Inductive Hurewicz vanishing criterion (singular homology)

If `X` is path connected with
trivial `π_ 1 X x` and its integral singular homology vanishes in every degree `n + 2`, then all
homotopy groups `π_ k X x` are trivial.

```lean
TauCeti.subsingleton_homotopyGroup_of_isZero_homology_singularChains {X : Type} [TopologicalSpace X]
  (x : X) [PathConnectedSpace X] [Subsingleton (HomotopyGroup.Pi 1 X x)]
  (hH :
    ∀ (n : ℕ),
      CategoryTheory.Limits.IsZero
        (HomologicalComplex.homology ((TauCeti.singularChains ℤ).obj ↧X) (n + 2)))
  (k : ℕ) : Subsingleton (HomotopyGroup.Pi k X x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.subsingleton_homotopyGroup_of_isZero_homology_singularChains`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Comparison.html#TauCeti.subsingleton_homotopyGroup_of_isZero_homology_singularChains).

## Other forms

**Inductive Hurewicz vanishing criterion (normalized cubical homology).** Formalized in Tau Ceti as [`TauCeti.subsingleton_homotopyGroup_of_isZero_homology_normalizedCubicalChainComplex`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Isomorphism.html#TauCeti.subsingleton_homotopyGroup_of_isZero_homology_normalizedCubicalChainComplex).

```lean
TauCeti.subsingleton_homotopyGroup_of_isZero_homology_normalizedCubicalChainComplex {X : Type}
  [TopologicalSpace X] (x : X) [PathConnectedSpace X] [Subsingleton (HomotopyGroup.Pi 1 X x)]
  (hH :
    ∀ (n : ℕ),
      CategoryTheory.Limits.IsZero
        (HomologicalComplex.homology ((TauCeti.normalizedCubicalChainComplex ℤ).obj ↧X) (n + 2)))
  (k : ℕ) : Subsingleton (HomotopyGroup.Pi k X x)
```

## Sources

- [Tau Ceti documentation: `TauCeti.subsingleton_homotopyGroup_of_isZero_homology_singularChains`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Comparison.html#TauCeti.subsingleton_homotopyGroup_of_isZero_homology_singularChains)
- [Source of `TauCeti.subsingleton_homotopyGroup_of_isZero_homology_singularChains` in TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Comparison.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Comparison.lean#L125)
