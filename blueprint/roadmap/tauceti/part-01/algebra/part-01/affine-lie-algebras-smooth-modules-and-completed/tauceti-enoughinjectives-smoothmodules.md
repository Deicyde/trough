---
declaration: theorem
origin: cited
lean: TauCeti.enoughInjectives_smoothModules
statement: formalized
proof: formalized
---

# TauCeti.enoughInjectives_smoothModules

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
- [Source of `TauCeti.enoughInjectives_smoothModules` in TauCeti/Algebra/Category/ModuleCat/Smooth/Coinduction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Category/ModuleCat/Smooth/Coinduction.lean#L234)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
