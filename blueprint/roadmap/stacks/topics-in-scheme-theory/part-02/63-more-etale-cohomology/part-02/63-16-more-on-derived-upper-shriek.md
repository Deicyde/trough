---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.derivedUpperShriek_homology_affineEtale, Stacks.EtaleCohomology.affineEtaleSheafifiedHomIso, Stacks.EtaleCohomology.affineEtaleSheafifiedHomIsoOfToBase, Stacks.EtaleCohomology.derivedUpperShriekHomologyAffineEtale
statement: formalized
proof: formalized
---

# 63.16 More on derived upper shriek

Section 63.16 of the Stacks Project, [Tag 0GLJ](https://stacks.math.columbia.edu/tag/0GLJ). 1 tag here is carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GLK, a lemma

[Tag 0GLK](https://stacks.math.columbia.edu/tag/0GLK) in the Stacks Project.

**`Stacks.EtaleCohomology.derivedUpperShriek_homology_affineEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/AffineEtaleHomology.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/AffineEtaleHomology.lean#L92). References: SGA 4½ Arcata (4.5.1), “more general”; SGA 7 XIII (2.1.6), “more general”.

> **Stacks Project, Tag 0GLK.** Let `f : X ⟶ Y` be a separated finite type morphism of
> quasi-compact and quasi-separated schemes, let `Λ` be a torsion ring (`n = 0` in `Λ` for some
> `n ≥ 1`) and let `K ∈ D(Y_étale, Λ)`.  For `m ∈ ℤ` the cohomology sheaf `H^m(Rf^! K)` restricted
> to `X_{affine, étale}` is the sheaf associated to the presheaf
> `U ↦ Hom_Y(R(U ⟶ Y)_! Λ, K[m])`.
>
> Here `Rf_! = R(fbar)_* ∘ j_!` is read off a compactification `j` of `f`, which exists by Nagata's
> theorem ([Stacks, Tag 0F41]), and `Rf^!` is its right adjoint of [Stacks, Tag 0G2C].  The
> identification holds for every compactification.  The functoriality of `R(U ⟶ Y)_! Λ` in `U` is
> that of the discussion preceding the lemma, and the identification is one of presheaves: the
> transition maps are those the source leaves to the reader.  The ring `Λ` lies in `Type`, the
> universe in which [Stacks, Tag 0G2C] is available.

```lean
theorem derivedUpperShriek_homology_affineEtale {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] [QuasiCompact f] [IsSeparated f]
    [CompactSpace X] [QuasiSeparatedSpace X] [CompactSpace Y] [QuasiSeparatedSpace Y] :
    (∃ j : CompactificationOf (Over.mk f), QuasiCompact j.immersion) ∧
      ∀ (j : CompactificationOf (Over.mk f)) (K : DerivedCategory (EtaleModules.{u, 0} Λ Y))
        (m : ℤ),
        letI := DerivedUpperShriek.isLeftAdjoint_derivedLowerShriekUnbounded Λ n hn hΛ f j
        Nonempty ((presheafToSheaf (AffineEtale.topology X) AddCommGrpCat.{u + 1 + 1}).obj
            (affineEtaleLowerShriekHomPresheafUnbounded.{u, 0} f j Λ K m) ≅
          (affineEtaleAbelianRestriction.{u, 0} Λ X).obj
            ((DerivedCategory.homologyFunctor _ m).obj
              ((derivedLowerShriekUnbounded.{u, 0} f j Λ).rightAdjoint.obj K)))
```

**`Stacks.EtaleCohomology.affineEtaleSheafifiedHomIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriekAffineEtale.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriekAffineEtale.lean#L308). The attribute's comment: “the comparison of the two sheafifications, which is the half of the tag not depending on Stacks 0BKV; Rf^! is an explicit right adjoint of Rf\_!, its existence being Stacks 0G2C”.

> **The content of Stacks Tag 0GLK that does not depend on Stacks Tag 0BKV.** The
> sheafification of the source's presheaf `U ↦ Hom_Y(R(U ⟶ Y)_! Λ, K[n])` on the small affine
> étale site of `X` is the sheafification of `U ↦ Hom_X((j_U)_! Λ, Rf^! K[n])`.

```lean
def affineEtaleSheafifiedHomIso {X Y : Scheme.{u}} {f : X ⟶ Y}
    (j : CompactificationOf (Over.mk f)) (Λ : Type r) [Ring Λ]
    {Uf : DerivedCategory.Plus (EtaleModules.{u, r} Λ Y) ⥤
      DerivedCategory.Plus (EtaleModules.{u, r} Λ X)}
    (adjF : derivedLowerShriek.{u, r} f j Λ ⊣ Uf)
    (K : DerivedCategory.Plus (EtaleModules.{u, r} Λ Y)) (n : ℤ) :
    (presheafToSheaf (AffineEtale.topology X) AddCommGrpCat.{max (u + 1) r + 1}).obj
        (affineEtaleLowerShriekHomPresheaf.{u, r} f j Λ K n) ≅
      (presheafToSheaf (AffineEtale.topology X) AddCommGrpCat.{max (u + 1) r + 1}).obj
        (affineEtaleUpperShriekHomPresheaf.{u, r} Λ X (Uf.obj K) n)
```

**`Stacks.EtaleCohomology.affineEtaleSheafifiedHomIsoOfToBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriekAffineEtale.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriekAffineEtale.lean#L331). The attribute's comment: “the comparison of the two sheafifications, assuming only a right adjoint of the proper pushforward R(fbar)\_*; the right adjoint of Rj\_! along the open immersion is constructed, not assumed”.

> **The same comparison, with only the right adjoint of the proper pushforward assumed.**
>
> `Rf_!` is the composite `R(fbar)_* ∘ Rj_!` of a compactification, and `Rj_!` has the right
> adjoint `Stacks.EtaleCohomology.etaleModuleDerivedExtensionByZeroAdj`, extension by zero along
> the open immersion being exact. So the adjunction `Rf_! ⊣ Rf^!` is
> `Stacks.EtaleCohomology.derivedLowerShriekAdjunctionOfFactors` of a right adjoint `Ubar` of
> `R(fbar)_*`, and `Rf^!` is `Ubar ⋙ Rj^{-1}`.

```lean
def affineEtaleSheafifiedHomIsoOfToBase {X Y : Scheme.{u}} {f : X ⟶ Y}
    (j : CompactificationOf (Over.mk f)) (Λ : Type r) [Ring Λ]
    {Ubar : DerivedCategory.Plus (EtaleModules.{u, r} Λ Y) ⥤
      DerivedCategory.Plus (EtaleModules.{u, r} Λ j.space)}
    (adjToBase : etaleModuleDerivedDirectImage.{u, r} Λ j.toBase ⊣ Ubar)
    (K : DerivedCategory.Plus (EtaleModules.{u, r} Λ Y)) (n : ℤ) :
    (presheafToSheaf (AffineEtale.topology X) AddCommGrpCat.{max (u + 1) r + 1}).obj
        (affineEtaleLowerShriekHomPresheaf.{u, r} f j Λ K n) ≅
      (presheafToSheaf (AffineEtale.topology X) AddCommGrpCat.{max (u + 1) r + 1}).obj
        (affineEtaleUpperShriekHomPresheaf.{u, r} Λ X
          ((Ubar ⋙ etaleModuleDerivedRestriction.{u, r} Λ j.immersion).obj K) n)
```

**`Stacks.EtaleCohomology.derivedUpperShriekHomologyAffineEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriekAffineEtale.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriekAffineEtale.lean#L364). The attribute's comment: “with Rf^! taken as an explicit right adjoint of Rf\_!, its existence being Stacks 0G2C, which is not proved in this library and is therefore an interface here; and with Stacks 0BKV supplied at the single object Rf^!K, the clauses of 0BKV in this library being stated for a RingedSite's SheafOfModules in the derived-sections presentation, which does not instantiate to Sheaf(X\_etale, ModuleCat Λ) in the Hom((j\_U)\_!Λ, -) presentation”.

> **Stacks Project, Tag 0GLK.** Let `f : X ⟶ Y` be a separated finite type morphism of
> quasi-compact and quasi-separated schemes, let `Λ` be a ring, let `K` be an object of
> `D⁺(Y_étale, Λ)` and let `n : ℤ`.  Let `Uf` be a right adjoint of `Rf_!`, so `Uf = Rf^!`.  Then
> the cohomology sheaf `H^n(Rf^! K)`, restricted to the small affine étale site of `X`, is the
> sheaf associated to the presheaf
> ```
> U ↦ Hom_Y(R(U ⟶ Y)_! Λ, K[n])
> ```
> The right adjoint `Uf` and the adjunction are data: the adjunction is what `Rf^!` is, and its
> existence is Stacks Tag 0G2C.  The hypothesis `sheafifiedCohomology` is Stacks Tag 0BKV
> together with the source's recollection `Hom_X(j_! Λ, M[n]) = H^n(U, M)`, at the single object
> `M = Rf^! K`.

```lean
def derivedUpperShriekHomologyAffineEtale {X Y : Scheme.{u}} {f : X ⟶ Y}
    (j : CompactificationOf (Over.mk f)) (Λ : Type r) [Ring Λ]
    {Uf : DerivedCategory.Plus (EtaleModules.{u, r} Λ Y) ⥤
      DerivedCategory.Plus (EtaleModules.{u, r} Λ X)}
    (adjF : derivedLowerShriek.{u, r} f j Λ ⊣ Uf)
    (K : DerivedCategory.Plus (EtaleModules.{u, r} Λ Y)) (n : ℤ)
    (sheafifiedCohomology :
      (presheafToSheaf (AffineEtale.topology X) AddCommGrpCat.{max (u + 1) r + 1}).obj
          (affineEtaleUpperShriekHomPresheaf.{u, r} Λ X (Uf.obj K) n) ≅
        (affineEtaleAbelianRestriction.{u, r} Λ X).obj
          ((DerivedCategory.Plus.homologyFunctor (EtaleModules.{u, r} Λ X) n).obj
            (Uf.obj K))) :
    (presheafToSheaf (AffineEtale.topology X) AddCommGrpCat.{max (u + 1) r + 1}).obj
        (affineEtaleLowerShriekHomPresheaf.{u, r} f j Λ K n) ≅
      (affineEtaleAbelianRestriction.{u, r} Λ X).obj
        ((DerivedCategory.Plus.homologyFunctor (EtaleModules.{u, r} Λ X) n).obj (Uf.obj K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 63.16, Tag 0GLJ](https://stacks.math.columbia.edu/tag/0GLJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
