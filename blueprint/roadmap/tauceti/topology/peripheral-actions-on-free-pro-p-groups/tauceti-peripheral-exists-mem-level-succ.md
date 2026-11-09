---
declaration: theorem
origin: cited
lean: TauCeti.Peripheral.exists_mem_level_succ
statement: formalized
proof: formalized
---

# TauCeti.Peripheral.exists_mem_level_succ

A pair of conjugators whose defect lies in `γ_n`, for positive `n`, can be corrected so that
its defect lies in `γ_{n+1}`. The corrections lie in `γ_{n-1}`, and the correction at the first
basis element is trivial. The unit hypothesis on `u` is used to rescale the required graded
correction.

```lean
TauCeti.Peripheral.exists_mem_level_succ.{u_1} {p r : ℕ} [Fact (Nat.Prime p)] {F : Type u_1}
  [Group F] [TopologicalSpace F] [IsTopologicalGroup F] [CompactSpace F]
  [TotallyDisconnectedSpace F] (hF : TauCeti.IsProP p F) (e : F ≃ₜ* TauCeti.freeProP p (Fin r))
  (u : ℤ_[p]ˣ) (n : ℕ) (hn : 1 ≤ n) (c : Fin r → F) (d : F)
  (h : (c, d) ∈ TauCeti.Peripheral.level hF (TauCeti.Peripheral.basis e) (↑u) n) :
  ∃ c' d',
    (∀ (i : Fin r), c' i ∈ TauCeti.closedLowerCentralSeries F (n - 1)) ∧
      d' ∈ TauCeti.closedLowerCentralSeries F (n - 1) ∧
        (∀ (h0 : 0 < r), c' ⟨0, h0⟩ = 1) ∧
          (fun i => c i * c' i, d * d') ∈
            TauCeti.Peripheral.level hF (TauCeti.Peripheral.basis e) (↑u) (n + 1)
```

## Depends on

- [TauCeti.Peripheral.level](tauceti-peripheral-level.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Peripheral.exists_mem_level_succ`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Lifting.html#TauCeti.Peripheral.exists_mem_level_succ).

## Sources

- [Tau Ceti documentation: `TauCeti.Peripheral.exists_mem_level_succ`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Lifting.html#TauCeti.Peripheral.exists_mem_level_succ)
- [Source of `TauCeti.Peripheral.exists_mem_level_succ` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Lifting.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Lifting.lean#L134)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/PeripheralActions/STATUS.md)
