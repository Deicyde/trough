---
declaration: theorem
origin: cited
lean: IsCoercive.orthogonalComplement_iSup_eigenspaces_formSolutionOperator_eq_bot
statement: formalized
proof: formalized
---

# The spectral theorem for the solution operator

its eigenspaces have trivial orthogonal
complement in `H`, even when `H` is incomplete.

```lean
IsCoercive.orthogonalComplement_iSup_eigenspaces_formSolutionOperator_eq_bot.{u_9, u_10}
  {V : Type u_9} {H : Type u_10} [NormedAddCommGroup V] [InnerProductSpace ℝ V] [CompleteSpace V]
  [NormedAddCommGroup H] [InnerProductSpace ℝ H] {B : V →L[ℝ] V →L[ℝ] ℝ} (hB : IsCoercive B)
  {J : V →L[ℝ] H} (hJ : IsCompactOperator ⇑J) (hsymm : ∀ (u v : V), (B u) v = (B v) u) :
  (⨆ mu, Module.End.eigenspace (↑(hB.formSolutionOperator J)) mu)ᗮ = ⊥
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsCoercive.orthogonalComplement_iSup_eigenspaces_formSolutionOperator_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Variational/Spectrum.html#IsCoercive.orthogonalComplement_iSup_eigenspaces_formSolutionOperator_eq_bot).

## Sources

- [Tau Ceti documentation: `IsCoercive.orthogonalComplement_iSup_eigenspaces_formSolutionOperator_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Variational/Spectrum.html#IsCoercive.orthogonalComplement_iSup_eigenspaces_formSolutionOperator_eq_bot)
- [Source of `IsCoercive.orthogonalComplement_iSup_eigenspaces_formSolutionOperator_eq_bot` in TauCeti/Analysis/InnerProductSpace/Variational/Spectrum.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/Variational/Spectrum.lean#L486)
