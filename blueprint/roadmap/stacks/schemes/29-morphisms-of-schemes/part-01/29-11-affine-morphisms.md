---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsAffineHom, AlgebraicGeometry.IsSeparated.of_isAffineHom, AlgebraicGeometry.instQuasiCompactOfIsAffineHom, AlgebraicGeometry.isAffineHom_iff_forall_exists_isAffineOpen, AlgebraicGeometry.relativeSpecPushforwardAlgebraIso, AlgebraicGeometry.isAffineHom_iff_exists_relativeSpecIso, Stacks.AffineAlgebraEquivalence.overRelativeSpecIso, Stacks.AffineAlgebraEquivalence.isAffineHom_iff_exists_quasicoherentAlgebra
statement: formalized
proof: formalized
---

# 29.11 Affine morphisms

Section 29.11 of the Stacks Project, [Tag 01S5](https://stacks.math.columbia.edu/tag/01S5). 15 tags here are carried by 20 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01S6, a definition

[Tag 01S6](https://stacks.math.columbia.edu/tag/01S6) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsAffineHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsAffineHom#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L151) (StacksFrontier). References: EGA II (1.2.1); EGA II (1.6.1); SGA 1 VIII (2.1); SGA 3 I (4.2).

## Tag 01S7, a lemma

[Tag 01S7](https://stacks.math.columbia.edu/tag/01S7) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsSeparated.of_isAffineHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsSeparated.of_isAffineHom#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L158) (StacksFrontier): “separated”. References: EGA I (5.5.7), “more general”; EGA I (5.5.9), “special case”; EGA II (1.2.4); SGA 3 VIIA (8.5.2), “affine implies separated”; SGA 3 VIA (4.6), “partial”; SGA 3 XI (4.3), “T is separated over S”.
- [`AlgebraicGeometry.instQuasiCompactOfIsAffineHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instQuasiCompactOfIsAffineHom#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L159) (StacksFrontier): “quasi-compact”. References: SGA 3 VIA (4.6), “partial”.

## Tag 01S8, a lemma

[Tag 01S8](https://stacks.math.columbia.edu/tag/01S8) in the Stacks Project.

**`AlgebraicGeometry.isAffineHom_iff_forall_exists_isAffineOpen`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/OpenCoverCriterion.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/OpenCoverCriterion.lean#L43). The attribute's comment: “equivalence of (1) and (2)”.

> **Stacks Project, Tag 01S8, equivalence of (1) and (2).** A morphism of schemes
> `f : X ⟶ S` is affine if and only if every point of `S` has an affine open neighbourhood
> whose inverse image under `f` is affine.

```lean
lemma isAffineHom_iff_forall_exists_isAffineOpen {X S : Scheme.{u}} (f : X ⟶ S) :
    IsAffineHom f ↔
      ∀ x : S, ∃ U : S.Opens, x ∈ U ∧ IsAffineOpen U ∧ IsAffineOpen (f ⁻¹ᵁ U)
```

**`AlgebraicGeometry.relativeSpecPushforwardAlgebraIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/RelativeSpecCriterion.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/RelativeSpecCriterion.lean#L204). The attribute's comment: “the source is the relative spectrum of the pushforward algebra”. References: EGA II (1.3.2).

> For an affine morphism `f : X ⟶ S`, the source is, over `S`, the relative spectrum of the
> pushforward `f_* 𝒪_X` of its structure sheaf, which is a quasi-coherent sheaf of
> `𝒪_S`-algebras.

```lean
def relativeSpecPushforwardAlgebraIso (f : X ⟶ S) [IsAffineHom f] :
    Over.mk f ≅ Over.mk (@relativeSpecToBase S (pushforwardAlgebra f)
      (isQuasicoherent_pushforwardAlgebra f))
```

**`AlgebraicGeometry.isAffineHom_iff_exists_relativeSpecIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/RelativeSpecCriterion.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/RelativeSpecCriterion.lean#L230). The attribute's comment: “equivalence of (1) and (3)”. References: EGA II (1.3.1), “partial”; SGA 3 I (4.2), “partial”.

> **Stacks Project, Tag 01S8, equivalence of (1) and (3).** A morphism of schemes is affine if
> and only if it is isomorphic, as an object over its target, to the structure morphism of the
> relative spectrum of a quasi-coherent sheaf of algebras on the target.

```lean
theorem isAffineHom_iff_exists_relativeSpecIso (f : X ⟶ S) :
    IsAffineHom f ↔
      ∃ (A : AlgebraSheaf S) (hA : AlgebraSheaf.IsQuasicoherent A),
        Nonempty (Over.mk f ≅ Over.mk (@relativeSpecToBase S A hA))
```

**`Stacks.AffineAlgebraEquivalence.overRelativeSpecIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpecBaseChange/AntiEquivalence.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeSpecBaseChange/AntiEquivalence.lean#L257). The attribute's comment: “the final statement: X = Spec\_S(f\_* O\_X) for an affine morphism f : X → S”.

> **Stacks Project, Tag 01S8, the final statement.** For an affine morphism `f : X ⟶ S` there
> is an isomorphism `X ≅ \underline{Spec}_S(f_* 𝒪_X)` of schemes over `S`.

```lean
public noncomputable def overRelativeSpecIso {X S : Scheme.{u}} (f : X ⟶ S) [IsAffineHom f] :
    letI := isQuasicoherent_pushforwardAlgebra f
    (Over.mk f : Over S) ≅ Over.mk (relativeSpecToBase (pushforwardAlgebra f))
```

**`Stacks.AffineAlgebraEquivalence.isAffineHom_iff_exists_quasicoherentAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpecBaseChange/AntiEquivalence.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeSpecBaseChange/AntiEquivalence.lean#L280). The attribute's comment: “part (3): f is affine iff X is a relative spectrum over S”. References: SGA 3 I (4.2), “partial”; SGA 3 III (0.1.7), “0.1.7(a)”.

> **Stacks Project, Tag 01S8, part (3).** A morphism of schemes `f : X ⟶ S` is affine if and
> only if there is a quasi-coherent sheaf of `𝒪_S`-algebras `A` and an isomorphism
> `X ≅ \underline{Spec}_S(A)` of schemes over `S`.
>
> The forward direction takes `A = f_* 𝒪_X` and is `overRelativeSpecIso`; the converse is
> `isAffineHom_relativeSpecToBase` together with `isAffineHom_of_overIso`.

```lean
public theorem isAffineHom_iff_exists_quasicoherentAlgebra {X S : Scheme.{u}} (f : X ⟶ S) :
    IsAffineHom f ↔ ∃ A : QuasicoherentAlgebra S,
      letI := A.property
      Nonempty ((Over.mk f : Over S) ≅ Over.mk (relativeSpecToBase A.obj))
```

## Tag 01S9, a remark

[Tag 01S9](https://stacks.math.columbia.edu/tag/01S9) in the Stacks Project.

**`AlgebraicGeometry.isAffineHom_of_iSup_eq_top_of_isAffineOpen_preimage`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/AffineCoverDirect.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/AffineCoverDirect.lean#L84).

> **Stacks Project, Tag 01S9.** If `S = ⋃ⱼ Wⱼ` is an affine open covering such that each
> `f⁻¹(Wⱼ)` is affine, then `f : X ⟶ S` is affine.

```lean
lemma isAffineHom_of_iSup_eq_top_of_isAffineOpen_preimage {ι : Type*} (W : ι → S.Opens)
    (hW : ∀ j, IsAffineOpen (W j)) (hcov : ⨆ j, W j = ⊤)
    (hfW : ∀ j, IsAffineOpen (f ⁻¹ᵁ W j)) :
    IsAffineHom f
```

## Tag 01SA, a lemma

[Tag 01SA](https://stacks.math.columbia.edu/tag/01SA) in the Stacks Project.

**`Stacks.AlgebraPullbackQcoh.affineEquivalenceAlgebras`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AlgebraPullbackQcoh/BaseChangeIso.lean, line 438](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/AlgebraPullbackQcoh/BaseChangeIso.lean#L438). References: SGA 3 I (4.2), “more general”.

> **All nine clauses of [Stacks, Tag 01SA].**  The canonical anti-equivalence between the
> schemes affine over a base and the quasi-coherent sheaves of commutative algebras on that base,
> compatible with arbitrary base change.
>
> The tag is registered by a single unqualified attribute on this nine-field structure.

```lean
def affineEquivalenceAlgebras : AffineAlgebraAntiEquivalence.{u}
```

**`Stacks.AffineAlgebraEquivalence.affineAlgebraAntiEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpecOpenRestriction/GeneralBaseChange.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeSpecOpenRestriction/GeneralBaseChange.lean#L191). The attribute's comment: “compatibility of the anti-equivalence with arbitrary base change”. References: EGA II (1.5.2); SGA 3 I (4.2), “more general”.

> **Stacks Project, Tag 01SA, the base-change clause.** The anti-equivalence between the
> schemes affine over `S` and the quasi-coherent sheaves of `𝒪_S`-algebras is compatible with
> arbitrary base change, unconditionally: the one assertion on which
> `Stacks.AffineAlgebraEquivalence.antiEquivalenceOfQuasicoherentAlgebraPullback` was left standing
> is `isQuasicoherentAlgebraPullback`, proved above.

```lean
public noncomputable def affineAlgebraAntiEquivalence : AffineAlgebraAntiEquivalence.{u}
```

## Tag 0H88, a lemma

[Tag 0H88](https://stacks.math.columbia.edu/tag/0H88) in the Stacks Project.

**`Stacks.AlgebraicGeometry.QcohLimits.isQuasicoherent_restrictScalars_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QcohLimits/RestrictScalars.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QcohLimits/RestrictScalars.lean#L203). References: EGA I (9.6.1).

> **Stacks Project, Tag 0H88.** Let `α : 𝒪_S ⟶ A` be a sheaf of rings on a scheme `S` which is
> quasi-coherent as an `𝒪_S`-module.  An `A`-module is quasi-coherent as an `𝒪_S`-module if and
> only if it is quasi-coherent as an `A`-module.

```lean
theorem isQuasicoherent_restrictScalars_iff
    (hA : ((SheafOfModules.restrictScalars.{u} α).obj (SheafOfModules.unit A)).IsQuasicoherent)
    (G : SheafOfModules.{u} A) :
    ((SheafOfModules.restrictScalars.{u} α).obj G).IsQuasicoherent ↔ G.IsQuasicoherent
```

## Tag 01SB, a lemma

[Tag 01SB](https://stacks.math.columbia.edu/tag/01SB) in the Stacks Project.

**`Stacks.AlgebraicGeometry.AffineQcohUnit.isEquivalence_affineQuasicoherentPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineQcohUnit/Equivalence.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/AffineQcohUnit/Equivalence.lean#L61). The attribute's comment: “the equivalence”.

> **Stacks Project, Tag 01SB, first assertion.**  For an affine morphism `f : X ⟶ S`, direct
> image induces an equivalence from quasi-coherent `𝒪_X`-modules to quasi-coherent modules over
> `f_* 𝒪_X`, with quasi-inverse `𝒢 ↦ f^*𝒢 ⊗_{f^*f_*𝒪_X} 𝒪_X`.

```lean
theorem isEquivalence_affineQuasicoherentPushforward [IsAffineHom f] :
    (affineQuasicoherentPushforward f).IsEquivalence
```

**`Stacks.AlgebraicGeometry.QcohLimits.affine_isQuasicoherent_restrictScalars_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QcohLimits/RestrictScalars.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QcohLimits/RestrictScalars.lean#L242). The attribute's comment: “quasi-coherence under scalar restriction”. References: EGA II (1.4.3), “special case”.

> **Stacks Project, Tag 01SB, second assertion.** An `f_* 𝒪_X`-module is quasi-coherent as an
> `𝒪_S`-module if and only if it is quasi-coherent as an `f_* 𝒪_X`-module.
>
> This is the whole of the tag's final statement ("Moreover, an `𝒜`-module is quasi-coherent as an
> `𝒪_S`-module if and only if it is quasi-coherent as an `𝒜`-module").  The tag's other assertion,
> the equivalence of categories, is not proved here, so the attribute is clause-qualified.

```lean
theorem affine_isQuasicoherent_restrictScalars_iff (f : X ⟶ S) [IsAffineHom f]
    (G : SheafOfModules.{u} (AffineQcohPushforward.pushforwardRing f.base X.ringCatSheaf)) :
    ((SheafOfModules.restrictScalars f.toRingCatSheafHom).obj G).IsQuasicoherent ↔
      G.IsQuasicoherent
```

## Tag 01SC, a lemma

[Tag 01SC](https://stacks.math.columbia.edu/tag/01SC) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.instIsAffineHomCompScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instIsAffineHomCompScheme#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L161) (StacksFrontier). References: EGA II (1.3.5); EGA II (1.3.6), “partial”; EGA II (1.6.2).

## Tag 01SD, a lemma

[Tag 01SD](https://stacks.math.columbia.edu/tag/01SD) in the Stacks Project.

**`AlgebraicGeometry.IsAffineHom.of_isPullback`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/BaseChange.lean, line 36](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/BaseChange.lean#L36).

> The base change of an affine morphism is affine: if `f : X ⟶ S` is affine and
> `g' ≫ f = f' ≫ g` is a cartesian square, then the base change `f' : X' ⟶ S'` of `f` along
> `g : S' ⟶ S` is affine.

```lean
lemma IsAffineHom.of_isPullback {X S X' S' : Scheme.{u}} {g' : X' ⟶ X} {f' : X' ⟶ S'}
    {f : X ⟶ S} {g : S' ⟶ S} (sq : IsPullback g' f' f g) [IsAffineHom f] :
    IsAffineHom f'
```

## Tag 01SE, a lemma

[Tag 01SE](https://stacks.math.columbia.edu/tag/01SE) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsClosedImmersion.instIsAffineHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsClosedImmersion.instIsAffineHom#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L163) (StacksFrontier). References: EGA I (4.2.3), “more general”; EGA II (1.2.2); EGA II (1.6.2); SGA 3 VIB (2.9.1), “special case”; SGA 3 XXV (4.3), “partial”.

## Tag 01SF, a lemma

[Tag 01SF](https://stacks.math.columbia.edu/tag/01SF) in the Stacks Project.

**`Stacks.NonvanishingAffineIntersection.isAffineOpen_inf_nonvanishingOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NonvanishingAffineIntersection/Basic.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/NonvanishingAffineIntersection/Basic.lean#L122). The attribute's comment: “affineness of the inclusion j : X\_s -> X, i.e. preimages of affine opens under j”. References: EGA II (5.5.8); SGA 6 II (2.2.3.1).

> Let `X` be a scheme, `M` an invertible `𝒪_X`-module and `s` a global section of `M`. For every
> affine open `U` of `X`, the intersection `U ∩ X_s` of `U` with the nonvanishing locus of `s` is
> affine.

```lean
theorem isAffineOpen_inf_nonvanishingOpen {U : X.Opens} (hU : IsAffineOpen U) :
    IsAffineOpen (U ⊓ Stacks.NonvanishingOpen.nonvanishingOpen X M s)
```

## Tag 01SG, a lemma

[Tag 01SG](https://stacks.math.columbia.edu/tag/01SG) in the Stacks Project.

**`AlgebraicGeometry.isAffineHom_of_isAffineHom_of_isAffineHom_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/AffineDiagonalTarget.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/AffineDiagonalTarget.lean#L55). The attribute's comment: “part (1)”.

> Let `g : X ⟶ Y` be a morphism of schemes over `S`. If `X` is affine over `S` and the diagonal
> `Y ⟶ Y ×_S Y` is affine, then `g` is affine.

```lean
public theorem isAffineHom_of_isAffineHom_of_isAffineHom_diagonal (g : X ⟶ Y) {a : X ⟶ S}
    (b : Y ⟶ S) (hab : g ≫ b = a) [IsAffineHom a]
    [IsAffineHom (pullback.diagonal b)] : IsAffineHom g
```

**`AlgebraicGeometry.isAffineHom_of_isAffineHom_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/AffineDiagonalTarget.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/AffineDiagonalTarget.lean#L66). The attribute's comment: “part (2)”.

> Let `g : X ⟶ Y` be a morphism of schemes over `S`. If `X` is affine over `S` and `Y` is
> separated over `S`, then `g` is affine.

```lean
public theorem isAffineHom_of_isAffineHom_of_isSeparated (g : X ⟶ Y) {a : X ⟶ S} (b : Y ⟶ S)
    (hab : g ≫ b = a) [IsAffineHom a] [IsSeparated b] : IsAffineHom g
```

**`AlgebraicGeometry.isAffineHom_of_isAffine_of_isAffineHom_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/AffineDiagonalTarget.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/AffineDiagonalTarget.lean#L74). The attribute's comment: “part (3)”.

> A morphism from an affine scheme to a scheme with affine
> diagonal is affine.

```lean
public theorem isAffineHom_of_isAffine_of_isAffineHom_diagonal (g : X ⟶ Y) [IsAffine X]
    [IsAffineHom (pullback.diagonal (terminal.from Y))] : IsAffineHom g
```

**`AlgebraicGeometry.isAffineHom_of_isAffine_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/AffineDiagonalTarget.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/AffineDiagonalTarget.lean#L81). The attribute's comment: “part (4)”.

> A morphism from an affine scheme to a separated scheme is affine.

```lean
public theorem isAffineHom_of_isAffine_of_isSeparated (g : X ⟶ Y) [IsAffine X]
    [Y.IsSeparated] : IsAffineHom g
```

## Tag 01SH, a lemma

[Tag 01SH](https://stacks.math.columbia.edu/tag/01SH) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.isAffineHom_of_isAffine`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isAffineHom_of_isAffine#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L165) (StacksFrontier). References: EGA II (1.2.3), “affine target”; EGA II (1.3.4), “sufficiency”; EGA II (1.3.6), “special case”; EGA II (1.6.2), “(v), special case”; EGA II (1.6.3), “affine target”; SGA 3 VIB (1.4.2), “more general”.

## Tag 01SI, a lemma

[Tag 01SI](https://stacks.math.columbia.edu/tag/01SI) in the Stacks Project.

**`AlgebraicGeometry.isAffineHom_of_isArtinianRing`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/Artinian.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/Artinian.lean#L39).

> **Stacks Project, Tag 01SI.** Every morphism from the spectrum of an
> Artinian ring to a scheme is affine.

```lean
lemma isAffineHom_of_isArtinianRing {A : CommRingCat.{u}} [IsArtinianRing A]
    {S : Scheme.{u}} (f : Spec A ⟶ S) : IsAffineHom f
```

## Tag 0C3A, a lemma

[Tag 0C3A](https://stacks.math.columbia.edu/tag/0C3A) in the Stacks Project.

**`AlgebraicGeometry.isAffineHom_of_isAffineHom_restrict_of_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/AffineImmersion.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/AffineImmersion.lean#L62). The attribute's comment: “immersion is affine”.

> **Stacks Project, Tag 0C3A, affineness of the immersion.** An immersion `j : Y ⟶ X` is
> affine as soon as there is an open `U ⊆ X` with affine inclusion over which `j` restricts to an
> affine morphism and whose complement meets the image of `j` in a closed set.

```lean
theorem isAffineHom_of_isAffineHom_restrict_of_isClosed {X Y : Scheme.{u}} (j : Y ⟶ X)
    [IsImmersion j] (U : X.Opens) [IsAffineHom U.ι] [IsAffineHom (j ∣_ U)]
    (hZ : IsClosed (Set.range (j : Y → X) ∩ (U : Set X)ᶜ)) : IsAffineHom j
```

**`AlgebraicGeometry.isAffine_of_isAffineHom_restrict_of_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/AffineImmersion.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/AffineImmersion.lean#L98). The attribute's comment: “source is affine”.

> **Stacks Project, Tag 0C3A, affineness of the source.** In the situation of
> `AlgebraicGeometry.isAffineHom_of_isAffineHom_restrict_of_isClosed` with an affine target, the
> source of the immersion is affine.

```lean
theorem isAffine_of_isAffineHom_restrict_of_isClosed {X Y : Scheme.{u}} (j : Y ⟶ X)
    [IsImmersion j] [IsAffine X] (U : X.Opens) [IsAffineHom U.ι] [IsAffineHom (j ∣_ U)]
    (hZ : IsClosed (Set.range (j : Y → X) ∩ (U : Set X)ᶜ)) : IsAffine Y
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.11, Tag 01S5](https://stacks.math.columbia.edu/tag/01S5)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
