---
declaration: section
origin: cited
lean: Stacks.Cohomology.ProjectionFormulaSection.projectionFormula, Stacks.Cohomology.ProjectionFormulaSection.isIso_projectionFormulaNatTransSource, Stacks.Cohomology.ProjectionFormulaOnRingedTopoi.projectionFormulaMap, Stacks.Cohomology.ProjectionFormulaOnRingedTopoi.projectionFormulaMap_naturality_source, Stacks.Cohomology.ProjectionFormulaOnRingedTopoi.projectionFormulaMap_naturality_target, Stacks.Cohomology.ProjectionFormulaPerfectOnRingedTopoi.projectionFormulaTransformation, Stacks.Cohomology.ProjectionFormulaOfToposHom.isIso_projectionFormulaMap_of_isPerfect, Stacks.Cohomology.ProjectionFormulaOfToposHom.projectionFormulaMap_baseChange_square
statement: formalized
proof: formalized
---

# 21.50 Projection formula

Section 21.50 of the Stacks Project, [Tag 0943](https://stacks.math.columbia.edu/tag/0943). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0943, the section

[Tag 0943](https://stacks.math.columbia.edu/tag/0943) in the Stacks Project.

**`Stacks.Cohomology.ProjectionFormulaSection.projectionFormula`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ProjectionFormulaSection.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ProjectionFormulaSection.lean#L144). The attribute's comment: “the canonical map of Section 21.50, natural in the two complexes together”.

> **The canonical map of Section 21.50 of [Stacks, Tag 0943]**, as a morphism of bifunctors on
> `D(𝒪_𝒞) × D(𝒪_𝒟)`:
>
> `Rf_*E ⊗^𝐋_{𝒪_𝒟} K ⟶ Rf_*(E ⊗^𝐋_{𝒪_𝒞} Lf^*K)`,
>
> natural in `E` and `K` together.  Its value at a pair is the map of [Stacks, Tag 0B56], the
> adjoint for `Lf^* ⊣ Rf_*` of the comparison `Lf^*(Rf_*E ⊗^𝐋 K) ≅ Lf^*Rf_*E ⊗^𝐋 Lf^*K` of
> [Stacks, Tag 07A4] followed by the counit `Lf^*Rf_*E ⟶ E` in the first factor.  There is no
> hypothesis on `f`, `E` or `K`: the section stresses that the map exists for every morphism of
> ringed topoi, and the joint naturality is the naturality of the adjoint-transpose construction
> the map instantiates.

```lean
def projectionFormula : pushforwardTensor f ⟶ tensorPullbackPushforward f
```

**`Stacks.Cohomology.ProjectionFormulaSection.isIso_projectionFormulaNatTransSource`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ProjectionFormulaSection.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ProjectionFormulaSection.lean#L205). The attribute's comment: “the lemma of Section 21.50: at a perfect complex the canonical map is invertible, here as an isomorphism of the two functors of the complex on the source”.

> **The lemma of Section 21.50 of [Stacks, Tag 0943]**, as an isomorphism of functors.  Let
> `f : (Sh(𝒞), 𝒪_𝒞) ⟶ (Sh(𝒟), 𝒪_𝒟)` be a morphism of ringed topoi and let `K ∈ D(𝒪_𝒟)` be
> perfect.  Then the canonical map of the section is invertible as a natural transformation of
> functors of the complex on the source:
>
> `Rf_*(-) ⊗^𝐋_{𝒪_𝒟} K ≅ Rf_*(- ⊗^𝐋_{𝒪_𝒞} Lf^*K)` on `D(𝒪_𝒞) ⥤ D(𝒪_𝒟)`.
>
> A natural transformation is invertible as soon as each of its components is, and each component
> is [Stacks, Tag 0944].

```lean
theorem isIso_projectionFormulaNatTransSource
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)))
    (hK : RingedSite.IsPerfect Y.toRingedSite K) :
    IsIso (projectionFormulaNatTransSource f K)
```

## Tag 0B56, an equation

[Tag 0B56](https://stacks.math.columbia.edu/tag/0B56) in the Stacks Project.

**`Stacks.Cohomology.ProjectionFormulaOnRingedTopoi.projectionFormulaMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ProjectionFormula.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ProjectionFormula.lean#L259). The attribute's comment: “the map”.

> **Equation 21.50.0.1 of [Stacks, Tag 0B56].**  For a morphism of ringed topoi
> `f : (Sh(C), O_C) ⟶ (Sh(D), O_D)`, `E ∈ D(O_C)` and `K ∈ D(O_D)`, the canonical map
>
> `Rf_*E ⊗^L_{O_D} K ⟶ Rf_*(E ⊗^L_{O_C} Lf^*K)`,
>
> with no further hypothesis.  It is the map adjoint, for the adjunction `Lf^* ⊣ Rf_*` of
> [Stacks, Tag 07A6], to the bifunctorial identification
> `Lf^*(Rf_*E ⊗^L K) ≅ Lf^*Rf_*E ⊗^L Lf^*K` of [Stacks, Tag 07A4] followed by the counit
> `Lf^*Rf_*E ⟶ E` in the first factor.

```lean
def projectionFormulaMap (hmos : f.u.IsMorphismOfSites Y.J X.J)
    (E : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))) :
    ((derivedTensorProductFunctor Y.O).obj ((derivedPushforward f).obj E)).obj K ⟶
      (derivedPushforward f).obj
        (((derivedTensorProductFunctor X.O).obj E).obj ((derivedPullback f).obj K))
```

**`Stacks.Cohomology.ProjectionFormulaOnRingedTopoi.projectionFormulaMap_naturality_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ProjectionFormula.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ProjectionFormula.lean#L286). The attribute's comment: “naturality in the source complex”.

> **Naturality of Equation 21.50.0.1 in the complex on the source**, `E ∈ D(O_C)`.

```lean
theorem projectionFormulaMap_naturality_source
    {E E' : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))} (φ : E ⟶ E')
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))) :
    ((derivedTensorProductFunctor Y.O).map ((derivedPushforward f).map φ)).app K ≫
        projectionFormulaMap f hmos E' K =
      projectionFormulaMap f hmos E K ≫
        (derivedPushforward f).map
          (((derivedTensorProductFunctor X.O).map φ).app ((derivedPullback f).obj K))
```

**`Stacks.Cohomology.ProjectionFormulaOnRingedTopoi.projectionFormulaMap_naturality_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ProjectionFormula.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ProjectionFormula.lean#L298). The attribute's comment: “naturality in the target complex”.

> **Naturality of Equation 21.50.0.1 in the complex on the target**, `K ∈ D(O_D)`.

```lean
theorem projectionFormulaMap_naturality_target
    (E : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    {K K' : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))} (k : K ⟶ K') :
    ((derivedTensorProductFunctor Y.O).obj ((derivedPushforward f).obj E)).map k ≫
        projectionFormulaMap f hmos E K' =
      projectionFormulaMap f hmos E K ≫
        (derivedPushforward f).map
          (((derivedTensorProductFunctor X.O).obj E).map ((derivedPullback f).map k))
```

**`Stacks.Cohomology.ProjectionFormulaPerfectOnRingedTopoi.projectionFormulaTransformation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ProjectionFormulaStrictlyPerfect.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ProjectionFormulaStrictlyPerfect.lean#L155). The attribute's comment: “the map as a natural transformation in the target complex”.

> **Equation 21.50.0.1 of [Stacks, Tag 0B56] as a natural transformation** of functors of the
> complex on the base.  Its component at `K` is
> `Stacks.Cohomology.ProjectionFormulaOnRingedTopoi.projectionFormulaMap f hmos E K`, and its
> naturality is `projectionFormulaMap_naturality_target`.

```lean
def projectionFormulaTransformation :
    projectionFormulaSource f E ⟶ projectionFormulaTarget f E
```

## Tag 0944, a lemma

[Tag 0944](https://stacks.math.columbia.edu/tag/0944) in the Stacks Project.

**`Stacks.Cohomology.ProjectionFormulaOfToposHom.isIso_projectionFormulaMap_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ProjectionFormulaPerfectOfToposHom.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ProjectionFormulaPerfectOfToposHom.lean#L122).

> **[Stacks, Tag 0944], the projection formula for a perfect complex.** Let
> `f : (Sh(𝒞), 𝒪_𝒞) ⟶ (Sh(𝒟), 𝒪_𝒟)` be a morphism of ringed topoi, `E ∈ D(𝒪_𝒞)` and
> `K ∈ D(𝒪_𝒟)`. If `K` is perfect, then the canonical map of [Stacks, Tag 0B56]
> `Rf_*E ⊗^𝐋_{𝒪_𝒟} K ⟶ Rf_*(E ⊗^𝐋_{𝒪_𝒞} Lf^*K)` is an isomorphism.

```lean
theorem isIso_projectionFormulaMap_of_isPerfect {X Y : RingedTopos.{u, u, u}}
    (f : RingedToposHom X Y)
    (E : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)))
    (hK : RingedSite.IsPerfect Y.toRingedSite K) :
    IsIso (projectionFormulaMap f E K)
```

## Tag 0E48, a remark

[Tag 0E48](https://stacks.math.columbia.edu/tag/0E48) in the Stacks Project.

**`Stacks.Cohomology.ProjectionFormulaOfToposHom.projectionFormulaMap_baseChange_square`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ProjectionFormulaBaseChange.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ProjectionFormulaBaseChange.lean#L108).

> **[Stacks, Tag 0E48].**  For a commutative square of morphisms of ringed topoi
>
> ```
>              g'
>   (Sh(C'), 𝒪_{C'}) --→ (Sh(C), 𝒪_C)
>       |  f'                |  f
>       v                    v
>   (Sh(D'), 𝒪_{D'}) --→ (Sh(D), 𝒪_D)
>              g
> ```
>
> and `E` in `D(𝒪_C)`, `K` in `D(𝒪_D)`, the map `p` of Equation 21.50.0.1 is compatible with the
> base change map `b` of [Stacks, Tag 07A7]: going down the left (`t`, the comparison of
> [Stacks, Tag 07A4] for `g`, then `b ⊗ 1`, then `p` for `f'`) equals going down the right (`Lg^*`
> of `p` for `f`, then `b`, then `R(f')_*` of `t` for `g'` followed by `1 ⊗ c`, where
> `c : L(g')^*Lf^*K ⟶ L(f')^*Lg^*K` identifies the two iterated pullbacks around the square), as
> maps `Lg^*(Rf_*E ⊗^L K) ⟶ R(f')_*(L(g')^*E ⊗^L L(f')^*Lg^*K)` in `D(𝒪_{D'})`.

