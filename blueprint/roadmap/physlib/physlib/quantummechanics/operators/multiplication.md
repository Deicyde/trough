---
declaration: module
origin: cited
lean: QuantumMechanics.SpaceDHilbertSpace.mulOperator, QuantumMechanics.SpaceDHilbertSpace.mem_mulOperator_domain_iff, QuantumMechanics.SpaceDHilbertSpace.mulOperator_apply_ae, QuantumMechanics.SpaceDHilbertSpace.mulOperator_domain_eq_top, QuantumMechanics.SpaceDHilbertSpace.mulOperator_domain_antitone, QuantumMechanics.SpaceDHilbertSpace.mem_mulOperator_domain_of_ae_eq_indicator, QuantumMechanics.SpaceDHilbertSpace.mulOperator_domain_eq_of_congr_norm, QuantumMechanics.SpaceDHilbertSpace.mulOperator_conj_domain
statement: formalized
proof: formalized
---

# Multiplication operators on `SpaceDHilbertSpace`

The module `Physlib.QuantumMechanics.Operators.Multiplication`, [Physlib/QuantumMechanics/Operators/Multiplication.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean): 29 declarations, 29 with a docstring; 2 private, not shown.

## i. Overview

> In this module we define and develop the properties of multiplication operators.
> Given a measure `μ` on `Space d` and any function `f : Space d → ℂ`, the multiplication operator
> `𝓜 μ f` is the partial linear map on `SpaceDHilbertSpace d μ` with domain
> `{ψ : SpaceDHilbertSpace d μ | MemHS (f • ψ) μ}` and mapping `ψ` to `f • ψ`.
> Prime examples of multiplication operators are the position operators which multiply by `xᵢ` and
> the potential operators which multiply by the potential function `V(x)` of a quantum system.
>
> Although the domain of `𝓜 μ f` is defined implicitly through `MemHS`, simple assumptions on `f`
> allow one to nail down some of its properties. For example, when `f` is `μ`-a.e. strongly measurable
> then the corresponding multiplication operator is densely defined, if `f` is `μ`-a.e. bounded then
> the domain is `⊤` and if `f` has temperate growth then the domain contains the Schwartz submodule.
>
> Multiplication operators also form the backbone for derivative operators, which are defined
> through multiplication in the Fourier domain: see `Operators/Derivative.lean`.

## ii. Key results

> - `mulOperator μ f` (notation `𝓜 μ f`) : The operator defined by `ψ ↦ f • ψ`
>     with maximal domain `{ψ : SpaceDHilbertSpace d μ | MemHS (f • ψ) μ}`.
> - `mulOperator_adjoint_eq_conj` : The adjoint of `𝓜 μ f` is the multiplication operator
>     defined by the conjugate of `f`.
> - `mulOperator_isSelfAdjoint` : The multiplication operator of a real function is self-adjoint.
> - `mulOperator_isUnbounded` : Multiplication operators with maximal domain are unbounded
>     (i.e. densely defined and closable).
> - `mulOperator_isClosed` : Multiplication operators with maximal domain are closed.
> - `mulOperator_eq_iff_ae_eq` : `𝓜 μ f = 𝓜 μ g ↔ f =ᵐ[μ] g` for `μ`-a.e. strongly measurable `f`
>     and σ-finite `μ`.
> - `mulOperator_const_smul_eq` : `𝓜 μ (c • f) = c • 𝓜 μ f` for non-zero `c`.
> - `mulOperator_add_ge` / `mulOperator_sub_ge` : `𝓜 μ (f ± g)` is an extension of `𝓜 μ f ± 𝓜 μ g`.
> - `mulOperator_smul_ge` : `𝓜 μ (f • g)` is an extension of `𝓜 μ f * 𝓜 μ g`.

## iv. References

> * Konrad Schmüdgen, Unbounded Self-Adjoint Operators on Hilbert Space, examples 1.3 and 3.8.
>   [ref: Schmudgen2012]

