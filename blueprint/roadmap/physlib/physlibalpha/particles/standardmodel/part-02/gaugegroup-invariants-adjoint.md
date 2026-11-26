---
declaration: module
origin: cited
lean: StandardModel.su3LabelFun, StandardModel.su3Label, StandardModel.su2LabelFun, StandardModel.su2Label, StandardModel.su3Label_apply, StandardModel.su2Label_apply, StandardModel.gellMannMatrix_eq_matrix, StandardModel.pauliMatrix_inr_eq_matrix
statement: formalized
proof: formalized
---

# Families of adjoint components and their invariants

The module `PhyslibAlpha.Particles.StandardModel.GaugeGroup.Invariants.Adjoint`, [PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean): 33 declarations, 33 with a docstring; 1 private, not shown.

> Families of components with colour or isospin adjoint indices, and the trace contraction their
> invariants reduce to.

## i. Overview

> The Standard Model labels the adjoint indices of `su(3)` by the eight Gell-Mann matrices
> `gellMannMatrix`, and those of `su(2)` by the three Pauli matrices, and moves them by the adjoint
> matrices `su3AdjointMatrix` and `su2AdjointMatrix`. These are the generalized Gell-Mann matrices
> `GellMann.matrix` of
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.SU.GellMann` for `N = 3` and
> `N = 2` under a relabelling, `su3Label` and `su2Label`, and the adjoint matrices are the matrices
> of the adjoint action in those bases (A).
>
> A family with one adjoint index has no invariant in its span, and a family with two adjoint
> indices of the same factor has its invariants reduced to the trace contraction `∑ a, T ![a, a]`
> (C for colour, D for isospin). These are the invariant tensors of `SuT[N, .adj]` and
> `SuT[N, .adj, .adj]` of
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.SU.Invariants.AdjUnit`, read on
> the components through the relabellings `relabelAdjIdx` and `relabelAdjPairIdx` of B. The lemmas
> of each family live in a namespace named after its representation, `ColourAdj`, `ColourAdjAdj`,
> `IsospinAdj` and `IsospinAdjAdj`.
>
> The hypercharge factor is abelian, so its adjoint action on `u(1)` is trivial: a family with two
> `u(1)` adjoint indices is moved by a hypercharge rotation not at all, and its trace contraction,
> its one component, is fixed by every map that fixes the components (E).

## ii. Key results

> - `StandardModel.su3Label`, `StandardModel.su2Label` : the Gell-Mann and Pauli labels as
>   generalized Gell-Mann labels.
> - `StandardModel.ColourAdj.reducesInvariantsTo_bot` : one colour adjoint index carries no
>   invariant, and its isospin twin.
> - `StandardModel.ColourAdjAdj.reducesInvariantsTo_span_traceContraction` : two colour adjoint
>   indices reduce to the trace contraction, and its isospin twin.

## iv. References

> * None.

## A. The Gell-Mann labels

> The Gell-Mann and Pauli matrices are the generalized Gell-Mann matrices up to a relabelling, so
> the Standard Model adjoint matrices are the matrices of the adjoint action.

**`StandardModel.su3LabelFun`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L82).

> The labels of the Gell-Mann matrices of `su(3)` as generalized Gell-Mann labels. They are the
> symmetric and antisymmetric matrices of the planes `(0, 1)`, `(0, 2)` and `(1, 2)`, and the two
> diagonal matrices.

```lean
def su3LabelFun : Fin 8 → GellMann.Index 3
```

**`StandardModel.su3Label`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L93).

> The relabelling of the Gell-Mann matrices of `su(3)` by generalized Gell-Mann labels.

```lean
noncomputable def su3Label : Fin 8 ≃ GellMann.Index 3
```

**`StandardModel.su2LabelFun`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L97).

> The labels of the Pauli matrices of `su(2)` as generalized Gell-Mann labels.

```lean
def su2LabelFun : Fin 3 → GellMann.Index 2
```

**`StandardModel.su2Label`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L103).

