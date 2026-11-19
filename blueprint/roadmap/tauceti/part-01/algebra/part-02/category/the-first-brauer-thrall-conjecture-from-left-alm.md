---
declaration: theorem
origin: cited
lean: TauCeti.isRepresentationFinite_of_length_le_of_isLeftAlmostSplit, TauCeti.isRepresentationFinite_of_length_le
statement: formalized
proof: formalized
---

# The first Brauer–Thrall conjecture from left almost split maps

Let `A` be an Artinian ring
over which every finitely generated indecomposable non-injective module has a left almost split map
with finitely generated target. If the finitely generated indecomposable modules have bounded
length, then `A` is representation-finite.

```lean
TauCeti.isRepresentationFinite_of_length_le_of_isLeftAlmostSplit.{v, w} {A : Type v} [Ring A]
  [IsArtinianRing A] (b : ℕ)
  (hlen :
    ∀ (M : ModuleCat A),
      Module.Finite A ↑M → CategoryTheory.Indecomposable M → Module.length A ↑M ≤ ↑b)
  (hsrc :
    ∀ (N : ModuleCat A),
      Module.Finite A ↑N →
        CategoryTheory.Indecomposable N →
          ¬CategoryTheory.Injective N → ∃ E i, Module.Finite A ↑E ∧ TauCeti.IsLeftAlmostSplit i) :
  TauCeti.IsRepresentationFinite A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Auslander–Reiten theorem, existence](the-auslander-reiten-theorem-existence.md)
- [Fitting's lemma, categorically](fittings-lemma-categorically.md)
- [The Harada–Sai lemma](the-harada-sai-lemma.md)
- [Jacobson's lemma](../../../category-theory/preadditive/jacobsons-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isRepresentationFinite_of_length_le_of_isLeftAlmostSplit`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/AuslanderReiten/BrauerThrall.html#TauCeti.isRepresentationFinite_of_length_le_of_isLeftAlmostSplit).

## Other forms

**The first Brauer–Thrall conjecture for a finite-dimensional algebra.** Formalized in Tau Ceti as [`TauCeti.isRepresentationFinite_of_length_le`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/AuslanderReiten/BrauerThrall.html#TauCeti.isRepresentationFinite_of_length_le).

```lean
TauCeti.isRepresentationFinite_of_length_le.{u, v, w} {A : Type v} [Ring A] (k : Type u) [Field k]
  [Algebra k A] [FiniteDimensional k A] (b : ℕ)
  (hlen :
    ∀ (M : ModuleCat A),
      Module.Finite A ↑M → CategoryTheory.Indecomposable M → Module.length A ↑M ≤ ↑b) :
  TauCeti.IsRepresentationFinite A
```

## Sources

- [Tau Ceti documentation: `TauCeti.isRepresentationFinite_of_length_le_of_isLeftAlmostSplit`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/AuslanderReiten/BrauerThrall.html#TauCeti.isRepresentationFinite_of_length_le_of_isLeftAlmostSplit)
- [Source of `TauCeti.isRepresentationFinite_of_length_le_of_isLeftAlmostSplit` in TauCeti/Algebra/Category/ModuleCat/AuslanderReiten/BrauerThrall.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Category/ModuleCat/AuslanderReiten/BrauerThrall.lean#L71)
