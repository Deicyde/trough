---
declaration: module
origin: cited
lean: CPTPMap.choi_ext, CPTPMap.choi_PSD_of_CPTP, CPTPMap.Tr_of_choi_of_CPTP, CPTPMap.compose_eq, CPTPMap.compose_assoc, CPTPMap.id_map, CPTPMap.id_MState, CPTPMap.id_compose
statement: formalized
proof: formalized
---

# Completely Positive Trace Preserving maps

The module `QuantumInfo.Channels.CPTP`, [QuantumInfo/Channels/CPTP.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean): 63 declarations (2 instances with no name), 43 with a docstring, 18 listed as significant; 9 private, not shown.

> A `CPTPMap` is a `ℂ`-linear map between matrices (`MatrixMap` is an alias), bundled with the facts
> that it `IsCompletelyPositive` and `IsTracePreserving`. CPTP maps are typically regarded as the
> "most general quantum operation", as they map density matrices (`MState`s) to density matrices. The
> type `PTPMap`, for maps that are positive (but not necessarily completely positive) is also
> declared.
>
> A large portion of the theory is in terms of the Choi matrix (`MatrixMap.choi_matrix`), as the
> positive-definiteness of this matrix corresponds to being a CP map. This is
> [Choi's theorem on CP maps](https://en.wikipedia.org/wiki/Choi%27s_theorem_on_completely_positive_maps).
>
> This file also defines several important examples of, classes of, and operations on, CPTPMaps:
>  * `compose`: Composition of maps
>  * `id`: The identity map
>  * `replacement`: The replacement channel that always outputs the same state
>  * `prod`: Tensor product of two CPTP maps, with notation M₁ ⊗ M₂
>  * `piProd`: Tensor product of finitely many CPTP maps (Pi-type product)
>  * `of_unitary`: The CPTP map corresponding to a unitary operation `U`
>  * `IsUnitary`: Predicate whether the map corresponds to any unitary
>  * `purify`: Purifying a channel into a unitary on a larger Hilbert space
>  * `complementary`: The complementary channel to its purification
>  * `IsEntanglementBreaking`, `IsDegradable`, `IsAntidegradable`: Entanglement breaking, degradable
>     and antidegradable channels.
>  * `SWAP`, `assoc`, `assoc'`, `traceLeft`, `traceRight`: The CPTP maps corresponding to important
>     operations on states. These correspond directly to `MState.SWAP`, `MState.assoc`,
>     `MState.assoc'`, `MState.traceLeft`, and `MState.traceRight`.

**`CPTPMap.choi`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L56).

> The Choi matrix of a CPTPMap.

```lean
def choi
```

**`CPTPMap.choi_ext`**, a theorem, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L59). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Two CPTPMaps are equal if their Choi matrices are equal.

```lean
theorem choi_ext {Λ₁ Λ₂ : CPTPMap dIn dOut} (h : Λ₁.choi = Λ₂.choi) : Λ₁ = Λ₂
```

**`CPTPMap.choi_PSD_of_CPTP`**, a theorem, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L64). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Choi matrix of a channel is PSD.

```lean
theorem choi_PSD_of_CPTP : Λ.map.choi_matrix.PosSemidef
```

**`CPTPMap.Tr_of_choi_of_CPTP`**, a theorem, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L69). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace of a Choi matrix of a CPTP map is the cardinality of the input space.

```lean
theorem Tr_of_choi_of_CPTP : Λ.choi.trace =
    (Finset.univ (α := dIn)).card
```

**`CPTPMap.CPTP_of_choi_PSD_Tr`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L74).

> Construct a CPTP map from a PSD Choi matrix with correct partial trace.

```lean
def CPTP_of_choi_PSD_Tr {M : Matrix (dOut × dIn) (dOut × dIn) ℂ} (h₁ : M.PosSemidef)
    (h₂ : M.traceLeft = 1) : CPTPMap dIn dOut
```

**`CPTPMap.choi_of_CPTP_of_choi`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L83).

