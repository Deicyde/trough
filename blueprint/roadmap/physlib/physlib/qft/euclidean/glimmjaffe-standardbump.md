---
declaration: module
origin: cited
lean: GlimmJaffe.standardBumpSequence
statement: formalized
proof: formalized
---

# Standard bump sequence

The module `Physlib.QFT.Euclidean.GlimmJaffe.StandardBump`, [Physlib/QFT/Euclidean/GlimmJaffe/StandardBump.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QFT/Euclidean/GlimmJaffe/StandardBump.lean): 1 declaration, 1 with a docstring.

> The mollifier sequence used in the OS1 endpoint condition of the Glimm–Jaffe axioms.

## i. Overview

> The OS1 endpoint condition smears the two-point function with a sequence of smooth bumps
> shrinking to the origin. This file fixes that sequence, following `OSforGFF`: the `n`-th bump
> on `EuclideanSpace ℝ (Fin (d + 1))` has inner radius `1 / (2n)` and outer radius `1 / n`.

## ii. Key results

> * `standardBumpSequence`: the standard bump sequence, defined for nonzero `n`.

## iv. References

> * Cherkis et al., *OSforGFF*. [ref: osforgff]

## A. The standard bump sequence

**`GlimmJaffe.standardBumpSequence`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QFT/Euclidean/GlimmJaffe/StandardBump.lean#L45).

> The standard bump sequence from `OSforGFF`, with outer radius `1 / n` for nonzero `n`.

```lean
def standardBumpSequence (n : ℕ) (hn : n ≠ 0) :
    ContDiffBump (0 : EuclideanSpace ℝ (Fin (d + 1)))
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/QFT/Euclidean/GlimmJaffe/StandardBump.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QFT/Euclidean/GlimmJaffe/StandardBump.lean)
