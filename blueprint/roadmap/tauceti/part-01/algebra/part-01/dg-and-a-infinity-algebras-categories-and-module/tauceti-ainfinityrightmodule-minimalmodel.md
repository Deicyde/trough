---
declaration: def
origin: cited
lean: TauCeti.AInfinityRightModule.minimalModel
statement: formalized
---

# TauCeti.AInfinityRightModule.minimalModel

The **minimal model** of a right `A∞` module over a field: the right `A∞` module over the same
algebra on the homology `ker m₁ ⧸ im m₁` of its unary operation, transferred along the contraction
of the module onto this homology.  Its unary operation vanishes (`differential_minimalModel`).

```lean
TauCeti.AInfinityRightModule.minimalModel.{uK, uA, uM} {K : Type uK} {A : Type uA} {M : Type uM}
  [Field K] [AddCommGroup A] [_root_.Module K A] [AddCommGroup M] [_root_.Module K M]
  {AA : TauCeti.AInfinityAlgebra K A} (MM : TauCeti.AInfinityRightModule AA M) :
  TauCeti.AInfinityRightModule AA (MM.differential.homology ⋯)
```

## Depends on

- [TauCeti.AInfinityRightModule.transfer](tauceti-ainfinityrightmodule-transfer.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AInfinityRightModule.minimalModel`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Module/Right/Minimal/Model.html#TauCeti.AInfinityRightModule.minimalModel).

## Sources

- [Tau Ceti documentation: `TauCeti.AInfinityRightModule.minimalModel`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Module/Right/Minimal/Model.html#TauCeti.AInfinityRightModule.minimalModel)
- [Source of `TauCeti.AInfinityRightModule.minimalModel` in TauCeti/Algebra/Homology/AInfinity/Module/Right/Minimal/Model.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Homology/AInfinity/Module/Right/Minimal/Model.lean#L88)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DGAInfinity/STATUS.md)