```lean
lemma choi_of_CPTP_of_choi (M : Matrix (dOut × dIn) (dOut × dIn) ℂ) {h₁} {h₂} :
    (CPTP_of_choi_PSD_Tr (M := M) h₁ h₂).choi = M
```

**`CPTPMap.mat_coe_eq_apply_mat`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L88).

```lean
lemma mat_coe_eq_apply_mat [DecidableEq dOut] (ρ : MState dIn) : (Λ ρ).m = Λ.map ρ.m
```

**`CPTPMap.funext`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L92).

```lean
lemma funext [DecidableEq dOut] {Λ₁ Λ₂ : CPTPMap dIn dOut} (h : ∀ ρ, Λ₁ ρ = Λ₂ ρ) : Λ₁ = Λ₂
```

**`CPTPMap.compose`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L96).

> The composition of CPTPMaps, as a CPTPMap.

```lean
def compose (Λ₂ : CPTPMap dM dOut) (Λ₁ : CPTPMap dIn dM) : CPTPMap dIn dOut
```

**`CPTPMap.compose_eq`**, a theorem, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L105). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Composition of CPTPMaps by `CPTPMap.compose` is compatible with the `instFunLike` action.

```lean
theorem compose_eq [DecidableEq dOut] {Λ₁ : CPTPMap dIn dM} {Λ₂ : CPTPMap dM dOut} : ∀ρ, (Λ₂ ∘ₘ Λ₁) ρ = Λ₂ (Λ₁ ρ)
```

**`CPTPMap.compose_assoc`**, a theorem, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L109). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Composition of CPTPMaps is associative.

```lean
theorem compose_assoc [DecidableEq dOut] (Λ₃ : CPTPMap dM₂ dOut) (Λ₂ : CPTPMap dM dM₂)
    (Λ₁ : CPTPMap dIn dM) : (Λ₃ ∘ₘ Λ₂) ∘ₘ Λ₁ = Λ₃ ∘ₘ (Λ₂ ∘ₘ Λ₁)
```

**`CPTPMap.instMixable`**, an instance, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L115).

> CPTPMaps have a convex structure from their Choi matrices.

```lean
instance instMixable : Mixable (Matrix (dOut × dIn) (dOut × dIn) ℂ) (CPTPMap dIn dOut)
```

**`CPTPMap.id`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L150).

> The identity channel, which leaves the input unchanged.

```lean
def id : CPTPMap dIn dIn
```

**`CPTPMap.id_map`**, a theorem, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L157). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The map `CPTPMap.id` leaves any matrix unchanged.

```lean
theorem id_map : (id (dIn := dIn)).map = LinearMap.id
```

**`CPTPMap.id_MState`**, a theorem, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L162). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The map `CPTPMap.id` leaves the input state unchanged.

```lean
theorem id_MState (ρ : MState dIn) : CPTPMap.id (dIn := dIn) ρ = ρ
```

**`CPTPMap.id_compose`**, a theorem, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L169). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The map `CPTPMap.id` composed with any map is the same map.

```lean
theorem id_compose [DecidableEq dOut] (Λ : CPTPMap dIn dOut) : id ∘ₘ Λ = Λ
```

**`CPTPMap.compose_id`**, a theorem, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L175). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Any map composed with `CPTPMap.id` is the same map.

```lean
theorem compose_id (Λ : CPTPMap dIn dOut) : Λ ∘ₘ id = Λ
```

**`CPTPMap.ofEquiv`**, a def, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L186).

> Given a equivalence (a bijection) between the types d₁ and d₂, that is, if they're
> the same dimension, then there's a CPTP channel for this. This is what we need for
> defining e.g. the SWAP channel, which is 'unitary' but takes heterogeneous input
> and outputs types (d₁ × d₂) and (d₂ × d₁).

```lean
def ofEquiv (σ : dIn ≃ dOut) : CPTPMap dIn dOut
```

**`CPTPMap.ofEquiv_apply`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L192).

```lean
lemma ofEquiv_apply (σ : dIn ≃ dOut) (ρ : MState dIn) :
    ofEquiv σ ρ = ρ.relabel σ.symm
```

