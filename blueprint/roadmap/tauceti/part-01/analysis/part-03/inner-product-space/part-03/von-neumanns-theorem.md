---
declaration: theorem
origin: cited
lean: LinearPMap.dense_adjoint_domain, LinearPMap.isSelfAdjoint_adjointComp
statement: formalized
proof: formalized
---

# von Neumann's theorem

The adjoint of a closable partial linear map between
complete inner product spaces has dense domain.

No density of `T.domain` is needed: the domain of `T.adjoint` is
`{y | Continuous ((innerₛₗ 𝕜 y).comp T.toFun)}` whether or not `T` is densely defined
(only the values of `T.adjoint` are junk off the densely defined case).

```lean
LinearPMap.dense_adjoint_domain.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [CompleteSpace E] [NormedAddCommGroup F]
  [InnerProductSpace 𝕜 F] [CompleteSpace F] {T : E →ₗ.[𝕜] F} (hTc : T.IsClosable) :
  Dense ↑T.adjoint.domain
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearPMap.dense_adjoint_domain`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LinearPMap/SubmoduleAdjoint.html#LinearPMap.dense_adjoint_domain).

## Other forms

**Von Neumann's theorem.** Formalized in Tau Ceti as [`LinearPMap.isSelfAdjoint_adjointComp`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LinearPMap/AdjointComp.html#LinearPMap.isSelfAdjoint_adjointComp).

```lean
LinearPMap.isSelfAdjoint_adjointComp.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [CompleteSpace E] [NormedAddCommGroup F]
  [InnerProductSpace 𝕜 F] [CompleteSpace F] (T : E →ₗ.[𝕜] F) (hT : T.IsClosed)
  (hd : Dense ↑T.domain) : IsSelfAdjoint T.adjointComp
```

## Sources

- [Tau Ceti documentation: `LinearPMap.dense_adjoint_domain`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LinearPMap/SubmoduleAdjoint.html#LinearPMap.dense_adjoint_domain)
- [Source of `LinearPMap.dense_adjoint_domain` in TauCeti/Analysis/InnerProductSpace/LinearPMap/SubmoduleAdjoint.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/InnerProductSpace/LinearPMap/SubmoduleAdjoint.lean#L106)
