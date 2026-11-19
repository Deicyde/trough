---
declaration: theorem
origin: cited
lean: TauCeti.IsIwanagaGorenstein.isEquivalence_toSingularityCategory, TauCeti.IsIwanagaGorenstein.essSurj_toSingularityCategory
statement: formalized
proof: formalized
---

# Buchweitz's theorem

over an Iwanaga–Gorenstein ring, Chen's functor from the stable
category of finitely generated Gorenstein-projective modules to the singularity category is an
equivalence of categories.

```lean
TauCeti.IsIwanagaGorenstein.isEquivalence_toSingularityCategory.{w, u} {A : Type u} [Ring A]
  [TauCeti.IsIwanagaGorenstein A] [HasDerivedCategory (FGModuleCat A)] :
  (CategoryTheory.GorensteinProjective.toSingularityCategory (FGModuleCat A)).IsEquivalence
```

## Depends on

- [TauCeti.SingularityCategory](../../part-01/stable-periodic-and-curved-homological-algebra/tauceti-singularitycategory.md)

## Proof depends on

- [Auslander–Bridger](auslander-bridger.md)
- [Chen's theorem, fullness](../../part-01/stable-periodic-and-curved-homological-algebra/chens-theorem-fullness.md)
- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsIwanagaGorenstein.isEquivalence_toSingularityCategory`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/GorensteinProjective/Buchweitz.html#TauCeti.IsIwanagaGorenstein.isEquivalence_toSingularityCategory).

## Other forms

**Buchweitz's theorem, density.** Formalized in Tau Ceti as [`TauCeti.IsIwanagaGorenstein.essSurj_toSingularityCategory`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/GorensteinProjective/Buchweitz.html#TauCeti.IsIwanagaGorenstein.essSurj_toSingularityCategory).

```lean
TauCeti.IsIwanagaGorenstein.essSurj_toSingularityCategory.{w, u} {A : Type u} [Ring A]
  [TauCeti.IsIwanagaGorenstein A] [HasDerivedCategory (FGModuleCat A)] :
  (CategoryTheory.GorensteinProjective.toSingularityCategory (FGModuleCat A)).EssSurj
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsIwanagaGorenstein.isEquivalence_toSingularityCategory`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/GorensteinProjective/Buchweitz.html#TauCeti.IsIwanagaGorenstein.isEquivalence_toSingularityCategory)
- [Source of `TauCeti.IsIwanagaGorenstein.isEquivalence_toSingularityCategory` in TauCeti/Algebra/Homology/GorensteinProjective/Buchweitz.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Homology/GorensteinProjective/Buchweitz.lean#L73)
