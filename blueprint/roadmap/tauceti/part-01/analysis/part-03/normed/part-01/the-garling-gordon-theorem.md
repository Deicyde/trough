---
declaration: theorem
origin: cited
lean: Submodule.exists_isIdempotentElem_ker_eq_norm_le_sqrt_finrank_add
statement: formalized
proof: formalized
---

# The Garling–Gordon theorem

Over `ℝ` or `ℂ`, every closed subspace `M` of finite
codimension in a normed space `X` is, for every `ε > 0`, the kernel of a projection of norm at
most `√(dim (X ⧸ M)) + ε`.

```lean
Submodule.exists_isIdempotentElem_ker_eq_norm_le_sqrt_finrank_add.{u_1, u_2} {𝕜 : Type u_1}
  {X : Type u_2} [RCLike 𝕜] [NormedAddCommGroup X] [NormedSpace 𝕜 X] (M : Submodule 𝕜 X)
  (hM : IsClosed ↑M) [FiniteDimensional 𝕜 (X ⧸ M)] {ε : ℝ} (hε : 0 < ε) :
  ∃ P, IsIdempotentElem P ∧ (↑P).ker = M ∧ ‖P‖ ≤ √↑(Module.finrank 𝕜 (X ⧸ M)) + ε
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [John's theorem](../../inner-product-space/part-02/johns-theorem.md)

## Lean

Formalized in Tau Ceti as [`Submodule.exists_isIdempotentElem_ker_eq_norm_le_sqrt_finrank_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/KadecSnobar.html#Submodule.exists_isIdempotentElem_ker_eq_norm_le_sqrt_finrank_add).

## Sources

- [Tau Ceti documentation: `Submodule.exists_isIdempotentElem_ker_eq_norm_le_sqrt_finrank_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/KadecSnobar.html#Submodule.exists_isIdempotentElem_ker_eq_norm_le_sqrt_finrank_add)
- [Source of `Submodule.exists_isIdempotentElem_ker_eq_norm_le_sqrt_finrank_add` in TauCeti/Analysis/Normed/Module/KadecSnobar.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Module/KadecSnobar.lean#L105)
