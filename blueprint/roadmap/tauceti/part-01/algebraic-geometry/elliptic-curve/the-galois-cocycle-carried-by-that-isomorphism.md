---
declaration: theorem
origin: cited
lean: WeierstrassCurve.map_quadraticTwistOfTraceNormVariableChange
statement: formalized
proof: formalized
---

# The Galois cocycle carried by that isomorphism

Conjugating
`quadraticTwistOfTraceNormVariableChange` by the nontrivial `σ ∈ Gal(L/K)` changes it by
`negVariableChange`, the change of variables `[-1]`: this is the cocycle identity for
`H¹(Gal(L/K), Aut E)`.

It does **not** say the class is nontrivial. `E` here is an arbitrary Weierstrass curve, and when
`negVariableChange = 1` — a singular curve in characteristic 2 with `a₁ = a₃ = 0`, say — the
identity below is plain equivariance. Nontriviality needs hypotheses this statement does not
carry.

```lean
WeierstrassCurve.map_quadraticTwistOfTraceNormVariableChange.{u_1, u_2} {K : Type u_1} [Field K]
  {L : Type u_2} [Field L] [Algebra K L] (E : WeierstrassCurve K) [Algebra.IsQuadraticExtension K L]
  {θ : L} (hθ : θ ∉ Set.range ⇑(algebraMap K L)) {σ : Gal(L/K)} (hσ : σ ≠ 1) :
  (E.quadraticTwistOfTraceNormVariableChange hθ hσ).map ↑σ =
    (E.baseChange L).negVariableChange * E.quadraticTwistOfTraceNormVariableChange hθ hσ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.map_quadraticTwistOfTraceNormVariableChange`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/QuadraticTwist/Basic.html#WeierstrassCurve.map_quadraticTwistOfTraceNormVariableChange).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.map_quadraticTwistOfTraceNormVariableChange`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/QuadraticTwist/Basic.html#WeierstrassCurve.map_quadraticTwistOfTraceNormVariableChange)
- [Source of `WeierstrassCurve.map_quadraticTwistOfTraceNormVariableChange` in TauCeti/AlgebraicGeometry/EllipticCurve/QuadraticTwist/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/QuadraticTwist/Basic.lean#L582)
