---
declaration: theorem
origin: cited
lean: Matrix.exists_sinkhorn_scaling
statement: formalized
proof: formalized
---

# The Sinkhorn–Knopp theorem for a strictly positive kernel

a strictly positive matrix `K`
and strictly positive row sums `a` and column sums `b` of equal total mass admit strictly positive
row factors `u` and column factors `v` such that the diagonal scaling `u i * K i j * v j` has row
sums `a` and column sums `b`.

The scaled matrix is the minimiser of the relative entropy against `K` with these marginals.

```lean
Matrix.exists_sinkhorn_scaling.{u_1, u_2} {ι : Type u_1} {κ : Type u_2} [Fintype ι] [Fintype κ]
  {K : Matrix ι κ ℝ} (hK : ∀ (i : ι) (j : κ), 0 < K i j) {a : ι → ℝ} {b : κ → ℝ}
  (ha : ∀ (i : ι), 0 < a i) (hb : ∀ (j : κ), 0 < b j) (hmass : ∑ i, a i = ∑ j, b j) :
  ∃ u v,
    (∀ (i : ι), 0 < u i) ∧
      (∀ (j : κ), 0 < v j) ∧
        (∀ (i : ι), ∑ j, u i * K i j * v j = a i) ∧ ∀ (j : κ), ∑ i, u i * K i j * v j = b j
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.exists_sinkhorn_scaling`](https://taucetiproject.org/docs/TauCeti/Data/Matrix/Scaling/Basic.html#Matrix.exists_sinkhorn_scaling).

## Sources

- [Tau Ceti documentation: `Matrix.exists_sinkhorn_scaling`](https://taucetiproject.org/docs/TauCeti/Data/Matrix/Scaling/Basic.html#Matrix.exists_sinkhorn_scaling)
- [Source of `Matrix.exists_sinkhorn_scaling` in TauCeti/Data/Matrix/Scaling/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Data/Matrix/Scaling/Basic.lean#L888)
