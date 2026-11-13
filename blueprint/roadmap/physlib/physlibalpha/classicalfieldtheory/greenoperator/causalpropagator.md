---
declaration: module
origin: cited
lean: GreenOperator.GreenOperators.greenFieldAddGroup, GreenOperator.GreenOperators.causalPropagator, GreenOperator.GreenOperators.causalPropagator_solves, GreenOperator.GreenOperators.causalPropagator_comp_operator, GreenOperator.GreenOperators.causalPropagator_support, GreenOperator.GreenOperators.causalPropagator_mem_solution, GreenOperator.GreenOperators.toSolutionSpace, GreenOperator.GreenOperators.range_compactOperator_le_ker
statement: formalized
proof: formalized
---

# The causal propagator and causal uniqueness

The module `PhyslibAlpha.ClassicalFieldTheory.GreenOperator.CausalPropagator`, [PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean): 22 declarations, 22 with a docstring.

> The difference of the retarded and advanced response solves the homogeneous equation.

## i. Overview

> The difference of the retarded and advanced response solves the homogeneous equation. Uniqueness of
> one-sided solutions follows from the support of the response.

## ii. Key results

> - `causalPropagator` : The causal propagator uses the sign convention retarded minus advanced.
> - `toSolutionSpace` : The causal propagator with its proven solution-space codomain.
> - `HasCausalCutoffs` : Temporal cutoff splitting of spacelike-compact admissible fields.
> - `eq_of_local_truncations` : Compact truncations agreeing with the same field in the observation's
>   causal past give identical retarded responses.

## iv. References

> None.

## A. The causal propagator and compact source kernel

> - `causalPropagator` : The causal propagator uses the sign convention retarded minus advanced.
> - `toSolutionSpace` : The causal propagator with its proven solution-space codomain.
>
> Lemmas: `causalPropagator_solves`, `causalPropagator_comp_operator`, `causalPropagator_support`,
> `causalPropagator_mem_solution`, `range_compactOperator_le_ker`, `compactOperator_injective`,
> `retarded_compact_of_causalPropagator_eq_zero`, `mem_range_of_causalPropagator_eq_zero`,
> `causalPropagator_ker`, `toSolutionSpace_ker`.

## B. Causal splitting and one-sided uniqueness

> - `HasCausalCutoffs` : Temporal cutoff splitting of spacelike-compact admissible fields.
>
> Lemmas: `futureSupported_unique`, `retarded_mem_futureSupportedFields`,
> `advanced_mem_futureSupportedFields_reverse`, `retarded_eq_of_futureSupported`,
> `advanced_eq_of_pastSupported`.

## C. Local field equations and causal agreement

> Lemmas: `eq_zero_of_no_causal_source`, `eq_of_no_causal_difference`, `eq_of_local_truncations`.

**`GreenOperator.GreenOperators.greenFieldAddGroup`**, an instance, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L80).

> Fix the inherited field addition for nested quotient inference.

```lean
local instance greenFieldAddGroup : AddCommGroup S
```

**`GreenOperator.GreenOperators.causalPropagator`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L83).

> The causal propagator uses the sign convention retarded minus advanced.

```lean
def causalPropagator : P.compactSources →ₗ[𝕜] S
```

**`GreenOperator.GreenOperators.causalPropagator_solves`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L87).

> The causal propagator produces homogeneous fields.

```lean
lemma causalPropagator_solves (f : P.compactSources) :
    P.operator (G.causalPropagator f) = 0
```

**`GreenOperator.GreenOperators.causalPropagator_comp_operator`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L93).

> Test sources differing by the field equation give the same causal response.

```lean
lemma causalPropagator_comp_operator (f : P.compactSources) :
    G.causalPropagator (P.compactOperator f) = 0
```

**`GreenOperator.GreenOperators.causalPropagator_support`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L100).

> Causal propagation is supported in the union of the future and past of its source.

```lean
lemma causalPropagator_support (f : P.compactSources) :
    tsupport (G.causalPropagator f : M → V) ⊆ C.causalHull (tsupport (f.val : M → V))
```

**`GreenOperator.GreenOperators.causalPropagator_mem_solution`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L107).

> Compact source support yields spacelike-compact homogeneous response.

```lean
lemma causalPropagator_mem_solution (f : P.compactSources) :
    G.causalPropagator f ∈ P.spacelikeCompactSolution C
```

**`GreenOperator.GreenOperators.toSolutionSpace`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L113).

> The causal propagator with its proven solution-space codomain.

```lean
def toSolutionSpace : P.compactSources →ₗ[𝕜] P.spacelikeCompactSolution C
```

**`GreenOperator.GreenOperators.range_compactOperator_le_ker`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L118).

> Equations of motion are in the kernel of the causal propagator.
> The reverse inclusion requires causal compactness and additional arguments.

```lean
lemma range_compactOperator_le_ker :
    LinearMap.range P.compactOperator ≤ LinearMap.ker G.causalPropagator
```

**`GreenOperator.GreenOperators.compactOperator_injective`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L125).

> A compact homogeneous field vanishes because either Green operator is a left inverse.

```lean
lemma compactOperator_injective : Function.Injective P.compactOperator
```

**`GreenOperator.GreenOperators.retarded_compact_of_causalPropagator_eq_zero`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L132).

> A source in the causal-propagator kernel has a compact retarded response.

