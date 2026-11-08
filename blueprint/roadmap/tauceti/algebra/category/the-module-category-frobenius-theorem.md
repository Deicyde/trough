---
declaration: theorem
origin: cited
lean: FGModuleCat.abelian_isFrobenius
statement: formalized
proof: formalized
---

# The module-category Frobenius theorem

For a finite-dimensional algebra `A` over a field
which is self-injective on both sides, the canonical exact structure on the category of finitely
generated (equivalently, finite-dimensional) `A`-modules is Frobenius.

```lean
FGModuleCat.abelian_isFrobenius.{u, v, w} (k : Type w) [Field k] {A : Type u} [Ring A] [Algebra k A]
  [FiniteDimensional k A] [Small.{v, u} A] [IsNoetherianRing A] (hl : Module.Injective A A)
  (hr : Module.Injective Aᵐᵒᵖ A) : (TauCeti.ExactStructure.abelian (FGModuleCat A)).IsFrobenius
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`FGModuleCat.abelian_isFrobenius`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/FGModuleCat/Frobenius.html#FGModuleCat.abelian_isFrobenius).

## Sources

- [Tau Ceti documentation: `FGModuleCat.abelian_isFrobenius`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/FGModuleCat/Frobenius.html#FGModuleCat.abelian_isFrobenius)
- [Source of `FGModuleCat.abelian_isFrobenius` in TauCeti/Algebra/Category/FGModuleCat/Frobenius.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/FGModuleCat/Frobenius.lean#L119)
