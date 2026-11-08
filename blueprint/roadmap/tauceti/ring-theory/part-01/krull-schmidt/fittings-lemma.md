---
declaration: theorem
origin: cited
lean: TauCeti.IsIndecomposableModule.isNilpotent_or_bijective, TauCeti.IsIndecomposableModule.isNilpotent_or_isUnit
statement: formalized
proof: formalized
---

# Fitting's lemma

an endomorphism of an indecomposable module that is both Noetherian and
Artinian is either nilpotent or bijective.

For a large enough exponent `m`, Mathlib's Fitting decomposition splits `M` as
`ker (f ^ m) ⊕ range (f ^ m)`. Indecomposability collapses one of the two summands: if the range
vanishes then `f ^ m = 0`, and if the kernel vanishes then `f` is injective while the range, being
everything, forces `f` to be surjective.

```lean
TauCeti.IsIndecomposableModule.isNilpotent_or_bijective.{u, v} {A : Type u} {M : Type v} [Ring A]
  [AddCommGroup M] [_root_.Module A M] [IsNoetherian A M] [IsArtinian A M]
  (h : TauCeti.IsIndecomposableModule A M) (f : Module.End A M) :
  IsNilpotent f ∨ Function.Bijective ⇑f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsIndecomposableModule.isNilpotent_or_bijective`](https://taucetiproject.org/docs/TauCeti/RingTheory/KrullSchmidt/Indecomposable.html#TauCeti.IsIndecomposableModule.isNilpotent_or_bijective).

## Other forms

**Fitting's lemma, restated.** Formalized in Tau Ceti as [`TauCeti.IsIndecomposableModule.isNilpotent_or_isUnit`](https://taucetiproject.org/docs/TauCeti/RingTheory/KrullSchmidt/Indecomposable.html#TauCeti.IsIndecomposableModule.isNilpotent_or_isUnit).

```lean
TauCeti.IsIndecomposableModule.isNilpotent_or_isUnit.{u, v} {A : Type u} {M : Type v} [Ring A]
  [AddCommGroup M] [_root_.Module A M] [IsNoetherian A M] [IsArtinian A M]
  (h : TauCeti.IsIndecomposableModule A M) (f : Module.End A M) : IsNilpotent f ∨ IsUnit f
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsIndecomposableModule.isNilpotent_or_bijective`](https://taucetiproject.org/docs/TauCeti/RingTheory/KrullSchmidt/Indecomposable.html#TauCeti.IsIndecomposableModule.isNilpotent_or_bijective)
- [Source of `TauCeti.IsIndecomposableModule.isNilpotent_or_bijective` in TauCeti/RingTheory/KrullSchmidt/Indecomposable.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/KrullSchmidt/Indecomposable.lean#L243)
