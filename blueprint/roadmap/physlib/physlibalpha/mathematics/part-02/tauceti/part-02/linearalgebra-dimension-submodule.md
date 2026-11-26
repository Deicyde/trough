---
declaration: module
origin: cited
lean: Submodule.inf_ne_bot_of_finrank_lt
statement: formalized
proof: formalized
---

# Intersections of submodules by dimension

The module `PhyslibAlpha.Mathematics.TauCeti.LinearAlgebra.Dimension.Submodule`, [PhyslibAlpha/Mathematics/TauCeti/LinearAlgebra/Dimension/Submodule.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/TauCeti/LinearAlgebra/Dimension/Submodule.lean): 1 declaration, 1 with a docstring.

> A dimension-counting criterion for nontrivial submodule intersection.

## i. Overview

> A dimension-counting criterion for nontrivial submodule intersection.

## ii. Key results

> This file proves the statement described in the overview.

## iv. References

> * Standard material; the statements and proofs are original to this formalization.

## A. Development

**`Submodule.inf_ne_bot_of_finrank_lt`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/TauCeti/LinearAlgebra/Dimension/Submodule.lean#L44).

> Two subspaces whose dimensions sum to more than the dimension of the ambient
> space have nontrivial intersection.

```lean
lemma inf_ne_bot_of_finrank_lt [FiniteDimensional 𝕜 E] {V W : Submodule 𝕜 E}
    (h : finrank 𝕜 E < finrank 𝕜 V + finrank 𝕜 W) : V ⊓ W ≠ ⊥
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/LinearAlgebra/Dimension/Submodule.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/TauCeti/LinearAlgebra/Dimension/Submodule.lean)
