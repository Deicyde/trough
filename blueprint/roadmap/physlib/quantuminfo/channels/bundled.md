---
declaration: module
origin: cited
lean: HPMap.funext_hermitian, HPMap.funext_pos, HPMap.funext_pos_trace, HPMap.funext_mstate, PMap.pos_Hermitian, PTPMap.pos_Hermitian, CPTPMap.ext, PUMap.pos_Hermitian
statement: formalized
proof: formalized
---

# Classes of Matrix Maps

The module `QuantumInfo.Channels.Bundled`, [QuantumInfo/Channels/Bundled.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean): 60 declarations (1 instance with no name), 25 with a docstring, 9 listed as significant.

> The bundled `MatrixMap`s: `HPMap`, `UnitalMap`, `TPMap`, `PMap`, and `CPMap`.
> These are defined over the bare minimum rings (`Semiring` or `RCLike`, respectively).
>
> The combinations `PTPMap` (positive trace-preserving), `CPTPMap`, and `CPUMap`
> (CP unital maps) take ℂ as the default class.
>
> The majority of quantum theory revolves around `CPTPMap`s, so those are explored more
> thoroughly in their file CPTP.lean.

**`HPMap`**, a structure, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L31).

> Hermitian-preserving linear maps.

```lean
structure HPMap extends MatrixMap dIn dOut 𝕜 where
  HP : MatrixMap.IsHermitianPreserving toLinearMap
```

**`UnitalMap`**, a structure, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L35).

> Unital linear maps.

```lean
structure UnitalMap [DecidableEq dIn] [DecidableEq dOut]
    extends MatrixMap dIn dOut R where
  unital : MatrixMap.Unital toLinearMap
```

**`TPMap`**, a structure, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L40).

> Trace-preserving linear maps.

```lean
structure TPMap [Fintype dIn] [Fintype dOut] extends MatrixMap dIn dOut R where
  TP : MatrixMap.IsTracePreserving toLinearMap
```

**`PMap`**, a structure, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L49).

> Positive linear maps.

```lean
structure PMap [Fintype dIn] [Fintype dOut]
    extends HPMap dIn dOut 𝕜 where
  pos : MatrixMap.IsPositive toLinearMap
  HP := pos.IsHermitianPreserving
```

**`CPMap`**, a structure, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L55).

> Completely positive linear maps.

```lean
structure CPMap [Fintype dIn] [Fintype dOut] [DecidableEq dIn]
    extends PMap dIn dOut 𝕜 where
  cp : MatrixMap.IsCompletelyPositive toLinearMap
  pos := cp.IsPositive
```

**`PTPMap`**, a structure, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L62).

> Positive trace-preserving linear maps. These includes all channels, but aren't
> necessarily *completely* positive, see `CPTPMap`.

```lean
structure PTPMap [Fintype dIn] [Fintype dOut]
  extends PMap dIn dOut 𝕜, TPMap dIn dOut 𝕜
```

**`PUMap`**, a structure, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L67).

> Positive unital maps. These are important because they are the
> dual to `PTPMap`: they are the most general way to map *observables*.

```lean
structure PUMap [Fintype dIn] [Fintype dOut] [DecidableEq dIn] [DecidableEq dOut]
  extends PMap dIn dOut 𝕜, UnitalMap dIn dOut 𝕜
```

**`CPTPMap`**, a structure, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L75).

> Completely positive trace-preserving linear maps. This is the most common
> meaning of "channel", often described as "the most general physically realizable
> quantum operation".

```lean
structure CPTPMap [Fintype dIn] [Fintype dOut] [DecidableEq dIn]
  extends PTPMap dIn dOut (𝕜 := 𝕜), CPMap dIn dOut 𝕜 where
```

**`CPUMap`**, a structure, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L80).

> Completely positive unital maps. These are important because they are the
> dual to `CPTPMap`: they are the physically realizable ways to map *observables*.

```lean
structure CPUMap [Fintype dIn] [Fintype dOut] [DecidableEq dIn] [DecidableEq dOut]
  extends CPMap dIn dOut 𝕜, PUMap dIn dOut 𝕜
```

## Hermitian-preserving maps

**`HPMap.map`**, an abbrev, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L96).

```lean
abbrev map (M : HPMap dIn dOut 𝕜) : MatrixMap dIn dOut 𝕜
```

**`HPMap.ext`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L99).

```lean
lemma ext (h : Λ₁.map = Λ₂.map) : Λ₁ = Λ₂
```

**`HPMap.funext_hermitian`**, a theorem, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L103). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Two maps are equal if they agree on all Hermitian inputs.

```lean
theorem funext_hermitian (h : ∀ M : HermitianMat dIn ℂ, CΛ₁.map M = CΛ₂.map M) :
    CΛ₁ = CΛ₂
```

