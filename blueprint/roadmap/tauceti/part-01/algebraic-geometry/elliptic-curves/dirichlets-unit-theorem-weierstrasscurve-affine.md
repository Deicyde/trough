---
declaration: theorem
origin: cited
lean: WeierstrassCurve.Affine.fg_units_ringOfIntegersFactor
statement: formalized
proof: formalized
---

# Dirichlet's unit theorem (`WeierstrassCurve.Affine.fg_units_ringOfIntegersFactor`)

**Dirichlet's unit theorem** for the field factors of the étale algebra of a curve over a
number field: the ring of integers of each factor `F[X] ⧸ (p)` has finitely generated unit
group.

```lean
WeierstrassCurve.Affine.fg_units_ringOfIntegersFactor.{u_2} {F : Type u_2} [Field F] [NumberField F]
  (W : WeierstrassCurve.Affine F) (p : W.f.Factors) :
  Monoid.FG (W.ringOfIntegersFactor (NumberField.RingOfIntegers F) p)ˣ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dirichlet's unit theorem (`NumberField.fg_units_integralClosure`)](../../number-theory/part-02/number-field/dirichlets-unit-theorem-numberfield-fg-units-int.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.Affine.fg_units_ringOfIntegersFactor`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/FinitelyGenerated.html#WeierstrassCurve.Affine.fg_units_ringOfIntegersFactor).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.Affine.fg_units_ringOfIntegersFactor`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/FinitelyGenerated.html#WeierstrassCurve.Affine.fg_units_ringOfIntegersFactor)
- [Source of `WeierstrassCurve.Affine.fg_units_ringOfIntegersFactor` in TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/FinitelyGenerated.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/FinitelyGenerated.lean#L129)