## A. Definition

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L85).

> The multiplication operator which maps `ψ` to the equivalence class of `f • ψ`
> with maximal domain `{ψ : SpaceDHilbertspace d μ | MemHS (f • ψ) μ}`.

```lean
def mulOperator (μ : Measure (Space d)) (f : Space d → ℂ) :
    SpaceDHilbertSpace d μ →ₗ.[ℂ] SpaceDHilbertSpace d μ
```

**`QuantumMechanics.SpaceDHilbertSpace.mem_mulOperator_domain_iff`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L119).

> The multiplication operator `𝓜 μ f` has maximal domain: `ψ` is in the domain exactly
> when multiplying by `f` gives an element of the Hilbert space.

```lean
lemma mem_mulOperator_domain_iff
    {μ : Measure (Space d)} {f : Space d → ℂ} {ψ : SpaceDHilbertSpace d μ} :
    ψ ∈ (𝓜 μ f).domain ↔ MemHS (f • ⇑ψ) μ
```

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_apply_ae`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L125).

> The defining property of a multiplication operator: `ψ` is mapped to `f • ψ`.

```lean
lemma mulOperator_apply_ae {μ : Measure (Space d)} {f : Space d → ℂ} (ψ : (𝓜 μ f).domain) :
    𝓜 μ f ψ =ᵐ[μ] f • ψ
```

## B. Domain

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_domain_eq_top`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L134).

> The multiplication operator of a `μ`-a.e. bounded function has full domain.

```lean
lemma mulOperator_domain_eq_top {μ : Measure (Space d)}
    {f : Space d → ℂ} (hf : AEStronglyMeasurable f μ) {c : ℝ} (hfc : ∀ᵐ x ∂μ, ‖f x‖ ≤ c) :
    (𝓜 μ f).domain = ⊤
```

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_domain_antitone`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L144).

> The domains of multiplication operators shrink with increasing function norm.

```lean
lemma mulOperator_domain_antitone {μ : Measure (Space d)}
    {f g : Space d → ℂ} (hg : AEStronglyMeasurable g μ) (h : ∀ᵐ x ∂μ, ‖g x‖ ≤ ‖f x‖) :
    (𝓜 μ f).domain ≤ (𝓜 μ g).domain
```

**`QuantumMechanics.SpaceDHilbertSpace.mem_mulOperator_domain_of_ae_eq_indicator`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L154).

> A state which is `μ`-a.e. equal to the indicator of a set on which `f` is `μ`-a.e. bounded
> lies in the domain of `𝓜 μ f`.

```lean
lemma mem_mulOperator_domain_of_ae_eq_indicator {μ : Measure (Space d)} {f : Space d → ℂ}
    (hf : AEStronglyMeasurable f μ) {s : Set (Space d)} {c : ℝ}
    (hfc : ∀ᵐ x ∂μ, x ∈ s → ‖f x‖ ≤ c) {ψ : SpaceDHilbertSpace d μ}
    (hψ : ψ =ᵐ[μ] s.indicator 1) : ψ ∈ (𝓜 μ f).domain
```

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_domain_eq_of_congr_norm`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L166).

> The multiplication operators corresponding to functions
> of `μ`-a.e. equal norm have the same domain.

```lean
lemma mulOperator_domain_eq_of_congr_norm {μ : Measure (Space d)} {f g : Space d → ℂ}
    (hf : AEStronglyMeasurable f μ) (hg : AEStronglyMeasurable g μ) (h : ∀ᵐ x ∂μ, ‖f x‖ = ‖g x‖) :
    (𝓜 μ f).domain = (𝓜 μ g).domain
```

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_conj_domain`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L176).

> The multiplication operators corresponding to a function
> and its conjugate have the same domain.

```lean
lemma mulOperator_conj_domain
    {μ : Measure (Space d)} {f : Space d → ℂ} (hf : AEStronglyMeasurable f μ) :
    (𝓜 μ (conj ∘ f)).domain = (𝓜 μ f).domain
