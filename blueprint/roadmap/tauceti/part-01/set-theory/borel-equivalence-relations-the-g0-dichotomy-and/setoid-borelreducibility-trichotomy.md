---
declaration: theorem
origin: cited
lean: Setoid.borelReducibility_trichotomy
statement: formalized
proof: formalized
---

# Setoid.borelReducibility_trichotomy

A Borel equivalence relation on a standard Borel space is Borel bireducible with equality
on some `Fin n` or on `ℕ`, or equality on Cantor space is Borel reducible to it. The finite
alternative includes the empty space, with `n = 0`.

```lean
Setoid.borelReducibility_trichotomy.{u_1} {X : Type u_1} [MeasurableSpace X] [StandardBorelSpace X]
  (E : Setoid X) (hE : MeasurableSet {p | E p.1 p.2}) :
  (∃ n, E.BorelBireducible ⊥) ∨ E.BorelBireducible ⊥ ∨ ⊥.BorelReducible E
```

## Depends on

- [Setoid.BorelReducible](setoid-borelreducible.md)

## Proof depends on

- [Silver's theorem](silvers-theorem.md)

## Lean

Formalized in Tau Ceti as [`Setoid.borelReducibility_trichotomy`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/NormalForms.html#Setoid.borelReducibility_trichotomy).

## Sources

- [Tau Ceti documentation: `Setoid.borelReducibility_trichotomy`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/NormalForms.html#Setoid.borelReducibility_trichotomy)
- [Source of `Setoid.borelReducibility_trichotomy` in TauCeti/SetTheory/Descriptive/NormalForms.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/SetTheory/Descriptive/NormalForms.lean#L44)
- [Tau Ceti roadmap status: Borel equivalence relations, the G₀ dichotomy and Silver's theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BorelEquivalenceRelations/STATUS.md)
