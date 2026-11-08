---
declaration: theorem
origin: cited
lean: Group.ResiduallyFinite.injective_of_surjective
statement: formalized
proof: formalized
---

# Malcev's theorem

A surjective endomorphism of a finitely generated residually finite
group is injective: such a group is Hopfian.

```lean
Group.ResiduallyFinite.injective_of_surjective.{u_1} {G : Type u_1} [Group G] [Group.FG G]
  [Group.ResiduallyFinite G] {f : G →* G} (hf : Function.Surjective ⇑f) : Function.Injective ⇑f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Group.ResiduallyFinite.injective_of_surjective`](https://taucetiproject.org/docs/TauCeti/GroupTheory/ResiduallyFinite.html#Group.ResiduallyFinite.injective_of_surjective).

## Sources

- [Tau Ceti documentation: `Group.ResiduallyFinite.injective_of_surjective`](https://taucetiproject.org/docs/TauCeti/GroupTheory/ResiduallyFinite.html#Group.ResiduallyFinite.injective_of_surjective)
- [Source of `Group.ResiduallyFinite.injective_of_surjective` in TauCeti/GroupTheory/ResiduallyFinite.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/ResiduallyFinite.lean#L40)
