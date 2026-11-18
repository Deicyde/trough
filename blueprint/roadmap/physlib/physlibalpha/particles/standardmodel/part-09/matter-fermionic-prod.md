---
declaration: module
origin: cited
lean: StandardModel.FermionicAlgebra.evenOdd, StandardModel.FermionicAlgebra.prodEquiv
statement: formalized
proof: formalized
---

# The fermionic algebra of a direct sum

The module `PhyslibAlpha.Particles.StandardModel.Matter.Fermionic.Prod`, [PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/Prod.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/Prod.lean): 2 declarations, 2 with a docstring.

## i. Overview

> Two matter fields, valued in `V` and `W`, are jointly a single matter field valued in
> `V × W`; its fermionic algebra is the **exterior product** of the two individual fermionic
> algebras. That is the content of `FermionicAlgebra.prodEquiv`: an algebra equivalence
>
> `FermionicAlgebra (M.prod N h hσ) ≃ₐ[ℂ] (evenOdd V ᵍ⊗[ℂ] evenOdd W)`
>
> onto the graded tensor product of the two algebras with respect to their Fermi-parity
> gradings. The graded — as opposed to ordinary — tensor product is what makes generators of
> *different* species anticommute, as fermions must.
>
> The proof is two steps. First the component space of a direct sum is the direct sum of the
> component spaces (`JetComponentSpace.prodEquiv`) — duals and conjugates both split. Then the
> exterior algebra of a direct sum is the graded tensor product of the exterior algebras,
> which is `CliffordAlgebra.prodEquiv` specialized to the zero quadratic form.

## ii. Key results

> - `FermionicAlgebra.evenOdd` : the Fermi-parity grading.
> - `FermionicAlgebra.prodEquiv` : the fermionic algebra of a direct sum is the exterior
>   product of the fermionic algebras.

## iv. References

> * None.

## A. The component space of a direct sum

> The splitting `JetComponentSpace.prodEquiv` of the component space of a direct sum lives
> with the component space itself, in
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.JetComponent.Basic`.

## B. The Fermi-parity grading

**`StandardModel.FermionicAlgebra.evenOdd`**, an abbrev, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/Prod.lean#L80).

> **The Fermi-parity grading** of the fermionic algebra: the `ZMod 2` grading of the
> exterior algebra by the number of component functions in a monomial. An even element
> commutes with everything; two odd elements anticommute.

```lean
abbrev FermionicAlgebra.evenOdd (M : MatterField jets) :
    ZMod 2 → Submodule ℂ (FermionicAlgebra M)
```

## C. The exterior product decomposition

**`StandardModel.FermionicAlgebra.prodEquiv`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/Prod.lean#L97).

> **The fermionic algebra of a direct sum is the exterior product of the fermionic
> algebras.** Two matter fields taken together are one field valued in the direct sum of
> their target spaces, and its fermionic algebra is the graded tensor product of theirs.
>
> The tensor product must be the *graded* one `ᵍ⊗`: an ordinary `⊗[ℂ]` would make a
> generator of the first field commute with a generator of the second, whereas fermionic
> generators anticommute across species just as they do within one.

```lean
noncomputable def FermionicAlgebra.prodEquiv (M N : MatterField jets)
    (h : M.massWeight = N.massWeight) (hσ : M.statistic = N.statistic) :
    FermionicAlgebra (M.prod N h hσ) ≃ₐ[ℂ]
      (FermionicAlgebra.evenOdd M ᵍ⊗[ℂ] FermionicAlgebra.evenOdd N)
```

## Depends on

- [The direct sum of two matter fields](../../../classicalfieldtheory/gaugetheory/part-05/matterfield-prod.md)
- [Derivations and representations on the exterior algebra](../../../mathematics/part-01/exterioralgebra.md)
- [The fermionic algebra of a matter field](matter-fermionic-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/Prod.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/Prod.lean)
