---
declaration: module
origin: cited
lean: StandardModel.GaugeGroupI.ofSU3, StandardModel.GaugeGroupI.ofSU2, StandardModel.GaugeGroupI.ofSU3_apply, StandardModel.GaugeGroupI.ofSU2_apply, StandardModel.ColourFundAntiFund.of_law, StandardModel.ColourFundAntiFund.sum, StandardModel.ColourFundAntiFund.deltaContraction, StandardModel.ColourFundAntiFund.deltaContraction_mem_span
statement: formalized
proof: formalized
---

# Families of colour and isospin components and their invariants

The module `PhyslibAlpha.Particles.StandardModel.GaugeGroup.Invariants.Basic`, [PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean): 35 declarations, 35 with a docstring.

> Families of components moved by the colour or isospin factor, and the contractions their invariants
> reduce to.

## i. Overview

> The invariant tensors of `SU(N)` are classified in `GlobalGaugeGroup.SU.Invariants`,
> for equivariant maps out of the tensors of `suTensor N`. Here those results are applied to the
> Standard Model. A family `T : ι → B` of components, indexed by colour or isospin labels and moved by
> the colour factor `repGauge (U, 1, 1)` or the isospin factor `repGauge (1, V, 1)` of the gauge
> group, is turned into the linear map `liftComponents` out of the tensors of `SU(3)` or `SU(2)` with
> an explicit list of colours, and its transformation law is exactly the equivariance of that map
> for the restriction of `repGauge` along the factor (A).
>
> A law is named by how the members of the family move as vectors of `B`. Under a fundamental law
> `f (T l) = ∑ a, U a l • T a`, so `T l` moves like the standard basis vector `e_l` of `ℂⁿ`; an
> anti-fundamental law has `conj U` in place of `U`. The component symbols of a field are values of
> an equivariant map on dual vectors, so they obey the dual of the field's law. The symbols of a
> doublet or triplet field form an anti-fundamental family, and those of its conjugate a fundamental
> one.
>
> For a family with a fundamental and an anti-fundamental index the invariants reduce to the delta
> contraction (B). For two fundamental or two anti-fundamental indices of `SU(2)` they reduce to the
> epsilon contraction (C), and for four fundamental indices of `SU(2)` to the two epsilon pairings
> (D). The contractions are written out on the components, and the lemmas `map_…Contraction` take
> the law a single linear map obeys, for the reductions over the whole gauge group. The lemmas of
> each family live in a namespace named after its representation, `ColourFundAntiFund`,
> `IsospinFundAntiFund`, `IsospinFundFund`, `IsospinAntiFundAntiFund` and `IsospinQuadFund`.

## ii. Key results

> - `StandardModel.ColourFundAntiFund.invariantReductionToSpan` : the colour invariants of a family
>   with one fundamental and one anti-fundamental colour index.
> - `StandardModel.IsospinFundAntiFund.invariantReductionToSpan` : its isospin twin.
> - `StandardModel.IsospinFundFund.invariantReductionToSpan`,
>   `StandardModel.IsospinAntiFundAntiFund.invariantReductionToSpan` : two isospin indices of the
>   same kind.
> - `StandardModel.IsospinQuadFund.reducesInvariantsTo_span_epsilonContractions` : four fundamental
>   isospin indices.

## iv. References

> * None.

## A. The factors of the gauge group

> The colour and isospin factors as homomorphisms into `GaugeGroupI`, along which the
> representation of the gauge group is restricted.

**`StandardModel.GaugeGroupI.ofSU3`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L82).

> The colour factor `SU(3)` of the gauge group.

```lean
def GaugeGroupI.ofSU3 : SU 3 →* GaugeGroupI
```

**`StandardModel.GaugeGroupI.ofSU2`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L85).

> The isospin factor `SU(2)` of the gauge group.

```lean
def GaugeGroupI.ofSU2 : SU 2 →* GaugeGroupI
```

**`StandardModel.GaugeGroupI.ofSU3_apply`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L89).

> The colour factor sends `U` to `(U, 1, 1)`.

```lean
lemma GaugeGroupI.ofSU3_apply (U : SU 3) : GaugeGroupI.ofSU3 U = (U, 1, 1)
```

