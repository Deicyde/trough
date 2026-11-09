---
declaration: def
origin: cited
lean: CategoryTheory.CommMon.invariantSubalgebraPresheaf
statement: formalized
---

# CategoryTheory.CommMon.invariantSubalgebraPresheaf

The presheaf of subalgebras of invariant sections of `A`.

```lean
CategoryTheory.CommMon.invariantSubalgebraPresheaf.{u, v} {X : AlgebraicGeometry.Scheme}
  {A : CategoryTheory.CommMon X.Modules} {G : Type v} [Group G] (ρ : G →* CategoryTheory.Aut A) :
  A.SubalgebraPresheaf
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.CommMon.invariantSubalgebraPresheaf`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Quotient/FiniteGroup/Relative/Basic.html#CategoryTheory.CommMon.invariantSubalgebraPresheaf).

## Sources

- [Tau Ceti documentation: `CategoryTheory.CommMon.invariantSubalgebraPresheaf`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Quotient/FiniteGroup/Relative/Basic.html#CategoryTheory.CommMon.invariantSubalgebraPresheaf)
- [Source of `CategoryTheory.CommMon.invariantSubalgebraPresheaf` in TauCeti/AlgebraicGeometry/Quotient/FiniteGroup/Relative/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Quotient/FiniteGroup/Relative/Basic.lean#L190)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularCurves/STATUS.md)
