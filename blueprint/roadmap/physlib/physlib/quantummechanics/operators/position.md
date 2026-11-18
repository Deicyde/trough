---
declaration: module
origin: cited
lean: QuantumMechanics.positionCLM, QuantumMechanics.positionCLM_apply_fun, QuantumMechanics.positionCLM_apply, QuantumMechanics.positionCLM_inner, QuantumMechanics.radiusRegPowCLM, QuantumMechanics.radiusRegPowCLM_apply_fun, QuantumMechanics.radiusRegPowCLM_apply, QuantumMechanics.radiusRegPowCLM_comp_eq
statement: formalized
proof: formalized
---

# Position operators

The module `Physlib.QuantumMechanics.Operators.Position`, [Physlib/QuantumMechanics/Operators/Position.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean): 36 declarations (1 instance with no name), 14 with a docstring; 1 private, not shown.

## i. Overview

> In this module we introduce several position operators for quantum mechanics on `Space d`.

## ii. Key results

> Definitions:
> - `positionCLM` : (components of) the position vector operator acting on Schwartz maps
>     `𝓢(Space d, ℂ)` by multiplication by `xᵢ`.
> - `radiusRegPowCLM` : operator acting on Schwartz maps by multiplication by
>     `(‖x‖² + ε²)^(s/2)`, a smooth regularization of `‖x‖ˢ`.
> - `positionOperator` : a self-adjoint multiplication operator acting on `SpaceDHilbertSpace d`.
> - `readiusRegPowOperator` : a self-adjoint multiplication operator acting on `SpaceDHilbertSpace d`.
>
> Notation:
> - `𝐱` for `positionCLM`
> - `𝐫₀` for `radiusRegPowCLM`
> - `𝐫` for `radiusPowLM`

## iv. References

> * None.

## A. Schwartz operators

### A.1. Position vector

**`QuantumMechanics.positionCLM`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L79).

> Component `i` of the position operator is the continuous linear map
> from `𝓢(Space d, ℂ)` to itself which maps `ψ` to `xᵢψ`.

```lean
def positionCLM : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)
```

**`QuantumMechanics.positionCLM_apply_fun`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L88).

```lean
lemma positionCLM_apply_fun (ψ : 𝓢(Space d, ℂ)) : 𝐱 i ψ = (fun x : Space d ↦ x i) • ⇑ψ
```

**`QuantumMechanics.positionCLM_apply`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L95).

```lean
lemma positionCLM_apply (ψ : 𝓢(Space d, ℂ)) (x : Space d) : 𝐱 i ψ x = x i * ψ x
```

**`QuantumMechanics.positionCLM_inner`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L100).

> The position operator is symmetric on Schwartz maps, in terms of `positionCLM`.

```lean
lemma positionCLM_inner (f g : 𝓢(Space d, ℂ)) :
    ⟪(SpaceDHilbertSpace.schwartzEquiv volume (𝐱 i f) : SpaceDHilbertSpace d),
      SpaceDHilbertSpace.schwartzEquiv volume g⟫_ℂ
      = ⟪(SpaceDHilbertSpace.schwartzEquiv volume f : SpaceDHilbertSpace d),
        SpaceDHilbertSpace.schwartzEquiv volume (𝐱 i g)⟫_ℂ
```

### A.2. Radius powers (regularized)

**`QuantumMechanics.radiusRegPowCLM`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L117).

> The radius operator to power `s`, regularized by `ε ≠ 0`, is the continuous linear map
> from `𝓢(Space d, ℂ)` to itself which maps `ψ` to `(‖x‖² + ε²)^(s/2) • ψ`.

```lean
def radiusRegPowCLM {d : ℕ} (ε : ℝˣ) (s : ℝ) : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)
```

**`QuantumMechanics.radiusRegPowCLM_apply_fun`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L126).

```lean
lemma radiusRegPowCLM_apply_fun {d : ℕ} (ε : ℝˣ) (s : ℝ) (ψ : 𝓢(Space d, ℂ)) :
    𝐫₀ ε s ψ = fun x ↦ (‖x‖ ^ 2 + ε ^ 2) ^ (s / 2) • ψ x
```

