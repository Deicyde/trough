---
declaration: module
origin: cited
lean: QuantumMechanics.OneDimension.HilbertSpace, QuantumMechanics.OneDimension.HilbertSpace.toBra, QuantumMechanics.OneDimension.HilbertSpace.toBra_apply, QuantumMechanics.OneDimension.HilbertSpace.toBra_surjective, QuantumMechanics.OneDimension.HilbertSpace.toBra_injective, QuantumMechanics.OneDimension.HilbertSpace.MemHS, QuantumMechanics.OneDimension.HilbertSpace.aeStronglyMeasurable_of_memHS, QuantumMechanics.OneDimension.HilbertSpace.memHS_iff
statement: formalized
proof: formalized
---

# Hilbert space for one dimension quantum mechanics

The module `Physlib.QuantumMechanics.HilbertSpaces.OneDimension.Basic`, [Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean): 25 declarations, 7 with a docstring.

**`QuantumMechanics.OneDimension.HilbertSpace`**, an abbrev, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L31).

> The Hilbert space for a one dimensional quantum system is defined as
> the space of almost-everywhere equal equivalence classes of square integrable functions
> from `ℝ` to `ℂ`.

```lean
abbrev HilbertSpace
```

**`QuantumMechanics.OneDimension.HilbertSpace.toBra`**, a def, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L38).

> The anti-linear map from the Hilbert space to it's dual.

```lean
def toBra : HilbertSpace →ₛₗ[starRingEnd ℂ] StrongDual ℂ HilbertSpace
```

**`QuantumMechanics.OneDimension.HilbertSpace.toBra_apply`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L41).

```lean
lemma toBra_apply (f g : HilbertSpace) : toBra f g = ⟪f, g⟫_ℂ
```

**`QuantumMechanics.OneDimension.HilbertSpace.toBra_surjective`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L45).

> The anti-linear map, `toBra`, taking a ket to it's corresponding
> bra is surjective.

```lean
lemma toBra_surjective : Function.Surjective toBra
```

**`QuantumMechanics.OneDimension.HilbertSpace.toBra_injective`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L50).

> The anti-linear map, `toBra`, taking a ket to it's corresponding
> bra is injective.

```lean
lemma toBra_injective : Function.Injective toBra
```

## Member of the Hilbert space as a property

**`QuantumMechanics.OneDimension.HilbertSpace.MemHS`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L62).

> The proposition `MemHS f` for a function `f : ℝ → ℂ` is defined
> to be true if the function `f` can be lifted to the Hilbert space.

```lean
def MemHS (f : ℝ → ℂ) : Prop
```

**`QuantumMechanics.OneDimension.HilbertSpace.aeStronglyMeasurable_of_memHS`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L64).

```lean
lemma aeStronglyMeasurable_of_memHS {f : ℝ → ℂ} (h : MemHS f) : AEStronglyMeasurable f
```

**`QuantumMechanics.OneDimension.HilbertSpace.memHS_iff`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L69).

> A function `f` satisfies `MemHS f` if and only if it is almost everywhere
> strongly measurable, and square integrable.

```lean
lemma memHS_iff {f : ℝ → ℂ} : MemHS f ↔
    AEStronglyMeasurable f ∧ Integrable (fun x => ‖f x‖ ^ 2)
```

**`QuantumMechanics.OneDimension.HilbertSpace.zero_memHS`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L77).

```lean
lemma zero_memHS : MemHS 0
```

**`QuantumMechanics.OneDimension.HilbertSpace.zero_fun_memHS`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L85).

```lean
lemma zero_fun_memHS : MemHS (fun _ : ℝ => (0 : ℂ))
```

**`QuantumMechanics.OneDimension.HilbertSpace.memHS_add`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L87).

```lean
lemma memHS_add {f g : ℝ → ℂ} (hf : MemHS f) (hg : MemHS g) :
    MemHS (f + g)
```

**`QuantumMechanics.OneDimension.HilbertSpace.memHS_smul`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L90).

```lean
lemma memHS_smul {f : ℝ → ℂ} {c : ℂ} (hf : MemHS f) :
    MemHS (c • f)
```

