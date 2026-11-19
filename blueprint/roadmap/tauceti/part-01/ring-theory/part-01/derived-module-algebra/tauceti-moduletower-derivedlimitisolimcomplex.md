---
declaration: def
origin: cited
lean: TauCeti.ModuleTower.derivedLimitIsoLimComplex
statement: formalized
---

# TauCeti.ModuleTower.derivedLimitIsoLimComplex

For a complex of towers whose terms have vanishing `lim¹`, for instance towers with surjective
transitions, the derived limit is the termwise limit: `Rlim K ≅ lim K` in `D(R)`, through the
comparison map `lim K → holim K`.

```lean
TauCeti.ModuleTower.derivedLimitIsoLimComplex.{w, w', v, u} {R : Type u} [Ring R]
  [HasDerivedCategory (TauCeti.ModuleTower R)] [HasDerivedCategory (ModuleCat R)]
  (K : CochainComplex (TauCeti.ModuleTower R) ℤ) (hK : ∀ (i : ℤ), Subsingleton (K.X i).limOne) :
  (TauCeti.ModuleTower.derivedLimit R).obj (DerivedCategory.Q.obj K) ≅
    DerivedCategory.Q.obj ((TauCeti.ModuleTower.limComplexFunctor R).obj K)
```

## Depends on

- [TauCeti.ModuleTower.derivedLimit](tauceti-moduletower-derivedlimit.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ModuleTower.derivedLimitIsoLimComplex`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Tower/DerivedLimit.html#TauCeti.ModuleTower.derivedLimitIsoLimComplex).

## Sources

- [Tau Ceti documentation: `TauCeti.ModuleTower.derivedLimitIsoLimComplex`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Tower/DerivedLimit.html#TauCeti.ModuleTower.derivedLimitIsoLimComplex)
- [Source of `TauCeti.ModuleTower.derivedLimitIsoLimComplex` in TauCeti/Algebra/Category/ModuleCat/Tower/DerivedLimit.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Category/ModuleCat/Tower/DerivedLimit.lean#L413)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
