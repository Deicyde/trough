---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_diag_iff_forall_yoneda, AlgebraicGeometry.Space.forall_yoneda_isRepresentableByAlgebraicSpaces_iff_isAlgebraicSpace, AlgebraicGeometry.Space.relativelyRepresentable_separated_locallyQuasiFinite_of_isPullback, AlgebraicGeometry.Space.relativelyRepresentable_diag_of_flat_presentation, AlgebraicGeometry.Space.relativelyRepresentable_of_isLocallyQuasiFinite_of_schemeSource
statement: formalized
proof: formalized
---

# 80.5 Bootstrapping the diagonal

Section 80.5 of the Stacks Project, [Tag 046I](https://stacks.math.columbia.edu/tag/046I). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03Y2, a lemma

[Tag 03Y2](https://stacks.math.columbia.edu/tag/03Y2) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_diag_iff_forall_yoneda`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Diagonal.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Diagonal.lean#L318). The attribute's comment: “conditions (1) and (2)”.

> **Stacks 03Y2, conditions (1) and (2).** The absolute diagonal of a presheaf on the big
> fppf site of `S` is representable by algebraic spaces exactly when every morphism to that
> presheaf from a scheme over `S` is representable by algebraic spaces.

```lean
theorem isRepresentableByAlgebraicSpaces_diag_iff_forall_yoneda
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) :
    IsRepresentableByAlgebraicSpaces B S hS (diag F) ↔
      ∀ (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ F),
        IsRepresentableByAlgebraicSpaces B S hS f
```

**`AlgebraicGeometry.Space.forall_yoneda_isRepresentableByAlgebraicSpaces_iff_isAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Diagonal.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Diagonal.lean#L342). The attribute's comment: “conditions (2) and (3)”.

> **Stacks 03Y2, conditions (2) and (3).** Representability by algebraic spaces of every
> morphism to a presheaf on the big fppf site of `S` from a scheme over `S` is equivalent to
> representability by algebraic spaces of every morphism to it from an algebraic space over
> `S`.

```lean
theorem forall_yoneda_isRepresentableByAlgebraicSpaces_iff_isAlgebraicSpace
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) :
    (∀ (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ F),
        IsRepresentableByAlgebraicSpaces B S hS f) ↔
      ∀ (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS X →
        ∀ (f : X ⟶ F), IsRepresentableByAlgebraicSpaces B S hS f
```

## Tag 046J, a lemma

[Tag 046J](https://stacks.math.columbia.edu/tag/046J) in the Stacks Project.

**`AlgebraicGeometry.Space.relativelyRepresentable_separated_locallyQuasiFinite_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/SeparatedQuasiFiniteDescent.lean, line 480](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/SeparatedQuasiFiniteDescent.lean#L480).

> **Stacks 046J**, conditional only on the fppf locality of separatedness.
>
> In a cartesian square of sheaves on the big fppf site of `S` whose right-hand column `g` is
> representable by algebraic spaces, surjective, flat and locally of finite presentation and
> whose top row `a` is representable by algebraic spaces, separated and locally quasi-finite,
> the bottom row `b` is representable by objects of the site, separated and locally
> quasi-finite.
>
> Representability of `b` by objects of the site is
> `AlgebraicGeometry.Space.relativelyRepresentable_of_isPullback_of_flat_surjective`, the
> source's own argument by effective fppf descent of schemes.  Separatedness and local
> quasi-finiteness descend by Stacks 0421 and Stacks 0427, each read at the fppf precoverage
> from its fpqc form.

```lean
theorem relativelyRepresentable_separated_locallyQuasiFinite_of_isPullback
    {E F H G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (a : E ⟶ F) (f : E ⟶ H) (g : F ⟶ G) (b : H ⟶ G) (sq : IsPullback a f g b)
    (hH : Presheaf.IsSheaf (BigFppfOver.topology B S hS) H)
    (hG : Presheaf.IsSheaf (BigFppfOver.topology B S hS) G)
    (hgRep : IsRepresentableByAlgebraicSpaces B S hS g)
    (hgSurj : HasProperty B S hS (surjectiveMorphismProperty B S hS) g hgRep)
    (hgFlat : HasProperty B S hS (flatProperty B S hS) g hgRep)
    (hgLfp : HasProperty B S hS (locallyOfFinitePresentationProperty B S hS) g hgRep)
    (haRep : IsRepresentableByAlgebraicSpaces B S hS a)
    (haSep : HasProperty B S hS (separatedProperty B S hS) a haRep)
    (haLqf : HasProperty B S hS (locallyQuasiFiniteProperty B S hS) a haRep) :
    ∃ hbRep : IsRepresentableByAlgebraicSpaces B S hS b,
      yoneda.relativelyRepresentable b ∧
        HasProperty B S hS (separatedProperty B S hS) b hbRep ∧
          HasProperty B S hS (locallyQuasiFiniteProperty B S hS) b hbRep
```

## Tag 046K, a lemma

[Tag 046K](https://stacks.math.columbia.edu/tag/046K) in the Stacks Project.

**`AlgebraicGeometry.Space.relativelyRepresentable_diag_of_flat_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Diagonal.lean, line 441](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Diagonal.lean#L441).

> **Stacks 046K.** Let `F` be a sheaf on the big fppf site of a scheme `S` which admits a
> morphism `f : X ⟶ F` from an algebraic space over `S` that is representable by algebraic
> spaces, surjective, flat and locally of finite presentation.  Then the absolute diagonal
> `Δ_F : F ⟶ F × F` is representable *by objects of the site*, that is, every fibre product of
> `Δ_F` with a scheme-valued point of `F × F` is again a scheme over `S` — not merely an
> algebraic space, as **Stacks 03Y2** would give.
>
> Let `d = Δ_F` and let `k = f × f : X ⨯ X ⟶ F × F`, which is representable by algebraic spaces,
> surjective, flat and locally of finite presentation by **Stacks 046D** and **Stacks 046H**.  The
> fibre product `W = (X ⨯ X) ×_{F × F} F` is the kernel pair `X ×_F X` of `f`, so its projection
> to `X ⨯ X` is representable by algebraic spaces, separated and locally quasi-finite.  Given a
> scheme-valued point `η : h_T ⟶ F × F`, the base change `T' = h_T ×_{F × F} (X ⨯ X) ⟶ h_T` of
> `k` inherits the three properties by **Stacks 046F**, and `T' ×_{X ⨯ X} W ⟶ T'` inherits
> separatedness and local quasi-finiteness from the projection of `W`; that fibre product is at
> the same time the base change of `Z = h_T ×_{F × F} F ⟶ h_T` along `T' ⟶ h_T`.  **Stacks 046J**
> applied to the resulting cartesian square makes `Z ⟶ h_T` representable by objects of the site,
> and `Z` is the fibre product of `Δ_F` with `η`.

```lean
theorem relativelyRepresentable_diag_of_flat_presentation
    {F X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : Presheaf.IsSheaf (BigFppfOver.topology B S hS) F)
    (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ F)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f)
    (hfSurj : HasProperty B S hS (surjectiveMorphismProperty B S hS) f hf)
    (hfFlat : HasProperty B S hS (flatProperty B S hS) f hf)
    (hfLfp : HasProperty B S hS (locallyOfFinitePresentationProperty B S hS) f hf) :
    yoneda.relativelyRepresentable (diag F)
```

## Tag 0AHV, a lemma

[Tag 0AHV](https://stacks.math.columbia.edu/tag/0AHV) in the Stacks Project.

**`AlgebraicGeometry.Space.relativelyRepresentable_of_isLocallyQuasiFinite_of_schemeSource`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/LocallyQuasiFiniteFromScheme.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/LocallyQuasiFiniteFromScheme.lean#L93).

> **Stacks 0AHV.** Let `F` be a presheaf of sets on the big fppf site of `S` and let `X` be a
> scheme over `S`, that is an object of the site. A morphism `a : h_X ⟶ F` which is representable
> by algebraic spaces and locally quasi-finite is representable by schemes.
>
> The hypothesis of local quasi-finiteness is the one of Stacks 03XZ: every base change of `a`
> along a scheme-valued point of `F` is a locally quasi-finite morphism of algebraic spaces
> over `S`.

```lean
theorem relativelyRepresentable_of_isLocallyQuasiFinite_of_schemeSource
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (X : BigFppfOver B S hS) (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (a : yoneda.obj X ⟶ F)
    (ha : IsRepresentableByAlgebraicSpaces B S hS a)
    (hlqf : HasProperty B S hS
      (fun ⦃_ _⦄ φ => IsLocallyQuasiFinite B S hS φ.hom) a ha) :
    yoneda.relativelyRepresentable a
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 80.5, Tag 046I](https://stacks.math.columbia.edu/tag/046I)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
