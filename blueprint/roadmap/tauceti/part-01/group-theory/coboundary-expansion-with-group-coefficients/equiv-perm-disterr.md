---
declaration: def
origin: cited
lean: Equiv.Perm.distErr
statement: formalized
---

# Equiv.Perm.distErr

The distance with errors between a permutation of degree `n` and one of degree `m`:
one minus the proportion, among the `max n m` points of the larger degree, of common indices
where the two permutations agree.

```lean
Equiv.Perm.distErr {n m : ℕ} (σ : Equiv.Perm (Fin n)) (τ : Equiv.Perm (Fin m)) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Equiv.Perm.distErr`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Perm/DistErr/Basic.html#Equiv.Perm.distErr).

## Sources

- [Tau Ceti documentation: `Equiv.Perm.distErr`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Perm/DistErr/Basic.html#Equiv.Perm.distErr)
- [Source of `Equiv.Perm.distErr` in TauCeti/GroupTheory/Perm/DistErr/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/Perm/DistErr/Basic.lean#L58)
- [Tau Ceti roadmap status: Coboundary expansion with group coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CoboundaryExpansion/STATUS.md)
