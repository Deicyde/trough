---
declaration: theorem
origin: cited
lean: TauCeti.tateIdentityY_sq_sub_X_mul_tateIdentityX_mul_tateIdentityY
statement: formalized
proof: formalized
---

# The Tate point near the identity lies on the Tate curve

With `x = X(1 + T)` and
`y = Y(1 + T)`, the equation `y² + x y = x³ + a₄(q) x + a₆(q)`, multiplied by `T⁶`, holds in
`ℤ⟦q⟧⟦T⟧` for `T² x = tateIdentityX` and `-T³ y = tateIdentityY`.

```lean
TauCeti.tateIdentityY_sq_sub_X_mul_tateIdentityX_mul_tateIdentityY :
  TauCeti.tateIdentityY ^ 2 - PowerSeries.X * TauCeti.tateIdentityX * TauCeti.tateIdentityY =
    TauCeti.tateIdentityX ^ 3 +
        PowerSeries.X ^ 4 * PowerSeries.C TauCeti.tateCurve.a₄ * TauCeti.tateIdentityX +
      PowerSeries.X ^ 6 * PowerSeries.C TauCeti.tateCurve.a₆
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.tateIdentityY_sq_sub_X_mul_tateIdentityX_mul_tateIdentityY`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/TateCurve/FormalGroup.html#TauCeti.tateIdentityY_sq_sub_X_mul_tateIdentityX_mul_tateIdentityY).

## Sources

- [Tau Ceti documentation: `TauCeti.tateIdentityY_sq_sub_X_mul_tateIdentityX_mul_tateIdentityY`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/TateCurve/FormalGroup.html#TauCeti.tateIdentityY_sq_sub_X_mul_tateIdentityX_mul_tateIdentityY)
- [Source of `TauCeti.tateIdentityY_sq_sub_X_mul_tateIdentityX_mul_tateIdentityY` in TauCeti/AlgebraicGeometry/EllipticCurve/TateCurve/FormalGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/TateCurve/FormalGroup.lean#L272)