**`CPTPMap.equiv_inverse`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L197).

```lean
lemma equiv_inverse (σ : dIn ≃ dOut)  : (ofEquiv σ) ∘ (ofEquiv σ.symm) = id (dIn := dOut)
```

**`CPTPMap.SWAP`**, a def, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L207).

> The SWAP operation, as a channel.

```lean
def SWAP : CPTPMap (d₁ × d₂) (d₂ × d₁)
```

**`CPTPMap.assoc`**, a def, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L211).

> The associator, as a channel.

```lean
def assoc : CPTPMap ((d₁ × d₂) × d₃) (d₁ × d₂ × d₃)
```

**`CPTPMap.assoc'`**, a def, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L215).

> The inverse associator, as a channel.

```lean
def assoc' : CPTPMap (d₁ × d₂ × d₃) ((d₁ × d₂) × d₃)
```

**`CPTPMap.SWAP_eq_MState_SWAP`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L219).

```lean
lemma SWAP_eq_MState_SWAP (ρ : MState (d₁ × d₂)) : SWAP (d₁ := d₁) (d₂ := d₂) ρ = ρ.SWAP
```

**`CPTPMap.assoc_eq_MState_assoc`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L223).

```lean
lemma assoc_eq_MState_assoc (ρ : MState ((d₁ × d₂) × d₃)) : assoc (d₁ := d₁) (d₂ := d₂) (d₃ := d₃) ρ = ρ.assoc
```

**`CPTPMap.assoc'_eq_MState_assoc'`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L227).

```lean
lemma assoc'_eq_MState_assoc' (ρ : MState (d₁ × d₂ × d₃)) : assoc' (d₁ := d₁) (d₂ := d₂) (d₃ := d₃) ρ = ρ.assoc'
```

**`CPTPMap.assoc_assoc'`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L231).

```lean
lemma assoc_assoc' : (assoc (d₁ := d₁) (d₂ := d₂) (d₃ := d₃)) ∘ₘ assoc' = id
```

**`CPTPMap.traceLeft`**, a def, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L242).

> Partial tracing out the left, as a CPTP map.

```lean
def traceLeft : CPTPMap (d₁ × d₂) d₂
```

**`CPTPMap.traceRight`**, a def, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L275).

> Partial tracing out the right, as a CPTP map.

```lean
def traceRight : CPTPMap (d₁ × d₂) d₁
```

**`CPTPMap.traceLeft_eq_MState_traceLeft`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L279).

```lean
lemma traceLeft_eq_MState_traceLeft (ρ : MState (d₁ × d₂)) :
    traceLeft (d₁ := d₁) (d₂ := d₂) ρ = ρ.traceLeft
```

**`CPTPMap.traceRight_eq_MState_traceRight`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L284).

```lean
lemma traceRight_eq_MState_traceRight (ρ : MState (d₁ × d₂)) :
    traceRight (d₁ := d₁) (d₂ := d₂) ρ = ρ.traceRight
```

**`CPTPMap.replacement`**, a def, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L291).

> The replacement channel that maps all inputs to a given state.

```lean
def replacement [Nonempty dIn] [DecidableEq dOut] (ρ : MState dOut) : CPTPMap dIn dOut
```

**`CPTPMap.replacement_apply`**, a theorem, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L303). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The output of `replacement ρ` is always that `ρ`.

```lean
theorem replacement_apply [Nonempty dIn] [DecidableEq dOut] (ρ : MState dOut) (ρ₀ : MState dIn) :
    replacement ρ ρ₀ = ρ
```

**An instance with no name**, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L318).

```lean
instance [Nonempty dIn] [Nonempty dOut] [DecidableEq dOut] : Inhabited (CPTPMap dIn dOut)
```

**An instance with no name**, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L321).

```lean
instance [Nonempty dIn] [Nonempty dOut] : Nonempty (CPTPMap dIn dOut)
```

**`CPTPMap.destroy`**, a def, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L327).

