---
declaration: module
origin: cited
lean: StandardModel.GaugeGroupI.ofSU3, StandardModel.GaugeGroupI.ofSU2, StandardModel.GaugeGroupI.ofSU3_apply, StandardModel.GaugeGroupI.ofSU2_apply, StandardModel.Family.sum_pi_two, StandardModel.IsSU3FundamentalAntiFundamentalMat, StandardModel.IsSU3FundamentalAntiFundamental, StandardModel.IsSU2FundamentalAntiFundamentalMat
statement: formalized
proof: formalized
---

# Families of colour and isospin components and their invariants

The module `PhyslibAlpha.Particles.StandardModel.GaugeGroup.Invariants.Basic`, [PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean): 48 declarations, 42 with a docstring.

## i. Overview

> The invariant tensors of `SU(N)` are classified in `LocalGaugeData.SU.Invariants`, for
> equivariant maps out of the tensors of `suTensor N`. Here those results are applied to the
> Standard Model. A family `T : ι → B` of components, indexed by colour or isospin labels and moved
> by the colour factor `repGauge (U, 1, 1)` or the isospin factor `repGauge (1, V, 1)` of the gauge
> group, is turned into a linear map out of the tensors of `SU(3)` or `SU(2)`, and its transformation
> law is exactly the equivariance of that map (A).
>
> A law is named by how the members of the family move as vectors of `B`. Under a fundamental law
> `f (T l) = ∑ a, U a l • T a`, so `T l` moves like the standard basis vector `e_l` of `ℂⁿ`; an
> anti-fundamental law has `conj U` in place of `U`. The component symbols of a field are values of
> an equivariant map on dual vectors, so they obey the dual of the field's law: the symbols of a
> doublet or triplet field form an anti-fundamental family, and those of its conjugate a fundamental
> one.
>
> For a family with a fundamental and an anti-fundamental index the invariants reduce to the delta
> contraction (B). For two fundamental or two anti-fundamental indices of `SU(2)` they reduce to the
> epsilon contraction (C), and for four fundamental indices of `SU(2)` to the two epsilon pairings
> (D). The contractions are written out on the components, and the maps `…Mat` record the laws a
> single linear map obeys, for the reductions over the whole gauge group.

## ii. Key results

> - `StandardModel.IsSU3FundamentalAntiFundamental.invariantReductionToSpan` : the colour invariants
>   of a family with one fundamental and one anti-fundamental colour index.
> - `StandardModel.IsSU2FundamentalAntiFundamental.invariantReductionToSpan` : its isospin twin.
> - `StandardModel.IsSU2BiFundamental.invariantReductionToSpan`,
>   `StandardModel.IsSU2BiAntiFundamental.invariantReductionToSpan` : two isospin indices of the
>   same kind.
> - `StandardModel.IsSU2QuadFundamental.reducesInvariantsTo_span_epsilonContractions` : four
>   fundamental isospin indices.

## iv. References

> * None.

## A. The factors of the gauge group

**`StandardModel.GaugeGroupI.ofSU3`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L73).

> The colour factor `SU(3)` of the gauge group.

```lean
def GaugeGroupI.ofSU3 : SU 3 →* GaugeGroupI
```

**`StandardModel.GaugeGroupI.ofSU2`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L76).

> The isospin factor `SU(2)` of the gauge group.

```lean
def GaugeGroupI.ofSU2 : SU 2 →* GaugeGroupI
```

**`StandardModel.GaugeGroupI.ofSU3_apply`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L79).

```lean
lemma GaugeGroupI.ofSU3_apply (U : SU 3) : GaugeGroupI.ofSU3 U = (U, 1, 1)
```

**`StandardModel.GaugeGroupI.ofSU2_apply`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L82).

```lean
lemma GaugeGroupI.ofSU2_apply (V : SU 2) : GaugeGroupI.ofSU2 V = (1, V, 1)
```

**`StandardModel.Family.sum_pi_two`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L87).

> A sum over pairs of indices is a double sum.

```lean
lemma sum_pi_two {n : ℕ} {M : Type*} [AddCommMonoid M] (F : (Fin 2 → Fin n) → M) :
    ∑ d : Fin 2 → Fin n, F d = ∑ x : Fin n, ∑ y : Fin n, F ![x, y]
```

## B. One fundamental and one anti-fundamental index

**`StandardModel.IsSU3FundamentalAntiFundamentalMat`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L104).

