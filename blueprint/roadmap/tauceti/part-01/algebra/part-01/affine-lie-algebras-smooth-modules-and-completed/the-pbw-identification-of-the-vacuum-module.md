---
declaration: def
origin: cited
lean: TauCeti.CurrentAlgebra.vacuumPBWEquiv
statement: formalized
---

# The PBW identification of the vacuum module

Over a field, `y ↦ y |0⟩` is a linear
isomorphism from the enveloping algebra `U(t⁻¹ L[t⁻¹])` of the negative currents onto the vacuum
module, for every form `Φ` and every central value `a`, including the critical level and `a = 0`.
It intertwines left multiplication on `U(t⁻¹ L[t⁻¹])` with the action on the vacuum module
(`TauCeti.CurrentAlgebra.vacuumPBWEquiv_mul`), so the vacuum module is a free module of rank one
over `U(t⁻¹ L[t⁻¹])` on the vacuum.

```lean
TauCeti.CurrentAlgebra.vacuumPBWEquiv.{u_1, u_2} {K : Type u_1} {L : Type u_2} [Field K] [LieRing L]
  [LieAlgebra K L] (Φ : LinearMap.BilinForm K L) (hΦ : LinearMap.BilinForm.lieInvariant L Φ)
  (hΦs : Φ.IsSymm) (a : K) :
  UniversalEnvelopingAlgebra K ↥(TauCeti.CurrentAlgebra.negativeLieSubalgebra Φ hΦ hΦs) ≃ₗ[K]
    TauCeti.CurrentAlgebra.VacuumModule Φ hΦ hΦs a
```

## Depends on

- [TauCeti.CurrentAlgebra.VacuumModule](tauceti-currentalgebra-vacuummodule.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CurrentAlgebra.vacuumPBWEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/Vacuum/Basic.html#TauCeti.CurrentAlgebra.vacuumPBWEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.CurrentAlgebra.vacuumPBWEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/Vacuum/Basic.html#TauCeti.CurrentAlgebra.vacuumPBWEquiv)
- [Source of `TauCeti.CurrentAlgebra.vacuumPBWEquiv` in TauCeti/Algebra/Lie/Current/Vacuum/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Current/Vacuum/Basic.lean#L342)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
