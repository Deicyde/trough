---
declaration: theorem
origin: cited
lean: TauCeti.EulerProductData.hasSum_idealTerm_vonMangoldt_of_zeroFree
statement: formalized
proof: formalized
---

# The logarithmic derivative of an Euler product as a von Mangoldt series

Suppose `Re(s)`
lies strictly to the right of the ideal-indexed abscissa of absolute convergence of `D` and every
local power series is zero-free on the disk of radius `N(P)⁻σ` for a real `σ < Re(s)`. Then the
ideal-indexed series of `Λ_D` converges absolutely at `s` to `-L'(s)/L(s)`, where `L` is the
`LSeries` of the norm coefficients of `D`:

`-logDeriv L(s) = ∑' A, Λ_D(A) / N(A) ^ s`.

```lean
TauCeti.EulerProductData.hasSum_idealTerm_vonMangoldt_of_zeroFree.{u_1} {K : Type u_1} [Field K]
  [NumberField K] (D : TauCeti.EulerProductData K) {σ : ℝ} {s : ℂ}
  (habs : TauCeti.idealAbscissaOfAbsConv K D.toIdealArithmeticFunction < ↑s.re)
  (hne :
    ∀ (P : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)) (z : ℂ),
      ‖z‖ < ‖↑(Ideal.absNorm P.asIdeal) ^ (-↑σ)‖ →
        FormalMultilinearSeries.ofScalarsSum (fun n => (PowerSeries.coeff n) (D.localPowerSeries P))
            z ≠
          0)
  (hs : σ < s.re) :
  HasSum (TauCeti.idealTerm K D.vonMangoldt s)
    (-logDeriv (LSeries ⇑((TauCeti.normCoeff K) D.toIdealArithmeticFunction)) s)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The analytic Euler product](the-analytic-euler-product.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.EulerProductData.hasSum_idealTerm_vonMangoldt_of_zeroFree`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/EulerProduct/Logarithm/VonMangoldtCoeff.html#TauCeti.EulerProductData.hasSum_idealTerm_vonMangoldt_of_zeroFree).

## Sources

- [Tau Ceti documentation: `TauCeti.EulerProductData.hasSum_idealTerm_vonMangoldt_of_zeroFree`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/EulerProduct/Logarithm/VonMangoldtCoeff.html#TauCeti.EulerProductData.hasSum_idealTerm_vonMangoldt_of_zeroFree)
- [Source of `TauCeti.EulerProductData.hasSum_idealTerm_vonMangoldt_of_zeroFree` in TauCeti/NumberTheory/ArithmeticDirichletSeries/EulerProduct/Logarithm/VonMangoldtCoeff.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ArithmeticDirichletSeries/EulerProduct/Logarithm/VonMangoldtCoeff.lean#L382)
- [Tau Ceti roadmap status: Arithmetic Dirichlet series and Tauberian methods](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ArithmeticDirichletSeries/STATUS.md)
