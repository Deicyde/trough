---
declaration: module
origin: cited
lean: StandardModel.su3LabelFun, StandardModel.su3Label, StandardModel.su2LabelFun, StandardModel.su2Label, StandardModel.su3Label_apply, StandardModel.su2Label_apply, StandardModel.gellMannMatrix_eq_matrix, StandardModel.pauliMatrix_inr_eq_matrix
statement: formalized
proof: formalized
---

# Families of adjoint components and their invariants

The module `PhyslibAlpha.Particles.StandardModel.GaugeGroup.Invariants.Adjoint`, [PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean): 42 declarations, 38 with a docstring.

## i. Overview

> The Standard Model labels the adjoint indices of `su(3)` by the eight Gell-Mann matrices
> `gellMannMatrix`, and those of `su(2)` by the three Pauli matrices, and moves them by the adjoint
> matrices `su3AdjointMatrix` and `su2AdjointMatrix`. These are the generalized Gell-Mann matrices of
> `LocalGaugeData.SU.GellMann` for `N = 3` and `N = 2` under a relabelling, `su3Label` and
> `su2Label`, and the adjoint matrices are the matrices of the adjoint action in those bases (A).
>
> A family with one adjoint index has no invariant in its span, and a family with two adjoint
> indices of the same factor has its invariants reduced to the trace contraction `∑ a, T ![a, a]`
> (C for colour, D for isospin): the invariant tensors of `SuT[N, .adj]` and `SuT[N, .adj, .adj]` of
> `LocalGaugeData.SU.Invariants.Adjoint`, read on the components through the relabelled
> component maps of B.

## ii. Key results

> - `StandardModel.su3Label`, `StandardModel.su2Label` : the Gell-Mann and Pauli labels as
>   generalized Gell-Mann labels.
> - `StandardModel.IsSU3Adjoint.reducesInvariantsTo_bot` : one colour adjoint index carries no
>   invariant, and its isospin twin.
> - `StandardModel.IsSU3BiAdjoint.reducesInvariantsTo_span_traceContraction` : two colour adjoint
>   indices reduce to the trace contraction, and its isospin twin.

## iv. References

> * None.

## A. The Gell-Mann labels

**`StandardModel.su3LabelFun`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L65).

> The labels of the Gell-Mann matrices of `su(3)` as generalized Gell-Mann labels: the
> symmetric and antisymmetric matrices of the planes `(0, 1)`, `(0, 2)` and `(1, 2)`, and the two
> diagonal matrices.

```lean
def su3LabelFun : Fin 8 → GellMann.Index 3
```

**`StandardModel.su3Label`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L76).

> The relabelling of the Gell-Mann matrices of `su(3)` by generalized Gell-Mann labels.

```lean
noncomputable def su3Label : Fin 8 ≃ GellMann.Index 3
```

**`StandardModel.su2LabelFun`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L80).

> The labels of the Pauli matrices of `su(2)` as generalized Gell-Mann labels.

```lean
def su2LabelFun : Fin 3 → GellMann.Index 2
```

**`StandardModel.su2Label`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L86).

> The relabelling of the Pauli matrices of `su(2)` by generalized Gell-Mann labels.

```lean
noncomputable def su2Label : Fin 3 ≃ GellMann.Index 2
```

**`StandardModel.su3Label_apply`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L90).

```lean
lemma su3Label_apply (a : Fin 8) : su3Label a = su3LabelFun a
```

**`StandardModel.su2Label_apply`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L93).

```lean
lemma su2Label_apply (i : Fin 3) : su2Label i = su2LabelFun i
```

**`StandardModel.gellMannMatrix_eq_matrix`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L96).

> The Gell-Mann matrices of `su(3)` are the generalized Gell-Mann matrices.

```lean
lemma gellMannMatrix_eq_matrix (a : Fin 8) :
    gellMannMatrix a = GellMann.matrix (su3Label a)
```

**`StandardModel.pauliMatrix_inr_eq_matrix`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L107).

> The Pauli matrices are the generalized Gell-Mann matrices of `su(2)`.

```lean
lemma pauliMatrix_inr_eq_matrix (i : Fin 3) :
    pauliMatrix (Sum.inr i) = GellMann.matrix (su2Label i)
```

**`StandardModel.ofReal_half_re_trace`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L115).

> A complex number fixed by conjugation is the image of its real part.

```lean
lemma ofReal_half_re_trace {z : ℂ} (hz : star (z / 2) = z / 2) :
    ((2⁻¹ * z.re : ℝ) : ℂ) = z / 2
```

**`StandardModel.su3AdjointMatrix_eq_adjMatrix`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L124).

