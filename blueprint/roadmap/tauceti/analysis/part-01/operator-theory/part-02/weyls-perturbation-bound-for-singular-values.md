---
declaration: theorem
origin: cited
lean: LinearMap.abs_singularValues_sub_singularValues_le, Matrix.IsHermitian.abs_eigenvalues₀_sub_le_norm
statement: formalized
proof: formalized
---

# Weyl's perturbation bound for singular values

Each singular value of a linear map between
finite-dimensional inner product spaces is `1`-Lipschitz in the operator norm:
`|σₙ(A) - σₙ(B)| ≤ ‖A - B‖`.

```lean
LinearMap.abs_singularValues_sub_singularValues_le.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E]
  [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [FiniteDimensional 𝕜 F] (A B : E →ₗ[𝕜] F) (n : ℕ) :
  |A.singularValues n - B.singularValues n| ≤ ‖LinearMap.toContinuousLinearMap (A - B)‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [ContinuousLinearMap.singularValue](../part-01/continuouslinearmap-singularvalue.md)
- [Weyl's inequality for symmetric operators on a finite-dimensional inner product space over `𝕜 = ℝ, ℂ`](../../../part-02/inner-product-space/part-02/weyls-inequality-for-symmetric-operators-on-a-fi.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.abs_singularValues_sub_singularValues_le`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/EckartYoung.html#LinearMap.abs_singularValues_sub_singularValues_le).

## Other forms

**Weyl's perturbation bound for ordered eigenvalues of Hermitian matrices.** Formalized in Tau Ceti as [`Matrix.IsHermitian.abs_eigenvalues₀_sub_le_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/Eigenvalues/Basic.html#Matrix.IsHermitian.abs_eigenvalues%E2%82%80_sub_le_norm).

```lean
Matrix.IsHermitian.abs_eigenvalues₀_sub_le_norm.{u_1, u_2} {𝕜 : Type u_1} {ι : Type u_2} [RCLike 𝕜]
  [Fintype ι] [DecidableEq ι] {A B : Matrix ι ι 𝕜} (hA : A.IsHermitian) (hB : B.IsHermitian)
  (i : Fin (Fintype.card ι)) : |hA.eigenvalues₀ i - hB.eigenvalues₀ i| ≤ ‖A - B‖
```

## Sources

- [Tau Ceti documentation: `LinearMap.abs_singularValues_sub_singularValues_le`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/EckartYoung.html#LinearMap.abs_singularValues_sub_singularValues_le)
- [Source of `LinearMap.abs_singularValues_sub_singularValues_le` in TauCeti/Analysis/OperatorIdeal/ApproximationNumber/EckartYoung.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/EckartYoung.lean#L103)
