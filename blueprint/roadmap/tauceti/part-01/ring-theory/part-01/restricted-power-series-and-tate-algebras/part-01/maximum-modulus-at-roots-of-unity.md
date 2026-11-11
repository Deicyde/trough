---
declaration: theorem
origin: cited
lean: MvPowerSeries.exists_norm_restrictedEval₂_eq_norm
statement: formalized
proof: formalized
---

# Maximum modulus at roots of unity

Let `φ : R → S` be an isometric ring homomorphism into
a complete ultrametric normed field containing a primitive `m`-th root of unity `ζ`, where
`‖m‖ = 1` in `S` and `m` exceeds every exponent of every coefficient of `f` of norm `‖f‖`. Then
there is a point `x` of the closed unit polydisc of `S ^ k`, with coordinates powers of `ζ`, at
which `‖f(x)‖ = ‖f‖`.

```lean
MvPowerSeries.exists_norm_restrictedEval₂_eq_norm.{u_1, u_2} {k : ℕ} {R : Type u_1} {S : Type u_2}
  [NormedCommRing R] [IsUltrametricDist R] [NormedField S] [IsUltrametricDist S] [CompleteSpace S]
  (φ : R →+* S) (hφ : ∀ (r : R), ‖φ r‖ = ‖r‖) {m : ℕ} {ζ : S} (hζ : IsPrimitiveRoot ζ m)
  (hm : ‖↑m‖ = 1) (f : ↥(MvPowerSeries.IsRestricted.subring fun x => 1))
  (hfm : ∀ (t : Fin k →₀ ℕ), ‖(MvPowerSeries.coeff t) ↑f‖ = ‖f‖ → ∀ (i : Fin k), t i < m) :
  ∃ x,
    ∃ (hx : ∀ (i : Fin k), ‖x i‖ ≤ 1),
      (∀ (i : Fin k), ∃ a < m, x i = ζ ^ a) ∧ ‖(MvPowerSeries.restrictedEval₂ φ x ⋯ hx) f‖ = ‖f‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MvPowerSeries.exists_norm_restrictedEval₂_eq_norm`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/MaximumModulus.html#MvPowerSeries.exists_norm_restrictedEval%E2%82%82_eq_norm).

## Sources

- [Tau Ceti documentation: `MvPowerSeries.exists_norm_restrictedEval₂_eq_norm`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/MaximumModulus.html#MvPowerSeries.exists_norm_restrictedEval%E2%82%82_eq_norm)
- [Source of `MvPowerSeries.exists_norm_restrictedEval₂_eq_norm` in TauCeti/RingTheory/MvPowerSeries/TateAlgebra/MaximumModulus.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/MaximumModulus.lean#L104)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
