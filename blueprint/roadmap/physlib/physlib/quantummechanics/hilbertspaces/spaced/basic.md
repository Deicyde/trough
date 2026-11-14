---
declaration: module
origin: cited
lean: QuantumMechanics.SpaceDHilbertSpace, QuantumMechanics.SpaceDHilbertSpace.ext_iff, QuantumMechanics.SpaceDHilbertSpace.toBra, QuantumMechanics.SpaceDHilbertSpace.toBra_apply_apply, QuantumMechanics.SpaceDHilbertSpace.toBra_symm_apply, QuantumMechanics.SpaceDHilbertSpace.MemHS, QuantumMechanics.SpaceDHilbertSpace.memHS_coe, QuantumMechanics.SpaceDHilbertSpace.memHS_iff
statement: formalized
proof: formalized
---

# Hilbert spaces for quantum mechanics on `Space d`

The module `Physlib.QuantumMechanics.HilbertSpaces.SpaceD.Basic`, [Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean): 52 declarations, 13 with a docstring.

## i. Overview

> The Hilbert spaces appropriate for doing quantum mechanics on `Space d` are the $L^2$-spaces
> `SpaceDHilbertSpace d μ := Lp ℂ 2 μ`, where `μ` is some measure on `Space d`.
> Elements of `SpaceDHilbertSpace d μ` are \_equivalence classes\_ of functions `Space d → ℂ` which are
> square-integrable with respect to `μ`, i.e. `∫ x, ‖f x‖ ^ 2 ∂μ` is finite, and where `f` and `g` are
> in the same equivalence class if they are `μ`-a.e. equal.
>
> The ability of a function to be interpreted as an element of `SpaceDHilbertSpace d μ` is captured
> by the property `MemHS`. If one has `hf : MemHS f μ` for a function `f : Space d → ℂ` this means
> that `f` is `μ`-a.e. strongly measurable and square-integrable; `mk hf` constructs the corresponding
> equivalence class of `f` in `SpaceDHilbertSpace d μ`.
>
> Given `SpaceDHilbertSpace d μ` and `Ω : Set (Space d)`, the Hilbert space
> `SpaceDHilbertSpaceOn Ω μ ≔ SpaceDHilbertSpace d (μ.restrict Ω)` may be interpreted as the
> sub-Hilbert space consisting of those vectors with domain contained in `Ω`.
> The reason is that for each `ψ` in `SpaceDHilbertSpaceOn Ω μ` we have
> `ψ =ᵐ[μ.restrict Ω] Ω.indicator ψ`, namely the equivalence class of `ψ` always
> contains a representative which vanishes on the complement of `Ω`.
> The linear isometry `restrictIncl Ω μ` describes this sub-Hilbert space relationship
> by mapping each `ψ` to this special representative in its equivalence class.
> Similarly, we may project `SpaceDHilbertSpace d μ` onto `SpaceDHilbertSpaceOn Ω μ` by enlarging the
> equivalence classes, essentially dropping information about the functions on the complement of `Ω`.

## ii. Key results

> - `SpaceDHilbertSpace d μ` : The $L^2$-space on `Space d` with respect to the measure `μ`.
> - `toBra` : The linear equivalence between the Hilbert space and its dual. This is the map which
>     sends each ket to its corresponding bra and \_vice versa\_.
> - `MemHS f μ` : The proposition capturing exactly when a function `f : Space d → ℂ` can be lifted
>     to an element of the Hilbert space.
> - `SpaceDHilbertSpaceOn Ω μ` : An abbreviation for the Hilbert space
>     `SpaceDHilbertSpace d (μ.restrict Ω)` appropriate for describing the $L^2$-space of complex
>     functions on a subset of `Space d`.
> - `subspaceProjection` : The continuous linear projection of `SpaceDHilbertSpace d μ` onto
>     `SpaceDHilbertSpaceOn Ω μ`.
> - `subspaceIncl` : The linear isometry including `SpaceDHilbertSpaceOn Ω μ`
>     as a sub-Hilbert space of `SpaceDHilbertspace d μ`.