**`StandardModel.GaugeGroupI.ofSU2_apply`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L93).

> The isospin factor sends `V` to `(1, V, 1)`.

```lean
lemma GaugeGroupI.ofSU2_apply (V : SU 2) : GaugeGroupI.ofSU2 V = (1, V, 1)
```

## B. One fundamental and one anti-fundamental index

> The invariants reduce to the delta contraction, for colour and for isospin.

**`StandardModel.ColourFundAntiFund.of_law`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L113).

> A family `T^a{}_b` with one fundamental and one anti-fundamental colour index: when every
> colour rotation `U` moves its members by a factor of `U` for the first index and of `conj U`
> for the second, the summed index first, its map out of the tensors of `SU(3)` is equivariant
> for the colour factor of the gauge group.

```lean
lemma of_law (hT : ∀ (U : SU 3) (l : Fin 2 → Fin 3), repGauge (U, 1, 1) (T l)
    = ∑ a : Fin 2 → Fin 3, (U.1 (a 0) (l 0) * starRingEnd ℂ (U.1 (a 1) (l 1))) • T a) :
    (suTensor 3).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU3)
      (liftComponents (T ∘ fundAntiFundIdx))
```

**`StandardModel.ColourFundAntiFund.sum`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L120).

> The map of a finite sum of families is equivariant when the map of each family is.

```lean
lemma sum {ι : Type} [Fintype ι] {T : ι → (Fin 2 → Fin 3) → B}
    (hT : ∀ i, (suTensor 3).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU3)
      (liftComponents (T i ∘ fundAntiFundIdx))) :
    (suTensor 3).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU3)
      (liftComponents ((fun l => ∑ i, T i l) ∘ fundAntiFundIdx))
```

**`StandardModel.ColourFundAntiFund.deltaContraction`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L128).

> The delta contraction `∑ a, T ![a, a]`.

```lean
def deltaContraction (T : (Fin 2 → Fin 3) → B) : B
```

**`StandardModel.ColourFundAntiFund.deltaContraction_mem_span`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L131).

> The delta contraction lies in the span of the components.

```lean
lemma deltaContraction_mem_span (T : (Fin 2 → Fin 3) → B) :
    deltaContraction T ∈ Submodule.span ℂ (Set.range T)
```

**`StandardModel.ColourFundAntiFund.map_deltaContraction`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L136).

> Any map moving the components by an element of `SU(3)` fixes the delta contraction.

```lean
lemma map_deltaContraction {U : SU 3} {f : B →ₗ[ℂ] B} (hf : ∀ l : Fin 2 → Fin 3,
    f (T l) = ∑ a : Fin 2 → Fin 3, (U.1 (a 0) (l 0) * starRingEnd ℂ (U.1 (a 1) (l 1))) • T a) :
    f (deltaContraction T) = deltaContraction T
```

**`StandardModel.ColourFundAntiFund.repGauge_deltaContraction`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L143).

> The delta contraction is colour invariant.

```lean
lemma repGauge_deltaContraction
    (hT : (suTensor 3).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU3)
      (liftComponents (T ∘ fundAntiFundIdx)))
    (U : SU 3) : repGauge (U, 1, 1) (deltaContraction T) = deltaContraction T
```

**`StandardModel.ColourFundAntiFund.invariantReductionToSpan`**, a def, [line 152](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L152).

> The colour invariants of the component span reduce to the span of the delta
> contraction.

```lean
noncomputable def invariantReductionToSpan
    (hT : (suTensor 3).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU3)
      (liftComponents (T ∘ fundAntiFundIdx))) :
    InvariantReductionToSpan (fun U : SU 3 => repGauge ((U, 1, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T))
```

**`StandardModel.IsospinFundAntiFund.of_law`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L168).

> A family `T^a{}_b` with one fundamental and one anti-fundamental isospin index: when every
> isospin rotation moves its members as the components of such a tensor, its map out of the
> tensors of `SU(2)` is equivariant for the isospin factor of the gauge group.

