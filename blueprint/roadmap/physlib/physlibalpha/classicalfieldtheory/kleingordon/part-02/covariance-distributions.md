---
declaration: module
origin: cited
lean: KleinGordon.Solution.actTestFunction_testFieldEquiv, KleinGordon.Solution.testOperator_actTestFunction, KleinGordon.Solution.distributionOperator_actDist, KleinGordon.Solution.actCompact, KleinGordon.Solution.actCompact_val, KleinGordon.Solution.retardedDistribution_actCompact, KleinGordon.Solution.advancedDistribution_actCompact, KleinGordon.Solution.retardedDistribution_actCompact_of_not
statement: formalized
proof: formalized
---

# Poincaré covariance for distributional sources

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.Covariance.Distributions`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean): 17 declarations, 17 with a docstring.

> The retarded and advanced solutions of compactly supported distributions are covariant.

## i. Overview

> The Poincaré group acts on distributions by transposition. The Klein–Gordon operator on
> distributions commutes with this action because the operator on test functions does. A
> transformed compactly supported distribution is compactly supported. The transformed retarded
> solution solves the equation for the transformed source and vanishes outside the transformed
> causal future. Uniqueness of the retarded solution then gives covariance. The point source is a
> retarded solution of a delta distribution. So it is covariant too.

## ii. Key results

> - `testOperator_actTestFunction` : the operator on test functions is covariant.
> - `distributionOperator_actDist` : the operator on distributions is covariant.
> - `retardedDistribution_actCompact` : the retarded solution of a distribution is covariant.
> - `retardedPointSource_actDist` : the retarded point source is covariant.

## iv. References

> None.

## A. The operator on test functions and distributions

> - `testOperator_actTestFunction` : the operator on test functions is covariant.
> - `distributionOperator_actDist` : the operator on distributions is covariant.

## B. Compactly supported distributions

> - `actCompact` : the action on compactly supported distributions.

## C. Covariance of the solutions

> - `retardedDistribution_actCompact` : the retarded solution of a distribution is covariant.

## D. The point source

> - `retardedPointSource_actDist` : the retarded point source is covariant.

**`KleinGordon.Solution.actTestFunction_testFieldEquiv`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean#L77).

> The action on test functions agrees with the action on test fields.

```lean
lemma actTestFunction_testFieldEquiv (g : PoincareGroup d) (f : TestField d ℝ) :
    actTestFunction g (testFieldEquiv ℝ f) = testFieldEquiv ℝ (actTest g f)
```

**`KleinGordon.Solution.testOperator_actTestFunction`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean#L83).

> The Klein–Gordon operator on test functions commutes with the Poincaré action.

```lean
lemma testOperator_actTestFunction (m : ℝ) (g : PoincareGroup d)
    (φ : 𝓓((⊤ : TopologicalSpace.Opens (SpaceTime d)), ℝ)) :
    Spacetime.testOperator m (actTestFunction g φ) =
      actTestFunction g (Spacetime.testOperator m φ)
```

**`KleinGordon.Solution.distributionOperator_actDist`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean#L95).

> The Klein–Gordon operator on distributions commutes with the Poincaré action.

```lean
lemma distributionOperator_actDist {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]
    (m : ℝ) (g : PoincareGroup d) (T : DistributionField d V) :
    distributionOperator m (actDist g T) = actDist g (distributionOperator m T)
```

**`KleinGordon.Solution.actCompact`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean#L109).

> The action of the Poincaré group on compactly supported distributions.

```lean
def actCompact (g : PoincareGroup d) (T : compactDistributions (SpaceTime d) V) :
    compactDistributions (SpaceTime d) V
```

**`KleinGordon.Solution.actCompact_val`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean#L118).

> The value of a transformed compactly supported distribution.

```lean
lemma actCompact_val (g : PoincareGroup d) (T : compactDistributions (SpaceTime d) V) :
    (actCompact g T : DistributionField d V) = actDist g T
```

**`KleinGordon.Solution.retardedDistribution_actCompact`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean#L124).

> The retarded solution of a distribution is covariant under orthochronous transformations.

```lean
lemma retardedDistribution_actCompact {g : PoincareGroup d} (hg : g.IsOrthochronous)
    (T : compactDistributions (SpaceTime d) V) :
    retardedDistribution m (actCompact g T) = actDist g (retardedDistribution m T)
