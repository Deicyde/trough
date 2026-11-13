---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_isPerfect_retract_restrict_of_supported, AlgebraicGeometry.Space.exists_isPerfect_restrict_iso_biprod_isIso_homologyFunctor_map_inl, AlgebraicGeometry.Space.exists_isPerfect_retract_restrict_isIso_homologyFunctor_map, AlgebraicGeometry.Space.exists_isPerfect_retract_restrict, AlgebraicGeometry.Space.exists_isPerfect_restrict_iso_biprod_of_isPerfect, AlgebraicGeometry.Space.exists_isPerfect_generator, AlgebraicGeometry.Space.exists_isPerfect_isZero_iff_forall_hom_shift_eq_zero, AlgebraicGeometry.Space.tfae_reflectsIsomorphisms_quasicoherentDerivedPushforward
statement: formalized
proof: formalized
---

# 75.15 Generating derived categories

Section 75.15 of the Stacks Project, [Tag 09IU](https://stacks.math.columbia.edu/tag/09IU). 6 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09IV, a lemma

[Tag 09IV](https://stacks.math.columbia.edu/tag/09IV) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isPerfect_retract_restrict_of_supported`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectSupportedExtension.lean, line 673](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectSupportedExtension.lean#L673).

> **Stacks 09IV.** Let `S` be a scheme, `X` a quasi-compact and quasi-separated algebraic space
> over `S`, `W ⊆ X` a quasi-compact open subspace and `T ⊆ |X|` a closed subset such that
> `X \ T ⟶ X` is quasi-compact. Let `E` be an object of `D_QCoh(𝒪_X)` and `α : P ⟶ E|_W` a map
> where `P` is a perfect object of `D(𝒪_W)` supported on `T ∩ W`. Then there exists a map
> `β : R ⟶ E` where `R` is a perfect object of `D(𝒪_X)` supported on `T` such that `P` is a
> direct summand of `R|_W` in `D(𝒪_W)` compatibly with `α` and `β|_W`: there are
> `s : P ⟶ R|_W` and `r : R|_W ⟶ P` with `s ≫ r = 𝟙 P` and `s ≫ β|_W = α`.

```lean
theorem exists_isPerfect_retract_restrict_of_supported
    (hZ : B.Contains (⊤_ Scheme.{u})) (X : AlgebraicSpaces B S hS)
    (hXqc : IsQuasiCompactSpace B S hS X.1) (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (W : Subfunctor X.1) (hW : IsOpenSubspace B S hS W)
    (hWqc : IsQuasiCompactSpace B S hS W.toFunctor) (T : Set (points B S hS X.1))
    (hT : IsClosed T)
    (hTqc : IsQuasiCompact B S hS
      ((openSubspacesOrderIso B S hS X.1 X.2).symm ⟨Tᶜ, hT.isOpen_compl⟩).1.ι)
    (E : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2)
    (P : DerivedCategory (Modules.{u, u} B S hS (openSubspaceSpace B S hS W hW).1
      (openSubspaceSpace B S hS W hW).2))
    (hP : (smallEtaleRingedSite B S hS (openSubspaceSpace B S hS W hW).1
      (openSubspaceSpace B S hS W hW).2).IsPerfect P)
    (hPT : CohomologySupportedOn B S hS (openSubspaceSpace B S hS W hW).1
      (openSubspaceSpace B S hS W hW).2 (pointsMap B S hS W.toFunctor W.ι ⁻¹' T) P)
    (α : P ⟶ (etaleModulePullback.{u, u} B S hS (openSubspaceHom B S hS W hW)
      (isEtale_openSubspaceHom B S hS W hW)).mapDerivedCategory.obj E.obj) :
    ∃ (R : DerivedCategory (Modules.{u, u} B S hS X.1 X.2)) (β : R ⟶ E.obj),
      (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect R ∧
      CohomologySupportedOn B S hS X.1 X.2 T R ∧
      ∃ (s : P ⟶ (etaleModulePullback.{u, u} B S hS (openSubspaceHom B S hS W hW)
          (isEtale_openSubspaceHom B S hS W hW)).mapDerivedCategory.obj R)
        (r : (etaleModulePullback.{u, u} B S hS (openSubspaceHom B S hS W hW)
          (isEtale_openSubspaceHom B S hS W hW)).mapDerivedCategory.obj R ⟶ P),
        s ≫ r = 𝟙 P ∧
        s ≫ (etaleModulePullback.{u, u} B S hS (openSubspaceHom B S hS W hW)
          (isEtale_openSubspaceHom B S hS W hW)).mapDerivedCategory.map β = α
```

## Tag 09IW, a remark

[Tag 09IW](https://stacks.math.columbia.edu/tag/09IW) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isPerfect_restrict_iso_biprod_isIso_homologyFunctor_map_inl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectSupportedExtensionCohomology.lean, line 757](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectSupportedExtensionCohomology.lean#L757). The attribute's comment: “first and second assertions: the shape of the restriction, and its top cohomology”.

> **Stacks 09IW, first two assertions.** Let `S` be a scheme, `X` a quasi-compact and
> quasi-separated algebraic space over `S`, `W ⊆ X` a quasi-compact open subspace, `T ⊆ |X|` a
> closed subset such that `X \ T ⟶ X` is quasi-compact, `E` an object of `D_QCoh(𝒪_X)` and
> `α : P ⟶ E|_W` a morphism from a perfect object `P` of `D(𝒪_W)` supported on `T ∩ W`. The
> construction of Stacks 09IV gives `β : R ⟶ E`, with `R` a perfect object of `D(𝒪_X)` supported
> on `T`, such that
>
> 1. `R|_W ≅ P ⊕ C` with `C ≅ P^{⊕ n₁}[1] ⊕ ⋯ ⊕ P^{⊕ nₘ}[m]` for some `m ≥ 0` and `n_j ≥ 0`
>    (`CategoryTheory.IsFiniteSumOfPositiveShifts`), `β|_W` being `α` on `P` and zero on `C`;
> 2. the highest degree cohomology sheaf of `R|_W` is that of `P`: whenever `Hⁱ(P) = 0` for all
>    `i > d`, the inclusion of the summand `P` induces `Hⁱ(P) ≅ Hⁱ(R|_W)` for every `i ≥ d`.
>
> Both derived categories are taken at arbitrary models; "supported on" is the condition of
> Stacks 08GF on every cohomology sheaf, and `D_QCoh(𝒪_X)` is the condition of Stacks 071X.

```lean
theorem exists_isPerfect_restrict_iso_biprod_isIso_homologyFunctor_map_inl
    (X : AlgebraicSpaces B S hS) (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1)
    (W : Subfunctor X.1) (hW : IsOpenSubspace B S hS W)
    (hWqc : IsQuasiCompactSpace B S hS W.toFunctor) (T : Set (points B S hS X.1))
    (hT : IsClosed T)
    (hTqc : IsQuasiCompact B S hS
      ((openSubspacesOrderIso B S hS X.1 X.2).symm ⟨Tᶜ, hT.isOpen_compl⟩).1.ι)
    [hDX : HasDerivedCategory.{w} (Modules.{u, u} B S hS X.1 X.2)]
    [hDW : HasDerivedCategory.{w'} (Modules.{u, u} B S hS (openSubspaceSpace B S hS W hW).1
      (openSubspaceSpace B S hS W hW).2)]
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hE : DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O)) E)
    (P : DerivedCategory (Modules.{u, u} B S hS (openSubspaceSpace B S hS W hW).1
      (openSubspaceSpace B S hS W hW).2))
    (hP : (smallEtaleRingedSite B S hS (openSubspaceSpace B S hS W hW).1
      (openSubspaceSpace B S hS W hW).2).IsPerfect P)
    (hPT : ∀ i : ℤ, supportOfSheaf B S hS (openSubspaceSpace B S hS W hW).1
      ((SheafOfModules.toSheaf.{u} _).obj ((DerivedCategory.homologyFunctor
        (Modules.{u, u} B S hS (openSubspaceSpace B S hS W hW).1
          (openSubspaceSpace B S hS W hW).2) i).obj P)) ⊆
        pointsMap B S hS W.toFunctor W.ι ⁻¹' T)
    (α : P ⟶ (etaleModulePullback.{u, u} B S hS (openSubspaceHom B S hS W hW)
      (isEtale_openSubspaceHom B S hS W hW)).mapDerivedCategory.obj E) :
    ∃ (R : DerivedCategory (Modules.{u, u} B S hS X.1 X.2)) (β : R ⟶ E),
      (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect R ∧
      (∀ i : ℤ, supportOfSheaf B S hS X.1
        ((SheafOfModules.toSheaf.{u} _).obj
          ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X.1 X.2) i).obj R)) ⊆ T) ∧
      ∃ (C : DerivedCategory (Modules.{u, u} B S hS (openSubspaceSpace B S hS W hW).1
          (openSubspaceSpace B S hS W hW).2))
        (e : (etaleModulePullback.{u, u} B S hS (openSubspaceHom B S hS W hW)
          (isEtale_openSubspaceHom B S hS W hW)).mapDerivedCategory.obj R ≅ P ⊞ C),
        IsFiniteSumOfPositiveShifts P C ∧
        (etaleModulePullback.{u, u} B S hS (openSubspaceHom B S hS W hW)
          (isEtale_openSubspaceHom B S hS W hW)).mapDerivedCategory.map β =
          e.hom ≫ biprod.fst ≫ α ∧
        ∀ d : ℤ, (∀ i : ℤ, d < i → IsZero ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS
            (openSubspaceSpace B S hS W hW).1
          (openSubspaceSpace B S hS W hW).2) i).obj P)) →
          ∀ i : ℤ, d ≤ i → IsIso ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS
              (openSubspaceSpace B S hS W hW).1
          (openSubspaceSpace B S hS W hW).2) i).map (biprod.inl ≫ e.inv))
```

**`AlgebraicGeometry.Space.exists_isPerfect_retract_restrict_isIso_homologyFunctor_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectSupportedExtensionCohomology.lean, line 821](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectSupportedExtensionCohomology.lean#L821). The attribute's comment: “third assertion: equality of cohomology sheaves above any given degree”.

> **Stacks 09IW, third assertion.** In the situation of Stacks 09IV — `S` a scheme, `X` a
> quasi-compact and quasi-separated algebraic space over `S`, `W ⊆ X` a quasi-compact open subspace,
> `T ⊆ |X|` closed with `X \ T ⟶ X` quasi-compact, `E` in `D_QCoh(𝒪_X)` and `α : P ⟶ E|_W` with
> `P` perfect in `D(𝒪_W)` supported on `T ∩ W` — one can achieve equality of the cohomology sheaves
> of `R|_W` and `P` above any given degree: for every integer `N` there is `β : R ⟶ E` with `R`
> perfect in `D(𝒪_X)` and supported on `T`, and `P` a direct summand of `R|_W` compatibly with `α`
> and `β|_W` — `s : P ⟶ R|_W` and `r : R|_W ⟶ P` with `s ≫ r = 𝟙 P` and `s ≫ β|_W = α`, indeed
> `β|_W = r ≫ α` — such that `Hⁱ(s) : Hⁱ(P) ⟶ Hⁱ(R|_W)` is an isomorphism for every `i ≥ N`.
>
> Both derived categories are taken at arbitrary models.

```lean
theorem exists_isPerfect_retract_restrict_isIso_homologyFunctor_map
    (X : AlgebraicSpaces B S hS) (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1)
    (W : Subfunctor X.1) (hW : IsOpenSubspace B S hS W)
    (hWqc : IsQuasiCompactSpace B S hS W.toFunctor) (T : Set (points B S hS X.1))
    (hT : IsClosed T)
    (hTqc : IsQuasiCompact B S hS
      ((openSubspacesOrderIso B S hS X.1 X.2).symm ⟨Tᶜ, hT.isOpen_compl⟩).1.ι)
    [hDX : HasDerivedCategory.{w} (Modules.{u, u} B S hS X.1 X.2)]
    [hDW : HasDerivedCategory.{w'} (Modules.{u, u} B S hS (openSubspaceSpace B S hS W hW).1
      (openSubspaceSpace B S hS W hW).2)]
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hE : DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O)) E)
    (P : DerivedCategory (Modules.{u, u} B S hS (openSubspaceSpace B S hS W hW).1
      (openSubspaceSpace B S hS W hW).2))
    (hP : (smallEtaleRingedSite B S hS (openSubspaceSpace B S hS W hW).1
      (openSubspaceSpace B S hS W hW).2).IsPerfect P)
    (hPT : ∀ i : ℤ, supportOfSheaf B S hS (openSubspaceSpace B S hS W hW).1
      ((SheafOfModules.toSheaf.{u} _).obj ((DerivedCategory.homologyFunctor
        (Modules.{u, u} B S hS (openSubspaceSpace B S hS W hW).1
          (openSubspaceSpace B S hS W hW).2) i).obj P)) ⊆
        pointsMap B S hS W.toFunctor W.ι ⁻¹' T)
    (α : P ⟶ (etaleModulePullback.{u, u} B S hS (openSubspaceHom B S hS W hW)
      (isEtale_openSubspaceHom B S hS W hW)).mapDerivedCategory.obj E) (N : ℤ) :
    ∃ (R : DerivedCategory (Modules.{u, u} B S hS X.1 X.2)) (β : R ⟶ E),
      (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect R ∧
      (∀ i : ℤ, supportOfSheaf B S hS X.1
        ((SheafOfModules.toSheaf.{u} _).obj
          ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X.1 X.2) i).obj R)) ⊆ T) ∧
      ∃ (s : P ⟶ (etaleModulePullback.{u, u} B S hS (openSubspaceHom B S hS W hW)
          (isEtale_openSubspaceHom B S hS W hW)).mapDerivedCategory.obj R)
        (r : (etaleModulePullback.{u, u} B S hS (openSubspaceHom B S hS W hW)
          (isEtale_openSubspaceHom B S hS W hW)).mapDerivedCategory.obj R ⟶ P),
        s ≫ r = 𝟙 P ∧
        s ≫ (etaleModulePullback.{u, u} B S hS (openSubspaceHom B S hS W hW)
          (isEtale_openSubspaceHom B S hS W hW)).mapDerivedCategory.map β = α ∧
        (etaleModulePullback.{u, u} B S hS (openSubspaceHom B S hS W hW)
          (isEtale_openSubspaceHom B S hS W hW)).mapDerivedCategory.map β = r ≫ α ∧
        ∀ i : ℤ, N ≤ i → IsIso ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS
            (openSubspaceSpace B S hS W hW).1
          (openSubspaceSpace B S hS W hW).2) i).map s)