> The linear map `f` moves the components of `T` as `U ∈ SU(3)` moves a tensor with one
> fundamental and one anti-fundamental index: a factor of `U` for the first index and a factor of
> `conj U` for the second, the summed index first.

```lean
def IsSU3FundamentalAntiFundamentalMat (U : SU 3) (f : B →ₗ[ℂ] B) (T : (Fin 2 → Fin 3) → B) :
    Prop
```

**`StandardModel.IsSU3FundamentalAntiFundamental`**, an abbrev, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L111).

> A family `T^a{}_b` with one fundamental and one anti-fundamental colour index: its map out of
> the tensors of `SU(3)` is equivariant for the colour factor of the gauge group.

```lean
abbrev IsSU3FundamentalAntiFundamental (B : Type*) [AddCommGroup B] [Module ℂ B]
    (repGauge : Representation ℂ GaugeGroupI B) (T : (Fin 2 → Fin 3) → B) : Prop
```

**`StandardModel.IsSU2FundamentalAntiFundamentalMat`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L118).

> The linear map `f` moves the components of `T` as `V ∈ SU(2)` moves a tensor with one
> fundamental and one anti-fundamental index.

```lean
def IsSU2FundamentalAntiFundamentalMat (V : SU 2) (f : B →ₗ[ℂ] B) (T : (Fin 2 → Fin 2) → B) :
    Prop
```

**`StandardModel.IsSU2FundamentalAntiFundamental`**, an abbrev, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L125).

> A family `T^a{}_b` with one fundamental and one anti-fundamental isospin index: its map out
> of the tensors of `SU(2)` is equivariant for the isospin factor of the gauge group.

```lean
abbrev IsSU2FundamentalAntiFundamental (B : Type*) [AddCommGroup B] [Module ℂ B]
    (repGauge : Representation ℂ GaugeGroupI B) (T : (Fin 2 → Fin 2) → B) : Prop
```

**`StandardModel.IsSU3FundamentalAntiFundamental.of_law`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L135).

> A family obeying the law for every colour rotation is such a family.

```lean
lemma of_law (hT : ∀ U : SU 3, IsSU3FundamentalAntiFundamentalMat U (repGauge (U, 1, 1)) T) :
    IsSU3FundamentalAntiFundamental B repGauge T
```

**`StandardModel.IsSU3FundamentalAntiFundamental.sum`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L140).

> A finite sum of such families is such a family.

```lean
lemma sum {ι : Type} [Fintype ι] {T : ι → (Fin 2 → Fin 3) → B}
    (hT : ∀ i, IsSU3FundamentalAntiFundamental B repGauge (T i)) :
    IsSU3FundamentalAntiFundamental B repGauge (fun l => ∑ i, T i l)
```

**`StandardModel.IsSU3FundamentalAntiFundamental.deltaContraction`**, a def, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L147).

> The delta contraction `∑ a, T ![a, a]`.

```lean
def deltaContraction (T : (Fin 2 → Fin 3) → B) : B
```

**`StandardModel.IsSU3FundamentalAntiFundamental.deltaContraction_mem_span`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L149).

```lean
lemma deltaContraction_mem_span (T : (Fin 2 → Fin 3) → B) :
    deltaContraction T ∈ Submodule.span ℂ (Set.range T)
```

**`StandardModel.IsSU3FundamentalAntiFundamental.map_deltaContraction`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L154).

> Any map moving the components by an element of `SU(3)` fixes the delta contraction.

```lean
lemma map_deltaContraction {U : SU 3} {f : B →ₗ[ℂ] B}
    (hf : IsSU3FundamentalAntiFundamentalMat U f T) :
    f (deltaContraction T) = deltaContraction T
```

**`StandardModel.IsSU3FundamentalAntiFundamental.repGauge_deltaContraction`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L161).

> The delta contraction is colour invariant.

```lean
lemma repGauge_deltaContraction (hT : IsSU3FundamentalAntiFundamental B repGauge T)
    (U : SU 3) : repGauge (U, 1, 1) (deltaContraction T) = deltaContraction T
```

**`StandardModel.IsSU3FundamentalAntiFundamental.invariantReductionToSpan`**, a def, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L168).

> The colour invariants of the component span reduce to the span of the delta
> contraction.

```lean
noncomputable def invariantReductionToSpan (hT : IsSU3FundamentalAntiFundamental B repGauge T) :
    InvariantReductionToSpan (fun U : SU 3 => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T))
```