**`HPMap.funext_pos`**, a theorem, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L113). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Two maps are equal if they agree on all positive inputs.

```lean
theorem funext_pos [Fintype dIn] (h : ∀ M : HermitianMat dIn ℂ, 0 ≤ M → CΛ₁.map M = CΛ₂.map M) :
    CΛ₁ = CΛ₂
```

**`HPMap.funext_pos_trace`**, a theorem, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L123). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Two maps are equal if they agree on all positive inputs with trace one

```lean
theorem funext_pos_trace [Fintype dIn]
  (h : ∀ M : HermitianMat dIn ℂ, 0 ≤ M → M.trace = 1 → CΛ₁.map M = CΛ₂.map M) :
    CΛ₁ = CΛ₂
```

**`HPMap.funext_mstate`**, a theorem, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L144). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Two maps are equal if they agree on all `MState`s.

```lean
theorem funext_mstate [Fintype dIn] [DecidableEq dIn] {Λ₁ Λ₂ : HPMap dIn dOut ℂ}
  (h : ∀ ρ : MState dIn, Λ₁.map ρ.m = Λ₂.map ρ.m) :
    Λ₁ = Λ₂
```

**`HPMap.instFunLike`**, an instance, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L150).

> Hermitian-preserving maps are functions from `HermitianMat`s to `HermitianMat`s.

```lean
noncomputable instance instFunLike : FunLike (HPMap dIn dOut ℂ) (HermitianMat dIn ℂ) (HermitianMat dOut ℂ)
```

**`HPMap.apply_hermitianMat_eq`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L155).

```lean
lemma apply_hermitianMat_eq (Λ : HPMap dIn dOut ℂ) (ρ : HermitianMat dIn ℂ) :
    Λ ρ = ⟨Λ.map ρ.1, Λ.HP ρ.2⟩
```

**An instance with no name**, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L159).

```lean
instance [Fintype dIn] : ContinuousLinearMapClass
    (HPMap dIn dOut ℂ) ℝ (HermitianMat dIn ℂ) (HermitianMat dOut ℂ)
```

## Positive-preserving maps

**`PMap.ext`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L179).

```lean
lemma ext {Λ₁ Λ₂ : PMap dIn dOut 𝕜} (h : Λ₁.map = Λ₂.map) : Λ₁ = Λ₂
```

**`PMap.injective_toHPMap`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L183).

```lean
lemma injective_toHPMap : (PMap.toHPMap (dIn := dIn) (dOut := dOut) (𝕜 := 𝕜)).Injective
```

**`PMap.instFunLike`**, an instance, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L187).

> Positive maps are functions from `HermitianMat`s to `HermitianMat`s.

```lean
noncomputable instance instFunLike : FunLike (PMap dIn dOut ℂ) (HermitianMat dIn ℂ) (HermitianMat dOut ℂ)
```

**`PMap.apply_hermitianMat_eq`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L191).

```lean
lemma apply_hermitianMat_eq (Λ : PMap dIn dOut ℂ) (ρ : HermitianMat dIn ℂ) :
    Λ ρ = ⟨Λ.map ρ.1, Λ.HP ρ.2⟩
```

**`PMap.instLinearMapClass`**, an instance, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L196).

```lean
instance instLinearMapClass : LinearMapClass (PMap dIn dOut ℂ) ℝ (HermitianMat dIn ℂ) (HermitianMat dOut ℂ)
```

**`PMap.instContinuousOrderHomClass`**, an instance, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L200).

```lean
instance instContinuousOrderHomClass : ContinuousOrderHomClass (PMap dIn dOut ℂ)
    (HermitianMat dIn ℂ) (HermitianMat dOut ℂ)
```

**`PMap.pos_Hermitian`**, a theorem, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L210). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Positive-presering maps also preserve positivity on, specifically, Hermitian matrices.

```lean
theorem pos_Hermitian (M : PMap dIn dOut ℂ) {x : HermitianMat dIn ℂ} (h : 0 ≤ x) : 0 ≤ M x
```

**`CPMap.of_kraus_CPMap`**, a def, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L217).

```lean
def of_kraus_CPMap {κ : Type*} [Fintype κ] [DecidableEq dIn] (M : κ → Matrix dOut dIn 𝕜) : CPMap dIn dOut 𝕜
```

## Positive trace-preserving maps

**`PTPMap.ext`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L234).

```lean
lemma ext {Λ₁ Λ₂ : PTPMap dIn dOut 𝕜} (h : Λ₁.map = Λ₂.map) : Λ₁ = Λ₂
```

**`PTPMap.injective_toPMap`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L238).

```lean
lemma injective_toPMap : (PTPMap.toPMap (dIn := dIn) (dOut := dOut) (𝕜 := 𝕜)).Injective
```

**`PTPMap.instFunLike`**, an instance, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L242).

