---
declaration: module
origin: cited
lean: KleinGordon.Spacetime.retardedResponse, KleinGordon.Spacetime.advancedResponse, KleinGordon.Spacetime.contDiff_retardedResponse, KleinGordon.Spacetime.contDiff_advancedResponse, KleinGordon.Spacetime.tsupport_retardedResponse_subset, KleinGordon.Spacetime.tsupport_advancedResponse_subset, KleinGordon.Spacetime.retardedResponse_sourceOperator, KleinGordon.Spacetime.advancedResponse_sourceOperator
statement: formalized
proof: formalized
---

# Green operators on spacetime

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.GreenOperators`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean): 34 declarations, 24 with a docstring.

> Retarded and advanced Green operators of the Klein–Gordon equation on `SpaceTime d` for every mass.

## i. Overview

> Retarded and advanced Green operators of the Klein–Gordon equation on `SpaceTime d` for every mass.
> Uniqueness and the exact sequence follow.

## ii. Key results

> - `retardedResponse` : The retarded spatial Fourier response of a compact source on Minkowski
>   spacetime.
> - `advancedResponse` : The advanced spatial Fourier response of a compact source on Minkowski
>   spacetime.
> - `testFieldEquiv` : The neighbour's compact smooth fields and Mathlib's bundled test functions have
>   the same data.
> - `retardedMap` : The retarded Fourier response as a real linear map into the existing smooth-field
>   space.
> - `advancedMap` : The advanced Fourier response as a real linear map into the existing smooth-field
>   space.
> - `retardedGreenOperator` : The retarded Fourier Green inverse for the existing Minkowski equation
>   in every dimension.
> - `advancedGreenOperator` : The advanced Fourier Green inverse for the existing Minkowski equation
>   in every dimension.
> - `greenOperators` : The spatial Fourier Green pair for Klein–Gordon fields in arbitrary spatial
>   dimension.

## iv. References

> None.

## A. The spatial Fourier Green construction on Minkowski spacetime

> - `retardedResponse` : The retarded spatial Fourier response of a compact source on Minkowski
>   spacetime.
> - `advancedResponse` : The advanced spatial Fourier response of a compact source on Minkowski
>   spacetime.
>
> Lemmas: `contDiff_retardedResponse`, `contDiff_advancedResponse`,
> `tsupport_retardedResponse_subset`, `tsupport_advancedResponse_subset`,
> `retardedResponse_sourceOperator`, `advancedResponse_sourceOperator`.

## B. Fourier Klein–Gordon Green operators in every dimension

> - `testFieldEquiv` : The neighbour's compact smooth fields and Mathlib's bundled test functions have
>   the same data.
> - `retardedMap` : The retarded Fourier response as a real linear map into the existing smooth-field
>   space.
> - `advancedMap` : The advanced Fourier response as a real linear map into the existing smooth-field
>   space.
> - `retardedGreenOperator` : The retarded Fourier Green inverse for the existing Minkowski equation
>   in every dimension.
> - `advancedGreenOperator` : The advanced Fourier Green inverse for the existing Minkowski equation
>   in every dimension.
> - `greenOperators` : The spatial Fourier Green pair for Klein–Gordon fields in arbitrary spatial
>   dimension.
>
> Lemmas: `testFieldEquiv_compactOperator`, `retardedMap_solves`, `advancedMap_solves`.

## C. Real scalar Fourier Green operators

> - `fiberIntertwiner` : A constant fibre transformation intertwines the equal-mass Klein–Gordon
>   equations.
> - `realRetardedGreenOperator` : The real part of the complex retarded response is a real scalar
>   Green inverse.
> - `realAdvancedGreenOperator` : The real part of the complex advanced response is a real scalar
>   Green inverse.
> - `realGreenOperators` : The real scalar Klein–Gordon Green pair for transposition in arbitrary
>   spatial dimension.
>
> Lemmas: `fiberIntertwiner_compactOperator`.

## D. Continuous evaluation of the spacetime Fourier response

> - `retardedEvaluation` : Continuous evaluation of the complex Banach-valued retarded Fourier
>   response.
> - `advancedEvaluation` : Continuous evaluation of the complex Banach-valued advanced Fourier
>   response.
> - `realRetardedEvaluation` : Continuous evaluation of the real scalar retarded Green response.
> - `realAdvancedEvaluation` : Continuous evaluation of the real scalar advanced Green response.
>
> Lemmas: `retardedEvaluation_apply`, `advancedEvaluation_apply`, `realRetardedEvaluation_apply`,
> `realAdvancedEvaluation_apply`.

## E. Uniqueness for the Fourier Klein–Gordon Green operators

> - `solutionSpaceEquivQuotient` : Spacelike-compact homogeneous solutions of the Klein–Gordon
>   equation are the compact source classes modulo the equation of motion, in every spatial dimension.
>
> Lemmas: `existsUnique_retardedSolution`, `causalGreen_exactSequence`.

**`KleinGordon.Spacetime.retardedResponse`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L132).

> The retarded spatial Fourier response of a compact source on Minkowski spacetime.

```lean
def retardedResponse (μ : ℝ) (f : 𝓓((⊤ : Opens (SpaceTime d)), F)) (p : SpaceTime d) : F
```

**`KleinGordon.Spacetime.advancedResponse`**, a def, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L136).

> The advanced spatial Fourier response of a compact source on Minkowski spacetime.

```lean
def advancedResponse (μ : ℝ) (f : 𝓓((⊤ : Opens (SpaceTime d)), F)) (p : SpaceTime d) : F
```

**`KleinGordon.Spacetime.contDiff_retardedResponse`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L139).

```lean
lemma contDiff_retardedResponse {μ : ℝ} (hμ : 0 ≤ μ)
    (f : 𝓓((⊤ : Opens (SpaceTime d)), F)) : ContDiff ℝ ∞ (retardedResponse F μ f)
