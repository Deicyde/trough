---
declaration: theorem
origin: cited
lean: AlgHom.exists_eq_smul_of_apply_eq_apply
statement: formalized
proof: formalized
---

# Schur's lemma for a full endomorphism representation

If `ρ` maps `B` onto the
endomorphism algebra of `M` and `T : M ≃ N` intertwines `ρ` with a representation `σ`, then every
linear map `U : M → N` intertwining `ρ` with `σ` is a scalar multiple of `T`.

```lean
AlgHom.exists_eq_smul_of_apply_eq_apply.{u_1, u_2, u_3, u_4} {K : Type u_1} {B : Type u_2}
  {M : Type u_3} {N : Type u_4} [Field K] [Ring B] [Algebra K B] [AddCommGroup M]
  [_root_.Module K M] [AddCommGroup N] [_root_.Module K N] {ρ : B →ₐ[K] Module.End K M}
  (hρ : Function.Surjective ⇑ρ) (σ : B →ₐ[K] Module.End K N) {T : M ≃ₗ[K] N}
  (hT : ∀ (b : B) (x : M), T ((ρ b) x) = (σ b) (T x)) {U : M →ₗ[K] N}
  (hU : ∀ (b : B) (x : M), U ((ρ b) x) = (σ b) (U x)) : ∃ c, U = c • ↑T
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AlgHom.exists_eq_smul_of_apply_eq_apply`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/End/Intertwiner.html#AlgHom.exists_eq_smul_of_apply_eq_apply).

## Sources

- [Tau Ceti documentation: `AlgHom.exists_eq_smul_of_apply_eq_apply`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/End/Intertwiner.html#AlgHom.exists_eq_smul_of_apply_eq_apply)
- [Source of `AlgHom.exists_eq_smul_of_apply_eq_apply` in TauCeti/LinearAlgebra/End/Intertwiner.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/End/Intertwiner.lean#L86)