```

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_hasDenseDomain`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L183).

> The multiplication operator corresponding to a `μ`-a.e. strongly measurable function
> is densely defined.

```lean
lemma mulOperator_hasDenseDomain
    {μ : Measure (Space d)} {f : Space d → ℂ} (hf : AEStronglyMeasurable f μ) :
    (𝓜 μ f).HasDenseDomain
```

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_domain_ge_of_hasTemperateGrowth`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L232).

> The multiplication operator corresponding to a function of temperate growth
> contains all Schwartz maps in its domain.

```lean
lemma mulOperator_domain_ge_of_hasTemperateGrowth {f : Space d → ℂ} (hf : f.HasTemperateGrowth)
    (μ : Measure (Space d)) [μ.HasTemperateGrowth] [μ.IsOpenPosMeasure] :
    SchwartzSubmodule d μ ≤ (𝓜 μ f).domain
```

## C. Adjoint

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_adjoint_eq_conj`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L358).

> The adjoint of a multiplication operator is again a multiplication operator.

```lean
lemma mulOperator_adjoint_eq_conj {μ : Measure (Space d)} [IsFiniteMeasureOnCompacts μ]
    {f : Space d → ℂ} (hf : AEStronglyMeasurable f μ) :
    (𝓜 μ f)† = 𝓜 μ (conj ∘ f)
```

### C.1. Self-adjoint

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_isSelfAdjoint_ofReal`**, a lemma, [line 376](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L376).

> The multiplication operator corresponding to a real function is self-adjoint.

```lean
lemma mulOperator_isSelfAdjoint_ofReal {μ : Measure (Space d)} [IsFiniteMeasureOnCompacts μ]
    {f : Space d → ℂ} (hf : AEStronglyMeasurable f μ) (hf' : conj ∘ f = f) :
    IsSelfAdjoint (𝓜 μ f)
```

## D. Closed & unbounded

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_isClosable`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L386).

> Multiplication operators of `μ`-a.e. strongly measurable functions are closable.

```lean
lemma mulOperator_isClosable {μ : Measure (Space d)} [IsFiniteMeasureOnCompacts μ]
    {f : Space d → ℂ} (hf : AEStronglyMeasurable f μ) :
    (𝓜 μ f).IsClosable
```

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_isUnbounded`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L394).

> Multiplication operators of `μ`-a.e. strongly measurable functions are unbounded.

```lean
lemma mulOperator_isUnbounded {μ : Measure (Space d)} [IsFiniteMeasureOnCompacts μ]
    {f : Space d → ℂ} (hf : AEStronglyMeasurable f μ) :
    (𝓜 μ f).IsUnbounded
```

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_isClosed`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L400).

> Multiplication operators of `μ`-a.e. strongly measurable functions are closed.

```lean
lemma mulOperator_isClosed {μ : Measure (Space d)} [IsFiniteMeasureOnCompacts μ]
    {f : Space d → ℂ} (hf : AEStronglyMeasurable f μ) :
    (𝓜 μ f).IsClosed
```

## E. Basic properties

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_zero`**, a lemma, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L413).

> The multiplication operator of the zero function is the zero operator (domain `⊤`).

```lean
lemma mulOperator_zero (μ : Measure (Space d)) : 𝓜 μ 0 = 0
```

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_eq_of_congr_ae`**, a lemma, [line 420](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L420).

> `μ`-a.e. equal functions give rise to the same multiplication operator.