```lean
lemma of_law (hT : ∀ (V : SU 2) (l : Fin 2 → Fin 2), repGauge (1, V, 1) (T l)
    = ∑ a : Fin 2 → Fin 2, (V.1 (a 0) (l 0) * starRingEnd ℂ (V.1 (a 1) (l 1))) • T a) :
    (suTensor 2).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents (T ∘ fundAntiFundIdx))
```

**`StandardModel.IsospinFundAntiFund.sum`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L175).

> The map of a finite sum of families is equivariant when the map of each family is.

```lean
lemma sum {ι : Type} [Fintype ι] {T : ι → (Fin 2 → Fin 2) → B}
    (hT : ∀ i, (suTensor 2).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents (T i ∘ fundAntiFundIdx))) :
    (suTensor 2).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents ((fun l => ∑ i, T i l) ∘ fundAntiFundIdx))
```

**`StandardModel.IsospinFundAntiFund.deltaContraction`**, a def, [line 183](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L183).

> The delta contraction `T ![0, 0] + T ![1, 1]`.

```lean
def deltaContraction (T : (Fin 2 → Fin 2) → B) : B
```

**`StandardModel.IsospinFundAntiFund.deltaContraction_eq_sum`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L187).

> The delta contraction is the trace `∑ a, T ![a, a]`.

```lean
lemma deltaContraction_eq_sum (T : (Fin 2 → Fin 2) → B) :
    deltaContraction T = ∑ a : Fin 2, T ![a, a]
```

**`StandardModel.IsospinFundAntiFund.deltaContraction_mem_span`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L192).

> The delta contraction lies in the span of the components.

```lean
lemma deltaContraction_mem_span (T : (Fin 2 → Fin 2) → B) :
    deltaContraction T ∈ Submodule.span ℂ (Set.range T)
```

**`StandardModel.IsospinFundAntiFund.map_deltaContraction`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L197).

> Any map moving the components by an element of `SU(2)` fixes the delta contraction.

```lean
lemma map_deltaContraction {V : SU 2} {f : B →ₗ[ℂ] B} (hf : ∀ l : Fin 2 → Fin 2,
    f (T l) = ∑ a : Fin 2 → Fin 2, (V.1 (a 0) (l 0) * starRingEnd ℂ (V.1 (a 1) (l 1))) • T a) :
    f (deltaContraction T) = deltaContraction T
```

**`StandardModel.IsospinFundAntiFund.repGauge_deltaContraction`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L204).

> The delta contraction is isospin invariant.

```lean
lemma repGauge_deltaContraction
    (hT : (suTensor 2).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents (T ∘ fundAntiFundIdx)))
    (V : SU 2) : repGauge (1, V, 1) (deltaContraction T) = deltaContraction T
```

**`StandardModel.IsospinFundAntiFund.invariantReductionToSpan`**, a def, [line 213](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L213).

> The isospin invariants of the component span reduce to the span of the delta
> contraction.

```lean
noncomputable def invariantReductionToSpan
    (hT : (suTensor 2).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents (T ∘ fundAntiFundIdx))) :
    InvariantReductionToSpan (fun V : SU 2 => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T))
```

**`StandardModel.IsospinFundAntiFund.reducesInvariantsTo_span_deltaContraction`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L224).

> The isospin invariants of the component span reduce to the line through the delta
> contraction.

```lean
lemma reducesInvariantsTo_span_deltaContraction
    (hT : (suTensor 2).IsEquivariant ![.fund, .antiFund] (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents (T ∘ fundAntiFundIdx))) :
    ReducesInvariantsTo (fun V : SU 2 => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T)) (ℂ ∙ deltaContraction T)
```

## C. Two isospin indices of the same kind

> Two fundamental or two anti-fundamental isospin indices have the epsilon contraction alone as
> invariant.

**`StandardModel.IsospinFundFund.of_law`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L249).

> A family `T^{ab}` with two fundamental isospin indices: when every isospin rotation `V` moves
> its members by one factor of `V` per index, its map out of the tensors of `SU(2)` is equivariant
> for the isospin factor of the gauge group.

```lean
lemma of_law (hT : ∀ (V : SU 2) (l : Fin 2 → Fin 2), repGauge (1, V, 1) (T l)
    = ∑ a : Fin 2 → Fin 2, (∏ i : Fin 2, V.1 (a i) (l i)) • T a) :
    (suTensor 2).IsEquivariant (fun _ : Fin 2 => .fund) (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents T)
```

