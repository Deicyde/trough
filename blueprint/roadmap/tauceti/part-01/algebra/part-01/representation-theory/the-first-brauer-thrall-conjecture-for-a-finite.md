---
declaration: theorem
origin: cited
lean: TauCeti.isRepresentationFinite_of_length_le, TauCeti.isRepresentationFinite_of_length_le_of_isLeftAlmostSplit
statement: formalized
proof: formalized
---

# The first Brauer–Thrall conjecture for a finite-dimensional algebra

if the finitely
generated indecomposable modules have bounded length, then there are only finitely many of them up
to isomorphism.

```lean
TauCeti.isRepresentationFinite_of_length_le.{u, v, w} {A : Type v} [Ring A] (k : Type u) [Field k]
  [Algebra k A] [FiniteDimensional k A] (b : ℕ)
  (hlen :
    ∀ (M : ModuleCat A),
      Module.Finite A ↑M → CategoryTheory.Indecomposable M → Module.length A ↑M ≤ ↑b) :
  TauCeti.IsRepresentationFinite A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Auslander–Reiten theorem, existence](the-auslander-reiten-theorem-existence.md)
- [Fitting's lemma, categorically](../category/fittings-lemma-categorically.md)
- [The Harada–Sai lemma](../category/the-harada-sai-lemma.md)
- [Jacobson's lemma](../../../category-theory/preadditive/jacobsons-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isRepresentationFinite_of_length_le`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/AuslanderReiten/BrauerThrall.html#TauCeti.isRepresentationFinite_of_length_le).

## Other forms

**The first Brauer–Thrall conjecture from left almost split maps.** Formalized in Tau Ceti as [`TauCeti.isRepresentationFinite_of_length_le_of_isLeftAlmostSplit`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/AuslanderReiten/BrauerThrall.html#TauCeti.isRepresentationFinite_of_length_le_of_isLeftAlmostSplit).

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

## Sources

- [Tau Ceti documentation: `TauCeti.isRepresentationFinite_of_length_le`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/AuslanderReiten/BrauerThrall.html#TauCeti.isRepresentationFinite_of_length_le)
- [Source of `TauCeti.isRepresentationFinite_of_length_le` in TauCeti/Algebra/Category/ModuleCat/AuslanderReiten/BrauerThrall.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Category/ModuleCat/AuslanderReiten/BrauerThrall.lean#L130)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RepresentationTheory/STATUS.md)
