---
declaration: theorem
origin: cited
lean: TauCeti.braidEquivalent_of_isReduced_wordProd_eq, TauCeti.matsumoto
statement: formalized
proof: formalized
---

# Matsumoto's theorem, relational form

Two reduced words representing the same element
of a Coxeter group are connected by braid moves.

```lean
TauCeti.braidEquivalent_of_isReduced_wordProd_eq.{u_1, u_2} {B : Type u_1} {W : Type u_2} [Group W]
  {M : CoxeterMatrix B} (cs : CoxeterSystem M W) {ω ω' : List B} (hω : cs.IsReduced ω)
  (hω' : cs.IsReduced ω') (hprod : cs.wordProd ω = cs.wordProd ω') :
  CoxeterSystem.BraidEquivalent M ω ω'
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Tits' lemma](tits-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.braidEquivalent_of_isReduced_wordProd_eq`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Coxeter/Matsumoto.html#TauCeti.braidEquivalent_of_isReduced_wordProd_eq).

## Other forms

**Matsumoto's theorem, monoid-valued form.** Formalized in Tau Ceti as [`TauCeti.matsumoto`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Coxeter/Matsumoto.html#TauCeti.matsumoto).

```lean
TauCeti.matsumoto.{u_1, u_2, u_3} {B : Type u_1} {W : Type u_2} [Group W] {M : CoxeterMatrix B}
  (cs : CoxeterSystem M W) {G : Type u_3} [Monoid G] (f : B → G)
  (hbraid :
    ∀ (i j : B),
      (List.map f (CoxeterSystem.braidWord M i j)).prod =
        (List.map f (CoxeterSystem.braidWord M j i)).prod)
  {ω ω' : List B} (hω : cs.IsReduced ω) (hω' : cs.IsReduced ω')
  (hprod : cs.wordProd ω = cs.wordProd ω') : (List.map f ω).prod = (List.map f ω').prod
```

## Sources

- [Tau Ceti documentation: `TauCeti.braidEquivalent_of_isReduced_wordProd_eq`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Coxeter/Matsumoto.html#TauCeti.braidEquivalent_of_isReduced_wordProd_eq)
- [Source of `TauCeti.braidEquivalent_of_isReduced_wordProd_eq` in TauCeti/GroupTheory/Coxeter/Matsumoto.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Coxeter/Matsumoto.lean#L81)