> The relabelling of the Pauli matrices of `su(2)` by generalized Gell-Mann labels.

```lean
noncomputable def su2Label : Fin 3 ≃ GellMann.Index 2
```

**`StandardModel.su3Label_apply`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L108).

> The relabelling of the Gell-Mann matrices is `su3LabelFun`.

```lean
lemma su3Label_apply (a : Fin 8) : su3Label a = su3LabelFun a
```

**`StandardModel.su2Label_apply`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L112).

> The relabelling of the Pauli matrices is `su2LabelFun`.

```lean
lemma su2Label_apply (i : Fin 3) : su2Label i = su2LabelFun i
```

**`StandardModel.gellMannMatrix_eq_matrix`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L115).

> The Gell-Mann matrices of `su(3)` are the generalized Gell-Mann matrices.

```lean
lemma gellMannMatrix_eq_matrix (a : Fin 8) :
    gellMannMatrix a = GellMann.matrix (su3Label a)
```

**`StandardModel.pauliMatrix_inr_eq_matrix`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L128).

> The Pauli matrices are the generalized Gell-Mann matrices of `su(2)`.

```lean
lemma pauliMatrix_inr_eq_matrix (i : Fin 3) :
    pauliMatrix (Sum.inr i) = GellMann.matrix (su2Label i)
```

**`StandardModel.su3AdjointMatrix_eq_adjMatrix`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L146).

> The adjoint matrix of `SU(3)` is the matrix of the adjoint action in the Gell-Mann
> basis.

```lean
lemma su3AdjointMatrix_eq_adjMatrix (U : SU 3) (a b : Fin 8) :
    ((su3AdjointMatrix U a b : ℝ) : ℂ) = adjMatrix U (su3Label a) (su3Label b)
```

**`StandardModel.su2AdjointMatrix_eq_adjMatrix`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L153).

> The adjoint matrix of `SU(2)` is the matrix of the adjoint action in the Pauli basis.

```lean
lemma su2AdjointMatrix_eq_adjMatrix (U : SU 2) (i j : Fin 3) :
    ((su2AdjointMatrix U i j : ℝ) : ℂ) = adjMatrix U (su2Label i) (su2Label j)
```

## B. Relabelled adjoint families

> A family indexed by the Standard Model labels of the adjoint index and moved by the Standard Model
> adjoint matrices is, after relabelling, a family moved by the matrices of the adjoint action.

**`StandardModel.relabelAdjIdx`**, a def, [line 175](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L175).

> The component indices of a tensor with one adjoint index of `SU(N)`, as a label in `ι`
> through the relabelling `e` of the Gell-Mann labels.

```lean
noncomputable def relabelAdjIdx : ComponentIdx (S := suTensor N) ![.adj] ≃ ι
```

**`StandardModel.relabelAdjPairIdx`**, a def, [line 180](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L180).

> The component indices of a tensor with two adjoint indices of `SU(N)`, as a pair of labels in
> `ι` through the relabelling `e` of the Gell-Mann labels.

```lean
noncomputable def relabelAdjPairIdx : ComponentIdx (S := suTensor N) ![.adj, .adj] ≃ (Fin 2 → ι)
```

**`StandardModel.liftComponents_relabelAdj_smul_of_law`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L188).

> A linear map moving a family with one adjoint label by the Standard Model adjoint matrix of
> `U` intertwines the map of the relabelled family with the action of `U`.

```lean
lemma liftComponents_relabelAdj_smul_of_law (T : ι → B) {f : B →ₗ[ℂ] B} {U : SU N}
    (hf : ∀ l, f (T l) = ∑ a, ((M U a l : ℝ) : ℂ) • T a) (t : SuT[N, .adj]) :
    f (liftComponents (T ∘ relabelAdjIdx e) t) = liftComponents (T ∘ relabelAdjIdx e) (U • t)
```

**`StandardModel.liftComponents_relabelAdjPair_smul_of_law`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L198).

