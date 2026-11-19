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
- [Source of `Equiv.Perm.movedNorm_parityRetract_le` in TauCeti/GroupTheory/Perm/ParityRetract.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/Perm/ParityRetract.lean#L106)
- [Tau Ceti roadmap status: Coboundary expansion with group coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CoboundaryExpansion/STATUS.md)