**`QuantumMechanics.radiusRegPowCLM_apply`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L134).

```lean
lemma radiusRegPowCLM_apply {d : ℕ} (ε : ℝˣ) (s : ℝ) (ψ : 𝓢(Space d, ℂ)) (x : Space d) :
    𝐫₀ ε s ψ x = (‖x‖ ^ 2 + ε ^ 2) ^ (s / 2) • ψ x
```

**`QuantumMechanics.radiusRegPowCLM_comp_eq`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L139).

```lean
lemma radiusRegPowCLM_comp_eq {d : ℕ} (ε : ℝˣ) (s t : ℝ) :
    𝐫₀[d] ε s ∘L 𝐫₀ ε t = 𝐫₀ ε (s+t)
```

**`QuantumMechanics.radiusRegPowCLM_zero`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L145).

```lean
lemma radiusRegPowCLM_zero {d : ℕ} (ε : ℝˣ) :
    𝐫₀ ε 0 = ContinuousLinearMap.id ℂ 𝓢(Space d, ℂ)
```

**`QuantumMechanics.positionSqCLM_eq`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L150).

```lean
lemma positionSqCLM_eq {d : ℕ} (ε : ℝˣ) :
    ∑ i, 𝐱 i ∘L 𝐱 i = 𝐫₀ ε 2 - ε.1 ^ 2 • ContinuousLinearMap.id ℂ 𝓢(Space d, ℂ)
```

### A.3. Radius powers

**`QuantumMechanics.radiusPowLM`**, a def, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L161).

> The radius operator to power `s` is the linear map from `𝓢(Space d, ℂ)` to `Space d → ℂ` that
> maps `ψ` to `x ↦ ‖x‖ˢψ(x)` (which is 'nearly' Schwartz for general `s`).

```lean
def radiusPowLM {d : ℕ} (s : ℝ) : 𝓢(Space d, ℂ) →ₗ[ℂ] Space d → ℂ
```

**`QuantumMechanics.radiusPowLM_apply_fun`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L172).

```lean
lemma radiusPowLM_apply_fun {d : ℕ} (s : ℝ) (ψ : 𝓢(Space d, ℂ)) :
    𝐫 s ψ = fun x ↦ ‖x‖ ^ s • ψ x
```

**`QuantumMechanics.radiusPowLM_apply`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L176).

```lean
lemma radiusPowLM_apply {d : ℕ} (s : ℝ) (ψ : 𝓢(Space d, ℂ)) (x : Space d) :
    𝐫 s ψ x = ‖x‖ ^ s • ψ x
```

**`QuantumMechanics.radiusPowLM_apply_contDiffAt`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L182).

> `x ↦ ‖x‖ˢψ(x)` is smooth away from `x = 0`.

```lean
lemma radiusPowLM_apply_contDiffAt {d : ℕ} (s : ℝ) (n : ℕ∞) (ψ : 𝓢(Space d, ℂ)) {x : Space d}
    (hx : x ≠ 0) : ContDiffAt ℝ n (𝐫 s ψ) x
```

**`QuantumMechanics.radiusPowLM_apply_stronglyMeasurable`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L192).

> `x ↦ ‖x‖ˢψ(x)` is strongly measurable.

```lean
lemma radiusPowLM_apply_stronglyMeasurable {d : ℕ} (s : ℝ) (ψ : 𝓢(Space d, ℂ)) :
    StronglyMeasurable (𝐫 s ψ)
```

**`QuantumMechanics.radiusPowLM_apply_memHS`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L199).

> `x ↦ ‖x‖ˢψ(x)` is square-integrable provided `s` is not too negative.

```lean
lemma radiusPowLM_apply_memHS {d : ℕ} (s : ℝ) (ψ : 𝓢(Space d, ℂ)) (a : ℕ)
    (hψ : ψ ∈ PolyBddSchwartzMap d a) (h : 0 < d + 2 * (a + s)) :
    MemHS (𝐫 s ψ)
```

