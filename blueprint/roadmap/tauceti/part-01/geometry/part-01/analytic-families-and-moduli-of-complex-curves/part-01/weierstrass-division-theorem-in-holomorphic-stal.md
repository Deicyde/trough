---
declaration: theorem
origin: cited
lean: TauCeti.holomorphicStructureSheaf.existsUnique_weierstrassDivision
statement: formalized
proof: formalized
---

# Weierstrass division theorem in holomorphic stalks

Given germs `f` and `g` at `(x₀, w₀)`
such that the vertical power series of `f` has nonzero image in `(𝒪_{E, x₀} ⧸ 𝔪_{x₀})⟦X⟧`, there
exist unique `q ∈ 𝒪_{E × ℂ, (x₀, w₀)}` and `r ∈ (𝒪_{E, x₀})[X]` forming a Weierstrass division of
`g` by `f`.

```lean
TauCeti.holomorphicStructureSheaf.existsUnique_weierstrassDivision {E : Type} [NormedAddCommGroup E]
  [NormedSpace ℂ E] [FiniteDimensional ℂ E] {x₀ : E} {w₀ : ℂ}
  {f :
    ↑((TauCeti.holomorphicStructureSheaf (modelWithCornersSelf ℂ (E × ℂ)) (E × ℂ)).presheaf.stalk
        (x₀, w₀))}
  (hf :
    (PowerSeries.map
          (IsLocalRing.residue
            ↑((TauCeti.holomorphicStructureSheaf (modelWithCornersSelf ℂ E) E).presheaf.stalk x₀)))
        ((TauCeti.holomorphicStructureSheaf.verticalPowerSeries x₀ w₀) f) ≠
      0)
  (g :
    ↑((TauCeti.holomorphicStructureSheaf (modelWithCornersSelf ℂ (E × ℂ)) (E × ℂ)).presheaf.stalk
        (x₀, w₀))) :
  ∃! qr,
    ((TauCeti.holomorphicStructureSheaf.verticalPowerSeries x₀ w₀) g).IsWeierstrassDivision
      ((TauCeti.holomorphicStructureSheaf.verticalPowerSeries x₀ w₀) f)
      ((TauCeti.holomorphicStructureSheaf.verticalPowerSeries x₀ w₀) qr.1) qr.2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Osgood's lemma](../../complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)
- [Weierstrass preparation theorem in holomorphic stalks](../part-02/weierstrass-preparation-theorem-in-holomorphic-s.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.holomorphicStructureSheaf.existsUnique_weierstrassDivision`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/StructureSheaf/Weierstrass.html#TauCeti.holomorphicStructureSheaf.existsUnique_weierstrassDivision).

## Sources

- [Tau Ceti documentation: `TauCeti.holomorphicStructureSheaf.existsUnique_weierstrassDivision`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/StructureSheaf/Weierstrass.html#TauCeti.holomorphicStructureSheaf.existsUnique_weierstrassDivision)
- [Source of `TauCeti.holomorphicStructureSheaf.existsUnique_weierstrassDivision` in TauCeti/Geometry/Manifold/Complex/StructureSheaf/Weierstrass.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Complex/StructureSheaf/Weierstrass.lean#L687)
