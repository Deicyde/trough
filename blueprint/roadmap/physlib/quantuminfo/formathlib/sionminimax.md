---
declaration: module
origin: cited
lean: ciSup_ciInf_le_ciInf_ciSup, sion_minimax, Set.image2_flip, BddAbove.range_max, BddBelow.range_min, ciInf_eq_min_cInf_inter_diff, lt_ciInf_iff, sup_ciSup
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.SionMinimax

The module `QuantumInfo.ForMathlib.SionMinimax`, [QuantumInfo/ForMathlib/SionMinimax.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean): 29 declarations, 2 with a docstring, 2 listed as significant; 3 private, not shown.

**`Set.image2_flip`**, a lemma, [line 17](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L17).

```lean
lemma Set.image2_flip {α β γ : Type*} {f : α → β → γ} (s : Set α) (t : Set β) :
    image2 (flip f) t s = image2 f s t
```

**`ciSup_ciInf_le_ciInf_ciSup`**, a theorem, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L26). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The **max-min theorem**. A version of `iSup_iInf_le_iInf_iSup` for conditionally complete lattices.

```lean
theorem ciSup_ciInf_le_ciInf_ciSup {ι': Type*} [Nonempty ι]
  (f : ι → ι' → α) (Ha : ∀ j, BddAbove (Set.range (f · j))) (Hb : ∀ i, BddBelow (Set.range (f i))) :
    ⨆ i, ⨅ j, f i j ≤ ⨅ j, ⨆ i, f i j
```

**`BddAbove.range_max`**, a lemma, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L31).

```lean
lemma BddAbove.range_max (hf : BddAbove (Set.range f)) (hg : BddAbove (Set.range g)) :
    BddAbove (Set.range (max f g))
```

**`BddBelow.range_min`**, a lemma, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L42).

```lean
lemma BddBelow.range_min (hf : BddBelow (Set.range f)) (hg : BddBelow (Set.range g)) :
    BddBelow (Set.range (min f g))
```

**`ciInf_eq_min_cInf_inter_diff`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L46).

```lean
lemma ciInf_eq_min_cInf_inter_diff (S T : Set ι)
  [Nonempty (S ∩ T : Set ι)] [Nonempty (S \ T : Set ι)] (hf : BddBelow (f '' S)) :
    ⨅ i : S, f i = (⨅ i : (S ∩ T : Set ι), f i) ⊓ ⨅ i : (S \ T : Set ι), f i
```

**`lt_ciInf_iff`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L68).

```lean
lemma lt_ciInf_iff (hf : BddBelow (Set.range f)) :
    a < iInf f ↔ ∃ b, a < b ∧ ∀ (i : ι), b ≤ f i
```

**`sup_ciSup`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L72).

```lean
lemma sup_ciSup (hf : BddAbove (Set.range f)) : a ⊔ ⨆ x, f x = ⨆ x, a ⊔ f x
```

**`inf_ciInf`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L75).

```lean
lemma inf_ciInf (hf : BddBelow (Set.range f)) : a ⊓ ⨅ x, f x = ⨅ x, a ⊓ f x
```

**`ciInf_sup_ciInf_le`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L78).

```lean
lemma ciInf_sup_ciInf_le (hf : BddBelow (Set.range f)) (hg : BddBelow (Set.range g)) :
    (⨅ i, f i) ⊔ ⨅ i, g i ≤ ⨅ i, f i ⊔ g i
```

**`le_ciSup_inf_ciSup`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L82).

```lean
lemma le_ciSup_inf_ciSup (hf : BddAbove (Set.range f)) (hg : BddAbove (Set.range g)) :
    ⨆ (i : ι), f i ⊓ g i ≤ (⨆ (i : ι), f i) ⊓ ⨆ (i : ι), g i
```

**`QuasiconvexOn.subset`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L88).

```lean
lemma QuasiconvexOn.subset
  {𝕜 E β : Type*} [Semiring 𝕜] [PartialOrder 𝕜] [AddCommMonoid E] [LE β] [SMul 𝕜 E]
  {s : Set E} {f : E → β} (h : QuasiconvexOn 𝕜 s f) {t : Set E} (hts : t ⊆ s) (ht : Convex 𝕜 t) :
    QuasiconvexOn 𝕜 t f
```

**`QuasiconvexOn.mem_segment_le_max`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L96).

```lean
lemma QuasiconvexOn.mem_segment_le_max
  {𝕜 E β : Type*} [Semiring 𝕜] [PartialOrder 𝕜] [AddCommMonoid E] [SemilatticeSup β] [SMul 𝕜 E]
  {s : Set E} {f : E → β} (h : QuasiconvexOn 𝕜 s f)
  {x y z : E} (hx : x ∈ s) (hy : y ∈ s) (hz : z ∈ segment 𝕜 x y):
    f z ≤ f x ⊔ f y
```