> The adjoint matrix of `SU(3)` is the matrix of the adjoint action in the Gell-Mann
> basis.

```lean
lemma su3AdjointMatrix_eq_adjMatrix (U : SU 3) (a b : Fin 8) :
    ((su3AdjointMatrix U a b : ℝ) : ℂ) = adjMatrix U (su3Label a) (su3Label b)
```

**`StandardModel.su2AdjointMatrix_eq_adjMatrix`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L131).

> The adjoint matrix of `SU(2)` is the matrix of the adjoint action in the Pauli basis.

```lean
lemma su2AdjointMatrix_eq_adjMatrix (U : SU 2) (i j : Fin 3) :
    ((su2AdjointMatrix U i j : ℝ) : ℂ) = adjMatrix U (su2Label i) (su2Label j)
```

## B. Relabelled adjoint families

> A family indexed by the Standard Model labels of the adjoint index and moved by the Standard Model
> adjoint matrices is, after relabelling, a family moved by the matrices of the adjoint action.

**`StandardModel.adjMap_smul_of_relabel_law`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L155).

> A linear map moving a family with one adjoint label by the Standard Model adjoint matrix of
> `U` intertwines the map of the relabelled family with the action of `U`.

```lean
lemma adjMap_smul_of_relabel_law (T : ι → B) {f : B →ₗ[ℂ] B} {U : SU N}
    (hf : ∀ l, f (T l) = ∑ a, ((M U a l : ℝ) : ℂ) • T a) (t : SuT[N, .adj]) :
    f (adjMap (T ∘ e.symm) t) = adjMap (T ∘ e.symm) (U • t)
```

**`StandardModel.adjPairMap_smul_of_relabel_law`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L165).

> A linear map moving a family with two adjoint labels by the Standard Model adjoint matrix of
> `U` on each label intertwines the map of the relabelled family with the action of `U`.

```lean
lemma adjPairMap_smul_of_relabel_law (T : (Fin 2 → ι) → B) {f : B →ₗ[ℂ] B} {U : SU N}
    (hf : ∀ l, f (T l) = ∑ a : Fin 2 → ι, (∏ i : Fin 2, ((M U (a i) (l i) : ℝ) : ℂ)) • T a)
    (t : SuT[N, .adj, .adj]) :
    f (adjPairMap (fun n => T (e.symm ∘ n)) t) = adjPairMap (fun n => T (e.symm ∘ n)) (U • t)
```

**`StandardModel.adjPairMap_relabel_two_smul_adjUnitTensor`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L176).

> The map of the relabelled family sends twice the unit tensor to the trace contraction.

```lean
lemma adjPairMap_relabel_two_smul_adjUnitTensor (T : (Fin 2 → ι) → B) :
    adjPairMap (fun n => T (e.symm ∘ n)) ((2 : ℂ) • adjUnitTensor N) = ∑ a : ι, T ![a, a]
```

## C. The colour adjoint families

**`StandardModel.IsSU3AdjointMat`**, a def, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L195).

> The linear map `f` moves the components of `T` as `U ∈ SU(3)` moves a tensor with one
> adjoint index: one factor of the adjoint matrix, the summed index first.

```lean
def IsSU3AdjointMat (U : SU 3) (f : B →ₗ[ℂ] B) (T : Fin 8 → B) : Prop
```

**`StandardModel.IsSU3Adjoint`**, an abbrev, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L200).

> A family `T^a` with one `su(3)` adjoint index: the map of the relabelled family out of the
> tensors of `SU(3)` is equivariant for the colour factor of the gauge group.

```lean
abbrev IsSU3Adjoint (B : Type*) [AddCommGroup B] [Module ℂ B]
    (repGauge : Representation ℂ GaugeGroupI B) (T : Fin 8 → B) : Prop
```

**`StandardModel.IsSU3BiAdjointMat`**, a def, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L206).

> The linear map `f` moves the components of `T` as `U ∈ SU(3)` moves a tensor with two
> adjoint indices: one factor of the adjoint matrix per index, the summed index first.

```lean
def IsSU3BiAdjointMat (U : SU 3) (f : B →ₗ[ℂ] B) (T : (Fin 2 → Fin 8) → B) : Prop
```

**`StandardModel.IsSU3BiAdjoint`**, an abbrev, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L212).

> A family `T^{ab}` with two `su(3)` adjoint indices: the map of the relabelled family out of
> the tensors of `SU(3)` is equivariant for the colour factor of the gauge group.

```lean
abbrev IsSU3BiAdjoint (B : Type*) [AddCommGroup B] [Module ℂ B]
    (repGauge : Representation ℂ GaugeGroupI B) (T : (Fin 2 → Fin 8) → B) : Prop
```

