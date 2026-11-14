---
declaration: module
origin: cited
lean: Function.HasTemperateGrowth.prod
statement: formalized
proof: formalized
---

# Functions of temperate growth

The module `Physlib.Mathematics.ForMathlib.HasTemperateGrowth`, [Physlib/Mathematics/ForMathlib/HasTemperateGrowth.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/HasTemperateGrowth.lean): 1 declaration, 1 with a docstring.

> This file is intended to collect useful general properties of `HasTemperateGrowth` which are not
> (yet) in Mathlib.

**`Function.HasTemperateGrowth.prod`**, a lemma, [line 25](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/HasTemperateGrowth.lean#L25).

> The finite product of functions of temperate growth is again of temperate growth.

```lean
lemma prod {ι : Type*} {s : Finset ι} {E F : Type*} [NormedAddCommGroup E]
    [NormedSpace ℝ E] [NormedCommRing F] [NormedAlgebra ℝ F] {f : ι → E → F}
    (hf : ∀ i ∈ s, HasTemperateGrowth (f i)) : HasTemperateGrowth (∏ i ∈ s, f i)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/HasTemperateGrowth.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/HasTemperateGrowth.lean)