#### A.3.1. As limit of regularized operators

**`QuantumMechanics.nhdsZeroUnits`**, an abbrev, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L276).

> Neighborhoods of "0" in the non-zero reals, i.e. those sets containing `(-ε,0) ∪ (0,ε) ⊆ ℝˣ`
> for some `ε > 0`.

```lean
abbrev nhdsZeroUnits : Filter ℝˣ
```

**An instance with no name**, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L278).

```lean
instance : NeBot nhdsZeroUnits
```

**`QuantumMechanics.radiusRegPow_tendsto_radiusPow`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L285).

> `𝐫[ε,s] ψ` converges pointwise to `𝐫[s] ψ` as `ε → 0` except perhaps at `x = 0`.

```lean
lemma radiusRegPow_tendsto_radiusPow {d : ℕ} (s : ℝ) (ψ : 𝓢(Space d, ℂ)) {x : Space d}
    (hx : x ≠ 0) : Tendsto (fun ε ↦ 𝐫₀ ε s ψ x) nhdsZeroUnits (nhds (𝐫 s ψ x))
```

**`QuantumMechanics.radiusRegPow_tendsto_radiusPow'`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L295).

> `𝐫[ε,s] ψ` converges pointwise to `𝐫[s] ψ` as `ε → 0` provided `𝐫[ε,s] ψ 0` is bounded.

```lean
lemma radiusRegPow_tendsto_radiusPow' {d : ℕ} (s : ℝ) (ψ : 𝓢(Space d, ℂ)) (h : 0 ≤ s ∨ ψ 0 = 0) :
    Tendsto (fun ε ↦ ⇑(𝐫₀ ε s ψ)) nhdsZeroUnits (nhds (𝐫 s ψ))
```

**`QuantumMechanics.radiusRegPow_ae_tendsto_radiusPow`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L311).

> a.e. version of `radiusRegPow_tendsto_radiusPow`

```lean
lemma radiusRegPow_ae_tendsto_radiusPow {d : ℕ} [NeZero d] (s : ℝ) (ψ : 𝓢(Space d, ℂ)) :
    ∀ᵐ x, Tendsto (fun ε ↦ 𝐫₀ ε s ψ x) nhdsZeroUnits (nhds (𝐫 s ψ x))
```

**`QuantumMechanics.radiusRegPow_ae_tendsto_iff`**, a lemma, [line 320](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L320).

```lean
lemma radiusRegPow_ae_tendsto_iff {d : ℕ} [NeZero d] {s : ℝ} {ψ : 𝓢(Space d, ℂ)}
    {φ : Space d → ℂ} : (∀ᵐ x, Tendsto (fun ε ↦ 𝐫₀ ε s ψ x) nhdsZeroUnits (nhds (φ x)))
    ↔ φ =ᵐ[volume] 𝐫 s ψ
```

## B. Unbounded operators

### B.1. Position vector

**`QuantumMechanics.positionOperator`**, a def, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L351).

> The operator on `SpaceDHilbertSpace d` acting by multiplication by `fun x ↦ xᵢ`.

```lean
def positionOperator : SpaceDHilbertSpace d μ →ₗ.[ℂ] SpaceDHilbertSpace d μ
```

**`QuantumMechanics.positionOperator_hasDenseDomain`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L357).

```lean
lemma positionOperator_hasDenseDomain : (𝓧 μ i).HasDenseDomain
```

**`QuantumMechanics.positionOperator_isSelfAdjoint`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L360).

```lean
lemma positionOperator_isSelfAdjoint [IsFiniteMeasureOnCompacts μ] : IsSelfAdjoint (𝓧 μ i)
```

**`QuantumMechanics.positionOperator_isUnbounded`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L363).

```lean
lemma positionOperator_isUnbounded [IsFiniteMeasureOnCompacts μ] : (𝓧 μ i).IsUnbounded
```

### B.2. Radius powers (regularized)

**`QuantumMechanics.radiusRegPowOperator`**, a def, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L372).