> There is a CPTP map that takes a system of any (nonzero) dimension and outputs the
> trivial Hilbert space, 1-dimensional, indexed by any `Unique` type. We can think of this
> as "destroying" the whole system; tracing out everything.

```lean
def destroy [Nonempty dIn] [Unique dOut] : CPTPMap dIn dOut
```

**`CPTPMap.eq_if_output_unique`**, a theorem, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L331). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Two CPTP maps into the same one-dimensional output space must be equal

```lean
theorem eq_if_output_unique [Unique dOut] (Λ₁ Λ₂ : CPTPMap dIn dOut) : Λ₁ = Λ₂
```

**`CPTPMap.instUnique`**, an instance, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L335).

> There is exactly one CPTPMap to a 1-dimensional space.

```lean
instance instUnique [Nonempty dIn] [Unique dOut] : Unique (CPTPMap dIn dOut)
```

**`CPTPMap.destroy_comp`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L340).

```lean
lemma destroy_comp {dOut₂ : Type*} [Unique dOut₂] [DecidableEq dOut] [Nonempty dIn] [Nonempty dOut]
  (Λ : CPTPMap dIn dOut) :
    destroy (dOut := dOut₂) ∘ₘ Λ = destroy
```

**`CPTPMap.prod`**, a def, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L353).

> The tensor product of two CPTPMaps.

```lean
def prod (Λ₁ : CPTPMap dI₁ dO₁) (Λ₂ : CPTPMap dI₂ dO₂) : CPTPMap (dI₁ × dI₂) (dO₁ × dO₂)
```

**`CPTPMap.prod_apply_prod`**, a theorem, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L363). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Tensor products commute with channel application:
> `(Λ₁ ⊗ᶜᵖ Λ₂) (ρ₁ ⊗ᴹ ρ₂) = Λ₁ ρ₁ ⊗ᴹ Λ₂ ρ₂`.

```lean
theorem prod_apply_prod (Λ₁ : CPTPMap dI₁ dO₁) (Λ₂ : CPTPMap dI₂ dO₂)
    (ρ₁ : MState dI₁) (ρ₂ : MState dI₂) :
    (Λ₁ ⊗ᶜᵖ Λ₂) (ρ₁ ⊗ᴹ ρ₂) = (Λ₁ ρ₁) ⊗ᴹ (Λ₂ ρ₂)
```

**`CPTPMap.piProd`**, a def, [line 380](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L380).

> Finitely-indexed tensor products of CPTPMaps.

```lean
def piProd (Λi : (i:ι) → CPTPMap (dI i) (dO i)) : CPTPMap ((i:ι) → dI i) ((i:ι) → dO i)
```

**`CPTPMap.fin_1_piProd`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L386).

```lean
lemma fin_1_piProd
  {dI : Fin 1 → Type v} [Fintype (dI 0)] [DecidableEq (dI 0)]
  {dO : Fin 1 → Type w} [Fintype (dO 0)] [DecidableEq (dO 0)]
  (Λi : (i : Fin 1) → CPTPMap (dI 0) (dO 0)) :
    piProd Λi =
      ofEquiv (Equiv.funUnique (Fin 1) (dO 0)).symm ∘ₘ
        ((Λi 1) ∘ₘ ofEquiv (Equiv.funUnique (Fin 1) (dI 0)))
```

**`CPTPMap.piProd_comp`**, a theorem, [line 412](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L412). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The tensor product of composed maps is the composition of the tensor products.

```lean
theorem piProd_comp
  {d₁ d₂ d₃ : ι → Type*}
  [∀ i, Fintype (d₁ i)] [∀ i, DecidableEq (d₁ i)]
  [∀ i, Fintype (d₂ i)] [∀ i, DecidableEq (d₂ i)]
  [∀ i, Fintype (d₃ i)] [∀ i, DecidableEq (d₃ i)]
  (Λ₁ : ∀ i, CPTPMap (d₁ i) (d₂ i)) (Λ₂ : ∀ i, CPTPMap (d₂ i) (d₃ i)) :
  piProd (fun i => (Λ₂ i) ∘ₘ (Λ₁ i)) = (piProd Λ₂) ∘ₘ (piProd Λ₁)
```

