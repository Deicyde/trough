---
declaration: def
origin: cited
lean: TauCeti.weilDifferentialRepresentation
statement: formalized
---

# The automorphism group acting on the Weil differentials

of `F' / k`: the restriction of
the dual of `TauCeti.repartitionRepresentation` to the stable subspace `Ω_F`, so that
`(σ • ω) a = ω (σ⁻¹ • a)`.

```lean
TauCeti.weilDifferentialRepresentation.{u, v, v'} (k : Type u) (F : Type v) (F' : Type v') [Field k]
  [Field F] [Field F'] [Algebra k F] [Algebra k F'] [Algebra F F'] [IsScalarTower k F F'] :
  Representation k Gal(F'/F) ↥(TauCeti.weilDifferentialSpace k F')
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.weilDifferentialRepresentation`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/Automorphism.html#TauCeti.weilDifferentialRepresentation).

## Sources

- [Tau Ceti documentation: `TauCeti.weilDifferentialRepresentation`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/Automorphism.html#TauCeti.weilDifferentialRepresentation)
- [Source of `TauCeti.weilDifferentialRepresentation` in TauCeti/FieldTheory/FunctionField/Differential/Automorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Differential/Automorphism.lean#L144)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicCurves/STATUS.md)
