---
declaration: def
origin: cited
lean: TauCeti.cartanEquiv
statement: formalized
---

# The resolution theorem for modules

If every finitely generated `R`-module admits a finite
resolution by finitely generated projective modules, then the Cartan map
`K₀(proj R) ⟶ G₀(mod R)` is an isomorphism; its inverse sends the class of a module to the
alternating class of any such resolution.

```lean
TauCeti.cartanEquiv.{u} (R : Type u) [Ring R]
  (h :
    ModuleCat.isFG R ≤
      (TauCeti.ExactStructure.abelian (ModuleCat R)).admitsFiniteResolution
        (TauCeti.finiteProjectiveModules R)) :
  TauCeti.ExactK0 (TauCeti.finiteProjectiveModulesExactStructure R) ≃+
    TauCeti.ExactK0 (TauCeti.finiteModulesExactStructure R)
```

## Depends on

- [The resolution theorem for modules admitting finite resolutions by finitely generated projectives](the-resolution-theorem-for-modules-admitting-fin.md)

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)
- [The resolution theorem for finite projective resolutions](../../../category-theory/grothendieck-group/the-resolution-theorem-for-finite-projective-res.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cartanEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/CartanMap/Basic.html#TauCeti.cartanEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.cartanEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/CartanMap/Basic.html#TauCeti.cartanEquiv)
- [Source of `TauCeti.cartanEquiv` in TauCeti/Algebra/Category/ModuleCat/CartanMap/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Category/ModuleCat/CartanMap/Basic.lean#L737)
