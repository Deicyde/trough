---
declaration: theorem
origin: cited
lean: ModuleCat.exists_isAlmostSplit_arTranslate, ModuleCat.exists_isAlmostSplit_of_not_injective
statement: formalized
proof: formalized
---

# The Auslander–Reiten theorem, existence

Over a finite-dimensional algebra, a finitely
generated indecomposable non-projective module `M` ends an almost-split sequence
`0 → τ M → E → M → 0` of `A`-modules whose left-hand end is the translate `τ M` and whose middle
term is finitely generated.

```lean
ModuleCat.exists_isAlmostSplit_arTranslate.{u, v, w} (k : Type u) {A : Type v} [Field k] [Ring A]
  [Algebra k A] [FiniteDimensional k A] (M : ModuleCat A) [Module.Finite A ↑M]
  (hiM : CategoryTheory.Indecomposable M) (hpM : ¬CategoryTheory.Projective M) :
  ∃ E i p,
    ∃ (h : CategoryTheory.CategoryStruct.comp i p = 0),
      Module.Finite A ↑E ∧
        { X₁ := ModuleCat.arTranslate k M, X₂ := E, X₃ := M, f := i, g := p,
            zero := h }.IsAlmostSplit
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Fitting's lemma, categorically](../../../category-theory/geometric-representation-categories-and-coherent/fittings-lemma-categorically.md)
- [Jacobson's lemma](../../../category-theory/preadditive/jacobsons-lemma.md)
- [Nakayama's lemma for `R[G]^ι`](../../other-results/nakayamas-lemma-for-r-g.md)
- [TauCeti.isLocalRing_end_of_indecomposable](../../../category-theory/preadditive/tauceti-islocalring-end-of-indecomposable.md)

## Lean

Formalized in Tau Ceti as [`ModuleCat.exists_isAlmostSplit_arTranslate`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/AuslanderReiten/Sequence.html#ModuleCat.exists_isAlmostSplit_arTranslate).

## Other forms

**The Auslander–Reiten theorem, existence on the left.** Formalized in Tau Ceti as [`ModuleCat.exists_isAlmostSplit_of_not_injective`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/AuslanderReiten/Sequence.html#ModuleCat.exists_isAlmostSplit_of_not_injective).

```lean
ModuleCat.exists_isAlmostSplit_of_not_injective.{u, v, w} (k : Type u) {A : Type v} [Field k]
  [Ring A] [Algebra k A] [FiniteDimensional k A] (N : ModuleCat A) [Module.Finite A ↑N]
  (hiN : CategoryTheory.Indecomposable N) (hinj : ¬CategoryTheory.Injective N) :
  ∃ E M i p,
    ∃ (h : CategoryTheory.CategoryStruct.comp i p = 0),
      Module.Finite A ↑E ∧
        Module.Finite A ↑M ∧ { X₁ := N, X₂ := E, X₃ := M, f := i, g := p, zero := h }.IsAlmostSplit
```

## Sources

- [Tau Ceti documentation: `ModuleCat.exists_isAlmostSplit_arTranslate`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/AuslanderReiten/Sequence.html#ModuleCat.exists_isAlmostSplit_arTranslate)
- [Source of `ModuleCat.exists_isAlmostSplit_arTranslate` in TauCeti/Algebra/Category/ModuleCat/AuslanderReiten/Sequence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/ModuleCat/AuslanderReiten/Sequence.lean#L66)
