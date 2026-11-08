---
declaration: theorem
origin: cited
lean: TauCeti.cartanProjection_map_incl
statement: formalized
proof: formalized
---

# The Cartan projection restricts to the identity on `U(H)`

```lean
TauCeti.cartanProjection_map_incl.{u, v} {K : Type u} {L : Type v} [Field K] [CharZero K]
  [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] [FiniteDimensional K L]
  {H : LieSubalgebra K L} [H.IsCartanSubalgebra] [LieModule.IsTriangularizable K (↥H) L]
  (b : (LieAlgebra.IsKilling.rootSystem H).Base) (h : UniversalEnvelopingAlgebra K ↥H) :
  (TauCeti.cartanProjection b) ((TauCeti.UniversalEnvelopingAlgebra.map K H.incl) h) = h
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.cartanProjection_map_incl`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/HarishChandra.html#TauCeti.cartanProjection_map_incl).

## Sources

- [Tau Ceti documentation: `TauCeti.cartanProjection_map_incl`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/HarishChandra.html#TauCeti.cartanProjection_map_incl)
- [Source of `TauCeti.cartanProjection_map_incl` in TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/HarishChandra.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/HarishChandra.lean#L121)