```

**`KleinGordon.Spacetime.contDiff_advancedResponse`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L143).

```lean
lemma contDiff_advancedResponse {μ : ℝ} (hμ : 0 ≤ μ)
    (f : 𝓓((⊤ : Opens (SpaceTime d)), F)) : ContDiff ℝ ∞ (advancedResponse F μ f)
```

**`KleinGordon.Spacetime.tsupport_retardedResponse_subset`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L148).

> The retarded spacetime field has support inside the coordinate light cones of its source.

```lean
lemma tsupport_retardedResponse_subset {μ : ℝ} (hμ : 0 ≤ μ)
    (f : 𝓓((⊤ : Opens (SpaceTime d)), F)) :
    tsupport (retardedResponse F μ f) ⊆ (coordinates d) ⁻¹'
      causalFuture (coordinates d '' tsupport f)
```

**`KleinGordon.Spacetime.tsupport_advancedResponse_subset`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L160).

> The advanced spacetime field has support inside the past coordinate light cones.

```lean
lemma tsupport_advancedResponse_subset {μ : ℝ} (hμ : 0 ≤ μ)
    (f : 𝓓((⊤ : Opens (SpaceTime d)), F)) :
    tsupport (advancedResponse F μ f) ⊆ (coordinates d) ⁻¹'
      causalPast (coordinates d '' tsupport f)
```

**`KleinGordon.Spacetime.retardedResponse_sourceOperator`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L172).

> The retarded response recovers a spacetime test field from its compact Klein–Gordon source.

```lean
lemma retardedResponse_sourceOperator {μ : ℝ} (hμ : 0 ≤ μ)
    (f : 𝓓((⊤ : Opens (SpaceTime d)), F)) (p : SpaceTime d) :
    retardedResponse F μ (sourceOperator F μ f) p = f p
```

**`KleinGordon.Spacetime.advancedResponse_sourceOperator`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L181).

> The advanced response recovers a spacetime test field from its compact Klein–Gordon source.

```lean
lemma advancedResponse_sourceOperator {μ : ℝ} (hμ : 0 ≤ μ)
    (f : 𝓓((⊤ : Opens (SpaceTime d)), F)) (p : SpaceTime d) :
    advancedResponse F μ (sourceOperator F μ f) p = f p
```

**`KleinGordon.Spacetime.testFieldEquiv`**, a def, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L195).

> The neighbour's compact smooth fields and Mathlib's bundled test functions have the same data.

```lean
def testFieldEquiv : TestField d F ≃ₗ[ℝ] 𝓓((⊤ : Opens (SpaceTime d)), F)
```

**`KleinGordon.Spacetime.testFieldEquiv_compactOperator`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L212).

```lean
lemma testFieldEquiv_compactOperator (m : ℝ) (f : TestField d F) :
    testFieldEquiv F ((equation m).compactOperator f) =
      sourceOperator F (m ^ 2) (testFieldEquiv F f)