**`CPTPMap.piProd_id`**, a lemma, [line 424](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L424).

```lean
lemma piProd_id :
    piProd (fun i ↦ (CPTPMap.id : CPTPMap (dI i) (dI i))) = CPTPMap.id
```

**`CPTPMap.ofUnitary`**, a def, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L434).

> Conjugating density matrices by a unitary as a channel. This is standard unitary evolution.

```lean
def ofUnitary (U : 𝐔[dIn]) : CPTPMap dIn dIn
```

**`CPTPMap.ofUnitary_eq_conj`**, a theorem, [line 440](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L440). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The unitary channel U conjugated by U.

```lean
theorem ofUnitary_eq_conj (U : 𝐔[dIn]) (ρ : MState dIn) :
    (ofUnitary U) ρ = ρ.uConj U
```

**`CPTPMap.IsUnitary`**, a def, [line 445](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L445).

> A channel is unitary iff it is `ofUnitary U`.

```lean
def IsUnitary (Λ : CPTPMap dIn dIn) : Prop
```

**`CPTPMap.IsUnitary_iff_uConj`**, a theorem, [line 449](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L449). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A channel is unitary iff it can be written as conjugation by a unitary.

```lean
theorem IsUnitary_iff_uConj (Λ : CPTPMap dIn dIn) : IsUnitary Λ ↔ ∃ U, ∀ ρ, Λ ρ = ρ.uConj U
```

**`CPTPMap.IsUnitary_equiv`**, a lemma, [line 453](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L453).

```lean
lemma IsUnitary_equiv (σ : dIn ≃ dIn) : IsUnitary (ofEquiv σ)
```

**`CPTPMap.exists_purify`**, a lemma, [line 710](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L710).

```lean
lemma exists_purify (Λ : CPTPMap dIn dOut) :
    ∃ (Λ' : CPTPMap (dIn × dOut × dOut) (dIn × dOut × dOut)),
      Λ'.IsUnitary ∧
      Λ = (
      let zero_prep : CPTPMap Unit (dOut × dOut) := replacement (MState.pure (Ket.basis default))
      let prep := (id ⊗ᶜᵖ zero_prep)
      let append : CPTPMap dIn (dIn × Unit) := CPTPMap.ofEquiv (Equiv.prodPUnit dIn).symm
      CPTPMap.traceLeft ∘ₘ CPTPMap.traceLeft ∘ₘ Λ' ∘ₘ prep ∘ₘ append
    )
```

**`CPTPMap.purify`**, a def, [line 750](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L750).

> Every channel can be written as a unitary channel on a larger system. In general, if
> the original channel was A→B, we may need to go as big as dilating the output system (the
> environment) by a factor of A*B. One way of stating this would be that it forms an
> isometry from A to (B×A×B). So that we can instead talk about the cleaner unitaries, we
> say that this is a unitary on (A×B×B). The defining properties that this is a valid
> purification comes are `purify_IsUnitary` and `purify_trace`. This means the environment
> always has type `dIn × dOut`.
>
> Furthermore, since we need a canonical "0" state on B in order to add with the input,
> we require a typeclass instance [Inhabited dOut].

```lean
def purify (Λ : CPTPMap dIn dOut) : CPTPMap (dIn × dOut × dOut) (dIn × dOut × dOut)
```

**`CPTPMap.purify_IsUnitary`**, a lemma, [line 753](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L753).

```lean
lemma purify_IsUnitary (Λ : CPTPMap dIn dOut) : Λ.purify.IsUnitary
```

**`CPTPMap.purify_trace`**, a theorem, [line 763](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L763). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> With a channel Λ : A → B, a valid purification (A×B×B)→(A×B×B) is such that:
>  * Preparing the default ∣0⟩ state on two copies of B
>  * Appending these to the input
>  * Applying the purified unitary channel
>  * Tracing out the two left parts of the output
> is equivalent to the original channel. This theorem states that the channel output by `purify`
> has this property.

