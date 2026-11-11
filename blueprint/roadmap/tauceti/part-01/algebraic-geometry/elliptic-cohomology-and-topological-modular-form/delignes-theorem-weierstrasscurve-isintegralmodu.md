---
declaration: theorem
origin: cited
lean: WeierstrassCurve.IsIntegralModularForm.mem_adjoin
statement: formalized
proof: formalized
---

# Deligne's theorem (`WeierstrassCurve.IsIntegralModularForm.mem_adjoin`)

Every integral modular form lies in the subring `ℤ[c₄, c₆, Δ]`.

```lean
WeierstrassCurve.IsIntegralModularForm.mem_adjoin {k : ℕ}
  {f : MvPolynomial WeierstrassCurve.Coeff ℤ} (hf : WeierstrassCurve.IsIntegralModularForm k f) :
  f ∈
    ℤ[WeierstrassCurve.c₄ WeierstrassCurve.Universal.curve,
      WeierstrassCurve.c₆ WeierstrassCurve.Universal.curve,
      WeierstrassCurve.Δ WeierstrassCurve.Universal.curve]
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.IsIntegralModularForm.mem_adjoin`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/ModularForm.html#WeierstrassCurve.IsIntegralModularForm.mem_adjoin).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.IsIntegralModularForm.mem_adjoin`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/ModularForm.html#WeierstrassCurve.IsIntegralModularForm.mem_adjoin)
- [Source of `WeierstrassCurve.IsIntegralModularForm.mem_adjoin` in TauCeti/AlgebraicGeometry/EllipticCurve/ModularForm.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/ModularForm.lean#L540)
