---
declaration: def
origin: cited
lean: TauCeti.FiniteCoveringSpace.profiniteCompletionAutFiberFunctorMulEquiv
statement: formalized
---

# The profinite completion of `π₁(X, x₀)` is the automorphism group of the finite-cover fibre functor

```lean
TauCeti.FiniteCoveringSpace.profiniteCompletionAutFiberFunctorMulEquiv.{u} {X : TopCat} (x₀ : ↑X)
  [PathConnectedSpace ↑X] [LocallyPathConnectedSpace ↑X]
  [TauCeti.SemilocallySimplyConnectedSpace ↑X] :
  ↑(ProfiniteGrp.ProfiniteCompletion.completion ↧(FundamentalGroup (↑X) x₀)).toProfinite.toTop ≃*
    CategoryTheory.Aut (TauCeti.FiniteCoveringSpace.fiberFunctor x₀)
```

## Depends on

- [TauCeti.CoveringSpace](tauceti-coveringspace.md)

## Proof depends on

- [TauCeti.CoveringSpace.mk](tauceti-coveringspace-mk.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteCoveringSpace.profiniteCompletionAutFiberFunctorMulEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/UniversalCover/Classification/ProfiniteFiberFunctor.html#TauCeti.FiniteCoveringSpace.profiniteCompletionAutFiberFunctorMulEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteCoveringSpace.profiniteCompletionAutFiberFunctorMulEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/UniversalCover/Classification/ProfiniteFiberFunctor.html#TauCeti.FiniteCoveringSpace.profiniteCompletionAutFiberFunctorMulEquiv)
- [Source of `TauCeti.FiniteCoveringSpace.profiniteCompletionAutFiberFunctorMulEquiv` in TauCeti/AlgebraicTopology/UniversalCover/Classification/ProfiniteFiberFunctor.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/UniversalCover/Classification/ProfiniteFiberFunctor.lean#L92)
- [Tau Ceti roadmap status: Universal covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/UniversalCovers/STATUS.md)