**`QuasiconcaveOn.min_le_mem_segment`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L103).

```lean
lemma QuasiconcaveOn.min_le_mem_segment
  {𝕜 E β : Type*} [Semiring 𝕜] [PartialOrder 𝕜] [AddCommMonoid E] [SemilatticeInf β] [SMul 𝕜 E]
  {s : Set E} {f : E → β} (h : QuasiconcaveOn 𝕜 s f)
  {x y z : E} (hx : x ∈ s) (hy : y ∈ s) (hz : z ∈ segment 𝕜 x y):
    f x ⊓ f y ≤ f z
```

**`LowerSemicontinuousOn.bddBelow`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L110).

```lean
lemma LowerSemicontinuousOn.bddBelow {α : Type*} [TopologicalSpace α] {S : Set α} {g : α → ℝ}
    (hg : LowerSemicontinuousOn g S) (hS : IsCompact S) : BddBelow (g '' S)
```

**`LowerSemicontinuousOn.max`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L137).

```lean
lemma LowerSemicontinuousOn.max {α : Type*} [TopologicalSpace α] {S : Set α} {f g : α → ℝ}
    (hf : LowerSemicontinuousOn f S) (hg : LowerSemicontinuousOn g S) :
    LowerSemicontinuousOn (fun x ↦ max (f x) (g x)) S
```

**`lowerSemicontinuousOn_iff_isClosed_preimage`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L148).

```lean
lemma lowerSemicontinuousOn_iff_isClosed_preimage {f : α → γ} [IsClosed s] :
    LowerSemicontinuousOn f s ↔ ∀ y, IsClosed (s ∩ f ⁻¹' Set.Iic y)
```

**`segment.isConnected`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L168).

```lean
lemma segment.isConnected {E : Type u_1} [AddCommGroup E] [Module ℝ E] [TopologicalSpace E] [ContinuousAdd E] [ContinuousSMul ℝ E] (a b : E) :
    IsConnected (segment ℝ a b)
```

**`BddAbove.range_inf_of_image2`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L173).

```lean
lemma BddAbove.range_inf_of_image2 {M N α : Type*} {f : M → N → α} [ConditionallyCompleteLinearOrder α]
  {S : Set M} {T : Set N} (h_bddA : BddAbove (Set.image2 f S T)) (h_bddB : BddBelow (Set.image2 f S T)) :
    BddAbove (Set.range fun y : T ↦ ⨅ x : S, f x y)
```

**`BddBelow.range_sup_of_image2`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L190).

```lean
lemma BddBelow.range_sup_of_image2 {M N α : Type*} {f : M → N → α} [ConditionallyCompleteLinearOrder α]
  {S : Set M} {T : Set N} (h_bddA : BddAbove (Set.image2 f S T)) (h_bddB : BddBelow (Set.image2 f S T)) :
      BddBelow (Set.range fun y : T ↦ ⨆ x : S, f x y)
```

**`ciInf_le_ciInf_of_subset`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L195).

```lean
lemma ciInf_le_ciInf_of_subset {α β : Type*} [ConditionallyCompleteLattice α]
  {f : β → α} {s t : Set β} (hs : s.Nonempty) (hf : BddBelow (f '' t)) (hst : s ⊆ t) :
    ⨅ x : t, f x ≤ ⨅ x : s, f x
```

**`LowerSemicontinuousOn.dite_top`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L207).

```lean
lemma LowerSemicontinuousOn.dite_top {α β : Type*} [TopologicalSpace α] [Preorder β] [OrderTop β]
  {s : Set α} (p : α → Prop) [DecidablePred p] {f : (a : α) → p a → β}
  (hf : LowerSemicontinuousOn (fun x : Subtype p ↦ f x.val x.prop) {x | x.val ∈ s})
  (h_relatively_closed : ∃ U : Set α, IsClosed U ∧ s ∩ U = s ∩ Set.ofPred p) :
    LowerSemicontinuousOn (fun x ↦ dite (p x) (f x) (fun _ ↦ ⊤)) s
```

**`LowerSemicontinuousOn.comp_continuousOn`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L230).

```lean
lemma LowerSemicontinuousOn.comp_continuousOn {α β γ : Type*}
  [TopologicalSpace α] [TopologicalSpace β] [Preorder γ] {f : α → β} {s : Set α} {g : β → γ} {t : Set β}
  (hg : LowerSemicontinuousOn g t) (hf : ContinuousOn f s) (h : Set.MapsTo f s t) :
    LowerSemicontinuousOn (g ∘ f) s
```

