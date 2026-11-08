---
declaration: theorem
origin: cited
lean: TauCeti.cartanProjection_mem_pbwFiltrationPrevious
statement: formalized
proof: formalized
---

# The Cartan projection preserves a strict PBW degree bound

the companion of
`TauCeti.cartanProjection_mem_pbwFiltration` for the step preceding degree `n`.

```lean
TauCeti.cartanProjection_mem_pbwFiltrationPrevious.{u, v} {K : Type u} {L : Type v} [Field K]
  [CharZero K] [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] [FiniteDimensional K L]
  {H : LieSubalgebra K L} [H.IsCartanSubalgebra] [LieModule.IsTriangularizable K (↥H) L]
  (b : (LieAlgebra.IsKilling.rootSystem H).Base) {n : ℕ} {u : UniversalEnvelopingAlgebra K L}
  (hu : u ∈ TauCeti.UniversalEnvelopingAlgebra.pbwFiltrationPrevious K L n) :
  (TauCeti.cartanProjection b) u ∈ TauCeti.UniversalEnvelopingAlgebra.pbwFiltrationPrevious K (↥H) n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.cartanProjection_mem_pbwFiltrationPrevious`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/LeadingTerm.html#TauCeti.cartanProjection_mem_pbwFiltrationPrevious).

## Sources

- [Tau Ceti documentation: `TauCeti.cartanProjection_mem_pbwFiltrationPrevious`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/LeadingTerm.html#TauCeti.cartanProjection_mem_pbwFiltrationPrevious)
- [Source of `TauCeti.cartanProjection_mem_pbwFiltrationPrevious` in TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/LeadingTerm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/LeadingTerm.lean#L131)
