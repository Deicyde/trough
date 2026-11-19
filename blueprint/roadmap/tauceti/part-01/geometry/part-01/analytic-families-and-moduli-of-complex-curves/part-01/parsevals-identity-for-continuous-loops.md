---
declaration: theorem
origin: cited
lean: TauCeti.CircleSobolev.inner_ofContinuousMap, TauCeti.CircleSobolev.real_inner_ofContinuousMap
statement: formalized
proof: formalized
---

# Parseval's identity for continuous loops

For continuous loops `f`, `g` in a
finite-dimensional complex inner product space, the inner product in `H⁰` of their Fourier
coefficient sequences is the mean `∫ ⟪f x, g x⟫` over the circle, for the normalized Haar
measure.

```lean
TauCeti.CircleSobolev.inner_ofContinuousMap.{u_2} (T : ℝ) [hT : Fact (0 < T)] {F : Type u_2}
  [NormedAddCommGroup F] [InnerProductSpace ℂ F] [FiniteDimensional ℂ F] (f g : C(AddCircle T, F)) :
  inner ℂ ((TauCeti.CircleSobolev.ofContinuousMap T) f)
      ((TauCeti.CircleSobolev.ofContinuousMap T) g) =
    ∫ (x : AddCircle T), inner ℂ (f x) (g x) ∂AddCircle.haarAddCircle
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CircleSobolev.inner_ofContinuousMap`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/OfContinuousMap.html#TauCeti.CircleSobolev.inner_ofContinuousMap).

## Other forms

**Parseval's identity for the real inner product.** Formalized in Tau Ceti as [`TauCeti.CircleSobolev.real_inner_ofContinuousMap`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/OfContinuousMap.html#TauCeti.CircleSobolev.real_inner_ofContinuousMap).

```lean
TauCeti.CircleSobolev.real_inner_ofContinuousMap.{u_2} (T : ℝ) [hT : Fact (0 < T)] {F : Type u_2}
  [NormedAddCommGroup F] [InnerProductSpace ℂ F] [FiniteDimensional ℂ F] (f g : C(AddCircle T, F)) :
  inner ℝ ((TauCeti.CircleSobolev.ofContinuousMap T) f)
      ((TauCeti.CircleSobolev.ofContinuousMap T) g) =
    ∫ (x : AddCircle T), (inner ℂ (f x) (g x)).re ∂AddCircle.haarAddCircle
```

## Sources

- [Tau Ceti documentation: `TauCeti.CircleSobolev.inner_ofContinuousMap`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/OfContinuousMap.html#TauCeti.CircleSobolev.inner_ofContinuousMap)
- [Source of `TauCeti.CircleSobolev.inner_ofContinuousMap` in TauCeti/Analysis/Sobolev/Circle/OfContinuousMap.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Sobolev/Circle/OfContinuousMap.lean#L257)
