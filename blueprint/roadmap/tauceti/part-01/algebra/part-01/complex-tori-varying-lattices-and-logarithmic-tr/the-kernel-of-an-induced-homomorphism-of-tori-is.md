---
declaration: theorem
origin: cited
lean: Submodule.isSmoothEmbedding_subtypeVal_ker_orbitRelQuotientMap
statement: formalized
proof: formalized
---

# The kernel of an induced homomorphism of tori is an embedded Lie subgroup

Let a linear
map `f : E → E'` over `𝕜 = ℝ` or `ℂ` carry a full lattice `L` into a discrete subgroup `L'`. The
inclusion into `E / L` of the kernel `f⁻¹(L') / L` of the induced map `E / L → E' / L'` is a `C^n`
embedding. For `𝕜 = ℂ` and `n = ω` this makes the kernel a closed complex Lie subgroup of the
complex torus `E / L`; it is closed by `Submodule.isClosed_orbitRelQuotient_mk_image_preimage`.

```lean
Submodule.isSmoothEmbedding_subtypeVal_ker_orbitRelQuotientMap.{u_4, u_5, u_6} {n : WithTop ℕ∞}
  {𝕜 : Type u_4} [RCLike 𝕜] {E : Type u_5} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [NormedSpace 𝕜 E] [IsScalarTower ℝ 𝕜 E] [FiniteDimensional ℝ E] {E' : Type u_6}
  [NormedAddCommGroup E'] [NormedSpace 𝕜 E'] (L : Submodule ℤ E) [DiscreteTopology ↥L]
  [IsZLattice ℝ L] {L' : Submodule ℤ E'} [DiscreteTopology ↥L'] (f : E →ₗ[𝕜] E')
  (h : L ≤ Submodule.comap (↑ℤ f) L') :
  Manifold.IsSmoothEmbedding (modelWithCornersSelf 𝕜 ↥f.ker) (modelWithCornersSelf 𝕜 E) n
    Subtype.val
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Submodule.isSmoothEmbedding_subtypeVal_ker_orbitRelQuotientMap`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Algebra/Quotient.html#Submodule.isSmoothEmbedding_subtypeVal_ker_orbitRelQuotientMap).

## Sources

- [Tau Ceti documentation: `Submodule.isSmoothEmbedding_subtypeVal_ker_orbitRelQuotientMap`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Algebra/Quotient.html#Submodule.isSmoothEmbedding_subtypeVal_ker_orbitRelQuotientMap)
- [Source of `Submodule.isSmoothEmbedding_subtypeVal_ker_orbitRelQuotientMap` in TauCeti/Geometry/Manifold/Algebra/Quotient.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Algebra/Quotient.lean#L559)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexTori/STATUS.md)
