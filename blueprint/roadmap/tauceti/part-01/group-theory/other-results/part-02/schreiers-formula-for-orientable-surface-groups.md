---
declaration: theorem
origin: cited
lean: TauCeti.SurfaceGroup.Orientable.rank_eq_one_sub_index_mul_eulerChar, TauCeti.SurfaceGroup.Nonorientable.rank_eq_one_sub_index_mul_eulerChar
statement: formalized
proof: formalized
---

# Schreier's formula for orientable surface groups with boundary

A subgroup `H` of finite
index `n` of `S⁺(g, m + 1)` has rank `1 - n * χ`, where `χ = 1 - 2g - m` is the Euler
characteristic of the surface.

```lean
TauCeti.SurfaceGroup.Orientable.rank_eq_one_sub_index_mul_eulerChar {g m : ℕ}
  (H : Subgroup (TauCeti.SurfaceGroup.Orientable g (m + 1))) [H.FiniteIndex] :
  ↑(Group.rank ↥H) = 1 - ↑H.index * TauCeti.SurfaceGroup.Orientable.eulerChar g (m + 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Schreier's index formula (`Subgroup.rank_sub_one_eq_index_mul_rank_sub_one`)](../../free-groups-equations-over-groups-and-limit-grou/schreiers-index-formula-subgroup-rank-sub-one-eq.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SurfaceGroup.Orientable.rank_eq_one_sub_index_mul_eulerChar`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SurfaceGroup/FiniteIndex.html#TauCeti.SurfaceGroup.Orientable.rank_eq_one_sub_index_mul_eulerChar).

## Other forms

**Schreier's formula for nonorientable surface groups with boundary.** Formalized in Tau Ceti as [`TauCeti.SurfaceGroup.Nonorientable.rank_eq_one_sub_index_mul_eulerChar`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SurfaceGroup/FiniteIndex.html#TauCeti.SurfaceGroup.Nonorientable.rank_eq_one_sub_index_mul_eulerChar).

```lean
TauCeti.SurfaceGroup.Nonorientable.rank_eq_one_sub_index_mul_eulerChar {g m : ℕ}
  (H : Subgroup (TauCeti.SurfaceGroup.Nonorientable g (m + 1))) [H.FiniteIndex] :
  ↑(Group.rank ↥H) = 1 - ↑H.index * TauCeti.SurfaceGroup.Nonorientable.eulerChar g (m + 1)
```

## Sources

- [Tau Ceti documentation: `TauCeti.SurfaceGroup.Orientable.rank_eq_one_sub_index_mul_eulerChar`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SurfaceGroup/FiniteIndex.html#TauCeti.SurfaceGroup.Orientable.rank_eq_one_sub_index_mul_eulerChar)
- [Source of `TauCeti.SurfaceGroup.Orientable.rank_eq_one_sub_index_mul_eulerChar` in TauCeti/GroupTheory/SurfaceGroup/FiniteIndex.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/SurfaceGroup/FiniteIndex.lean#L55)
