---
declaration: theorem
origin: cited
lean: MonoidHom.card_comp_eq_and_closure_range_eq_congr
statement: formalized
proof: formalized
---

# Gaschütz's counting lemma

For a subgroup `K` of a finite group `G`, the number of
`ι`-tuples that generate `K` and lift a given generating tuple of `H` along `f` does not depend on
that generating tuple.

```lean
MonoidHom.card_comp_eq_and_closure_range_eq_congr.{u_1, u_2, u_3} {G : Type u_1} {H : Type u_2}
  {ι : Type u_3} [Group G] [Group H] (f : G →* H) [Finite G] [Finite ι] (K : Subgroup G)
  {h h' : ι → H} (hh : Subgroup.closure (Set.range h) = ⊤)
  (hh' : Subgroup.closure (Set.range h') = ⊤) :
  Nat.card { x // ⇑f ∘ x = h ∧ Subgroup.closure (Set.range x) = K } =
    Nat.card { x // ⇑f ∘ x = h' ∧ Subgroup.closure (Set.range x) = K }
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MonoidHom.card_comp_eq_and_closure_range_eq_congr`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Gaschutz.html#MonoidHom.card_comp_eq_and_closure_range_eq_congr).

## Sources

- [Tau Ceti documentation: `MonoidHom.card_comp_eq_and_closure_range_eq_congr`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Gaschutz.html#MonoidHom.card_comp_eq_and_closure_range_eq_congr)
- [Source of `MonoidHom.card_comp_eq_and_closure_range_eq_congr` in TauCeti/GroupTheory/Gaschutz.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Gaschutz.lean#L70)