**`StandardModel.IsSU2FundamentalAntiFundamental.of_law`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L180).

> A family obeying the law for every isospin rotation is such a family.

```lean
lemma of_law (hT : ∀ V : SU 2, IsSU2FundamentalAntiFundamentalMat V (repGauge (1, V, 1)) T) :
    IsSU2FundamentalAntiFundamental B repGauge T
```

**`StandardModel.IsSU2FundamentalAntiFundamental.sum`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L185).

> A finite sum of such families is such a family.

```lean
lemma sum {ι : Type} [Fintype ι] {T : ι → (Fin 2 → Fin 2) → B}
    (hT : ∀ i, IsSU2FundamentalAntiFundamental B repGauge (T i)) :
    IsSU2FundamentalAntiFundamental B repGauge (fun l => ∑ i, T i l)
```

**`StandardModel.IsSU2FundamentalAntiFundamental.deltaContraction`**, a def, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L192).

> The delta contraction `T ![0, 0] + T ![1, 1]`.

```lean
def deltaContraction (T : (Fin 2 → Fin 2) → B) : B
```

**`StandardModel.IsSU2FundamentalAntiFundamental.deltaContraction_eq_sum`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L195).

```lean
lemma deltaContraction_eq_sum (T : (Fin 2 → Fin 2) → B) :
    deltaContraction T = ∑ a : Fin 2, T ![a, a]
```

**`StandardModel.IsSU2FundamentalAntiFundamental.deltaContraction_mem_span`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L199).

```lean
lemma deltaContraction_mem_span (T : (Fin 2 → Fin 2) → B) :
    deltaContraction T ∈ Submodule.span ℂ (Set.range T)
```

**`StandardModel.IsSU2FundamentalAntiFundamental.map_deltaContraction`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L204).

> Any map moving the components by an element of `SU(2)` fixes the delta contraction.

```lean
lemma map_deltaContraction {V : SU 2} {f : B →ₗ[ℂ] B}
    (hf : IsSU2FundamentalAntiFundamentalMat V f T) :
    f (deltaContraction T) = deltaContraction T
```

**`StandardModel.IsSU2FundamentalAntiFundamental.repGauge_deltaContraction`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L211).

> The delta contraction is isospin invariant.

```lean
lemma repGauge_deltaContraction (hT : IsSU2FundamentalAntiFundamental B repGauge T)
    (V : SU 2) : repGauge (1, V, 1) (deltaContraction T) = deltaContraction T
```

**`StandardModel.IsSU2FundamentalAntiFundamental.invariantReductionToSpan`**, a def, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L218).

> The isospin invariants of the component span reduce to the span of the delta
> contraction.

```lean
noncomputable def invariantReductionToSpan (hT : IsSU2FundamentalAntiFundamental B repGauge T) :
    InvariantReductionToSpan (fun V : SU 2 => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T))
```

**`StandardModel.IsSU2FundamentalAntiFundamental.reducesInvariantsTo_span_deltaContraction`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L227).

> The isospin invariants of the component span reduce to the line through the delta
> contraction.

```lean
lemma reducesInvariantsTo_span_deltaContraction
    (hT : IsSU2FundamentalAntiFundamental B repGauge T) :
    ReducesInvariantsTo (fun V : SU 2 => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T)) (ℂ ∙ deltaContraction T)
```

## C. Two isospin indices of the same kind

**`StandardModel.IsSU2BiFundamentalMat`**, a def, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L243).

> The linear map `f` moves the components of `T` as `V ∈ SU(2)` moves a tensor with two
> fundamental indices: one factor of `V` per index.

```lean
def IsSU2BiFundamentalMat (V : SU 2) (f : B →ₗ[ℂ] B) (T : (Fin 2 → Fin 2) → B) : Prop
```

**`StandardModel.IsSU2BiAntiFundamentalMat`**, a def, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L248).

> The linear map `f` moves the components of `T` as `V ∈ SU(2)` moves a tensor with two
> anti-fundamental indices: one factor of `conj V` per index.

```lean
def IsSU2BiAntiFundamentalMat (V : SU 2) (f : B →ₗ[ℂ] B) (T : (Fin 2 → Fin 2) → B) : Prop
```

**`StandardModel.IsSU2BiFundamental`**, an abbrev, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L254).

> A family `T^{ab}` with two fundamental isospin indices: its map out of the tensors of `SU(2)`
> is equivariant for the isospin factor of the gauge group.

