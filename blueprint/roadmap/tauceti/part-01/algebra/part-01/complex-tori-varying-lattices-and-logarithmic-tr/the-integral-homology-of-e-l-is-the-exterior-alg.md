---
declaration: def
origin: cited
lean: Submodule.orbitRelQuotientHomologyEquiv
statement: formalized
---

# The integral homology of `E / L` is the exterior algebra on `L`

For a full lattice `L`
in a finite-dimensional real normed space `E`, for instance the period lattice of a complex torus,
`Hₙ(E / L; ℤ) ≃ ⋀ⁿ L` for every `n`. The inverse sends `l₁ ∧ ⋯ ∧ lₙ` to the Pontryagin product of
the classes of `l₁, …, lₙ` (`Submodule.orbitRelQuotientHomologyEquiv_symm_ιMulti`).

```lean
Submodule.orbitRelQuotientHomologyEquiv {E : Type} [NormedAddCommGroup E] [NormedSpace ℝ E]
  (L : Submodule ℤ E) [DiscreteTopology ↥L] [FiniteDimensional ℝ E] [IsZLattice ℝ L] (n : ℕ) :
  ↑(HomologicalComplex.homology
        ((TauCeti.singularChains ℤ).obj ↧(AddAction.orbitRel.Quotient (↥L) E)) n) ≃ₗ[ℤ]
    ↥(⋀[ℤ]^n ↥L)
```

## Depends on

- [The Hurewicz theorem](../../../algebraic-topology/algebraic-topology-of-spaces-and-manifolds/the-hurewicz-theorem.md)

## Proof depends on

- [The Eilenberg–Zilber theorem for singular chains](../../../algebraic-topology/singular/the-eilenberg-zilber-theorem-for-singular-chains.md)
- [The Künneth theorem for cubical homology](../../../algebraic-topology/singular/the-kunneth-theorem-for-cubical-homology.md)
- [The Mayer–Vietoris isomorphism of a sphere](../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)

## Lean

Formalized in Tau Ceti as [`Submodule.orbitRelQuotientHomologyEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Torus/ZLattice.html#Submodule.orbitRelQuotientHomologyEquiv).

## Sources

- [Tau Ceti documentation: `Submodule.orbitRelQuotientHomologyEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Torus/ZLattice.html#Submodule.orbitRelQuotientHomologyEquiv)
- [Source of `Submodule.orbitRelQuotientHomologyEquiv` in TauCeti/AlgebraicTopology/Singular/Torus/ZLattice.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Singular/Torus/ZLattice.lean#L203)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexTori/STATUS.md)
