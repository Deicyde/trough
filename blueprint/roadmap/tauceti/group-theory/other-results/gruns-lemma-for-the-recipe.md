---
declaration: theorem
origin: cited
lean: TauCeti.DerivedCentralQuotient.center_eq_bot
statement: formalized
proof: formalized
---

# Grün's lemma for the recipe

when the derived subgroup is perfect, the derived central
quotient has trivial centre.

This is the reason the two steps compose in the stated order: the centre is removed once and for
all, and does not reappear.

```lean
TauCeti.DerivedCentralQuotient.center_eq_bot.{u_1} {G : Type u_1} [Group G]
  [Group.IsPerfect ↥(commutator G)] : Subgroup.center (TauCeti.DerivedCentralQuotient G) = ⊥
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.DerivedCentralQuotient.center_eq_bot`](https://taucetiproject.org/docs/TauCeti/GroupTheory/DerivedCentralQuotient.html#TauCeti.DerivedCentralQuotient.center_eq_bot).

## Sources

- [Tau Ceti documentation: `TauCeti.DerivedCentralQuotient.center_eq_bot`](https://taucetiproject.org/docs/TauCeti/GroupTheory/DerivedCentralQuotient.html#TauCeti.DerivedCentralQuotient.center_eq_bot)
- [Source of `TauCeti.DerivedCentralQuotient.center_eq_bot` in TauCeti/GroupTheory/DerivedCentralQuotient.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/DerivedCentralQuotient.lean#L216)
