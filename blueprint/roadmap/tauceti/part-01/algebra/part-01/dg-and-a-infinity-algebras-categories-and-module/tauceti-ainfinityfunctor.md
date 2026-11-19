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
- [Source of `TauCeti.AInfinityFunctor` in TauCeti/CategoryTheory/AInfinity/Functor/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/AInfinity/Functor/Basic.lean#L91)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DGAInfinity/STATUS.md)