**`QuantumMechanics.OneDimension.HilbertSpace.memHS_of_ae`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L93).

```lean
lemma memHS_of_ae {g : ℝ → ℂ} (f : ℝ → ℂ) (hf : MemHS f) (hfg : f =ᵐ[MeasureTheory.volume] g) :
    MemHS g
```

## Construction of elements of the Hilbert space

**`QuantumMechanics.OneDimension.HilbertSpace.aeEqFun_mk_mem_iff`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L102).

```lean
lemma aeEqFun_mk_mem_iff (f : ℝ → ℂ) (hf : AEStronglyMeasurable f volume) :
    AEEqFun.mk f hf ∈ HilbertSpace ↔ MemHS f
```

**`QuantumMechanics.OneDimension.HilbertSpace.mk`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L109).

> Given a function `f : ℝ → ℂ` such that `MemHS f` is true via `hf`, then `HilbertSpace.mk hf`
> is the element of the `HilbertSpace` defined by `f`.

```lean
def mk {f : ℝ → ℂ} (hf : MemHS f) : HilbertSpace
```

**`QuantumMechanics.OneDimension.HilbertSpace.coe_hilbertSpace_memHS`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L113).

```lean
lemma coe_hilbertSpace_memHS (f : HilbertSpace) : MemHS (f : ℝ → ℂ)
```

**`QuantumMechanics.OneDimension.HilbertSpace.mk_surjective`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L118).

```lean
lemma mk_surjective (f : HilbertSpace) : ∃ (g : ℝ → ℂ), ∃ (hg : MemHS g), mk hg = f
```

**`QuantumMechanics.OneDimension.HilbertSpace.coe_mk_ae`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L122).

```lean
lemma coe_mk_ae {f : ℝ → ℂ} (hf : MemHS f) : (mk hf : ℝ → ℂ) =ᵐ[MeasureTheory.volume] f
```

**`QuantumMechanics.OneDimension.HilbertSpace.inner_mk_mk`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L125).

```lean
lemma inner_mk_mk {f g : ℝ → ℂ} {hf : MemHS f} {hg : MemHS g} :
    inner ℂ (mk hf) (mk hg) = ∫ x : ℝ, starRingEnd ℂ (f x) * g x
```

**`QuantumMechanics.OneDimension.HilbertSpace.eLpNorm_mk`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L132).

```lean
lemma eLpNorm_mk {f : ℝ → ℂ} {hf : MemHS f} : eLpNorm (mk hf) 2 volume = eLpNorm f 2 volume
```

**`QuantumMechanics.OneDimension.HilbertSpace.mem_iff'`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L135).

```lean
lemma mem_iff' {f : ℝ → ℂ} (hf : MeasureTheory.AEStronglyMeasurable f MeasureTheory.volume) :
    MeasureTheory.AEEqFun.mk f hf ∈ HilbertSpace
    ↔ MeasureTheory.Integrable (fun x => ‖f x‖ ^ 2)
```

**`QuantumMechanics.OneDimension.HilbertSpace.mk_add`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L140).

```lean
lemma mk_add {f g : ℝ → ℂ} {hf : MemHS f} {hg : MemHS g} :
    mk (memHS_add hf hg) = mk hf + mk hg
```

**`QuantumMechanics.OneDimension.HilbertSpace.mk_smul`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L143).

```lean
lemma mk_smul {f : ℝ → ℂ} {c : ℂ} {hf : MemHS f} :
    mk (memHS_smul (c := c) hf) = c • mk hf
```

**`QuantumMechanics.OneDimension.HilbertSpace.mk_eq_iff`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L146).

```lean
lemma mk_eq_iff {f g : ℝ → ℂ} {hf : MemHS f} {hg : MemHS g} :
    mk hf = mk hg ↔ f =ᵐ[volume] g
```

**`QuantumMechanics.OneDimension.HilbertSpace.ext_iff`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean#L150).

```lean
lemma ext_iff {f g : HilbertSpace} :
    f = g ↔ (f : ℝ → ℂ) =ᶠ[ae volume] (g : ℝ → ℂ)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Basic.lean)