```lean
lemma mulOperator_eq_of_congr_ae {μ : Measure (Space d)} {f g : Space d → ℂ} (h : f =ᵐ[μ] g) :
    𝓜 μ f = 𝓜 μ g
```

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_eq_iff_ae_eq`**, a lemma, [line 430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L430).

> For a `μ`-a.e. strongly measurable `f` and σ-finite `μ`, the multiplication
> operator determines the function up to `μ`-a.e. equality.
> No measurability of `g` is needed.

```lean
lemma mulOperator_eq_iff_ae_eq {μ : Measure (Space d)} [SigmaFinite μ] {f g : Space d → ℂ}
    (hf : AEStronglyMeasurable f μ) : 𝓜 μ f = 𝓜 μ g ↔ f =ᵐ[μ] g
```

### E.1. Smul & neg

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_const_smul_ge`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L460).

> Scalar multiplication and `mulOperator` commute except possibly for `c = 0`
> where the domains of `0 • 𝓜 μ f` and `𝓜 μ 0 = 0` may not agree.
>
> See `mulOperator_const_smul_eq` for equality when `c ≠ 0`.

```lean
lemma mulOperator_const_smul_ge (μ : Measure (Space d)) (f : Space d → ℂ) (c : ℂ) :
    c • 𝓜 μ f ≤ 𝓜 μ (c • f)
```

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_const_smul_eq`**, a lemma, [line 476](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L476).

> Scalar multiplication and `mulOperator` commute for `c ≠ 0`.

```lean
lemma mulOperator_const_smul_eq (μ : Measure (Space d)) (f : Space d → ℂ) {c : ℂ} (hc : c ≠ 0) :
    𝓜 μ (c • f) = c • 𝓜 μ f
```

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_neg`**, a lemma, [line 484](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L484).

> Negation and `mulOperator` commute.

```lean
lemma mulOperator_neg (μ : Measure (Space d)) (f : Space d → ℂ) : 𝓜 μ (-f) = -𝓜 μ f
```

### E.2. Add & sub

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_add_ge`**, a lemma, [line 499](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L499).

> `𝓜 μ (f + g)` extends `𝓜 μ f + 𝓜 μ g`.
>
> In general the domains do not match: `ψ ∈ (𝓜 μ f + 𝓜 μ g).domain` amounts to `MemHS (f • ψ) μ`
> \_and\_ `MemHS (g • ψ) μ` whereas `ψ ∈ (𝓜 μ (f + g)).domain` is equivalent to the weaker condition
> `MemHS ((f + g) • ψ) μ`.
>
> See `mulOperator_add_eq` and `mulOperator_add_eq'` for sufficient conditions
> to ensure equality.

```lean
lemma mulOperator_add_ge (μ : Measure (Space d)) (f g : Space d → ℂ) :
    𝓜 μ f + 𝓜 μ g ≤ 𝓜 μ (f + g)
```

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_add_eq`**, a lemma, [line 516](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L516).

> `(𝓜 μ g).domain = ⊤` is a sufficient condition to ensure equality in `mulOperator_add_ge`.

```lean
lemma mulOperator_add_eq
    {μ : Measure (Space d)} (f : Space d → ℂ) {g : Space d → ℂ} (h : (𝓜 μ g).domain = ⊤) :
    𝓜 μ (f + g) = 𝓜 μ f + 𝓜 μ g
```

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_add_eq'`**, a lemma, [line 528](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L528).

> Having both `‖f x‖ ≤ c * ‖f x + g x‖` and `‖g x‖ ≤ c' * ‖f x + g x‖` `μ`-a.e. is a sufficient
> condition to ensure equality in `mulOperator_add_ge`.