## iv. References

> * None.

## A. SpaceDHilbertSpace

**`QuantumMechanics.SpaceDHilbertSpace`**, an abbrev, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L84).

> The L²-space of `μ`-a.e. equal equivalence classes of functions `f : Space d → ℂ`
> for which `∫ x, ‖f x‖² ∂μ` is finite.

```lean
abbrev SpaceDHilbertSpace (d : ℕ) (μ : Measure (Space d) := volume)
```

**`QuantumMechanics.SpaceDHilbertSpace.ext_iff`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L93).

> Elements of `SpaceDHilbertSpace d μ` are equivalence classes
> of `μ`-a.e. equal functions `Space d → ℂ`.

```lean
lemma ext_iff : ψ = φ ↔ ψ =ᵐ[μ] φ
```

### A.1. Dual space

**`QuantumMechanics.SpaceDHilbertSpace.toBra`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L102).

> The anti-linear equivalence between `SpaceDHilbertSpace d μ` and its dual.
>
> This is the map that takes a ket to its corresponding bra and \_vice versa\_.

```lean
def toBra : SpaceDHilbertSpace d μ ≃ₛₗ[starRingEnd ℂ] StrongDual ℂ (SpaceDHilbertSpace d μ)
```

**`QuantumMechanics.SpaceDHilbertSpace.toBra_apply_apply`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L106).

```lean
lemma toBra_apply_apply : toBra ψ φ = ⟪ψ, φ⟫_ℂ
```

**`QuantumMechanics.SpaceDHilbertSpace.toBra_symm_apply`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L109).

```lean
lemma toBra_symm_apply (f : StrongDual ℂ (SpaceDHilbertSpace d μ)) : ⟪toBra.symm f, ψ⟫_ℂ = f ψ
```

### A.2. Membership

**`QuantumMechanics.SpaceDHilbertSpace.MemHS`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L118).

> For a function `f : Space d → ℂ`, the proposition `MemHS f μ` means that the function `f`
> can be lifted to an element of the Hilbert space.

```lean
def MemHS (f : Space d → ℂ) (μ : Measure (Space d) := volume) : Prop
```

**`QuantumMechanics.SpaceDHilbertSpace.memHS_coe`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L121).

> Elements of the Hilbert space satisfy the property `MemHS`.

```lean
lemma memHS_coe : MemHS ψ μ
```

**`QuantumMechanics.SpaceDHilbertSpace.memHS_iff`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L125).

> A function `f : Space d → ℂ` satisfies `MemHS f μ` if and only if
> it is `μ`-a.e. strongly measurable and `∫ x, ‖f x‖ ^ 2 ∂μ` is finite.

```lean
lemma memHS_iff : MemHS f μ ↔ AEStronglyMeasurable f μ ∧ Integrable (fun x ↦ ‖f x‖ ^ 2) μ
```

**`QuantumMechanics.SpaceDHilbertSpace.mem_iff`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L130).

```lean
lemma mem_iff {f : Space d →ₘ[μ] ℂ} : f ∈ SpaceDHilbertSpace d μ ↔ MemHS f μ
```

**`QuantumMechanics.SpaceDHilbertSpace.MemHS.zero`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L133).

```lean
lemma MemHS.zero : MemHS (0 : Space d → ℂ) μ
```

**`QuantumMechanics.SpaceDHilbertSpace.MemHS.neg`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L135).

```lean
lemma MemHS.neg (hf : MemHS f μ) : MemHS (-f) μ
```

**`QuantumMechanics.SpaceDHilbertSpace.memHS_neg_iff`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L137).

```lean
lemma memHS_neg_iff : MemHS (-f) μ ↔ MemHS f μ
```

**`QuantumMechanics.SpaceDHilbertSpace.MemHS.add`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L139).

```lean
lemma MemHS.add (hf : MemHS f μ) (hg : MemHS g μ) : MemHS (f + g) μ
```

