---
declaration: def
origin: cited
lean: TauCeti.brauerCohomologyEquiv
statement: formalized
---

# The comparison isomorphism

`Br(K) ≃ H²_cont(G_K, (Kˢ)ˣ)` with Mathlib's continuous
cohomology, for `K` in any universe: the explicit comparison `brauerExplicitH2Equiv K` followed by
`explicitH2AddEquivContinuousCohomology`. It is characterized by
`brauerCohomologyEquiv_crossedProductClass`: the class of the crossed product of a cocycle of a
finite Galois `L ⊆ Kˢ` goes to the continuous class of the inflation of that cocycle; see
`brauerCohomologyEquiv_unique`.

```lean
TauCeti.brauerCohomologyEquiv.{u} (K : Type u) [Field K] :
  Additive (BrauerGroup K) ≃+
    ↑(continuousCohomology 2
          (TauCeti.ofDiscreteModule ℤ (TauCeti.AbsoluteGaloisGroup K)
            (TauCeti.UnitsCoeff K))).toModuleCat
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.brauerCohomologyEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/CrossedProduct/Comparison.html#TauCeti.brauerCohomologyEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.brauerCohomologyEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/CrossedProduct/Comparison.html#TauCeti.brauerCohomologyEquiv)
- [Source of `TauCeti.brauerCohomologyEquiv` in TauCeti/Algebra/CrossedProduct/Comparison.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/CrossedProduct/Comparison.lean#L268)
- [Tau Ceti roadmap status: Quadratic forms and cohomological invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuadraticFormInvariants/STATUS.md)
