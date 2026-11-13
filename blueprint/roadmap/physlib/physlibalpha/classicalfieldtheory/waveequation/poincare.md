---
declaration: module
origin: cited
lean: WaveEquation.sum_eta_lorentz, WaveEquation.deriv_finset_sum, WaveEquation.deriv_deriv_comp_lorentz, WaveEquation.waveTrace_comp_lorentz, WaveEquation.deriv_comp_add_right, WaveEquation.waveTrace_act, WaveEquation.smoothWaveOperator_actSmooth
statement: formalized
proof: formalized
---

# The wave operator is Poincaré invariant

The module `PhyslibAlpha.ClassicalFieldTheory.WaveEquation.Poincare`, [PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Poincare.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Poincare.lean): 7 declarations, 7 with a docstring.

> The wave operator commutes with the action of the Poincaré group on fields.

## i. Overview

> The wave operator is the Minkowski metric trace of the second derivative. A Lorentz
> transformation changes the second derivative by the matrix of the transformation. The metric
> trace is unchanged because the matrix preserves the metric. A translation commutes with every
> derivative. Together these show that the wave operator commutes with the action of the Poincaré
> group on smooth fields.

## ii. Key results

> - `sum_eta_lorentz` : the matrix of a Lorentz transformation preserves the metric.
> - `waveTrace_comp_lorentz` : the metric trace of the second derivative of `u ∘ Λ`.
> - `smoothWaveOperator_actSmooth` : the wave operator commutes with the action of the Poincaré group.

## iv. References

> None.

## A. The metric is preserved

> - `sum_eta_lorentz` : the matrix of a Lorentz transformation preserves the metric.

## B. Derivatives of Lorentz transformed functions

> - `waveTrace_comp_lorentz` : the metric trace of the second derivative of `u ∘ Λ`.

## C. Derivatives of translated functions

> - `deriv_comp_add_right` : a translation commutes with the spacetime derivative.

**`WaveEquation.sum_eta_lorentz`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Poincare.lean#L68).

> The matrix of a Lorentz transformation preserves the metric.

```lean
lemma sum_eta_lorentz (Λ : LorentzGroup d) (ν ρ : Fin 1 ⊕ Fin d) :
    ∑ μ, η μ μ * Λ.1 ν μ * Λ.1 ρ μ = η ν ρ
```

**`WaveEquation.deriv_finset_sum`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Poincare.lean#L96).

> The spacetime derivative of a finite sum is the sum of the derivatives.

```lean
lemma deriv_finset_sum {ι : Type*} (s : Finset ι) (f : ι → SpaceTime d → V)
    (hf : ∀ i ∈ s, Differentiable ℝ (f i)) (μ : Fin 1 ⊕ Fin d) (x : SpaceTime d) :
    ∂_ μ (fun y => ∑ i ∈ s, f i y) x = ∑ i ∈ s, ∂_ μ (f i) x
```

**`WaveEquation.deriv_deriv_comp_lorentz`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Poincare.lean#L103).

> The second derivative of a Lorentz transformed function.

```lean
lemma deriv_deriv_comp_lorentz (u : SpaceTime d → V) (hu : ContDiff ℝ ∞ u) (Λ : LorentzGroup d)
    (μ : Fin 1 ⊕ Fin d) (x : SpaceTime d) :
    ∂_ μ (∂_ μ (fun y => u (Λ • y))) x =
      ∑ ν, ∑ ρ, (Λ.1 ν μ * Λ.1 ρ μ) • ∂_ ρ (∂_ ν u) (Λ • x)
```

**`WaveEquation.waveTrace_comp_lorentz`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Poincare.lean#L128).

> The metric trace of the second derivative of a Lorentz transformed function.

```lean
lemma waveTrace_comp_lorentz (u : SpaceTime d → V) (hu : ContDiff ℝ ∞ u) (Λ : LorentzGroup d)
    (x : SpaceTime d) :
    ∑ μ, (η μ μ : ℝ) • ∂_ μ (∂_ μ (fun y => u (Λ • y))) x =
      ∑ ν, (η ν ν : ℝ) • ∂_ ν (∂_ ν u) (Λ • x)
```

**`WaveEquation.deriv_comp_add_right`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Poincare.lean#L159).

> A translation commutes with the spacetime derivative.

```lean
lemma deriv_comp_add_right (u : SpaceTime d → V) (b : SpaceTime d) (μ : Fin 1 ⊕ Fin d) :
    ∂_ μ (fun y => u (y + b)) = fun y => ∂_ μ u (y + b)
```

**`WaveEquation.waveTrace_act`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Poincare.lean#L166).

> The metric trace of the second derivative of a transformed function.

```lean
lemma waveTrace_act (g : PoincareGroup d) (u : SpaceTime d → V) (hu : ContDiff ℝ ∞ u)
    (x : SpaceTime d) :
    ∑ μ, (η μ μ : ℝ) • ∂_ μ (∂_ μ (PoincareGroup.act g u)) x =
      ∑ μ, (η μ μ : ℝ) • ∂_ μ (∂_ μ u) (g⁻¹ • x)
```

**`WaveEquation.smoothWaveOperator_actSmooth`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Poincare.lean#L185).

> The wave operator commutes with the action of the Poincaré group.

```lean
lemma smoothWaveOperator_actSmooth (g : PoincareGroup d) (u : smoothFields d V) :
    smoothWaveOperator (PoincareGroup.actSmooth g u) =
      PoincareGroup.actSmooth g (smoothWaveOperator u)
```

## Depends on

- [The wave operator](basic.md)
- [The Poincaré action on smooth fields](../../relativity/poincare/fields.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Poincare.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Poincare.lean)
