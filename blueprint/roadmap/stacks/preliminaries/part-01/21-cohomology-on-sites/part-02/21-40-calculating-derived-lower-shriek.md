---
declaration: section
origin: cited
lean: Stacks.Sites.FibredCategory.fiberHomologyPresheafFunctor, Stacks.Sites.FibredCategory.fiberHomologyPresheaf_obj, Stacks.Sites.FibredCategory.fiberHomologyPresheaf_map, Stacks.Sites.FibredCategory.fiberHomologyPresheafFunctor_map_app, Stacks.Sites.FibredCategory.fiberHomologySheaf, Stacks.Sites.FibredCategory.fiberHomologySheaf_sheafify, Stacks.Sites.FibredCategory.fiberHomologySheafSheafifyIso, Stacks.Sites.FibredCategory.FibredCategorySituation.derivedLowerShriekHomologyIsoFiberHomology
statement: formalized
proof: formalized
---

# 21.40 Calculating derived lower shriek

Section 21.40 of the Stacks Project, [Tag 08P7](https://stacks.math.columbia.edu/tag/08P7). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08PI, a lemma

[Tag 08PI](https://stacks.math.columbia.edu/tag/08PI) in the Stacks Project.

**`Stacks.Sites.FibredCategory.fiberHomologyPresheafFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/FibreHomologyPresheaf.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/FibreHomologyPresheaf.lean#L124). The attribute's comment: “the presheaf of fibre homology”.

> **The presheaf of fibre homology.** The presheaf `L_{n,p}(F)` on the base whose value at `V` is
> the homology `H_n(C_V, F|_{C_V})` of the fibre at `V`, with restriction maps given by the chosen
> pullback functors and restriction of `F` along the chosen cartesian lifts, and regarded as a
> functor of the coefficient presheaf `F`.

```lean
def fiberHomologyPresheafFunctor (n : ℕ) :
    (s.Cᵒᵖ ⥤ AddCommGrpCat.{max w uD vD uC}) ⥤
      (s.base.Cᵒᵖ ⥤ AddCommGrpCat.{max w uD vD uC})
```

**`Stacks.Sites.FibredCategory.fiberHomologyPresheaf_obj`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/FibreHomologyPresheaf.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/FibreHomologyPresheaf.lean#L196). The attribute's comment: “the values of the presheaf of fibre homology”.

> **The values of the presheaf of fibre homology.** Its value at `V` is the homology
> `H_n(C_V, F|_{C_V})` of the fibre at `V`.

```lean
lemma fiberHomologyPresheaf_obj (F : s.Cᵒᵖ ⥤ AddCommGrpCat.{max w uD vD uC}) (n : ℕ)
    (V : s.base.Cᵒᵖ) :
    (fiberHomologyPresheaf s F n).obj V =
      CategoryHomology.categoryHomology.{uC, max w uD vD uC}
        ((Functor.Fiber.fiberInclusion (p := s.p) (S := V.unop)).op ⋙ F) n
```

**`Stacks.Sites.FibredCategory.fiberHomologyPresheaf_map`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/FibreHomologyPresheaf.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/FibreHomologyPresheaf.lean#L207). The attribute's comment: “the restriction maps of the presheaf of fibre homology”.

> **The restriction maps of the presheaf of fibre homology.** The restriction map along
> `h : V' ⟶ V` is the map on homology of Stacks 08PH attached to the chosen pullback functor `h^*`
> and to restriction of `F` along the chosen cartesian lifts of `h`.

```lean
lemma fiberHomologyPresheaf_map (F : s.Cᵒᵖ ⥤ AddCommGrpCat.{max w uD vD uC}) (n : ℕ)
    {V V' : s.base.C} (h : V' ⟶ V) :
    (fiberHomologyPresheaf s F n).map h.op =
      CategoryHomology.categoryHomologyMap.{uC, uC, max w uD vD uC}
        ((Functor.chosenPullbacks s.p).pullbackFunctor h) (fiberCartesianRestriction s F h) n
```

**`Stacks.Sites.FibredCategory.fiberHomologyPresheafFunctor_map_app`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/FibreHomologyPresheaf.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/FibreHomologyPresheaf.lean#L218). The attribute's comment: “functoriality of the presheaf of fibre homology in the coefficients”.

> **Functoriality of the presheaf of fibre homology in the coefficients.** The map induced by
> `α : F ⟶ G` is the map on homology of Stacks 08PH attached to the identity functor of the fibre and
> to `α` restricted to it.

```lean
lemma fiberHomologyPresheafFunctor_map_app {F G : s.Cᵒᵖ ⥤ AddCommGrpCat.{max w uD vD uC}}
    (α : F ⟶ G) (n : ℕ) (V : s.base.Cᵒᵖ) :
    ((fiberHomologyPresheafFunctor s n).map α).app V =
      CategoryHomology.categoryHomologyMap.{uC, uC, max w uD vD uC} (𝟭 (s.p.Fiber V.unop))
        (Functor.whiskerLeft (Functor.Fiber.fiberInclusion (p := s.p) (S := V.unop)).op α) n
```

**`Stacks.Sites.FibredCategory.fiberHomologySheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/FibreHomologyPresheaf.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/FibreHomologyPresheaf.lean#L228). The attribute's comment: “the sheaf of fibre homology”.

> **The sheaf `L_n(F)` of fibre homology.** The abelian sheaf on the base associated to the
> presheaf of fibre homology.

```lean
abbrev fiberHomologySheaf [HasWeakSheafify s.base.J AddCommGrpCat.{max w uD vD uC}]
    (F : s.Cᵒᵖ ⥤ AddCommGrpCat.{max w uD vD uC}) (n : ℕ) :
    Sheaf s.base.J AddCommGrpCat.{max w uD vD uC}
```

**`Stacks.Sites.FibredCategory.fiberHomologySheaf_sheafify`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/FibreHomologySheafification.lean, line 1245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/FibreHomologySheafification.lean#L1245).

> Sheafifying the coefficients on the total category does not change the
> associated sheaf of fibre homology.

```lean
theorem fiberHomologySheaf_sheafify
    [HasWeakSheafify s.base.J AddCommGrpCat.{max w uD vD uC}]
    [HasWeakSheafify s.topology AddCommGrpCat.{max w uD vD uC}]
    (F : s.Cᵒᵖ ⥤ AddCommGrpCat.{max w uD vD uC}) (n : ℕ) :
    IsIso ((presheafToSheaf s.base.J AddCommGrpCat.{max w uD vD uC}).map
      ((fiberHomologyPresheafFunctor s n).map
        ((sheafificationAdjunction s.topology AddCommGrpCat.{max w uD vD uC}).unit.app F)))
```

**`Stacks.Sites.FibredCategory.fiberHomologySheafSheafifyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/FibreHomologySheafification.lean, line 1290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/FibreHomologySheafification.lean#L1290). The attribute's comment: “the sheaf of fibre homology is unchanged by sheafifying the coefficients”.

> **Stacks 08PI.** The sheaf `L_n(F)` of fibre homology is unchanged when the coefficient
> presheaf is replaced by its sheafification on the total category: the canonical map
> `L_n(F) ⟶ L_n(F^#)` of `fiberHomologySheaf_sheafify` is an isomorphism.

```lean
def fiberHomologySheafSheafifyIso
    [HasWeakSheafify s.base.J AddCommGrpCat.{max w uD vD uC}]
    [HasWeakSheafify s.topology AddCommGrpCat.{max w uD vD uC}]
    (F : s.Cᵒᵖ ⥤ AddCommGrpCat.{max w uD vD uC}) (n : ℕ) :
    fiberHomologySheaf s F n ≅
      fiberHomologySheaf s
        ((sheafToPresheaf s.topology AddCommGrpCat.{max w uD vD uC}).obj
          ((presheafToSheaf s.topology AddCommGrpCat.{max w uD vD uC}).obj F)) n
```

## Tag 08PJ, a lemma

[Tag 08PJ](https://stacks.math.columbia.edu/tag/08PJ) in the Stacks Project.

**`Stacks.Sites.FibredCategory.FibredCategorySituation.derivedLowerShriekHomologyIsoFiberHomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/UliftFreeCoverGenerators.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/UliftFreeCoverGenerators.lean#L356).

> **Stacks 08PJ.** Let `p : C ⥤ D` be a fibred category over a ringed site `D`, with `C` carrying
> the inherited topology and `π` the induced morphism of topoi (Stacks 08P8). For every `n ≥ 0`,
> the functor `F ↦ L_n π_!(F) = H^{-n}(Lπ_! F)` on abelian sheaves on `C` is the functor
> `F ↦ L_n(F)` of Stacks 08PI, the sheaf on `D` associated to the presheaf
> `V ↦ H_n(C_V, F|_{C_V})`, naturally in `F`.
>
> Here `Lπ_!` is the left derived functor whose existence is Stacks 07AC
> (`hasPointwiseLeftDerivedFunctor_abelianLowerShriekOnHomotopy`), and the two acyclicity inputs of
> the comparison `derivedLowerShriekHomologyIso` are proved for every fibred situation:
> `abelianLowerShriekAcyclic` and `abelianLowerShriekGeneratorsAcyclic`.

```lean
def derivedLowerShriekHomologyIsoFiberHomology (n : ℕ) :
    s.derivedAbelianLowerShriekHomology n ≅
      sheafToPresheaf s.topology AddCommGrpCat.{max w uD vD uC} ⋙
        fiberHomologyPresheafFunctor s n ⋙
          presheafToSheaf s.base.J AddCommGrpCat.{max w uD vD uC}
```

## Tag 08PK, a lemma

[Tag 08PK](https://stacks.math.columbia.edu/tag/08PK) in the Stacks Project.

**`Stacks.Sites.FibredCategory.MorphismSituation.derivedAbelianLowerShriekHomologyObjIsoFiberHomologySheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/DerivedLowerShriekMorphismFibreHomology.lean, line 574](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/DerivedLowerShriekMorphismFibreHomology.lean#L574). The attribute's comment: “L_n g_!(F') is the sheaf of H_n(I_U, F'_U); assumes 07AC and cover acyclicity”.

> For an abelian sheaf `F'` on the source, `L_n g_!(F')` is the sheaf on the total category
> associated to the presheaf `U ↦ H_n(I_U, F'_U)`. This takes as hypotheses the acyclicity
> conditions `h` for `g_!` and `h''` for `g''_!` and the cover acyclicity `hcov` of the
> amelioration.

```lean
def derivedAbelianLowerShriekHomologyObjIsoFiberHomologySheaf
    (h : S.AbelianLowerShriekAcyclic)
    (h'' : (amelioratedSituation S).AbelianLowerShriekAcyclic)
    (hcov : (amelioratedSituation S).UliftFreeCoverLowerShriekAcyclic) (n : ℕ)
    (F' : Sheaf S.sourceTopology AddCommGrpCat.{max w u₀ u₁ u₂ v₀ v₁ v₂}) :
    (S.derivedAbelianLowerShriekHomology n).obj F' ≅
      fiberHomologySheaf (amelioratedSituation S)
        ((amelioratedLowerShriek S).obj F').obj n
```

**`Stacks.Sites.FibredCategory.MorphismSituation.derivedAbelianLowerShriekHomologyObjIsoFiberHomologySheaf_unconditional`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/DerivedLowerShriekMorphismFibreHomologyUnconditional.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/DerivedLowerShriekMorphismFibreHomologyUnconditional.lean#L121). The attribute's comment: “L_n g_!(F') is the sheaf of H_n(I_U, F'_U)”.

> For an abelian sheaf `F'` on the source, `L_n g_!(F')` is the sheaf on the total category
> associated to the presheaf `U ↦ H_n(I_U, F'_U)`, where `I_U` is the fibre over `U` of the
> amelioration of `u`.

```lean
def derivedAbelianLowerShriekHomologyObjIsoFiberHomologySheaf_unconditional (n : ℕ)
    (F' : Sheaf S.sourceTopology AddCommGrpCat.{max w u₀ u₁ u₂ v₀ v₁ v₂}) :
    (S.derivedAbelianLowerShriekHomology n).obj F' ≅
      fiberHomologySheaf (amelioratedSituation S)
        ((amelioratedLowerShriek S).obj F').obj n
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.40, Tag 08P7](https://stacks.math.columbia.edu/tag/08P7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