> A linear map moving a family with two adjoint labels by the Standard Model adjoint matrix of
> `U` on each label intertwines the map of the relabelled family with the action of `U`.

```lean
lemma liftComponents_relabelAdjPair_smul_of_law (T : (Fin 2 → ι) → B) {f : B →ₗ[ℂ] B} {U : SU N}
    (hf : ∀ l, f (T l) = ∑ a : Fin 2 → ι, (∏ i : Fin 2, ((M U (a i) (l i) : ℝ) : ℂ)) • T a)
    (t : SuT[N, .adj, .adj]) :
    f (liftComponents (T ∘ relabelAdjPairIdx e) t)
      = liftComponents (T ∘ relabelAdjPairIdx e) (U • t)
```

**`StandardModel.liftComponents_relabelAdjPair_two_smul_adjUnitTensor`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L210).

> The map of the relabelled family sends twice the unit tensor to the trace contraction.

```lean
lemma liftComponents_relabelAdjPair_two_smul_adjUnitTensor (T : (Fin 2 → ι) → B) :
    liftComponents (T ∘ relabelAdjPairIdx e) ((2 : ℂ) • adjUnitTensor N) = ∑ a : ι, T ![a, a]
```

## C. The colour adjoint families

> A family with one colour adjoint index has no invariant, and one with two has the trace
> contraction alone.

**`StandardModel.ColourAdj.of_law`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L238).

> A family `T^a` with one `su(3)` adjoint index: when every colour rotation `U` moves its
> members by the adjoint matrix of `U`, the summed index first, the map of the relabelled family
> out of the tensors of `SU(3)` is equivariant for the colour factor of the gauge group.

```lean
lemma of_law (hT : ∀ (U : SU 3) (l : Fin 8),
    repGauge (U, 1, 1) (T l) = ∑ a : Fin 8, ((su3AdjointMatrix U a l : ℝ) : ℂ) • T a) :
    (suTensor 3).IsEquivariant ![.adj] (repGauge.comp GaugeGroupI.ofSU3)
      (liftComponents (T ∘ relabelAdjIdx su3Label))
```

**`StandardModel.ColourAdj.isStableUnder_span`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L246).

> The span of the components is stable under the colour factor.

```lean
lemma isStableUnder_span
    (hT : (suTensor 3).IsEquivariant ![.adj] (repGauge.comp GaugeGroupI.ofSU3)
      (liftComponents (T ∘ relabelAdjIdx su3Label))) :
    IsStableUnder (fun U : SU 3 => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T))
```

**`StandardModel.ColourAdj.reducesInvariantsTo_bot`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L256).

> A colour invariant of the span of the components joined with a stable submodule lies in
> that submodule. An adjoint index contributes nothing to the invariants.

```lean
lemma reducesInvariantsTo_bot
    (hT : (suTensor 3).IsEquivariant ![.adj] (repGauge.comp GaugeGroupI.ofSU3)
      (liftComponents (T ∘ relabelAdjIdx su3Label))) :
    ReducesInvariantsTo (fun U : SU 3 => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T)) ⊥
```

**`StandardModel.ColourAdjAdj.of_law`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L274).

> A family `T^{ab}` with two `su(3)` adjoint indices: when every colour rotation `U` moves its
> members by one factor of the adjoint matrix of `U` per index, the summed index first, the map
> of the relabelled family out of the tensors of `SU(3)` is equivariant for the colour factor of
> the gauge group.

```lean
lemma of_law (hT : ∀ (U : SU 3) (l : Fin 2 → Fin 8), repGauge (U, 1, 1) (T l)
    = ∑ a : Fin 2 → Fin 8, (∏ i : Fin 2, ((su3AdjointMatrix U (a i) (l i) : ℝ) : ℂ)) • T a) :
    (suTensor 3).IsEquivariant ![.adj, .adj] (repGauge.comp GaugeGroupI.ofSU3)
      (liftComponents (T ∘ relabelAdjPairIdx su3Label))
```

