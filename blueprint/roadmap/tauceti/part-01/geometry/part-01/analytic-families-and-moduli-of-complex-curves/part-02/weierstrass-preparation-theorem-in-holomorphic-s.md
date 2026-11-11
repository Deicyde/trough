---
declaration: theorem
origin: cited
lean: TauCeti.holomorphicStructureSheaf.existsUnique_weierstrassPreparation
statement: formalized
proof: formalized
---

# Weierstrass preparation theorem in holomorphic stalks

Every holomorphic germ `f` at
`(x₀, w₀)` whose vertical power series has nonzero image in `(𝒪_{E, x₀} ⧸ 𝔪_{x₀})⟦X⟧` admits a
unique factorization `f = evalVertical x₀ w₀ P * u` into a distinguished polynomial `P` over
`𝒪_{E, x₀}` and a unit germ `u` at `(x₀, w₀)`.

```lean
TauCeti.holomorphicStructureSheaf.existsUnique_weierstrassPreparation {E : Type}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [FiniteDimensional ℂ E] {x₀ : E} {w₀ : ℂ}
  {f :
    ↑((TauCeti.holomorphicStructureSheaf (modelWithCornersSelf ℂ (E × ℂ)) (E × ℂ)).presheaf.stalk
        (x₀, w₀))}
  (hf :
    (PowerSeries.map
          (IsLocalRing.residue
            ↑((TauCeti.holomorphicStructureSheaf (modelWithCornersSelf ℂ E) E).presheaf.stalk x₀)))
        ((TauCeti.holomorphicStructureSheaf.verticalPowerSeries x₀ w₀) f) ≠
      0) :
  ∃! pu,
    pu.1.IsDistinguishedAt
        (IsLocalRing.maximalIdeal
          ↑((TauCeti.holomorphicStructureSheaf (modelWithCornersSelf ℂ E) E).presheaf.stalk x₀)) ∧
      IsUnit pu.2 ∧ f = (TauCeti.holomorphicStructureSheaf.evalVertical x₀ w₀) pu.1 * pu.2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Complex analytic Weierstrass preparation theorem](../../complex-manifolds-dolbeault-theory-and-kahler-ge/complex-analytic-weierstrass-preparation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.holomorphicStructureSheaf.existsUnique_weierstrassPreparation`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/StructureSheaf/Weierstrass.html#TauCeti.holomorphicStructureSheaf.existsUnique_weierstrassPreparation).

## Sources

- [Tau Ceti documentation: `TauCeti.holomorphicStructureSheaf.existsUnique_weierstrassPreparation`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/StructureSheaf/Weierstrass.html#TauCeti.holomorphicStructureSheaf.existsUnique_weierstrassPreparation)
- [Source of `TauCeti.holomorphicStructureSheaf.existsUnique_weierstrassPreparation` in TauCeti/Geometry/Manifold/Complex/StructureSheaf/Weierstrass.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Complex/StructureSheaf/Weierstrass.lean#L618)
