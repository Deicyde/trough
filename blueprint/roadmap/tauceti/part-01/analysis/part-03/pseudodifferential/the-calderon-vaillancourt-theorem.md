---
declaration: theorem
origin: cited
lean: TauCeti.Symbol.exists_quantizeUniformOrderZeroLp, TauCeti.Symbol.exists_quantizeUniformOrderZero
statement: formalized
proof: formalized
---

# The Calderón–Vaillancourt theorem

The quantization of a symbol of order `0` whose
estimates hold uniformly in the position extends from Schwartz functions to a bounded operator on
`L²(ℝⁿ)`: there is a bounded operator `T` on `L²` with `T u = Op(a) u` almost everywhere for every
Schwartz function `u`. No support condition in the position is needed.

```lean
TauCeti.Symbol.exists_quantizeUniformOrderZeroLp.{u_1, u_2} {n : ℕ} {V : Type u_1} {W : Type u_2}
  [NormedAddCommGroup V] [InnerProductSpace ℂ V] [CompleteSpace V] [NormedAddCommGroup W]
  [InnerProductSpace ℂ W] [CompleteSpace W] (a : TauCeti.Symbol n V W 0) (ha : a.IsUniform) :
  ∃ T,
    ∀ (u : SchwartzMap (TauCeti.CoordinateSpace n) V),
      ↑↑(T (u.toLp 2 MeasureTheory.volume)) =ᵐ[MeasureTheory.volume]
        TauCeti.quantizeSchwartzValue a.coefficient u
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cotlar–Stein lemma](../inner-product-space/part-01/the-cotlar-stein-lemma.md)
- [Young's inequality for integral kernels](../../../measure-theory/integral/part-02/youngs-inequality-for-integral-kernels.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Symbol.exists_quantizeUniformOrderZeroLp`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/CalderonVaillancourt.html#TauCeti.Symbol.exists_quantizeUniformOrderZeroLp).

## Other forms

**The Calderón–Vaillancourt theorem on `H⁰ = L²`, for finite-dimensional coefficient spaces.** Formalized in Tau Ceti as [`TauCeti.Symbol.exists_quantizeUniformOrderZero`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/CalderonVaillancourt.html#TauCeti.Symbol.exists_quantizeUniformOrderZero).

```lean
TauCeti.Symbol.exists_quantizeUniformOrderZero.{u_3, u_4} {n : ℕ} {V : Type u_3} {W : Type u_4}
  [NormedAddCommGroup V] [NormedSpace ℂ V] [CompleteSpace V] [FiniteDimensional ℂ V]
  [NormedAddCommGroup W] [NormedSpace ℂ W] [CompleteSpace W] [FiniteDimensional ℂ W]
  (a : TauCeti.Symbol n V W 0) (ha : a.IsUniform) :
  ∃ T,
    ∀ (u : SchwartzMap (TauCeti.CoordinateSpace n) V)
      (φ : SchwartzMap (TauCeti.CoordinateSpace n) ℂ),
      ↑(T ((SchwartzMap.toBesselPotentialSpaceCLM 0 2) u)) φ =
        ∫ (x : TauCeti.CoordinateSpace n), φ x • TauCeti.quantizeSchwartzValue a.coefficient u x
```

## Sources

- [Tau Ceti documentation: `TauCeti.Symbol.exists_quantizeUniformOrderZeroLp`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/CalderonVaillancourt.html#TauCeti.Symbol.exists_quantizeUniformOrderZeroLp)
- [Source of `TauCeti.Symbol.exists_quantizeUniformOrderZeroLp` in TauCeti/Analysis/Pseudodifferential/CalderonVaillancourt.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Pseudodifferential/CalderonVaillancourt.lean#L651)