**`StandardModel.IsSU3Adjoint.of_law`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L222).

> A family obeying the law for every colour rotation is such a family.

```lean
lemma of_law (hT : ∀ U : SU 3, IsSU3AdjointMat U (repGauge (U, 1, 1)) T) :
    IsSU3Adjoint B repGauge T
```

**`StandardModel.IsSU3Adjoint.isStableUnder_span`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L227).

> The span of the components is stable under the colour factor.

```lean
lemma isStableUnder_span (hT : IsSU3Adjoint B repGauge T) :
    IsStableUnder (fun U : SU 3 => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T))
```

**`StandardModel.IsSU3Adjoint.reducesInvariantsTo_bot`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L235).

> A colour invariant of the span of the components joined with a stable submodule lies in
> that submodule: an adjoint index contributes nothing to the invariants.

```lean
lemma reducesInvariantsTo_bot (hT : IsSU3Adjoint B repGauge T) :
    ReducesInvariantsTo (fun U : SU 3 => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T)) ⊥
```

**`StandardModel.IsSU3BiAdjoint.of_law`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L248).

> A family obeying the law for every colour rotation is such a family.

```lean
lemma of_law (hT : ∀ U : SU 3, IsSU3BiAdjointMat U (repGauge (U, 1, 1)) T) :
    IsSU3BiAdjoint B repGauge T
```

**`StandardModel.IsSU3BiAdjoint.traceContraction`**, a def, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L254).

> The trace contraction `∑ a, T ![a, a]` of the two adjoint indices.

```lean
def traceContraction (T : (Fin 2 → Fin 8) → B) : B
```

**`StandardModel.IsSU3BiAdjoint.traceContraction_mem_span`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L256).

```lean
lemma traceContraction_mem_span (T : (Fin 2 → Fin 8) → B) :
    traceContraction T ∈ Submodule.span ℂ (Set.range T)
```

**`StandardModel.IsSU3BiAdjoint.map_traceContraction`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L262).

> Any map moving the components by the adjoint matrix of an element of `SU(3)` fixes the
> trace contraction.

```lean
lemma map_traceContraction {U : SU 3} {f : B →ₗ[ℂ] B} (hf : IsSU3BiAdjointMat U f T) :
    f (traceContraction T) = traceContraction T
```

**`StandardModel.IsSU3BiAdjoint.range_adjPairMap`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L269).

> The range of the map of the relabelled family is the span of the components.

```lean
lemma range_adjPairMap (T : (Fin 2 → Fin 8) → B) :
    LinearMap.range (adjPairMap fun n => T (su3Label.symm ∘ n))
      = Submodule.span ℂ (Set.range T)
```

**`StandardModel.IsSU3BiAdjoint.isStableUnder_span`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L276).

> The span of the components is stable under the colour factor.

```lean
lemma isStableUnder_span (hT : IsSU3BiAdjoint B repGauge T) :
    IsStableUnder (fun U : SU 3 => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T))
```

**`StandardModel.IsSU3BiAdjoint.reducesInvariantsTo_span_traceContraction`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L284).

> The colour invariants of the span of the components reduce to the line through the trace
> contraction.

```lean
lemma reducesInvariantsTo_span_traceContraction (hT : IsSU3BiAdjoint B repGauge T) :
    ReducesInvariantsTo (fun U : SU 3 => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T)) (ℂ ∙ traceContraction T)
```

## D. The isospin adjoint families

**`StandardModel.IsSU2AdjointMat`**, a def, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L305).

> The linear map `f` moves the components of `T` as `U ∈ SU(2)` moves a tensor with one
> adjoint index: one factor of the adjoint matrix, the summed index first.

```lean
def IsSU2AdjointMat (U : SU 2) (f : B →ₗ[ℂ] B) (T : Fin 3 → B) : Prop
```

**`StandardModel.IsSU2Adjoint`**, an abbrev, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L310).

> A family `T^a` with one `su(2)` adjoint index: the map of the relabelled family out of the
> tensors of `SU(2)` is equivariant for the isospin factor of the gauge group.

```lean
abbrev IsSU2Adjoint (B : Type*) [AddCommGroup B] [Module ℂ B]
    (repGauge : Representation ℂ GaugeGroupI B) (T : Fin 3 → B) : Prop
```

**`StandardModel.IsSU2BiAdjointMat`**, a def, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L316).

> The linear map `f` moves the components of `T` as `U ∈ SU(2)` moves a tensor with two
> adjoint indices: one factor of the adjoint matrix per index, the summed index first.

