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
- [Source of `TauCeti.CoveringSpace.autFiberFunctorMulEquiv` in TauCeti/AlgebraicTopology/UniversalCover/Classification/FiberFunctor.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/UniversalCover/Classification/FiberFunctor.lean#L113)
- [Tau Ceti roadmap status: Universal covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/UniversalCovers/STATUS.md)
