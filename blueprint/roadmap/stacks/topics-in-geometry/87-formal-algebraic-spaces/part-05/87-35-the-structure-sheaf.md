---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.exists_isStructureSheaf, AlgebraicGeometry.FormalSpace.exists_isAffineFormalAlgebraicSpace_not_enough_sections, AlgebraicGeometry.FormalSpace.completedCechComplex_homology_isZero, AlgebraicGeometry.FormalSpace.exists_completedCechComplex_homology_isZero_of_isCountablyIndexed, AlgebraicGeometry.FormalSpace.subsingleton_sheafH_countablyIndexedStructureSheaf, AlgebraicGeometry.FormalSpace.subsingleton_sheafH_canonicalStructureSheaf, AlgebraicGeometry.FormalSpace.not_nonempty_abelian_quasicoherentModules_completionAlongIdeal
statement: formalized
proof: formalized
---

# 87.35 The structure sheaf

Section 87.35 of the Stacks Project, [Tag 0DEI](https://stacks.math.columbia.edu/tag/0DEI). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DEJ, a lemma

[Tag 0DEJ](https://stacks.math.columbia.edu/tag/0DEJ) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_isStructureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/StructureSheaf/Exists.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/StructureSheaf/Exists.lean#L66).

> **Stacks 0DEJ.** Every formal algebraic space has a structure sheaf: a sheaf of topological
> rings `𝒪_X` on its small étale site `X_étale` such that `𝒪_X(U_red) = lim Γ(U_λ, 𝒪_{U_λ})` as
> topological rings, canonically, for every affine formal algebraic space `U` with a morphism
> `U ⟶ X` representable by algebraic spaces and étale, and every colimit presentation
> `U = colim U_λ` of `U` as in Stacks 0AI7 (`AlgebraicGeometry.FormalSpace.IsStructureSheaf`).

```lean
theorem exists_isStructureSheaf {X : FppfSheaf B S hS} (hX : IsFormalAlgebraicSpace B S hS X) :
    ∃ O : Sheaf (canonicalSmallEtaleTopology hX) TopCommRingCat.{u + 1}, IsStructureSheaf hX O
```

## Tag 0DEK, a remark

[Tag 0DEK](https://stacks.math.columbia.edu/tag/0DEK) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_isAffineFormalAlgebraicSpace_not_enough_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/NotEnoughSections.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/NotEnoughSections.lean#L209).

> The structure sheaf of a formal algebraic space does not always have enough sections. There
> is an affine formal algebraic space `X` which is not McQuillan (it fails condition (4) of Stacks
> 0AIC) and whose points are not separated by regular functions, in the sense of Stacks 0CBD:
> * for every presentation `X = colim X_λ` by affine thickenings as in Stacks 0AI7, the ring
>   `lim Γ(X_λ, O_{X_λ})` of regular functions is a field, every stage `X_λ` has infinitely many
>   points (they are the points of `X`, see
>   `AlgebraicGeometry.FormalSpace.pointsULiftEquivStage`), and each regular function vanishes
>   either at all points of a stage or at none, so it separates no two points;
> * `X` has infinitely many points, and its reduction `X_red` is represented by a scheme of the
>   site with infinitely many points.

```lean
theorem exists_isAffineFormalAlgebraicSpace_not_enough_sections :
    ∃ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) (X : FppfSheaf B S hS),
      IsAffineFormalAlgebraicSpace B S hS X ∧
      ¬ HasSomeSurjectivePresentation B S hS X ∧
      (∀ (I : Type (u + 1)) [Preorder I] [Nonempty I] [IsDirected I (· ≤ ·)]
        (D : I ⥤ BigAffineFppf B S hS),
        (∀ ⦃i j : I⦄ (f : i ⟶ j),
          Stacks.Thickenings.IsThickening ((BigAffineFppf.toScheme B S hS).map (D.map f))) →
        Nonempty (X ≅ colimit (D ⋙ BigAffineFppf.inclusion B S hS ⋙
          Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))) →
        IsField (sectionDiagram B S hS D ⋙ forget CommRingCat.{u}).sections ∧
        (∀ i : I, Infinite ((BigAffineFppf.toScheme B S hS).obj (D.obj i))) ∧
        ∀ (f : (sectionDiagram B S hS D ⋙ forget CommRingCat.{u}).sections) (i : I)
          (x y : (BigAffineFppf.toScheme B S hS).obj (D.obj i)),
          x ∈ ((BigAffineFppf.toScheme B S hS).obj (D.obj i)).basicOpen (f.1 (op i)) ↔
            y ∈ ((BigAffineFppf.toScheme B S hS).obj (D.obj i)).basicOpen (f.1 (op i))) ∧
      Infinite (Space.pointsULift.{u + 1} B S hS X.obj) ∧
      ∃ (T : BigFppfOver B S hS)
        (ι : (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj T ⟶ X),
        IsReduction B S hS X ((Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj T) ι ∧
        Infinite ((BigFppfOver.toScheme B S hS).obj T)
```

## Tag 0DEL, a lemma

[Tag 0DEL](https://stacks.math.columbia.edu/tag/0DEL) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.completedCechComplex_homology_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/StructureSheafEtaleCohomology.lean, line 411](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/StructureSheafEtaleCohomology.lean#L411). The attribute's comment: “the computation half of the proof: for a covering of `X = Spf A` by one affine étale chart `Spf B^∧` the Čech cohomology of `𝒪_X` vanishes in every positive degree. The site-theoretic half, the reduction of `Hⁿ(X_étale, 𝒪_X)` to these Čech complexes along Stacks 03F9, 03OZ, 0DEE and 0DEF, is not carried: this library does have the étale sites of a formal algebraic space, `AlgebraicGeometry.FormalSpace.SmallEtale` and its siblings of Stacks 0DEA, and Stacks 0DEE as an equivalence, AlgebraicGeometry.FormalSpace.affineEtaleEquivalence, but no structure sheaf on an étale site; Stacks 0DEF is formalized only as the ring-theoretic category of the completions `B^∧`. Stated for an arbitrary antitone sequence of ideals and an arbitrary faithfully flat `A`-algebra, which generalizes the source's weakly admissible `A` and étale covering `A → B`”.

> **Stacks 0DEL.**  Let `X = Spf A` be a countably indexed affine formal algebraic space, with
> `J₀ ⊇ J₁ ⊇ ⋯` a countable fundamental system of weak ideals of definition of `A`, and let
> `{Spf B^∧ ⟶ Spf A}` be a covering in the affine étale site, so that `A → B` is faithfully flat.
> Then `Ȟⁿ({Spf B^∧ ⟶ Spf A}, 𝒪_X) = 0` for `n > 0`.

```lean
theorem completedCechComplex_homology_isZero [Module.FaithfullyFlat A B] (n : ℕ) (hn : 0 < n) :
    IsZero ((completedCechComplex B J hJ).homology (n + 1))
```

**`AlgebraicGeometry.FormalSpace.exists_completedCechComplex_homology_isZero_of_isCountablyIndexed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/StructureSheafEtaleCohomology.lean, line 495](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/StructureSheafEtaleCohomology.lean#L495). The attribute's comment: “the covering-level content with the source's own hypotheses: a countably indexed affine formal algebraic space and a surjective affine étale chart of it, in place of the antitone sequence of ideals and the faithfully flat algebra of `completedCechComplex_homology_isZero`. The conclusion is still the vanishing of the Čech cohomology of the covering, not of `Hⁿ(X_étale, 𝒪_X)`: this library has no structure sheaf on the étale site of a formal algebraic space: Stacks 0DEE is an equivalence here, AlgebraicGeometry.FormalSpace.affineEtaleEquivalence, but Stacks 0DEF is formalized only as the ring-theoretic category of the completions `B^∧`, so no object of the affine étale site is known to be of the form `Spf B^∧` and the sections of `𝒪_X` are undefined”.

> **Stacks 0DEL** with the hypotheses of the source.  A countably indexed affine formal
> algebraic space `X` is the formal spectrum of a weakly admissible topological ring `A` carrying
> a countable antitone fundamental system `J₀ ⊇ J₁ ⊇ ⋯` of weak ideals of definition, and for
> every covering `{Spf B^∧ ⟶ Spf A}` of `X` by one affine étale chart, in the sense of Stacks
> 0DEF and with `Spf B^∧ ⟶ Spf A` surjective, the Čech complex of `𝒪_X` for that covering has no
> cohomology in positive Čech degrees.
>
> Affineness of `X` is not assumed: it is part of the conclusion, `X` being exhibited as a formal
> spectrum.

```lean
theorem exists_completedCechComplex_homology_isZero_of_isCountablyIndexed
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) {X : FppfSheaf B S hS}
    (hc : IsCountablyIndexed B S hS X) :
    ∃ (A : Type u) (_ : CommRing A) (_ : TopologicalSpace A) (_ : IsTopologicalRing A)
      (_ : IsLinearTopology A A) (hA : TopologicalRing.IsWeaklyAdmissible A)
      (Q : QuotientSystem B S hS A) (J : ℕ → Ideal A) (hJ : Antitone J),
      (∀ k, TopologicalRing.IsWeakIdealOfDefinition (J k)) ∧
        (nhds (0 : A)).HasBasis (fun _ : ℕ ↦ True) (fun k ↦ (J k : Set A)) ∧
        Nonempty (X ≅ formalSpectrum Q) ∧
        ∀ (Y : EtaleCompletion A) (E : QuotientSystem B S hS Y.completion)
          (g : ContinuousHom Q E), g.toRingHom = Y.structureMap →
          IsSurjective B S hS (formalSpectrumMap hA g) → ∀ n : ℕ, 0 < n →
            letI : Algebra A Y.carrier := Y.str.toAlgebra
            IsZero ((completedCechComplex Y.carrier J hJ).homology (n + 1))
```

**`AlgebraicGeometry.FormalSpace.subsingleton_sheafH_countablyIndexedStructureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/StructureSheafHigherVanishing.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/StructureSheafHigherVanishing.lean#L119). The attribute's comment: “at an arbitrary reduction `X_red` of `X`, which Stacks 0DEA reads `X_étale` against”.

> **Stacks 0DEL.** Let `X` be a countably indexed affine formal algebraic space over `S`, and
> let `X_red` be a reduction of `X`. Then the structure sheaf `𝒪_X` has no higher cohomology on
> `X_étale`: `Hⁿ(X_étale, 𝒪_X) = 0` for `n > 0`.
>
> Only the countable presentation of `X` is used, not the set-theoretic condition which makes `X`
> an affine formal algebraic space, so the statement is given for a countably indexed sheaf.

```lean
theorem subsingleton_sheafH_countablyIndexedStructureSheaf (hc : IsCountablyIndexed B S hS X)
    (R : Reduction B S hS X) [HasExt.{x} (Sheaf R.smallEtaleTopology AddCommGrpCat.{u + 1})]
    (n : ℕ) (hn : 0 < n) :
    Subsingleton (Sheaf.H
      ((sheafCompose _ Space.topCommRingToAddCommGrp).obj
        (countablyIndexedStructureSheaf hc R)) n)
```

**`AlgebraicGeometry.FormalSpace.subsingleton_sheafH_canonicalStructureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/StructureSheafHigherVanishing.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/StructureSheafHigherVanishing.lean#L131).

> **Stacks 0DEL.** If `X` is a countably indexed affine formal algebraic space over `S`, then
> `Hⁿ(X_étale, 𝒪_X) = 0` for `n > 0`, where `X_étale` is the small étale site of Stacks 0DEA at the
> reduction of `X` given by Stacks 0AIN, and `𝒪_X` is the structure sheaf of `X` on it.

```lean
theorem subsingleton_sheafH_canonicalStructureSheaf (hX : IsAffineFormalAlgebraicSpace B S hS X)
    (hc : IsCountablyIndexed B S hS X)
    [HasExt.{x} (Sheaf (canonicalSmallEtaleTopology
      (isFormalAlgebraicSpace_of_isAffineFormalAlgebraicSpace B S hS hX)) AddCommGrpCat.{u + 1})]
    (n : ℕ) (hn : 0 < n) :
    Subsingleton (Sheaf.H
      ((sheafCompose _ Space.topCommRingToAddCommGrp).obj
        (countablyIndexedStructureSheaf hc
          (canonicalReduction
            (isFormalAlgebraicSpace_of_isAffineFormalAlgebraicSpace B S hS hX)))) n)
```

## Tag 0DEM, a remark

[Tag 0DEM](https://stacks.math.columbia.edu/tag/0DEM) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.not_nonempty_abelian_quasicoherentModules_completionAlongIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionQuasicoherentNotAbelian.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionQuasicoherentNotAbelian.lean#L79). The attribute's comment: “the content of Examples, Section 0ALF: for every Noetherian domain `A` complete for a principal ideal `(π)` with `π ≠ 0` not a unit, `Spf(A)` is a Noetherian affine formal algebraic space whose quasi-coherent modules do not form an abelian category”.

> **Stacks 0DEM.** Let `A` be a Noetherian domain which is complete for a principal ideal
> `I = (π)` with `π` neither zero nor a unit, and let `X = Spf(A)` be the completion of `Spec A`
> along `V(I)`, over any base scheme `S` of any big fppf site. Then `X` is a Noetherian affine
> formal algebraic space, and the category of quasi-coherent modules on `X` (Stacks 06WG) is not
> abelian: it admits no abelian structure at all.
>
> Formal Spaces, Remark 0DEM, says that for almost any Noetherian affine formal algebraic space the
> natural category of quasi-coherent modules is not abelian, referring to Examples, Section 0ALF;
> the content of that section is the identification of these modules with the complete
> `A`-modules (`AlgebraicGeometry.FormalSpace.quasicoherentModulesCompletionEquiv`) together with
> the non-abelianness of the latter (Stacks 07JR), and this statement is that content for every
> such `A`, of which the section's `ℤ_p` is one.

```lean
theorem not_nonempty_abelian_quasicoherentModules_completionAlongIdeal
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) {A : Type u} [CommRing A]
    [IsNoetherianRing A] [NoZeroDivisors A] (f : Spec (.of A) ⟶ S)
    (hA : B.Contains (Spec (.of A))) (I : Ideal A) (hAc : IsAdicComplete I A) (π : A)
    (hIπ : I = Ideal.span {π}) (hπ : π ≠ 0) (hπu : ¬ IsUnit π) :
    IsAffineFormalAlgebraicSpace B S hS (completionAlongIdeal B S hS f hA I) ∧
      IsNoetherian B S hS (completionAlongIdeal B S hS f hA I) ∧
      ¬ Nonempty (Abelian (FibredSite.quasicoherentModules.{u, u + 1, u + 1, u} B S hS
        (completionFibred B S hS f hA I).p
        (isFiberedInGroupoids_completionFibred B S hS f hA I)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.35, Tag 0DEI](https://stacks.math.columbia.edu/tag/0DEI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
