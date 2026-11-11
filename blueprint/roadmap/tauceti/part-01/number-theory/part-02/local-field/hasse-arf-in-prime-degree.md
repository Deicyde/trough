---
declaration: theorem
origin: cited
lean: TauCeti.LocalFieldsRamification.UpperJump.exists_eq_intCast_of_finrank_prime, TauCeti.LocalFieldsRamification.hasseArf, TauCeti.LocalFieldsRamification.UpperJump.exists_eq_intCast_of_isPGroup, TauCeti.LocalFieldsRamification.UpperJump.exists_eq_intCast_of_exponent_prime
statement: formalized
proof: formalized
---

# Hasse--Arf in prime degree

Every upper ramification break of a finite Galois extension
of prime degree is an integer.

```lean
TauCeti.LocalFieldsRamification.UpperJump.exists_eq_intCast_of_finrank_prime.{u_1, u_2}
  {K : Type u_1} {L : Type u_2} [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] [Field L] [ValuativeRel L] [TopologicalSpace L]
  [IsNonarchimedeanLocalField L] [Algebra K L] [ValuativeExtension K L] [Module.Finite K L]
  [IsGalois K L] {u : ↑TauCeti.LocalFieldsRamification.RamificationIndexDomain}
  (hu : TauCeti.LocalFieldsRamification.UpperJump K L u)
  (hdegree : Nat.Prime (Module.finrank K L)) : ∃ z, ↑u = ↑z
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [Herbrand's theorem in the upper numbering](../../part-01/local-fields-and-ramification/herbrands-theorem-in-the-upper-numbering.md)
- [Hilbert's formula, truncated](hilberts-formula-truncated.md)
- [Hilbert's Theorem 90 for cyclic extensions](../../../field-theory/galois/hilberts-theorem-90-for-cyclic-extensions.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.LocalFieldsRamification.upperJump_iff_exists_isCyclic_intermediateField](../../part-01/local-fields-and-ramification/tauceti-localfieldsramification-upperjump-iff-ex.md)
- [The third isomorphism theorem for coset spaces](../../../group-theory/other-results/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LocalFieldsRamification.UpperJump.exists_eq_intCast_of_finrank_prime`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/HasseArf/PrimeDegree.html#TauCeti.LocalFieldsRamification.UpperJump.exists_eq_intCast_of_finrank_prime).

## Other forms

**Hasse--Arf.** Formalized in Tau Ceti as [`TauCeti.LocalFieldsRamification.hasseArf`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/HasseArf/Abelian.html#TauCeti.LocalFieldsRamification.hasseArf).

```lean
TauCeti.LocalFieldsRamification.hasseArf.{u, v} (K : Type u) (L : Type v) [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] [Field L] [ValuativeRel L]
  [TopologicalSpace L] [IsNonarchimedeanLocalField L] [Algebra K L] [ValuativeExtension K L]
  [Module.Finite K L] [IsAbelianGalois K L]
  {w : ↑TauCeti.LocalFieldsRamification.RamificationIndexDomain}
  (hw : TauCeti.LocalFieldsRamification.UpperJump K L w) : ∃ z, ↑w = ↑z
```

**Hasse--Arf for cyclic extensions of prime-power degree.** Formalized in Tau Ceti as [`TauCeti.LocalFieldsRamification.UpperJump.exists_eq_intCast_of_isPGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/HasseArf/CyclicPGroup.html#TauCeti.LocalFieldsRamification.UpperJump.exists_eq_intCast_of_isPGroup).

```lean
TauCeti.LocalFieldsRamification.UpperJump.exists_eq_intCast_of_isPGroup.{u, v} {K : Type u}
  {L : Type v} [Field K] [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K]
  [Field L] [ValuativeRel L] [TopologicalSpace L] [IsNonarchimedeanLocalField L] [Algebra K L]
  [ValuativeExtension K L] [Module.Finite K L] [IsGalois K L] [IsCyclic Gal(L/K)] {p : ℕ}
  [Fact (Nat.Prime p)] (hp : IsPGroup p Gal(L/K))
  {u : ↑TauCeti.LocalFieldsRamification.RamificationIndexDomain}
  (hu : TauCeti.LocalFieldsRamification.UpperJump K L u) : ∃ z, ↑u = ↑z
```

**Hasse--Arf for elementary abelian extensions.** Formalized in Tau Ceti as [`TauCeti.LocalFieldsRamification.UpperJump.exists_eq_intCast_of_exponent_prime`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/CyclicReduction.html#TauCeti.LocalFieldsRamification.UpperJump.exists_eq_intCast_of_exponent_prime).

```lean
TauCeti.LocalFieldsRamification.UpperJump.exists_eq_intCast_of_exponent_prime.{u_1, u_2}
  {K : Type u_1} {L : Type u_2} [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] [Field L] [ValuativeRel L] [TopologicalSpace L]
  [IsNonarchimedeanLocalField L] [Algebra K L] [ValuativeExtension K L] [Module.Finite K L]
  [IsAbelianGalois K L] {u : ↑TauCeti.LocalFieldsRamification.RamificationIndexDomain}
  (hu : TauCeti.LocalFieldsRamification.UpperJump K L u)
  (hp : Nat.Prime (Monoid.exponent Gal(L/K))) : ∃ z, ↑u = ↑z
```

## Sources

- [Tau Ceti documentation: `TauCeti.LocalFieldsRamification.UpperJump.exists_eq_intCast_of_finrank_prime`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/HasseArf/PrimeDegree.html#TauCeti.LocalFieldsRamification.UpperJump.exists_eq_intCast_of_finrank_prime)
- [Source of `TauCeti.LocalFieldsRamification.UpperJump.exists_eq_intCast_of_finrank_prime` in TauCeti/NumberTheory/LocalField/Herbrand/HasseArf/PrimeDegree.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/Herbrand/HasseArf/PrimeDegree.lean#L127)
