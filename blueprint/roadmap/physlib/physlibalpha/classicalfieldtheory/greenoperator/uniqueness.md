---
declaration: module
origin: cited
lean: GreenOperator.distribution_eq_zero_of_retarded, GreenOperator.GreenOperators.solutionFieldAddGroup, GreenOperator.GreenOperators.compact_equation_of_causal_split, GreenOperator.GreenOperators.sourceOfCausalSplit, GreenOperator.GreenOperators.causalPropagator_sourceOfCausalSplit, GreenOperator.GreenOperators.toSolutionSpace_surjective, GreenOperator.GreenOperators.solutionSpaceEquivQuotient, GreenOperator.GreenOperators.solutionSpaceEquivQuotient_symm_mk
statement: formalized
proof: formalized
---

# Uniqueness and the causal exact sequence

The module `PhyslibAlpha.ClassicalFieldTheory.GreenOperator.Uniqueness`, [PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean): 18 declarations, 18 with a docstring.

## i. Overview

> Existence and uniqueness of retarded solutions and the exact sequence of compact sources and
> spacelike compact fields.

## ii. Key results

> - `sourceOfCausalSplit` : The compact source obtained from a causal splitting of a homogeneous
>   field.
> - `solutionSpaceEquivQuotient` : Compact test fields modulo the equation of motion are equivalent to
>   spacelike-compact homogeneous solutions.
> - `solutionSpaceEquivQuotientOfLocalization` : Homogeneous spacelike-compact solutions are source
>   classes, with one-sided inverse and uniqueness hypotheses discharged by local compact
>   constructions.
> - `toSpacelikeCompact` : The causal propagator with the support codomain required in the exact
>   sequence.

## iv. References

> None.

## A. One-sided uniqueness for weak solutions

> Lemmas: `distribution_eq_zero_of_retarded`.

## B. Homogeneous solutions as source classes

> - `sourceOfCausalSplit` : The compact source obtained from a causal splitting of a homogeneous
>   field.
> - `solutionSpaceEquivQuotient` : Compact test fields modulo the equation of motion are equivalent to
>   spacelike-compact homogeneous solutions.
> - `solutionSpaceEquivQuotientOfLocalization` : Homogeneous spacelike-compact solutions are source
>   classes, with one-sided inverse and uniqueness hypotheses discharged by local compact
>   constructions.
>
> Lemmas: `compact_equation_of_causal_split`, `causalPropagator_sourceOfCausalSplit`,
> `toSolutionSpace_surjective`, `solutionSpaceEquivQuotient_symm_mk`,
> `solutionSpaceEquivQuotient_toSolutionSpace`, `spacelikeCompactOperator_surjective_of_localization`.

## C. The causal Green exact sequence

> - `toSpacelikeCompact` : The causal propagator with the support codomain required in the exact
>   sequence.
>
> Lemmas: `toSpacelikeCompact_ker`, `exact_compactSources`, `exact_spacelikeCompactFields`,
> `causalGreen_exactSequence`.

## D. General sourced field equations

> Lemmas: `existsUnique_retardedSolution`, `existsUnique_retardedSolution_of_localization`.

**`GreenOperator.distribution_eq_zero_of_retarded`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean#L89).

> Compact advanced Green data and causal localization force a retarded weak homogeneous
> solution to vanish. The native test model preserves the underlying scalar test fields.

```lean
lemma distribution_eq_zero_of_retarded
    (e : P.compactSources ≃ₗ[ℝ] _root_.TestFunction (⊤ : Opens E) ℝ ⊤)
    (he : ∀ f : P.compactSources, (e f : E → ℝ) = f.val.val)
    (G : AdvancedGreenOperator C P) (L : PastLocalization C.reverse P)
    (hC : C.HasCompactCausalDiamonds) (K : Set E) (hK : IsCompact K)
    (T : Distribution (⊤ : Opens E) V ⊤)
    (hT : Distribution.IsVanishingOn T (C.causalFuture K)ᶜ)
    (hzero : ∀ f : P.compactSources, T (e (P.compactOperator f)) = 0) : T = 0
```

**`GreenOperator.GreenOperators.solutionFieldAddGroup`**, an instance, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean#L138).

> Fix the inherited field addition for nested quotient inference.

```lean
local instance solutionFieldAddGroup : AddCommGroup S
```

**`GreenOperator.GreenOperators.compact_equation_of_causal_split`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean#L141).

> Equal equations of a future-supported and a past-supported field have compact support.

