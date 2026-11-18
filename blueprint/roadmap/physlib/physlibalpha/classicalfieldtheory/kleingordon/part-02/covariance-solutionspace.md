---
declaration: module
origin: cited
lean: KleinGordon.Solution.actSmooth_mem_spacelikeCompactSolution, KleinGordon.Solution.actSol, KleinGordon.Solution.actSol_coe, KleinGordon.Solution.SourceClasses, KleinGordon.Solution.actQuot, KleinGordon.Solution.actQuot_mk, KleinGordon.Solution.solutionsEquivQuotient_symm_mk, KleinGordon.Solution.propagatorClass_actQuot
statement: formalized
proof: formalized
---

# The solution space as a Poincaré representation

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.Covariance.SolutionSpace`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/SolutionSpace.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/SolutionSpace.lean): 10 declarations (1 instance with no name), 10 with a docstring.

> The space of homogeneous solutions with spacelike compact support carries an action of the
> Poincaré group. The causal propagator is an equivariant isomorphism from the compact sources
> modulo the equation of motion to this space.

## i. Overview

> A homogeneous solution with spacelike compact support is mapped to another one by every Poincaré
> transformation. The causal hull of a set is mapped to the causal hull of the image by every
> transformation including time reversals. The action on compact sources descends to the quotient by
> the image of the equation of motion because the equation of motion is covariant. The isomorphism
> of the quotient with the solution space sends the class of a source `f` to the causal propagator
> `E f`. It is covariant for orthochronous transformations and changes sign for time reversals.

## ii. Key results

> - `actSol` : the action on spacelike compact homogeneous solutions.
> - `actQuot` : the action on compact sources modulo the equation of motion.
> - `propagatorClass_actQuot` : the isomorphism is covariant for orthochronous transformations.
> - `propagatorClass_actQuot_of_not` : the isomorphism changes sign under time reversals.

## iv. References

> None.

## A. The action on solutions

> - `actSol` : the action on spacelike compact homogeneous solutions.

## B. The action on the quotient

> - `actQuot` : the action on compact sources modulo the equation of motion.

## C. Covariance of the isomorphism

> - `propagatorClass_actQuot` : the isomorphism is covariant for orthochronous transformations.

**An instance with no name**, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/SolutionSpace.lean#L69).

> Smooth fields form an additive group, needed to form the quotient.

```lean
local instance : AddCommGroup (smoothFields d F)
```

**`KleinGordon.Solution.actSmooth_mem_spacelikeCompactSolution`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/SolutionSpace.lean#L74).

> The action preserves homogeneous solutions with spacelike compact support.

```lean
lemma actSmooth_mem_spacelikeCompactSolution (g : PoincareGroup d) {u : smoothFields d F}
    (hu : u ∈ (equation (d := d) (V := F) m).spacelikeCompactSolution (causalRelation d)) :
    actSmooth g u ∈ (equation (d := d) (V := F) m).spacelikeCompactSolution (causalRelation d)
```

**`KleinGordon.Solution.actSol`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/SolutionSpace.lean#L88).

> The action of the Poincaré group on homogeneous solutions with spacelike compact support.

```lean
def actSol (g : PoincareGroup d) :
    (equation (d := d) (V := F) m).spacelikeCompactSolution (causalRelation d) →ₗ[ℝ]
      (equation (d := d) (V := F) m).spacelikeCompactSolution (causalRelation d)
```

**`KleinGordon.Solution.actSol_coe`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/SolutionSpace.lean#L95).

> The value of a transformed solution.

```lean
lemma actSol_coe (g : PoincareGroup d)
    (u : (equation (d := d) (V := F) m).spacelikeCompactSolution (causalRelation d)) :
    ((actSol g u : (equation (d := d) (V := F) m).spacelikeCompactSolution (causalRelation d)) :
      smoothFields d F) = actSmooth g u
```

**`KleinGordon.Solution.SourceClasses`**, an abbrev, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/SolutionSpace.lean#L105).

> Compact sources modulo the equation of motion.

```lean
abbrev SourceClasses (d : ℕ) (F : Type) [NormedAddCommGroup F] [NormedSpace ℂ F] (m : ℝ)
```

**`KleinGordon.Solution.actQuot`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/SolutionSpace.lean#L110).

> The action on compact sources modulo the equation of motion.

```lean
def actQuot (g : PoincareGroup d) : SourceClasses d F m →ₗ[ℝ] SourceClasses d F m
```

**`KleinGordon.Solution.actQuot_mk`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/SolutionSpace.lean#L117).

> The action on the class of a source is the class of the transformed source.

```lean
lemma actQuot_mk (g : PoincareGroup d) (f : (equation (d := d) (V := F) m).compactSources) :
    actQuot (F := F) (m := m) g (Submodule.Quotient.mk f : SourceClasses d F m) =
      Submodule.Quotient.mk (actTest g f)
```

**`KleinGordon.Solution.solutionsEquivQuotient_symm_mk`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/SolutionSpace.lean#L129).

> The isomorphism from the quotient of compact sources onto the solutions sends the class of a
> source to its causal propagator.

```lean
lemma solutionsEquivQuotient_symm_mk (f : (equation (d := d) (V := F) m).compactSources) :
    ((solutionsEquivQuotient (d := d) (F := F) (m := m)).symm (Submodule.Quotient.mk f) :
        smoothFields d F) = propagator F m f
```

**`KleinGordon.Solution.propagatorClass_actQuot`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/SolutionSpace.lean#L135).

> The isomorphism of compact sources modulo the equation of motion with the solutions is
> covariant under orthochronous Poincaré transformations.

```lean
lemma propagatorClass_actQuot {g : PoincareGroup d} (hg : g.IsOrthochronous)
    (x : SourceClasses d F m) :
    (solutionsEquivQuotient (d := d) (F := F) (m := m)).symm (actQuot (F := F) (m := m) g x) =
      actSol g ((solutionsEquivQuotient (d := d) (F := F) (m := m)).symm x)
```

**`KleinGordon.Solution.propagatorClass_actQuot_of_not`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/SolutionSpace.lean#L146).

> The isomorphism changes sign under Poincaré transformations that reverse time.

```lean
lemma propagatorClass_actQuot_of_not {g : PoincareGroup d} (hg : ¬ g.IsOrthochronous)
    (x : SourceClasses d F m) :
    (solutionsEquivQuotient (d := d) (F := F) (m := m)).symm (actQuot (F := F) (m := m) g x) =
      -actSol g ((solutionsEquivQuotient (d := d) (F := F) (m := m)).symm x)
```

## Depends on

- [Klein–Gordon fields and causal propagation](../part-01/solution.md)
- [The Poincaré action on smooth fields](../../../relativity/poincare/fields.md)

## Proof depends on

- [Poincaré covariance of the Klein–Gordon Green operators](covariance-operators.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/SolutionSpace.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/SolutionSpace.lean)
