---
declaration: section
origin: cited
lean: AlgebraicGeometry.AreSiblingsPerfectRegularSource, AlgebraicGeometry.AreSiblingsCoherent, AlgebraicGeometry.AreSiblingsPerfect, AlgebraicGeometry.exists_fourierMukai_areSiblingsCoherent, AlgebraicGeometry.nonempty_iso_of_areSiblings_of_isProjective, Stacks.AlgebraicGeometry.DerivedVarieties.Orlov.essImage_of_agree_on_zeroDimensional, Stacks.AlgebraicGeometry.DerivedVarieties.Orlov.exists_areSiblingsPerfect_of_fixes_zeroDimensional, Stacks.AlgebraicGeometry.DerivedVarieties.Orlov.exists_areSiblingsPerfectRegularSource_perfectFourierMukaiOver
statement: formalized
proof: formalized
---

# 57.12 Special functors

Section 57.12 of the Stacks Project, [Tag 0FZY](https://stacks.math.columbia.edu/tag/0FZY). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FZZ, a definition

[Tag 0FZZ](https://stacks.math.columbia.edu/tag/0FZZ) in the Stacks Project.

**`AlgebraicGeometry.AreSiblingsPerfectRegularSource`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/AutoequivalenceSiblings.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/AutoequivalenceSiblings.lean#L105). The attribute's comment: “the case of a regular source: siblings of exact functors `D_perf(𝒪_X) ⥤ D_perf(𝒪_Y)` for `X` quasi-compact regular and `Y` Noetherian”.

> **Stacks Project, Tag 0FZZ, for a regular source.** If `X` is regular then
> `D_perf(𝒪_X) = D^b_Coh(𝒪_X)` by [Stacks, Tag 0FDC], and the source uses the same terminology for
> exact functors `D_perf(𝒪_X) ⥤ D_perf(𝒪_Y)`, with no hypothesis on `Y` beyond the standing one: two
> such functors are **siblings** if they are siblings as exact functors
> `D^b_Coh(𝒪_X) ⥤ D^b_Coh(𝒪_Y)`, after precomposition with `D^b_Coh(𝒪_X) = D_perf(𝒪_X)` and
> composition with the inclusion `D_perf(𝒪_Y) ⊆ D^b_Coh(𝒪_Y)` of [Stacks, Tag 0FXU] (`Y`
> Noetherian, as a scheme of finite type over a field is). For `Y` regular as well this is
> `AlgebraicGeometry.AreSiblingsPerfect`
> (`AlgebraicGeometry.areSiblingsPerfect_iff_areSiblingsPerfectRegularSource`).

```lean
def _root_.AlgebraicGeometry.AreSiblingsPerfectRegularSource : Prop
```

**`AlgebraicGeometry.AreSiblingsCoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SiblingFunctors/BoundedCoherent.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SiblingFunctors/BoundedCoherent.lean#L195). The attribute's comment: “siblings of exact functors between the bounded coherent derived categories”.

> **Stacks Project, Tag 0FZZ.** Two exact functors `D^b_Coh(𝒪_X) ⥤ D^b_Coh(𝒪_Y)` are
> **siblings**, or `F'` is a **sibling** of `F`, if they are siblings in the sense of
> [Stacks, Tag 0FZT] for the abelian category `Coh(𝒪_X)`: their restrictions along the comparison
> functor `D^b(Coh(𝒪_X)) ⥤ D^b_Coh(𝒪_X)` of the identification `D^b_Coh(𝒪_X) = D^b(Coh(𝒪_X))` of
> [Stacks, Tag 0FDB] are siblings, that is, they agree up to natural isomorphism on the coherent
> modules and up to isomorphism at each object.

```lean
def AreSiblingsCoherent : Prop
```

**`AlgebraicGeometry.AreSiblingsPerfect`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SiblingFunctors/BoundedCoherent.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SiblingFunctors/BoundedCoherent.lean#L282). The attribute's comment: “the regular case: siblings of exact functors between the perfect derived categories of quasi-compact regular schemes”.

> **Stacks Project, Tag 0FZZ, the regular case.** On quasi-compact regular schemes
> `D_perf(𝒪_X) = D^b_Coh(𝒪_X)` by [Stacks, Tag 0FDC], and the same terminology is used for exact
> functors `D_perf(𝒪_X) ⥤ D_perf(𝒪_Y)`: two of them are **siblings** if they are siblings as exact
> functors `D^b_Coh(𝒪_X) ⥤ D^b_Coh(𝒪_Y)` after being moved there along that identification, which
> on each of the two schemes is the inclusion of one of the two subcategories into the other.

```lean
def AreSiblingsPerfect : Prop
```

## Tag 0G00, a lemma

[Tag 0G00](https://stacks.math.columbia.edu/tag/0G00) in the Stacks Project.

**`AlgebraicGeometry.exists_fourierMukai_areSiblingsCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SiblingFunctors/FourierMukaiSibling.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SiblingFunctors/FourierMukaiSibling.lean#L269). The attribute's comment: “a k-linear exact functor of D^b\_Coh sending Coh into Coh has a sibling which is the Fourier-Mukai functor of a coherent kernel flat over X with support finite over Y”.

> Let `k` be a field, let `X` and `Y` be schemes of finite type over `k` with `X` separated, and
> let `F : D^b_Coh(𝒪_X) ⥤ D^b_Coh(𝒪_Y)` be a `k`-linear exact functor sending
> `Coh(𝒪_X) ⊂ D^b_Coh(𝒪_X)` into `Coh(𝒪_Y) ⊂ D^b_Coh(𝒪_Y)`. Then there exists a Fourier-Mukai
> functor `F' : D^b_Coh(𝒪_X) ⥤ D^b_Coh(𝒪_Y)` whose kernel is a coherent `𝒪_{X ×_k Y}`-module `𝒦`
> flat over `X` and with support finite over `Y` which is a sibling of `F`.
>
> Finite type over `k` is `LocallyOfFiniteType` together with `QuasiCompact`; `X ×_k Y` is the
> fibre product over `Spec k`. The kernel `𝒦` is an object of
> `AlgebraicGeometry.CoherentKernels.finiteFlatCoherentKernel` — coherent, flat over `X`, with
> scheme-theoretic support finite over `Y` — and `F'` is the functor induced on `D^b_Coh` by the
> Fourier-Mukai functor `Φ_𝒦` of the complex `𝒦[0]`, which preserves `D^b_Coh`
> (`fourierMukaiOfKernel`). That `F` sends coherent modules to coherent modules is the statement
> that the image under `F` of a coherent module placed in degree zero is isomorphic to a coherent
> module placed in degree zero; `k`-linearity is with respect to the `k`-linear structures induced
> by the structure morphisms.

```lean
theorem exists_fourierMukai_areSiblingsCoherent [IsSeparated X.hom]
    (F : (DerivedCategoryB.derivedCategoryBBounded (coherentInModules X.left)).FullSubcategory ⥤
      (DerivedCategoryB.derivedCategoryBBounded (coherentInModules Y.left)).FullSubcategory)
    [F.CommShift ℤ] [F.IsTriangulated]
    (hlin : letI : Linear k (SheafOfModules.{u} X.left.ringCatSheaf) := modulesLinear k X
      letI : Linear k (SheafOfModules.{u} Y.left.ringCatSheaf) := modulesLinear k Y
      F.Linear k)
    (hF : ∀ A, (boundedCoherentSingleFunctor Y.left).essImage
      (F.obj ((boundedCoherentSingleFunctor X.left).obj A))) :
    ∃ K : (finiteFlatCoherentKernel k X Y).FullSubcategory,
      AreSiblingsCoherent F (fourierMukaiOfKernel k X Y K)
```

## Tag 0G01, a remark

[Tag 0G01](https://stacks.math.columbia.edu/tag/0G01) in the Stacks Project.

**`AlgebraicGeometry.nonempty_iso_of_areSiblings_of_isProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/TwistOfFixing.lean, line 739](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/TwistOfFixing.lean#L739). The attribute's comment: “first sentence: siblings out of D^b\_Coh of a reduced projective scheme over a field, the first fully faithful, are isomorphic; the remaining sentences are commentary”.

> **Stacks Project, Tag 0G01**, its first sentence. Let `k` be a field and `X` a reduced scheme
> which is projective over `k` (`AlgebraicGeometry.IsProjective` of `f : X ⟶ Spec k`, the first
> condition of [Stacks, Tag 01W8]). If `F, F' : D^b_Coh(𝒪_X) ⥤ 𝒟` are siblings and `F` is fully
> faithful, then `F ≅ F'`. Here `𝒟` is an arbitrary triangulated category and "siblings" is the
> relation of [Stacks, Tag 0FZT] for `Coh(𝒪_X)`, read through the identification
> `D^b(Coh(𝒪_X)) = D^b_Coh(𝒪_X)` of [Stacks, Tag 0FDB].
>
> A projective `k`-scheme is proper over `k` with an ample invertible module
> (`AlgebraicGeometry.IsProjective.isProper_and_exists_isAmple_of_isAffine`), and for those this is
> `AlgebraicGeometry.nonempty_iso_of_areSiblings_coherentToModulesDerivedBounded`, the source's
> argument "via the proof of [Stacks, Tag 0G0C]". The remaining sentences of the remark (that
> siblings are not known to be isomorphic in general, the case of [Stacks, Tag 0G00], the reference
> to Noah's work and the invitation to email) are commentary, with no mathematical content to
> formalize.

```lean
theorem _root_.AlgebraicGeometry.nonempty_iso_of_areSiblings_of_isProjective
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    (hf : AlgebraicGeometry.IsProjective f) [IsReduced X]
    {D : Type*} [Category* D] [HasZeroObject D] [HasShift D ℤ] [Preadditive D]
    [∀ n : ℤ, (shiftFunctor D n).Additive] [Pretriangulated D] [IsTriangulated D]
    (F F' : (DerivedCategoryB.derivedCategoryBBounded (coherentInModules X)).FullSubcategory ⥤ D)
    [F.CommShift ℤ] [F.IsTriangulated] [F'.CommShift ℤ] [F'.IsTriangulated]
    (h : AreSiblings (coherentToModulesDerivedBounded X ⋙ F)
      (coherentToModulesDerivedBounded X ⋙ F'))
    (hF : Nonempty F.FullyFaithful) : Nonempty (F ≅ F')
```

## Tag 0GX0, a lemma

[Tag 0GX0](https://stacks.math.columbia.edu/tag/0GX0) in the Stacks Project.

**`Stacks.AlgebraicGeometry.DerivedVarieties.Orlov.essImage_of_agree_on_zeroDimensional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/EssentialImage.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/EssentialImage.lean#L121).

> Let `k` be a field and let `X`, `Y` be proper schemes over `k` with
> `X` regular. Let `F, G : D_perf(𝒪_X) ⥤ D_perf(𝒪_Y)` be `k`-linear exact functors such that
> (1) `F(𝓕) ≅ G(𝓕)` for every coherent `𝒪_X`-module `𝓕` with `dim Supp(𝓕) = 0`, and (2) `F` is
> fully faithful. Then the essential image of `G` is contained in the essential image of `F`.
>
> The coherent module `𝓕` is read in `D_perf(𝒪_X)` placed in degree zero; the hypothesis asks for
> the isomorphism for every proof that it is perfect, which is automatic on a regular scheme
> (`isPerfect_single_of_isCoherent`).

```lean
theorem essImage_of_agree_on_zeroDimensional (hX : IsRegular X.left)
    (F G : PerfectDerivedCategory X.left ⥤ PerfectDerivedCategory Y.left)
    [F.CommShift ℤ] [F.IsTriangulated] [F.Linear k] [G.CommShift ℤ] [G.IsTriangulated]
    [G.Linear k]
    (hagree : ∀ (M : X.left.Modules), M.IsCoherent →
      topologicalKrullDim (SheafOfModules.supp M) = 0 →
      ∀ (hM : IsPerfect (X := X.left.toRingedSpace)
          ((DerivedCategory.singleFunctor X.left.Modules 0).obj M)),
        Nonempty (F.obj (⟨_, hM⟩ : PerfectDerivedCategory X.left) ≅
          G.obj (⟨_, hM⟩ : PerfectDerivedCategory X.left)))
    (hFF : Nonempty F.FullyFaithful) (E : PerfectDerivedCategory X.left) :
    F.essImage (G.obj E)
```

## Tag 0G27, a lemma

[Tag 0G27](https://stacks.math.columbia.edu/tag/0G27) in the Stacks Project.

**`Stacks.AlgebraicGeometry.DerivedVarieties.Orlov.exists_areSiblingsPerfect_of_fixes_zeroDimensional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/TwistOfFixing.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/TwistOfFixing.lean#L145).

> **[Stacks, Tag 0G27].** Let `k` be a field, let `X` be a proper scheme over `k` which is
> regular, and let `F : D_perf(𝒪_X) ⥤ D_perf(𝒪_X)` be a `k`-linear exact functor. Assume that for
> every coherent `𝒪_X`-module `𝓕` with `dim Supp(𝓕) = 0` there is an isomorphism `𝓕 ≅ F(𝓕)`. Then
> there exist an automorphism `f : X ⟶ X` over `k` which induces the identity on the underlying
> topological space and an invertible `𝒪_X`-module `ℒ` such that `F` and
> `F'(M) = Lf^*M ⊗^𝐋_{𝒪_X} ℒ` are siblings.
>
> Here `F'` is `perfectPullbackDerivedTensor f.hom ℒ` and "siblings" is
> `AlgebraicGeometry.AreSiblingsPerfect` ([Stacks, Tag 0FZZ]: siblings as functors on
> `D_perf = D^b_Coh`, `X` being regular). `F` is fully faithful by [Stacks, Tag 0G26] and essentially
> surjective by [Stacks, Tag 0GX0], and the rest of the source's proof is
> `exists_areSiblingsPerfect_of_fullyFaithful_of_essSurj`.

```lean
theorem exists_areSiblingsPerfect_of_fixes_zeroDimensional (hX : IsRegular X.left)
    (F : PerfectDerivedCategory X.left ⥤ PerfectDerivedCategory X.left) [F.CommShift ℤ]
    [F.IsTriangulated]
    (hlin : letI : Linear k X.left.Modules := modulesLinear k X; F.Linear k)
    (hfix : ∀ (𝓕 : X.left.Modules), 𝓕.IsCoherent →
      topologicalKrullDim (SheafOfModules.supp 𝓕) = 0 →
      ∀ h𝓕 : IsPerfect (X := X.left.toRingedSpace)
          ((DerivedCategory.singleFunctor X.left.Modules 0).obj 𝓕),
        Nonempty ((F.obj ⟨_, h𝓕⟩).obj ≅ (DerivedCategory.singleFunctor X.left.Modules 0).obj 𝓕)) :
    haveI : IsNoetherian X.left := isNoetherian_of_locallyOfFiniteType X.hom
    ∃ (f : X.left ≅ X.left) (L : X.left.Modules)
      (hL : Stacks.SheafOfModules.IsInvertible X.left.presheaf X.left.ringCatSheaf.2 L),
      f.hom ≫ X.hom = X.hom ∧ (∀ x : X.left, f.hom x = x) ∧
      @AreSiblingsPerfect X.left X.left hX hX _ _ F
        (perfectPullbackDerivedTensor f.hom L (isPerfect_single_of_isInvertible hX L hL))
        ‹_› ‹_›
        (show (perfectPullbackDerivedTensor f.hom L
          (isPerfect_single_of_isInvertible hX L hL)).CommShift ℤ from inferInstance)
        (show (perfectPullbackDerivedTensor f.hom L
          (isPerfect_single_of_isInvertible hX L hL)).IsTriangulated from inferInstance)
```

## Tag 0G06, a lemma

[Tag 0G06](https://stacks.math.columbia.edu/tag/0G06) in the Stacks Project.

**`Stacks.AlgebraicGeometry.DerivedVarieties.Orlov.exists_areSiblingsPerfectRegularSource_perfectFourierMukaiOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/TwistOfFixing.lean, line 392](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/TwistOfFixing.lean#L392).

> **[Stacks, Tag 0G06].** Let `k` be a field, let `X`, `Y` be proper schemes over `k` with `X`
> regular, and let `F, G : D_perf(𝒪_X) ⥤ D_perf(𝒪_Y)` be `k`-linear exact functors such that
> (1) `F(𝓕) ≅ G(𝓕)` for every coherent `𝒪_X`-module `𝓕` with `dim Supp(𝓕) = 0`, (2) `F` is fully
> faithful, and (3) `G` is a Fourier-Mukai functor whose kernel is in `D_perf(𝒪_{X × Y})`. Then
> there is a Fourier-Mukai functor `F' : D_perf(𝒪_X) ⥤ D_perf(𝒪_Y)` whose kernel is in
> `D_perf(𝒪_{X × Y})` such that `F` and `F'` are siblings.
>
> Here (3) reads: `G` is naturally isomorphic to `Φ_P = perfectFourierMukaiOver k X Y hP` for a
> perfect `P` on `X ×_k Y`; the conclusion gives `F' = Φ_{P'}` itself, and "siblings" is
> `AlgebraicGeometry.AreSiblingsPerfectRegularSource` ([Stacks, Tag 0FZZ] for a regular `X` and an
> arbitrary `Y` of finite type over `k`).
>
> The proof is the source's. By [Stacks, Tag 0GX0] the essential image of `G` lies in that of `F`.
> Let `R` be the exact right adjoint of `F` ([Stacks, Tag 0FYN]); `F` being fully faithful,
> `H = R ∘ G` satisfies `F ∘ H ≅ G` and fixes the zero-dimensional sheaves, so by
> [Stacks, Tag 0G27] it is a sibling of `H'(M) = Lf^*M ⊗^𝐋 ℒ` for an automorphism `f` of `X` over
> `k` and an invertible `ℒ`. With `T(M) = L(f⁻¹)^*(M ⊗^𝐋 ℒ^∨)`, `H' ∘ T ≅ 𝟭`, `T` preserves
> coherent modules, and `G ∘ T` is the Fourier-Mukai functor of the twisted kernel
> `P' = L pr_1^*ℒ^∨ ⊗^𝐋 L(f × 𝟙)^* P`. Then `F ≅ F ∘ H' ∘ T` is a sibling of
> `F ∘ H ∘ T ≅ G ∘ T ≅ Φ_{P'}`.

```lean
theorem exists_areSiblingsPerfectRegularSource_perfectFourierMukaiOver (hX : IsRegular X.left)
    (F G : PerfectDerivedCategory X.left ⥤ PerfectDerivedCategory Y.left)
    [F.CommShift ℤ] [F.IsTriangulated] [G.CommShift ℤ] [G.IsTriangulated]
    (hFlin : letI : Linear k X.left.Modules := modulesLinear k X
      letI : Linear k Y.left.Modules := modulesLinear k Y
      F.Linear k)
    (hGlin : letI : Linear k X.left.Modules := modulesLinear k X
      letI : Linear k Y.left.Modules := modulesLinear k Y
      G.Linear k)
    (hagree : ∀ (M : X.left.Modules), M.IsCoherent →
      topologicalKrullDim (SheafOfModules.supp M) = 0 →
      ∀ (hM : IsPerfect (X := X.left.toRingedSpace)
          ((DerivedCategory.singleFunctor X.left.Modules 0).obj M)),
        Nonempty (F.obj (⟨_, hM⟩ : PerfectDerivedCategory X.left) ≅
          G.obj (⟨_, hM⟩ : PerfectDerivedCategory X.left)))
    (hFF : Nonempty F.FullyFaithful)
    (hG : haveI : IsNoetherian Y.left := isNoetherian_of_locallyOfFiniteType Y.hom
      ∃ (P : DerivedCategory (pullback X.hom Y.hom).Modules)
        (hP : IsPerfect (X := (pullback X.hom Y.hom).toRingedSpace) P),
        Nonempty (G ≅ perfectFourierMukaiOver k X Y hP)) :
    haveI : IsNoetherian X.left := isNoetherian_of_locallyOfFiniteType X.hom
    haveI : IsNoetherian Y.left := isNoetherian_of_locallyOfFiniteType Y.hom
    ∃ (P' : DerivedCategory (pullback X.hom Y.hom).Modules)
      (hP' : IsPerfect (X := (pullback X.hom Y.hom).toRingedSpace) P'),
      @AreSiblingsPerfectRegularSource X.left Y.left hX _ _ F (perfectFourierMukaiOver k X Y hP')
        ‹_› ‹_›
        (@commShift_fourierMukaiOn _ _ _ X.hom Y.hom _ _ _
          (isTriangulated_perfectInModules X.left) (isTriangulated_perfectInModules Y.left) _)
        (@isTriangulated_fourierMukaiOn _ _ _ X.hom Y.hom _ _ _
          (isTriangulated_perfectInModules X.left) (isTriangulated_perfectInModules Y.left) _)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 57.12, Tag 0FZY](https://stacks.math.columbia.edu/tag/0FZY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
