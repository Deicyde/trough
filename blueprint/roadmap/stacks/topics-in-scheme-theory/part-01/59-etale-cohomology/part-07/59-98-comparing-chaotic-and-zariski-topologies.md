---
declaration: section
origin: cited
lean: AlgebraicGeometry.SmallAffineZariski.essImage_iff_isZero_derivedSections_and_isCSquareIso
statement: formalized
proof: formalized
---

# 59.98 Comparing chaotic and Zariski topologies

Section 59.98 of the Stacks Project, [Tag 0F1K](https://stacks.math.columbia.edu/tag/0F1K). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F1L, a lemma

[Tag 0F1L](https://stacks.math.columbia.edu/tag/0F1L) in the Stacks Project.

**`AlgebraicGeometry.SmallAffineZariski.essImage_iff_isZero_derivedSections_and_isCSquareIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/ChaoticComparison.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/ChaoticComparison.lean#L207).

> **Stacks 0F1L.** Let `𝒪` be a sheaf of rings for the Zariski topology on the affine opens of a
> scheme `S` and let `ε` be the comparison from the Zariski topology to the chaotic topology, in
> which every presheaf is a sheaf. A bounded-below object `K` of `D(𝒪_chaotic)` lies in the
> essential image of the derived direct image `Rε_*` if and only if the derived sections of `K` over
> every empty affine open vanish and the canonical map `c^K_{U,V,W,V ∩ W}` of Stacks 0F16 is an
> isomorphism for every square exhibiting an affine open `U` as the union of two standard opens `V`
> and `W` with intersection `V ∩ W`.

```lean
theorem essImage_iff_isZero_derivedSections_and_isCSquareIso
    (K : DerivedCategory (SheafOfModules.{u + 1}
      (Stacks.SheafOfModules.Tensor.ringSheaf (trivialRingedSite B S hS O).O)))
    (hK : (DerivedCategory.TStructure.t
      (C := SheafOfModules.{u + 1}
        (Stacks.SheafOfModules.Tensor.ringSheaf (trivialRingedSite B S hS O).O))).plus K) :
    Rε.essImage K ↔
      ((∀ (sq : Square (SmallAffineZariski B S hS)) (U : SmallAffineZariski B S hS),
          IsEmpty ((toScheme B S hS).obj U) →
            IsZero (((Stacks.MayerVietoris.CanonicalMapOfComplexes.derivedCSquareData.{u + 1,
              u + 1} (R := (Stacks.SheafOfModules.Tensor.ringSheaf (trivialRingedSite B S hS O).O))
              sq).derivedSections U).obj K)) ∧
        ∀ sq : Square (SmallAffineZariski B S hS), IsStandardOpenCoverSquare B S hS sq →
          (Stacks.MayerVietoris.CanonicalMapOfComplexes.derivedCSquareData.{u + 1, u + 1}
            (R := (Stacks.SheafOfModules.Tensor.ringSheaf (trivialRingedSite B S hS O).O))
            sq).IsCSquareIso K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.98, Tag 0F1K](https://stacks.math.columbia.edu/tag/0F1K)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