**`StandardModel.IsospinFundFund.sum`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L256).

> The map of a finite sum of families is equivariant when the map of each family is.

```lean
lemma sum {ι : Type} [Fintype ι] {T : ι → (Fin 2 → Fin 2) → B}
    (hT : ∀ i, (suTensor 2).IsEquivariant (fun _ : Fin 2 => .fund)
      (repGauge.comp GaugeGroupI.ofSU2) (liftComponents (T i))) :
    (suTensor 2).IsEquivariant (fun _ : Fin 2 => .fund) (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents fun l => ∑ i, T i l)
```

**`StandardModel.IsospinFundFund.epsilonContraction`**, a def, [line 264](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L264).

> The epsilon contraction `T ![0, 1] - T ![1, 0]`.

```lean
def epsilonContraction (T : (Fin 2 → Fin 2) → B) : B
```

**`StandardModel.IsospinFundFund.map_epsilonContraction`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L267).

> Any map moving the components by an element of `SU(2)` fixes the epsilon contraction.

```lean
lemma map_epsilonContraction {V : SU 2} {f : B →ₗ[ℂ] B} (hf : ∀ l : Fin 2 → Fin 2,
    f (T l) = ∑ a : Fin 2 → Fin 2, (∏ i : Fin 2, V.1 (a i) (l i)) • T a) :
    f (epsilonContraction T) = epsilonContraction T
```

**`StandardModel.IsospinFundFund.repGauge_epsilonContraction`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L274).

> The epsilon contraction is isospin invariant.

```lean
lemma repGauge_epsilonContraction
    (hT : (suTensor 2).IsEquivariant (fun _ : Fin 2 => .fund) (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents T)) (V : SU 2) :
    repGauge (1, V, 1) (epsilonContraction T) = epsilonContraction T
```

**`StandardModel.IsospinFundFund.invariantReductionToSpan`**, a def, [line 283](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L283).

> The isospin invariants of the component span reduce to the span of the epsilon
> contraction.

```lean
noncomputable def invariantReductionToSpan
    (hT : (suTensor 2).IsEquivariant (fun _ : Fin 2 => .fund) (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents T)) :
    InvariantReductionToSpan (fun V : SU 2 => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T))
```

**`StandardModel.IsospinAntiFundAntiFund.of_law`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L299).

> A family `T_{ab}` with two anti-fundamental isospin indices: when every isospin rotation `V`
> moves its members by one factor of `conj V` per index, its map out of the tensors of `SU(2)` is
> equivariant for the isospin factor of the gauge group.

```lean
lemma of_law (hT : ∀ (V : SU 2) (l : Fin 2 → Fin 2), repGauge (1, V, 1) (T l)
    = ∑ a : Fin 2 → Fin 2,
        (starRingEnd ℂ (V.1 (a 0) (l 0)) * starRingEnd ℂ (V.1 (a 1) (l 1))) • T a) :
    (suTensor 2).IsEquivariant (fun _ : Fin 2 => .antiFund) (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents T)
```

**`StandardModel.IsospinAntiFundAntiFund.sum`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L308).

> The map of a finite sum of families is equivariant when the map of each family is.

```lean
lemma sum {ι : Type} [Fintype ι] {T : ι → (Fin 2 → Fin 2) → B}
    (hT : ∀ i, (suTensor 2).IsEquivariant (fun _ : Fin 2 => .antiFund)
      (repGauge.comp GaugeGroupI.ofSU2) (liftComponents (T i))) :
    (suTensor 2).IsEquivariant (fun _ : Fin 2 => .antiFund) (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents fun l => ∑ i, T i l)
```

**`StandardModel.IsospinAntiFundAntiFund.map_epsilonContraction`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L317).

> Any map moving the components by an element of `SU(2)` in the anti-fundamental fixes the
> epsilon contraction.

