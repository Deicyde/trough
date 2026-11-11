---
declaration: theorem
origin: cited
lean: Equiv.Perm.hammingDist_eq_movedNorm
statement: formalized
proof: formalized
---

# Equiv.Perm.hammingDist_eq_movedNorm

The Hamming distance of two permutations is the moved-point norm of their quotient.

```lean
Equiv.Perm.hammingDist_eq_movedNorm.{u_1} {α : Type u_1} [Fintype α] [DecidableEq α]
  (σ τ : Equiv.Perm α) : ↑(hammingDist ⇑σ ⇑τ) = (Equiv.Perm.movedNorm α) (σ⁻¹ * τ)
```

## Depends on

- [Equiv.Perm.movedNorm](equiv-perm-movednorm.md)

## Lean

Formalized in Tau Ceti as [`Equiv.Perm.hammingDist_eq_movedNorm`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Perm/MovedNorm.html#Equiv.Perm.hammingDist_eq_movedNorm).

## Sources

- [Tau Ceti documentation: `Equiv.Perm.hammingDist_eq_movedNorm`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Perm/MovedNorm.html#Equiv.Perm.hammingDist_eq_movedNorm)
- [Source of `Equiv.Perm.hammingDist_eq_movedNorm` in TauCeti/GroupTheory/Perm/MovedNorm.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Perm/MovedNorm.lean#L58)
- [Tau Ceti roadmap status: Coboundary expansion with group coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CoboundaryExpansion/STATUS.md)
