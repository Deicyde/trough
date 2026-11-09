---
declaration: theorem
origin: cited
lean: TauCeti.zpowHat_eq_padicPow_component
statement: formalized
proof: formalized
---

# The `ℓ`-adic comparison

On a pro-`ℓ` group, the profinite power by `a` is Tau Ceti's
`ℓ`-adic power by the `ℓ`-adic component of `a`.

```lean
TauCeti.zpowHat_eq_padicPow_component.{u, v} {G : Type v} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G] {ℓ : ℕ} [Fact (Nat.Prime ℓ)]
  (hG : TauCeti.IsProP ℓ G) (x : G) (a : Additive ↑TauCeti.zHat.toProfinite.toTop) :
  TauCeti.zpowHat x a = hG.padicPow x ((TauCeti.zHat.component ℓ) a)
```

## Depends on

- [The profinite power](the-profinite-power.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.zpowHat_eq_padicPow_component`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Pow.html#TauCeti.zpowHat_eq_padicPow_component).

## Sources

- [Tau Ceti documentation: `TauCeti.zpowHat_eq_padicPow_component`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Pow.html#TauCeti.zpowHat_eq_padicPow_component)
- [Source of `TauCeti.zpowHat_eq_padicPow_component` in TauCeti/Topology/Algebra/Group/Profinite/ZHat/Pow.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Pow.lean#L259)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteArithmetic/STATUS.md)
