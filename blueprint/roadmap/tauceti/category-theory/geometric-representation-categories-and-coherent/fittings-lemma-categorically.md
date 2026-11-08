---
declaration: theorem
origin: cited
lean: TauCeti.indecomposable_iff_isLocalRing_end, FGModuleCat.isLocalRing_end_of_indecomposable
statement: formalized
proof: formalized
---

# Fitting's lemma, categorically

an object of `ModuleCat A` whose underlying module has
finite length is indecomposable exactly when its ring of endomorphisms in the category is local.

```lean
TauCeti.indecomposable_iff_isLocalRing_end.{u, v} {A : Type u} [Ring A] (M : ModuleCat A)
  (hM : IsFiniteLength A ↑M) : CategoryTheory.Indecomposable M ↔ IsLocalRing (CategoryTheory.End M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Fitting's lemma](../../ring-theory/krull-schmidt/fittings-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.indecomposable_iff_isLocalRing_end`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Indecomposable.html#TauCeti.indecomposable_iff_isLocalRing_end).

## Other forms

**Fitting's lemma in `FGModuleCat A`.** Formalized in Tau Ceti as [`FGModuleCat.isLocalRing_end_of_indecomposable`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/FGModuleCat/KrullSchmidt.html#FGModuleCat.isLocalRing_end_of_indecomposable).

```lean
FGModuleCat.isLocalRing_end_of_indecomposable.{w, v} {A : Type v} [Ring A] {X : FGModuleCat A}
  [IsNoetherian A ↑X.obj] [IsArtinian A ↑X.obj] (hX : CategoryTheory.Indecomposable X.obj) :
  IsLocalRing (CategoryTheory.End X)
```

## Sources

- [Tau Ceti documentation: `TauCeti.indecomposable_iff_isLocalRing_end`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Indecomposable.html#TauCeti.indecomposable_iff_isLocalRing_end)
- [Source of `TauCeti.indecomposable_iff_isLocalRing_end` in TauCeti/Algebra/Category/ModuleCat/Indecomposable.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/ModuleCat/Indecomposable.lean#L77)
