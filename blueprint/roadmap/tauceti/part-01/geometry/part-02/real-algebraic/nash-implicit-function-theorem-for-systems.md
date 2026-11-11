---
declaration: theorem
origin: cited
lean: HasStrictFDerivAt.isNashAt_implicitFunctionOfProdDomain
statement: formalized
proof: formalized
---

# Nash implicit function theorem for systems

If the coordinates of a finite system are
Nash at `u` and its partial derivative in the unknown variables is invertible, every coordinate
of Mathlib's chosen implicit function is a Nash germ at the parameter point.

```lean
HasStrictFDerivAt.isNashAt_implicitFunctionOfProdDomain.{u_1, u_2, u_3} {σ : Type u_1}
  {τ : Type u_2} {ρ : Type u_3} [Fintype σ] [Fintype τ] [Fintype ρ] {F : (σ ⊕ τ → ℝ) → ρ → ℝ}
  {u : (σ → ℝ) × (τ → ℝ)} {D : (σ → ℝ) × (τ → ℝ) →L[ℝ] ρ → ℝ}
  (hD : HasStrictFDerivAt (fun p => F (Sum.elim p.1 p.2)) D u)
  (hInv : (D ∘SL ContinuousLinearMap.inr ℝ (σ → ℝ) (τ → ℝ)).IsInvertible)
  (hF : ∀ (i : ρ), TauCeti.IsNashAt (fun z => F z i) (Sum.elim u.1 u.2)) (i : τ) :
  TauCeti.IsNashAt (fun x => hD.implicitFunctionOfProdDomain hInv x i) u.1
```

## Depends on

- [TauCeti.IsNashAt](../../part-01/real-analytic-geometry-and-semianalytic-triangul/tauceti-isnashat.md)

## Proof depends on

- [The analytic implicit function theorem](../../../analysis/part-02/analytic/the-analytic-implicit-function-theorem.md)
- [The local Nash graph criterion](../../part-01/real-analytic-geometry-and-semianalytic-triangul/the-local-nash-graph-criterion.md)
- [The Tarski–Seidenberg theorem](../../part-01/complex-morse-theory-affine-topology-and-weak-le/the-tarski-seidenberg-theorem.md)

## Lean

Formalized in Tau Ceti as [`HasStrictFDerivAt.isNashAt_implicitFunctionOfProdDomain`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Nash/Implicit/System.html#HasStrictFDerivAt.isNashAt_implicitFunctionOfProdDomain).

## Sources

- [Tau Ceti documentation: `HasStrictFDerivAt.isNashAt_implicitFunctionOfProdDomain`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Nash/Implicit/System.html#HasStrictFDerivAt.isNashAt_implicitFunctionOfProdDomain)
- [Source of `HasStrictFDerivAt.isNashAt_implicitFunctionOfProdDomain` in TauCeti/Geometry/RealAlgebraic/Nash/Implicit/System.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/RealAlgebraic/Nash/Implicit/System.lean#L100)
