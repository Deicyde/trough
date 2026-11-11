---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_isZero_homology_derivedModulePushforward_baseChange, AlgebraicGeometry.Space.exists_isZero_homology_derivedModulePushforward, AlgebraicGeometry.Space.qcohDerived_derivedModulePushforward_obj, AlgebraicGeometry.Space.preservesCoproducts_quasicoherentDerivedPushforward, AlgebraicGeometry.Space.nonempty_representedQuasicoherentDerivedPullbackIso_and_pushforwardIso, AlgebraicGeometry.Space.reflectsIsomorphisms_affineQuasicoherentDerivedPushforward, AlgebraicGeometry.Space.isIso_affinePullPushMap
statement: formalized
proof: formalized
---

# 75.6 Total direct image

Section 75.6 of the Stacks Project, [Tag 08F9](https://stacks.math.columbia.edu/tag/08F9). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08FA, a lemma

[Tag 08FA](https://stacks.math.columbia.edu/tag/08FA) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isZero_homology_derivedModulePushforward_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPushforwardBound.lean, line 487](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPushforwardBound.lean#L487). The attribute's comment: “part (3)”.

> **Stacks 08FA, part (3).**  Let `f : X ⟶ Y` be a quasi-compact and quasi-separated morphism
> of algebraic spaces over `S`, with `Y` quasi-compact.  There is an integer `N` such that for every
> morphism of algebraic spaces `Y' ⟶ Y`, with base change `f' : X' ⟶ Y'` of `f`, and every `E` in
> `D_QCoh(𝒪_{X'})` with `H^m(E) = 0` for `m > 0`, we have `H^m(Rf'_*E) = 0` for `m ≥ N`.

```lean
theorem exists_isZero_homology_derivedModulePushforward_baseChange {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hY : IsQuasiCompactSpace B S hS Y.1) :
    ∃ N : ℤ, ∀ (Y' X' : AlgebraicSpaces B S hS) (g : Y' ⟶ Y) (g' : X' ⟶ X) (f' : X' ⟶ Y'),
      IsPullback g' f' f g →
      ∀ E : DerivedCategory (Modules.{u, u} B S hS X'.1 X'.2), QcohDerived B S hS X' E →
        (∀ m : ℤ, 0 < m → IsZero ((DerivedCategory.homologyFunctor _ m).obj E)) →
        ∀ m : ℤ, N ≤ m → IsZero ((DerivedCategory.homologyFunctor _ m).obj
          ((derivedModulePushforward B S hS f').obj E))
```

**`AlgebraicGeometry.Space.exists_isZero_homology_derivedModulePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPushforwardBound.lean, line 516](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPushforwardBound.lean#L516). The attribute's comment: “part (2)”.

> **Stacks 08FA, part (2).**  Let `f : X ⟶ Y` be a quasi-compact and quasi-separated morphism
> of algebraic spaces over `S`, with `Y` quasi-compact.  There is an integer `N` such that for every
> `E` in `D_QCoh(𝒪_X)` with `H^m(E) = 0` for `m > 0`, we have `H^m(Rf_*E) = 0` for `m ≥ N`.

```lean
theorem exists_isZero_homology_derivedModulePushforward {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hY : IsQuasiCompactSpace B S hS Y.1) :
    ∃ N : ℤ, ∀ E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2), QcohDerived B S hS X E →
      (∀ m : ℤ, 0 < m → IsZero ((DerivedCategory.homologyFunctor _ m).obj E)) →
      ∀ m : ℤ, N ≤ m → IsZero ((DerivedCategory.homologyFunctor _ m).obj
        ((derivedModulePushforward B S hS f).obj E))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.qcohDerived_derivedModulePushforward_obj`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedDirectImage.lean#L218), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPushforwardTags.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPushforwardTags.lean#L33) (StacksFrontier): “part (1)”.

## Tag 08FB, a lemma

[Tag 08FB](https://stacks.math.columbia.edu/tag/08FB) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.preservesCoproducts_quasicoherentDerivedPushforward`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPushforwardDirectSums.lean#L232), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPushforwardTags.lean, line 31](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDerivedPushforwardTags.lean#L31) (StacksFrontier).

## Tag 08GH, a remark

[Tag 08GH](https://stacks.math.columbia.edu/tag/08GH) in the Stacks Project.

**`AlgebraicGeometry.Space.nonempty_representedQuasicoherentDerivedPullbackIso_and_pushforwardIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RepresentedQuasicoherentDerivedSquare.lean, line 633](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RepresentedQuasicoherentDerivedSquare.lean#L633).

> **Stacks 08GH.** Let `g : T' ⟶ T` be a morphism of the big fppf site over `S`, so that
> `f = h_g : X' ⟶ X` is a morphism of representable algebraic spaces represented by the morphism of
> schemes `g_0 : X'_0 ⟶ X_0`.  Under the equivalences `D_QCoh(𝒪_{X_0}) ≌ D_QCoh(𝒪_X)` of
> Stacks 071Q,
>
> 1. `Lg_0^* : D_QCoh(𝒪_{X_0}) ⥤ D_QCoh(𝒪_{X'_0})` corresponds to
>    `Lf^* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_{X'})`, and
> 2. if `f` is quasi-compact and quasi-separated, `Rg_{0,*} : D_QCoh(𝒪_{X'_0}) ⥤ D_QCoh(𝒪_{X_0})`
>    corresponds to `Rf_* : D_QCoh(𝒪_{X'}) ⥤ D_QCoh(𝒪_X)`.

```lean
theorem nonempty_representedQuasicoherentDerivedPullbackIso_and_pushforwardIso :
    Nonempty (Stacks.Duality.quasiCoherentDerivedPullback' (B.inclusion.map g.left) ⋙
        (representedDualityQuasicoherentDerivedEquivalence B S hS T').functor ≅
      (representedDualityQuasicoherentDerivedEquivalence B S hS T).functor ⋙
        quasicoherentDerivedModulePullback (representedSpaceMap B S hS g)) ∧
    ∀ (hfqc : IsQuasiCompact B S hS (representedSpaceMap B S hS g).hom)
      (hfqs : IsQuasiSeparated B S hS (representedSpaceMap B S hS g).hom),
      Nonempty (Stacks.Duality.quasiCoherentDerivedPushforward (B.inclusion.map g.left)
          (isQuasicoherent_homology_derivedPushforward_representedSchemeMap g hfqc hfqs) ⋙
          (representedDualityQuasicoherentDerivedEquivalence B S hS T).functor ≅
        (representedDualityQuasicoherentDerivedEquivalence B S hS T').functor ⋙
          quasicoherentDerivedPushforward B S hS (representedSpaceMap B S hS g) hfqc hfqs)
```

## Tag 08II, a lemma

[Tag 08II](https://stacks.math.columbia.edu/tag/08II) in the Stacks Project.

**`AlgebraicGeometry.Space.reflectsIsomorphisms_affineQuasicoherentDerivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineDerivedPushforwardReflectsIsomorphisms.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineDerivedPushforwardReflectsIsomorphisms.lean#L327).

> **[Stacks, Tag 08II].**  Let `S` be a scheme and let `f : X ⟶ Y` be an affine morphism of
> algebraic spaces over `S`.  Then `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` reflects isomorphisms.
>
> Here `Rf_*` is any total right derived functor of the direct image of `𝒪_X`-modules, with its
> derivation unit `α`, restricted to `D_QCoh` as
> `AlgebraicGeometry.Space.affineQuasicoherentDerivedPushforward`.  The proof is
> `AlgebraicGeometry.Space.isIso_of_isIso_derivedModulePushforward_map_of_isAffineHom`: the cone `C`
> of a morphism `E ⟶ F` of `D_QCoh(𝒪_X)` lies in `D_QCoh(𝒪_X)`, `Rf_*C = 0` when `Rf_*` of the
> morphism is invertible, and `H^i(Rf_*C) = f_*H^i(C)` with `f_*` conservative on quasi-coherent
> modules forces `C = 0`.

```lean
theorem reflectsIsomorphisms_affineQuasicoherentDerivedPushforward :
    (affineQuasicoherentDerivedPushforward B S hS f hf Rf α).ReflectsIsomorphisms
```

## Tag 08IJ, a lemma

[Tag 08IJ](https://stacks.math.columbia.edu/tag/08IJ) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_affinePullPushMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineDerivedPullPush.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineDerivedPullPush.lean#L200).

> **Stacks 08IJ.** Let `f : X ⟶ Y` be an affine morphism of algebraic spaces over `S`. For `E`
> in `D_QCoh(𝒪_Y)` the canonical map `E ⊗^L f_*𝒪_X ⟶ Rf_*Lf^*E` is an isomorphism, so
> `Rf_*Lf^*E = E ⊗^L_{𝒪_Y} f_*𝒪_X`.

```lean
theorem isIso_affinePullPushMap (f : X ⟶ Y) (hf : IsAffineHom B S hS f.hom)
    (E : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS Y)))
    (hE : QcohDerived B S hS Y E) :
    IsIso (affinePullPushMap f hf E)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.6, Tag 08F9](https://stacks.math.columbia.edu/tag/08F9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
