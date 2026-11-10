---
declaration: theorem
origin: cited
lean: TauCeti.exists_jointImplicitFunction_of_eventually_differentiableAt
statement: formalized
proof: formalized
---

# The joint holomorphic implicit function theorem

Let `G : E₁ × E₂ → F` be complex
differentiable near `u`, with invertible partial derivative `∂₂G(u) : E₂ →L[ℂ] F`. Then there is a
map `ψ : E₁ × F → E₂`, holomorphic (indeed analytic) near `(u.1, G u)`, with `ψ (u.1, G u) = u.2`
and `G (z, ψ (z, w)) = w` near `(u.1, G u)`; moreover, for `(z, v)` near `u` and `w` near `G u`,
`G (z, v) = w` holds exactly when `ψ (z, w) = v`. One choice of `ψ` is
`HasStrictFDerivAt.jointImplicitFunctionOfProdDomain`, and any two maps with these properties
agree near `(u.1, G u)`
(`HasStrictFDerivAt.eventuallyEq_jointImplicitFunctionOfProdDomain_of_continuousAt`).

```lean
TauCeti.exists_jointImplicitFunction_of_eventually_differentiableAt.{u_1, u_2, u_3} {E₁ : Type u_1}
  [NormedAddCommGroup E₁] [NormedSpace ℂ E₁] [FiniteDimensional ℂ E₁] {E₂ : Type u_2}
  [NormedAddCommGroup E₂] [NormedSpace ℂ E₂] [FiniteDimensional ℂ E₂] {F : Type u_3}
  [NormedAddCommGroup F] [NormedSpace ℂ F] {G : E₁ × E₂ → F} {u : E₁ × E₂}
  (hG : ∀ᶠ (x : E₁ × E₂) in nhds u, DifferentiableAt ℂ G x)
  (hinv : (fderiv ℂ G u ∘SL ContinuousLinearMap.inr ℂ E₁ E₂).IsInvertible) :
  ∃ ψ,
    (∀ᶠ (p : E₁ × F) in nhds (u.1, G u), AnalyticAt ℂ ψ p) ∧
      ψ (u.1, G u) = u.2 ∧
        (∀ᶠ (p : E₁ × F) in nhds (u.1, G u), G (p.1, ψ p) = p.2) ∧
          ∀ᶠ (q : (E₁ × E₂) × F) in nhds (u, G u), G q.1 = q.2 ↔ ψ (q.1.1, q.2) = q.1.2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The analytic implicit function theorem](../../../part-01/analytic/the-analytic-implicit-function-theorem.md)
- [Osgood's lemma](../../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_jointImplicitFunction_of_eventually_differentiableAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/ImplicitFunction.html#TauCeti.exists_jointImplicitFunction_of_eventually_differentiableAt).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_jointImplicitFunction_of_eventually_differentiableAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/ImplicitFunction.html#TauCeti.exists_jointImplicitFunction_of_eventually_differentiableAt)
- [Source of `TauCeti.exists_jointImplicitFunction_of_eventually_differentiableAt` in TauCeti/Analysis/Complex/ImplicitFunction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/ImplicitFunction.lean#L49)
