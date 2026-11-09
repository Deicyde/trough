---
declaration: def
origin: cited
lean: TauCeti.groupCohomologyOddEquivTorsionBy
statement: formalized
---

# Odd-degree cohomology of the trivial action

When `C_m` acts trivially on `T`, its
cohomology in odd degree is the `m`-torsion `T[m]`: the class of a norm-zero element `x`
corresponds to `x` itself.

```lean
TauCeti.groupCohomologyOddEquivTorsionBy (T : Type) [AddCommGroup T] (m : ℕ) [NeZero m] (i : ℕ)
  (hi : Odd i) :
  ↑(groupCohomology ((AddEquiv.refl T).cyclicRep ⋯) i) ≃ₗ[ℤ] ↥(Submodule.torsionBy ℤ T ↑m)
```

## Depends on

- [AddEquiv.cyclicRep](addequiv-cyclicrep.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.groupCohomologyOddEquivTorsionBy`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.html#TauCeti.groupCohomologyOddEquivTorsionBy).

## Sources

- [Tau Ceti documentation: `TauCeti.groupCohomologyOddEquivTorsionBy`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.html#TauCeti.groupCohomologyOddEquivTorsionBy)
- [Source of `TauCeti.groupCohomologyOddEquivTorsionBy` in TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/GroupCohomology/CyclicAutomorphism.lean#L637)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexTori/STATUS.md)
