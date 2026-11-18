---
declaration: theorem
origin: cited
lean: MvPolynomial.norm_eval_hasseDeriv_le
statement: formalized
proof: formalized
---

# The multivariate evaluated Hasse derivative bound

for `F` supported on a finite set `T`
of exponents, with coefficients of norm at most `H` on `T`, and a point with `‖a s‖ ≤ A s`,
`‖∂^d F (a)‖ ≤ H ∑_{μ ∈ T} ∏ₛ choose (μ s) (d s) · A s ^ (μ s - d s)`.

```lean
MvPolynomial.norm_eval_hasseDeriv_le.{u_1, u_2} {R : Type u_1} {σ : Type u_2} [SeminormedCommRing R]
  [Fintype σ] {T : Finset (σ →₀ ℕ)} {F : MvPolynomial σ R}
  (hF : F ∈ MvPolynomial.restrictSupport R ↑T) {H : ℝ} (hcoeff : ∀ μ ∈ T, ‖F.coeff μ‖ ≤ H)
  {a : σ → R} {A : σ → ℝ} (ha : ∀ (s : σ), ‖a s‖ ≤ A s) (d : σ →₀ ℕ) :
  ‖(MvPolynomial.eval a) ((MvPolynomial.hasseDeriv d) F)‖ ≤
    H * ∑ μ ∈ T, ∏ s, ↑((μ s).choose (d s)) * A s ^ (μ s - d s)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MvPolynomial.norm_eval_hasseDeriv_le`](https://taucetiproject.org/docs/TauCeti/Analysis/MvPolynomial/HasseDerivBound.html#MvPolynomial.norm_eval_hasseDeriv_le).

## Sources

- [Tau Ceti documentation: `MvPolynomial.norm_eval_hasseDeriv_le`](https://taucetiproject.org/docs/TauCeti/Analysis/MvPolynomial/HasseDerivBound.html#MvPolynomial.norm_eval_hasseDeriv_le)
- [Source of `MvPolynomial.norm_eval_hasseDeriv_le` in TauCeti/Analysis/MvPolynomial/HasseDerivBound.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/MvPolynomial/HasseDerivBound.lean#L84)
