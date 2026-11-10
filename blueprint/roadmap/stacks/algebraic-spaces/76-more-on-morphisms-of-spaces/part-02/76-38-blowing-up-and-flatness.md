---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_isFiniteTypeQuasicoherentIdeal_disjoint_pullbackIdealSubsheaf_eq_idealSmul, AlgebraicGeometry.Space.exists_isFlatteningBlowup_of_isLocallyOfFinitePresentation
statement: formalized
proof: formalized
---

# 76.38 Blowing up and flatness

Section 76.38 of the Stacks Project, [Tag 087A](https://stacks.math.columbia.edu/tag/087A). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 087B, a lemma

[Tag 087B](https://stacks.math.columbia.edu/tag/087B) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isFiniteTypeQuasicoherentIdeal_disjoint_pullbackIdealSubsheaf_eq_idealSmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeIdealEtaleFittingDescentUnconditional.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeIdealEtaleFittingDescentUnconditional.lean#L61).

> **Stacks 087B.**  Let `X` be a quasi-compact and quasi-separated algebraic space over `S`,
> let `φ : W ⟶ X` be a quasi-compact separated étale morphism, let `U ⊆ X` be a quasi-compact
> open subspace and let `𝓘 ⊆ 𝒪_W` be a finite type quasi-coherent sheaf of ideals with
> `V(𝓘) ∩ φ⁻¹(U) = ∅`.  Then there is a finite type quasi-coherent sheaf of ideals `𝓙 ⊆ 𝒪_X`
> such that
>
> 1. `V(𝓙) ∩ U = ∅`, and
> 2. `φ⁻¹(𝓙) 𝒪_W = 𝓘 𝓘'` for some finite type quasi-coherent sheaf of ideals `𝓘' ⊆ 𝒪_W`.
>
> The inverse-image ideal `φ⁻¹(𝓙) 𝒪_W` is `AlgebraicGeometry.Space.pullbackIdealSubsheaf`, which
> is defined for representable morphisms; a separated étale morphism is representable by
> Stacks 0418, and the statement names that proof.

```lean
theorem exists_isFiniteTypeQuasicoherentIdeal_disjoint_pullbackIdealSubsheaf_eq_idealSmul
    {X W : AlgebraicSpaces B S hS} (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1)
    (φ : W ⟶ X) (hφqc : IsQuasiCompact B S hS φ.hom) (hφsep : IsSeparated B S hS φ.hom)
    (hφet : IsEtale B S hS φ.hom)
    (U : Subfunctor X.1) (hU : IsOpenSubspace B S hS U)
    (hUqc : IsQuasiCompactSpace B S hS U.toFunctor)
    (I : (SheafOfModules.unit (structureRingSheaf B S hS W)).Submodule)
    (hI : IsFiniteTypeQuasicoherentIdeal B S hS W I)
    (hIU : Disjoint (idealZeroLocus B S hS W I)
      (subspacePointSet B S hS W.1 (U.preimage φ.hom))) :
    ∃ J : (SheafOfModules.unit (structureRingSheaf B S hS X)).Submodule,
      IsFiniteTypeQuasicoherentIdeal B S hS X J ∧
        Disjoint (idealZeroLocus B S hS X J) (subspacePointSet B S hS X.1 U) ∧
        ∃ I' : (SheafOfModules.unit (structureRingSheaf B S hS W)).Submodule,
          IsFiniteTypeQuasicoherentIdeal B S hS W I' ∧
            pullbackIdealSubsheaf B S hS φ
                (relativelyRepresentable_of_isLocallyQuasiFinite_isSeparated B S hS φ.hom W.2 X.2
                  (isLocallyQuasiFinite_of_isEtale' B S hS hφet) hφsep) J =
              Stacks.Sites.idealSmul (O := structureSheaf B S hS W.1 W.2) I I'
```

## Tag 087C, a theorem

[Tag 087C](https://stacks.math.columbia.edu/tag/087C) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isFlatteningBlowup_of_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatteningByBlowupAlgebraicSpaceUnconditional.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatteningByBlowupAlgebraicSpaceUnconditional.lean#L51).

> **Flattening by blowing up for algebraic spaces.** Let `A` be a quasi-compact and
> quasi-separated algebraic space over `S`, let `f : X ⟶ A` be locally of finite presentation with
> `X` quasi-compact, let `F` be a quasi-coherent `𝒪_X`-module of finite type and let `U ⊆ A` be a
> quasi-compact open subspace such that `F_U = F|_{X ×_A U}` is of finite presentation and flat
> over `U`. Then there is a blowup `b : A' ⟶ A` in a finitely presented closed subspace `Z`
> disjoint from `U` (a `U`-admissible blowup) such that the strict transform of `F` with respect
> to `b` is an `𝒪_{X ×_A A'}`-module of finite presentation, flat over `A'`.

```lean
theorem exists_isFlatteningBlowup_of_isLocallyOfFinitePresentation
    {A : AlgebraicSpaces B S hS} (hAqc : IsQuasiCompactSpace B S hS A.1)
    (hAqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal A.1)
    (U : OpenSubspaces B S hS A.1) (hUqc : IsQuasiCompactSpace B S hS U.1.toFunctor)
    {X : AlgebraicSpaces B S hS} (f : X ⟶ A)
    (hXqc : IsQuasiCompactSpace B S hS X.1) (hf : IsLocallyOfFinitePresentation B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (hFqc : F.IsQuasicoherentOnSite)
    (hFft : F.IsFiniteTypeOnSite)
    (hFUfp : ((modulePullback B S hS (restrictOverι f U)).obj F).IsFinitePresentationOnSite)
    (hFUflat : IsFlatOver B S hS (restrictOver f U).2 (restrictOverHom f U).hom
      ((modulePullback B S hS (restrictOverι f U)).obj F)) :
    ∃ (Z : ClosedSubspaces B S hS A.1) (A' : AlgebraicSpaces B S hS) (b : A' ⟶ A),
      IsFlatteningBlowup f F U Z b
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.38, Tag 087A](https://stacks.math.columbia.edu/tag/087A)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
