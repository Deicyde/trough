---
declaration: module
origin: cited
lean: StandardModel.BosonicAlgebra.prodEquiv
statement: formalized
proof: formalized
---

# The bosonic algebra of a direct sum

The module `PhyslibAlpha.Particles.StandardModel.Matter.Bosonic.Prod`, [PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/Prod.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/Prod.lean): 1 declaration, 1 with a docstring.

## i. Overview

> Two bosonic matter fields, valued in `V` and `W`, are jointly a single matter field valued
> in `V × W`; its bosonic algebra is the **tensor product** of the two individual bosonic
> algebras. That is the content of `BosonicAlgebra.prodEquiv`: an algebra equivalence
>
> `BosonicAlgebra (M.prod N h hσ) ≃ₐ[ℂ] BosonicAlgebra M ⊗[ℂ] BosonicAlgebra N`.
>
> Unlike the fermionic analogue `FermionicAlgebra.prodEquiv`, the *ordinary* tensor product
> suffices: bosonic generators of different species commute, so no grading is needed.
>
> The proof is two steps. First the component space of a direct sum is the direct sum of the
> component spaces (`JetComponentSpace.prodEquiv`). Then the symmetric algebra of a direct
> sum is the tensor product of the symmetric algebras, which is
> `SymmetricAlgebra.prodEquiv`.

## ii. Key results

> - `BosonicAlgebra.prodEquiv` : the bosonic algebra of a direct sum is the tensor product
>   of the bosonic algebras.

## iv. References

> * None.

## A. The tensor product decomposition

**`StandardModel.BosonicAlgebra.prodEquiv`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/Prod.lean#L65).

> **The bosonic algebra of a direct sum is the tensor product of the bosonic algebras.**
> Two bosonic matter fields taken together are one field valued in the direct sum of their
> target spaces, and its bosonic algebra is the tensor product of theirs. The ordinary —
> rather than the graded — tensor product is correct here: bosonic generators commute
> across species just as they do within one.

```lean
noncomputable def BosonicAlgebra.prodEquiv (M N : MatterField jets)
    (h : M.massWeight = N.massWeight) (hσ : M.statistic = N.statistic) :
    BosonicAlgebra (M.prod N h hσ) ≃ₐ[ℂ] BosonicAlgebra M ⊗[ℂ] BosonicAlgebra N
```

## Depends on

- [The direct sum of two matter fields](../../../classicalfieldtheory/gaugetheory/part-05/matterfield-prod.md)
- [The bosonic algebra of a matter field](matter-bosonic-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/Prod.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/Prod.lean)
