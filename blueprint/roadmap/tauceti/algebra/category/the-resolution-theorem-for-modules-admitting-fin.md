---
declaration: def
origin: cited
lean: TauCeti.moduleResolutionEquiv
statement: formalized
---

# The resolution theorem for modules admitting finite resolutions by finitely generated projectives

their exact `K₀` is the exact `K₀` of the finitely generated projective modules.
This is `TauCeti.ExactStructure.resolutionEquiv` in `ModuleCat R`; its inverse sends the class of a
module to the alternating class of any such resolution.

```lean
TauCeti.moduleResolutionEquiv.{u} (R : Type u) [Ring R] :
  TauCeti.ExactK0 (TauCeti.finiteProjectiveModulesExactStructure R) ≃+
    TauCeti.ExactK0 (TauCeti.finiteProjectiveResolutionExactStructure R)
```

## Depends on

- [The resolution theorem for finite projective resolutions](../../category-theory/grothendieck-group/the-resolution-theorem-for-finite-projective-res.md)

## Proof depends on

- [The dual Noether isomorphism](../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.moduleResolutionEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/CartanMap/Basic.html#TauCeti.moduleResolutionEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.moduleResolutionEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/CartanMap/Basic.html#TauCeti.moduleResolutionEquiv)
- [Source of `TauCeti.moduleResolutionEquiv` in TauCeti/Algebra/Category/ModuleCat/CartanMap/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/ModuleCat/CartanMap/Basic.lean#L517)
