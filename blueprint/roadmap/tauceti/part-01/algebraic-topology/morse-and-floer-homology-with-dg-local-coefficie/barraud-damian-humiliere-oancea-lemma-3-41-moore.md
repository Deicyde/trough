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

## Proof depends on

- [The Hurewicz theorem](../algebraic-topology-of-spaces-and-manifolds/the-hurewicz-theorem.md)
- [Inductive Hurewicz vanishing criterion (singular homology)](../algebraic-topology-of-spaces-and-manifolds/inductive-hurewicz-vanishing-criterion-singular.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MooreLoopSpace.isAspherical_iff_double_singularHomology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/LoopSpace/Aspherical.html#TauCeti.MooreLoopSpace.isAspherical_iff_double_singularHomology).

## Sources

- [Tau Ceti documentation: `TauCeti.MooreLoopSpace.isAspherical_iff_double_singularHomology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/LoopSpace/Aspherical.html#TauCeti.MooreLoopSpace.isAspherical_iff_double_singularHomology)
- [Source of `TauCeti.MooreLoopSpace.isAspherical_iff_double_singularHomology` in TauCeti/AlgebraicTopology/Homotopy/LoopSpace/Aspherical.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Homotopy/LoopSpace/Aspherical.lean#L330)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DGFloer/STATUS.md)