**`StandardModel.ColourAdjAdj.traceContraction`**, a def, [line 282](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L282).

> The trace contraction `∑ a, T ![a, a]` of the two adjoint indices.

```lean
def traceContraction (T : (Fin 2 → Fin 8) → B) : B
```

**`StandardModel.ColourAdjAdj.map_traceContraction`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L286).

> Any map moving the components by the adjoint matrix of an element of `SU(3)` fixes the
> trace contraction.

```lean
lemma map_traceContraction {U : SU 3} {f : B →ₗ[ℂ] B} (hf : ∀ l : Fin 2 → Fin 8, f (T l)
    = ∑ a : Fin 2 → Fin 8, (∏ i : Fin 2, ((su3AdjointMatrix U (a i) (l i) : ℝ) : ℂ)) • T a) :
    f (traceContraction T) = traceContraction T
```

**`StandardModel.ColourAdjAdj.isStableUnder_span`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L294).

> The span of the components is stable under the colour factor.

```lean
lemma isStableUnder_span
    (hT : (suTensor 3).IsEquivariant ![.adj, .adj] (repGauge.comp GaugeGroupI.ofSU3)
      (liftComponents (T ∘ relabelAdjPairIdx su3Label))) :
    IsStableUnder (fun U : SU 3 => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T))
```

**`StandardModel.ColourAdjAdj.reducesInvariantsTo_span_traceContraction`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L304).

> The colour invariants of the span of the components reduce to the line through the trace
> contraction.

```lean
lemma reducesInvariantsTo_span_traceContraction
    (hT : (suTensor 3).IsEquivariant ![.adj, .adj] (repGauge.comp GaugeGroupI.ofSU3)
      (liftComponents (T ∘ relabelAdjPairIdx su3Label))) :
    ReducesInvariantsTo (fun U : SU 3 => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T)) (ℂ ∙ traceContraction T)
```

## D. The isospin adjoint families

> The isospin twins of the families of section C.

**`StandardModel.IsospinAdj.of_law`**, a lemma, [line 331](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L331).

> A family `T^a` with one `su(2)` adjoint index: when every isospin rotation `U` moves its
> members by the adjoint matrix of `U`, the summed index first, the map of the relabelled family
> out of the tensors of `SU(2)` is equivariant for the isospin factor of the gauge group.

```lean
lemma of_law (hT : ∀ (U : SU 2) (l : Fin 3),
    repGauge (1, U, 1) (T l) = ∑ a : Fin 3, ((su2AdjointMatrix U a l : ℝ) : ℂ) • T a) :
    (suTensor 2).IsEquivariant ![.adj] (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents (T ∘ relabelAdjIdx su2Label))
```

**`StandardModel.IsospinAdj.isStableUnder_span`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L339).

> The span of the components is stable under the isospin factor.

```lean
lemma isStableUnder_span
    (hT : (suTensor 2).IsEquivariant ![.adj] (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents (T ∘ relabelAdjIdx su2Label))) :
    IsStableUnder (fun U : SU 2 => repGauge ((1, U, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T))
```

**`StandardModel.IsospinAdj.reducesInvariantsTo_bot`**, a lemma, [line 349](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L349).

> An isospin invariant of the span of the components joined with a stable submodule lies in
> that submodule. An adjoint index contributes nothing to the invariants.

```lean
lemma reducesInvariantsTo_bot
    (hT : (suTensor 2).IsEquivariant ![.adj] (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents (T ∘ relabelAdjIdx su2Label))) :
    ReducesInvariantsTo (fun U : SU 2 => repGauge ((1, U, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T)) ⊥
```

**`StandardModel.IsospinAdjAdj.of_law`**, a lemma, [line 367](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L367).

> A family `T^{ab}` with two `su(2)` adjoint indices: when every isospin rotation `U` moves its
> members by one factor of the adjoint matrix of `U` per index, the summed index first, the map
> of the relabelled family out of the tensors of `SU(2)` is equivariant for the isospin factor of
> the gauge group.

