---
declaration: theorem
origin: cited
lean: LinearPMap.dense_adjoint_domain
statement: formalized
proof: formalized
---

# von Neumann's theorem

The adjoint of a closed densely defined partial
linear map between complete inner product spaces has dense domain.

```lean
LinearPMap.dense_adjoint_domain.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [CompleteSpace E] [NormedAddCommGroup F]
  [InnerProductSpace 𝕜 F] [CompleteSpace F] {T : E →ₗ.[𝕜] F} (hT : Dense ↑T.domain)
  (hTc : T.IsClosed) : Dense ↑T.adjoint.domain
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearPMap.dense_adjoint_domain`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LinearPMap/SubmoduleAdjoint.html#LinearPMap.dense_adjoint_domain).

## Sources

- [Tau Ceti documentation: `LinearPMap.dense_adjoint_domain`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LinearPMap/SubmoduleAdjoint.html#LinearPMap.dense_adjoint_domain)
- [Source of `LinearPMap.dense_adjoint_domain` in TauCeti/Analysis/InnerProductSpace/LinearPMap/SubmoduleAdjoint.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/LinearPMap/SubmoduleAdjoint.lean#L104)
