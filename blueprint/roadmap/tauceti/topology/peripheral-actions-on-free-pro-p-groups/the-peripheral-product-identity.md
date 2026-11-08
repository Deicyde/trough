---
declaration: theorem
origin: cited
lean: TauCeti.Peripheral.exists_defect_eq_one
statement: formalized
proof: formalized
---

# The peripheral product identity

For every unit `u ∈ ℤ_pˣ`, the basis `x = basis e` of a
free pro-`p` group admits conjugators `c` on the basis, with `c 0 = 1` in positive rank, and `d`
on the cusp such that `(∏_i (c i)⁻¹ * x i ^ u * c i) * (d⁻¹ * cusp x ^ u * d) = 1`, the product
taken in order and `^ u` the `p`-adic power.

```lean
TauCeti.Peripheral.exists_defect_eq_one.{u_1} {p r : ℕ} [Fact (Nat.Prime p)] {F : Type u_1}
  [Group F] [TopologicalSpace F] [IsTopologicalGroup F] [CompactSpace F]
  [TotallyDisconnectedSpace F] (hF : TauCeti.IsProP p F) (e : F ≃ₜ* TauCeti.freeProP p (Fin r))
  (u : ℤ_[p]ˣ) :
  ∃ c d,
    (∀ (h0 : 0 < r), c ⟨0, h0⟩ = 1) ∧
      TauCeti.Peripheral.defect hF (TauCeti.Peripheral.basis e) (↑u) c d = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The compactness step](the-compactness-step.md)
- [Solutions at every level](solutions-at-every-level.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Peripheral.exists_defect_eq_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Identity.html#TauCeti.Peripheral.exists_defect_eq_one).

## Sources

- [Tau Ceti documentation: `TauCeti.Peripheral.exists_defect_eq_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Identity.html#TauCeti.Peripheral.exists_defect_eq_one)
- [Source of `TauCeti.Peripheral.exists_defect_eq_one` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Identity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Identity.lean#L97)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/PeripheralActions/STATUS.md)
