---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsEmbeddedAssociatedPoint, AlgebraicGeometry.IsEmbeddedPoint, AlgebraicGeometry.IsEmbeddedComponent, AlgebraicGeometry.mem_associatedPoints_of_isGenericPoint_irreducibleComponent_supp, AlgebraicGeometry.isEmbeddedAssociatedPoint_iff_not_genericPoint, AlgebraicGeometry.isEmbeddedPoint_iff_not_genericPoint, AlgebraicGeometry.hasNoEmbeddedAssociatedPoints_iff_hasPropertySk_one, AlgebraicGeometry.isCohenMacaulay_iff_hasNoEmbeddedPoints_of_topologicalKrullDim_le_one
statement: formalized
proof: formalized
---

# 31.4 Embedded points

Section 31.4 of the Stacks Project, [Tag 05AJ](https://stacks.math.columbia.edu/tag/05AJ). 7 tags here are carried by 26 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05AK, a definition

[Tag 05AK](https://stacks.math.columbia.edu/tag/05AK) in the Stacks Project.

**`AlgebraicGeometry.IsEmbeddedAssociatedPoint`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Embedded.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Embedded.lean#L69). The attribute's comment: “part (1)”.

> **Stacks 05AK, part (1).** An associated point is *embedded* when it is a proper
> specialization of another associated point.

```lean
noncomputable abbrev IsEmbeddedAssociatedPoint {X : Scheme.{u}} (F : X.Modules) (x : X) : Prop
```

**`AlgebraicGeometry.IsEmbeddedPoint`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Embedded.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Embedded.lean#L80). The attribute's comment: “part (2)”.

> **Stacks 05AK, part (2).** An embedded point of a scheme is an embedded associated point of
> its structure sheaf.

```lean
noncomputable abbrev IsEmbeddedPoint (X : Scheme.{u}) (x : X) : Prop
```

**`AlgebraicGeometry.IsEmbeddedComponent`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Embedded.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Embedded.lean#L88). The attribute's comment: “part (3)”.

> **Stacks 05AK, part (3).** An embedded component is the closure of an embedded point.

```lean
noncomputable abbrev IsEmbeddedComponent (X : Scheme.{u}) (Z : Set X) : Prop
```

## Tag 05AL, a lemma

[Tag 05AL](https://stacks.math.columbia.edu/tag/05AL) in the Stacks Project.

**`AlgebraicGeometry.mem_associatedPoints_of_isGenericPoint_irreducibleComponent_supp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/EmbeddedCharacterization.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/EmbeddedCharacterization.lean#L83). The attribute's comment: “part (1)”. References: EGA IV (3.1.3), “special case”.

> **Stacks 05AL, part (1).** The generic point of an irreducible component of the support of a
> coherent sheaf is associated to that sheaf.

```lean
theorem mem_associatedPoints_of_isGenericPoint_irreducibleComponent_supp (X : Scheme.{u})
    [IsLocallyNoetherian X] (F : X.Modules) [F.IsCoherent]
    {Z : Set (↥(SheafOfModules.supp F))}
    (hZ : Z ∈ irreducibleComponents (↥(SheafOfModules.supp F))) {x : X}
    (hx : IsGenericPoint x (Subtype.val '' Z)) :
    x ∈ Stacks.Divisors.associatedPoints F
```

**`AlgebraicGeometry.isEmbeddedAssociatedPoint_iff_not_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/EmbeddedCharacterization.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/EmbeddedCharacterization.lean#L98). The attribute's comment: “part (2)”.

> **Stacks 05AL, part (2).** An associated point of a coherent sheaf is embedded exactly when
> it is not generic in any irreducible component of its support.

```lean
theorem isEmbeddedAssociatedPoint_iff_not_genericPoint (X : Scheme.{u}) [IsLocallyNoetherian X]
    (F : X.Modules) [F.IsCoherent] (x : X) :
    IsEmbeddedAssociatedPoint F x ↔
      x ∈ Stacks.Divisors.associatedPoints F ∧
        ¬ ∃ Z ∈ irreducibleComponents (↥(SheafOfModules.supp F)),
          IsGenericPoint x (Subtype.val '' Z)
```

**`AlgebraicGeometry.isEmbeddedPoint_iff_not_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/EmbeddedCharacterization.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/EmbeddedCharacterization.lean#L125). The attribute's comment: “embedded points of the scheme”.

> **Stacks 05AL, concluding assertion.** The embedded points of a locally Noetherian scheme
> are precisely its non-generic associated points.

```lean
theorem isEmbeddedPoint_iff_not_genericPoint (X : Scheme.{u}) [IsLocallyNoetherian X] (x : X) :
    IsEmbeddedPoint X x ↔
      x ∈ Stacks.Divisors.schemeAssociatedPoints X ∧
        ¬ ∃ Z ∈ irreducibleComponents X, IsGenericPoint x Z
```

## Tag 0346, a lemma

[Tag 0346](https://stacks.math.columbia.edu/tag/0346) in the Stacks Project.

**`AlgebraicGeometry.hasNoEmbeddedAssociatedPoints_iff_hasPropertySk_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Serre.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/Serre.lean#L230).

> **Stacks Project, Tag 0346.** A coherent sheaf on a locally Noetherian scheme has no
> embedded associated points if and only if it satisfies Serre's condition `(S₁)`.

```lean
theorem hasNoEmbeddedAssociatedPoints_iff_hasPropertySk_one (X : Scheme.{u})
    [IsLocallyNoetherian X] (F : X.Modules) [F.IsCoherent] :
    HasNoEmbeddedAssociatedPoints F ↔ SheafHasPropertySk X F 1
```

## Tag 0BXG, a lemma

[Tag 0BXG](https://stacks.math.columbia.edu/tag/0BXG) in the Stacks Project.

**`AlgebraicGeometry.isCohenMacaulay_iff_hasNoEmbeddedPoints_of_topologicalKrullDim_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/EmbeddedPoints/DimensionOne.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/EmbeddedPoints/DimensionOne.lean#L91). References: EGA IV (7.2.1.1), “a) <=> c)”; EGA IV (5.7.8), “more general”.

> A locally Noetherian scheme of dimension at most one is Cohen--Macaulay if and only if it
> has no embedded points.

```lean
theorem isCohenMacaulay_iff_hasNoEmbeddedPoints_of_topologicalKrullDim_le_one
    (X : Scheme.{u}) [IsLocallyNoetherian X]
    (hX : topologicalKrullDim X ≤ 1) :
    IsCohenMacaulay X ↔ HasNoEmbeddedPoints X
```

## Tag 083P, a lemma

[Tag 083P](https://stacks.math.columbia.edu/tag/083P) in the Stacks Project.

**`AlgebraicGeometry.isSchemeTheoreticallyDense_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/SchemeTheoreticallyDense.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/SchemeTheoreticallyDense.lean#L189).

> **Stacks Project, Tag 083P.** For an open subscheme of a locally Noetherian scheme,
> scheme-theoretic density is equivalent to topological density together with containment of every
> embedded point, and also to containment of every associated point.

```lean
theorem isSchemeTheoreticallyDense_tfae (X : Scheme.{u}) [IsLocallyNoetherian X] (U : X.Opens) :
    List.TFAE [
      Scheme.Opens.IsSchemeTheoreticallyDense U,
      Dense (U : Set X) ∧ (∀ x : X, IsEmbeddedPoint X x → x ∈ U),
      Stacks.Divisors.schemeAssociatedPoints X ⊆ (U : Set X)]
```

## Tag 02OL, a lemma

[Tag 02OL](https://stacks.math.columbia.edu/tag/02OL) in the Stacks Project.

**`Stacks.AlgebraicGeometry.CoherentSubquotients.exists_greatest_isNowhereDenseCoherentSubobject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentSubquotients/NowhereDense.lean, line 545](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentSubquotients/NowhereDense.lean#L545). The attribute's comment: “greatest subsheaf”.

> **[Stacks, Tag 02OL].** Among the coherent subsheaves of a coherent sheaf `F` on a locally
> Noetherian scheme whose support is nowhere dense in the support of `F` there is a greatest
> one.

```lean
public theorem exists_greatest_isNowhereDenseCoherentSubobject
    {X : Scheme.{u}} [IsLocallyNoetherian X] (F : X.Modules) [F.IsCoherent] :
    ∃ K : Subobject F,
      IsNowhereDenseCoherentSubobject F K ∧
        ∀ L : Subobject F, IsNowhereDenseCoherentSubobject F L → L ≤ K
```

**`Stacks.AlgebraicGeometry.CoherentSubquotients.supp_cokernel_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentSubquotients/NowhereDense.lean, line 562](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentSubquotients/NowhereDense.lean#L562). The attribute's comment: “part (1): support of the quotient”.

> **[Stacks, Tag 02OL], part (1).** The quotient of `F` by a coherent subsheaf with nowhere
> dense support has the same support as `F`.

```lean
public theorem supp_cokernel_eq {X : Scheme.{u}} [IsLocallyNoetherian X]
    (F : X.Modules) [F.IsCoherent] (K : Subobject F)
    (hK : IsNowhereDenseCoherentSubobject F K) :
    (⟨(cokernel K.arrow).val, (cokernel K.arrow).isSheaf⟩ :
      RingedSpace.ModuleSheaf.{u} X.toRingedSpace).supp =
      (⟨F.val, F.isSheaf⟩ : RingedSpace.ModuleSheaf.{u} X.toRingedSpace).supp
```

**`Stacks.AlgebraicGeometry.CoherentSubquotients.cokernel_hasNoEmbeddedAssociatedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentSubquotients/NowhereDense.lean, line 739](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentSubquotients/NowhereDense.lean#L739). The attribute's comment: “part (2): no embedded associated points”.

> **[Stacks, Tag 02OL], part (2).** The quotient of `F` by a coherent subsheaf with nowhere
> dense support has no embedded associated points.

```lean
public theorem cokernel_hasNoEmbeddedAssociatedPoints
    {X : Scheme.{u}} [IsLocallyNoetherian X]
    (F : X.Modules) [F.IsCoherent] (K : Subobject F)
    (hK : IsNowhereDenseCoherentSubobject F K)
    (hmax : ∀ L : Subobject F, IsNowhereDenseCoherentSubobject F L → L ≤ K) :
    AlgebraicGeometry.HasNoEmbeddedAssociatedPoints (cokernel K.arrow)
```

**`Stacks.AlgebraicGeometry.CoherentSubquotients.exists_denseOpen_cokernel_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentSubquotients/NowhereDense.lean, line 787](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentSubquotients/NowhereDense.lean#L787). The attribute's comment: “part (3): agreement on a dense open”.

> **[Stacks, Tag 02OL], part (3).** There is a dense open subset, meeting the support of `F`
> densely, over every open subset of which the quotient map is an isomorphism on sections.

```lean
public theorem exists_denseOpen_cokernel_iso
    {X : Scheme.{u}} [IsLocallyNoetherian X]
    (F : X.Modules) [F.IsCoherent] (K : Subobject F)
    (hK : IsNowhereDenseCoherentSubobject F K) :
    ∃ U : X.Opens,
      Dense (U : Set X) ∧
      Dense {x : ↥((⟨F.val, F.isSheaf⟩ :
            RingedSpace.ModuleSheaf.{u} X.toRingedSpace).supp) | (x : X) ∈ U} ∧
          ∀ V : X.Opens, V ≤ U →
            IsIso ((cokernel.π K.arrow).val.app (op V))
```

**`Stacks.AlgebraicGeometry.EmbeddedPoints.exists_greatest_isNowhereDenseCoherentSubobject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/EmbeddedPoints/Remove.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/EmbeddedPoints/Remove.lean#L138). The attribute's comment: “greatest subsheaf”.

> **Stacks Project, Tag 02OL, maximal subsheaf.** The coherent subsheaves whose support is
> nowhere dense in the support of `F` have a greatest member.

```lean
theorem exists_greatest_isNowhereDenseCoherentSubobject [IsLocallyNoetherian X]
    (F : X.Modules) [F.IsCoherent] :
    ∃ K : Subobject F,
      IsNowhereDenseCoherentSubobject F K ∧
        ∀ L : Subobject F, IsNowhereDenseCoherentSubobject F L → L ≤ K
```

**`Stacks.AlgebraicGeometry.EmbeddedPoints.supp_cokernel_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/EmbeddedPoints/Remove.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/EmbeddedPoints/Remove.lean#L216). The attribute's comment: “part (1): support of the quotient”.

> **Stacks Project, Tag 02OL, part (1).** The quotient has the same support.

```lean
theorem supp_cokernel_eq [IsLocallyNoetherian X] (F : X.Modules) [F.IsCoherent] (K : Subobject F)
    (hK : IsNowhereDenseCoherentSubobject F K) :
    (⟨(cokernel K.arrow).val, (cokernel K.arrow).isSheaf⟩ :
      RingedSpace.ModuleSheaf.{u} X.toRingedSpace).supp =
      (⟨F.val, F.isSheaf⟩ : RingedSpace.ModuleSheaf.{u} X.toRingedSpace).supp
```

**`Stacks.AlgebraicGeometry.EmbeddedPoints.cokernel_hasNoEmbeddedAssociatedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/EmbeddedPoints/Remove.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/EmbeddedPoints/Remove.lean#L245). The attribute's comment: “part (2): no embedded associated points”.

> **Stacks Project, Tag 02OL, part (2).** The quotient by a greatest nowhere dense coherent
> subobject has no embedded associated points.

```lean
theorem cokernel_hasNoEmbeddedAssociatedPoints [IsLocallyNoetherian X]
    (F : X.Modules) [F.IsCoherent] (K : Subobject F)
    (hK : IsNowhereDenseCoherentSubobject F K)
    (hmax : ∀ L : Subobject F, IsNowhereDenseCoherentSubobject F L → L ≤ K) :
    HasNoEmbeddedAssociatedPoints (cokernel K.arrow)
```

**`Stacks.AlgebraicGeometry.EmbeddedPoints.exists_denseOpen_cokernel_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/EmbeddedPoints/Remove.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/EmbeddedPoints/Remove.lean#L363). The attribute's comment: “part (3): agreement on a dense open”.

> **Stacks Project, Tag 02OL, part (3).** The canonical quotient map becomes an isomorphism on
> a dense open meeting the support densely.

```lean
theorem exists_denseOpen_cokernel_iso [IsLocallyNoetherian X] (F : X.Modules) [F.IsCoherent]
    (K : Subobject F) (hK : IsNowhereDenseCoherentSubobject F K) :
    ∃ U : X.Opens,
      Dense (U : Set X) ∧
      Dense {x : ↥((⟨F.val, F.isSheaf⟩ :
            RingedSpace.ModuleSheaf.{u} X.toRingedSpace).supp) | (x : X) ∈ U} ∧
          ∀ V : X.Opens, V ≤ U →
            IsIso ((cokernel.π K.arrow).val.app (op V))
```

## Tag 02OM, a lemma

[Tag 02OM](https://stacks.math.columbia.edu/tag/02OM) in the Stacks Project.

**`AlgebraicGeometry.hasNoEmbeddedPoints_annihilatorIdeal_subscheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/SchemeTheoreticSupport.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/SchemeTheoreticSupport.lean#L162). The attribute's comment: “absence of embedded points on the support”.

> **[Stacks, Tag 02OM].** The closed subscheme cut out by the annihilator of a coherent module
> with no embedded associated points has no embedded points.

```lean
theorem hasNoEmbeddedPoints_annihilatorIdeal_subscheme [IsLocallyNoetherian X]
    (F : X.Modules) [F.IsCoherent] (hF : HasNoEmbeddedAssociatedPoints F) :
    HasNoEmbeddedPoints (annihilatorIdeal' F).subscheme
```

**`AlgebraicGeometry.exists_isCoherent_submodule_eq_annihilatorIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/SchemeTheoreticSupport.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/SchemeTheoreticSupport.lean#L287). The attribute's comment: “coherence of the defining ideal”.

> **[Stacks, Tag 02OM].** The ideals cutting out the scheme-theoretic support over the affine
> opens are the sections of a coherent subsheaf of the structure sheaf, namely the annihilator
> sheaf of [Stacks, Tag 0H2H].

```lean
theorem exists_isCoherent_submodule_eq_annihilatorIdeal [IsLocallyNoetherian X]
    (F : X.Modules) [F.IsCoherent] :
    ∃ I : (SheafOfModules.unit X.ringCatSheaf).Submodule,
      I.toSheafOfModules.IsCoherent ∧
        I = Stacks.SheafOfModules.annihilatorSheaf X.toRingedSpace F ∧
          ∀ U : X.affineOpens, (annihilatorIdeal' F).ideal U =
            (show Ideal Γ(X, U.1) from I.toSubmodule.obj (op U.1))
```

**`AlgebraicGeometry.isCoherent_of_pushforward_iso_annihilatorIdeal_subscheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/SchemeTheoreticSupport.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/SchemeTheoreticSupport.lean#L319). The attribute's comment: “coherence of the descended sheaf”.

> **[Stacks, Tag 02OM].** Every quasi-coherent module on the scheme-theoretic support whose
> direct image is `F` is itself coherent.

```lean
theorem isCoherent_of_pushforward_iso_annihilatorIdeal_subscheme [IsLocallyNoetherian X]
    (F : X.Modules) [F.IsCoherent] (G : (annihilatorIdeal' F).subscheme.Modules)
    [G.IsQuasicoherent]
    (e : (Scheme.Modules.pushforward (annihilatorIdeal' F).subschemeι).obj G ≅ F) :
    G.IsCoherent
```

**`AlgebraicGeometry.hasNoEmbeddedAssociatedPoints_of_pushforward_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/SchemeTheoreticSupport.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/SchemeTheoreticSupport.lean#L336). The attribute's comment: “absence of embedded associated points on the descended sheaf”.

> **[Stacks, Tag 02OM].** Every quasi-coherent module on the scheme-theoretic support whose
> direct image is `F` inherits from `F` the absence of embedded associated points.

```lean
theorem hasNoEmbeddedAssociatedPoints_of_pushforward_iso [IsLocallyNoetherian X]
    (F : X.Modules) [F.IsCoherent] (hF : HasNoEmbeddedAssociatedPoints F)
    (G : (annihilatorIdeal' F).subscheme.Modules) [G.IsQuasicoherent]
    (e : (Scheme.Modules.pushforward (annihilatorIdeal' F).subschemeι).obj G ≅ F) :
    HasNoEmbeddedAssociatedPoints G
```

**`AlgebraicGeometry.exists_coherent_module_on_annihilatorIdeal_subscheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/SchemeTheoreticSupport.lean, line 414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/SchemeTheoreticSupport.lean#L414). The attribute's comment: “existence and properties of the descended sheaf”.

> **[Stacks, Tag 02OM].** A coherent module with no embedded associated points on a locally
> Noetherian scheme descends along the inclusion of its scheme-theoretic support to a coherent
> module with full support and again no embedded associated points.

```lean
theorem exists_coherent_module_on_annihilatorIdeal_subscheme [IsLocallyNoetherian X]
    (F : X.Modules) [F.IsCoherent] (hF : HasNoEmbeddedAssociatedPoints F) :
    ∃ G : (annihilatorIdeal' F).subscheme.Modules,
      G.IsCoherent ∧ HasNoEmbeddedAssociatedPoints G ∧
        SheafOfModules.supp G = Set.univ ∧
          Nonempty ((Scheme.Modules.pushforward
            (annihilatorIdeal' F).subschemeι).obj G ≅ F)
```

**`AlgebraicGeometry.annihilatorIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SchemeTheoreticSupport/Basic.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SchemeTheoreticSupport/Basic.lean#L142). The attribute's comment: “the ideal sheaf cutting out the support”. References: EGA IV (4.6.16); EGA IV (4.6.18); SGA 4 XVII (6.3.4), “special case”.

> **[Stacks, Tag 02OM] the ideal sheaf cutting out the scheme-theoretic support.** The
> annihilators of the sections of a coherent module on a locally Noetherian scheme form an ideal
> sheaf; the closed subscheme it cuts out is the scheme-theoretic support of the module.

```lean
noncomputable def annihilatorIdeal [IsLocallyNoetherian X] (F : X.Modules) [F.IsCoherent] :
    X.IdealSheafData
```

**`AlgebraicGeometry.exists_isCoherent_pushforward_iso_subschemeι_annihilatorIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SchemeTheoreticSupport/Basic.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SchemeTheoreticSupport/Basic.lean#L197). The attribute's comment: “existence of the coherent module on the support”.

> **[Stacks, Tag 02OM], the descended module.** A coherent module on a locally Noetherian
> scheme is the direct image of a coherent module on its scheme-theoretic support.
>
> This is [Stacks, Tag 087T]'s coherent descent applied to `annihilatorIdeal_smul_eq_zero`.

```lean
theorem exists_isCoherent_pushforward_iso_subschemeι_annihilatorIdeal [IsLocallyNoetherian X]
    (F : X.Modules) [F.IsCoherent] :
    ∃ G : (annihilatorIdeal F).subscheme.Modules, G.IsCoherent ∧
      Nonempty ((Scheme.Modules.pushforward (annihilatorIdeal F).subschemeι).obj G ≅ F)
```

**`AlgebraicGeometry.hasNoEmbeddedPoints_subscheme_annihilatorIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SchemeTheoreticSupport/Basic.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SchemeTheoreticSupport/Basic.lean#L345). The attribute's comment: “absence of embedded points on the support”.

> **[Stacks, Tag 02OM], no embedded points on the support.** If a coherent module on a locally
> Noetherian scheme has no embedded associated points, then the closed subscheme cut out by its
> annihilator has no embedded points.
>
> The subscheme's ring of functions over the preimage of an affine open `U` is
> `Γ(X, U) ⧸ Ann Γ(F, U)`, which has no embedded primes by Tag 02M8 because `Γ(F, U)` has none by
> `sections_hasNoEmbeddedAssociatedPrimes`; an embedded point of the subscheme would give two
> nested associated primes there.

```lean
theorem hasNoEmbeddedPoints_subscheme_annihilatorIdeal [IsLocallyNoetherian X] (F : X.Modules)
    [F.IsCoherent] (hF : HasNoEmbeddedAssociatedPoints F) :
    HasNoEmbeddedPoints (annihilatorIdeal F).subscheme
```

**`AlgebraicGeometry.exists_isCoherent_pushforward_iso_of_hasNoEmbeddedAssociatedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SchemeTheoreticSupport/Basic.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SchemeTheoreticSupport/Basic.lean#L400). The attribute's comment: “the descended module on a support without embedded points”.

> **[Stacks, Tag 02OM].** A coherent module without embedded associated points on a locally
> Noetherian scheme is the direct image of a coherent module on a closed subscheme without
> embedded points, and that module has full support.
>
> This is the source's statement with clause (b) — that the descended module itself has no embedded
> associated points — omitted; see the module docstring.

```lean
theorem exists_isCoherent_pushforward_iso_of_hasNoEmbeddedAssociatedPoints [IsLocallyNoetherian X]
    (F : X.Modules) [F.IsCoherent] (hF : HasNoEmbeddedAssociatedPoints F) :
    HasNoEmbeddedPoints (annihilatorIdeal F).subscheme ∧
      ∃ G : (annihilatorIdeal F).subscheme.Modules, G.IsCoherent ∧
        SheafOfModules.supp G = Set.univ ∧
        Nonempty ((Scheme.Modules.pushforward (annihilatorIdeal F).subschemeι).obj G ≅ F)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.annihilatorIdeal'`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/AnnihilatorSupport.lean#L56), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/SchemeTheoreticSupport.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/SchemeTheoreticSupport.lean#L218) (StacksFrontier): “the ideal sheaf cutting out the support”.
- [`Stacks.SheafOfModules.isCoherent_annihilatorSheaf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/AnnihilatorCoherent.lean#L75), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/SchemeTheoreticSupport.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/SchemeTheoreticSupport.lean#L220) (StacksFrontier): “coherence of the annihilator”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.4, Tag 05AJ](https://stacks.math.columbia.edu/tag/05AJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
