---
declaration: def
origin: cited
lean: Module.SatisfiesSerreS
statement: formalized
---

# Module.SatisfiesSerreS

An `R`-module `M` satisfies *Serre's condition* `(S_n)` if for every prime `p` of `R` the depth
of `M_p` over `R_p` is at least `min (n, dim Supp M_p)`. This is meant for finite modules over a
Noetherian ring. Since the zero module has depth `⊤`, primes outside the support impose nothing.
Stacks, Definition 10.157.1 (031P).

```lean
Module.SatisfiesSerreS.{u, v} (n : ℕ) (R : Type u) [CommRing R] (M : Type v) [AddCommGroup M]
  [_root_.Module R M] : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Module.SatisfiesSerreS`](https://taucetiproject.org/docs/TauCeti/RingTheory/SerreCondition/Basic.html#Module.SatisfiesSerreS).

## Sources

- [Tau Ceti documentation: `Module.SatisfiesSerreS`](https://taucetiproject.org/docs/TauCeti/RingTheory/SerreCondition/Basic.html#Module.SatisfiesSerreS)
- [Source of `Module.SatisfiesSerreS` in TauCeti/RingTheory/SerreCondition/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/SerreCondition/Basic.lean#L80)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
