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
- [Source of `Equiv.Perm.hammingDist_eq_movedNorm` in TauCeti/GroupTheory/Perm/MovedNorm.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/Perm/MovedNorm.lean#L58)
- [Tau Ceti roadmap status: Coboundary expansion with group coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CoboundaryExpansion/STATUS.md)