```lean
theorem purify_trace (Λ : CPTPMap dIn dOut) : Λ = (
    let zero_prep : CPTPMap Unit (dOut × dOut) := replacement (MState.pure (Ket.basis default))
    let prep := (id ⊗ᶜᵖ zero_prep)
    let append : CPTPMap dIn (dIn × Unit) := CPTPMap.ofEquiv (Equiv.prodPUnit dIn).symm
    CPTPMap.traceLeft ∘ₘ CPTPMap.traceLeft ∘ₘ Λ.purify ∘ₘ prep ∘ₘ append
  )
```

**`CPTPMap.prep_append_map_entry`**, a theorem, [line 778](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L778). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Stinespring preparation `prep ∘ append` acts on a matrix entry by the Kronecker product
> with the fixed pure state `|default⟩⟨default|` on `dOut × dOut`.

```lean
theorem prep_append_map_entry (X : Matrix dIn dIn ℂ)
    (a₁ : dIn) (b₁c₁ : dOut × dOut) (a₂ : dIn) (b₂c₂ : dOut × dOut) :
    let τ := MState.pure (Ket.basis (default : dOut × dOut))
    let zero_prep : CPTPMap Unit (dOut × dOut) := replacement τ
    let prep := (id ⊗ᶜᵖ zero_prep)
    let append : CPTPMap dIn (dIn × Unit) := CPTPMap.ofEquiv (Equiv.prodPUnit dIn).symm
    (prep ∘ₘ append).map X (a₁, b₁c₁) (a₂, b₂c₂) =
    X a₁ a₂ * τ.m b₁c₁ b₂c₂
```

**`CPTPMap.complementary`**, a def, [line 789](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L789).

> The complementary channel comes from tracing out the other half (the right half) of the purified channel `purify`.

```lean
def complementary (Λ : CPTPMap dIn dOut) : CPTPMap dIn (dIn × dOut)
```

**`CPTPMap.IsDegradableTo`**, a def, [line 802](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L802).

> A channel is *degradable to* another, if the other can be written as a composition of
> a \_degrading\_ channel D with the original channel.

```lean
def IsDegradableTo (Λ : CPTPMap dIn dOut) (Λ₂ : CPTPMap dIn dOut₂) : Prop
```

**`CPTPMap.IsAntidegradableTo`**, a def, [line 807](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L807).

> A channel is *antidegradable to* another, if the other `IsDegradableTo` this one.

```lean
def IsAntidegradableTo (Λ : CPTPMap dIn dOut) (Λ₂ : CPTPMap dIn dOut₂) : Prop
```

**`CPTPMap.IsDegradable`**, a def, [line 811](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L811).

> A channel is *degradable* if it `IsDegradableTo` its complementary channel.

```lean
def IsDegradable (Λ : CPTPMap dIn dOut) : Prop
```

**`CPTPMap.IsAntidegradable`**, a def, [line 816](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L816).

> A channel is *antidegradable* if it `IsAntidegradableTo` its complementary channel.

```lean
def IsAntidegradable (Λ : CPTPMap dIn dOut) : Prop
```

**`CPTPMap.instTop`**, an instance, [line 823](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L823).

> `CPTPMap`s inherit a topology from their choi matrices.

```lean
instance instTop : TopologicalSpace (CPTPMap dIn dOut)
```

**`CPTPMap.choi_IsEmbedding`**, a theorem, [line 827](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L827). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The projection from `CPTPMap` to the Choi matrix is an embedding

```lean
theorem choi_IsEmbedding : Topology.IsEmbedding (CPTPMap.choi (dIn := dIn) (dOut := dOut))
```

**`CPTPMap.instT3Space`**, an instance, [line 831](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean#L831).

```lean
instance instT3Space : T3Space (CPTPMap dIn dOut)
```

## Depends on

- [Classes of Matrix Maps](bundled.md)
- [Unitary operators on quantum state](../operators/unitary.md)

## Sources

- [QuantumInfo/Channels/CPTP.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/CPTP.lean)