> Positive trace-preserving maps are functions from `HermitianMat`s to `HermitianMat`s.

```lean
noncomputable instance instFunLike : FunLike (PTPMap dIn dOut ℂ) (HermitianMat dIn ℂ) (HermitianMat dOut ℂ)
```

**`PTPMap.apply_hermitianMat_eq_toPMap`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L246).

```lean
lemma apply_hermitianMat_eq_toPMap (Λ : PTPMap dIn dOut ℂ) (ρ : HermitianMat dIn ℂ) :
    Λ ρ = Λ.toPMap ρ
```

**`PTPMap.instLinearMapClass`**, an instance, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L249).

```lean
instance instLinearMapClass : LinearMapClass (PTPMap dIn dOut ℂ) ℝ (HermitianMat dIn ℂ) (HermitianMat dOut ℂ)
```

**`PTPMap.instHContinuousOrderHomClass`**, an instance, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L253).

```lean
instance instHContinuousOrderHomClass : ContinuousOrderHomClass (PTPMap dIn dOut ℂ)
    (HermitianMat dIn ℂ) (HermitianMat dOut ℂ)
```

**`PTPMap.pos_Hermitian`**, a theorem, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L263). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> PTP maps also preserve positivity on Hermitian matrices.

```lean
theorem pos_Hermitian (M : PTPMap dIn dOut ℂ) {x : HermitianMat dIn ℂ} (h : 0 ≤ x) : 0 ≤ M x
```

**`PTPMap.instMFunLike`**, an instance, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L267).

> `PTPMap`s are functions from `MState`s to `MState`s.

```lean
noncomputable instance instMFunLike [DecidableEq dIn] [DecidableEq dOut] :
    FunLike (PTPMap dIn dOut) (MState dIn) (MState dOut)
```

**`PTPMap.apply_mstate_eq`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L278).

```lean
lemma apply_mstate_eq [DecidableEq dIn] [DecidableEq dOut] (Λ : PTPMap dIn dOut ℂ) (ρ : MState dIn) :
    Λ ρ = MState.mk
      (Λ.toHPMap ρ.M) (HermitianMat.zero_le_iff.mpr (Λ.pos ρ.psd)) (by
        rw [HermitianMat.trace_eq_one_iff, ← ρ.tr']
        exact Λ.TP ρ)
```

**`PTPMap.instMContinuousMapClass`**, an instance, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L284).

```lean
instance instMContinuousMapClass [DecidableEq dIn] [DecidableEq dOut] :
    ContinuousMapClass (PTPMap dIn dOut) (MState dIn) (MState dOut)
```

**`PTPMap.val_apply_MState`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L291).

```lean
lemma val_apply_MState [DecidableEq dIn] (M : PTPMap dIn dOut) (ρ : MState dIn) :
    (M ρ : HermitianMat dOut ℂ) = (instFunLike.coe M) ρ
```

**`PTPMap.nonemptyOut`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L298).

```lean
lemma nonemptyOut (Λ : PTPMap dIn dOut) [hIn : Nonempty dIn] [DecidableEq dIn] : Nonempty dOut
```

## Completely positive trace-preserving linear maps

**`CPTPMap.ext`**, a theorem, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L321). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Two `CPTPMap`s are equal if their `MatrixMap`s are equal.

```lean
theorem ext {Λ₁ Λ₂ : CPTPMap dIn dOut 𝕜} (h : Λ₁.map = Λ₂.map) : Λ₁ = Λ₂
```

**`CPTPMap.injective_toPTPMap`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L325).

```lean
lemma injective_toPTPMap : (CPTPMap.toPTPMap (dIn := dIn) (dOut := dOut) (𝕜 := 𝕜)).Injective
```

**`CPTPMap.instMFunLike`**, an instance, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L350).

> `CPTPMap`s are functions from `MState`s to `MState`s.

```lean
noncomputable instance instMFunLike [DecidableEq dOut] : FunLike (CPTPMap dIn dOut) (MState dIn) (MState dOut)
```

**`CPTPMap.apply_mState_eq_toPTPMap`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L354).

```lean
lemma apply_mState_eq_toPTPMap [DecidableEq dOut] (Λ : CPTPMap dIn dOut) (ρ : MState dIn) :
    Λ ρ = Λ.toPTPMap ρ
```

**`CPTPMap.IsTracePreserving`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L363).

```lean
lemma IsTracePreserving (Λ : CPTPMap dIn dOut 𝕜) : Λ.map.IsTracePreserving
```

**`CPTPMap.of_kraus_CPTPMap`**, a def, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L366).

```lean
def of_kraus_CPTPMap {κ : Type*} [Fintype κ]
  (M : κ → Matrix dOut dIn 𝕜)
  (hTP : (∑ k, (M k).conjTranspose * (M k)) = 1) : CPTPMap dIn dOut 𝕜
```