**`QuantumMechanics.SpaceDHilbertSpace.MemHS.sub`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L141).

```lean
lemma MemHS.sub (hf : MemHS f μ) (hg : MemHS g μ) : MemHS (f - g) μ
```

**`QuantumMechanics.SpaceDHilbertSpace.MemHS.const_smul`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L143).

```lean
lemma MemHS.const_smul (c : ℂ) (hf : MemHS f μ) : MemHS (c • f) μ
```

**`QuantumMechanics.SpaceDHilbertSpace.memHS_const_smul_iff`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L145).

```lean
lemma memHS_const_smul_iff {c : ℂ} (hc : c ≠ 0) : MemHS (c • f) μ ↔ MemHS f μ
```

**`QuantumMechanics.SpaceDHilbertSpace.MemHS.ae_eq`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L148).

```lean
lemma MemHS.ae_eq (hfg : f =ᵐ[μ] g) (hf : MemHS f μ) : MemHS g μ
```

**`QuantumMechanics.SpaceDHilbertSpace.memHS_congr_ae`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L150).

```lean
lemma memHS_congr_ae (hfg : f =ᵐ[μ] g) : MemHS f μ ↔ MemHS g μ
```

**`QuantumMechanics.SpaceDHilbertSpace.MemHS.congr_norm`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L152).

```lean
lemma MemHS.congr_norm
    (hf : MemHS f μ) (hg : AEStronglyMeasurable g μ) (hfg : ∀ᵐ x ∂μ, ‖f x‖ = ‖g x‖) : MemHS g μ
```

**`QuantumMechanics.SpaceDHilbertSpace.memHS_congr_norm`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L156).

```lean
lemma memHS_congr_norm (hf : AEStronglyMeasurable f μ) (hg : AEStronglyMeasurable g μ)
    (hfg : ∀ᵐ x ∂μ, ‖f x‖ = ‖g x‖) : MemHS f μ ↔ MemHS g μ
```

**`QuantumMechanics.SpaceDHilbertSpace.MemHS.mono`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L160).

```lean
lemma MemHS.mono (hf : MemHS f μ) (hg : AEStronglyMeasurable g μ) (hfg : ∀ᵐ x ∂μ, ‖g x‖ ≤ ‖f x‖) :
    MemHS g μ
```

**`QuantumMechanics.SpaceDHilbertSpace.MemHS.mono_measure`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L164).

```lean
lemma MemHS.mono_measure (h : μ' ≤ μ) (hf : MemHS f μ) : MemHS f μ'
```

**`QuantumMechanics.SpaceDHilbertSpace.MemHS.restrict`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L166).

```lean
lemma MemHS.restrict (Ω : Set (Space d)) (hf : MemHS f μ) : MemHS f (μ.restrict Ω)
```

**`QuantumMechanics.SpaceDHilbertSpace.MemHS.mono_restrict`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L169).

```lean
lemma MemHS.mono_restrict {Ω Ω' : Set (Space d)} (h : Ω' ≤ Ω) (hf : MemHS f (μ.restrict Ω)) :
    MemHS f (μ.restrict Ω')
```

**`QuantumMechanics.SpaceDHilbertSpace.MemHS.indicator`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L173).

```lean
lemma MemHS.indicator {Ω : Set (Space d)} (hΩ : MeasurableSet Ω) (hf : MemHS f μ) :
    MemHS (Ω.indicator f) μ
```

**`QuantumMechanics.SpaceDHilbertSpace.MemHS.indicator_of_restrict`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L179).

> If `f` is a member of the Hilbert space with measure restricted to `Ω` then the representative
> `Ω.indicator f` which vanishes outside `Ω` is a member of `SpaceDHilbertSpace d μ`.

```lean
lemma MemHS.indicator_of_restrict
    {Ω : Set (Space d)} (hΩ : MeasurableSet Ω) (hf : MemHS f (μ.restrict Ω)) :
    MemHS (Ω.indicator f) μ
```

