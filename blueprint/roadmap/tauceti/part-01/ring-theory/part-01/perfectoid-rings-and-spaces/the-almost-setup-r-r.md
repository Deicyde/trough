---
declaration: def
origin: cited
lean: TauCeti.Perfectoid.almostSetup
statement: formalized
---

# The almost setup `(R°, R°°)`

**The almost setup `(R°, R°°)`** of a Huber ring `R` admitting a pseudouniformiser with
compatible `p`-power roots, for instance of a perfectoid Tate ring: the ideal `R°°` of
topologically nilpotent elements of `R°` is idempotent and `R°° ⊗[R°] R°°` is flat. The setup
depends only on `R`, not on a choice of roots.

```lean
TauCeti.Perfectoid.almostSetup.{u_1} (p : ℕ) (R : Type u_1) [CommRing R] [TopologicalSpace R]
  [NonarchimedeanRing R] [Fact (1 < p)] [Nonempty (TauCeti.Perfectoid.PseudoUniformizerRoots p R)]
  [TauCeti.Huber.IsHuberRing R] : TauCeti.Almost.BasicSetup ↥(TauCeti.Huber.powerBoundedSubring R)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Perfectoid.almostSetup`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfectoid/AlmostSetup.html#TauCeti.Perfectoid.almostSetup).

## Sources

- [Tau Ceti documentation: `TauCeti.Perfectoid.almostSetup`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfectoid/AlmostSetup.html#TauCeti.Perfectoid.almostSetup)
- [Source of `TauCeti.Perfectoid.almostSetup` in TauCeti/RingTheory/Perfectoid/AlmostSetup.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Perfectoid/AlmostSetup.lean#L66)
- [Tau Ceti roadmap status: Perfectoid rings and spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PerfectoidSpaces/STATUS.md)
