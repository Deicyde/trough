---
declaration: theorem
origin: cited
lean: TauCeti.rank_jacobiMatrixAt_dehomogenize_div, TauCeti.mulVec_surjective_jacobiMatrixAt_iff_exists_eval_pderiv_ne_zero
statement: formalized
proof: formalized
---

# The Jacobian criterion in a ratio chart

at a common zero `b` of a family of homogeneous
equations with `b i ≠ 0`, the Jacobian matrix of the dehomogenized equations at the coordinate
ratios `b (i.succAbove j) / b i` has the same rank as the Jacobian matrix of the homogeneous
equations at `b`.

```lean
TauCeti.rank_jacobiMatrixAt_dehomogenize_div.{u_3, u_4} {ι : Type u_3} {K : Type u_4} [Field K]
  [Finite ι] {n : ℕ} (i : Fin (n + 1)) {p : ι → MvPolynomial (Fin (n + 1)) K} {d : ι → ℕ}
  (hp : ∀ (k : ι), (p k).IsHomogeneous (d k)) {b : Fin (n + 1) → K} (hi : b i ≠ 0)
  (hb : ∀ (k : ι), (MvPolynomial.eval b) (p k) = 0) :
  (TauCeti.jacobiMatrixAt (fun k => (TauCeti.dehomogenize i) (p k)) fun j =>
        b (i.succAbove j) / b i).rank =
    (TauCeti.jacobiMatrixAt p b).rank
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.rank_jacobiMatrixAt_dehomogenize_div`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Jacobian/Basic.html#TauCeti.rank_jacobiMatrixAt_dehomogenize_div).

## Other forms

**The Jacobian criterion for a single equation.** Formalized in Tau Ceti as [`TauCeti.mulVec_surjective_jacobiMatrixAt_iff_exists_eval_pderiv_ne_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Jacobian/Basic.html#TauCeti.mulVec_surjective_jacobiMatrixAt_iff_exists_eval_pderiv_ne_zero).

```lean
TauCeti.mulVec_surjective_jacobiMatrixAt_iff_exists_eval_pderiv_ne_zero.{u_2, u_3, u_4}
  {σ : Type u_2} {ι : Type u_3} {K : Type u_4} [Field K] [Unique ι] [Fintype σ]
  {p : ι → MvPolynomial σ K} {v : σ → K} :
  Function.Surjective (TauCeti.jacobiMatrixAt p v).mulVec ↔
    ∃ j, (MvPolynomial.eval v) ((MvPolynomial.pderiv j) (p default)) ≠ 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.rank_jacobiMatrixAt_dehomogenize_div`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Jacobian/Basic.html#TauCeti.rank_jacobiMatrixAt_dehomogenize_div)
- [Source of `TauCeti.rank_jacobiMatrixAt_dehomogenize_div` in TauCeti/RingTheory/MvPolynomial/Jacobian/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/MvPolynomial/Jacobian/Basic.lean#L228)
