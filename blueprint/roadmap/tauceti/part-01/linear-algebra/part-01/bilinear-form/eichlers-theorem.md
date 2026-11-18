---
declaration: theorem
origin: cited
lean: LinearMap.BilinForm.eq_orthComponents_iff
statement: formalized
proof: formalized
---

# Eichler's theorem

For a reflexive positive definite integral form, a set of submodules
consists of pairwise orthogonal orthogonally indecomposable submodules spanning `M` exactly when
it is the set of orthogonal components. In particular such a decomposition exists and is unique.

```lean
LinearMap.BilinForm.eq_orthComponents_iff.{u_3} {M : Type u_3} [AddCommGroup M]
  {B : LinearMap.BilinForm ℤ M} (hB : B.IsRefl)
  (hpos : (LinearMap.BilinMap.toQuadraticMap B).PosDef) {S : Set (Submodule ℤ M)} :
  S = B.orthComponents ↔
    (∀ N ∈ S, B.IsOrthIndecomposable N) ∧ (S.Pairwise fun N N' => N ≤ B.orthogonal N') ∧ sSup S = ⊤
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.BilinForm.eq_orthComponents_iff`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/BilinearForm/Indecomposable.html#LinearMap.BilinForm.eq_orthComponents_iff).

## Sources

- [Tau Ceti documentation: `LinearMap.BilinForm.eq_orthComponents_iff`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/BilinearForm/Indecomposable.html#LinearMap.BilinForm.eq_orthComponents_iff)
- [Source of `LinearMap.BilinForm.eq_orthComponents_iff` in TauCeti/LinearAlgebra/BilinearForm/Indecomposable.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/BilinearForm/Indecomposable.lean#L318)