**`UpperSemicontinuousOn.comp_continuousOn`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L245).

```lean
lemma UpperSemicontinuousOn.comp_continuousOn {α β γ : Type*}
  [TopologicalSpace α] [TopologicalSpace β] [Preorder γ] {f : α → β} {s : Set α} {g : β → γ} {t : Set β}
  (hg : UpperSemicontinuousOn g t) (hf : ContinuousOn f s) (h : Set.MapsTo f s t) :
    UpperSemicontinuousOn (g ∘ f) s
```

**`LowerSemicontinuousOn.ite_top`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L251).

```lean
lemma LowerSemicontinuousOn.ite_top {α β : Type*} [TopologicalSpace α] [Preorder β] [OrderTop β]
  {s : Set α} (p : α → Prop) [DecidablePred p] {f : (a : α) → β} (hf : LowerSemicontinuousOn f (s ∩ Set.ofPred p))
  (h_relatively_closed : ∃ U : Set α, IsClosed U ∧ s ∩ U = s ∩ Set.ofPred p) :
    LowerSemicontinuousOn (fun x ↦ ite (p x) (f x) ⊤) s
```

**`LeftOrdContinuous.comp_lowerSemicontinuousOn_strong_assumptions`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L257).

```lean
lemma LeftOrdContinuous.comp_lowerSemicontinuousOn_strong_assumptions {α γ δ : Type*}
  [TopologicalSpace α] [LinearOrder γ] [LinearOrder δ] [TopologicalSpace δ] [OrderTopology δ]
  [TopologicalSpace γ] [OrderTopology γ] [DenselyOrdered γ] [DenselyOrdered δ]
  {s : Set α} {g : γ → δ} {f : α → γ} (hg : LeftOrdContinuous g) (hf : LowerSemicontinuousOn f s) (hg2 : Monotone g) :
    LowerSemicontinuousOn (g ∘ f) s
```

**`UpperSemicontinuousOn.frequently_lt_of_tendsto`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L292).

```lean
lemma UpperSemicontinuousOn.frequently_lt_of_tendsto {α β γ : Type*} [TopologicalSpace β] [Preorder γ]
  {f : β → γ} {T : Set β} (hf : UpperSemicontinuousOn f T) {c : γ} {zs : α → β} {z : β}
  {l : Filter α} [l.NeBot] (hzs : l.Tendsto zs (nhds z)) (hx₂ : f z < c) (hzI : ∀ a, zs a ∈ T) (hzT : z ∈ T) :
    ∀ᶠ a in l, f (zs a) < c
```

**`Finset.ciInf_insert`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L301).

```lean
lemma Finset.ciInf_insert {α β : Type*} [DecidableEq α] [ConditionallyCompleteLattice β]
  (t : Finset α) (ht : t.Nonempty) (x : α) (f : α → β) :
    ⨅ (a : (insert x t : _)), f a = f x ⊓ ⨅ (a : t), f a
```

**`Finset.ciSup_insert`**, a lemma, [line 320](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L320).

```lean
lemma Finset.ciSup_insert {α β : Type*} [DecidableEq α] [ConditionallyCompleteLattice β]
  (t : Finset α) (ht : t.Nonempty) (x : α) (f : α → β) :
    ⨆ (a : (insert x t : _)), f a = f x ⊔ ⨆ (a : t), f a
```

> Following https://projecteuclid.org/journals/kodai-mathematical-journal/volume-11/issue-1/Elementary-proof-for-Sions-minimax-theorem/10.2996/kmj/1138038812.full, with some corrections. There are two errors in Lemma 2 and the main theorem: an incorrect step that
> `(∀ x, a < f x) → (a < ⨅ x, f x)`. This is repaired by taking an extra `exists_between` to get `a < b < ⨅ ...`, concluding that
> `(∀ x, b < f x) → (b ≤ ⨅ x, f x)` and so `(a < ⨅ x, f x)`.

**`sion_minimax`**, a theorem, [line 683](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean#L683). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> **Sion's Minimax theorem**. Because of `ciSup` and `ciInf` junk values when f isn't
> bounded, we need to assume that it's bounded above and below.

```lean
theorem sion_minimax
  (h_bddA : BddAbove (Set.image2 f S T))
  (h_bddB : BddBelow (Set.image2 f S T))
    : ⨅ x : S, ⨆ y : T, f x y = ⨆ y : T, ⨅ x : S, f x y
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [QuantumInfo/ForMathlib/SionMinimax.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/SionMinimax.lean)
