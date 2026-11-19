---
declaration: def
origin: cited
lean: TauCeti.complexDescent
statement: formalized
---

# TauCeti.complexDescent

Real modules are equivalent to complex modules equipped with conjugation.
The unit is `w ↦ 1 ⊗ w`, and the counit is `z ⊗ w ↦ z • w`. The equivalence
includes naturality and both triangle identities.

```lean
TauCeti.complexDescent.{u} : ModuleCat ℝ ≌ TauCeti.StarModuleCat ℂ
```

## Depends on

- [TauCeti.StarModuleCat](tauceti-starmodulecat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.complexDescent`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/StarModuleCat/ComplexDescent.html#TauCeti.complexDescent).

## Sources

- [Tau Ceti documentation: `TauCeti.complexDescent`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/StarModuleCat/ComplexDescent.html#TauCeti.complexDescent)
- [Source of `TauCeti.complexDescent` in TauCeti/Algebra/Category/StarModuleCat/ComplexDescent.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Category/StarModuleCat/ComplexDescent.lean#L196)
- [Tau Ceti roadmap status: Local variational field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LocalVariationalFieldTheory/STATUS.md)
