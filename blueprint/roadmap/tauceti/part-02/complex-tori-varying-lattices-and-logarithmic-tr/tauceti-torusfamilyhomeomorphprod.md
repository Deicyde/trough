---
declaration: def
origin: cited
lean: TauCeti.torusFamilyHomeomorphProd
statement: formalized
---

# TauCeti.torusFamilyHomeomorphProd

**The global trivialization** of a continuous family of full lattices. For a `ℤ`-basis `b`
of `Λ` indexed by `ι`, the map `[y, v] ↦ (y, [F_y⁻¹ v])`, with `F_y⁻¹` the coordinate map of the
period basis at `y`, is a homeomorphism from the orbit space of the period translation action to
the product of `Y` with the fixed torus `ℝ^ι/ℤ^ι`. It lies over `Y`
(`TauCeti.fst_torusFamilyHomeomorphProd`), and on each fibre it is induced by the real linear
isomorphism `F_y⁻¹`.

```lean
TauCeti.torusFamilyHomeomorphProd.{u_1, u_2, u_3, u_4} {Y : Type u_1} {Λ : Type u_2}
  [AddCommGroup Λ] {E : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  (P : Y → Λ →ₗ[ℤ] E) [∀ (y : Y), DiscreteTopology ↥(P y).range]
  [∀ (y : Y), IsZLattice ℝ (P y).range] {ι : Type u_4} [Finite ι] (b : Module.Basis ι ℤ Λ)
  (hinj : ∀ (y : Y), Function.Injective ⇑(P y)) [TopologicalSpace Y]
  (hcont : ∀ (l : Λ), Continuous fun y => (P y) l) :
  AddAction.orbitRel.Quotient Λ (Y × E) ≃ₜ
    Y × (ι → ℝ) ⧸ Submodule.span ℤ (Set.range ⇑(Pi.basisFun ℝ ι))
```

## Depends on

- [TauCeti.periodBasis](tauceti-periodbasis.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.torusFamilyHomeomorphProd`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Family/HomeomorphProd.html#TauCeti.torusFamilyHomeomorphProd).

## Sources

- [Tau Ceti documentation: `TauCeti.torusFamilyHomeomorphProd`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Family/HomeomorphProd.html#TauCeti.torusFamilyHomeomorphProd)
- [Source of `TauCeti.torusFamilyHomeomorphProd` in TauCeti/Algebra/Module/ZLattice/Family/HomeomorphProd.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Module/ZLattice/Family/HomeomorphProd.lean#L95)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexTori/STATUS.md)
