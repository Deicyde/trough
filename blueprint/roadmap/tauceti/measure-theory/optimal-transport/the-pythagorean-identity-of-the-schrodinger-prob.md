---
declaration: theorem
origin: cited
lean: TauCeti.IsCoupling.klDiv_eq_klDiv_add_klDiv_of_eq_withDensity
statement: formalized
proof: formalized
---

# The Pythagorean identity of the Schrödinger problem

Let `π` be a coupling of `μ` and `ν`
whose density against the finite reference `R` is `exp (φ(x) + ψ(y))`, for measurable potentials
`φ ∈ L¹(μ)` and `ψ ∈ L¹(ν)`. Then every coupling `γ` of `μ` and `ν` satisfies
`klDiv γ R = klDiv γ π + klDiv π R`.

```lean
TauCeti.IsCoupling.klDiv_eq_klDiv_add_klDiv_of_eq_withDensity.{u_1, u_2} {X : Type u_1}
  {Y : Type u_2} [MeasurableSpace X] [MeasurableSpace Y] {π R : MeasureTheory.Measure (X × Y)}
  {μ : MeasureTheory.Measure X} {ν : MeasureTheory.Measure Y} {φ : X → ℝ} {ψ : Y → ℝ}
  [MeasureTheory.IsFiniteMeasure μ] [MeasureTheory.IsFiniteMeasure R]
  {γ : MeasureTheory.Measure (X × Y)} (hγ : TauCeti.IsCoupling γ μ ν)
  (hπ : TauCeti.IsCoupling π μ ν)
  (hπR : π = R.withDensity fun z => ENNReal.ofReal (Real.exp (φ z.1 + ψ z.2))) (hφ : Measurable φ)
  (hψ : Measurable ψ) (hφi : MeasureTheory.Integrable φ μ) (hψi : MeasureTheory.Integrable ψ ν) :
  InformationTheory.klDiv γ R = InformationTheory.klDiv γ π + InformationTheory.klDiv π R
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Csiszár's Pythagorean identity](../../other-areas/information-theory/csiszars-pythagorean-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsCoupling.klDiv_eq_klDiv_add_klDiv_of_eq_withDensity`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Entropic/Basic.html#TauCeti.IsCoupling.klDiv_eq_klDiv_add_klDiv_of_eq_withDensity).

## Sources

- [Tau Ceti documentation: `TauCeti.IsCoupling.klDiv_eq_klDiv_add_klDiv_of_eq_withDensity`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Entropic/Basic.html#TauCeti.IsCoupling.klDiv_eq_klDiv_add_klDiv_of_eq_withDensity)
- [Source of `TauCeti.IsCoupling.klDiv_eq_klDiv_add_klDiv_of_eq_withDensity` in TauCeti/MeasureTheory/OptimalTransport/Entropic/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/Entropic/Basic.lean#L337)
