---
declaration: theorem
origin: cited
lean: TauCeti.IsGoodCycle.apply_self_eq_zero_of_one_lt_mult
statement: formalized
proof: formalized
---

# TauCeti.IsGoodCycle.apply\_self\_eq\_zero\_of\_one\_lt\_mult

An image occurring with multiplicity at least two has square zero.

```lean
TauCeti.IsGoodCycle.apply_self_eq_zero_of_one_lt_mult.{u_1, u_2, u_3} {H : Type u_1} {ι : Type u_2}
  {P : Type u_3} [AddCommGroup H] [Fintype ι] {B : LinearMap.BilinForm ℤ H} {κ e : H} {C : ι → H}
  {m : ι → ℕ} [Fintype P] {δ : ι → ℕ} {pts : ι → Finset P} (hB : B.IsSymm)
  (h : TauCeti.IsGoodCycle B κ e C m δ pts) {i : ι} (hi : 1 < m i) : (B (C i)) (C i) = 0
```

## Depends on

- [TauCeti.IsGoodCycle](tauceti-isgoodcycle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsGoodCycle.apply_self_eq_zero_of_one_lt_mult`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/GoodCycle.html#TauCeti.IsGoodCycle.apply_self_eq_zero_of_one_lt_mult).

## Sources

- [Tau Ceti documentation: `TauCeti.IsGoodCycle.apply_self_eq_zero_of_one_lt_mult`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/GoodCycle.html#TauCeti.IsGoodCycle.apply_self_eq_zero_of_one_lt_mult)
- [Source of `TauCeti.IsGoodCycle.apply_self_eq_zero_of_one_lt_mult` in TauCeti/Geometry/Symplectic/JHolomorphic/GoodCycle.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/JHolomorphic/GoodCycle.lean#L349)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TaubesGromov/STATUS.md)
