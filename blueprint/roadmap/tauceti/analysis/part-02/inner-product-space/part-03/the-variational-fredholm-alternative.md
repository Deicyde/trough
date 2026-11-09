---
declaration: theorem
origin: cited
lean: IsCoercive.fredholmAlternative_formPerturbation
statement: formalized
proof: formalized
---

# The variational Fredholm alternative

For a compact continuous linear map `J`, either the
homogeneous perturbation of `B` by `κ ⟪J ·, J ·⟫` has a nonzero solution, or every represented
forcing has a unique solution.

```lean
IsCoercive.fredholmAlternative_formPerturbation.{u_1, u_2} {V : Type u_1} {H : Type u_2}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [CompleteSpace V] [SeminormedAddCommGroup H]
  [InnerProductSpace ℝ H] {B : V →L[ℝ] V →L[ℝ] ℝ} (hB : IsCoercive B) {J : V →L[ℝ] H}
  (hJ : IsCompactOperator ⇑J) (kappa : ℝ) :
  (∃ u, u ≠ 0 ∧ ∀ (v : V), (B u) v - kappa * inner ℝ (J u) (J v) = 0) ∨
    ∀ (ell : StrongDual ℝ V), ∃! u, ∀ (v : V), (B u) v - kappa * inner ℝ (J u) (J v) = ell v
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsCoercive.fredholmAlternative_formPerturbation`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Variational/Fredholm.html#IsCoercive.fredholmAlternative_formPerturbation).

## Sources

- [Tau Ceti documentation: `IsCoercive.fredholmAlternative_formPerturbation`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Variational/Fredholm.html#IsCoercive.fredholmAlternative_formPerturbation)
- [Source of `IsCoercive.fredholmAlternative_formPerturbation` in TauCeti/Analysis/InnerProductSpace/Variational/Fredholm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/Variational/Fredholm.lean#L132)
