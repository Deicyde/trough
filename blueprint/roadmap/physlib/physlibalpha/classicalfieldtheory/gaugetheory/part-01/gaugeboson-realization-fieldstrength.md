---
declaration: module
origin: cited
lean: GaugeAlgebraRealization.fieldStrength, GaugeAlgebraRealization.fieldStrength_apply, GaugeAlgebraRealization.fieldStrength_zero, GaugeAlgebraRealization.pair_eq_fieldStrength_sub_commutatorFam, GaugeAlgebraRealization.bracketFam_swap_of_commute, GaugeAlgebraRealization.commutatorFam_swap, GaugeAlgebraRealization.fieldStrength_swap, GaugeAlgebraRealization.fieldStrength_map
statement: formalized
proof: formalized
---

# The field strength

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.Realization.FieldStrength`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/FieldStrength.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/FieldStrength.lean): 11 declarations, 10 with a docstring.

## i. Overview

> The field strength is defined as
> ```
>   F_{μν} = ∂_μ A_ν − ∂_ν A_μ + ⁅A_μ, A_ν⁆
> ```
> with `⁅·,·⁆` the gauge-algebra bracket, which already carries the physicists' factor
> of `i` (on the matrix factors `⁅a, b⁆ = i(ab − ba)`). In terms of the plain matrix
> commutator this is `F_{μν} = ∂_μ A_ν − ∂_ν A_μ + i [A_μ, A_ν]`, the sign forced by
> the convention `ω_μ(g) = i (∂_μ g) g⁻¹` for the Maurer–Cartan form (equivalently, by
> its structural equation `∂_μ ω_ν − ∂_ν ω_μ + ⁅ω_μ, ω_ν⁆ = 0`): only with this
> coefficient do the inhomogeneous terms cancel. With the derivative symbols as
> primitives the field strength is itself a family of derivative symbols
> `s ↦ [∂_s F_μν]`: the derivative terms shift the multiset index, the commutator term
> is the Leibniz convolution `commutatorFam`. It transforms in the adjoint at every
> derivative order simultaneously (`repGauge_fieldStrength`,
> `transformsInAdjoint_fieldStrength`).

## ii. Key results

> - `repGauge_fieldStrength` : the field strength transforms in the adjoint, at every derivative
>   order: under a gauge jet `U` every derivative symbol of `F_μν` transforms by the pure Leibniz
>   convolution of the dual adjoint action over the multiset antidiagonal — the exact analogue of
>   `gauge_apply_deriv` with *no* Maurer–Cartan shift, since the field strength transforms
>   homogeneously
> - `transformsInAdjoint_fieldStrength` : the field strength is an adjoint gauge tensor: the packaging
>   of `repGauge_fieldStrength` as `TransformsInAdjoint` — the base case of the covariant-derivative
>   recursion `TransformsInAdjoint.covDerivAdjoint`

## iv. References

> * None.

**`GaugeAlgebraRealization.fieldStrength`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/FieldStrength.lean#L76).

> The field strength `F_μν = ∂_μ A_ν − ∂_ν A_μ + ⁅A_μ, A_ν⁆` of a family of
> gauge-field symbols, as a family of derivative symbols: the `s`-th derivative has
> the derivative terms through the shifted symbols `A (μ ::ₘ s) ν`, the commutator
> term through the Leibniz convolution `commutatorFam`. This is the physicists'
> `F_μν^a = ∂_μ A_ν^a − ∂_ν A_μ^a + f^a_{bc} A_μ^b A_ν^c`: the gauge-algebra bracket
> already carries the physicists' factor of `i`, so no explicit factor appears — the
> same normalization as in the structural equation of the Maurer–Cartan form, which
> is exactly what makes the field strength transform without inhomogeneous terms
> (`repGauge_fieldStrength`).

```lean
noncomputable def fieldStrength
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℝ 𝔤 →ₗ[ℝ] B
```

**`GaugeAlgebraRealization.fieldStrength_apply`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/FieldStrength.lean#L83).

```lean
lemma fieldStrength_apply
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ 𝔤) :
    fieldStrength A μ ν s φ = A (μ ::ₘ s) ν φ - A (ν ::ₘ s) μ φ + commutatorFam A μ ν s φ
```

**`GaugeAlgebraRealization.fieldStrength_zero`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/FieldStrength.lean#L91).

> The underived field strength: derivative symbols on singletons, plus the plain
> commutator.

```lean
lemma fieldStrength_zero
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (μ ν : Fin 1 ⊕ Fin 3) :
    fieldStrength A μ ν 0 = A {μ} ν - A {ν} μ + commutator A μ ν
