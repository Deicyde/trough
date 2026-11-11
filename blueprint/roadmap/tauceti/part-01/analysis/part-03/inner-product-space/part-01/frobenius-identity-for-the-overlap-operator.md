---
declaration: theorem
origin: cited
lean: TauCeti.sum_sq_singularValues_overlapOperator
statement: formalized
proof: formalized
---

# Frobenius identity for the overlap operator

the squared singular values of the overlap
operator sum to the squared Frobenius norm `∑ⱼ ∑ᵢ ‖⟪uᵢ, vⱼ⟫‖²` of its matrix.

```lean
TauCeti.sum_sq_singularValues_overlapOperator.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} {E : Type u_2}
  {ι : Type u_3} {κ : Type u_4} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [Fintype ι] [Fintype κ] (u : ι → E) (v : κ → E) :
  ((TauCeti.overlapOperator 𝕜 u v).singularValues.sum fun x s => s ^ 2) =
    ∑ j, ∑ i, ‖inner 𝕜 (u i) (v j)‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_sq_singularValues_overlapOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Orthonormal/Overlap.html#TauCeti.sum_sq_singularValues_overlapOperator).

## Sources

- [Tau Ceti documentation: `TauCeti.sum_sq_singularValues_overlapOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Orthonormal/Overlap.html#TauCeti.sum_sq_singularValues_overlapOperator)
- [Source of `TauCeti.sum_sq_singularValues_overlapOperator` in TauCeti/Analysis/InnerProductSpace/Orthonormal/Overlap.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/Orthonormal/Overlap.lean#L106)