```lean
lemma compact_equation_of_causal_split (hC : C.HasCompactCausalDiamonds)
    (uPlus : P.futureSupportedFields C) (uMinus : P.futureSupportedFields C.reverse)
    (heq : P.operator uPlus.val = P.operator uMinus.val) :
    HasCompactSupport (P.operator uPlus.val : M → V)
```

**`GreenOperator.GreenOperators.sourceOfCausalSplit`**, a def, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean#L153).

> The compact source obtained from a causal splitting of a homogeneous field.

```lean
def sourceOfCausalSplit (hC : C.HasCompactCausalDiamonds)
    (uPlus : P.futureSupportedFields C) (uMinus : P.futureSupportedFields C.reverse)
    (heq : P.operator uPlus.val = P.operator uMinus.val) : P.compactSources
```

**`GreenOperator.GreenOperators.causalPropagator_sourceOfCausalSplit`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean#L159).

> The causal propagator reconstructs the difference of a causal split from its common source.

```lean
lemma causalPropagator_sourceOfCausalSplit (hC : C.HasCompactCausalDiamonds)
    (hret : Function.Injective (P.futureSupportedOperator C))
    (hadv : Function.Injective (P.futureSupportedOperator C.reverse))
    (uPlus : P.futureSupportedFields C) (uMinus : P.futureSupportedFields C.reverse)
    (heq : P.operator uPlus.val = P.operator uMinus.val) :
    G.causalPropagator (sourceOfCausalSplit hC uPlus uMinus heq) = uPlus.val - uMinus.val
```

**`GreenOperator.GreenOperators.toSolutionSpace_surjective`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean#L171).

> Every spacelike-compact homogeneous field is produced by a compact source.
> The source is constructed from a causal cutoff rather than postulated as a preimage.

```lean
lemma toSolutionSpace_surjective (hC : C.HasCompactCausalDiamonds)
    (hret : Function.Injective (P.futureSupportedOperator C)) (hadv : Function.Injective
      (P.futureSupportedOperator C.reverse))
    (hcut : P.HasCausalCutoffs C) : Function.Surjective G.toSolutionSpace
```

**`GreenOperator.GreenOperators.solutionSpaceEquivQuotient`**, a def, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean#L187).

> Compact test fields modulo the equation of motion are equivalent to spacelike-compact
> homogeneous solutions. All support, cutoff and one-sided supported hypotheses are explicit.

```lean
noncomputable def solutionSpaceEquivQuotient (hC : C.HasCompactCausalDiamonds)
    (hret : Function.Injective (P.futureSupportedOperator C)) (hadv : Function.Injective
      (P.futureSupportedOperator C.reverse))
    (hcut : P.HasCausalCutoffs C) :
    P.spacelikeCompactSolution C ≃ₗ[𝕜]
      (P.compactSources ⧸ LinearMap.range P.compactOperator)
```

**`GreenOperator.GreenOperators.solutionSpaceEquivQuotient_symm_mk`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean#L200).

> The quotient-to-solution map is exactly the causal propagator on each source class.

```lean
lemma solutionSpaceEquivQuotient_symm_mk (hC : C.HasCompactCausalDiamonds)
    (hret : Function.Injective (P.futureSupportedOperator C))
    (hadv : Function.Injective (P.futureSupportedOperator C.reverse))
    (hcut : P.HasCausalCutoffs C) (f : P.compactSources) :
    (G.solutionSpaceEquivQuotient hC hret hadv hcut).symm (Submodule.Quotient.mk f) =
      G.toSolutionSpace f
```

**`GreenOperator.GreenOperators.solutionSpaceEquivQuotient_toSolutionSpace`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean#L209).

> A causally produced solution represents precisely the class of its source.

```lean
lemma solutionSpaceEquivQuotient_toSolutionSpace (hC : C.HasCompactCausalDiamonds)
    (hret : Function.Injective (P.futureSupportedOperator C))
    (hadv : Function.Injective (P.futureSupportedOperator C.reverse))
    (hcut : P.HasCausalCutoffs C) (f : P.compactSources) :
    G.solutionSpaceEquivQuotient hC hret hadv hcut (G.toSolutionSpace f) =
      Submodule.Quotient.mk f
```

**`GreenOperator.GreenOperators.spacelikeCompactOperator_surjective_of_localization`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean#L221).

> The final equation map is onto by solving the two cutoff pieces with the constructed
> extensions.

