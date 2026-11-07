---
declaration: theorem
origin: cited
lean: TauCeti.MooreLoopSpace.isAspherical_iff_double_singularHomology
statement: formalized
proof: formalized
---

# Barraud--Damian--Humilière--Oancea, Lemma 3.41 (Moore singular homology)

A path-connected
space `X` is aspherical if and only if its double Moore loop space is path connected with vanishing
positive-degree integral singular homology.

```lean
TauCeti.MooreLoopSpace.isAspherical_iff_double_singularHomology {X : Type} [TopologicalSpace X]
  (x : X) [PathConnectedSpace X] :
  TauCeti.IsAspherical X x ↔
    PathConnectedSpace (TauCeti.MooreLoopSpace (TauCeti.MooreLoopSpace X x) 1) ∧
      ∀ (m : ℕ),
        m ≠ 0 →
          CategoryTheory.Limits.IsZero
            (HomologicalComplex.homology
              ((TauCeti.singularChains ℤ).obj
                ↧(TauCeti.MooreLoopSpace (TauCeti.MooreLoopSpace X x) 1))
              m)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MooreLoopSpace.isAspherical_iff_double_singularHomology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/LoopSpace/Aspherical.html#TauCeti.MooreLoopSpace.isAspherical_iff_double_singularHomology).

## Sources

- [Tau Ceti documentation: `TauCeti.MooreLoopSpace.isAspherical_iff_double_singularHomology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/LoopSpace/Aspherical.html#TauCeti.MooreLoopSpace.isAspherical_iff_double_singularHomology)
- [Source of `TauCeti.MooreLoopSpace.isAspherical_iff_double_singularHomology` in TauCeti/AlgebraicTopology/Homotopy/LoopSpace/Aspherical.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Homotopy/LoopSpace/Aspherical.lean#L303)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DGFloer/STATUS.md)
