---
declaration: theorem
origin: cited
lean: TauCeti.CurveX3SubX.hurwitz_genus_formula
statement: formalized
proof: formalized
---

# The Hurwitz genus formula for `y² = x³ - x` over `K(x)`, as a numerical identity

with
`e - 1` summed over the four ramified places,

`2 g - 2 = [K(W) : K(x)] (2 g(K(x)) - 2) + ∑ (e - 1)`,

which reads `2 · 1 - 2 = 2 · (0 - 2) + 4`. The genus `g = 1` on the left is computed from the
Riemann–Roch spaces `L(n · O)` (`WeierstrassCurve.Affine.genus_functionField`), independently of
the ramification data on the right.

```lean
TauCeti.CurveX3SubX.hurwitz_genus_formula.{u_1} {K : Type u_1} [Field K] [NeZero 2] :
  2 * ↑(TauCeti.genus K (TauCeti.CurveX3SubX.curve K).toAffine.FunctionField) - 2 =
    ↑(Module.finrank (RatFunc K) (TauCeti.CurveX3SubX.curve K).toAffine.FunctionField) *
        (2 * ↑(TauCeti.genus K (RatFunc K)) - 2) +
      (↑(TauCeti.Place.ramificationIdx (RatFunc K)
                  (TauCeti.Place.infinity (TauCeti.CurveX3SubX.curve K).toAffine)) -
              1 +
            (↑(TauCeti.Place.ramificationIdx (RatFunc K)
                  ↑((TauCeti.CurveX3SubX.curve K).toAffine.pointEquivDegreeOnePlace
                      (TauCeti.CurveX3SubX.pointZero K))) -
              1) +
          (↑(TauCeti.Place.ramificationIdx (RatFunc K)
                ↑((TauCeti.CurveX3SubX.curve K).toAffine.pointEquivDegreeOnePlace
                    (TauCeti.CurveX3SubX.pointOne K))) -
            1) +
        (↑(TauCeti.Place.ramificationIdx (RatFunc K)
              ↑((TauCeti.CurveX3SubX.curve K).toAffine.pointEquivDegreeOnePlace
                  (TauCeti.CurveX3SubX.pointNegOne K))) -
          1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../field-theory/function-field/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [The Riemann–Roch theorem (Stichtenoth, Theorem 1.5.15), for the divisor `(ω)` itself](../algebraic-curves-function-fields-divisors-and-ri/the-riemann-roch-theorem-stichtenoth-theorem-1-5.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CurveX3SubX.hurwitz_genus_formula`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Affine/FunctionField/TameDifferent.html#TauCeti.CurveX3SubX.hurwitz_genus_formula).

## Sources

- [Tau Ceti documentation: `TauCeti.CurveX3SubX.hurwitz_genus_formula`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Affine/FunctionField/TameDifferent.html#TauCeti.CurveX3SubX.hurwitz_genus_formula)
- [Source of `TauCeti.CurveX3SubX.hurwitz_genus_formula` in TauCeti/AlgebraicGeometry/EllipticCurve/Affine/FunctionField/TameDifferent.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/Affine/FunctionField/TameDifferent.lean#L139)
