---
declaration: theorem
origin: cited
lean: TauCeti.natCard_quotSMulTop_div_natCard_torsionBy_of_exact
statement: formalized
proof: formalized
---

# Multiplicativity of the Euler quotient

**Multiplicativity of the Euler quotient** along a short exact sequence
`0 → M₁ → M₂ → M₃ → 0` whose outer terms have finite `r`-torsion:
`χ_r(M₂) = χ_r(M₁) χ_r(M₃)`. The cokernels are unconstrained: if one of them is infinite, both
sides are `0`.

```lean
TauCeti.natCard_quotSMulTop_div_natCard_torsionBy_of_exact.{u_1, u_2, u_3, u_4} {R : Type u_1}
  [CommRing R] (r : R) {M₁ : Type u_2} {M₂ : Type u_3} {M₃ : Type u_4} [AddCommGroup M₁]
  [_root_.Module R M₁] [AddCommGroup M₂] [_root_.Module R M₂] [AddCommGroup M₃] [_root_.Module R M₃]
  {f : M₁ →ₗ[R] M₂} {g : M₂ →ₗ[R] M₃} (hfg : Function.Exact ⇑f ⇑g) (hf : Function.Injective ⇑f)
  (hg : Function.Surjective ⇑g) [Finite ↥(Submodule.torsionBy R M₁ r)]
  [Finite ↥(Submodule.torsionBy R M₃ r)] :
  ↑(Nat.card (QuotSMulTop r M₂)) / ↑(Nat.card ↥(Submodule.torsionBy R M₂ r)) =
    ↑(Nat.card (QuotSMulTop r M₁)) / ↑(Nat.card ↥(Submodule.torsionBy R M₁ r)) *
      (↑(Nat.card (QuotSMulTop r M₃)) / ↑(Nat.card ↥(Submodule.torsionBy R M₃ r)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.natCard_quotSMulTop_div_natCard_torsionBy_of_exact`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/Torsion/EulerQuotient.html#TauCeti.natCard_quotSMulTop_div_natCard_torsionBy_of_exact).

## Sources

- [Tau Ceti documentation: `TauCeti.natCard_quotSMulTop_div_natCard_torsionBy_of_exact`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/Torsion/EulerQuotient.html#TauCeti.natCard_quotSMulTop_div_natCard_torsionBy_of_exact)
- [Source of `TauCeti.natCard_quotSMulTop_div_natCard_torsionBy_of_exact` in TauCeti/Algebra/Module/Torsion/EulerQuotient.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Module/Torsion/EulerQuotient.lean#L118)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
