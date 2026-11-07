---
declaration: theorem
origin: cited
lean: TauCeti.enoughInjectives_smoothModules
statement: formalized
proof: formalized
---

# TauCeti.enoughInjectives\_smoothModules

For a directed family `J` of left ideals of `A : Type u`, the smooth `A`-modules in universe
`max u w` have enough injectives: every smooth module embeds, through the unit of the coinduction
adjunction along `ℤ →+* A`, into the coinduction of an injective abelian group.

```lean
TauCeti.enoughInjectives_smoothModules.{w, u, u_1} {A : Type u} [Ring A] {ι : Type u_1}
  {J : ι → Submodule A A} [Nonempty ι] (hJ : Directed (fun x1 x2 => x1 ≥ x2) J) :
  CategoryTheory.EnoughInjectives (TauCeti.smoothModules J).FullSubcategory
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.coinduction](tauceti-coinduction.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.enoughInjectives_smoothModules`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Smooth/Coinduction.html#TauCeti.enoughInjectives_smoothModules).

## Sources

- [Tau Ceti documentation: `TauCeti.enoughInjectives_smoothModules`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Smooth/Coinduction.html#TauCeti.enoughInjectives_smoothModules)
- [Source of `TauCeti.enoughInjectives_smoothModules` in TauCeti/Algebra/Category/ModuleCat/Smooth/Coinduction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/ModuleCat/Smooth/Coinduction.lean#L234)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
