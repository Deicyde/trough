---
declaration: theorem
origin: cited
lean: CFSG.Milestones.burnside_schur
statement: formalized
proof: formalized
---

# QT_primitive_regular_cyclic_Burnside_Schur

The milestone module `CFSG.Milestones.QT_primitive_regular_cyclic_Burnside_Schur`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/QT_primitive_regular_cyclic_Burnside_Schur.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QT_primitive_regular_cyclic_Burnside_Schur.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.burnside_schur` (theorem, [line 12](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QT_primitive_regular_cyclic_Burnside_Schur.lean#L12)). Proved here.

```lean
theorem _root_.CFSG.Milestones.burnside_schur {Ω : Type*} [Finite Ω] (G K : Subgroup (Equiv.Perm Ω))
    (hΩ : 2 ≤ Nat.card Ω) (hKG : K ≤ G) [IsPreprimitive G Ω] [IsCyclic K]
    [IsPretransitive K Ω] (hK : ∀ x : Ω, stabilizer K x = ⊥) :
    IsMultiplyPretransitive G Ω 2 ∨
      ∃ p : ℕ, p.Prime ∧ Nat.card Ω = p ∧ ∃ e : Ω ≃ ZMod p,
        e.permCongr '' (K : Set (Equiv.Perm Ω)) = {t | ∃ b, ∀ x, t x = x + b} ∧
        (∀ g ∈ G, ∃ a ≠ 0, ∃ b, ∀ x, e (g x) = a * e x + b) ∧
        (K.subgroupOf G).Normal
```

No case theorem's file imports it, directly or through other files.

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/QT_primitive_regular_cyclic_Burnside_Schur.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QT_primitive_regular_cyclic_Burnside_Schur.lean)
