---
declaration: theorem
origin: cited
lean: TauCeti.IsAffinoidAlgebra.exists_finite_injective
statement: formalized
proof: formalized
---

# Affinoid Noether normalisation

Every nonzero affinoid algebra over a complete
ultrametric field is finite over an injectively embedded finite-variable Tate algebra.
Finiteness uses the algebra structure induced by the displayed map.

```lean
TauCeti.IsAffinoidAlgebra.exists_finite_injective.{u, u_1} {K : Type u} [NormedField K]
  [IsUltrametricDist K] [CompleteSpace K] {A : Type u_1} [CommRing A] [Algebra K A] [Nontrivial A]
  (hA : TauCeti.IsAffinoidAlgebra K A) : ∃ n g, Function.Injective ⇑g ∧ g.Finite
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAffinoidAlgebra.exists_finite_injective`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/NoetherNormalization.html#TauCeti.IsAffinoidAlgebra.exists_finite_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAffinoidAlgebra.exists_finite_injective`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/NoetherNormalization.html#TauCeti.IsAffinoidAlgebra.exists_finite_injective)
- [Source of `TauCeti.IsAffinoidAlgebra.exists_finite_injective` in TauCeti/RingTheory/Affinoid/NoetherNormalization.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Affinoid/NoetherNormalization.lean#L160)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
