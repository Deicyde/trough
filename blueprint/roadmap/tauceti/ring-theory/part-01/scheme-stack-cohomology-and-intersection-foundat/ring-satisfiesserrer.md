---
declaration: def
origin: cited
lean: Ring.SatisfiesSerreR
statement: formalized
---

# Ring.SatisfiesSerreR

A ring `R` satisfies *Serre's condition* `(R_n)` if every prime of height at most `n` lies in
the regular locus, that is, `R_p` is a regular local ring whenever `ht p ≤ n`. Stacks,
Definition 10.157.1 (031P).

```lean
Ring.SatisfiesSerreR.{u} (n : ℕ) (R : Type u) [CommRing R] : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Ring.SatisfiesSerreR`](https://taucetiproject.org/docs/TauCeti/RingTheory/SerreCondition/Basic.html#Ring.SatisfiesSerreR).

## Sources

- [Tau Ceti documentation: `Ring.SatisfiesSerreR`](https://taucetiproject.org/docs/TauCeti/RingTheory/SerreCondition/Basic.html#Ring.SatisfiesSerreR)
- [Source of `Ring.SatisfiesSerreR` in TauCeti/RingTheory/SerreCondition/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/SerreCondition/Basic.lean#L195)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
