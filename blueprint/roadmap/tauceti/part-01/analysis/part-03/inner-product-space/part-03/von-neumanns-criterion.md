---
declaration: theorem
origin: cited
lean: LinearPMap.isSelfAdjoint_of_surjective_addSub
statement: formalized
proof: formalized
---

# Von Neumann's criterion

A symmetric partial linear map is self-adjoint if its
shifts by `+i` and `-i` are surjective. Density follows from the first shift, so no
independent density hypothesis is needed.

```lean
LinearPMap.isSelfAdjoint_of_surjective_addSub.{u_3} {H : Type u_3} [NormedAddCommGroup H]
  [InnerProductSpace ℂ H] [CompleteSpace H] (A : H →ₗ.[ℂ] H) (hsym : A.IsFormalAdjoint A)
  (hplus : ∀ (φ : H), ∃ ψ, ↑A ψ + Complex.I • ↑ψ = φ)
  (hminus : ∀ (φ : H), ∃ ψ, ↑A ψ - Complex.I • ↑ψ = φ) : IsSelfAdjoint A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearPMap.isSelfAdjoint_of_surjective_addSub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LinearPMap/SelfAdjoint.html#LinearPMap.isSelfAdjoint_of_surjective_addSub).

## Sources

- [Tau Ceti documentation: `LinearPMap.isSelfAdjoint_of_surjective_addSub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LinearPMap/SelfAdjoint.html#LinearPMap.isSelfAdjoint_of_surjective_addSub)
- [Source of `LinearPMap.isSelfAdjoint_of_surjective_addSub` in TauCeti/Analysis/InnerProductSpace/LinearPMap/SelfAdjoint.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/LinearPMap/SelfAdjoint.lean#L395)
