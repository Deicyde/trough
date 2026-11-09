---
declaration: theorem
origin: cited
lean: Setoid.mk_quotient_le_aleph0_or_eq_continuum
statement: formalized
proof: formalized
---

# The cardinality form of Silver's theorem

A Borel equivalence relation on a standard Borel
space has at most `ℵ₀` or exactly `𝔠` classes.

```lean
Setoid.mk_quotient_le_aleph0_or_eq_continuum.{u_1} {X : Type u_1} [MeasurableSpace X]
  [StandardBorelSpace X] (E : Setoid X) (hE : MeasurableSet {p | E p.1 p.2}) :
  Cardinal.mk (Quotient E) ≤ Cardinal.aleph0 ∨ Cardinal.mk (Quotient E) = Cardinal.continuum
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Silver's theorem](silvers-theorem.md)

## Lean

Formalized in Tau Ceti as [`Setoid.mk_quotient_le_aleph0_or_eq_continuum`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/Silver.html#Setoid.mk_quotient_le_aleph0_or_eq_continuum).

## Sources

- [Tau Ceti documentation: `Setoid.mk_quotient_le_aleph0_or_eq_continuum`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/Silver.html#Setoid.mk_quotient_le_aleph0_or_eq_continuum)
- [Source of `Setoid.mk_quotient_le_aleph0_or_eq_continuum` in TauCeti/SetTheory/Descriptive/Silver.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/SetTheory/Descriptive/Silver.lean#L151)
