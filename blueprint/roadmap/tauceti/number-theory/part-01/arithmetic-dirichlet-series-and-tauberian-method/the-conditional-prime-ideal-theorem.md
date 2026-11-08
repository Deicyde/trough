---
declaration: theorem
origin: cited
lean: TauCeti.primeIdealTheorem_of_boundary
statement: formalized
proof: formalized
---

# The conditional prime ideal theorem

Boundary data for all prime ideals with residue one
give the standard asymptotic equivalences for `ψ`, `ϑ`, and `π`.

```lean
TauCeti.primeIdealTheorem_of_boundary.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (B : TauCeti.PrimeBoundaryRemainder K Set.univ 1) :
  (Asymptotics.IsEquivalent Filter.atTop (TauCeti.primePsi K Set.univ) fun x => x) ∧
    (Asymptotics.IsEquivalent Filter.atTop (TauCeti.primeTheta K Set.univ) fun x => x) ∧
      Asymptotics.IsEquivalent Filter.atTop (TauCeti.primeCount K Set.univ) TauCeti.Real.logIntegral
```

## Depends on

- [Boundary data for the prime Dirichlet series of `S`](boundary-data-for-the-prime-dirichlet-series-of.md)

## Proof depends on

- [Prime-number-theorem transfer from exact boundary data](prime-number-theorem-transfer-from-exact-boundar.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.primeIdealTheorem_of_boundary`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Prime/Boundary.html#TauCeti.primeIdealTheorem_of_boundary).

## Sources

- [Tau Ceti documentation: `TauCeti.primeIdealTheorem_of_boundary`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Prime/Boundary.html#TauCeti.primeIdealTheorem_of_boundary)
- [Source of `TauCeti.primeIdealTheorem_of_boundary` in TauCeti/NumberTheory/ArithmeticDirichletSeries/Prime/Boundary.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ArithmeticDirichletSeries/Prime/Boundary.lean#L204)