```lean
lemma spacelikeCompactOperator_surjective_of_localization
    (Lret : PastLocalization C P) (Ladv : PastLocalization C.reverse P)
    (hC : C.HasCompactCausalDiamonds) (hcut : P.HasCausalCutoffs C) :
    Function.Surjective (P.spacelikeCompactOperator C)
```

**`GreenOperator.GreenOperators.solutionSpaceEquivQuotientOfLocalization`**, a def, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean#L241).

> Homogeneous spacelike-compact solutions are source classes, with one-sided inverse and
> uniqueness hypotheses discharged by local compact constructions.

```lean
noncomputable def solutionSpaceEquivQuotientOfLocalization
    (Lret : PastLocalization C P) (Ladv : PastLocalization C.reverse P)
    (hC : C.HasCompactCausalDiamonds) (hcut : P.HasCausalCutoffs C) :
    P.spacelikeCompactSolution C ≃ₗ[𝕜]
      (P.compactSources ⧸ LinearMap.range P.compactOperator)
```

**`GreenOperator.GreenOperators.toSpacelikeCompact`**, a def, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean#L252).

> The causal propagator with the support codomain required in the exact sequence.

```lean
def toSpacelikeCompact : P.compactSources →ₗ[𝕜] P.spacelikeCompactFields C
```

**`GreenOperator.GreenOperators.toSpacelikeCompact_ker`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean#L256).

> The codomain restriction does not change the propagator's kernel.

```lean
lemma toSpacelikeCompact_ker :
    LinearMap.ker G.toSpacelikeCompact = LinearMap.ker G.causalPropagator
```

**`GreenOperator.GreenOperators.exact_compactSources`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean#L262).

> Exactness at compact sources in the support-typed causal sequence.

```lean
lemma exact_compactSources (hC : C.HasCompactCausalDiamonds) :
    Function.Exact P.compactOperator G.toSpacelikeCompact
```

**`GreenOperator.GreenOperators.exact_spacelikeCompactFields`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean#L267).

> Exactness at spacelike-compact fields follows from causal splitting and one-sided uniqueness.

```lean
lemma exact_spacelikeCompactFields (hC : C.HasCompactCausalDiamonds)
    (hret : Function.Injective (P.futureSupportedOperator C))
    (hadv : Function.Injective (P.futureSupportedOperator C.reverse))
    (hcut : P.HasCausalCutoffs C) :
    Function.Exact G.toSpacelikeCompact (P.spacelikeCompactOperator C)
```

**`GreenOperator.GreenOperators.causalGreen_exactSequence`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean#L289).

> The full causal Green sequence, including injectivity and terminal surjectivity.
> The larger-support inverses and uniqueness are derived from compact Green data and localization.

```lean
lemma causalGreen_exactSequence
    (Lret : PastLocalization C P) (Ladv : PastLocalization C.reverse P)
    (hC : C.HasCompactCausalDiamonds) (hcut : P.HasCausalCutoffs C) :
    Function.Injective P.compactOperator ∧
      Function.Exact P.compactOperator G.toSpacelikeCompact ∧
      Function.Exact G.toSpacelikeCompact (P.spacelikeCompactOperator C) ∧
      Function.Surjective (P.spacelikeCompactOperator C)
```

**`GreenOperator.RetardedGreenOperator.existsUnique_retardedSolution`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean#L316).

> A source has exactly one sharply retarded solution when the future-supported homogeneous
> kernel vanishes. Existence follows from the supplied Green operator.

```lean
lemma existsUnique_retardedSolution
    (huniq : Function.Injective (P.futureSupportedOperator C)) (f : P.compactSources) :
    ∃! u : S, P.operator u = f.val ∧
      tsupport (u : M → V) ⊆ C.causalFuture (tsupport (f.val : M → V))
```

**`GreenOperator.RetardedGreenOperator.existsUnique_retardedSolution_of_localization`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean#L329).

> Local compact-cutoff geometry proves the uniqueness hypothesis of the compact-source theorem.

```lean
lemma existsUnique_retardedSolution_of_localization (L : PastLocalization C P)
    (hC : C.HasCompactCausalDiamonds) (f : P.compactSources) :
    ∃! u : S, P.operator u = f.val ∧
      tsupport (u : M → V) ⊆ C.causalFuture (tsupport (f.val : M → V))
```

## Depends on

- [The causal propagator and causal uniqueness](causalpropagator.md)
- [Localization and extension of retarded responses](localization.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/Uniqueness.lean)