### A.3. Construction of elements

**`QuantumMechanics.SpaceDHilbertSpace.mk`**, a def, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L197).

> Given a function `f : Space d → ℂ` such that `MemHS f μ` is true via `hf`,
> `mk hf` is the element of the Hilbert space defined by `f`.

```lean
def mk : SpaceDHilbertSpace d μ
```

**`QuantumMechanics.SpaceDHilbertSpace.mk_neg`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L202).

```lean
lemma mk_neg : mk hf.neg = -mk hf
```

**`QuantumMechanics.SpaceDHilbertSpace.mk_add`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L205).

```lean
lemma mk_add : mk (hf.add hg) = mk hf + mk hg
```

**`QuantumMechanics.SpaceDHilbertSpace.mk_sub`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L208).

```lean
lemma mk_sub : mk (hf.sub hg) = mk hf - mk hg
```

**`QuantumMechanics.SpaceDHilbertSpace.mk_const_smul`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L211).

```lean
lemma mk_const_smul (c : ℂ) : mk (hf.const_smul c) = c • mk hf
```

**`QuantumMechanics.SpaceDHilbertSpace.mk_eq_iff`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L213).

```lean
lemma mk_eq_iff : mk hf = mk hg ↔ f =ᵐ[μ] g
```

**`QuantumMechanics.SpaceDHilbertSpace.mk_surjective`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L215).

```lean
lemma mk_surjective : ∃ (f : Space d → ℂ) (hf : MemHS f μ), mk hf = ψ
```

**`QuantumMechanics.SpaceDHilbertSpace.coeFn_mk`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L218).

```lean
lemma coeFn_mk : mk hf =ᵐ[μ] f
```

**`QuantumMechanics.SpaceDHilbertSpace.inner_mk_mk`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L220).

```lean
lemma inner_mk_mk : ⟪mk hf, mk hg⟫_ℂ = ∫ x, starRingEnd ℂ (f x) * g x ∂μ
```

### A.4. Coersions

**`QuantumMechanics.SpaceDHilbertSpace.coeFn_zero`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L235).

```lean
lemma coeFn_zero : ⇑(0 : SpaceDHilbertSpace d μ) =ᵐ[μ] 0
```

**`QuantumMechanics.SpaceDHilbertSpace.coeFn_neg`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L237).

```lean
lemma coeFn_neg : ⇑(-ψ) =ᵐ[μ] -ψ
```

**`QuantumMechanics.SpaceDHilbertSpace.coeFn_add`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L239).

```lean
lemma coeFn_add : ⇑(ψ.val + φ.val) =ᵐ[μ] ψ + φ
```

**`QuantumMechanics.SpaceDHilbertSpace.coeFn_sub`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L241).

```lean
lemma coeFn_sub : ⇑(ψ.val - φ.val) =ᵐ[μ] ψ - φ
```

**`QuantumMechanics.SpaceDHilbertSpace.coeFn_smul`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L243).

```lean
lemma coeFn_smul : ⇑(c • ψ) =ᵐ[μ] c • ψ
```

### A.5. Misc.

**`QuantumMechanics.SpaceDHilbertSpace.toTemperedDistribution`**, an abbrev, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L252).

> The tempered distribution associated to a state.

```lean
abbrev toTemperedDistribution [μ.HasTemperateGrowth]
    (ψ : SpaceDHilbertSpace d μ) : 𝓢'(Space d, ℂ)
```

**`QuantumMechanics.SpaceDHilbertSpace.toTemperedDistributionCLM`**, an abbrev, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L256).

> The embedding of states into tempered distributions as a continuous linear map.

```lean
abbrev toTemperedDistributionCLM (d : ℕ) (μ : Measure (Space d) := volume)
    [μ.HasTemperateGrowth] : SpaceDHilbertSpace d μ →L[ℂ] 𝓢'(Space d, ℂ)
```

