---
declaration: section
origin: cited
lean: Stacks.RelativeSpec.relativeSpecFunctor, relativeSpecFunctor, Stacks.RelativeSpec.algebraPullback_nonempty, Stacks.RelativeSpec.relativeSpecFunctorPullbackToOriginal_base, Stacks.RelativeSpec.relativeSpecFunctorPullbackToOriginal_algebra, Stacks.RelativeSpec.relativeSpecFunctor_pullback_iso_pullback, Stacks.RelativeSpec.relativeSpecFunctor_pullback_iso_pullback_fst, Stacks.RelativeSpec.relativeSpecFunctor_pullback_iso_pullback_snd
statement: formalized
proof: formalized
---

# 27.4 Relative spectrum as a functor

Section 27.4 of the Stacks Project, [Tag 01LQ](https://stacks.math.columbia.edu/tag/01LQ). 8 tags here are carried by 26 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01LR, an equation

[Tag 01LR](https://stacks.math.columbia.edu/tag/01LR) in the Stacks Project.

**`Stacks.RelativeSpec.relativeSpecFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpecRepresentability/Basic.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpecRepresentability/Basic.lean#L283).

> The contravariant functor sending a test scheme `T` to the pairs
> `(f : T ⟶ X, φ : A ⟶ f_* 𝒪_T)` and a morphism of test schemes to pullback of such pairs.

```lean
noncomputable def relativeSpecFunctor (s : RelativeSpecSituation.{u}) :
    Scheme.{u}ᵒᵖ ⥤ Type u
```

Declarations registered for the tag:

- [`relativeSpecFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=relativeSpecFunctor#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/RelativeSpec/FunctorOfPoints.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/FunctorOfPoints.lean#L97) (StacksFrontier).

## Tag 01LS, a lemma

[Tag 01LS](https://stacks.math.columbia.edu/tag/01LS) in the Stacks Project.

**`Stacks.RelativeSpec.algebraPullback_nonempty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/BaseChange.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/BaseChange.lean#L129). The attribute's comment: “existence of the pulled-back algebra”.

> **Stacks Project, Tag 01LS.** Extension of scalars of a quasi-coherent algebra sheaf along
> any morphism of schemes exists and is quasi-coherent.

```lean
theorem algebraPullback_nonempty : Nonempty (AlgebraPullback s g)
```

**`Stacks.RelativeSpec.relativeSpecFunctorPullbackToOriginal_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/BaseChange.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/BaseChange.lean#L233). The attribute's comment: “base component of the canonical map to the original functor”.

> **Stacks Project, Tag 01LS.** On a test scheme, the canonical map composes the structural
> morphism with the base-change morphism.

```lean
theorem relativeSpecFunctorPullbackToOriginal_base {T : Scheme.{u}}
    (p : RelativeSpecPair (pullbackAlgebra s g).situation T) :
    ((relativeSpecFunctorPullbackToOriginal s g).app (.op T) p).1 = p.1 ≫ g
```

**`Stacks.RelativeSpec.relativeSpecFunctorPullbackToOriginal_algebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/BaseChange.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/BaseChange.lean#L240). The attribute's comment: “algebra component of the canonical map to the original functor”.

> **Stacks Project, Tag 01LS.** The algebra component of the canonical map is obtained from
> the transpose of `g⁻¹A ⟶ g⁺A`, then pushed forward along the test-scheme map.

```lean
theorem relativeSpecFunctorPullbackToOriginal_algebra {T : Scheme.{u}}
    (p : RelativeSpecPair (pullbackAlgebra s g).situation T) :
    HEq ((relativeSpecFunctorPullbackToOriginal s g).app (.op T) p).2.right
      (((TopCat.Sheaf.pullbackPushforwardAdjunction CommRingCat g.base).homEquiv
          s.algebra.right (pullbackAlgebra s g).algebra.right
          (pullbackAlgebra s g).map).hom ≫
        (TopCat.Presheaf.pushforward CommRingCat g.base).map p.2.right)
```

**`Stacks.RelativeSpec.relativeSpecFunctor_pullback_iso_pullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/BaseChange.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/BaseChange.lean#L330). The attribute's comment: “canonical base-change isomorphism”.

> **Stacks Project, Tag 01LS.** Formation of the relative spectrum functor commutes with
> arbitrary base change.

```lean
noncomputable def relativeSpecFunctor_pullback_iso_pullback :
    relativeSpecFunctor (pullbackAlgebra s g).situation ≅
      pullback (yoneda.map g) (relativeSpecFunctorToBase s)
```

**`Stacks.RelativeSpec.relativeSpecFunctor_pullback_iso_pullback_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/BaseChange.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/BaseChange.lean#L338). The attribute's comment: “first component of the canonical isomorphism”.

> **Stacks Project, Tag 01LS.** The first component of the canonical base-change isomorphism
> remembers the map from a test scheme to the new base.

```lean
theorem relativeSpecFunctor_pullback_iso_pullback_fst :
    (relativeSpecFunctor_pullback_iso_pullback s g).hom ≫
        pullback.fst (yoneda.map g) (relativeSpecFunctorToBase s) =
      relativeSpecFunctorToBase (pullbackAlgebra s g).situation
```

**`Stacks.RelativeSpec.relativeSpecFunctor_pullback_iso_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/BaseChange.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/BaseChange.lean#L347). The attribute's comment: “second component of the canonical isomorphism”.

> **Stacks Project, Tag 01LS.** The second component of the isomorphism is the canonical
> transformation induced by the algebra pullback map.

```lean
theorem relativeSpecFunctor_pullback_iso_pullback_snd :
    (relativeSpecFunctor_pullback_iso_pullback s g).hom ≫
        pullback.snd (yoneda.map g) (relativeSpecFunctorToBase s) =
      relativeSpecFunctorPullbackToOriginal s g
```

**`Stacks.RelativeSpec.RelativeSpecSituation.baseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/FunctorBaseChange.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/FunctorBaseChange.lean#L153). The attribute's comment: “the base-changed situation (S', g^*A)”.

> **Stacks Project, Tag 01LS.** The relative-spectrum situation obtained from `(S, A)` by base
> change along `g : S' ⟶ S`: the base is `S'` and the algebra is `A' = g^*A`, the pullback
> `g⁻¹A ⊗_{g⁻¹𝒪_S} 𝒪_{S'}` of `A` as an algebra sheaf, which is again quasi-coherent.

```lean
def RelativeSpecSituation.baseChange (s : RelativeSpecSituation.{u}) {S' : Scheme.{u}}
    (g : S' ⟶ s.base) : RelativeSpecSituation.{u}
```

**`Stacks.RelativeSpec.baseChangeToOriginal_app_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/FunctorBaseChange.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/FunctorBaseChange.lean#L207). The attribute's comment: “base component of the canonical map to the original functor”.

> **Stacks Project, Tag 01LS.** The morphism to `S` underlying the image of a pair under the
> canonical transformation `F' ⟶ F` is the morphism to `S'` of the pair, composed with `g`.

```lean
theorem baseChangeToOriginal_app_fst {T : Scheme.{u}}
    (p : RelativeSpecPair (s.baseChange g) T) :
    ((baseChangeToOriginal s g).app (.op T) p).1 = p.1 ≫ g
```

**`Stacks.RelativeSpec.baseChangeToOriginal_app_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/FunctorBaseChange.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/FunctorBaseChange.lean#L216). The attribute's comment: “algebra component of the canonical map to the original functor”.

> **Stacks Project, Tag 01LS.** The algebra map of the image of a pair under the canonical
> transformation `F' ⟶ F` is the direct image along `g` of the pair's algebra map, precomposed
> with the adjunct of the canonical map `g⁻¹A ⟶ g^*A`.

```lean
theorem baseChangeToOriginal_app_right {T : Scheme.{u}}
    (p : RelativeSpecPair (s.baseChange g) T) :
    ((baseChangeToOriginal s g).app (.op T) p).2.right =
      ((TopCat.Sheaf.pullbackPushforwardAdjunction CommRingCat g.base).homEquiv
          s.algebra.right ((algebraPullback g).obj s.algebra).right
          ((algebraPullbackMap g).app s.algebra)).hom ≫
        (TopCat.Presheaf.pushforward CommRingCat g.base).map p.2.right
```

**`Stacks.RelativeSpec.relativeSpecFunctorBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/FunctorBaseChange.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/FunctorBaseChange.lean#L321). The attribute's comment: “canonical base-change isomorphism”.

> **Stacks Project, Tag 01LS.** Formation of the relative-spectrum functor commutes with
> arbitrary base change: the functor attached to `(S', g^*A)` is canonically the fibre product
> `h_{S'} ×_{h_S} F` of the functor of points of `S'` and the functor attached to `(S, A)` over
> the functor of points of `S`.

```lean
def relativeSpecFunctorBaseChangeIso :
    relativeSpecFunctor (s.baseChange g) ≅
      pullback (yoneda.map g) (relativeSpecFunctorToBase s)
```

**`Stacks.RelativeSpec.relativeSpecFunctorBaseChangeIso_hom_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/FunctorBaseChange.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/FunctorBaseChange.lean#L329). The attribute's comment: “first component of the canonical isomorphism”.

> **Stacks Project, Tag 01LS.** The first component of the base-change isomorphism is the
> structural map of `F'` to the functor of points of the new base.

```lean
theorem relativeSpecFunctorBaseChangeIso_hom_fst :
    (relativeSpecFunctorBaseChangeIso s g).hom ≫
        pullback.fst (yoneda.map g) (relativeSpecFunctorToBase s) =
      relativeSpecFunctorToBase (s.baseChange g)
```

**`Stacks.RelativeSpec.relativeSpecFunctorBaseChangeIso_hom_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/FunctorBaseChange.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/FunctorBaseChange.lean#L338). The attribute's comment: “second component of the canonical isomorphism”.

> **Stacks Project, Tag 01LS.** The second component of the base-change isomorphism is the
> canonical transformation `F' ⟶ F` induced by the base-change map of algebras.

```lean
theorem relativeSpecFunctorBaseChangeIso_hom_snd :
    (relativeSpecFunctorBaseChangeIso s g).hom ≫
        pullback.snd (yoneda.map g) (relativeSpecFunctorToBase s) =
      baseChangeToOriginal s g
```

## Tag 01LT, a lemma

[Tag 01LT](https://stacks.math.columbia.edu/tag/01LT) in the Stacks Project.

**`Stacks.AffineAlgebraEquivalence.relativeSpecIsoSpecSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpecOpenRestriction/RelativeSpecAffineBase.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpecOpenRestriction/RelativeSpecAffineBase.lean#L99). The attribute's comment: “the scheme-level form: over an affine base the relative spectrum is the spectrum of the ring of global sections of the algebra”.

> **[Stacks, Tag 01LT] at the level of schemes.** Over an affine base the relative spectrum
> of a quasi-coherent sheaf of algebras is the spectrum of the ring of global sections of the
> algebra:
>
> `Spec_S(A) ≅ Spec Γ(S, A)`.
>
> `Stacks.RelativeSpec.relativeSpecFunctor_representableBy` is the same tag in its
> functor-of-points form; this is the identification with the glued relative spectrum
> `Stacks.AffineAlgebraEquivalence.relativeSpec`.
>
> It is an isomorphism of schemes; no compatibility with the structure morphism to `S` is
> claimed.

```lean
public noncomputable def relativeSpecIsoSpecSections [IsAffine S] :
    relativeSpec A ≅ Spec (A.right.obj.obj (op (⊤ : S.Opens)))
```

**`Stacks.RelativeSpec.relativeSpecFunctor_representableBy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpecRepresentability/Basic.lean, line 496](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpecRepresentability/Basic.lean#L496).

> If the base is affine, the functor of relative-spectrum pairs associated to a quasi-coherent
> algebra is represented by the spectrum of the algebra's ring of global sections.

```lean
theorem relativeSpecFunctor_representableBy (s : RelativeSpecSituation.{u}) [IsAffine s.base] :
    Nonempty ((relativeSpecFunctor s).RepresentableBy
      (Spec (s.algebra.right.obj.obj (.op (⊤ : s.base.Opens)))))
```

## Tag 01LU, a lemma

[Tag 01LU](https://stacks.math.columbia.edu/tag/01LU) in the Stacks Project.

**`Stacks.RelativeSpec.relativeSpecFunctor_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/Representability.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/Representability.lean#L409).

> The functor associated to a quasi-coherent algebra on a scheme is representable by a
> scheme.

```lean
theorem relativeSpecFunctor_isRepresentable : (relativeSpecFunctor s).IsRepresentable
```

## Tag 01LV, a lemma

[Tag 01LV](https://stacks.math.columbia.edu/tag/01LV) in the Stacks Project.

**`Stacks.RelativeSpec.relativeSpecRepresentableBy`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/Representability.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/Representability.lean#L374).

> The glued relative spectrum represents the relative spectrum functor, with universal element
> the structure morphism together with the universal algebra map.

```lean
noncomputable def relativeSpecRepresentableBy :
    (relativeSpecFunctor s).RepresentableBy (gluedSpectrum s).scheme
```

**`Stacks.RelativeSpec.gluedSpectrumIso_hom_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/Representability.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/Representability.lean#L432). The attribute's comment: “canonical comparison over the base”.

> The canonical comparison between the glued relative spectrum and a scheme representing the
> relative spectrum functor is a morphism over the base, where the representing scheme carries the
> structure morphism of its universal element.

```lean
theorem gluedSpectrumIso_hom_toBase {X : Scheme.{u}}
    (h : (relativeSpecFunctor s).RepresentableBy X) :
    (gluedSpectrumIso s h).hom ≫ (h.homEquiv (𝟙 X)).1 = (gluedSpectrum s).toBase
```

## Tag 01LW, a definition

[Tag 01LW](https://stacks.math.columbia.edu/tag/01LW) in the Stacks Project.

**`Stacks.RelativeSpec.relativeSpecRepresentableBy`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/Representability.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/Representability.lean#L374). The attribute's comment: “the relative spectrum with its universal algebra map”.

> The glued relative spectrum represents the relative spectrum functor, with universal element
> the structure morphism together with the universal algebra map.

```lean
noncomputable def relativeSpecRepresentableBy :
    (relativeSpecFunctor s).RepresentableBy (gluedSpectrum s).scheme
```

## Tag 01LX, a lemma

[Tag 01LX](https://stacks.math.columbia.edu/tag/01LX) in the Stacks Project.

**`Stacks.AffineAlgebraEquivalence.isAffineOpen_preimage_relativeSpecToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineAlgebraEquivalence2/RelativeSpec.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineAlgebraEquivalence2/RelativeSpec.lean#L137). The attribute's comment: “affine\_inverse\_image”. References: SGA 3 I (4.2), “Spec(A) affine over S”.

> **Stacks Project, Tag 01LX(1).** The preimage of an affine open of the base in the relative
> spectrum is affine.

```lean
public theorem isAffineOpen_preimage_relativeSpecToBase (U : S.affineOpens) :
    IsAffineOpen (relativeSpecToBase A ⁻¹ᵁ (U : S.Opens))
```

**`Stacks.AffineAlgebraEquivalence.pushforwardAlgebraIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpecEssSurj/Basic.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpecEssSurj/Basic.lean#L296). The attribute's comment: “universal\_map\_iso”. References: SGA 3 I (4.2), “A ≅ π\_*O\_Spec(A)”.

> **Stacks Project, Tag 01LX(3).** The isomorphism of sheaves of `𝒪_S`-algebras
> `(relativeSpecToBase A)_* 𝒪 ≅ A`. Its inverse is the universal map
> `A ⟶ (relativeSpecToBase A)_* 𝒪` of the relative spectrum, so this says that the universal map
> is an isomorphism; it is also the essential surjectivity of the pushforward functor.

```lean
public noncomputable def pushforwardAlgebraIso : pushforwardAlgebra (relativeSpecToBase A) ≅ A
```

**`Stacks.AffineAlgebraEquivalence.relativeSpecBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpecOpenRestriction/RelativeSpecBaseChange.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpecOpenRestriction/RelativeSpecBaseChange.lean#L113). The attribute's comment: “part (2): Spec\_S(A) ×\_S T = Spec\_T(g^*A) for an arbitrary morphism g : T → S”. References: EGA II (1.5.6); SGA 3 III (0.1.7); SGA 3 VIA (2.1.2), “more general”.

> **Stacks Project, Tag 01LX part (2).** For a quasi-coherent sheaf of `𝒪_S`-algebras `A` and
> an arbitrary morphism of schemes `g : T ⟶ S`, the fibre product
> `\underline{Spec}_S(A) ×_S T` is the relative spectrum over `T` of the base change `g^*A`:
> ```
> T ×_S \underline{Spec}_S(A) = \underline{Spec}_T(g^*A).
> ```
> The base change `g^*A` is quasi-coherent by
> `Stacks.AffineAlgebraEquivalence.isQuasicoherent_algebraPullback_obj`, which is what makes the
> right-hand side meaningful.

```lean
public noncomputable def relativeSpecBaseChangeIso :
    (Over.pullback g).obj (Over.mk (relativeSpecToBase A)) ≅
      Over.mk (relativeSpecToBase ((algebraPullback g).obj A))
```

## Tag 01LY, a lemma

[Tag 01LY](https://stacks.math.columbia.edu/tag/01LY) in the Stacks Project.

**`Stacks.RelativeSpec.AlgebraSheaf.isQuasicoherent_pushforwardAlgebra`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/CanonicalMorphism.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/CanonicalMorphism.lean#L106). The attribute's comment: “quasi-coherence of the pushed-forward algebra”. References: EGA I (4.1.1), “more general”; EGA I (9.2.2), “special case”; EGA IV (11.10.3); EGA IV (21.12.1); EGA IV (3.1.10.2), “special case”; SGA 3 III (0.13), “special case”; SGA 3 VIB (11.0), “special case”.

> For a quasi-compact and quasi-separated morphism of schemes `f : X ⟶ S`, the sheaf of
> `𝒪_S`-algebras `f_* 𝒪_X` is quasi-coherent.
>
> This is Tag 01LC for the structure sheaf of `X`: the `𝒪_S`-module underlying `f_* 𝒪_X` is the
> direct image of the unit module over `𝒪_X`.

```lean
instance AlgebraSheaf.isQuasicoherent_pushforwardAlgebra [QuasiCompact f] [QuasiSeparated f] :
    AlgebraSheaf.IsQuasicoherent (pushforwardAlgebra f)
```

**`Stacks.RelativeSpec.toRelativeSpec`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/CanonicalMorphism.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/CanonicalMorphism.lean#L156). The attribute's comment: “canonical morphism”. References: EGA III (4.3.1).

> The canonical morphism `can : X ⟶ Spec_S(f_* 𝒪_X)` from the source of a quasi-compact,
> quasi-separated morphism to the relative spectrum of the direct image of its structure sheaf. It
> is the morphism classified by the identity map of `f_* 𝒪_X` under the representing bijection of
> Tag 01LV.

```lean
noncomputable def toRelativeSpec : X ⟶ (gluedSpectrum (pushforwardSituation f)).scheme
```

**`Stacks.RelativeSpec.toRelativeSpec_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/CanonicalMorphism.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/CanonicalMorphism.lean#L171). The attribute's comment: “morphism over the base”.

> The canonical morphism to the relative spectrum of `f_* 𝒪_X` is a morphism of schemes over
> `S`.

```lean
theorem toRelativeSpec_toBase :
    toRelativeSpec f ≫ (gluedSpectrum (pushforwardSituation f)).toBase = f
```

**`Stacks.RelativeSpec.ι_toRelativeSpec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/CanonicalMorphism.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/CanonicalMorphism.lean#L192). The attribute's comment: “identification on affine opens”.

> Over an affine open `U` of the base, the canonical morphism to the relative spectrum of
> `f_* 𝒪_X` restricts on `f⁻¹(U)` to the canonical morphism `f⁻¹(U) ⟶ Spec Γ(f⁻¹(U), 𝒪_X)`,
> followed by the chart of `U`.

```lean
theorem ι_toRelativeSpec (U : S.affineOpens) :
    (f ⁻¹ᵁ U.1).ι ≫ toRelativeSpec f =
      (f ⁻¹ᵁ U.1).toSpecΓ ≫ (gluedSpectrum (pushforwardSituation f)).chart U
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.4, Tag 01LQ](https://stacks.math.columbia.edu/tag/01LQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
