---
declaration: module
origin: cited
lean: Representation.ContinuousMatrixCoeff, Representation.continuousMatrixCoeff_of_span, Representation.integral_sub_one_mem_span, Representation.comp_integral_eq_integral, Representation.coordRep, Representation.coordRep_apply, Representation.coordRep_mul, Representation.toRepresentation_apply_equivFun_symm
statement: formalized
proof: formalized
---

# Reynolds elements for compact groups

The module `PhyslibAlpha.Mathematics.RepresentationTheory.Reynolds.Compact`, [PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Compact.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Compact.lean): 11 declarations, 11 with a docstring.

> Continuous finite-dimensional representations of compact groups have Reynolds elements.

## i. Overview

> Let `ρ` be a complex representation of a compact topological group `H` and `W` a
> finite-dimensional subrepresentation on which `ρ` is continuous. Averaging the operators `ρ h`
> on `W` over the normalized Haar measure gives an operator `P` on `W`. Left invariance of the Haar
> measure gives `ρ g ∘ P = P`, so `P` maps into the invariants of `W`.
>
> The operator `P` is also a finite combination `Σ cᵢ ρ hᵢ` with `Σ cᵢ = 1`. The set
> `1 + span {ρ h - 1}`, the affine span of the operators `ρ h`, is closed and convex because it is a
> translate of a finite-dimensional subspace. It contains every `ρ h`, so it contains their average
> by `Convex.integral_mem`. By `Representation.exists_isReynolds_of_sub_one_mem_span` this makes
> `P` the action of a Reynolds element.
>
> The integral is carried out in coordinates. A basis identifies `W` with `Fin n → ℂ`, and the
> operators `ρ h` become continuous linear maps on this normed space.
>
> Continuity of `ρ` on `W` is phrased without a topology on `W` or `V`, as continuity of every
> matrix coefficient `h ↦ φ (ρ h w)` with `φ` a linear functional on `W`. Since `W` is
> finite-dimensional this is continuity for its unique vector space topology. A finite spanning
> family with continuous coefficients is enough to prove it.

## ii. Key results

> - `Representation.ContinuousMatrixCoeff` is continuity of a representation on a subspace.
> - `Representation.continuousMatrixCoeff_of_span` proves it from a finite spanning family.
> - `Representation.exists_isReynolds_of_compactSpace` gives Reynolds elements for compact groups.

## iv. References

> - The Haar average as a Reynolds operator, see for example
>   T. Bröcker and T. tom Dieck, *Representations of Compact Lie Groups*.

## A. Continuity on a finite-dimensional subrepresentation

### A.1. The definition

**`Representation.ContinuousMatrixCoeff`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Compact.lean#L87).

> The representation is continuous on the subrepresentation `W` if every matrix coefficient
> `h ↦ φ (ρ h w)`, for `w` in `W` and `φ` a linear functional on `W`, is continuous. For a
> finite-dimensional `W` this is continuity for the unique vector space topology on `W`.

```lean
def ContinuousMatrixCoeff (W : Subrepresentation ρ) : Prop
```

### A.2. Continuity from a spanning family

**`Representation.continuousMatrixCoeff_of_span`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Compact.lean#L99).

> A subrepresentation spanned by a finite family `v`, on which the group acts by continuous
> coefficients `ρ h (v i) = Σ j, a i j h • v j`, has continuous matrix coefficients.

```lean
lemma continuousMatrixCoeff_of_span [IsTopologicalRing k] {ι : Type*} [Fintype ι]
    (W : Subrepresentation ρ) (v : ι → V) (hvW : ∀ i, v i ∈ W.toSubmodule)
    (hspan : W.toSubmodule ≤ Submodule.span k (Set.range v)) (a : ι → ι → H → k)
    (ha : ∀ i j, Continuous (a i j)) (hρ : ∀ h i, ρ h (v i) = ∑ j, a i j h • v j) :
    ContinuousMatrixCoeff W
```

## B. Averaging continuous linear maps over a compact group

### B.1. The average lies in one plus the span of the group image

**`Representation.integral_sub_one_mem_span`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Compact.lean#L139).

> The average of a family of operators on a finite-dimensional space, with respect to a
> probability measure, lies in the affine span `1 + span {F h - 1}` of the family.

```lean
lemma integral_sub_one_mem_span (μ : Measure H) [IsProbabilityMeasure μ]
    {F : H → E →L[ℂ] E} (hF : Integrable F μ) :
    (∫ h, F h ∂μ) - 1 ∈ Submodule.span ℂ (Set.range fun h => F h - 1)
```

