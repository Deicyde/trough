---
declaration: theorem
origin: cited
lean: TauCeti.TateCohomology.cup_bijective_of_forall_isPGroup, TauCeti.TateCohomology.cup_bijective_of_cupTrivialInt_injective
statement: formalized
proof: formalized
---

# Tate's theorem

Let `G` be a finite group, `N` a representation of `G` over `ℤ` and
`u ∈ H²(G, N)`. Suppose that

* `u` generates `H²(G, N)`, a group of order `|G|`;
* for every subgroup `S` of `G` of prime-power order, `H¹(S, N) = 0` and `H²(S, N)` has order
  `|S|`.

Then cup product with `u` is a bijection `H^r(G, ℤ) → H^{r+2}(G, ℤ ⊗ N)` in every integer degree
`r`. The classical hypothesis that the restriction of `u` to each subgroup generates its `H²` is
a consequence of these and is not assumed.

```lean
TauCeti.TateCohomology.cup_bijective_of_forall_isPGroup {G : Type} [Group G] [Fintype G]
  (N : Rep.{0, 0, 0} ℤ G) (u : ↑(tateCohomology N 2))
  (hgen : ∀ (y : ↑(tateCohomology N 2)), ∃ m, m • u = y)
  (hcardG : Nat.card ↑(tateCohomology N 2) = Nat.card G)
  (h1 :
    ∀ (p : ℕ) [Fact (Nat.Prime p)] (S : Subgroup G) [inst : Fintype ↥S],
      IsPGroup p ↥S → CategoryTheory.Limits.IsZero (tateCohomology (Rep.res S.subtype N) 1))
  (hcard :
    ∀ (p : ℕ) [Fact (Nat.Prime p)] (S : Subgroup G) [inst : Fintype ↥S],
      IsPGroup p ↥S → Nat.card ↑(tateCohomology (Rep.res S.subtype N) 2) = Nat.card ↥S)
  (r r' : ℤ) (h : r + 2 = r') :
  Function.Bijective fun x => ((TauCeti.TateCohomology.cup (Rep.trivial ℤ G ℤ) N r 2 r' h) x) u
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Tate's isomorphism criterion](tates-isomorphism-criterion.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TateCohomology.cup_bijective_of_forall_isPGroup`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/TateCohomology/Cup/TateTheorem.html#TauCeti.TateCohomology.cup_bijective_of_forall_isPGroup).

## Other forms

**Tate's theorem, with the degree-zero injection as hypothesis.** Formalized in Tau Ceti as [`TauCeti.TateCohomology.cup_bijective_of_cupTrivialInt_injective`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/TateCohomology/Cup/TateTheorem.html#TauCeti.TateCohomology.cup_bijective_of_cupTrivialInt_injective).

```lean
TauCeti.TateCohomology.cup_bijective_of_cupTrivialInt_injective {G : Type} [Group G] [Fintype G]
  (N : Rep.{0, 0, 0} ℤ G) (u : ↑(tateCohomology N 2))
  (hinj₀ : Function.Injective ⇑(TauCeti.TateCohomology.cupTrivialInt N u))
  (h1 :
    ∀ (p : ℕ) [Fact (Nat.Prime p)] (S : Subgroup G) [inst : Fintype ↥S],
      IsPGroup p ↥S → CategoryTheory.Limits.IsZero (tateCohomology (Rep.res S.subtype N) 1))
  (hcard :
    ∀ (p : ℕ) [Fact (Nat.Prime p)] (S : Subgroup G) [inst : Fintype ↥S],
      IsPGroup p ↥S → Nat.card ↑(tateCohomology (Rep.res S.subtype N) 2) = Nat.card ↥S)
  (r r' : ℤ) (h : r + 2 = r') :
  Function.Bijective fun x => ((TauCeti.TateCohomology.cup (Rep.trivial ℤ G ℤ) N r 2 r' h) x) u
```

## Sources

- [Tau Ceti documentation: `TauCeti.TateCohomology.cup_bijective_of_forall_isPGroup`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/TateCohomology/Cup/TateTheorem.html#TauCeti.TateCohomology.cup_bijective_of_forall_isPGroup)
- [Source of `TauCeti.TateCohomology.cup_bijective_of_forall_isPGroup` in TauCeti/RepresentationTheory/Homological/TateCohomology/Cup/TateTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Homological/TateCohomology/Cup/TateTheorem.lean#L199)