```lean
lemma of_law (hT : ∀ (U : SU 2) (l : Fin 2 → Fin 3), repGauge (1, U, 1) (T l)
    = ∑ a : Fin 2 → Fin 3, (∏ i : Fin 2, ((su2AdjointMatrix U (a i) (l i) : ℝ) : ℂ)) • T a) :
    (suTensor 2).IsEquivariant ![.adj, .adj] (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents (T ∘ relabelAdjPairIdx su2Label))
```

**`StandardModel.IsospinAdjAdj.traceContraction`**, a def, [line 375](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L375).

> The trace contraction `∑ a, T ![a, a]` of the two adjoint indices.

```lean
def traceContraction (T : (Fin 2 → Fin 3) → B) : B
```

**`StandardModel.IsospinAdjAdj.map_traceContraction`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L379).

> Any map moving the components by the adjoint matrix of an element of `SU(2)` fixes the
> trace contraction.

```lean
lemma map_traceContraction {U : SU 2} {f : B →ₗ[ℂ] B} (hf : ∀ l : Fin 2 → Fin 3, f (T l)
    = ∑ a : Fin 2 → Fin 3, (∏ i : Fin 2, ((su2AdjointMatrix U (a i) (l i) : ℝ) : ℂ)) • T a) :
    f (traceContraction T) = traceContraction T
```

**`StandardModel.IsospinAdjAdj.isStableUnder_span`**, a lemma, [line 387](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L387).

> The span of the components is stable under the isospin factor.

```lean
lemma isStableUnder_span
    (hT : (suTensor 2).IsEquivariant ![.adj, .adj] (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents (T ∘ relabelAdjPairIdx su2Label))) :
    IsStableUnder (fun U : SU 2 => repGauge ((1, U, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T))
```

**`StandardModel.IsospinAdjAdj.reducesInvariantsTo_span_traceContraction`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L397).

> The isospin invariants of the span of the components reduce to the line through the trace
> contraction.

```lean
lemma reducesInvariantsTo_span_traceContraction
    (hT : (suTensor 2).IsEquivariant ![.adj, .adj] (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents (T ∘ relabelAdjPairIdx su2Label))) :
    ReducesInvariantsTo (fun U : SU 2 => repGauge ((1, U, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T)) (ℂ ∙ traceContraction T)
```

## E. The hypercharge adjoint families

> The hypercharge factor is abelian, so its adjoint action on `u(1)` is trivial, and there is no
> tensor species to relabel. A family `T : (Fin 2 → Fin 1) → B` with two `u(1)` adjoint indices is
> moved by a hypercharge rotation by one factor of the `1 × 1` adjoint matrix `1` per index, which is
> to say not at all, so its law is stated directly as `∀ l, f (T l) = T l`. The trace contraction
> is the one component of the family, and every map fixing the components fixes it.

**`StandardModel.HyperchargeAdjAdj.traceContraction`**, a def, [line 425](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L425).

> The trace contraction: the Kronecker contraction of the two `u(1)` indices, which is the one
> component of the family.

```lean
def traceContraction (T : (Fin 2 → Fin 1) → B) : B
```

**`StandardModel.HyperchargeAdjAdj.map_traceContraction`**, a lemma, [line 428](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean#L428).

> Any map fixing the components fixes the trace contraction.

```lean
lemma map_traceContraction {T : (Fin 2 → Fin 1) → B} {f : B →ₗ[ℂ] B}
    (hf : ∀ l : Fin 2 → Fin 1, f (T l) = T l) :
    f (traceContraction T) = traceContraction T
```

## Depends on

- [The unit tensor of the adjoint colour of `SU(N)`](../../../classicalfieldtheory/gaugetheory/part-03/globalgaugegroup-su-invariants-adjunit.md)
- [The adjoint matrices of `SU(2)` and `SU(3)`](gaugegroup-adjointmatrix.md)
- [Families of colour and isospin components and their invariants](gaugegroup-invariants-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Adjoint.lean)
