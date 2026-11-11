---
declaration: def
origin: cited
lean: TauCeti.torusFamilyMarking
statement: formalized
---

# TauCeti.torusFamilyMarking

The **canonical marking** of the fibre over `y` of a period family: the identification
`H₁(T_y; ℤ) ≃ₗ[ℤ] Λ` of the first integral homology of the torus `T_y` over `y` with the lattice
`Λ`. It identifies the fibre with `E / LinearMap.range (P y)`, applies
`AddSubgroup.orbitRelQuotientFirstHomologyEquiv`, and pulls the period back along the injective
map `P y`. The class of a loop goes to its period displacement
(`TauCeti.torusFamilyMarking_loopClass`).

```lean
TauCeti.torusFamilyMarking.{u_1} {Y E : Type} [TopologicalSpace Y] [AddCommGroup E]
  [TopologicalSpace E] [IsTopologicalAddGroup E] [SimplyConnectedSpace E] {Λ : Type u_1}
  [AddCommGroup Λ] (P : Y → Λ →ₗ[ℤ] E) [∀ (y : Y), DiscreteTopology ↥(P y).range]
  (hcont : ∀ (l : Λ), Continuous fun y => (P y) l) (hinj : ∀ (y : Y), Function.Injective ⇑(P y))
  (y : Y) :
  ↑(HomologicalComplex.homology
        ((TauCeti.singularChains ℤ).obj ↧↑{z | TauCeti.torusFamilyProjection P z = y}) 1) ≃ₗ[ℤ]
    Λ
```

## Depends on

- [The Hurewicz theorem](../../../algebraic-topology/algebraic-topology-of-spaces-and-manifolds/the-hurewicz-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.torusFamilyMarking`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Torus/Family.html#TauCeti.torusFamilyMarking).

## Sources

- [Tau Ceti documentation: `TauCeti.torusFamilyMarking`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Torus/Family.html#TauCeti.torusFamilyMarking)
- [Source of `TauCeti.torusFamilyMarking` in TauCeti/AlgebraicTopology/Singular/Torus/Family.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Singular/Torus/Family.lean#L117)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexTori/STATUS.md)
