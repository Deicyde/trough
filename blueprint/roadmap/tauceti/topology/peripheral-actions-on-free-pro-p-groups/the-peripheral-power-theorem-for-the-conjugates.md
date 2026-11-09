---
declaration: theorem
origin: cited
lean: TauCeti.Peripheral.exists_peripheralAut_conj_cusp
statement: formalized
proof: formalized
---

# The peripheral-power theorem for the conjugates of the cusp

For every unit `u ∈ ℤ_pˣ`
there are a continuous automorphism `φ` of `F`, conjugators `c` on the basis `x = basis e`, with
`c 0 = 1` in positive rank, and `d : F`, such that `φ (x i) = (c i)⁻¹ * x i ^ u * c i` for every
`i` and, for every `q : F`, `φ` carries the conjugate `y = q * cusp x * q⁻¹` of the cusp to
`d'⁻¹ * y ^ u * d'` with `d' = q * d * (φ q)⁻¹`. At `q = 1` the conjugator is `d`.

```lean
TauCeti.Peripheral.exists_peripheralAut_conj_cusp.{u_1} {p r : ℕ} [Fact (Nat.Prime p)]
  {F : Type u_1} [Group F] [TopologicalSpace F] [IsTopologicalGroup F] [CompactSpace F]
  [TotallyDisconnectedSpace F] (hF : TauCeti.IsProP p F) (e : F ≃ₜ* TauCeti.freeProP p (Fin r))
  (u : ℤ_[p]ˣ) :
  ∃ φ c d,
    (∀ (h0 : 0 < r), c ⟨0, h0⟩ = 1) ∧
      (∀ (i : Fin r),
          φ (TauCeti.Peripheral.basis e i) =
            (c i)⁻¹ * hF.padicPow (TauCeti.Peripheral.basis e i) ↑u * c i) ∧
        ∀ (q : F),
          φ (q * TauCeti.Peripheral.cusp (TauCeti.Peripheral.basis e) * q⁻¹) =
            (q * d * (φ q)⁻¹)⁻¹ *
                hF.padicPow (q * TauCeti.Peripheral.cusp (TauCeti.Peripheral.basis e) * q⁻¹) ↑u *
              (q * d * (φ q)⁻¹)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The peripheral-power theorem](the-peripheral-power-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Peripheral.exists_peripheralAut_conj_cusp`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Automorphism.html#TauCeti.Peripheral.exists_peripheralAut_conj_cusp).

## Sources

- [Tau Ceti documentation: `TauCeti.Peripheral.exists_peripheralAut_conj_cusp`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Automorphism.html#TauCeti.Peripheral.exists_peripheralAut_conj_cusp)
- [Source of `TauCeti.Peripheral.exists_peripheralAut_conj_cusp` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Automorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Automorphism.lean#L82)
