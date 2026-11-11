---
declaration: theorem
origin: cited
lean: Submodule.exists_projection_norm_le_sqrt_finrank
statement: formalized
proof: formalized
---

# The Kadec–Snobar theorem

Over `ℝ` or `ℂ`, every finite-dimensional subspace `M` of a
normed space is the range of a projection of norm at most `√(dim M)`: there is a continuous linear
map `P : X → M` restricting to the identity of `M` with `‖P‖ ≤ √(dim M)`, so that
`M.subtypeL ∘L P` is a projection of `X` onto `M` of the same norm.

```lean
Submodule.exists_projection_norm_le_sqrt_finrank.{u_1, u_2} {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup X] [NormedSpace 𝕜 X] (M : Submodule 𝕜 X) [FiniteDimensional 𝕜 ↥M] :
  ∃ P, (∀ (x : ↥M), P ↑x = x) ∧ ‖P‖ ≤ √↑(Module.finrank 𝕜 ↥M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [John's theorem](../../inner-product-space/part-02/johns-theorem.md)

## Lean

Formalized in Tau Ceti as [`Submodule.exists_projection_norm_le_sqrt_finrank`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/KadecSnobar.html#Submodule.exists_projection_norm_le_sqrt_finrank).

## Sources

- [Tau Ceti documentation: `Submodule.exists_projection_norm_le_sqrt_finrank`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/KadecSnobar.html#Submodule.exists_projection_norm_le_sqrt_finrank)
- [Source of `Submodule.exists_projection_norm_le_sqrt_finrank` in TauCeti/Analysis/Normed/Module/KadecSnobar.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Module/KadecSnobar.lean#L72)
