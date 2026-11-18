---
declaration: module
origin: cited
lean: ProbabilisticTheory.IsGenerator, ProbabilisticTheory.IsGenerator.unique
statement: formalized
proof: formalized
---

# Generators of one-parameter groups

The module `PhyslibAlpha.ProbabilisticTheory.Dynamics.Generator`, [PhyslibAlpha/ProbabilisticTheory/Dynamics/Generator.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Dynamics/Generator.lean): 2 declarations, 2 with a docstring.

> The generator of a one-parameter family on a normed space, and its uniqueness.

## i. Overview

> The generator of a one-parameter family `α` on a normed space is `D a = lim\_\{t → 0} (α t a - a) /
> t`, stated with `HasDerivAt`. It needs a topology but no algebraic structure, and it is unique when
> it exists.

## ii. Key results

> - `IsGenerator` : `D` generates `α`.
> - `IsGenerator.unique` : the generator is unique.

## iv. References

> * None.

## A. The generator

**`ProbabilisticTheory.IsGenerator`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Dynamics/Generator.lean#L49).

> `D` is the infinitesimal generator, at `t = 0`, of the one-parameter family `α`: for every `a`,
> `t ↦ α t a` is differentiable at `0` with derivative `D a`. No algebraic structure on `E` (product,
> order, `⋆`) is assumed — this is purely about the curve `t ↦ α t a` in a normed space.

```lean
def IsGenerator (α : ℝ → E → E) (D : E → E) : Prop
```

**`ProbabilisticTheory.IsGenerator.unique`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Dynamics/Generator.lean#L54).

> The generator of a one-parameter family, if it exists, is unique — immediate from uniqueness of
> derivatives (`HasDerivAt.unique`).

```lean
lemma IsGenerator.unique {α : ℝ → E → E} {D₁ D₂ : E → E} (h₁ : IsGenerator α D₁)
    (h₂ : IsGenerator α D₂) : D₁ = D₂
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Dynamics/Generator.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Dynamics/Generator.lean)