```lean
theorem projectionFormulaMap_baseChange_square (h : g.comp f' = f.comp g')
    (E : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))) :
    (derivedPullbackTensorIso g).hom.app ((derivedPushforward f).obj E, K) ≫
        (Functor.uncurry.obj (derivedTensorProductFunctor Y'.O)).map
            (derivedBaseChangeMap f g' f' g h E ×ₘ 𝟙 ((derivedPullback g).obj K)) ≫
          adjunctionTensorMap (derivedAdjunction f')
            (Functor.uncurry.obj (derivedTensorProductFunctor Y'.O))
            (Functor.uncurry.obj (derivedTensorProductFunctor X'.O))
            (derivedPullbackTensorIso f').hom
            ((derivedPullback g').obj E) ((derivedPullback g).obj K) =
      (derivedPullback g).map
          (adjunctionTensorMap (derivedAdjunction f)
            (Functor.uncurry.obj (derivedTensorProductFunctor Y.O))
            (Functor.uncurry.obj (derivedTensorProductFunctor X.O))
            (derivedPullbackTensorIso f).hom E K) ≫
        derivedBaseChangeMap f g' f' g h
            (((derivedTensorProductFunctor X.O).obj E).obj ((derivedPullback f).obj K)) ≫
          (derivedPushforward f').map
            ((derivedPullbackTensorIso g').hom.app (E, (derivedPullback f).obj K) ≫
              (Functor.uncurry.obj (derivedTensorProductFunctor X'.O)).map
                (𝟙 ((derivedPullback g').obj E) ×ₘ
                  (Stacks.AffineProjectionFormula.squareCompositeIso
                    (derivedPullbackCompIsoLeft f' g)
                    (derivedPullbackCompIsoRight f g' f' g h)).inv.app K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.50, Tag 0943](https://stacks.math.columbia.edu/tag/0943)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