```

**`GaugeAlgebraRealization.pair_eq_fieldStrength_sub_commutatorFam`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/FieldStrength.lean#L100).

> The antisymmetrized pair of derivative symbols is the field strength minus its
> commutator term.

```lean
lemma pair_eq_fieldStrength_sub_commutatorFam
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (ν μ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    A (ν ::ₘ s) μ - A (μ ::ₘ s) ν = fieldStrength A ν μ s - commutatorFam A ν μ s
```

## A. The antisymmetry of the field strength

> The field strength is antisymmetric in its two covector indices as soon as the
> symbols of the gauge field commute with one another in `B`: the two derivative terms
> swap outright, and the commutator term swaps by the antisymmetry of the gauge-algebra
> bracket, once the two factors of each product may be exchanged.

**`GaugeAlgebraRealization.bracketFam_swap_of_commute`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/FieldStrength.lean#L120).

> The bracket of two component families with commuting values is antisymmetric: in
> the basis expansion the structure constants are antisymmetric in the two gauge
> indices, and the two field factors of each term may be exchanged.

```lean
lemma bracketFam_swap_of_commute {f g : Module.Dual ℝ 𝔤 →ₗ[ℝ] B}
    (hfg : ∀ φ ψ, Commute (f φ) (g ψ)) :
    bracketFam g f = - bracketFam f g
```

**`GaugeAlgebraRealization.commutatorFam_swap`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/FieldStrength.lean#L138).

> The derived commutator term is antisymmetric in its two directions when the symbols
> of the gauge field commute: swapping the two parts of the antidiagonal matches the
> Leibniz convolution with the swapped one termwise.

```lean
lemma commutatorFam_swap
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (hA : ∀ (s s' : Multiset (Fin 1 ⊕ Fin 3)) (μ μ' : Fin 1 ⊕ Fin 3)
      (ψ ψ' : Module.Dual ℝ 𝔤), Commute (A s μ ψ) (A s' μ' ψ'))
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    commutatorFam A ν μ s = - commutatorFam A μ ν s
```

**`GaugeAlgebraRealization.fieldStrength_swap`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/FieldStrength.lean#L153).

> The field strength is antisymmetric in its two covector indices when the symbols of
> the gauge field commute: the two derivative terms swap outright, the commutator term
> by `commutatorFam_swap`.

```lean
lemma fieldStrength_swap
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (hA : ∀ (s s' : Multiset (Fin 1 ⊕ Fin 3)) (μ μ' : Fin 1 ⊕ Fin 3)
      (ψ ψ' : Module.Dual ℝ 𝔤), Commute (A s μ ψ) (A s' μ' ψ'))
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    fieldStrength A ν μ s = - fieldStrength A μ ν s
```

**`GaugeAlgebraRealization.fieldStrength_map`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/FieldStrength.lean#L164).

> The field strength is natural in the algebra: a multiplicative linear map carries the
> field strength of a family to the field strength of its image.

```lean
lemma fieldStrength_map {B' : Type} [Ring B'] [Module ℝ B'] [SMulCommClass ℝ B' B']
    [IsScalarTower ℝ B' B'] (Φ : B →ₗ[ℝ] B') (hΦ : ∀ b₁ b₂, Φ (b₁ * b₂) = Φ b₁ * Φ b₂)
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    fieldStrength (fun p ρ => Φ ∘ₗ A p ρ) μ ν s = Φ ∘ₗ fieldStrength A μ ν s
```

**`GaugeAlgebraRealization.repGauge_fieldStrength`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/FieldStrength.lean#L190).

> **The field strength transforms in the adjoint, at every derivative order**: under
> a gauge jet `U` every derivative symbol of `F_μν` transforms by the pure Leibniz
> convolution of the dual adjoint action over the multiset antidiagonal — the exact
> analogue of `gauge_apply_deriv` with *no* Maurer–Cartan shift, since the field
> strength transforms homogeneously. The `κ`-into-the-adjoint splittings of the
> derivative terms (`repGauge_cons_apply`) cancel the `ad` cross-term convolutions of
> the commutator (`repGauge_commutatorFam`) through the coassociativity and swap of
> the antidiagonal, and the derived Maurer–Cartan shifts cancel the bracket-shift
> convolution through the all-orders structural equation.

```lean
lemma repGauge_fieldStrength
    (U : GJ) (s : Multiset (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    repGauge U (fieldStrength h.A μ ν s φ) =
      (s.antidiagonal.map fun p =>
        fieldStrength h.A μ ν p.2 (jets.adjointDualCoeff U⁻¹ p.1 φ)).sum
```

**`GaugeAlgebraRealization.transformsInAdjoint_fieldStrength`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/FieldStrength.lean#L268).

> **The field strength is an adjoint gauge tensor**: the packaging of
> `repGauge_fieldStrength` as `TransformsInAdjoint` — the base case of the
> covariant-derivative recursion `TransformsInAdjoint.covDerivAdjoint`.

```lean
lemma transformsInAdjoint_fieldStrength
    (μ ν : Fin 1 ⊕ Fin 3) : TransformsInAdjoint jets repGauge (fieldStrength h.A μ ν)
```

**`GaugeAlgebraRealization.repGauge_fieldStrength_zero`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/FieldStrength.lean#L275).

> The underived transformation law: at `s = 0` the Leibniz convolution collapses to
> the homogeneous law — the field strength transforms by the base-point dual adjoint
> action of `U⁻¹` on the adjoint index.

```lean
lemma repGauge_fieldStrength_zero
    (U : GJ) (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    repGauge U (fieldStrength h.A μ ν 0 φ) =
      fieldStrength h.A μ ν 0 (jets.adjointDualCoeff U⁻¹ 0 φ)
```

## Depends on

- [Adjoint gauge tensors and the covariant derivative](../part-02/gaugeboson-realization-transformsadjoint.md)

## Proof depends on

- [The Maurer–Cartan form of a local gauge data package](../part-04/localgaugedata-maurercartan.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/FieldStrength.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/FieldStrength.lean)
