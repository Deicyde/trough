---
declaration: module
origin: cited
lean: QuantumMechanics.SpaceDHilbertSpace.PolyBddSchwartzMap, QuantumMechanics.SpaceDHilbertSpace.polyBddSchwartzIncl, QuantumMechanics.SpaceDHilbertSpace.PolyBddSchwartzSubmodule, QuantumMechanics.SpaceDHilbertSpace.polyBddSchwartzIncl_injective, QuantumMechanics.SpaceDHilbertSpace.polyBddSchwartzEquiv, QuantumMechanics.SpaceDHilbertSpace.PolyBddSchwartzSubmodule.toFun_eq_coe, QuantumMechanics.SpaceDHilbertSpace.PolyBddSchwartzSubmodule.polyBddSchwartzEquiv_symm_apply_coe, QuantumMechanics.SpaceDHilbertSpace.PolyBddSchwartzSubmodule.polyBddSchwartzEquiv_coe_ae
statement: formalized
proof: formalized
---

# Polynomially-bounded Schwartz submodules

The module `Physlib.QuantumMechanics.HilbertSpaces.SpaceD.PolyBddSchwartzSubmodule`, [Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean): 17 declarations (2 instances with no name), 4 with a docstring; 2 private, not shown.

## i. Overview

> In this module we define polynomially-bounded Schwartz submodules of `SpaceDHilbertSpace d μ`.
>
> For each `a : ℕ∞`, `PolyBddSchwartzSubmodule d a μ` is the submodule corresponding to Schwartz
> maps `f` satisfying the polynomial growth bounds `‖x‖ ^ (-k) * ‖f x‖ ≤ Cₖ` for all `(k : ℕ) ≤ a`.
> In particular, for `a = ⊤` such a bound holds for all natural numbers.
>
> These serve as a natural domain for singular unbounded operators. For example, the `1/r` Coulomb
> potential operator maps `PolyBddSchwartzSubmodule d ⊤ μ` to itself. In the same way that multiplying
> a Schwartz map by any polynomial in the coordinates results in a square-integrable function,
> polynomially-bounded Schwartz maps may be multiplied by Laurent polynomials and remain
> square-integrable (the precise condition depends on `d`, `a` and the negative degree of
> the Laurent polynomial).
>
> Note: the condition defining polynomially-bounded Schwartz maps is phrased as
> `‖x‖ ^ (-k) * ‖f x‖ ≤ Cₖ` rather than as `‖f x‖ ≤ Cₖ * ‖x‖ ^ k` to mirror `SchwartzMap.decay`.
> These two conditions only differ at `x = 0` and are therefore equivalent for `d > 0` since
> then `f 0` may be determined by continuity. For `d = 0` the former does not constrain `f 0 = 0`
> (since `x = 0` is the only point and `0⁻¹ = 0`) while the latter does (and would therefore spoil
> their being dense in `SpaceDHilbertSpace 0 ≅ ℂ`).

## ii. Key results

> - `PolyBddSchwartzSubmodule d (a : ℕ∞) μ`: Restriction of `SchwartzSubmodule d μ` to those
>   Schwartz maps which are bounded by powers of `‖x‖`.
> - `PolyBddSchwartzSubmodule.dense`: These submodules are dense in `SpaceDHilbertSpace d μ`.

## iv. References

> * None.

## A. Definitions

**`QuantumMechanics.SpaceDHilbertSpace.PolyBddSchwartzMap`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean#L72).

> A function is a bounded Schwartz map if it is both Schwartz and bounded by powers of `‖x‖`.

```lean
def PolyBddSchwartzMap (d : ℕ) (a : ℕ∞) : Submodule ℂ 𝓢(Space d, ℂ)
```

**`QuantumMechanics.SpaceDHilbertSpace.polyBddSchwartzIncl`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean#L92).

> The continuous linear map `schwartzIncl` with domain restricted to `PolyBddSchwartzMap d a`.

```lean
def polyBddSchwartzIncl {d : ℕ} {a : ℕ∞} (μ : Measure (Space d)) [μ.HasTemperateGrowth] :
    PolyBddSchwartzMap d a →L[ℂ] SpaceDHilbertSpace d μ
```

**`QuantumMechanics.SpaceDHilbertSpace.PolyBddSchwartzSubmodule`**, an abbrev, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean#L98).

> The submodule of `SpaceDHilbertSpace d` corresponding to bounded Schwartz maps.

```lean
abbrev PolyBddSchwartzSubmodule
    (d : ℕ) (a : ℕ∞) (μ : Measure (Space d) := volume) [μ.HasTemperateGrowth] :
    Submodule ℂ (SpaceDHilbertSpace d μ)
```

**`QuantumMechanics.SpaceDHilbertSpace.polyBddSchwartzIncl_injective`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean#L103).

```lean
lemma polyBddSchwartzIncl_injective
    {d : ℕ} (a : ℕ∞) (μ : Measure (Space d)) [μ.HasTemperateGrowth] [μ.IsOpenPosMeasure] :
    Function.Injective (polyBddSchwartzIncl (a := a) μ)
```

