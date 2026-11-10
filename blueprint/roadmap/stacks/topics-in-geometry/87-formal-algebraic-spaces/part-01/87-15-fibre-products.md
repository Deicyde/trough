---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_of_etaleCover, AlgebraicGeometry.FormalSpace.not_forall_isFormalAlgebraicSpace_of_etaleCover, AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_of_etaleCover_of_admitsCoproductIndex, AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_pullback_of_isSeparated, AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_pullback_of_isAffineFormal, AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_pullback_of_representableDiagonal, AlgebraicGeometry.FormalSpace.hasPullbacks_formalAlgebraicSpaces, AlgebraicGeometry.FormalSpace.exists_iso_reduction_fibreProduct
statement: formalized
proof: formalized
---

# 87.15 Fibre products

Section 87.15 of the Stacks Project, [Tag 0AJ0](https://stacks.math.columbia.edu/tag/0AJ0). 5 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AJ1, a lemma

[Tag 0AJ1](https://stacks.math.columbia.edu/tag/0AJ1) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_of_etaleCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleCover.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleCover.lean#L237).

> **Stacks 0AJ1.** A jointly surjective family of representable étale maps from formal
> algebraic spaces makes its target a formal algebraic space, provided the target satisfies the
> set-theoretic condition of Stacks 0AIS.

```lean
theorem isFormalAlgebraicSpace_of_etaleCover {I : Type (u + 1)}
    (X : FppfSheaf B S hS) (Xi : I → FppfSheaf B S hS) (f : ∀ i, Xi i ⟶ X)
    (hXi : ∀ i, IsFormalAlgebraicSpace B S hS (Xi i))
    (hf : ∀ i, ∃ hfi : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (f i).hom,
      Space.HasPropertyULift.{u + 1} B S hS
        (fun _ _ g ↦ Space.IsEtaleULift.{u + 1} B S hS g.hom) (f i).hom hfi)
    (hsurj : letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) :=
        Sheaf.instHasColimitsOfSize
      Sheaf.IsLocallySurjective (Sigma.desc f))
    (hXset : SatisfiesSetTheoreticCondition B S hS X) :
    IsFormalAlgebraicSpace B S hS X
```

**`AlgebraicGeometry.FormalSpace.not_forall_isFormalAlgebraicSpace_of_etaleCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleCoverCounterexample.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleCoverCounterexample.lean#L261). The attribute's comment: “the statement as printed is false: over any nonempty S, the sheaf of locally constant functions to a discrete set as large as the size cutoff of the site, with the family of its constant sections out of h_S, satisfies (a)-(c) but fails the set-theoretic condition of Stacks 0AIS; the corrected form is AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_of_etaleCover_of_admitsCoproductIndex”.

> **Stacks 0AJ1 is false without a bound on the index.** Over a nonempty scheme `S` of a big
> fppf site, it is not the case that every fppf sheaf `X` with a family `{Xᵢ ⟶ X}` satisfying
> conditions (a), (b) and (c) of Stacks 0AJ1 is a formal algebraic space: the sheaf of locally
> constant functions with values in a discrete set as large as the cutoff of the site, with its
> family of constant functions out of `h_S`, satisfies (a)–(c) but not the set-theoretic
> condition of Stacks 0AIS that Definition 0AIM asks of a formal algebraic space.

```lean
theorem not_forall_isFormalAlgebraicSpace_of_etaleCover [Nonempty S] :
    letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) := Sheaf.instHasColimitsOfSize
    ¬ ∀ (I : Type (u + 1)) (X : FppfSheaf B S hS) (Xi : I → FppfSheaf B S hS)
      (f : ∀ i, Xi i ⟶ X),
      (∀ i, IsFormalAlgebraicSpace B S hS (Xi i)) →
      (∀ i, ∃ hfi : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (f i).hom,
        Space.HasPropertyULift.{u + 1} B S hS
          (fun _ _ g ↦ Space.IsEtaleULift.{u + 1} B S hS g.hom) (f i).hom hfi) →
      Sheaf.IsLocallySurjective (Sigma.desc f) →
      IsFormalAlgebraicSpace B S hS X
```

**`AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_of_etaleCover_of_admitsCoproductIndex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleCoverSetCondition.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleCoverSetCondition.lean#L318). The attribute's comment: “corrected form: the printed statement is false for an index set as large as the size cutoff of the site, the target then failing the set-theoretic condition of Stacks 0AIS that Definition 0AIM asks of a formal algebraic space (AlgebraicGeometry.FormalSpace.not_forall_isFormalAlgebraicSpace_of_etaleCover); stated, under the source's hypotheses (a)-(c), for an index admissible for coproducts in the site, the proviso 'I not too large' of Stacks 0AIS observation (3), and with that condition derived, not assumed”.

> **Stacks 0AJ1, for an index which is not too large.** Let `{Xᵢ ⟶ X}_{i ∈ I}` be a family of
> maps of fppf sheaves on the big fppf site of `S`, indexed by a type admissible for coproducts in
> the site (of cardinality below the cofinality of its size cutoff; for instance a countable one),
> such that (a) each `Xᵢ` is a formal algebraic space over `S`, (b) each `Xᵢ ⟶ X` is
> representable by algebraic spaces and étale, and (c) `∐ Xᵢ ⟶ X` is a surjection of sheaves.
> Then `X` is a formal algebraic space over `S`.
>
> The atlas is the source's: the atlases of the `Xᵢ` composed with the maps `Xᵢ ⟶ X`
> (`AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_of_etaleCover`). The set-theoretic
> condition of Stacks 0AIS, which Definition 0AIM asks of `X` as well, is not assumed: it is
> derived from (a)–(c) by
> `AlgebraicGeometry.FormalSpace.satisfiesSetTheoreticCondition_of_etaleCover`, which is where
> the size of the index enters, as observation (3) of Remark 0AIS says it must. Without a bound
> on the index the statement is false
> (`AlgebraicGeometry.FormalSpace.not_forall_isFormalAlgebraicSpace_of_etaleCover`).

```lean
theorem isFormalAlgebraicSpace_of_etaleCover_of_admitsCoproductIndex
    {I : Type (u + 1)} [Small.{u} I] [B.AdmitsCoproductIndex I]
    (X : FppfSheaf B S hS) (Xi : I → FppfSheaf B S hS) (f : ∀ i, Xi i ⟶ X)
    (hXi : ∀ i, IsFormalAlgebraicSpace B S hS (Xi i))
    (hf : ∀ i, ∃ hfi : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (f i).hom,
      Space.HasPropertyULift.{u + 1} B S hS
        (fun _ _ g ↦ Space.IsEtaleULift.{u + 1} B S hS g.hom) (f i).hom hfi)
    (hsurj : letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) :=
        Sheaf.instHasColimitsOfSize
      Sheaf.IsLocallySurjective (Sigma.desc f)) :
    IsFormalAlgebraicSpace B S hS X
```

## Tag 0AJ2, a lemma

[Tag 0AJ2](https://stacks.math.columbia.edu/tag/0AJ2) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_pullback_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProduct.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProduct.lean#L189). The attribute's comment: “the case of a base separated in the sense of clause (2) of Stacks 0AJ6, where Stacks 0AN3 clause (1) makes every fibre product of two affine formal algebraic spaces over the base an affine formal algebraic space, in place of the directed colimit argument of Stacks 0AIU that the general case needs”.

> **Stacks 0AJ2** for a base which is separated in the sense of clause (2) of Stacks 0AJ6.
> The fibre product of two formal algebraic spaces over such a base, whose relative products of
> representables are representable, is a formal algebraic space.
>
> Separatedness enters only through Stacks 0AN3 clause (1): it makes the fibre product of two
> affine formal algebraic spaces over `Z` again an affine formal algebraic space, which is the
> hypothesis `hstage` of `isFormalAlgebraicSpace_pullback_of_affineStages`. The set-theoretic
> condition of Stacks 0AIS on `X ×_Z Y` and on the intermediate fibre products follows from
> `hZrep` alone, by `satisfiesSetTheoreticCondition_pullback_of_hasRepresentableRelativeProducts`
> over `Z` and, after the pasting isomorphism, over `Z` again.

```lean
theorem isFormalAlgebraicSpace_pullback_of_isSeparated
    {X Y Z : FppfSheaf B S hS} (p : X ⟶ Z) (q : Y ⟶ Z)
    (hZrep : HasRepresentableRelativeProducts B S hS Z)
    (hZsep : IsSeparated B S hS Z)
    (hX : IsFormalAlgebraicSpace B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y) :
    IsFormalAlgebraicSpace B S hS (pullback p q)
```

**`AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_pullback_of_isAffineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProduct.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProduct.lean#L219). The attribute's comment: “the case of two affine formal algebraic spaces over a base separated in the sense of clause (2) of Stacks 0AJ6, where Stacks 0AN3 clause (1) makes the fibre product of the two an affine formal algebraic space”.

> **Stacks 0AJ2** for a separated base, on two affine formal algebraic spaces: an affine
> formal algebraic space is a formal algebraic space, so this is a special case of
> `isFormalAlgebraicSpace_pullback_of_isSeparated`.

```lean
theorem isFormalAlgebraicSpace_pullback_of_isAffineFormal
    {X Y Z : FppfSheaf B S hS} (p : X ⟶ Z) (q : Y ⟶ Z)
    (hZrep : HasRepresentableRelativeProducts B S hS Z)
    (hZsep : IsSeparated B S hS Z)
    (hX : IsAffineFormalAlgebraicSpace B S hS X)
    (hY : IsAffineFormalAlgebraicSpace B S hS Y) :
    IsFormalAlgebraicSpace B S hS (pullback p q)
```

**`AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_pullback_of_representableDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProductRepresentableDiagonal.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProductRepresentableDiagonal.lean#L211).

> **Stacks 0AJ2.** Let `S` be a scheme, let `X` and `Y` be formal algebraic spaces over `S` and
> let `Z` be a sheaf on `(Sch/S)_fppf` whose diagonal is representable by algebraic spaces. For
> maps of sheaves `p : X ⟶ Z` and `q : Y ⟶ Z`, the fibre product `X ×_Z Y` is a formal algebraic
> space.

```lean
theorem isFormalAlgebraicSpace_pullback_of_representableDiagonal
    {X Y Z : FppfSheaf B S hS} (p : X ⟶ Z) (q : Y ⟶ Z)
    (hZ : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (diag Z.obj))
    (hX : IsFormalAlgebraicSpace B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y) :
    IsFormalAlgebraicSpace B S hS (pullback p q)
```

## Tag 0AJ3, a lemma

[Tag 0AJ3](https://stacks.math.columbia.edu/tag/0AJ3) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.hasPullbacks_formalAlgebraicSpaces`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProductFormalBase.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProductFormalBase.lean#L292).

> **Stacks 0AJ3.** The category of formal algebraic spaces over a scheme `S` has fibre
> products.
>
> The fibre product is the fibre product of the underlying fppf sheaves: that is again a formal
> algebraic space by
> `AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_pullback_of_isFormalAlgebraicSpace`, so the
> full inclusion into fppf sheaves creates fibre products and the subcategory inherits them.

```lean
instance hasPullbacks_formalAlgebraicSpaces : HasPullbacks (FormalAlgebraicSpaces B S hS)
```

## Tag 0CB9, a lemma

[Tag 0CB9](https://stacks.math.columbia.edu/tag/0CB9) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_iso_reduction_fibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProductReduction.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProductReduction.lean#L150). The attribute's comment: “with reductions of the five spaces, and both fibre products, as hypotheses”.

> **Stacks 0CB9.** Let `X ⟶ Z` and `Y ⟶ Z` be morphisms of formal algebraic spaces over `S`,
> let `iX : Xred ⟶ X`, `iY : Yred ⟶ Y` and `iZ : Zred ⟶ Z` be reductions and let `Xred ⟶ Zred` and
> `Yred ⟶ Zred` be compatible with the two given morphisms. Let `P` be a fibre product of `X` and
> `Y` over `Z`, let `Q` be a fibre product of `Xred` and `Yred` over `Zred`, and let
> `iP : Pred ⟶ P` and `iQ : Qred ⟶ Q` be reductions of those two fibre products. Then the
> inclusions of the reductions induce a morphism `Q ⟶ P` over which `Qred` and `Pred` are
> isomorphic: `(X ×_Z Y)_red = (X_red ×_{Z_red} Y_red)_red`.

```lean
theorem exists_iso_reduction_fibreProduct
    (_hX : IsFormalAlgebraicSpace B S hS X) (_hY : IsFormalAlgebraicSpace B S hS Y)
    (_hZ : IsFormalAlgebraicSpace B S hS Z)
    (hiX : IsReduction B S hS X Xred iX) (hiY : IsReduction B S hS Y Yred iY)
    (hiZ : IsReduction B S hS Z Zred iZ)
    (hfred : fred ≫ iZ = iX ≫ f) (hgred : gred ≫ iZ = iY ≫ g)
    (hP : IsPullback p₁ p₂ f g) (hQ : IsPullback q₁ q₂ fred gred)
    (hiP : IsReduction B S hS P Pred iP) (hiQ : IsReduction B S hS Q Qred iQ) :
    ∃ (cmp : Q ⟶ P) (e : Qred ≅ Pred),
      cmp ≫ p₁ = q₁ ≫ iX ∧ cmp ≫ p₂ = q₂ ≫ iY ∧ e.hom ≫ iP = iQ ≫ cmp
```

## Tag 0AN2, a lemma

[Tag 0AN2](https://stacks.math.columbia.edu/tag/0AN2) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.relativelyRepresentable_pullback_diagonal_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/DiagonalRepresentable.lean, line 1039](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/DiagonalRepresentable.lean#L1039). The attribute's comment: “representable by schemes, for a morphism whose source is an arbitrary formal algebraic space”.

> **Stacks 0AN2, representability, for a morphism whose source is an *arbitrary* formal
> algebraic space:** the relative diagonal of a morphism of fppf sheaves out of a formal
> algebraic space is representable by objects of the big fppf site of `S`.
>
> This discharges the hypothesis of
> `AlgebraicGeometry.FormalSpace.relativelyRepresentable_pullback_diagonal`, the relative
> diagonal being a base change of the absolute one.

```lean
theorem relativelyRepresentable_pullback_diagonal_of_isFormalAlgebraicSpace
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) (hX : IsFormalAlgebraicSpace B S hS X) :
    (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).relativelyRepresentable
      (pullback.diagonal f)
```

**`AlgebraicGeometry.FormalSpace.relative_locallyOfFiniteType_pullback_diagonal_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/DiagonalRepresentable.lean, line 1227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/DiagonalRepresentable.lean#L1227). The attribute's comment: “locally of finite type, for a morphism whose source is an arbitrary formal algebraic space”.

> **Stacks 0AN2, local finite type, for a morphism whose source is an *arbitrary* formal
> algebraic space:** every represented base change of the relative diagonal of a morphism of fppf
> sheaves out of a formal algebraic space is a locally of finite type morphism of schemes.
>
> This discharges the hypothesis of
> `AlgebraicGeometry.FormalSpace.relative_pullback_diagonal` for local finite type, the relative
> diagonal being a base change of the absolute one.

```lean
theorem relative_locallyOfFiniteType_pullback_diagonal_of_isFormalAlgebraicSpace
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) (hX : IsFormalAlgebraicSpace B S hS X) :
    (MorphismProperty.inverseImage
      (@AlgebraicGeometry.LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)) (pullback.diagonal f)
```

**`AlgebraicGeometry.FormalSpace.relative_locallyQuasiFinite_pullback_diagonal_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/DiagonalRepresentable.lean, line 1241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/DiagonalRepresentable.lean#L1241). The attribute's comment: “locally quasi-finite, for a morphism whose source is an arbitrary formal algebraic space”.

> **Stacks 0AN2, local quasi-finiteness, for a morphism whose source is an *arbitrary* formal
> algebraic space:** every represented base change of the relative diagonal is a locally
> quasi-finite, locally of finite type morphism of schemes.

```lean
theorem relative_locallyQuasiFinite_pullback_diagonal_of_isFormalAlgebraicSpace
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) (hX : IsFormalAlgebraicSpace B S hS X) :
    (MorphismProperty.inverseImage
      ((@AlgebraicGeometry.LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u}) ⊓
        (@AlgebraicGeometry.LocallyQuasiFinite.{u} : MorphismProperty Scheme.{u}))
      (BigFppfOver.toScheme B S hS)).relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)) (pullback.diagonal f)
```

**`AlgebraicGeometry.FormalSpace.relative_isSeparated_pullback_diagonal_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/DiagonalRepresentable.lean, line 1255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/DiagonalRepresentable.lean#L1255). The attribute's comment: “separated, for a morphism whose source is an arbitrary formal algebraic space”.

> **Stacks 0AN2, separatedness, for a morphism whose source is an *arbitrary* formal
> algebraic space:** every represented base change of the relative diagonal is a separated
> morphism of schemes.

```lean
theorem relative_isSeparated_pullback_diagonal_of_isFormalAlgebraicSpace
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) (hX : IsFormalAlgebraicSpace B S hS X) :
    (MorphismProperty.inverseImage
      (@AlgebraicGeometry.IsSeparated.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)) (pullback.diagonal f)
```

**`AlgebraicGeometry.FormalSpace.relativelyRepresentable_pullback_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean#L114). The attribute's comment: “representability, by base change from the representability assertion of Stacks 0AIP for the absolute diagonal of the source, which is available for an arbitrary formal algebraic space in StacksFrontier.AlgebraicGeometry.FormalSpace.DiagonalRepresentable, where this reduction is fed it”.

> If the absolute diagonal of an fppf sheaf `X` on the big fppf site of `S` is representable by
> objects of the site, then so is the relative diagonal of every morphism out of `X`.

```lean
theorem relativelyRepresentable_pullback_diagonal {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).relativelyRepresentable
      (diag X)) :
    (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).relativelyRepresentable
      (pullback.diagonal f)
```

**`AlgebraicGeometry.FormalSpace.relative_pullback_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean#L132). The attribute's comment: “the locally quasi-finite, locally of finite type and separated assertions at once, by base change from the corresponding assertion of Stacks 0AIP for the absolute diagonal of the source, taken uniformly in the property of morphisms of the site; all three are available for an arbitrary formal algebraic space in StacksFrontier.AlgebraicGeometry.FormalSpace.DiagonalRepresentable, where this reduction is fed them”.

> If every represented base change of the absolute diagonal of an fppf sheaf `X` on the big
> fppf site of `S` is a morphism of the site with `Q`, then the same holds for the relative
> diagonal of every morphism out of `X`.

```lean
theorem relative_pullback_diagonal (Q : MorphismProperty (BigFppfOver B S hS))
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : Q.relative (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)) (diag X)) :
    Q.relative (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (pullback.diagonal f)
```

**`AlgebraicGeometry.FormalSpace.relativelyRepresentable_pullback_diagonal_of_isAffineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean#L266). The attribute's comment: “representable by schemes, for a morphism whose source is an affine formal algebraic space”.

> The relative diagonal of a morphism out of an affine formal algebraic space is representable
> by objects of the site.

```lean
theorem relativelyRepresentable_pullback_diagonal_of_isAffineFormal
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) (hX : IsAffineFormalAlgebraicSpace B S hS X) :
    (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).relativelyRepresentable
      (pullback.diagonal f)
```

**`AlgebraicGeometry.FormalSpace.relative_locallyQuasiFinite_pullback_diagonal_of_isAffineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean#L276). The attribute's comment: “locally quasi-finite, for a morphism whose source is an affine formal algebraic space”.

> Every represented base change of the relative diagonal of a morphism out of an affine formal
> algebraic space is a locally quasi-finite, locally of finite type morphism of schemes.

```lean
theorem relative_locallyQuasiFinite_pullback_diagonal_of_isAffineFormal
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) (hX : IsAffineFormalAlgebraicSpace B S hS X) :
    (MorphismProperty.inverseImage
      ((@AlgebraicGeometry.LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u}) ⊓
        (@AlgebraicGeometry.LocallyQuasiFinite.{u} : MorphismProperty Scheme.{u}))
      (BigFppfOver.toScheme B S hS)).relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)) (pullback.diagonal f)