```

**`KleinGordon.Spacetime.retardedMap`**, a def, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L219).

> The retarded Fourier response as a real linear map into the existing smooth-field space.

```lean
def retardedMap (m : ℝ) : TestField d F →ₗ[ℝ] smoothFields d F
```

**`KleinGordon.Spacetime.advancedMap`**, a def, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L234).

> The advanced Fourier response as a real linear map into the existing smooth-field space.

```lean
def advancedMap (m : ℝ) : TestField d F →ₗ[ℝ] smoothFields d F
```

**`KleinGordon.Spacetime.retardedMap_solves`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L256).

```lean
lemma retardedMap_solves (m : ℝ) (f : TestField d F) :
    KleinGordon.Spacetime.operator m (retardedMap F m f) = f.val
```

**`KleinGordon.Spacetime.advancedMap_solves`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L269).

```lean
lemma advancedMap_solves (m : ℝ) (f : TestField d F) :
    KleinGordon.Spacetime.operator m (advancedMap F m f) = f.val
```

**`KleinGordon.Spacetime.retardedGreenOperator`**, a def, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L284).

> The retarded Fourier Green inverse for the existing Minkowski equation in every dimension.

```lean
def retardedGreenOperator (m : ℝ) :
    RetardedGreenOperator (causalRelation d) (equation (V := F) m)
```

**`KleinGordon.Spacetime.advancedGreenOperator`**, a def, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L302).

> The advanced Fourier Green inverse for the existing Minkowski equation in every dimension.

```lean
def advancedGreenOperator (m : ℝ) :
    AdvancedGreenOperator (causalRelation d) (equation (V := F) m)
```

**`KleinGordon.Spacetime.greenOperators`**, a def, [line 320](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L320).

> The spatial Fourier Green pair for Klein–Gordon fields in arbitrary spatial dimension.

```lean
def greenOperators (m : ℝ) :
    GreenOperators (causalRelation d) (equation (V := F) m)
```

**`KleinGordon.Spacetime.fiberIntertwiner`**, a def, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L330).

> A constant fibre transformation intertwines the equal-mass Klein–Gordon equations.

```lean
def fiberIntertwiner (m : ℝ) (L : V →L[ℝ] W) :
    FieldIntertwiner (equation (d := d) (V := V) m)
      (equation (d := d) (V := W) m)
```

**`KleinGordon.Spacetime.fiberIntertwiner_compactOperator`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L341).

```lean
lemma fiberIntertwiner_compactOperator (m : ℝ) (L : V →L[ℝ] W) (f : TestField d V) :
    (fiberIntertwiner m L).compactMap ((equation m).compactOperator f) =
      (equation m).compactOperator ((fiberIntertwiner m L).compactMap f)
```

**`KleinGordon.Spacetime.realRetardedGreenOperator`**, a def, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L348).

> The real part of the complex retarded response is a real scalar Green inverse.

```lean
def realRetardedGreenOperator (m : ℝ) :
    RetardedGreenOperator (causalRelation d)
      (equation (V := ℝ) m)
```

**`KleinGordon.Spacetime.realAdvancedGreenOperator`**, a def, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L377).

> The real part of the complex advanced response is a real scalar Green inverse.

```lean
def realAdvancedGreenOperator (m : ℝ) :
    AdvancedGreenOperator (causalRelation d)
      (equation (V := ℝ) m)
```

**`KleinGordon.Spacetime.realGreenOperators`**, a def, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L406).

> The real scalar Klein–Gordon Green pair for transposition in arbitrary spatial dimension.

```lean
def realGreenOperators (m : ℝ) :
    GreenOperators (causalRelation d) (equation (V := ℝ) m)
```

**`KleinGordon.Spacetime.retardedEvaluation`**, a def, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L415).

> Continuous evaluation of the complex Banach-valued retarded Fourier response.

```lean
def retardedEvaluation {μ : ℝ} (hμ : 0 ≤ μ) (p : SpaceTime d) :
    𝓓((⊤ : Opens (SpaceTime d)), F) →L[ℝ] F
```

**`KleinGordon.Spacetime.advancedEvaluation`**, a def, [line 421](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L421).

> Continuous evaluation of the complex Banach-valued advanced Fourier response.

```lean
def advancedEvaluation {μ : ℝ} (hμ : 0 ≤ μ) (p : SpaceTime d) :
    𝓓((⊤ : Opens (SpaceTime d)), F) →L[ℝ] F
```

**`KleinGordon.Spacetime.retardedEvaluation_apply`**, a lemma, [line 426](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L426).

```lean
lemma retardedEvaluation_apply {μ : ℝ} (hμ : 0 ≤ μ) (p : SpaceTime d)
    (f : 𝓓((⊤ : Opens (SpaceTime d)), F)) :
    retardedEvaluation F hμ p f = retardedResponse F μ f p