**`QuantumMechanics.SpaceDHilbertSpace.polyBddSchwartzEquiv`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean#L110).

> The linear equivalence between polynomially-bounded Schwartz maps and the corresponding
> submodule of the Hilbert space.

```lean
def polyBddSchwartzEquiv
    {d : ℕ} {a : ℕ∞} (μ : Measure (Space d)) [μ.HasTemperateGrowth] [μ.IsOpenPosMeasure] :
    PolyBddSchwartzMap d a ≃ₗ[ℂ] PolyBddSchwartzSubmodule d a μ
```

## B. Coercions

**An instance with no name**, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean#L124).

```lean
instance : CoeOut (PolyBddSchwartzMap d a) 𝓢(Space d, ℂ)
```

**An instance with no name**, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean#L126).

```lean
instance : CoeFun (PolyBddSchwartzMap d a) (fun _ ↦ Space d → ℂ)
```

**`QuantumMechanics.SpaceDHilbertSpace.PolyBddSchwartzSubmodule.toFun_eq_coe`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean#L129).

```lean
lemma toFun_eq_coe (f : PolyBddSchwartzMap d a) (x : Space d) : f.val.toFun x = f.val x
```

**`QuantumMechanics.SpaceDHilbertSpace.PolyBddSchwartzSubmodule.polyBddSchwartzEquiv_symm_apply_coe`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean#L131).

```lean
lemma polyBddSchwartzEquiv_symm_apply_coe [μ.IsOpenPosMeasure]
    {ψ : SchwartzSubmodule d μ} (hψ : ↑ψ ∈ PolyBddSchwartzSubmodule d a μ) :
    ((polyBddSchwartzEquiv μ).symm ⟨ψ, hψ⟩).val = (schwartzEquiv μ).symm ψ
```

**`QuantumMechanics.SpaceDHilbertSpace.PolyBddSchwartzSubmodule.polyBddSchwartzEquiv_coe_ae`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean#L142).

```lean
lemma polyBddSchwartzEquiv_coe_ae [μ.IsOpenPosMeasure] (f : PolyBddSchwartzMap d a) :
    polyBddSchwartzEquiv μ f =ᵐ[μ] f.val
```

### C. (In)equalities

**`QuantumMechanics.SpaceDHilbertSpace.PolyBddSchwartzSubmodule.PolyBddSchwartzMap_zero_eq_top`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean#L150).

```lean
lemma PolyBddSchwartzMap_zero_eq_top (d : ℕ) : PolyBddSchwartzMap d 0 = ⊤
```

**`QuantumMechanics.SpaceDHilbertSpace.PolyBddSchwartzSubmodule.PolyBddSchwartzMap_antitone`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean#L155).

```lean
lemma PolyBddSchwartzMap_antitone (d : ℕ) {a b : ℕ∞} (h : a ≤ b) :
    PolyBddSchwartzMap d b ≤ PolyBddSchwartzMap d a
```

**`QuantumMechanics.SpaceDHilbertSpace.PolyBddSchwartzSubmodule.of_zero_eq`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean#L158).

```lean
lemma of_zero_eq : PolyBddSchwartzSubmodule d 0 μ = SchwartzSubmodule d μ
```

**`QuantumMechanics.SpaceDHilbertSpace.PolyBddSchwartzSubmodule.le_SchwartzSubmodule`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean#L161).

```lean
lemma le_SchwartzSubmodule (d : ℕ) (a : ℕ∞) : PolyBddSchwartzSubmodule d a ≤ SchwartzSubmodule d
```

**`QuantumMechanics.SpaceDHilbertSpace.PolyBddSchwartzSubmodule.antitone`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean#L164).

```lean
lemma antitone {a b : ℕ∞} (h : a ≤ b) :
    PolyBddSchwartzSubmodule d b μ ≤ PolyBddSchwartzSubmodule d a μ
```

### D. Density

**`QuantumMechanics.SpaceDHilbertSpace.PolyBddSchwartzSubmodule.dense_top`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean#L197).

```lean
lemma dense_top (hμ : μ ≤ volume) [μ.IsOpenPosMeasure] [IsFiniteMeasureOnCompacts μ] :
    Dense (PolyBddSchwartzSubmodule d ⊤ μ : Set (SpaceDHilbertSpace d μ))
```

**`QuantumMechanics.SpaceDHilbertSpace.PolyBddSchwartzSubmodule.dense`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean#L304).

```lean
lemma dense (hμ : μ ≤ volume) [μ.IsOpenPosMeasure] [IsFiniteMeasureOnCompacts μ] :
    Dense (PolyBddSchwartzSubmodule d a μ : Set (SpaceDHilbertSpace d μ))
```

## Depends on

- [Schwartz submodule](schwartzsubmodule.md)

## Sources

- [Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PolyBddSchwartzSubmodule.lean)