```

**`AlgebraicGeometry.FormalSpace.relative_locallyOfFiniteType_pullback_diagonal_of_isAffineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean#L292). The attribute's comment: “locally of finite type, for a morphism whose source is an affine formal algebraic space”.

> Every represented base change of the relative diagonal of a morphism out of an affine formal
> algebraic space is a locally of finite type morphism of schemes.

```lean
theorem relative_locallyOfFiniteType_pullback_diagonal_of_isAffineFormal
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) (hX : IsAffineFormalAlgebraicSpace B S hS X) :
    (MorphismProperty.inverseImage
      (@AlgebraicGeometry.LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)) (pullback.diagonal f)
```

**`AlgebraicGeometry.FormalSpace.relative_isSeparated_pullback_diagonal_of_isAffineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean#L305). The attribute's comment: “separated, for a morphism whose source is an affine formal algebraic space”.

> Every represented base change of the relative diagonal of a morphism out of an affine formal
> algebraic space is a separated morphism of schemes.

```lean
theorem relative_isSeparated_pullback_diagonal_of_isAffineFormal
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) (hX : IsAffineFormalAlgebraicSpace B S hS X) :
    (MorphismProperty.inverseImage
      (@AlgebraicGeometry.IsSeparated.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)) (pullback.diagonal f)
```

**`AlgebraicGeometry.FormalSpace.mono_pullback_diagonal_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean#L320). The attribute's comment: “monomorphism, for a morphism whose source is an arbitrary formal algebraic space”.

> The relative diagonal of a morphism of fppf sheaves out of a formal algebraic space is a
> monomorphism, which by **Stacks 0AQB** is the monomorphism condition for a morphism of formal
> algebraic spaces.

```lean
theorem mono_pullback_diagonal_of_isFormalAlgebraicSpace {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (_hX : IsFormalAlgebraicSpace B S hS X) : Mono (pullback.diagonal f)
```

Declarations registered for the tag:

- [`CategoryTheory.Limits.pullback.instIsSplitMonoDiagonal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.pullback.instIsSplitMonoDiagonal#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean#L326) (StacksFrontier): “monomorphism”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.15, Tag 0AJ0](https://stacks.math.columbia.edu/tag/0AJ0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
