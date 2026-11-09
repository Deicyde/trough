---
declaration: theorem
origin: cited
lean: MonoidHom.transfer_commutator_eq_one
statement: formalized
proof: formalized
---

# Furtwängler's theorem, the group-theoretic principal ideal theorem

if the commutator
subgroup `G'` of `G` is finitely generated and of finite index (for instance if `G` is finite),
the transfer `G → A` of every homomorphism `ϕ : G' →* A` to a commutative group is trivial. For
`ϕ` the abelianization map, this says that the transfer `G → G' ⧸ G''` is trivial.

```lean
MonoidHom.transfer_commutator_eq_one.{u_1} {G : Type} [Group G] [Group.FG ↥(commutator G)]
  [(commutator G).FiniteIndex] {A : Type u_1} [CommGroup A] (ϕ : ↥(commutator G) →* A) :
  ϕ.transfer = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Nakayama's lemma over `ℤ`](../../ring-theory/part-02/other-results/part-02/nakayamas-lemma-over-z.md)

## Lean

Formalized in Tau Ceti as [`MonoidHom.transfer_commutator_eq_one`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Transfer/Commutator.html#MonoidHom.transfer_commutator_eq_one).

## Sources

- [Tau Ceti documentation: `MonoidHom.transfer_commutator_eq_one`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Transfer/Commutator.html#MonoidHom.transfer_commutator_eq_one)
- [Source of `MonoidHom.transfer_commutator_eq_one` in TauCeti/GroupTheory/Transfer/Commutator.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Transfer/Commutator.lean#L299)
