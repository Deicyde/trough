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
- [Source of `TauCeti.FiniteCoveringSpace.profiniteCompletionAutFiberFunctorMulEquiv` in TauCeti/AlgebraicTopology/UniversalCover/Classification/ProfiniteFiberFunctor.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/UniversalCover/Classification/ProfiniteFiberFunctor.lean#L92)
- [Tau Ceti roadmap status: Universal covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/UniversalCovers/STATUS.md)
