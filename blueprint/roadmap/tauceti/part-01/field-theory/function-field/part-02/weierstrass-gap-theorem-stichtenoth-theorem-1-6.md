---
declaration: theorem
origin: cited
lean: TauCeti.Place.card_weierstrassGaps
statement: formalized
proof: formalized
---

# Weierstrass gap theorem (Stichtenoth, Theorem 1.6.8)

at a rational place of a function
field with integrally closed constants and genus `g`, there are exactly `g` gaps.

```lean
TauCeti.Place.card_weierstrassGaps.{u_1, u_2} {k : Type u_1} {F : Type u_2} [Field k] [Field F]
  [Algebra k F] (hF : TauCeti.IsFunctionField k F) {P : TauCeti.Place k F} (hP : P.degree = 1) :
  P.weierstrassGaps.card = TauCeti.genus k F
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Riemann–Roch theorem (Stichtenoth, Theorem 1.5.15), for the divisor `(ω)` itself](../../../algebraic-geometry/algebraic-curves-function-fields-divisors-and-ri/the-riemann-roch-theorem-stichtenoth-theorem-1-5.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Place.card_weierstrassGaps`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Consequences/WeierstrassGaps.html#TauCeti.Place.card_weierstrassGaps).

## Sources

- [Tau Ceti documentation: `TauCeti.Place.card_weierstrassGaps`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Consequences/WeierstrassGaps.html#TauCeti.Place.card_weierstrassGaps)
- [Source of `TauCeti.Place.card_weierstrassGaps` in TauCeti/FieldTheory/FunctionField/Consequences/WeierstrassGaps.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/FunctionField/Consequences/WeierstrassGaps.lean#L301)
