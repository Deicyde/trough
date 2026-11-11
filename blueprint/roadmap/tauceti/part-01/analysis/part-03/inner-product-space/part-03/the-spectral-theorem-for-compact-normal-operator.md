---
declaration: theorem
origin: cited
lean: IsStarNormal.orthogonalComplement_iSup_eigenspaces_eq_bot
statement: formalized
proof: formalized
---

# The spectral theorem for compact normal operators

the eigenspaces of a compact normal
operator on a complex Hilbert space have trivial mutual orthogonal complement.

```lean
IsStarNormal.orthogonalComplement_iSup_eigenspaces_eq_bot.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℂ E] [CompleteSpace E] {T : E →L[ℂ] E}
  (hT : IsStarNormal T) (hc : IsCompactOperator ⇑T) : (⨆ μ, Module.End.eigenspace (↑T) μ)ᗮ = ⊥
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsStarNormal.orthogonalComplement_iSup_eigenspaces_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Spectral/CompactNormal.html#IsStarNormal.orthogonalComplement_iSup_eigenspaces_eq_bot).

## Sources

- [Tau Ceti documentation: `IsStarNormal.orthogonalComplement_iSup_eigenspaces_eq_bot`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Spectral/CompactNormal.html#IsStarNormal.orthogonalComplement_iSup_eigenspaces_eq_bot)
- [Source of `IsStarNormal.orthogonalComplement_iSup_eigenspaces_eq_bot` in TauCeti/Analysis/InnerProductSpace/Spectral/CompactNormal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/Spectral/CompactNormal.lean#L87)
