---
declaration: theorem
origin: cited
lean: TauCeti.Contour.Cycle.homologyCauchyTheorem
statement: formalized
proof: formalized
---

# The homology Cauchy theorem for contour cycles

Let `C` be a finite formal integer
combination of closed piecewise-`C¹` curves whose trace lies in an open set `U`. If `C` is
null-homologous in `U` and `f` is holomorphic on `U`, with values in any complex normed space,
then the contour integral of `f` over the whole cycle vanishes.

The null-homology assumption is imposed only on `C`, not on each supported curve, so the theorem
includes cancellations between different generators.

```lean
TauCeti.Contour.Cycle.homologyCauchyTheorem.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] {f : ℂ → E} {C : TauCeti.Contour.Cycle} {U : Set ℂ} (hU : IsOpen U)
  (hCU : C.IsIn U) (hf : DifferentiableOn ℂ f U) (hnull : C.IsNullHomologous U) :
  (TauCeti.Contour.Cycle.integral f) C = 0
```

## Depends on

- [Generalized winding number](../../part-02/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number.md)
- [TauCeti.Contour.Cycle](../../part-02/contour-integration-and-the-hungerbuhler-wasem-g/tauceti-contour-cycle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.Cycle.homologyCauchyTheorem`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cycle/HomologyCauchy.html#TauCeti.Contour.Cycle.homologyCauchyTheorem).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.Cycle.homologyCauchyTheorem`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cycle/HomologyCauchy.html#TauCeti.Contour.Cycle.homologyCauchyTheorem)
- [Source of `TauCeti.Contour.Cycle.homologyCauchyTheorem` in TauCeti/Analysis/Contour/Cycle/HomologyCauchy.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/Cycle/HomologyCauchy.lean#L254)
- [Tau Ceti roadmap status: Banach algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BanachAlgebras/STATUS.md)
