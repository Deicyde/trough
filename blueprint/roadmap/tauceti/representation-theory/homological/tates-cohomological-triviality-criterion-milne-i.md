---
declaration: theorem
origin: cited
lean: TauCeti.TateCohomology.isZero_of_forall_isPGroup, TauCeti.groupCohomology.isZero_of_forall_isPGroup
statement: formalized
proof: formalized
---

# Tate's cohomological triviality criterion (Milne II 3.10)

Let `G` be a finite group and
`A` a representation of `G`. If its Tate cohomology vanishes in degrees `q` and `q + 1` for every
subgroup `S` of `G` of prime-power order, then it vanishes in degree `n` for every subgroup `S`
of `G` and every integer `n`.

```lean
TauCeti.TateCohomology.isZero_of_forall_isPGroup.{u} {k G : Type u} [CommRing k] [Group G]
  [Finite G] (A : Rep.{u, u, u} k G) {q : ℤ}
  (h₁ :
    ∀ (p : ℕ) [Fact (Nat.Prime p)] (S : Subgroup G) [inst : Fintype ↥S],
      IsPGroup p ↥S → CategoryTheory.Limits.IsZero (tateCohomology (Rep.res S.subtype A) q))
  (h₂ :
    ∀ (p : ℕ) [Fact (Nat.Prime p)] (S : Subgroup G) [inst : Fintype ↥S],
      IsPGroup p ↥S → CategoryTheory.Limits.IsZero (tateCohomology (Rep.res S.subtype A) (q + 1)))
  (S : Subgroup G) [Fintype ↥S] (n : ℤ) :
  CategoryTheory.Limits.IsZero (tateCohomology (Rep.res S.subtype A) n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Sylow reduction of Tate's triviality criterion (Milne II 3.10, last paragraph)](the-sylow-reduction-of-tates-triviality-criterio.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TateCohomology.isZero_of_forall_isPGroup`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/TateCohomology/TrivialityCriterion.html#TauCeti.TateCohomology.isZero_of_forall_isPGroup).

## Other forms

**Tate's cohomological triviality criterion for ordinary cohomology (Milne II 3.10).** Formalized in Tau Ceti as [`TauCeti.groupCohomology.isZero_of_forall_isPGroup`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/TateCohomology/TrivialityCriterion.html#TauCeti.groupCohomology.isZero_of_forall_isPGroup).

```lean
TauCeti.groupCohomology.isZero_of_forall_isPGroup.{u} {k G : Type u} [CommRing k] [Group G]
  [Finite G] (A : Rep.{u, u, u} k G) {q : ℕ}
  (h₁ :
    ∀ (p : ℕ) [Fact (Nat.Prime p)] (S : Subgroup G),
      IsPGroup p ↥S → CategoryTheory.Limits.IsZero (groupCohomology (Rep.res S.subtype A) (q + 1)))
  (h₂ :
    ∀ (p : ℕ) [Fact (Nat.Prime p)] (S : Subgroup G),
      IsPGroup p ↥S → CategoryTheory.Limits.IsZero (groupCohomology (Rep.res S.subtype A) (q + 2)))
  (S : Subgroup G) (n : ℕ) :
  CategoryTheory.Limits.IsZero (groupCohomology (Rep.res S.subtype A) (n + 1))
```

## Sources

- [Tau Ceti documentation: `TauCeti.TateCohomology.isZero_of_forall_isPGroup`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/TateCohomology/TrivialityCriterion.html#TauCeti.TateCohomology.isZero_of_forall_isPGroup)
- [Source of `TauCeti.TateCohomology.isZero_of_forall_isPGroup` in TauCeti/RepresentationTheory/Homological/TateCohomology/TrivialityCriterion.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/TateCohomology/TrivialityCriterion.lean#L189)
