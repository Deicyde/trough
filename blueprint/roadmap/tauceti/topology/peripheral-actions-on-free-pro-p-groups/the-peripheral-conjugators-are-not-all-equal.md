---
declaration: theorem
origin: cited
lean: TauCeti.Peripheral.exists_ne_of_apply_eq_conj
statement: formalized
proof: formalized
---

# The peripheral conjugators are not all equal

For a free pro-`p` group of rank at least
two and `u ∈ ℤ_p` other than `0` and `1`, if an endomorphism `φ` satisfies
`φ (x i) = (c i)⁻¹ * x i ^ u * c i` for every basis element and `φ z = d⁻¹ * z ^ u * d` on the
cusp, then some `c i` differs from `d`.

```lean
TauCeti.Peripheral.exists_ne_of_apply_eq_conj.{u_1, u_2} {p : ℕ} [Fact (Nat.Prime p)] {F : Type u_1}
  [Group F] [TopologicalSpace F] [IsTopologicalGroup F] [CompactSpace F]
  [TotallyDisconnectedSpace F] {M : Type u_2} [FunLike M F F] [MonoidHomClass M F F] {n : ℕ}
  (hF : TauCeti.IsProP p F) (e : F ≃ₜ* TauCeti.freeProP p (Fin (n + 2))) {u : ℤ_[p]} (hu₀ : u ≠ 0)
  (hu₁ : u ≠ 1) (φ : M) {c : Fin (n + 2) → F} {d : F}
  (hc :
    ∀ (i : Fin (n + 2)),
      φ (TauCeti.Peripheral.basis e i) =
        (c i)⁻¹ * hF.padicPow (TauCeti.Peripheral.basis e i) u * c i)
  (hd :
    φ (TauCeti.Peripheral.cusp (TauCeti.Peripheral.basis e)) =
      d⁻¹ * hF.padicPow (TauCeti.Peripheral.cusp (TauCeti.Peripheral.basis e)) u * d) :
  ∃ i, c i ≠ d
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Peripheral.exists_ne_of_apply_eq_conj`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Conjugator.html#TauCeti.Peripheral.exists_ne_of_apply_eq_conj).

## Sources

- [Tau Ceti documentation: `TauCeti.Peripheral.exists_ne_of_apply_eq_conj`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Conjugator.html#TauCeti.Peripheral.exists_ne_of_apply_eq_conj)
- [Source of `TauCeti.Peripheral.exists_ne_of_apply_eq_conj` in TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Conjugator.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/Peripheral/Conjugator.lean#L111)
- [Tau Ceti roadmap status: Peripheral actions on free pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/PeripheralActions/STATUS.md)