```lean
def IsSU2BiAdjointMat (U : SU 2) (f : B →ₗ[ℂ] B) (T : (Fin 2 → Fin 3) → B) : Prop
```

**`StandardModel.IsSU2BiAdjoint`**, an abbrev, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L322).

> A family `T^{ab}` with two `su(2)` adjoint indices: the map of the relabelled family out of
> the tensors of `SU(2)` is equivariant for the isospin factor of the gauge group.

```lean
abbrev IsSU2BiAdjoint (B : Type*) [AddCommGroup B] [Module ℂ B]
    (repGauge : Representation ℂ GaugeGroupI B) (T : (Fin 2 → Fin 3) → B) : Prop
```

**`StandardModel.IsSU2Adjoint.of_law`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L332).

> A family obeying the law for every isospin rotation is such a family.

```lean
lemma of_law (hT : ∀ U : SU 2, IsSU2AdjointMat U (repGauge (1, U, 1)) T) :
    IsSU2Adjoint B repGauge T
```

**`StandardModel.IsSU2Adjoint.isStableUnder_span`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L337).

> The span of the components is stable under the isospin factor.

```lean
lemma isStableUnder_span (hT : IsSU2Adjoint B repGauge T) :
    IsStableUnder (fun U : SU 2 => repGauge ((1, U, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T))
```

**`StandardModel.IsSU2Adjoint.reducesInvariantsTo_bot`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L345).

> A isospin invariant of the span of the components joined with a stable submodule lies in
> that submodule: an adjoint index contributes nothing to the invariants.

```lean
lemma reducesInvariantsTo_bot (hT : IsSU2Adjoint B repGauge T) :
    ReducesInvariantsTo (fun U : SU 2 => repGauge ((1, U, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T)) ⊥
```

**`StandardModel.IsSU2BiAdjoint.of_law`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L358).

> A family obeying the law for every isospin rotation is such a family.

```lean
lemma of_law (hT : ∀ U : SU 2, IsSU2BiAdjointMat U (repGauge (1, U, 1)) T) :
    IsSU2BiAdjoint B repGauge T
```

**`StandardModel.IsSU2BiAdjoint.traceContraction`**, a def, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L364).

> The trace contraction `∑ a, T ![a, a]` of the two adjoint indices.

```lean
def traceContraction (T : (Fin 2 → Fin 3) → B) : B
```

**`StandardModel.IsSU2BiAdjoint.traceContraction_mem_span`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L366).

```lean
lemma traceContraction_mem_span (T : (Fin 2 → Fin 3) → B) :
    traceContraction T ∈ Submodule.span ℂ (Set.range T)
```

**`StandardModel.IsSU2BiAdjoint.map_traceContraction`**, a lemma, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L372).

> Any map moving the components by the adjoint matrix of an element of `SU(2)` fixes the
> trace contraction.

```lean
lemma map_traceContraction {U : SU 2} {f : B →ₗ[ℂ] B} (hf : IsSU2BiAdjointMat U f T) :
    f (traceContraction T) = traceContraction T
```

**`StandardModel.IsSU2BiAdjoint.range_adjPairMap`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L379).

> The range of the map of the relabelled family is the span of the components.

```lean
lemma range_adjPairMap (T : (Fin 2 → Fin 3) → B) :
    LinearMap.range (adjPairMap fun n => T (su2Label.symm ∘ n))
      = Submodule.span ℂ (Set.range T)
```

**`StandardModel.IsSU2BiAdjoint.isStableUnder_span`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L386).

> The span of the components is stable under the isospin factor.

```lean
lemma isStableUnder_span (hT : IsSU2BiAdjoint B repGauge T) :
    IsStableUnder (fun U : SU 2 => repGauge ((1, U, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T))
```

**`StandardModel.IsSU2BiAdjoint.reducesInvariantsTo_span_traceContraction`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L394).

> The isospin invariants of the span of the components reduce to the line through the trace
> contraction.

```lean
lemma reducesInvariantsTo_span_traceContraction (hT : IsSU2BiAdjoint B repGauge T) :
    ReducesInvariantsTo (fun U : SU 2 => repGauge ((1, U, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T)) (ℂ ∙ traceContraction T)
```

## Depends on

- [Invariants of one and of two adjoint indices of `SU(N)`](../../../classicalfieldtheory/gaugetheory/part-05/localgaugedata-su-invariants-adjoint.md)
- [The adjoint matrices of `SU(2)` and `SU(3)`](gaugegroup-adjointmatrix.md)
- [Families of colour and isospin components and their invariants](gaugegroup-invariants-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean)
