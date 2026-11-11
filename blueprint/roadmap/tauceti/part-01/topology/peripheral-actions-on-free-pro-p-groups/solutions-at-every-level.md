---
declaration: theorem
origin: cited
lean: TauCeti.Peripheral.exists_mem_level
statement: formalized
proof: formalized
---

# Solutions at every level

For a unit `u`, every peripheral level of the basis
`x = basis e` of a free pro-`p` group contains a pair of conjugators whose conjugator at the
first basis element is trivial when the rank is positive.

```lean
TauCeti.Peripheral.exists_mem_level.{u_1} {p r : ℕ} [Fact (Nat.Prime p)] {F : Type u_1} [Group F]
  [TopologicalSpace F] [IsTopologicalGroup F] [CompactSpace F] [TotallyDisconnectedSpace F]
  (hF : TauCeti.IsProP p F) (e : F ≃ₜ* TauCeti.freeProP p (Fin r)) (u : ℤ_[p]ˣ) (n : ℕ) :
  ∃ c d,
    (∀ (h0 : 0 < r), c ⟨0, h0⟩ = 1) ∧
      (c, d) ∈ TauCeti.Peripheral.level hF (TauCeti.Peripheral.basis e) (↑u) n
```

## Depends on

- [TauCeti.Peripheral.level](tauceti-peripheral-level.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Peripheral.exists_mem_level`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Identity.html#TauCeti.Peripheral.exists_mem_level).

## Sources

- [Tau Ceti documentation: `TauCeti.Peripheral.exists_mem_level`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Identity.html#TauCeti.Peripheral.exists_mem_level)
- [Source of `TauCeti.Peripheral.exists_mem_level` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Identity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Identity.lean#L56)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/PeripheralActions/STATUS.md)
