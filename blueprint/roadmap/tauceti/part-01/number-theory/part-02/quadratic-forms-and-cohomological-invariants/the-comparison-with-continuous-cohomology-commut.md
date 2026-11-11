---
declaration: theorem
origin: cited
lean: TauCeti.brauerCohomologyEquiv_uliftEquiv
statement: formalized
proof: formalized
---

# The comparison with continuous cohomology commutes with universe lifting

Scalar extension
of Brauer classes from `K` to `ULift K` corresponds, under `brauerCohomologyEquiv`, to transport of
Mathlib's continuous second Galois cohomology along `K ≃+* ULift K`.

```lean
TauCeti.brauerCohomologyEquiv_uliftEquiv.{u, w} {K : Type u} [Field K] (x : BrauerGroup K) :
  (TauCeti.brauerCohomologyEquiv (ULift.{w, u} K))
      (Additive.ofMul ((TauCeti.BrauerGroup.uliftEquiv K) x)) =
    ULift.ringEquiv.symm.unitsContinuousH2Congr
      ((TauCeti.brauerCohomologyEquiv K) (Additive.ofMul x))
```

## Depends on

- [The comparison isomorphism](the-comparison-isomorphism.md)

## Proof depends on

- [Artin--Wedderburn over a separably closed field](../../../algebra/part-02/central-simple/artin-wedderburn-over-a-separably-closed-field.md)
- [The Skolem-Noether theorem](../../../algebra/part-02/central-simple/the-skolem-noether-theorem.md)
- [Wedderburn-Artin for central simple algebras](../../../algebra/part-02/central-simple/wedderburn-artin-for-central-simple-algebras.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.brauerCohomologyEquiv_uliftEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/CrossedProduct/BaseChange/ULift.html#TauCeti.brauerCohomologyEquiv_uliftEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.brauerCohomologyEquiv_uliftEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/CrossedProduct/BaseChange/ULift.html#TauCeti.brauerCohomologyEquiv_uliftEquiv)
- [Source of `TauCeti.brauerCohomologyEquiv_uliftEquiv` in TauCeti/Algebra/CrossedProduct/BaseChange/ULift.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/CrossedProduct/BaseChange/ULift.lean#L232)
- [Tau Ceti roadmap status: Quadratic forms and cohomological invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuadraticFormInvariants/STATUS.md)
