---
declaration: def
origin: cited
lean: TauCeti.periodBasis
statement: formalized
---

# TauCeti.periodBasis

The **period basis** at `y`: the periods `P y (b i)` of a `ℤ`-basis `b` of `Λ`, viewed as a
real basis of `E`. They form a `ℤ`-basis of the full lattice `LinearMap.range (P y)`, hence a real
basis of `E`. Its inverse coordinate map `x ↦ ∑ i, x i • P y (b i)` is the real linear
isomorphism `ℝ^ι ≃ E` carrying the standard lattice `ℤ^ι` onto the periods at `y`.

```lean
TauCeti.periodBasis.{u_1, u_2, u_3, u_4} {Y : Type u_1} {Λ : Type u_2} [AddCommGroup Λ]
  {E : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] (P : Y → Λ →ₗ[ℤ] E)
  [FiniteDimensional ℝ E] [∀ (y : Y), DiscreteTopology ↥(P y).range]
  [∀ (y : Y), IsZLattice ℝ (P y).range] {ι : Type u_4} (b : Module.Basis ι ℤ Λ)
  (hinj : ∀ (y : Y), Function.Injective ⇑(P y)) (y : Y) : Module.Basis ι ℝ E
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.periodBasis`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Family/Basic.html#TauCeti.periodBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.periodBasis`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Family/Basic.html#TauCeti.periodBasis)
- [Source of `TauCeti.periodBasis` in TauCeti/Algebra/Module/ZLattice/Family/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Module/ZLattice/Family/Basic.lean#L100)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexTori/STATUS.md)
