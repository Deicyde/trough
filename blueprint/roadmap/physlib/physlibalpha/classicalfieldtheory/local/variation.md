---
declaration: module
origin: cited
lean: ClassicalFieldTheory.Local.AdmissibleVariation.coord_euclidean
statement: formalized
proof: formalized
---

# Alpha extensions for admissible local variations

The module `PhyslibAlpha.ClassicalFieldTheory.Local.Variation`, [PhyslibAlpha/ClassicalFieldTheory/Local/Variation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Variation.lean): 1 declaration, 1 with a docstring.

> Euclidean components of admissible variations are test functions.

## i. Overview

> This module adds the Euclidean component API needed by the coordinate-readout CFT stack in
> `PhyslibAlpha`.
>
> The underlying `AdmissibleVariation` structure remains the maintained one from `Physlib`; this file
> only adds helper lemmas used by the Alpha development.

## ii. Key results

> - `ClassicalFieldTheory.Local.AdmissibleVariation.coord_euclidean` : a Euclidean component of an
>   admissible variation is again a test function.

## iv. References

> * None.

## A. Euclidean components of admissible variations

**`ClassicalFieldTheory.Local.AdmissibleVariation.coord_euclidean`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Variation.lean#L56).

> A Euclidean component of an admissible variation is again a test function.

```lean
lemma coord_euclidean (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m))) (a : Fin m) :
    IsTestFunction (fun x => (η.toFun x) a)
```

## Depends on

- [Admissible local variations](../../../physlib/classicalfieldtheory/local/variation.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/Local/Variation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Variation.lean)