```lean
abbrev IsSU2BiFundamental (B : Type*) [AddCommGroup B] [Module ℂ B]
    (repGauge : Representation ℂ GaugeGroupI B) (T : (Fin 2 → Fin 2) → B) : Prop
```

**`StandardModel.IsSU2BiAntiFundamental`**, an abbrev, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L260).

> A family `T_{ab}` with two anti-fundamental isospin indices: its map out of the tensors of
> `SU(2)` is equivariant for the isospin factor of the gauge group.

```lean
abbrev IsSU2BiAntiFundamental (B : Type*) [AddCommGroup B] [Module ℂ B]
    (repGauge : Representation ℂ GaugeGroupI B) (T : (Fin 2 → Fin 2) → B) : Prop
```

**`StandardModel.IsSU2BiFundamental.of_law`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L270).

> A family obeying the law for every isospin rotation is such a family.

```lean
lemma of_law (hT : ∀ V : SU 2, IsSU2BiFundamentalMat V (repGauge (1, V, 1)) T) :
    IsSU2BiFundamental B repGauge T
```

**`StandardModel.IsSU2BiFundamental.sum`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L275).

> A finite sum of such families is such a family.

```lean
lemma sum {ι : Type} [Fintype ι] {T : ι → (Fin 2 → Fin 2) → B}
    (hT : ∀ i, IsSU2BiFundamental B repGauge (T i)) :
    IsSU2BiFundamental B repGauge (fun l => ∑ i, T i l)
```

**`StandardModel.IsSU2BiFundamental.epsilonContraction`**, a def, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L282).

> The epsilon contraction `T ![0, 1] - T ![1, 0]`.

```lean
def epsilonContraction (T : (Fin 2 → Fin 2) → B) : B
```

**`StandardModel.IsSU2BiFundamental.epsilonContraction_mem_span`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L284).

```lean
lemma epsilonContraction_mem_span (T : (Fin 2 → Fin 2) → B) :
    epsilonContraction T ∈ Submodule.span ℂ (Set.range T)
```

**`StandardModel.IsSU2BiFundamental.map_epsilonContraction`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L289).

> Any map moving the components by an element of `SU(2)` fixes the epsilon contraction.

```lean
lemma map_epsilonContraction {V : SU 2} {f : B →ₗ[ℂ] B} (hf : IsSU2BiFundamentalMat V f T) :
    f (epsilonContraction T) = epsilonContraction T
```

**`StandardModel.IsSU2BiFundamental.repGauge_epsilonContraction`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L295).

> The epsilon contraction is isospin invariant.

```lean
lemma repGauge_epsilonContraction (hT : IsSU2BiFundamental B repGauge T) (V : SU 2) :
    repGauge (1, V, 1) (epsilonContraction T) = epsilonContraction T
```

**`StandardModel.IsSU2BiFundamental.invariantReductionToSpan`**, a def, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L302).

> The isospin invariants of the component span reduce to the span of the epsilon
> contraction.

```lean
noncomputable def invariantReductionToSpan (hT : IsSU2BiFundamental B repGauge T) :
    InvariantReductionToSpan (fun V : SU 2 => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T))
```

**`StandardModel.IsSU2BiAntiFundamental.of_law`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L314).

> A family obeying the law for every isospin rotation is such a family.

```lean
lemma of_law (hT : ∀ V : SU 2, IsSU2BiAntiFundamentalMat V (repGauge (1, V, 1)) T) :
    IsSU2BiAntiFundamental B repGauge T
```

**`StandardModel.IsSU2BiAntiFundamental.sum`**, a lemma, [line 320](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L320).

> A finite sum of such families is such a family.

```lean
lemma sum {ι : Type} [Fintype ι] {T : ι → (Fin 2 → Fin 2) → B}
    (hT : ∀ i, IsSU2BiAntiFundamental B repGauge (T i)) :
    IsSU2BiAntiFundamental B repGauge (fun l => ∑ i, T i l)
```

**`StandardModel.IsSU2BiAntiFundamental.map_epsilonContraction`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L328).

> Any map moving the components by an element of `SU(2)` in the anti-fundamental fixes the
> epsilon contraction.

```lean
lemma map_epsilonContraction {V : SU 2} {f : B →ₗ[ℂ] B} (hf : IsSU2BiAntiFundamentalMat V f T) :
    f (IsSU2BiFundamental.epsilonContraction T) = IsSU2BiFundamental.epsilonContraction T
```

