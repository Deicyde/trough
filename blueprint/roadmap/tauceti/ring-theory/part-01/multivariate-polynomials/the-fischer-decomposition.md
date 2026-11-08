---
declaration: theorem
origin: cited
lean: MvPolynomial.harmonicSubmodule_sup_map_mulLeft_normSq, MvPolynomial.disjoint_ker_laplacian_map_mulLeft_normSq
statement: formalized
proof: formalized
---

# The Fischer decomposition

every homogeneous polynomial of degree `e + 2` is the sum of a
harmonic one and `r²` times a homogeneous polynomial of degree `e`. The sum is direct by
`MvPolynomial.disjoint_ker_laplacian_map_mulLeft_normSq`.

```lean
MvPolynomial.harmonicSubmodule_sup_map_mulLeft_normSq.{u_1, u_3} {σ : Type u_1} {K : Type u_3}
  [Field K] [Fintype σ] [CharZero K] [Nonempty σ] (e : ℕ) :
  MvPolynomial.harmonicSubmodule σ K (e + 2) ⊔
      Submodule.map (LinearMap.mulLeft K (MvPolynomial.normSq σ K))
        (MvPolynomial.homogeneousSubmodule σ K e) =
    MvPolynomial.homogeneousSubmodule σ K (e + 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MvPolynomial.harmonicSubmodule_sup_map_mulLeft_normSq`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Harmonic.html#MvPolynomial.harmonicSubmodule_sup_map_mulLeft_normSq).

## Other forms

**The Fischer decomposition, disjointness.** Formalized in Tau Ceti as [`MvPolynomial.disjoint_ker_laplacian_map_mulLeft_normSq`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Harmonic.html#MvPolynomial.disjoint_ker_laplacian_map_mulLeft_normSq).

```lean
MvPolynomial.disjoint_ker_laplacian_map_mulLeft_normSq.{u_1, u_3} {σ : Type u_1} {K : Type u_3}
  [Field K] [Fintype σ] [CharZero K] [Nonempty σ] (e : ℕ) :
  Disjoint MvPolynomial.laplacian.ker
    (Submodule.map (LinearMap.mulLeft K (MvPolynomial.normSq σ K))
      (MvPolynomial.homogeneousSubmodule σ K e))
```

## Sources

- [Tau Ceti documentation: `MvPolynomial.harmonicSubmodule_sup_map_mulLeft_normSq`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Harmonic.html#MvPolynomial.harmonicSubmodule_sup_map_mulLeft_normSq)
- [Source of `MvPolynomial.harmonicSubmodule_sup_map_mulLeft_normSq` in TauCeti/RingTheory/MvPolynomial/Harmonic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/MvPolynomial/Harmonic.lean#L307)
