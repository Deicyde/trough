---
declaration: theorem
origin: cited
lean: IsSelfAdjoint.add_of_isRelativelyBounded
statement: formalized
proof: formalized
---

# The Kato–Rellich theorem

Let `A` be a self-adjoint partial linear map on a Hilbert space
and `V` a symmetric partial linear map that is relatively bounded with respect to `A` with
constants `a` and `b < 1`, that is `dom A ⊆ dom V` and `‖V x‖ ≤ a * ‖x‖ + b * ‖A x‖` on `dom A`.
Then `A + V`, whose domain is `dom A`, is self-adjoint.

```lean
IsSelfAdjoint.add_of_isRelativelyBounded.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [CompleteSpace E] {A V : E →ₗ.[𝕜] E}
  (hA : IsSelfAdjoint A) (hV : V.IsFormalAdjoint V) {a b : ℝ} (hAV : V.IsRelativelyBounded A a b)
  (hb : b < 1) : IsSelfAdjoint (A + V)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsSelfAdjoint.add_of_isRelativelyBounded`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LinearPMap/KatoRellich.html#IsSelfAdjoint.add_of_isRelativelyBounded).

## Sources

- [Tau Ceti documentation: `IsSelfAdjoint.add_of_isRelativelyBounded`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LinearPMap/KatoRellich.html#IsSelfAdjoint.add_of_isRelativelyBounded)
- [Source of `IsSelfAdjoint.add_of_isRelativelyBounded` in TauCeti/Analysis/InnerProductSpace/LinearPMap/KatoRellich.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/LinearPMap/KatoRellich.lean#L114)
- [Tau Ceti roadmap status: Operator theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OperatorTheory/STATUS.md)