```

**`KleinGordon.Spacetime.advancedEvaluation_apply`**, a lemma, [line 430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L430).

```lean
lemma advancedEvaluation_apply {μ : ℝ} (hμ : 0 ≤ μ) (p : SpaceTime d)
    (f : 𝓓((⊤ : Opens (SpaceTime d)), F)) :
    advancedEvaluation F hμ p f = advancedResponse F μ f p
```

**`KleinGordon.Spacetime.realRetardedEvaluation`**, a def, [line 437](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L437).

> Continuous evaluation of the real scalar retarded Green response.

```lean
def realRetardedEvaluation (m : ℝ) (p : SpaceTime d) :
    𝓓((⊤ : Opens (SpaceTime d)), ℝ) →L[ℝ] ℝ
```

**`KleinGordon.Spacetime.realAdvancedEvaluation`**, a def, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L443).

> Continuous evaluation of the real scalar advanced Green response.

```lean
def realAdvancedEvaluation (m : ℝ) (p : SpaceTime d) :
    𝓓((⊤ : Opens (SpaceTime d)), ℝ) →L[ℝ] ℝ
```

**`KleinGordon.Spacetime.realRetardedEvaluation_apply`**, a lemma, [line 448](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L448).

```lean
lemma realRetardedEvaluation_apply (m : ℝ) (p : SpaceTime d) (f : TestField d ℝ) :
    realRetardedEvaluation m p (testFieldEquiv ℝ f) =
      ((realRetardedGreenOperator m).toLinearMap f).val p
```

**`KleinGordon.Spacetime.realAdvancedEvaluation_apply`**, a lemma, [line 452](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L452).

```lean
lemma realAdvancedEvaluation_apply (m : ℝ) (p : SpaceTime d) (f : TestField d ℝ) :
    realAdvancedEvaluation m p (testFieldEquiv ℝ f) =
      ((realAdvancedGreenOperator m).toLinearMap f).val p
```

**`KleinGordon.Spacetime.existsUnique_retardedSolution`**, a lemma, [line 461](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L461).

> A compact smooth source has exactly one sharply retarded solution of the Klein–Gordon
> equation, in every spatial dimension.

```lean
lemma existsUnique_retardedSolution (m : ℝ)
    (f : (equation (d := d) (V := F) m).compactSources) :
    ∃! u : smoothFields d F,
      (equation (V := F) m).operator u = f.val ∧
      tsupport (u : SpaceTime d → F) ⊆
        (causalRelation d).causalFuture (tsupport (f.val : SpaceTime d → F))
```

**`KleinGordon.Spacetime.causalGreen_exactSequence`**, a lemma, [line 473](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L473).

> The causal Green sequence for the Klein–Gordon equation in every spatial dimension:
> the equation of motion is injective on compact fields, the causal propagator is exact in the
> middle and the equation of motion is surjective on spacelike-compact fields.

```lean
lemma causalGreen_exactSequence (m : ℝ) :
    let P := equation (d := d) (V := F) m
    Function.Injective P.compactOperator ∧
      Function.Exact P.compactOperator (greenOperators F m).toSpacelikeCompact ∧
      Function.Exact (greenOperators F m).toSpacelikeCompact
        (P.spacelikeCompactOperator (causalRelation d)) ∧
      Function.Surjective (P.spacelikeCompactOperator (causalRelation d))
```

**`KleinGordon.Spacetime.smoothFieldsAddGroup`**, an instance, [line 485](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L485).

> Fix the inherited field addition for quotient inference.

```lean
local instance smoothFieldsAddGroup : AddCommGroup (smoothFields d F)
```

**`KleinGordon.Spacetime.solutionSpaceEquivQuotient`**, a def, [line 490](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean#L490).

> Spacelike-compact homogeneous solutions of the Klein–Gordon equation are the compact source
> classes modulo the equation of motion, in every spatial dimension.

```lean
noncomputable def solutionSpaceEquivQuotient (m : ℝ) :
    let P := equation (d := d) (V := F) m
    P.spacelikeCompactSolution (causalRelation d) ≃ₗ[ℝ]
      (P.compactSources ⧸ LinearMap.range P.compactOperator)
```

## Depends on

- [Smooth spacetime fields as Green operator input](../../greenoperator/smoothfields.md)
- [Uniqueness and the causal exact sequence](../../greenoperator/uniqueness.md)
- [Coordinates of spacetime](coordinates.md)
- [Cutoff responses of compact sources](cutoffresponse.md)

## Proof depends on

- [Finite propagation speed](finitepropagation.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/GreenOperators.lean)
