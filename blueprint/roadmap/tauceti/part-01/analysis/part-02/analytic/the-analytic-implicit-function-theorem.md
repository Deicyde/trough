---
declaration: theorem
origin: cited
lean: HasStrictFDerivAt.analyticAt_implicitFunctionOfProdDomain, ImplicitFunctionData.analyticAt_implicitFunction
statement: formalized
proof: formalized
---

# The analytic implicit function theorem

If `f : E₁ × E → F` is analytic at `u` and its
partial derivative in the second variable is invertible there, the implicit function `ψ` with
`f (x, ψ x) = f u` near `u.1` is analytic at `u.1`.

```lean
HasStrictFDerivAt.analyticAt_implicitFunctionOfProdDomain.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [CompleteSpace E] {F : Type u_3} [NormedAddCommGroup F] [NormedSpace 𝕜 F] [CompleteSpace F]
  {E₁ : Type u_4} [NormedAddCommGroup E₁] [NormedSpace 𝕜 E₁] [CompleteSpace E₁] {f : E₁ × E → F}
  {f'u : E₁ × E →L[𝕜] F} {u : E₁ × E} (dfu : HasStrictFDerivAt f f'u u)
  (if₂u : (f'u ∘SL ContinuousLinearMap.inr 𝕜 E₁ E).IsInvertible) (hf : AnalyticAt 𝕜 f u) :
  AnalyticAt 𝕜 (dfu.implicitFunctionOfProdDomain if₂u) u.1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HasStrictFDerivAt.analyticAt_implicitFunctionOfProdDomain`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/Inverse.html#HasStrictFDerivAt.analyticAt_implicitFunctionOfProdDomain).

## Other forms

**The analytic implicit function theorem, general form.** Formalized in Tau Ceti as [`ImplicitFunctionData.analyticAt_implicitFunction`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/Inverse.html#ImplicitFunctionData.analyticAt_implicitFunction).

```lean
ImplicitFunctionData.analyticAt_implicitFunction.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [CompleteSpace E] {F : Type u_3} [NormedAddCommGroup F] [NormedSpace 𝕜 F] [CompleteSpace F]
  {G : Type u_4} [NormedAddCommGroup G] [NormedSpace 𝕜 G] [CompleteSpace G]
  {φ : ImplicitFunctionData 𝕜 E F G} (hl : AnalyticAt 𝕜 φ.leftFun φ.pt)
  (hr : AnalyticAt 𝕜 φ.rightFun φ.pt) :
  AnalyticAt 𝕜 (Function.uncurry φ.implicitFunction) (φ.prodFun φ.pt)
```

## Sources

- [Tau Ceti documentation: `HasStrictFDerivAt.analyticAt_implicitFunctionOfProdDomain`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/Inverse.html#HasStrictFDerivAt.analyticAt_implicitFunctionOfProdDomain)
- [Source of `HasStrictFDerivAt.analyticAt_implicitFunctionOfProdDomain` in TauCeti/Analysis/Analytic/Inverse.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Analytic/Inverse.lean#L145)
