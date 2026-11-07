---
declaration: theorem
origin: cited
lean: TauCeti.primeNumberTheoremTransfer
statement: formalized
proof: formalized
---

# Prime-number-theorem transfer from exact boundary data

The three conclusions are,
respectively, the von Mangoldt-weighted prime-power asymptotic, the logarithmically weighted prime
asymptotic after removing higher powers, and the unweighted prime-counting asymptotic after Abel
summation.  The error-term formulation includes residue zero.

```lean
TauCeti.primeNumberTheoremTransfer.{u_1} {K : Type u_1} [Field K] [NumberField K]
  {S : Set (IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K))} {δ : ℝ}
  (B : TauCeti.PrimeBoundaryRemainder K S δ) :
  ((fun x => TauCeti.primePsi K S x - δ * x) =o[Filter.atTop] fun x => x) ∧
    ((fun x => TauCeti.primeTheta K S x - δ * x) =o[Filter.atTop] fun x => x) ∧
      (fun x => TauCeti.primeCount K S x - δ * TauCeti.Real.logIntegral x) =o[Filter.atTop] fun x =>
        x / Real.log x
```

## Depends on

- [Boundary data for the prime Dirichlet series of `S`](boundary-data-for-the-prime-dirichlet-series-of.md)

## Proof depends on

- [The Wiener--Ikehara theorem](the-wiener-ikehara-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.primeNumberTheoremTransfer`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Prime/Boundary.html#TauCeti.primeNumberTheoremTransfer).

## Sources

- [Tau Ceti documentation: `TauCeti.primeNumberTheoremTransfer`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Prime/Boundary.html#TauCeti.primeNumberTheoremTransfer)
- [Source of `TauCeti.primeNumberTheoremTransfer` in TauCeti/NumberTheory/ArithmeticDirichletSeries/Prime/Boundary.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ArithmeticDirichletSeries/Prime/Boundary.lean#L167)
- [Tau Ceti roadmap status: Arithmetic Dirichlet series and Tauberian methods](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ArithmeticDirichletSeries/STATUS.md)
