---
declaration: theorem
origin: cited
lean: Equiv.Perm.movedNorm_parityRetract_le
statement: formalized
proof: formalized
---

# Equiv.Perm.movedNorm_parityRetract_le

The parity retraction does not increase the moved-point norm.

```lean
Equiv.Perm.movedNorm_parityRetract_le.{u_1} {α : Type u_1} [Fintype α] [DecidableEq α]
  {t : Equiv.Perm α} (ht : t.IsSwap) (σ : Equiv.Perm α) :
  (Equiv.Perm.movedNorm α) ((Equiv.Perm.parityRetract ht) σ) ≤ (Equiv.Perm.movedNorm α) σ
```

## Depends on

- [Equiv.Perm.movedNorm](equiv-perm-movednorm.md)

## Lean

Formalized in Tau Ceti as [`Equiv.Perm.movedNorm_parityRetract_le`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Perm/ParityRetract.html#Equiv.Perm.movedNorm_parityRetract_le).

## Sources

- [Tau Ceti documentation: `Equiv.Perm.movedNorm_parityRetract_le`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Perm/ParityRetract.html#Equiv.Perm.movedNorm_parityRetract_le)
- [Source of `Equiv.Perm.movedNorm_parityRetract_le` in TauCeti/GroupTheory/Perm/ParityRetract.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Perm/ParityRetract.lean#L106)
- [Tau Ceti roadmap status: Coboundary expansion with group coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CoboundaryExpansion/STATUS.md)