**`StandardModel.IsSU2BiAntiFundamental.repGauge_epsilonContraction`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L335).

> The epsilon contraction is isospin invariant.

```lean
lemma repGauge_epsilonContraction (hT : IsSU2BiAntiFundamental B repGauge T) (V : SU 2) :
    repGauge (1, V, 1) (IsSU2BiFundamental.epsilonContraction T)
      = IsSU2BiFundamental.epsilonContraction T
```

**`StandardModel.IsSU2BiAntiFundamental.invariantReductionToSpan`**, a def, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L343).

> The isospin invariants of the component span reduce to the span of the epsilon
> contraction.

```lean
noncomputable def invariantReductionToSpan (hT : IsSU2BiAntiFundamental B repGauge T) :
    InvariantReductionToSpan (fun V : SU 2 => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T))
```

## D. Four fundamental isospin indices

**`StandardModel.IsSU2QuadFundamentalMat`**, a def, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L358).

> The linear map `f` moves the components of `T` as `V ∈ SU(2)` moves a tensor with four
> fundamental indices: one factor of `V` per index.

```lean
def IsSU2QuadFundamentalMat (V : SU 2) (f : B →ₗ[ℂ] B) (T : (Fin 4 → Fin 2) → B) : Prop
```

**`StandardModel.IsSU2QuadFundamental`**, an abbrev, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L363).

> A family `T^{abcd}` with four fundamental isospin indices: its map out of the tensors of
> `SU(2)` is equivariant for the isospin factor of the gauge group.

```lean
abbrev IsSU2QuadFundamental (B : Type*) [AddCommGroup B] [Module ℂ B]
    (repGauge : Representation ℂ GaugeGroupI B) (T : (Fin 4 → Fin 2) → B) : Prop
```

**`StandardModel.IsSU2QuadFundamental.of_law`**, a lemma, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L372).

> A family obeying the law for every isospin rotation is such a family.

```lean
lemma of_law (hT : ∀ V : SU 2, IsSU2QuadFundamentalMat V (repGauge (1, V, 1)) T) :
    IsSU2QuadFundamental B repGauge T
```

**`StandardModel.IsSU2QuadFundamental.sum_pi_four`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L377).

> A sum over families of four fundamental indices is a fourfold sum.

```lean
lemma sum_pi_four {M : Type*} [AddCommMonoid M] (F : (Fin 4 → Fin 2) → M) :
    ∑ d : Fin 4 → Fin 2, F d
      = ∑ x : Fin 2, ∑ y : Fin 2, ∑ z : Fin 2, ∑ w : Fin 2, F ![x, y, z, w]
```

**`StandardModel.IsSU2QuadFundamental.epsilonContraction₁₂`**, a def, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L384).

> The contraction pairing the first index with the second and the third with the
> fourth.

```lean
def epsilonContraction₁₂ (T : (Fin 4 → Fin 2) → B) : B
```

**`StandardModel.IsSU2QuadFundamental.epsilonContraction₁₃`**, a def, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L389).

> The contraction pairing the first index with the third and the second with the
> fourth.

```lean
def epsilonContraction₁₃ (T : (Fin 4 → Fin 2) → B) : B
```

**`StandardModel.IsSU2QuadFundamental.reducesInvariantsTo_span_epsilonContractions`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L394).

> The isospin invariants of the component span reduce to the span of the two epsilon
> contractions.

```lean
lemma reducesInvariantsTo_span_epsilonContractions (hT : IsSU2QuadFundamental B repGauge T) :
    ReducesInvariantsTo (fun V : SU 2 => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T))
      (Submodule.span ℂ {epsilonContraction₁₂ T, epsilonContraction₁₃ T})
```

## Depends on

- [The Standard Model Gauge Group](../../../../physlib/particles/standardmodel/gaugegroup/basic.md)
- [Invariants of two fundamental or two anti-fundamental indices of `SU(N)`](../../../classicalfieldtheory/gaugetheory/part-05/localgaugedata-su-invariants-bifund.md)
- [Invariants of a fundamental and an anti-fundamental index of `SU(N)`](../../../classicalfieldtheory/gaugetheory/part-05/localgaugedata-su-invariants-fundanti.md)

## Proof depends on

- [Invariants of four fundamental indices of `SU(2)`](../../../classicalfieldtheory/gaugetheory/part-05/localgaugedata-su-invariants-quadfund.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean)
