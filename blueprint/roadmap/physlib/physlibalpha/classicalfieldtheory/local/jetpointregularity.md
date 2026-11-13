---
declaration: module
origin: cited
lean: ClassicalFieldTheory.Local.jetCoordinatesAt_contDiff, ClassicalFieldTheory.Local.jetBaseCoordinates_contDiff, ClassicalFieldTheory.Local.jetCoordinatesAt_eq_zero_of_notMem_tsupport, ClassicalFieldTheory.Local.jetDirectionAt_eq_zero_of_notMem_tsupport
statement: formalized
proof: formalized
---

# Regularity and support for jet-coordinate maps

The module `PhyslibAlpha.ClassicalFieldTheory.Local.JetPointRegularity`, [PhyslibAlpha/ClassicalFieldTheory/Local/JetPointRegularity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointRegularity.lean): 4 declarations, 4 with a docstring; 1 private, not shown.

> Smoothness of jet-coordinate maps of smooth fields and their vanishing outside the support.

## i. Overview

> This module collects the analytic facts about coordinate-level jet maps that are needed later in
> the local variational argument.
>
> At this stage, it provides:
>
> - smoothness of jet-coordinate maps of smooth fields,
> - smoothness of the base-plus-coordinate jet map,
> - and vanishing of jet coordinates outside topological support.

## ii. Key results

> - `ClassicalFieldTheory.Local.jetCoordinatesAt_contDiff`
> - `ClassicalFieldTheory.Local.jetBaseCoordinates_contDiff`
> - `ClassicalFieldTheory.Local.jetCoordinatesAt_eq_zero_of_notMem_tsupport`
> - `ClassicalFieldTheory.Local.jetDirectionAt_eq_zero_of_notMem_tsupport`

## iv. References

> * None.

## A. Smoothness of jet-coordinate maps

**`ClassicalFieldTheory.Local.jetCoordinatesAt_contDiff`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointRegularity.lean#L56).

> Smoothness of the jet-coordinate map of a smooth field.

```lean
lemma jetCoordinatesAt_contDiff (k : ℕ) (g : Space d → EuclideanSpace ℝ (Fin m))
    (hg : ContDiff ℝ ∞ g) :
    ContDiff ℝ ∞ (jetCoordinatesAt k g)
```

**`ClassicalFieldTheory.Local.jetBaseCoordinates_contDiff`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointRegularity.lean#L69).

> Smoothness of the base-plus-coordinate jet map of a smooth field.

```lean
lemma jetBaseCoordinates_contDiff (k : ℕ) (g : Space d → EuclideanSpace ℝ (Fin m))
    (hg : ContDiff ℝ ∞ g) :
    ContDiff ℝ ∞ (fun x : Space d => (x, jetCoordinatesAt k g x))
```

## B. Support and vanishing lemmas

**`ClassicalFieldTheory.Local.jetCoordinatesAt_eq_zero_of_notMem_tsupport`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointRegularity.lean#L87).

> Outside the topological support of a field, all of its jet coordinates vanish.

```lean
lemma jetCoordinatesAt_eq_zero_of_notMem_tsupport (k : ℕ)
    (g : Space d → EuclideanSpace ℝ (Fin m)) {x : Space d}
    (hx : x ∉ tsupport g) :
    jetCoordinatesAt k g x = 0
```

**`ClassicalFieldTheory.Local.jetDirectionAt_eq_zero_of_notMem_tsupport`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointRegularity.lean#L96).

> Outside the topological support of a field, the corresponding jet-fiber direction vanishes.

```lean
lemma jetDirectionAt_eq_zero_of_notMem_tsupport (k : ℕ)
    (g : Space d → EuclideanSpace ℝ (Fin m)) {x : Space d}
    (hx : x ∉ tsupport g) :
    jetDirectionAt k g x = 0
```

## Depends on

- [Fiber directions on jet points](jetpointfiber.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/Local/JetPointRegularity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointRegularity.lean)
