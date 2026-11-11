---
declaration: def
origin: cited
lean: TauCeti.torusExteriorPowerEquiv
statement: formalized
---

# The homology of a torus is the exterior algebra on its first homology

over any
commutative ring `k`, the Pontryagin product induces an isomorphism `⋀ⁿ H₁(Tⁱ; k) ≃ Hₙ(Tⁱ; k)` for
the torus `Tⁱ = ι → S¹`, sending `a₁ ∧ ⋯ ∧ aₙ` to `a₁ ⋯ aₙ`.

```lean
TauCeti.torusExteriorPowerEquiv.{u} (k : Type u) [CommRing k] (ι : Type u) [Finite ι] (n : ℕ) :
  ↥(⋀[k]^n
        ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) 1).obj
                (CategoryTheory.MonoidalCategoryStruct.tensorUnit (ModuleCat k))).obj
            ↧(ι → ULift.{u, 0} Circle))) ≃ₗ[k]
    ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) n).obj
            (CategoryTheory.MonoidalCategoryStruct.tensorUnit (ModuleCat k))).obj
        ↧(ι → ULift.{u, 0} Circle))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Eilenberg–Zilber theorem for singular chains](../singular/the-eilenberg-zilber-theorem-for-singular-chains.md)
- [The Künneth theorem for cubical homology](../singular/the-kunneth-theorem-for-cubical-homology.md)
- [The Mayer–Vietoris isomorphism of a sphere](../singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.torusExteriorPowerEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Torus/Exterior.html#TauCeti.torusExteriorPowerEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.torusExteriorPowerEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Torus/Exterior.html#TauCeti.torusExteriorPowerEquiv)
- [Source of `TauCeti.torusExteriorPowerEquiv` in TauCeti/AlgebraicTopology/Singular/Torus/Exterior.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Singular/Torus/Exterior.lean#L340)
- [Tau Ceti roadmap status: Algebraic topology of spaces and manifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AlgebraicTopology/STATUS.md)