**`QuantumMechanics.SpaceDHilbertSpace.tendsto_zero_iff_tendsto_zero_lintegral_enorm_sq`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L261).

```lean
lemma tendsto_zero_iff_tendsto_zero_lintegral_enorm_sq
    {α : Type*} {l : Filter α} {ψ : α → SpaceDHilbertSpace d μ} :
    Tendsto ψ l (nhds 0) ↔ Tendsto (fun a ↦ ∫⁻ x, ‖ψ a x‖ₑ ^ 2 ∂μ) l (nhds 0)
```

## B. SpaceDHilbertSpaceOn

**`QuantumMechanics.SpaceDHilbertSpaceOn`**, an abbrev, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L283).

> The L²-space `SpaceDHilbertSpace d (μ.restrict Ω)`.
>
> Elements are equivalence classes of functions which agree `μ`-a.e. on `Ω` and which have
> `∫ x in Ω, ‖f x‖ ^ 2 ∂μ` finite.

```lean
abbrev SpaceDHilbertSpaceOn {d : ℕ} (Ω : Set (Space d)) (μ : Measure (Space d) := volume)
```

**`QuantumMechanics.SpaceDHilbertSpaceOn.subspaceProjection`**, a def, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L298).

> The continuous linear map projecting `SpaceDHilbertSpace d μ` onto `SpaceDHilbertSpaceOn Ω μ`.
>
> As a function it agrees with `Lp.LpToLpOfMeasureLeSMul` for `c = 1` (since `μ.restrict Ω ≤ μ`),
> the continuous `ℝ`-linear map of Mathlib from `Lp ℂ 2 μ` to `Lp ℂ 2 (μ.restrict Ω)`, from which
> its continuity is deduced.

```lean
def subspaceProjection : SpaceDHilbertSpace d μ →L[ℂ] SpaceDHilbertSpaceOn Ω μ
```

**`QuantumMechanics.SpaceDHilbertSpaceOn.subspaceProjection_apply`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L315).

```lean
lemma subspaceProjection_apply : subspaceProjection Ω μ ψ =ᵐ[μ.restrict Ω] ψ
```

**`QuantumMechanics.SpaceDHilbertSpaceOn.subspaceProjection_norm_le`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L318).

```lean
lemma subspaceProjection_norm_le : ‖subspaceProjection Ω μ ψ‖ ≤ ‖ψ‖
```

**`QuantumMechanics.SpaceDHilbertSpaceOn.subspaceIncl`**, a def, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L327).

> The linear isometry including `SpaceDHilbertSpaceOn Ω μ` as a sub-Hilbert space of
> `SpaceDHilbertSpace d μ`, defined by mapping `ψ` to `Ω.indicator ψ`.

```lean
def subspaceIncl : SpaceDHilbertSpaceOn Ω μ →ₗᵢ[ℂ] SpaceDHilbertSpace d μ
```

**`QuantumMechanics.SpaceDHilbertSpaceOn.subspaceIncl_apply`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L342).

```lean
lemma subspaceIncl_apply : subspaceIncl hΩ μ φ =ᵐ[μ] Ω.indicator φ
```

**`QuantumMechanics.SpaceDHilbertSpaceOn.leftInverse_subspaceProjection`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L345).

```lean
lemma leftInverse_subspaceProjection :
    LeftInverse (subspaceProjection Ω μ) (subspaceIncl hΩ μ)
```

**`QuantumMechanics.SpaceDHilbertSpaceOn.subspaceProjection_subspaceIncl_apply`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L355).

```lean
lemma subspaceProjection_subspaceIncl_apply : subspaceProjection Ω μ (subspaceIncl hΩ μ φ) = φ
```

**`QuantumMechanics.SpaceDHilbertSpaceOn.subspaceProjection_surjective`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean#L359).

```lean
lemma subspaceProjection_surjective : Surjective (subspaceProjection Ω μ)
```

## Depends on

- [The structure of a module on Space](../../../spaceandtime/space/part-01/module.md)

## Sources

- [Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/Basic.lean)