**`PUMap.ext`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L379).

```lean
lemma ext {Λ₁ Λ₂ : PUMap dIn dOut 𝕜} (h : Λ₁.map = Λ₂.map) : Λ₁ = Λ₂
```

**`PUMap.injective_toPMap`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L383).

```lean
lemma injective_toPMap : (PUMap.toPMap (dIn := dIn) (dOut := dOut) (𝕜 := 𝕜)).Injective
```

**`PUMap.instFunLike`**, an instance, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L388).

> `PUMap`s are functions from `HermitianMat`s to `HermitianMat`s.

```lean
noncomputable instance instFunLike : FunLike (PUMap dIn dOut ℂ) (HermitianMat dIn ℂ) (HermitianMat dOut ℂ)
```

**`PUMap.apply_hermitianMat_eq_toPMap`**, a lemma, [line 392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L392).

```lean
lemma apply_hermitianMat_eq_toPMap (Λ : PUMap dIn dOut ℂ) (ρ : HermitianMat dIn ℂ) :
    Λ ρ = Λ.toPMap ρ
```

**`PUMap.instLinearMapClass`**, an instance, [line 395](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L395).

```lean
instance instLinearMapClass : LinearMapClass (PUMap dIn dOut ℂ) ℝ (HermitianMat dIn ℂ) (HermitianMat dOut ℂ)
```

**`PUMap.instHContinuousOrderHomClass`**, an instance, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L399).

```lean
instance instHContinuousOrderHomClass : ContinuousOrderHomClass (PUMap dIn dOut ℂ)
    (HermitianMat dIn ℂ) (HermitianMat dOut ℂ)
```

**`PUMap.instOneHomClass`**, an instance, [line 407](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L407).

```lean
instance instOneHomClass : OneHomClass (PUMap dIn dOut ℂ)
    (HermitianMat dIn ℂ) (HermitianMat dOut ℂ)
```

**`PUMap.pos_Hermitian`**, a theorem, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L413). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> CPTP maps also preserve positivity on Hermitian matrices.

```lean
theorem pos_Hermitian (M : PUMap dIn dOut ℂ) {x : HermitianMat dIn ℂ} (h : 0 ≤ x) : 0 ≤ M x
```

**`CPUMap.ext`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L422).

```lean
lemma ext {Λ₁ Λ₂ : CPUMap dIn dOut 𝕜} (h : Λ₁.map = Λ₂.map) : Λ₁ = Λ₂
```

**`CPUMap.injective_toPMap`**, a lemma, [line 426](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L426).

```lean
lemma injective_toPMap : (CPMap.toPMap ∘ CPUMap.toCPMap (dIn := dIn) (dOut := dOut) (𝕜 := 𝕜)).Injective
```

**`CPUMap.instFunLike`**, an instance, [line 431](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L431).

> `CPUMap`s are functions from `HermitianMat`s to `HermitianMat`s.

```lean
noncomputable instance instFunLike : FunLike (CPUMap dIn dOut ℂ) (HermitianMat dIn ℂ) (HermitianMat dOut ℂ)
```

**`CPUMap.apply_hermitianMat_eq_toPMap`**, a lemma, [line 435](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L435).

```lean
lemma apply_hermitianMat_eq_toPMap (Λ : CPUMap dIn dOut ℂ) (ρ : HermitianMat dIn ℂ) :
    Λ ρ = Λ.toPMap ρ
```

**`CPUMap.instLinearMapClass`**, an instance, [line 438](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L438).

```lean
instance instLinearMapClass : LinearMapClass (CPUMap dIn dOut ℂ) ℝ (HermitianMat dIn ℂ) (HermitianMat dOut ℂ)
```

**`CPUMap.instHContinuousOrderHomClass`**, an instance, [line 442](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L442).

```lean
instance instHContinuousOrderHomClass : ContinuousOrderHomClass (CPUMap dIn dOut ℂ)
    (HermitianMat dIn ℂ) (HermitianMat dOut ℂ)
```

**`CPUMap.instOneHomClass`**, an instance, [line 450](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L450).

```lean
instance instOneHomClass : OneHomClass (CPUMap dIn dOut ℂ)
    (HermitianMat dIn ℂ) (HermitianMat dOut ℂ)
```

**`CPUMap.pos_Hermitian`**, a theorem, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean#L456). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> CPTP maps also preserve positivity on Hermitian matrices.

```lean
theorem pos_Hermitian (M : CPUMap dIn dOut ℂ) {x : HermitianMat dIn ℂ} (h : 0 ≤ x) : 0 ≤ M x
```

## Depends on

- [Properties of Matrix Maps](unbundled.md)

## Sources

- [QuantumInfo/Channels/Bundled.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Bundled.lean)
