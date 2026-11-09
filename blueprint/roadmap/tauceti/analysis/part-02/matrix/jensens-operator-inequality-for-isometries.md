---
declaration: theorem
origin: cited
lean: Matrix.conjTranspose_mul_cfc_mul_le_cfc_conjTranspose_mul_mul
statement: formalized
proof: formalized
---

# Jensen's operator inequality for isometries

Let `f` be operator concave on a set `S` of
matrices closed under unitary conjugation, in the sense that `A ↦ cfc f A` is concave on `S`. For
a Hermitian `A ∈ S` and an isometry `V`, that is `Vᴴ * V = 1`, compressing by `V` lowers the
functional calculus: `Vᴴ * cfc f A * V ≤ cfc f (Vᴴ * A * V)`.

```lean
Matrix.conjTranspose_mul_cfc_mul_le_cfc_conjTranspose_mul_mul.{u_1, u_2, u_3} {m : Type u_1}
  {n : Type u_2} {𝕜 : Type u_3} [RCLike 𝕜] [Fintype m] [DecidableEq m] [Fintype n] [DecidableEq n]
  {f : ℝ → ℝ} {S : Set (Matrix m m 𝕜)} (hf : ConcaveOn ℝ S (cfc f))
  (hS : ∀ a ∈ S, ∀ u ∈ unitary (Matrix m m 𝕜), u * a * star u ∈ S) {A : Matrix m m 𝕜} (hAS : A ∈ S)
  (hA : A.IsHermitian) {V : Matrix m n 𝕜} (hV : V.conjTranspose * V = 1) :
  V.conjTranspose * cfc f A * V ≤ cfc f (V.conjTranspose * A * V)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.conjTranspose_mul_cfc_mul_le_cfc_conjTranspose_mul_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/OperatorJensen.html#Matrix.conjTranspose_mul_cfc_mul_le_cfc_conjTranspose_mul_mul).

## Sources

- [Tau Ceti documentation: `Matrix.conjTranspose_mul_cfc_mul_le_cfc_conjTranspose_mul_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/OperatorJensen.html#Matrix.conjTranspose_mul_cfc_mul_le_cfc_conjTranspose_mul_mul)
- [Source of `Matrix.conjTranspose_mul_cfc_mul_le_cfc_conjTranspose_mul_mul` in TauCeti/Analysis/Matrix/OperatorJensen.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Matrix/OperatorJensen.lean#L60)