> The operator on `SpaceDHilbertSpace d` acting by multiplication by
> `fun x ↦ (‖x‖² + ε²)^(s/2)`.

```lean
def radiusRegPowOperator (ε : ℝˣ) (s : ℝ) :
    SpaceDHilbertSpace d μ →ₗ.[ℂ] SpaceDHilbertSpace d μ
```

**`QuantumMechanics.radiusRegPowOperator_hasDenseDomain`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L379).

```lean
lemma radiusRegPowOperator_hasDenseDomain (ε : ℝˣ) (s : ℝ) : (𝓡₀ μ ε s).HasDenseDomain
```

**`QuantumMechanics.radiusRegPowOperator_isSelfAdjoint`**, a lemma, [line 382](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L382).

```lean
lemma radiusRegPowOperator_isSelfAdjoint [IsFiniteMeasureOnCompacts μ] (ε : ℝˣ) (s : ℝ) :
    IsSelfAdjoint (𝓡₀ μ ε s)
```

**`QuantumMechanics.radiusRegPowOperator_isUnbounded`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L386).

```lean
lemma radiusRegPowOperator_isUnbounded [IsFiniteMeasureOnCompacts μ] (ε : ℝˣ) (s : ℝ) :
    (𝓡₀ μ ε s).IsUnbounded
```

### B.3. Radius powers

**`QuantumMechanics.radiusPowOperator`**, a def, [line 395](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L395).

> The operator on `SpaceDHilbertSpace d` acting by multiplication by `fun x ↦ ‖x‖ˢ`.

```lean
def radiusPowOperator (s : ℝ) : SpaceDHilbertSpace d μ →ₗ.[ℂ] SpaceDHilbertSpace d μ
```

**`QuantumMechanics.radiusPowOperator_hasDenseDomain`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L401).

```lean
lemma radiusPowOperator_hasDenseDomain (s : ℝ) : (𝓡 μ s).HasDenseDomain
```

**`QuantumMechanics.radiusPowOperator_isSelfAdjoint`**, a lemma, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L404).

```lean
lemma radiusPowOperator_isSelfAdjoint [IsFiniteMeasureOnCompacts μ] (s : ℝ) :
    IsSelfAdjoint (𝓡 μ s)
```

**`QuantumMechanics.radiusPowOperator_isUnbounded`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L408).

```lean
lemma radiusPowOperator_isUnbounded [IsFiniteMeasureOnCompacts μ] (s : ℝ) : (𝓡 μ s).IsUnbounded
```

**`QuantumMechanics.radiusPowLM_apply_polyBddSchwartz_memHS`**, a lemma, [line 420](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L420).

```lean
lemma radiusPowLM_apply_polyBddSchwartz_memHS
    {d : ℕ} {s : ℝ} (ψ : PolyBddSchwartzSubmodule d ⌊1 - d / 2 - s⌋.toNat) :
    MemHS (𝐫[d] s ((polyBddSchwartzEquiv volume).symm ψ))
```

**`QuantumMechanics.radiusPowOperator_domain_ge`**, a lemma, [line 426](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean#L426).

```lean
lemma radiusPowOperator_domain_ge {d : ℕ} (s : ℝ) :
    PolyBddSchwartzSubmodule d ⌊1 - d / 2 - s⌋.toNat ≤ (radiusPowOperator volume s).domain
```

## Depends on

- [Polynomially-bounded Schwartz submodules](../hilbertspaces/spaced/polybddschwartzsubmodule.md)
- [Multiplication operators on `SpaceDHilbertSpace`](multiplication.md)
- [Regularized powers of the norm on space](../../spaceandtime/space/part-02/norm-regularized.md)

## Proof depends on

- [Derivatives on Space](../../spaceandtime/space/part-01/derivatives-basic.md)
- [Integrability of norm powers on subsets of Space](../../spaceandtime/space/part-02/integrals-normpow.md)

## Sources

- [Physlib/QuantumMechanics/Operators/Position.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Position.lean)
