---
declaration: theorem
origin: cited
lean: TauCeti.Symbol.exists_quantizeUniformOrderZero, TauCeti.Symbol.hasSobolevExtension_quantizeUniformCLM_zero, TauCeti.Symbol.exists_quantizeUniformOrderZeroLp
statement: formalized
proof: formalized
---

# The Calderón–Vaillancourt theorem on `H⁰ = L²`, for finite-dimensional coefficient spaces

The quantization of a symbol of order `0` whose estimates hold uniformly in the position
extends from Schwartz functions to a bounded operator `H⁰(ℝⁿ; V) → H⁰(ℝⁿ; W)`.

The norms of `V` and `W` need not come from inner products: isomorphisms `e₁ : V ≃L[ℂ] ℂ^k` and
`e₂ : W ≃L[ℂ] ℂ^l` reduce the statement
(`TauCeti.Symbol.toDistr_postcomp_comp_comp_postcomp_toBesselPotentialSpaceCLM_apply`) to
`TauCeti.Symbol.exists_quantizeUniformOrderZeroLp` for the conjugated symbol `e₂ a e₁⁻¹`.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cotlar–Stein lemma](../../part-03/inner-product-space/part-01/the-cotlar-stein-lemma.md)
- [Young's inequality for integral kernels](../../../measure-theory/integral/part-02/youngs-inequality-for-integral-kernels.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Symbol.exists_quantizeUniformOrderZero`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/CalderonVaillancourt.html#TauCeti.Symbol.exists_quantizeUniformOrderZero).

## Other forms

**Calderón–Vaillancourt.** Formalized in Tau Ceti as [`TauCeti.Symbol.hasSobolevExtension_quantizeUniformCLM_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/UniformSobolev.html#TauCeti.Symbol.hasSobolevExtension_quantizeUniformCLM_zero).

```lean
TauCeti.Symbol.hasSobolevExtension_quantizeUniformCLM_zero.{u_1, u_2} {n : ℕ} {m : ℝ} {V : Type u_1}
  {W : Type u_2} [NormedAddCommGroup V] [InnerProductSpace ℂ V] [CompleteSpace V]
  [NormedAddCommGroup W] [InnerProductSpace ℂ W] [CompleteSpace W] {b : TauCeti.Symbol n V W m}
  (hb : b.IsUniform) (hm : m ≤ 0) : SchwartzMap.HasSobolevExtension (b.quantizeUniformCLM hb) 0 0
```

**The Calderón–Vaillancourt theorem.** Formalized in Tau Ceti as [`TauCeti.Symbol.exists_quantizeUniformOrderZeroLp`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/CalderonVaillancourt.html#TauCeti.Symbol.exists_quantizeUniformOrderZeroLp).

```lean
TauCeti.Symbol.exists_quantizeUniformOrderZeroLp.{u_1, u_2} {n : ℕ} {V : Type u_1} {W : Type u_2}
  [NormedAddCommGroup V] [InnerProductSpace ℂ V] [CompleteSpace V] [NormedAddCommGroup W]
  [InnerProductSpace ℂ W] [CompleteSpace W] (a : TauCeti.Symbol n V W 0) (ha : a.IsUniform) :
  ∃ T,
    ∀ (u : SchwartzMap (TauCeti.CoordinateSpace n) V),
      ↑↑(T (u.toLp 2 MeasureTheory.volume)) =ᵐ[MeasureTheory.volume]
        TauCeti.quantizeSchwartzValue a.coefficient u
```

## Sources

- [Tau Ceti documentation: `TauCeti.Symbol.exists_quantizeUniformOrderZero`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/CalderonVaillancourt.html#TauCeti.Symbol.exists_quantizeUniformOrderZero)
- [Source of `TauCeti.Symbol.exists_quantizeUniformOrderZero` in TauCeti/Analysis/Pseudodifferential/CalderonVaillancourt.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Pseudodifferential/CalderonVaillancourt.lean#L672)
- [Tau Ceti roadmap status: Pseudodifferential operators and elliptic analysis on bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PseudodifferentialOperators/STATUS.md)
