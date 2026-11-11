---
declaration: def
origin: cited
lean: TauCeti.CoveringSpace.autFiberFunctorMulEquiv
statement: formalized
---

# The fundamental group of `X` at `x₀` is the automorphism group of the fibre functor over `x₀`

A loop class is sent to the natural automorphism acting on every fibre by monodromy; that this is
a bijection onto all natural automorphisms is Tannaka duality for `π₁(X, x₀)`-sets, transported
along the classification of covering spaces by `π₁(X, x₀)`-sets.

```lean
TauCeti.CoveringSpace.autFiberFunctorMulEquiv.{u} {X : TopCat} (x₀ : ↑X) [PathConnectedSpace ↑X]
  [LocallyPathConnectedSpace ↑X] [TauCeti.SemilocallySimplyConnectedSpace ↑X] :
  FundamentalGroup (↑X) x₀ ≃* CategoryTheory.Aut (TauCeti.CoveringSpace.fiberFunctor x₀)
```

## Depends on

- [TauCeti.CoveringSpace](tauceti-coveringspace.md)

## Proof depends on

- [TauCeti.CoveringSpace.mk](tauceti-coveringspace-mk.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CoveringSpace.autFiberFunctorMulEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/UniversalCover/Classification/FiberFunctor.html#TauCeti.CoveringSpace.autFiberFunctorMulEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.CoveringSpace.autFiberFunctorMulEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/UniversalCover/Classification/FiberFunctor.html#TauCeti.CoveringSpace.autFiberFunctorMulEquiv)
- [Source of `TauCeti.CoveringSpace.autFiberFunctorMulEquiv` in TauCeti/AlgebraicTopology/UniversalCover/Classification/FiberFunctor.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/UniversalCover/Classification/FiberFunctor.lean#L113)
- [Tau Ceti roadmap status: Universal covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/UniversalCovers/STATUS.md)
