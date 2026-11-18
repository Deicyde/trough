---
declaration: def
origin: cited
lean: TauCeti.coinduction
statement: formalized
---

# TauCeti.coinduction

The *coinduction* of `R`-modules to smooth `A`-modules along `f : R →+* A`: the smooth part of
the coextension of scalars `Hom_R(A, V)`, which is the module of continuous `R`-linear maps
`A → V` when the `J i` form a basis of neighborhoods of `0`
(`TauCeti.mem_smoothPart_coextendScalars_iff_continuous`).

```lean
TauCeti.coinduction.{w, u₁, u, u_1} {R : Type u₁} {A : Type u} [Ring R] [Ring A] (f : R →+* A)
  {ι : Type u_1} {J : ι → Submodule A A} [Nonempty ι] (hJ : Directed (fun x1 x2 => x1 ≥ x2) J) :
  CategoryTheory.Functor (ModuleCat R) (TauCeti.smoothModules J).FullSubcategory
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.coinduction`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Smooth/Coinduction.html#TauCeti.coinduction).

## Sources

- [Tau Ceti documentation: `TauCeti.coinduction`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Smooth/Coinduction.html#TauCeti.coinduction)
- [Source of `TauCeti.coinduction` in TauCeti/Algebra/Category/ModuleCat/Smooth/Coinduction.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Category/ModuleCat/Smooth/Coinduction.lean#L144)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