```

## Tag 09IX, a lemma

[Tag 09IX](https://stacks.math.columbia.edu/tag/09IX) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isPerfect_retract_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectDirectSummandExtension.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectDirectSummandExtension.lean#L187).

> **Stacks 09IX.** Let `S` be a scheme, `X` a quasi-compact and quasi-separated algebraic space
> over `S`, `W` a quasi-compact open subspace of `X` and `P` a perfect object of `D(𝒪_W)`. Then `P`
> is a direct summand of the restriction `Q|_W` of a perfect object `Q` of `D(𝒪_X)`: there are
> `s : P ⟶ Q|_W` and `r : Q|_W ⟶ P` with `s ≫ r = 𝟙`.
>
> The induction of Stacks 09IT on the quasi-compact opens containing `W`, with
> `AlgebraicGeometry.Space.isSummandOfPerfectRestriction_step` as the inductive step.

```lean
theorem exists_isPerfect_retract_restrict (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS) (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1) (W : Subfunctor X.1)
    (hW : IsOpenSubspace B S hS W) (hWqc : IsQuasiCompactSpace B S hS W.toFunctor)
    (P : DerivedCategory (Modules.{u, u} B S hS (openSubspaceSpace B S hS W hW).1
      (openSubspaceSpace B S hS W hW).2))
    (hP : (smallEtaleRingedSite B S hS (openSubspaceSpace B S hS W hW).1
      (openSubspaceSpace B S hS W hW).2).IsPerfect P) :
    ∃ Q : DerivedCategory (Modules.{u, u} B S hS X.1 X.2),
      (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect Q ∧
      ∃ (s : P ⟶ (etaleModulePullback.{u, u} B S hS
          (ObjectProperty.homMk W.ι : openSubspaceSpace B S hS W hW ⟶ X)
          (isEtale_of_isOpenImmersion B S hS hW.2)).mapDerivedCategory.obj Q)
        (r : (etaleModulePullback.{u, u} B S hS
          (ObjectProperty.homMk W.ι : openSubspaceSpace B S hS W hW ⟶ X)
          (isEtale_of_isOpenImmersion B S hS hW.2)).mapDerivedCategory.obj Q ⟶ P),
        s ≫ r = 𝟙 P
```

**`AlgebraicGeometry.Space.exists_isPerfect_restrict_iso_biprod_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectDirectSummandRestriction.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectDirectSummandRestriction.lean#L72).

> **Stacks 09IX.** Let `S` be a scheme, `X` a quasi-compact and quasi-separated algebraic space
> over `S` and `W ⊆ X` a quasi-compact open subspace. Let `P` be a perfect object of `D(𝒪_W)`.
> Then `P` is a direct summand of the restriction of a perfect object of `D(𝒪_X)`: there are a
> perfect `R` in `D(𝒪_X)` and an object `C` of `D(𝒪_W)` with `R|_W ≅ P ⊕ C`. Both derived
> categories are taken at arbitrary models; quasi-separation is absolute, over the final object of
> the base category of schemes.

```lean
theorem exists_isPerfect_restrict_iso_biprod_of_isPerfect
    (X : AlgebraicSpaces B S hS) (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1)
    (W : Subfunctor X.1) (hW : IsOpenSubspace B S hS W)
    (hWqc : IsQuasiCompactSpace B S hS W.toFunctor)
    [hDX : HasDerivedCategory.{w} (Modules.{u, u} B S hS X.1 X.2)]
    [hDW : HasDerivedCategory.{w'} (Modules.{u, u} B S hS (openSubspaceSpace B S hS W hW).1
      (openSubspaceSpace B S hS W hW).2)]
    (P : DerivedCategory (Modules.{u, u} B S hS (openSubspaceSpace B S hS W hW).1
      (openSubspaceSpace B S hS W hW).2))
    (hP : (smallEtaleRingedSite B S hS (openSubspaceSpace B S hS W hW).1
      (openSubspaceSpace B S hS W hW).2).IsPerfect P) :
    ∃ R : DerivedCategory (Modules.{u, u} B S hS X.1 X.2),
      (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect R ∧
      ∃ C : DerivedCategory (Modules.{u, u} B S hS (openSubspaceSpace B S hS W hW).1
          (openSubspaceSpace B S hS W hW).2),
        Nonempty ((etaleModulePullback.{u, u} B S hS (openSubspaceHom B S hS W hW)
          (isEtale_openSubspaceHom B S hS W hW)).mapDerivedCategory.obj R ≅ P ⊞ C)
```

## Tag 09IY, a theorem

[Tag 09IY](https://stacks.math.columbia.edu/tag/09IY) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isPerfect_generator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectCompactQcqs.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectCompactQcqs.lean#L171).

> **Stacks 09IY.** Let `X` be a quasi-compact and quasi-separated algebraic space over `S`.
> There is a perfect object `P` of `D(𝒪_X)` such that an object `E` of `D_QCoh(𝒪_X)` is zero if and
> only if `Hom(P[n], E) = 0` for all `n ∈ ℤ`.
>
> The compact weak generator of `D_QCoh(𝒪_X)` of
> `AlgebraicGeometry.Space.exists_isCompactObject_isWeakTriangulatedGenerator_of_qcqs` is perfect by
> Stacks 09M8.

```lean
theorem exists_isPerfect_generator (X : AlgebraicSpaces B S hS)
    (hqc : IsQuasiCompactSpace B S hS X.1)
    (hqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1) :
    ∃ P : DerivedCategory (Modules.{u, u} B S hS X.1 X.2),
      (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect P ∧
        ∀ E : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2,
          IsZero E.obj ↔ ∀ n : ℤ, Subsingleton (P⟦n⟧ ⟶ E.obj)
```

**`AlgebraicGeometry.Space.exists_isPerfect_isZero_iff_forall_hom_shift_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/QcqsPerfectGenerator.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/QcqsPerfectGenerator.lean#L48).

> **Stacks 09IY.** Let `S` be a scheme and `X` a quasi-compact and quasi-separated algebraic
> space over `S`. The category `D_QCoh(𝒪_X)` is generated by a single perfect object: there is a
> perfect object `P` of `D(𝒪_X)` such that for `E` in `D_QCoh(𝒪_X)` the following are equivalent:
> (1) `E = 0`, (2) `Hom(P[n], E) = 0` for all `n ∈ ℤ`.

```lean
theorem exists_isPerfect_isZero_iff_forall_hom_shift_eq_zero (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u})) (X : AlgebraicSpaces B S hS)
    (hXqc : IsQuasiCompactSpace B S hS X.1) (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1) :
    ∃ P : DerivedCategory (Modules.{u, u} B S hS X.1 X.2),
      (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect P ∧
      ∀ E, qcohDerivedProp B S hS X E → (IsZero E ↔ ∀ (n : ℤ) (g : P⟦n⟧ ⟶ E), g = 0)
```

## Tag 0E4R, a remark

[Tag 0E4R](https://stacks.math.columbia.edu/tag/0E4R) in the Stacks Project.

**`AlgebraicGeometry.Space.tfae_reflectsIsomorphisms_quasicoherentDerivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPushforwardGenerator.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPushforwardGenerator.lean#L59). The attribute's comment: “the equivalence of (1), (2) and (3)”.

> **Stacks 0E4R.** Let `f : X ⟶ Y` be a quasi-compact and quasi-separated morphism of algebraic
> spaces and `E` a generator of `D_QCoh(𝒪_Y)`. The following are equivalent:
> 1. for `K` in `D_QCoh(𝒪_X)`, `Rf_*K = 0` if and only if `K = 0`;
> 2. `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` reflects isomorphisms;
> 3. `Lf^*E` is a generator of `D_QCoh(𝒪_X)`.

```lean
theorem tfae_reflectsIsomorphisms_quasicoherentDerivedPushforward (f : X ⟶ Y)
    (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (E : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2)
    (hE : ∀ K : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2,
      IsZero K ↔ ∀ n : ℤ, Subsingleton (E⟦n⟧ ⟶ K)) :
    List.TFAE [∀ K : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2,
        IsZero ((quasicoherentDerivedPushforward B S hS f hfqc hfqs).obj K) ↔ IsZero K,
      (quasicoherentDerivedPushforward B S hS f hfqc hfqs).ReflectsIsomorphisms,
      ∀ K : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2,
        IsZero K ↔ ∀ n : ℤ, Subsingleton (((quasicoherentDerivedModulePullback f).obj E)⟦n⟧ ⟶ K)]
```

**`AlgebraicGeometry.Space.isZero_quasicoherentDerivedPushforward_obj_iff_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPushforwardGenerator.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPushforwardGenerator.lean#L75). The attribute's comment: “the conditions hold if f is affine”.

> **Stacks 0E4R, the case of an affine morphism.** For `f` affine, `Rf_*K = 0` if and only if
> `K = 0`, for `K` in `D_QCoh(𝒪_X)`.

```lean
theorem isZero_quasicoherentDerivedPushforward_obj_iff_of_isAffineHom (f : X ⟶ Y)
    (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hf : IsAffineHom B S hS f.hom) (K : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2) :
    IsZero ((quasicoherentDerivedPushforward B S hS f hfqc hfqs).obj K) ↔ IsZero K
```

**`AlgebraicGeometry.Space.isZero_quasicoherentDerivedPushforward_obj_iff_of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPushforwardGenerator.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPushforwardGenerator.lean#L86). The attribute's comment: “the conditions hold if f is an open immersion”.

> **Stacks 0E4R, the case of an open immersion.** For an open immersion `j`, `Rj_*K = 0` if and
> only if `K = 0`: the restriction of `Rj_*K` to the open is `K`.

```lean
theorem isZero_quasicoherentDerivedPushforward_obj_iff_of_isOpenImmersion (f : X ⟶ Y)
    (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hf : IsOpenImmersion B S hS f.hom)
    (K : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2) :
    IsZero ((quasicoherentDerivedPushforward B S hS f hfqc hfqs).obj K) ↔ IsZero K
```

**`AlgebraicGeometry.Space.isZero_quasicoherentDerivedPushforward_obj_iff_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPushforwardGenerator.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPushforwardGenerator.lean#L103). The attribute's comment: “the conditions are stable under composition”.

> **Stacks 0E4R, compositions.** If `Rf_*` and `Rg_*` detect zero objects of `D_QCoh`, then
> so does `R(f ≫ g)_*`.

```lean
theorem isZero_quasicoherentDerivedPushforward_obj_iff_comp (f : X ⟶ Y) (g : Y ⟶ Z)
    (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hgqc : IsQuasiCompact B S hS g.hom) (hgqs : IsQuasiSeparated B S hS g.hom)
    (hfgqc : IsQuasiCompact B S hS (f ≫ g).hom) (hfgqs : IsQuasiSeparated B S hS (f ≫ g).hom)
    (hf : ∀ K : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2,
      IsZero ((quasicoherentDerivedPushforward B S hS f hfqc hfqs).obj K) ↔ IsZero K)
    (hg : ∀ K : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2,
      IsZero ((quasicoherentDerivedPushforward B S hS g hgqc hgqs).obj K) ↔ IsZero K)
    (K : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2) :
    IsZero ((quasicoherentDerivedPushforward B S hS (f ≫ g) hfgqc hfgqs).obj K) ↔ IsZero K
```

## Tag 0AEC, a lemma

[Tag 0AEC](https://stacks.math.columbia.edu/tag/0AEC) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isPerfect_generator_of_supported`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedPerfectGenerator.lean, line 393](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SupportedPerfectGenerator.lean#L393).

> **Stacks 0AEC.** Let `S` be a scheme, `X` a quasi-compact and quasi-separated algebraic space
> over `S`, and `T ⊆ |X|` a closed subset such that `|X| ∖ T` is quasi-compact. Then
> `D_{QCoh,T}(𝒪_X)` is generated by a single perfect object: there is a perfect object `P` of
> `D(𝒪_X)` with quasi-coherent cohomology supported on `T` (an object of `D_{QCoh,T}(𝒪_X)`) such that
> an object `E` of `D_QCoh(𝒪_X)` supported on `T` is zero if and only if `Hom(P[n], E) = 0` for all
> `n ∈ ℤ`.
>
> `D_{QCoh,T}(𝒪_X)` is the full subcategory of `D_QCoh(𝒪_X)` of the objects whose cohomology
> sheaves are supported on `T` (`AlgebraicGeometry.Space.CohomologySupportedOn`, Stacks 08GF);
> `|X| ∖ T` carries the topology of `|X|`.

```lean
theorem exists_isPerfect_generator_of_supported (X : AlgebraicSpaces B S hS)
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1)
    (T : Set (points B S hS X.1)) (hT : IsClosed T) (hTc : IsCompact Tᶜ) :
    ∃ P : DerivedCategory (Modules.{u, u} B S hS X.1 X.2),
      (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect P ∧
      DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))) P ∧
      CohomologySupportedOn B S hS X.1 X.2 T P ∧
      ∀ E : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2,
        CohomologySupportedOn B S hS X.1 X.2 T E.obj →
          (IsZero E.obj ↔ ∀ (n : ℤ) (g : P⟦n⟧ ⟶ E.obj), g = 0)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.15, Tag 09IU](https://stacks.math.columbia.edu/tag/09IU)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
