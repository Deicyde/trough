---
declaration: theorem
origin: cited
lean: Matrix.mem_closure_orbit_iff_forall_rank_pow_le, Matrix.mem_zeroLocus_vanishingIdeal_orbit_iff_forall_rank_pow_le
statement: formalized
proof: formalized
---

# Gerstenhaber's theorem

Over a field with continuous ring operations and closed points in
which `0` is not isolated, such as `ℂ`, a matrix `Y` lies in the closure of the conjugacy class of
a nilpotent matrix `X` exactly when `rank (Y ^ k) ≤ rank (X ^ k)` for every `k`.

```lean
Matrix.mem_closure_orbit_iff_forall_rank_pow_le.{u_1, u_2} {n : Type u_1} [Fintype n]
  [DecidableEq n] {K : Type u_2} [Field K] [TopologicalSpace K] [IsTopologicalRing K] [T1Space K]
  [(nhdsWithin 0 {0}ᶜ).NeBot] {X Y : Matrix n n K} (hX : IsNilpotent X) :
  Y ∈ closure (MulAction.orbit (ConjAct (GL n K)) X) ↔ ∀ (k : ℕ), (Y ^ k).rank ≤ (X ^ k).rank
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.mem_closure_orbit_iff_forall_rank_pow_le`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Rank/OrbitClosure.html#Matrix.mem_closure_orbit_iff_forall_rank_pow_le).

## Other forms

**Gerstenhaber's theorem, Zariski form.** Formalized in Tau Ceti as [`Matrix.mem_zeroLocus_vanishingIdeal_orbit_iff_forall_rank_pow_le`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Rank/OrbitClosure.html#Matrix.mem_zeroLocus_vanishingIdeal_orbit_iff_forall_rank_pow_le).

```lean
Matrix.mem_zeroLocus_vanishingIdeal_orbit_iff_forall_rank_pow_le.{u_1, u_2, u_3} {n : Type u_1}
  [Fintype n] [DecidableEq n] {K : Type u_2} [Field K] {k : Type u_3} [Field k] [Algebra k K]
  [Infinite K] {X Y : Matrix n n K} (hX : IsNilpotent X) :
  Function.uncurry Y ∈
      MvPolynomial.zeroLocus K
        (MvPolynomial.vanishingIdeal k (Function.uncurry '' MulAction.orbit (ConjAct (GL n K)) X)) ↔
    ∀ (j : ℕ), (Y ^ j).rank ≤ (X ^ j).rank
```

## Sources

- [Tau Ceti documentation: `Matrix.mem_closure_orbit_iff_forall_rank_pow_le`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Rank/OrbitClosure.html#Matrix.mem_closure_orbit_iff_forall_rank_pow_le)
- [Source of `Matrix.mem_closure_orbit_iff_forall_rank_pow_le` in TauCeti/LinearAlgebra/Matrix/Rank/OrbitClosure.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Matrix/Rank/OrbitClosure.lean#L276)
