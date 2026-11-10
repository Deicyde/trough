---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialSiteSituation.nonempty_simplicialModuleResolution, CategoryTheory.SimplicialSiteSituation.SimplicialModuleResolution.sectionsComplex, CategoryTheory.SimplicialSiteSituation.SimplicialModuleResolution.sectionsComplex_exactAt_le_one, CategoryTheory.SimplicialSiteSituation.SimplicialModuleResolution.sectionsComplex_acyclic, CategoryTheory.SimplicialSiteSituation.SimplicialModuleResolution.exists_sectionsSpectralSequence, CategoryTheory.SimplicialSiteSituation.componentModuleCohomologyIso, CategoryTheory.SimplicialSiteSituation.componentModuleCohomologyObjIso
statement: formalized
proof: formalized
---

# 85.10 Cohomology on ringed simplicial sites

Section 85.10 of the Stacks Project, [Tag 0D7B](https://stacks.math.columbia.edu/tag/0D7B). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D9B, a lemma

[Tag 0D9B](https://stacks.math.columbia.edu/tag/0D9B) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.nonempty_simplicialModuleResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleResolution.lean, line 1529](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleResolution.lean#L1529).

> **Stacks 0D9B.** There is a complex of modules over the structure sheaf of the total
> simplicial site whose term in degree `n` is the lower-shriek image `g_{n!}𝒪_n` of the `n`-th
> component structure sheaf, whose differentials are the canonical alternating face maps, and
> which is a resolution of the structure sheaf.

```lean
public theorem nonempty_simplicialModuleResolution (S : SimplicialSiteSituation.{u})
    (O : Sheaf S.totalTopology RingCat.{u}) :
    Nonempty (SimplicialModuleResolutionActual S O)
```

## Tag 0D9C, a lemma

[Tag 0D9C](https://stacks.math.columbia.edu/tag/0D9C) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.SimplicialModuleResolution.sectionsComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/SectionsComplex.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/SectionsComplex.lean#L207). The attribute's comment: “the complex”.

> **Stacks 0D9C.** The canonical complex
>
> `0 → Γ(C_total, F) → Γ(C_0, F_0) → Γ(C_1, F_1) → …`
>
> obtained by applying `Hom(-, F)` to the resolution `… → g_{1!} O_1 → g_{0!} O_0 → O`. Its term in
> index `0` is `Hom(O, F) = Γ(C_total, F)` and its term in index `n + 1` is `Γ(C_n, F_n)`.

```lean
public def sectionsComplex : CochainComplex AddCommGrpCat.{u} ℕ
```

**`CategoryTheory.SimplicialSiteSituation.SimplicialModuleResolution.sectionsComplex_exactAt_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/SectionsComplex.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/SectionsComplex.lean#L304). The attribute's comment: “exactness in degrees -1 and 0”.

> **Stacks 0D9C.** The complex `0 → Γ(C_total, F) → Γ(C_0, F_0) → …` is exact in degrees `-1`
> and `0`, i.e. in indices `0` and `1`, for every sheaf of `O`-modules `F`.

```lean
public theorem sectionsComplex_exactAt_le_one (i : ℕ) (hi : i ≤ 1) :
    (D.sectionsComplex F).ExactAt i
```

**`CategoryTheory.SimplicialSiteSituation.SimplicialModuleResolution.sectionsComplex_acyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/SectionsComplex.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/SectionsComplex.lean#L313). The attribute's comment: “exactness in all degrees for an injective module”.

> **Stacks 0D9C.** The complex `0 → Γ(C_total, F) → Γ(C_0, F_0) → …` is exact in every degree
> when `F` is an injective `O`-module.

```lean
public theorem sectionsComplex_acyclic [Injective F] : (D.sectionsComplex F).Acyclic
```

## Tag 0D7E, a lemma

[Tag 0D7E](https://stacks.math.columbia.edu/tag/0D7E) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.SimplicialModuleResolution.exists_sectionsSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleCohomologySpectralSequence.lean, line 688](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleCohomologySpectralSequence.lean#L688).

> **Stacks 0D7E.** In Situation 09WE let `O` be a sheaf of rings on the total site. For `K` in
> `D⁺(O)` there is a spectral sequence `(E_r, d_r)`, functorial in `K` and presented from its first
> page, with
>
> `E_1^{p,q} = H^q(C_p, K_p),  d_1^{p,q} : E_1^{p,q} → E_1^{p+1,q}`
>
> converging to `H^{p+q}(C_total, K)`. Here `K_p = g_p^* K` is the restriction of `K` to the
> component `C_p` (Stacks 0D72), `H^q(C_p, -)` is the cohomology of `RΓ(C_p, -)` on `D⁺(O_p)` and
> `H^n(C_total, -)` that of `RΓ(C_total, -)` on `D⁺(O)`, global sections of a sheaf of modules
> being those of its underlying abelian sheaf. The identification of the first page is natural in
> `K`, and the first page vanishes in the negative columns.

```lean
public theorem exists_sectionsSpectralSequence :
    ∃ E : DerivedCategory.Plus (SheafOfModules.{u} O) ⥤
        CohomologicalSpectralSequence AddCommGrpCat.{u} 1,
      (∀ (p : ℕ) (q : ℤ), Nonempty (E ⋙
          CategoryTheory.SpectralSequence.pageFunctor AddCommGrpCat.{u} _ 1 1 le_rfl ⋙
            HomologicalComplex.eval AddCommGrpCat.{u} _ ((p : ℤ), q) ≅
        (componentModuleRestriction S O ⦋p⦌).mapDerivedCategoryPlus ⋙
          (SheafOfModules.toSheaf (componentRingSheaf S O ⦋p⦌) ⋙
            Sheaf.Γ (S.componentTopology ⦋p⦌) AddCommGrpCat.{u}).rightDerivedFunctorPlus ⋙
            DerivedCategory.Plus.homologyFunctor AddCommGrpCat.{u} q)) ∧
      (∀ (K : DerivedCategory.Plus (SheafOfModules.{u} O)) (p q : ℤ), p < 0 →
        IsZero (((E.obj K).page 1 le_rfl).X (p, q))) ∧
      ∀ K : DerivedCategory.Plus (SheafOfModules.{u} O),
        CategoryTheory.SpectralSequence.AbutsTo (E.obj K)
          (fun n => (DerivedCategory.Plus.homologyFunctor AddCommGrpCat.{u} n).obj
            ((SheafOfModules.toSheaf O ⋙
              Sheaf.Γ S.totalTopology AddCommGrpCat.{u}).rightDerivedFunctorPlus.obj K))
```

## Tag 0DH2, a lemma

[Tag 0DH2](https://stacks.math.columbia.edu/tag/0DH2) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.componentModuleCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleCohomology.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleCohomology.lean#L104).

> In the situation of Stacks 09WE let `O` be a sheaf of rings on the total site, let `U` be
> an object of the degree-`n` component and let `p : ℕ`. For a sheaf of `O`-modules `F` one has
> `H^p(U, g_n^*F) ≅ H^p(U, F)`, where on the right-hand side `U` is viewed as an object of the
> total category; the isomorphism is natural in `F`.

```lean
noncomputable def componentModuleCohomologyIso (U : S.component n) (p : ℕ) :
    componentModuleRestriction S O n ⋙ SheafOfModules.toSheaf.{u} (componentRingSheaf S O n) ⋙
        cohomology (S.componentTopology n) U p ≅
      SheafOfModules.toSheaf.{u} O ⋙
        cohomology S.totalTopology ((componentFunctor S n).obj U) p
```

**`CategoryTheory.SimplicialSiteSituation.componentModuleCohomologyObjIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleCohomology.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleCohomology.lean#L125).

> **`H^p(U, g_n^*F) ≅ H^p(U, F)` at a single sheaf of modules.** For `F` a sheaf of
> `O`-modules on the total site of a simplicial-site situation and `U` an object of the degree-`n`
> component, `H^p(U, g_n^*F) ≅ H^p(U, F)` with `U` viewed on the right-hand side as an object of
> the total category.

```lean
noncomputable def componentModuleCohomologyObjIso (F : SheafOfModules.{u} O)
    (U : S.component n) (p : ℕ) :
    (cohomology (S.componentTopology n) U p).obj
        ((SheafOfModules.toSheaf.{u} (componentRingSheaf S O n)).obj
          ((componentModuleRestriction S O n).obj F)) ≅
      (cohomology S.totalTopology ((componentFunctor S n).obj U) p).obj
        ((SheafOfModules.toSheaf.{u} O).obj F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.10, Tag 0D7B](https://stacks.math.columbia.edu/tag/0D7B)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
