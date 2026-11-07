---
declaration: theorem
origin: cited
lean: TauCeti.nonempty_layerTateModule
statement: formalized
proof: formalized
---

# Existence of the Tate module of a finite layer

(NSW (5.6.5) and the proof of (7.4.1)). For
a finite Galois extension `L/K` of `p`-adic fields there is a finitely generated
`ℤ_p[Gal(L/K)]`-module of projective dimension at most one which is an extension of the
augmentation ideal by `A(L)`.

```lean
TauCeti.nonempty_layerTateModule.{u} (p : ℕ) [Fact (Nat.Prime p)] (K L : Type u) [Field L] [Field K]
  [Algebra K L] [Algebra ℚ_[p] L] [Module.Finite ℚ_[p] L] [Algebra ℚ_[p] K]
  [IsScalarTower ℚ_[p] K L] [IsGalois K L] : Nonempty (TauCeti.LayerTateModule p L K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dimension shifting in every positive degree](../../part-02/continuous-cohomology-of-profinite-groups/dimension-shifting-in-every-positive-degree.md)
- [The Kummer isomorphism](../../part-02/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [The local class formation](../../part-01/class-field-theory/the-local-class-formation.md)
- [The local invariant](../../part-01/class-field-theory/the-local-invariant.md)
- [Local reciprocity for `A(L)`](local-reciprocity-for-a-l.md)
- [The strict cohomological dimension through integral coefficients](../../part-02/continuous-cohomology-of-profinite-groups/the-strict-cohomological-dimension-through-integ.md)
- [Tate's theorem for a class formation](../../part-01/class-field-theory/tates-theorem-for-a-class-formation.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.nonempty_layerTateModule`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/MultiplicativeCompletion/LayerTateModule/Cohomology.html#TauCeti.nonempty_layerTateModule).

## Sources

- [Tau Ceti documentation: `TauCeti.nonempty_layerTateModule`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/MultiplicativeCompletion/LayerTateModule/Cohomology.html#TauCeti.nonempty_layerTateModule)
- [Source of `TauCeti.nonempty_layerTateModule` in TauCeti/NumberTheory/Padics/MultiplicativeCompletion/LayerTateModule/Cohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/MultiplicativeCompletion/LayerTateModule/Cohomology.lean#L90)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalGaloisGroups/STATUS.md)
