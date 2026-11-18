---
declaration: module
origin: cited
lean: KleinGordon.Solution.operator_actSmooth, KleinGordon.Solution.compactOperator_actTest, KleinGordon.Solution.existsUnique_advanced, KleinGordon.Solution.tsupport_actTest, KleinGordon.Solution.retarded_actTest, KleinGordon.Solution.advanced_actTest, KleinGordon.Solution.retarded_actTest_of_not, KleinGordon.Solution.advanced_actTest_of_not
statement: formalized
proof: formalized
---

# Poincaré covariance of the Klein–Gordon Green operators

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.Covariance.Operators`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Operators.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Operators.lean): 10 declarations, 10 with a docstring.

> The retarded and advanced solutions commute with the Poincaré group.

## i. Overview

> The Klein–Gordon equation is invariant under the Poincaré group. If `u` solves the equation with
> source `f` then `g • u` solves it with source `g • f`. An orthochronous element maps the causal
> future of the support of `f` to the causal future of the support of `g • f`. So `g • R f` is a
> solution with the support condition of the retarded solution for `g • f`. Uniqueness gives
> `R (g • f) = g • R f`. The same holds for the advanced solution. An element that reverses time
> exchanges the two. So the causal propagator `E` is covariant up to a sign.

## ii. Key results

> - `operator_actSmooth` : the Klein–Gordon operator commutes with the Poincaré action.
> - `retarded_actTest` : the retarded solution is covariant under orthochronous elements.
> - `advanced_actTest` : the advanced solution is covariant under orthochronous elements.
> - `retarded_actTest_of_not` : a time reversal exchanges retarded and advanced solutions.
> - `propagator_actTest` : the causal propagator is covariant under orthochronous elements.

## iv. References

> None.

## A. The operator

> - `operator_actSmooth` : the Klein–Gordon operator commutes with the Poincaré action.

## B. Uniqueness of advanced solutions

> - `existsUnique_advanced` : a compact source has exactly one solution supported in the causal
>   past of the source.

## C. Covariance of the Green operators

> - `retarded_actTest` : the retarded solution is covariant under orthochronous elements.
> - `advanced_actTest` : the advanced solution is covariant under orthochronous elements.
> - `retarded_actTest_of_not` : a time reversal exchanges retarded and advanced solutions.
> - `advanced_actTest_of_not` : the same for the advanced solution.

## D. Covariance of the causal propagator

> - `propagator_actTest` : the causal propagator is covariant under orthochronous elements.
> - `propagator_actTest_of_not` : a time reversal changes the sign of the causal propagator.

**`KleinGordon.Solution.operator_actSmooth`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Operators.lean#L84).

> The Klein–Gordon operator commutes with the action of the Poincaré group.

```lean
lemma operator_actSmooth (m : ℝ) (g : PoincareGroup d) (u : smoothFields d V) :
    Spacetime.operator m (actSmooth g u) = actSmooth g (Spacetime.operator m u)
```

**`KleinGordon.Solution.compactOperator_actTest`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Operators.lean#L90).

> The compact operator commutes with the action on test fields.

```lean
lemma compactOperator_actTest (m : ℝ) (g : PoincareGroup d) (f : TestField d V) :
    (equation m).compactOperator (actTest g f) = actTest g ((equation m).compactOperator f)
```

**`KleinGordon.Solution.existsUnique_advanced`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Operators.lean#L101).

> A compact source has exactly one solution supported in the causal past of the source.

```lean
lemma existsUnique_advanced (f : TestField d F) :
    ∃! u : smoothFields d F, Spacetime.operator m u = f ∧
      tsupport (u : SpaceTime d → F) ⊆
        (causalRelation d).causalPast (tsupport (f : SpaceTime d → F))
```

**`KleinGordon.Solution.tsupport_actTest`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Operators.lean#L116).

> The support of a transformed test field is the image of the support.

```lean
lemma tsupport_actTest (g : PoincareGroup d) (f : TestField d F) :
    tsupport ((actTest g f : TestField d F) : SpaceTime d → F) =
      g • tsupport (f : SpaceTime d → F)
```

**`KleinGordon.Solution.retarded_actTest`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Operators.lean#L122).

> The retarded solution is covariant under orthochronous Poincaré transformations.

```lean
lemma retarded_actTest {g : PoincareGroup d} (hg : g.IsOrthochronous) (f : TestField d F) :
    retarded F m (actTest g f) = actSmooth g (retarded F m f)
```

**`KleinGordon.Solution.advanced_actTest`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Operators.lean#L131).

> The advanced solution is covariant under orthochronous Poincaré transformations.

```lean
lemma advanced_actTest {g : PoincareGroup d} (hg : g.IsOrthochronous) (f : TestField d F) :
    advanced F m (actTest g f) = actSmooth g (advanced F m f)
```

**`KleinGordon.Solution.retarded_actTest_of_not`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Operators.lean#L141).

> A time reversal turns the retarded solution of the transformed source into the transformed
> advanced solution.

```lean
lemma retarded_actTest_of_not {g : PoincareGroup d} (hg : ¬ g.IsOrthochronous)
    (f : TestField d F) : retarded F m (actTest g f) = actSmooth g (advanced F m f)
```

**`KleinGordon.Solution.advanced_actTest_of_not`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Operators.lean#L151).

> A time reversal turns the advanced solution of the transformed source into the transformed
> retarded solution.

```lean
lemma advanced_actTest_of_not {g : PoincareGroup d} (hg : ¬ g.IsOrthochronous)
    (f : TestField d F) : advanced F m (actTest g f) = actSmooth g (retarded F m f)
```

**`KleinGordon.Solution.propagator_actTest`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Operators.lean#L166).

> The causal propagator is covariant under orthochronous Poincaré transformations.

```lean
lemma propagator_actTest {g : PoincareGroup d} (hg : g.IsOrthochronous) (f : TestField d F) :
    propagator F m (actTest g f) = actSmooth g (propagator F m f)
```

**`KleinGordon.Solution.propagator_actTest_of_not`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Operators.lean#L171).

> A time reversal changes the sign of the causal propagator.

```lean
lemma propagator_actTest_of_not {g : PoincareGroup d} (hg : ¬ g.IsOrthochronous)
    (f : TestField d F) :
    propagator F m (actTest g f) = -actSmooth g (propagator F m f)
```

## Depends on

- [Klein–Gordon fields and causal propagation](../part-01/solution.md)
- [The Poincaré action on smooth fields](../../../relativity/poincare/fields.md)

## Proof depends on

- [The wave operator is Poincaré invariant](../../waveequation/poincare.md)
- [The causal structure is Poincaré invariant](../../../relativity/poincare/causality.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Operators.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Operators.lean)
