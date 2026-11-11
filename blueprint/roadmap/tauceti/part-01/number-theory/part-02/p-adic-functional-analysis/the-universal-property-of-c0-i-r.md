---
declaration: def
origin: cited
lean: ZeroAtInftyContinuousMap.linearCombinationEquiv
statement: formalized
---

# The universal property of `C₀(I, R)`

Over a commutative ring admitting a multiplicative
pseudo-uniformiser, bounded families `I → M` in a complete ultrametric module correspond to
continuous linear maps `C₀(I, R) →L[R] M`, isometrically for the sup norm and the operator norm.
A family `e` is sent to its linear combination map `a ↦ ∑' i, a i • e i`, and a map `u` to its
values `u (single i 1)` at the unit coordinate vectors.

```lean
ZeroAtInftyContinuousMap.linearCombinationEquiv.{u_1, u_2, u_3} {I : Type u_1} (R : Type u_2)
  (M : Type u_3) [TopologicalSpace I] [DiscreteTopology I] [NormedCommRing R]
  [TauCeti.NormedRing.IsTate R] [NormedAddCommGroup M] [_root_.Module R M] [IsBoundedSMul R M]
  [IsUltrametricDist M] [CompleteSpace M] [DecidableEq I] :
  ↥(lp (fun x => M) ⊤) ≃ₗᵢ[R] ZeroAtInftyContinuousMap I R →L[R] M
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ZeroAtInftyContinuousMap.linearCombinationEquiv`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/ZeroAtInfty/LinearCombination.html#ZeroAtInftyContinuousMap.linearCombinationEquiv).

## Sources

- [Tau Ceti documentation: `ZeroAtInftyContinuousMap.linearCombinationEquiv`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/ZeroAtInfty/LinearCombination.html#ZeroAtInftyContinuousMap.linearCombinationEquiv)
- [Source of `ZeroAtInftyContinuousMap.linearCombinationEquiv` in TauCeti/Topology/ContinuousMap/ZeroAtInfty/LinearCombination.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/ContinuousMap/ZeroAtInfty/LinearCombination.lean#L279)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
