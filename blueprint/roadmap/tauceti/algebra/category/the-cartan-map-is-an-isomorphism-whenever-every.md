---
declaration: theorem
origin: cited
lean: TauCeti.cartanMap_bijective
statement: formalized
proof: formalized
---

# The Cartan map is an isomorphism whenever every finitely generated `R`-module admits a finite resolution by finitely generated projective modules; this is the bijectivity statement of `TauCeti.cartanEquiv`

```lean
TauCeti.cartanMap_bijective.{u} (R : Type u) [Ring R]
  (h :
    ModuleCat.isFG R ≤
      (TauCeti.ExactStructure.abelian (ModuleCat R)).admitsFiniteResolution
        (TauCeti.finiteProjectiveModules R)) :
  Function.Bijective ⇑(TauCeti.cartanMap R)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The dual Noether isomorphism](../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)
- [The resolution theorem for modules](the-resolution-theorem-for-modules.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cartanMap_bijective`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/CartanMap/Basic.html#TauCeti.cartanMap_bijective).

## Sources

- [Tau Ceti documentation: `TauCeti.cartanMap_bijective`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/CartanMap/Basic.html#TauCeti.cartanMap_bijective)
- [Source of `TauCeti.cartanMap_bijective` in TauCeti/Algebra/Category/ModuleCat/CartanMap/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/ModuleCat/CartanMap/Basic.lean#L727)
