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

Formalized in Tau Ceti as [`Equiv.Perm.distErr`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Perm/DistErr.html#Equiv.Perm.distErr).

## Sources

- [Tau Ceti documentation: `Equiv.Perm.distErr`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Perm/DistErr.html#Equiv.Perm.distErr)
- [Source of `Equiv.Perm.distErr` in TauCeti/GroupTheory/Perm/DistErr.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Perm/DistErr.lean#L50)
- [Tau Ceti roadmap status: Coboundary expansion with group coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CoboundaryExpansion/STATUS.md)