```

**`KleinGordon.Solution.advancedDistribution_actCompact`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean#L136).

> The advanced solution of a distribution is covariant under orthochronous transformations.

```lean
lemma advancedDistribution_actCompact {g : PoincareGroup d} (hg : g.IsOrthochronous)
    (T : compactDistributions (SpaceTime d) V) :
    advancedDistribution m (actCompact g T) = actDist g (advancedDistribution m T)
```

**`KleinGordon.Solution.retardedDistribution_actCompact_of_not`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean#L149).

> A time reversal turns the retarded solution of the transformed source into the transformed
> advanced solution.

```lean
lemma retardedDistribution_actCompact_of_not {g : PoincareGroup d} (hg : ¬ g.IsOrthochronous)
    (T : compactDistributions (SpaceTime d) V) :
    retardedDistribution m (actCompact g T) = actDist g (advancedDistribution m T)
```

**`KleinGordon.Solution.advancedDistribution_actCompact_of_not`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean#L162).

> A time reversal turns the advanced solution of the transformed source into the transformed
> retarded solution.

```lean
lemma advancedDistribution_actCompact_of_not {g : PoincareGroup d} (hg : ¬ g.IsOrthochronous)
    (T : compactDistributions (SpaceTime d) V) :
    advancedDistribution m (actCompact g T) = actDist g (retardedDistribution m T)
```

**`KleinGordon.Solution.deltaCompact`**, a def, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean#L178).

> The delta distribution at `p` as a compactly supported distribution.

```lean
def deltaCompact (p : SpaceTime d) : compactDistributions (SpaceTime d) ℝ
```

**`KleinGordon.Solution.actCompact_deltaCompact`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean#L184).

> The action sends the delta distribution at `p` to the delta distribution at `g p`.

```lean
lemma actCompact_deltaCompact (g : PoincareGroup d) (p : SpaceTime d) :
    actCompact g (deltaCompact p) = deltaCompact (g • p)
```

**`KleinGordon.Solution.retardedPointSource_eq`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean#L191).

> The retarded point source is the retarded solution of the delta distribution.

```lean
lemma retardedPointSource_eq (p : SpaceTime d) :
    retardedPointSource m p = retardedDistribution m (deltaCompact p)
```

**`KleinGordon.Solution.advancedPointSource_eq`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean#L197).

> The advanced point source is the advanced solution of the delta distribution.

```lean
lemma advancedPointSource_eq (p : SpaceTime d) :
    advancedPointSource m p = advancedDistribution m (deltaCompact p)
```

**`KleinGordon.Solution.retardedPointSource_actDist`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean#L203).

> The retarded point source is covariant under orthochronous transformations.

```lean
lemma retardedPointSource_actDist {g : PoincareGroup d} (hg : g.IsOrthochronous)
    (p : SpaceTime d) :
    actDist g (retardedPointSource m p) = retardedPointSource m (g • p)
```

**`KleinGordon.Solution.advancedPointSource_actDist`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean#L210).

> The advanced point source is covariant under orthochronous transformations.

```lean
lemma advancedPointSource_actDist {g : PoincareGroup d} (hg : g.IsOrthochronous)
    (p : SpaceTime d) :
    actDist g (advancedPointSource m p) = advancedPointSource m (g • p)
```

**`KleinGordon.Solution.retardedPointSource_actDist_of_not`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean#L218).

> A time reversal turns the transformed retarded point source into the advanced point
> source at the transformed point.

```lean
lemma retardedPointSource_actDist_of_not {g : PoincareGroup d} (hg : ¬ g.IsOrthochronous)
    (p : SpaceTime d) :
    actDist g (retardedPointSource m p) = advancedPointSource m (g • p)
```

**`KleinGordon.Solution.advancedPointSource_actDist_of_not`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean#L226).

> A time reversal turns the transformed advanced point source into the retarded point source
> at the transformed point.

```lean
lemma advancedPointSource_actDist_of_not {g : PoincareGroup d} (hg : ¬ g.IsOrthochronous)
    (p : SpaceTime d) :
    actDist g (advancedPointSource m p) = retardedPointSource m (g • p)
```

## Depends on

- [Klein–Gordon fields and causal propagation](../part-01/solution.md)
- [The Poincaré action on test functions and distributions](../../../relativity/poincare/distributions.md)
- [The Poincaré action on smooth fields](../../../relativity/poincare/fields.md)

## Proof depends on

- [Poincaré covariance of the Klein–Gordon Green operators](covariance-operators.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Distributions.lean)