```lean
lemma retarded_compact_of_causalPropagator_eq_zero (hC : C.HasCompactCausalDiamonds)
    (f : P.compactSources) (hf : G.causalPropagator f = 0) :
    HasCompactSupport (G.retarded.toLinearMap f : M → V)
```

**`GreenOperator.GreenOperators.mem_range_of_causalPropagator_eq_zero`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L140).

> Every zero causal response is an equation-of-motion source of a compact field.

```lean
lemma mem_range_of_causalPropagator_eq_zero (hC : C.HasCompactCausalDiamonds)
    (f : P.compactSources) (hf : G.causalPropagator f = 0) :
    f ∈ LinearMap.range P.compactOperator
```

**`GreenOperator.GreenOperators.causalPropagator_ker`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L151).

> The kernel of the causal propagator consists precisely of equation-of-motion sources.
> The proof uses compact causal diamonds rather than an assumed exactness hypothesis.

```lean
lemma causalPropagator_ker (hC : C.HasCompactCausalDiamonds) :
    LinearMap.ker G.causalPropagator = LinearMap.range P.compactOperator
```

**`GreenOperator.GreenOperators.toSolutionSpace_ker`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L159).

> The solution-valued propagator has the same kernel as its unrestricted counterpart.

```lean
lemma toSolutionSpace_ker :
    LinearMap.ker G.toSolutionSpace = LinearMap.ker G.causalPropagator
```

**`LocalOperator.futureSupported_unique`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L175).

> Every two future-supported fields with the same equation coincide.

```lean
lemma futureSupported_unique (h : Function.Injective (P.futureSupportedOperator C))
    {u v : S} (hu : u ∈ P.futureSupportedFields C) (hv : v ∈ P.futureSupportedFields C)
    (heq : P.operator u = P.operator v) : u = v
```

**`LocalOperator.HasCausalCutoffs`**, a def, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L185).

> Temporal cutoff splitting of spacelike-compact admissible fields.
> In a smooth spacetime this is proved using a suitable smooth Cauchy cutoff and its complement.
> It contains no Green-operator or solution-surjectivity assertion.

```lean
def HasCausalCutoffs : Prop
```

**`GreenOperator.GreenOperators.retarded_mem_futureSupportedFields`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L202).

> Retarded compact-source responses belong to the extension's support class.

```lean
lemma retarded_mem_futureSupportedFields (f : P.compactSources) :
    G.retarded.toLinearMap f ∈ P.futureSupportedFields C
```

**`GreenOperator.GreenOperators.advanced_mem_futureSupportedFields_reverse`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L207).

> Advanced compact-source responses belong to the past-supported extension class.

```lean
lemma advanced_mem_futureSupportedFields_reverse (f : P.compactSources) :
    G.advanced.toLinearMap f ∈ P.futureSupportedFields C.reverse
```

**`GreenOperator.GreenOperators.retarded_eq_of_futureSupported`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L212).

> One-sided uniqueness identifies any future-supported solution with the retarded response.

```lean
lemma retarded_eq_of_futureSupported (h : Function.Injective (P.futureSupportedOperator C))
    (f : P.compactSources) {u : S} (hu : u ∈ P.futureSupportedFields C)
    (hPu : P.operator u = f.val) : G.retarded.toLinearMap f = u
```

**`GreenOperator.GreenOperators.advanced_eq_of_pastSupported`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L219).

> One-sided uniqueness identifies any past-supported solution with the advanced response.

```lean
lemma advanced_eq_of_pastSupported (h : Function.Injective (P.futureSupportedOperator C.reverse))
    (f : P.compactSources) {u : S} (hu : u ∈ P.futureSupportedFields C.reverse)
    (hPu : P.operator u = f.val) : G.advanced.toLinearMap f = u
```

**`GreenOperator.RetardedGreenOperator.eq_zero_of_no_causal_source`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L238).

> A compact source unable to reach the observation event has zero retarded response there.

```lean
lemma eq_zero_of_no_causal_source (f : P.compactSources) {x : M}
    (h : ∀ y : M, C.Precedes y x → y ∉ tsupport (f.val : M → V)) :
    (G.toLinearMap f : M → V) x = 0
```

**`GreenOperator.RetardedGreenOperator.eq_of_no_causal_difference`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L248).

> Two compact-source responses coincide when their discrepancy cannot reach the observation
> event.

```lean
lemma eq_of_no_causal_difference (f g : P.compactSources) {x : M}
    (h : ∀ y : M, C.Precedes y x → y ∉ tsupport ((f.val - g.val : S) : M → V)) :
    (G.toLinearMap f : M → V) x = (G.toLinearMap g : M → V) x
```

**`GreenOperator.RetardedGreenOperator.eq_of_local_truncations`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean#L257).

> Compact truncations agreeing with the same field in the observation's causal past give
> identical retarded responses. Equality is needed as germs to control topological support.

```lean
lemma eq_of_local_truncations (f g : P.compactSources) (u : S) {x : M}
    (hf : ∀ y : M, C.Precedes y x → (f.val : M → V) =ᶠ[𝓝 y] (u : M → V))
    (hg : ∀ y : M, C.Precedes y x → (g.val : M → V) =ᶠ[𝓝 y] (u : M → V)) :
    (G.toLinearMap f : M → V) x = (G.toLinearMap g : M → V) x
```

## Depends on

- [Green operators and causally supported fields](basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GreenOperator/CausalPropagator.lean)