```lean
lemma mulOperator_add_eq' {μ : Measure (Space d)}
    {f g : Space d → ℂ} (hf : AEStronglyMeasurable f μ) (hg : AEStronglyMeasurable g μ)
    (c c' : ℝ) (hf' : ∀ᵐ x ∂μ, ‖f x‖ ≤ c * ‖f x + g x‖) (hg' : ∀ᵐ x ∂μ, ‖g x‖ ≤ c' * ‖f x + g x‖) :
    𝓜 μ (f + g) = 𝓜 μ f + 𝓜 μ g
```

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_sub_ge`**, a lemma, [line 554](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L554).

> `𝓜 μ (f - g)` extends `𝓜 μ f - 𝓜 μ g`.
>
> In general the domains do not match: `ψ ∈ (𝓜 μ f - 𝓜 μ g).domain` amounts to `MemHS (f • ψ) μ`
> \_and\_ `MemHS (g • ψ) μ` whereas `ψ ∈ (𝓜 μ (f - g)).domain` is equivalent to the weaker condition
> `MemHS ((f - g) • ψ) μ`.
>
> See `mulOperator_sub_eq` and `mulOperator_sub_eq'` for sufficient conditions
> to ensure equality.

```lean
lemma mulOperator_sub_ge (μ : Measure (Space d)) (f g : Space d → ℂ) :
    𝓜 μ f - 𝓜 μ g ≤ 𝓜 μ (f - g)
```

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_sub_eq`**, a lemma, [line 560](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L560).

> `(𝓜 μ g).domain = ⊤` is a sufficient condition to ensure equality in `mulOperator_sub_ge`.

```lean
lemma mulOperator_sub_eq
    {μ : Measure (Space d)} (f : Space d → ℂ) {g : Space d → ℂ} (h : (𝓜 μ g).domain = ⊤) :
    𝓜 μ (f - g) = 𝓜 μ f - 𝓜 μ g
```

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_sub_eq'`**, a lemma, [line 567](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L567).

> Having both `‖f x‖ ≤ c * ‖f x - g x‖` and `‖g x‖ ≤ c' * ‖f x - g x‖` `μ`-a.e. is a sufficient
> condition to ensure equality in `mulOperator_sub_ge`.

```lean
lemma mulOperator_sub_eq' {μ : Measure (Space d)}
    {f g : Space d → ℂ} (hf : AEStronglyMeasurable f μ) (hg : AEStronglyMeasurable g μ)
    (c c' : ℝ) (hf' : ∀ᵐ x ∂μ, ‖f x‖ ≤ c * ‖f x - g x‖) (hg' : ∀ᵐ x ∂μ, ‖g x‖ ≤ c' * ‖f x - g x‖) :
    𝓜 μ (f - g) = 𝓜 μ f - 𝓜 μ g
```

### E.3. Composition

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_smul_ge`**, a lemma, [line 587](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L587).

> `𝓜 μ (f • g)` extends `𝓜 μ f * 𝓜 μ g`.
>
> In general the domains do not match: `ψ ∈ (𝓜 μ f * 𝓜 μ g).domain`
> amounts to `MemHS (g • ψ) μ` \_and\_ `MemHS (f • g • ψ) μ` whereas
> `ψ ∈ (𝓜 μ (f • g)).domain` only requires `MemHS (f • g • ψ) μ`.
>
> See `mulOperator_smul_eq` for a sufficient condition to ensure equality.

```lean
lemma mulOperator_smul_ge (μ : Measure (Space d)) (f g : Space d → ℂ) :
    𝓜 μ f ∘ᵣ 𝓜 μ g ≤ 𝓜 μ (f • g)
```

**`QuantumMechanics.SpaceDHilbertSpace.mulOperator_smul_eq`**, a lemma, [line 603](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean#L603).

> `(𝓜 μ g).domain = ⊤` is a sufficient condition to ensure equality in `mulOperator_smul_ge`.

```lean
lemma mulOperator_smul_eq
    {μ : Measure (Space d)} (f : Space d → ℂ) {g : Space d → ℂ} (h : (𝓜 μ g).domain = ⊤) :
    𝓜 μ f ∘ᵣ 𝓜 μ g = 𝓜 μ (f • g)
```

## F. Spectrum

## Depends on

- [Schwartz submodule](../hilbertspaces/spaced/schwartzsubmodule.md)
- [Unbounded operators](unbounded.md)

## Sources

- [Physlib/QuantumMechanics/Operators/Multiplication.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Multiplication.lean)
