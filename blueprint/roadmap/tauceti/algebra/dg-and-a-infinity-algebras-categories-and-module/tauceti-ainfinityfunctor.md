---
declaration: structure
origin: cited
lean: TauCeti.AInfinityFunctor
statement: formalized
---

# TauCeti.AInfinityFunctor

An **`A∞` functor** between nonunital `A∞` categories `ℬ` on `C` and `𝒞` on `D`: a map of
objects `obj : C → D` together with an `A∞` morphism from the total algebra of morphisms of `ℬ` to
that of the induced category `𝒞.induced obj`, whose components send a composable string of `C` to
a morphism between the images of its endpoints and every other string to zero.  Its component of
arity `n` on a composable string `X₀, …, Xₙ` is the functor component
`fₙ : Hom(Xₙ₋₁, Xₙ) ⊗ ⋯ ⊗ Hom(X₀, X₁) ⟶ Hom(obj X₀, obj Xₙ)` of degree `1 - n`.

```lean
TauCeti.AInfinityFunctor.{u₁, u₂, v₁, v₂, w} {R : Type w} [CommRing R] {C : Type u₁} {D : Type u₂}
  [TauCeti.GradedLinearQuiver R C] [TauCeti.GradedLinearQuiver R D]
  (ℬ : TauCeti.AInfinityCategory R C) (𝒞 : TauCeti.AInfinityCategory R D) :
  Type (max (max (max (max u₁ u₂) v₁) v₂) w)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AInfinityFunctor`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/AInfinity/Functor/Basic.html#TauCeti.AInfinityFunctor).

## Sources

- [Tau Ceti documentation: `TauCeti.AInfinityFunctor`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/AInfinity/Functor/Basic.html#TauCeti.AInfinityFunctor)
- [Source of `TauCeti.AInfinityFunctor` in TauCeti/CategoryTheory/AInfinity/Functor/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/AInfinity/Functor/Basic.lean#L91)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DGAInfinity/STATUS.md)