### B.2. The average is invariant

**`Representation.comp_integral_eq_integral`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Compact.lean#L163).

> The average of a multiplicative family of operators over a left-invariant measure is
> absorbed by each operator of the family.

```lean
lemma comp_integral_eq_integral [Group H] [MeasurableMul H] (μ : Measure H) [μ.IsMulLeftInvariant]
    {F : H → E →L[ℂ] E} (hF : Integrable F μ) (hmul : ∀ g h, F (g * h) = (F g).comp (F h))
    (g : H) : (F g).comp (∫ h, F h ∂μ) = ∫ h, F h ∂μ
```

## C. The subrepresentation in coordinates

**`Representation.coordRep`**, a def, [line 184](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Compact.lean#L184).

> The action of a group element on a finite-dimensional subrepresentation, written in the
> coordinates of a chosen basis as a continuous linear map on `Fin n → ℂ`.

```lean
noncomputable def coordRep (W : Subrepresentation ρ) [FiniteDimensional ℂ W.toSubmodule]
    (h : H) : (Fin (Module.finrank ℂ W.toSubmodule) → ℂ) →L[ℂ]
      (Fin (Module.finrank ℂ W.toSubmodule) → ℂ)
```

**`Representation.coordRep_apply`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Compact.lean#L193).

> The coordinate form of the action is the action conjugated by the coordinate map.

```lean
lemma coordRep_apply (h : H) (x : Fin (Module.finrank ℂ W.toSubmodule) → ℂ) :
    coordRep W h x = (Module.finBasis ℂ W.toSubmodule).equivFun
      (W.toRepresentation h ((Module.finBasis ℂ W.toSubmodule).equivFun.symm x))
```

**`Representation.coordRep_mul`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Compact.lean#L199).

> The coordinate form of the action is multiplicative.

```lean
lemma coordRep_mul (g h : H) : coordRep W (g * h) = (coordRep W g).comp (coordRep W h)
```

**`Representation.toRepresentation_apply_equivFun_symm`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Compact.lean#L204).

> The action on a vector given by its coordinates, in terms of the coordinate form.

```lean
lemma toRepresentation_apply_equivFun_symm (h : H)
    (x : Fin (Module.finrank ℂ W.toSubmodule) → ℂ) :
    W.toRepresentation h ((Module.finBasis ℂ W.toSubmodule).equivFun.symm x) =
      (Module.finBasis ℂ W.toSubmodule).equivFun.symm (coordRep W h x)
```

**`Representation.continuous_coordRep`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Compact.lean#L211).

> The coordinate form of the representation is continuous when the matrix coefficients are.

```lean
lemma continuous_coordRep [TopologicalSpace H] (hW : ContinuousMatrixCoeff W) :
    Continuous (coordRep W)
```

**`Representation.conj_sub_one_mem_span`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Compact.lean#L219).

> Conjugating back to the subrepresentation, an operator in `1 + span {coordRep h - 1}`
> becomes an operator in `1 + span {ρ h - 1}`.

```lean
lemma conj_sub_one_mem_span
    {P : (Fin (Module.finrank ℂ W.toSubmodule) → ℂ) →L[ℂ] Fin (Module.finrank ℂ W.toSubmodule) → ℂ}
    (hP : P - 1 ∈ Submodule.span ℂ (Set.range fun h => coordRep W h - 1)) :
    (Module.finBasis ℂ W.toSubmodule).equivFun.symm.conj (P : Module.End ℂ _) - 1 ∈
      Submodule.span ℂ (Set.range fun h => W.toRepresentation h - 1)
```

## D. Existence of Reynolds elements

**`Representation.exists_isReynolds_of_compactSpace`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Compact.lean#L249).

> A representation of a compact group which is continuous on a finite-dimensional
> subrepresentation has a Reynolds element on it. The Reynolds element realizes the average of the
> group action over the normalized Haar measure.

```lean
lemma exists_isReynolds_of_compactSpace [TopologicalSpace H] [IsTopologicalGroup H] [CompactSpace H]
    (hW : ContinuousMatrixCoeff W) : ∃ r, ρ.IsReynolds W.toSubmodule r
```

## Depends on

- [Reynolds elements](reynolds-basic.md)

## Sources

- [PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Compact.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/Compact.lean)
