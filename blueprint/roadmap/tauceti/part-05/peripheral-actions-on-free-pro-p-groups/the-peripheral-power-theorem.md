---
declaration: theorem
origin: cited
lean: TauCeti.Peripheral.exists_peripheralAut
statement: formalized
proof: formalized
---

# The peripheral-power theorem

For every unit `u ∈ ℤ_pˣ` there are a continuous
automorphism `φ` of `F`, conjugators `c` on the basis `x = basis e`, with `c 0 = 1` in positive
rank, and a conjugator `d` on the cusp, such that `φ (x i) = (c i)⁻¹ * x i ^ u * c i` for every
`i` and `φ (cusp x) = d⁻¹ * cusp x ^ u * d`, where `^ u` is the `p`-adic power.

```lean
TauCeti.Peripheral.exists_peripheralAut.{u_1} {p r : ℕ} [Fact (Nat.Prime p)] {F : Type u_1}
  [Group F] [TopologicalSpace F] [IsTopologicalGroup F] [CompactSpace F]
  [TotallyDisconnectedSpace F] (hF : TauCeti.IsProP p F) (e : F ≃ₜ* TauCeti.freeProP p (Fin r))
  (u : ℤ_[p]ˣ) :
  ∃ φ c d,
    (∀ (h0 : 0 < r), c ⟨0, h0⟩ = 1) ∧
      (∀ (i : Fin r),
          φ (TauCeti.Peripheral.basis e i) =
            (c i)⁻¹ * hF.padicPow (TauCeti.Peripheral.basis e i) ↑u * c i) ∧
        φ (TauCeti.Peripheral.cusp (TauCeti.Peripheral.basis e)) =
          d⁻¹ * hF.padicPow (TauCeti.Peripheral.cusp (TauCeti.Peripheral.basis e)) ↑u * d
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The peripheral product identity](the-peripheral-product-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Peripheral.exists_peripheralAut`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Automorphism.html#TauCeti.Peripheral.exists_peripheralAut).

## Sources

- [Tau Ceti documentation: `TauCeti.Peripheral.exists_peripheralAut`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Automorphism.html#TauCeti.Peripheral.exists_peripheralAut)
- [Source of `TauCeti.Peripheral.exists_peripheralAut` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Automorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Automorphism.lean#L64)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/PeripheralActions/STATUS.md)
