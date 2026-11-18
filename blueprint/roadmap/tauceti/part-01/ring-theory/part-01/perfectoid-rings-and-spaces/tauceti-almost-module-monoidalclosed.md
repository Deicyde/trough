---
declaration: instance
origin: cited
lean: TauCeti.Almost.Module.monoidalClosed
statement: formalized
---

# TauCeti.Almost.Module.monoidalClosed

Almost modules form a closed symmetric monoidal category, with internal Hom
the almostification of the module of almost morphisms.

```lean
TauCeti.Almost.Module.monoidalClosed.{u} {V : Type u} [CommRing V]
  (S : TauCeti.Almost.BasicSetup V) : CategoryTheory.MonoidalClosed (TauCeti.Almost.Module S)
```

## Depends on

- [TauCeti.Almost.Module](tauceti-almost-module.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Almost.Module.monoidalClosed`](https://taucetiproject.org/docs/TauCeti/RingTheory/Almost/Closed.html#TauCeti.Almost.Module.monoidalClosed).

## Sources

- [Tau Ceti documentation: `TauCeti.Almost.Module.monoidalClosed`](https://taucetiproject.org/docs/TauCeti/RingTheory/Almost/Closed.html#TauCeti.Almost.Module.monoidalClosed)
- [Source of `TauCeti.Almost.Module.monoidalClosed` in TauCeti/RingTheory/Almost/Closed.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Almost/Closed.lean#L115)
- [Tau Ceti roadmap status: Perfectoid rings and spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PerfectoidSpaces/STATUS.md)
