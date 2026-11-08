---
declaration: theorem
origin: cited
lean: LinearMap.abs_singularValues_sub_singularValues_le
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

- [ContinuousLinearMap.singularValue](../../part-01/operator-theory/continuouslinearmap-singularvalue.md)
- [Eckart–Young](eckart-young.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.abs_singularValues_sub_singularValues_le`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/EckartYoung.html#LinearMap.abs_singularValues_sub_singularValues_le).

## Sources

- [Tau Ceti documentation: `LinearMap.abs_singularValues_sub_singularValues_le`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/EckartYoung.html#LinearMap.abs_singularValues_sub_singularValues_le)
- [Source of `LinearMap.abs_singularValues_sub_singularValues_le` in TauCeti/Analysis/OperatorIdeal/ApproximationNumber/EckartYoung.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/EckartYoung.lean#L103)
