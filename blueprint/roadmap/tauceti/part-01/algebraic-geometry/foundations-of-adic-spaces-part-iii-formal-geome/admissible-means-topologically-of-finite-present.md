---
declaration: theorem
origin: cited
lean: TauCeti.Huber.isAdmissibleAlgebra_iff_flat
statement: formalized
proof: formalized
---

# Admissible means topologically of finite presentation and flat

Over a valuation ring `O`
that is separated for the `ϖ`-adic topology, with `ϖ ≠ 0`, an `O`-algebra is admissible exactly
when it is topologically of finite presentation and flat over `O`: having no `ϖ`-torsion means
having no torsion at all, and torsion-free modules over the Bézout domain `O` are flat
(Bosch–Lütkebohmert I, §1, p. 293).

```lean
TauCeti.Huber.isAdmissibleAlgebra_iff_flat.{u_1, u_2} {O : Type u_1} [CommRing O]
  [TopologicalSpace O] [NonarchimedeanRing O] {A : Type u_2} [CommRing A] [Algebra O A] [IsDomain O]
  [ValuationRing O] {ϖ : O} (hϖ : ϖ ≠ 0) [IsHausdorff (Ideal.span {ϖ}) O] :
  TauCeti.Huber.IsAdmissibleAlgebra ϖ A ↔
    TauCeti.Huber.IsTopologicallyFinitePresentation O A ∧ Module.Flat O A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.isAdmissibleAlgebra_iff_flat`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/TopologicallyFiniteType/FinitePresentation.html#TauCeti.Huber.isAdmissibleAlgebra_iff_flat).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.isAdmissibleAlgebra_iff_flat`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/TopologicallyFiniteType/FinitePresentation.html#TauCeti.Huber.isAdmissibleAlgebra_iff_flat)
- [Source of `TauCeti.Huber.isAdmissibleAlgebra_iff_flat` in TauCeti/RingTheory/Huber/TopologicallyFiniteType/FinitePresentation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Huber/TopologicallyFiniteType/FinitePresentation.lean#L255)
- [Tau Ceti roadmap status: Foundations of adic spaces, part III — formal geometry, formal models and coherent sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartIII/STATUS.md)