```lean
lemma map_epsilonContraction {V : SU 2} {f : B →ₗ[ℂ] B} (hf : ∀ l : Fin 2 → Fin 2,
    f (T l) = ∑ a : Fin 2 → Fin 2,
        (starRingEnd ℂ (V.1 (a 0) (l 0)) * starRingEnd ℂ (V.1 (a 1) (l 1))) • T a) :
    f (IsospinFundFund.epsilonContraction T) = IsospinFundFund.epsilonContraction T
```

**`StandardModel.IsospinAntiFundAntiFund.repGauge_epsilonContraction`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L326).

> The epsilon contraction is isospin invariant.

```lean
lemma repGauge_epsilonContraction
    (hT : (suTensor 2).IsEquivariant (fun _ : Fin 2 => .antiFund)
      (repGauge.comp GaugeGroupI.ofSU2) (liftComponents T)) (V : SU 2) :
    repGauge (1, V, 1) (IsospinFundFund.epsilonContraction T)
      = IsospinFundFund.epsilonContraction T
```

**`StandardModel.IsospinAntiFundAntiFund.invariantReductionToSpan`**, a def, [line 336](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L336).

> The isospin invariants of the component span reduce to the span of the epsilon
> contraction.

```lean
noncomputable def invariantReductionToSpan
    (hT : (suTensor 2).IsEquivariant (fun _ : Fin 2 => .antiFund)
      (repGauge.comp GaugeGroupI.ofSU2) (liftComponents T)) :
    InvariantReductionToSpan (fun V : SU 2 => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T))
```

## D. Four fundamental isospin indices

> The invariants reduce to the two ways of pairing the four indices by epsilon.

**`StandardModel.IsospinQuadFund.of_law`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L360).

> A family `T^{abcd}` with four fundamental isospin indices: when every isospin rotation `V`
> moves its members by one factor of `V` per index, its map out of the tensors of `SU(2)` is
> equivariant for the isospin factor of the gauge group.

```lean
lemma of_law (hT : ∀ (V : SU 2) (l : Fin 4 → Fin 2), repGauge (1, V, 1) (T l)
    = ∑ a : Fin 4 → Fin 2, (∏ i : Fin 4, V.1 (a i) (l i)) • T a) :
    (suTensor 2).IsEquivariant (fun _ : Fin 4 => .fund) (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents T)
```

**`StandardModel.IsospinQuadFund.epsilonContraction₁₂`**, a def, [line 368](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L368).

> The contraction pairing the first index with the second and the third with the
> fourth.

```lean
def epsilonContraction₁₂ (T : (Fin 4 → Fin 2) → B) : B
```

**`StandardModel.IsospinQuadFund.epsilonContraction₁₃`**, a def, [line 373](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L373).

> The contraction pairing the first index with the third and the second with the
> fourth.

```lean
def epsilonContraction₁₃ (T : (Fin 4 → Fin 2) → B) : B
```

**`StandardModel.IsospinQuadFund.reducesInvariantsTo_span_epsilonContractions`**, a lemma, [line 378](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean#L378).

> The isospin invariants of the component span reduce to the span of the two epsilon
> contractions.

```lean
lemma reducesInvariantsTo_span_epsilonContractions
    (hT : (suTensor 2).IsEquivariant (fun _ : Fin 4 => .fund) (repGauge.comp GaugeGroupI.ofSU2)
      (liftComponents T)) :
    ReducesInvariantsTo (fun V : SU 2 => repGauge ((1, V, 1) : GaugeGroupI))
      (Submodule.span ℂ (Set.range T))
      (Submodule.span ℂ {epsilonContraction₁₂ T, epsilonContraction₁₃ T})
```

## Depends on

- [The Standard Model Gauge Group](../../../../physlib/particles/standardmodel/gaugegroup/basic.md)
- [The Kronecker delta of `SU(N)`](../../../classicalfieldtheory/gaugetheory/part-03/globalgaugegroup-su-invariants-delta.md)
- [The Levi-Civita tensors of `SU(N)`](../../../classicalfieldtheory/gaugetheory/part-03/globalgaugegroup-su-invariants-levicivita.md)

## Proof depends on

- [The pairings of four fundamental indices of `SU(2)` by the Levi-Civita symbol](../../../classicalfieldtheory/gaugetheory/part-03/globalgaugegroup-su-invariants-levicivitapairing.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Invariants/Basic.lean)
