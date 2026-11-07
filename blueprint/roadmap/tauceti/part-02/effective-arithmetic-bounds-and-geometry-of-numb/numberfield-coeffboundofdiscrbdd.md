---
declaration: def
origin: cited
lean: NumberField.coeffBoundOfDiscrBdd
statement: formalized
---

# NumberField.coeffBoundOfDiscrBdd

An explicit height bound for the integer minimal polynomial of a primitive generator of a number
field of discriminant `≤ N`. It is `⌈M ^ D * (D.choose (D / 2))⌉₊` where `D = rankOfDiscrBdd N` is
Mathlib's degree bound and `M = max √(1 + boundOfDiscBdd N ^ 2) 1` dominates the per-conjugate bound
of both the real and complex primitive elements of `finite_of_discr_bdd`.

```lean
NumberField.coeffBoundOfDiscrBdd (N : ℕ) : ℕ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NumberField.coeffBoundOfDiscrBdd`](https://taucetiproject.org/docs/TauCeti/NumberTheory/EffectiveBounds/HermiteCount/Basic.html#NumberField.coeffBoundOfDiscrBdd).

## Sources

- [Tau Ceti documentation: `NumberField.coeffBoundOfDiscrBdd`](https://taucetiproject.org/docs/TauCeti/NumberTheory/EffectiveBounds/HermiteCount/Basic.html#NumberField.coeffBoundOfDiscrBdd)
- [Source of `NumberField.coeffBoundOfDiscrBdd` in TauCeti/NumberTheory/EffectiveBounds/HermiteCount/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/EffectiveBounds/HermiteCount/Basic.lean#L74)
- [Tau Ceti roadmap status: Effective arithmetic bounds and geometry of numbers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/EffectiveBounds/STATUS.md)
