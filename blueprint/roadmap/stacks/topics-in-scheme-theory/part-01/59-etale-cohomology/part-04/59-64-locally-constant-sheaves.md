---
declaration: section
origin: cited
lean: Stacks.ConstantSheaf.IsLocallyConstant, Stacks.ConstantSheaf.IsFiniteLocallyConstant, CategoryTheory.Sheaf.IsConstant, AlgebraicGeometry.isLocallyConstant_smallEtaleSheafPullback, Stacks.ConstantSheaf.isLocallyConstant_finiteEtalePushforward, Stacks.ConstantSheaf.isFiniteLocallyConstant_finiteEtalePushforward, Stacks.ConstantSheaf.isLocallyConstant_finiteEtalePushforward_abelian, Stacks.ConstantSheaf.isFiniteLocallyConstant_finiteEtalePushforward_abelian
statement: formalized
proof: formalized
---

# 59.64 Locally constant sheaves

Section 59.64 of the Stacks Project, [Tag 09Y8](https://stacks.math.columbia.edu/tag/09Y8). 8 tags here are carried by 17 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03RU, a definition

[Tag 03RU](https://stacks.math.columbia.edu/tag/03RU) in the Stacks Project.

**`Stacks.ConstantSheaf.IsLocallyConstant`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/Defs.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/Defs.lean#L73). The attribute's comment: “finite locally constant sheaves of sets and of abelian groups”. References: EGA 0 (3.6.1), “locally simple”; SGA 3 X (9.2.1), “(2), (4)”; SGA 4 IX (2.0), “locally constant”.

> **Stacks 093Q (2).** A sheaf is locally constant if every object of the site has a covering
> on each member of which its restriction is a constant sheaf.

```lean
class IsLocallyConstant [∀ U : C, HasWeakSheafify (J.over U) D] (F : Sheaf J D) : Prop
```

**`Stacks.ConstantSheaf.IsFiniteLocallyConstant`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/Defs.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/Defs.lean#L86). The attribute's comment: “finite locally constant sheaves of sets and of abelian groups”.

> **Stacks 093Q (3).** A sheaf with values in a concrete category is finite locally constant
> if every object of the site has a covering on each member of which it is a constant sheaf with
> finite underlying value. For `Type` and `Grp`, this is respectively the source's notion for
> sheaves of sets and sheaves of groups.

```lean
class IsFiniteLocallyConstant {FD : D → D → Type*} {CD : D → Type w}
    [∀ X Y, FunLike (FD X Y) (CD X) (CD Y)] [ConcreteCategory.{w} D FD]
    [∀ U : C, HasWeakSheafify (J.over U) D] (F : Sheaf J D) : Prop
```

Declarations registered for the tag:

- [`CategoryTheory.Sheaf.IsConstant`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.IsConstant#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/Defs.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/Defs.lean#L61) (StacksFrontier): “constant sheaves of sets, of abelian groups and of Lambda-modules”. References: EGA 0 (3.6.1); SGA 4 IV (2.7.5); SGA 4 IV (4.3.4); SGA 4 IX (2.0).

## Tag 095A, a lemma

[Tag 095A](https://stacks.math.columbia.edu/tag/095A) in the Stacks Project.

**`AlgebraicGeometry.isLocallyConstant_smallEtaleSheafPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocallyConstantPullback/SmallEtaleInverseImage.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocallyConstantPullback/SmallEtaleInverseImage.lean#L129). The attribute's comment: “small étale inverse image”.

> **Tag 093R for small étale sites.** The inverse image of a locally constant sheaf along a
> morphism of small étale sites is locally constant, for arbitrary coefficients.

```lean
public theorem isLocallyConstant_smallEtaleSheafPullback
    (F : Sheaf (SmallEtale.topology B S.obj S.property) A)
    [Stacks.ConstantSheaf.IsLocallyConstant (SmallEtale.topology B S.obj S.property) F] :
    Stacks.ConstantSheaf.IsLocallyConstant (SmallEtale.topology B T.obj T.property)
      (((smallEtaleBaseChange B f).sheafPullback A
        (SmallEtale.topology B S.obj S.property)
        (SmallEtale.topology B T.obj T.property)).obj F)
```

## Tag 095B, a lemma

[Tag 095B](https://stacks.math.columbia.edu/tag/095B) in the Stacks Project.

**`Stacks.ConstantSheaf.isLocallyConstant_finiteEtalePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/FiniteEtalePushforward/LocallyQConstant.lean, line 486](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/FiniteEtalePushforward/LocallyQConstant.lean#L486). The attribute's comment: “locally constant sheaves of sets”.

> Direct image of a locally constant étale sheaf of sets along a finite étale
> morphism is locally constant.

```lean
public theorem isLocallyConstant_finiteEtalePushforward {X Y : Scheme.{u}}
    (f : X ⟶ Y) [IsFinite f] [Etale f]
    (F : Sheaf (smallEtaleTopology X) (Type (max (u + 1) v)))
    [Stacks.ConstantSheaf.IsLocallyConstant (smallEtaleTopology X) F] :
    Stacks.ConstantSheaf.IsLocallyConstant (smallEtaleTopology Y)
      (((Stacks.EtaleCohomology.smallEtaleBaseChange f).sheafPushforwardContinuous
        (Type (max (u + 1) v)) (smallEtaleTopology Y) (smallEtaleTopology X)).obj F)
```

**`Stacks.ConstantSheaf.isFiniteLocallyConstant_finiteEtalePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/FiniteEtalePushforward/LocallyQConstant.lean, line 502](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/FiniteEtalePushforward/LocallyQConstant.lean#L502). The attribute's comment: “finite locally constant sheaves of sets”.

> Direct image of a finite locally constant étale sheaf of sets along a finite
> étale morphism is finite locally constant.

```lean
public theorem isFiniteLocallyConstant_finiteEtalePushforward {X Y : Scheme.{u}}
    (f : X ⟶ Y) [IsFinite f] [Etale f]
    (F : Sheaf (smallEtaleTopology X) (Type (max (u + 1) v)))
    [Stacks.ConstantSheaf.IsFiniteLocallyConstant (smallEtaleTopology X) F] :
    Stacks.ConstantSheaf.IsFiniteLocallyConstant (smallEtaleTopology Y)
      (((Stacks.EtaleCohomology.smallEtaleBaseChange f).sheafPushforwardContinuous
        (Type (max (u + 1) v)) (smallEtaleTopology Y) (smallEtaleTopology X)).obj F)
```

**`Stacks.ConstantSheaf.isLocallyConstant_finiteEtalePushforward_abelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/FiniteEtalePushforward/LocallyQConstant.lean, line 518](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/FiniteEtalePushforward/LocallyQConstant.lean#L518). The attribute's comment: “locally constant sheaves of abelian groups”.

> Direct image of a locally constant étale sheaf of abelian groups along a
> finite étale morphism is locally constant.

```lean
public theorem isLocallyConstant_finiteEtalePushforward_abelian {X Y : Scheme.{u}}
    (f : X ⟶ Y) [IsFinite f] [Etale f]
    [∀ U : X.Etale, HasWeakSheafify ((smallEtaleTopology X).over U) AddCommGrpCat.{max (u + 1) v}]
    [∀ V : Y.Etale, HasWeakSheafify ((smallEtaleTopology Y).over V) AddCommGrpCat.{max (u + 1) v}]
    (F : Sheaf (smallEtaleTopology X) AddCommGrpCat.{max (u + 1) v})
    [Stacks.ConstantSheaf.IsLocallyConstant (smallEtaleTopology X) F] :
    Stacks.ConstantSheaf.IsLocallyConstant (smallEtaleTopology Y)
      (((Stacks.EtaleCohomology.smallEtaleBaseChange f).sheafPushforwardContinuous
        AddCommGrpCat.{max (u + 1) v} (smallEtaleTopology Y) (smallEtaleTopology X)).obj F)
```

**`Stacks.ConstantSheaf.isFiniteLocallyConstant_finiteEtalePushforward_abelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/FiniteEtalePushforward/LocallyQConstant.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/FiniteEtalePushforward/LocallyQConstant.lean#L536). The attribute's comment: “finite locally constant sheaves of abelian groups”.

> Direct image of a finite locally constant étale sheaf of abelian groups
> along a finite étale morphism is finite locally constant.

```lean
public theorem isFiniteLocallyConstant_finiteEtalePushforward_abelian {X Y : Scheme.{u}}
    (f : X ⟶ Y) [IsFinite f] [Etale f]
    [∀ U : X.Etale, HasWeakSheafify ((smallEtaleTopology X).over U) AddCommGrpCat.{max (u + 1) v}]
    [∀ V : Y.Etale, HasWeakSheafify ((smallEtaleTopology Y).over V) AddCommGrpCat.{max (u + 1) v}]
    (F : Sheaf (smallEtaleTopology X) AddCommGrpCat.{max (u + 1) v})
    [Stacks.ConstantSheaf.IsFiniteLocallyConstant (smallEtaleTopology X) F] :
    Stacks.ConstantSheaf.IsFiniteLocallyConstant (smallEtaleTopology Y)
      (((Stacks.EtaleCohomology.smallEtaleBaseChange f).sheafPushforwardContinuous
        AddCommGrpCat.{max (u + 1) v} (smallEtaleTopology Y) (smallEtaleTopology X)).obj F)
```

**`Stacks.ConstantSheaf.isLocallyConstant_finiteEtalePushforward_modules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/FiniteEtalePushforward/LocallyQConstant.lean, line 554](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/FiniteEtalePushforward/LocallyQConstant.lean#L554). The attribute's comment: “locally constant sheaves of modules”.

> Direct image of a locally constant étale sheaf of modules along a finite
> étale morphism is locally constant.

```lean
public theorem isLocallyConstant_finiteEtalePushforward_modules {X Y : Scheme.{u}}
    (f : X ⟶ Y) [IsFinite f] [Etale f]
    (R : Type r) [Ring R]
    [∀ U : X.Etale, HasWeakSheafify ((smallEtaleTopology X).over U) (ModuleCat.{max (u + 1) v} R)]
    [∀ V : Y.Etale, HasWeakSheafify ((smallEtaleTopology Y).over V) (ModuleCat.{max (u + 1) v} R)]
    (F : Sheaf (smallEtaleTopology X) (ModuleCat.{max (u + 1) v} R))
    [Stacks.ConstantSheaf.IsLocallyConstant (smallEtaleTopology X) F] :
    Stacks.ConstantSheaf.IsLocallyConstant (smallEtaleTopology Y)
      (((Stacks.EtaleCohomology.smallEtaleBaseChange f).sheafPushforwardContinuous
        (ModuleCat.{max (u + 1) v} R) (smallEtaleTopology Y) (smallEtaleTopology X)).obj F)
```

**`Stacks.ConstantSheaf.isFiniteTypeLocallyConstant_finiteEtalePushforward_modules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/FiniteEtalePushforward/LocallyQConstant.lean, line 573](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/FiniteEtalePushforward/LocallyQConstant.lean#L573). The attribute's comment: “finite-type locally constant sheaves of modules”.

> Direct image of a finite-type locally constant étale sheaf of modules
> along a finite étale morphism is finite-type locally constant.

```lean
public theorem isFiniteTypeLocallyConstant_finiteEtalePushforward_modules {X Y : Scheme.{u}}
    (f : X ⟶ Y) [IsFinite f] [Etale f]
    (R : Type r) [Ring R]
    [∀ U : X.Etale, HasWeakSheafify ((smallEtaleTopology X).over U) (ModuleCat.{max (u + 1) v} R)]
    [∀ V : Y.Etale, HasWeakSheafify ((smallEtaleTopology Y).over V) (ModuleCat.{max (u + 1) v} R)]
    (F : Sheaf (smallEtaleTopology X) (ModuleCat.{max (u + 1) v} R))
    (hF : Stacks.ConstantSheaf.IsFiniteTypeLocallyConstant R (smallEtaleTopology X) F) :
    Stacks.ConstantSheaf.IsFiniteTypeLocallyConstant R (smallEtaleTopology Y)
      (((Stacks.EtaleCohomology.smallEtaleBaseChange f).sheafPushforwardContinuous
        (ModuleCat.{max (u + 1) v} R) (smallEtaleTopology Y) (smallEtaleTopology X)).obj F)
```

## Tag 03RV, a lemma

[Tag 03RV](https://stacks.math.columbia.edu/tag/03RV) in the Stacks Project.

**`Stacks.EtaleCohomology.isFiniteLocallyConstant_iff_finiteEtaleRepresentable_of_descent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/EtaleLocalRepresentability.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/EtaleLocalRepresentability.lean#L179).

> A sheaf of sets on the small étale site of `X` is finite locally constant if and only if it is
> represented by an object of the site whose structure morphism is finite, that is, by a scheme
> finite étale over `X`. It takes a binder `hdesc : EtaleDescentForFiniteEtaleRepresentability B`,
> which defaults to the theorem `Stacks.EtaleCohomology.etaleDescentForFiniteEtaleRepresentability`,
> so the statement applies to `B X F` alone.

```lean
public theorem isFiniteLocallyConstant_iff_finiteEtaleRepresentable_of_descent
    (B : AlgebraicGeometry.BigEtaleSite.{u}) (X : B.Scheme)
    (F : Sheaf (SmallEtale.topology B X.1 X.property) (Type (u + 1)))
    (hdesc : EtaleDescentForFiniteEtaleRepresentability B :=
      etaleDescentForFiniteEtaleRepresentability B) :
    Stacks.ConstantSheaf.IsFiniteLocallyConstant (SmallEtale.topology B X.1 X.property) F ↔
      ∃ U : SmallEtale B X.1 X.property,
        IsFinite (B.inclusion.map U.obj.hom) ∧
          Nonempty (F ≅
            (Sheaf.sheafifiedYoneda (SmallEtale.topology B X.1 X.property)).obj U)
```

**`Stacks.EtaleCohomology.isFiniteLocallyConstant_iff_finiteEtaleRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/RepresentabilityDescent.lean, line 1316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/RepresentabilityDescent.lean#L1316). References: SGA 4 IX (2.2).

> **Stacks Project, Tag 03RV.** A sheaf of sets on the small étale site of `X` is finite
> locally constant if and only if it is represented by an object of the site whose structure
> morphism is finite — that is, by a scheme finite étale over `X`.
>
> The reverse implication is
> `Stacks.EtaleCohomology.isFiniteLocallyConstant_of_finiteEtaleRepresentable`. The forward one is
> the étale-local representability of
> `Stacks.EtaleCohomology.exists_sliceRepresentatives_of_isFiniteLocallyConstant` followed by
> effective descent for schemes affine over the base along an fpqc covering, Stacks 0245, in the
> form `AlgebraicGeometry.DescentData.isFamilyEffective_of_isAffineHom_of_anyIndex`.

```lean
public theorem isFiniteLocallyConstant_iff_finiteEtaleRepresentable
    (B : BigEtaleSite.{u}) (X : B.Scheme)
    (F : Sheaf (SmallEtale.topology B X.1 X.2) (Type (u + 1))) :
    Stacks.ConstantSheaf.IsFiniteLocallyConstant (SmallEtale.topology B X.1 X.2) F ↔
      ∃ U : SmallEtale B X.1 X.2,
        IsFinite (B.inclusion.map U.obj.hom) ∧
          Nonempty (F ≅
            (Sheaf.sheafifiedYoneda (SmallEtale.topology B X.1 X.2)).obj U)
```

**`AlgebraicGeometry.finiteLocallyConstantFiniteEtaleEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FundamentalGroupLocallyConstant/Sets.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FundamentalGroupLocallyConstant/Sets.lean#L67). The attribute's comment: “the equivalence of categories; the object-level statement is Stacks.EtaleCohomology.isFiniteLocallyConstant\_iff\_finiteEtaleRepresentable”.

> The equivalence between the finite locally constant sheaves of sets on the small étale site
> of `X` and the finite étale covers of `X`.

```lean
public noncomputable def finiteLocallyConstantFiniteEtaleEquivalence :
    FiniteLocallyConstantSheaf B X ≌ FiniteEtaleOver X.1
```

## Tag 095C, a lemma

[Tag 095C](https://stacks.math.columbia.edu/tag/095C) in the Stacks Project.

**`Stacks.ConstantSheaf.exists_etaleCover_restrict_eq_constantSheaf_map`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleLocallyConstantMorphisms.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleLocallyConstantMorphisms.lean#L68). The attribute's comment: “sheaves of sets”. References: SGA 4 IX (2.1), “(i), étale site”.

> **Stacks 095C (1).** A morphism of locally constant sheaves of sets on the small étale site
> of a scheme, whose source is finite locally constant, is on an étale covering of any object the
> morphism of constant sheaves attached to a map of sets.

```lean
lemma exists_etaleCover_restrict_eq_constantSheaf_map
    [∀ U : X.Etale, HasWeakSheafify ((smallEtaleTopology X).over U) (Type w)]
    (F G : Sheaf (smallEtaleTopology X) (Type w)) (φ : F ⟶ G)
    [IsFiniteLocallyConstant (smallEtaleTopology X) F]
    [IsLocallyConstant (smallEtaleTopology X) G] (U : X.Etale) :
    ∃ (I : Type (u + 1)) (V : I → X.Etale) (f : ∀ i, V i ⟶ U),
      Sieve.ofArrows V f ∈ smallEtaleTopology X U ∧ ∀ i,
        ∃ (A B : Type w), Finite A ∧
          ∃ (g : A ⟶ B)
            (eF : (constantSheaf ((smallEtaleTopology X).over (V i)) (Type w)).obj A ≅
              ((smallEtaleTopology X).overPullback (Type w) (V i)).obj F)
            (eG : (constantSheaf ((smallEtaleTopology X).over (V i)) (Type w)).obj B ≅
              ((smallEtaleTopology X).overPullback (Type w) (V i)).obj G),
              (constantSheaf ((smallEtaleTopology X).over (V i)) (Type w)).map g ≫ eG.hom =
                eF.hom ≫ ((smallEtaleTopology X).overPullback (Type w) (V i)).map φ
```

**`Stacks.ConstantSheaf.exists_etaleCover_restrict_eq_constantSheaf_map_abelian`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleLocallyConstantMorphisms.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleLocallyConstantMorphisms.lean#L89). The attribute's comment: “sheaves of abelian groups”. References: SGA 4 IX (2.1), “(ii) map, étale abelian”.

> **Stacks 095C (2).** A morphism of locally constant sheaves of abelian groups on the small
> étale site of a scheme, whose source is finite locally constant, is on an étale covering of any
> object the morphism of constant sheaves attached to a homomorphism of abelian groups.

```lean
lemma exists_etaleCover_restrict_eq_constantSheaf_map_abelian [UnivLE.{u + 1, w}]
    [∀ U : X.Etale, HasWeakSheafify ((smallEtaleTopology X).over U) Ab.{w}]
    (F G : Sheaf (smallEtaleTopology X) Ab.{w}) (φ : F ⟶ G)
    [IsFiniteLocallyConstant (smallEtaleTopology X) F]
    [IsLocallyConstant (smallEtaleTopology X) G] (U : X.Etale) :
    ∃ (I : Type (u + 1)) (V : I → X.Etale) (f : ∀ i, V i ⟶ U),
      Sieve.ofArrows V f ∈ smallEtaleTopology X U ∧ ∀ i,
        ∃ (A B : Ab.{w}), Finite (A : Type w) ∧
          ∃ (g : A ⟶ B)
            (eF : (constantSheaf ((smallEtaleTopology X).over (V i)) Ab.{w}).obj A ≅
              ((smallEtaleTopology X).overPullback Ab.{w} (V i)).obj F)
            (eG : (constantSheaf ((smallEtaleTopology X).over (V i)) Ab.{w}).obj B ≅
              ((smallEtaleTopology X).overPullback Ab.{w} (V i)).obj G),
              (constantSheaf ((smallEtaleTopology X).over (V i)) Ab.{w}).map g ≫ eG.hom =
                eF.hom ≫ ((smallEtaleTopology X).overPullback Ab.{w} (V i)).map φ
```

**`Stacks.ConstantSheaf.exists_etaleCover_restrict_eq_constantSheaf_map_modules`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleLocallyConstantMorphisms.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleLocallyConstantMorphisms.lean#L110). The attribute's comment: “sheaves of modules”. References: SGA 4 IX (2.1), “(ii) map, étale site”.

> **Stacks 095C (3).** A morphism of locally constant sheaves of `R`-modules on the small
> étale site of a scheme, whose source is locally constant of finite type, is on an étale covering
> of any object the morphism of constant sheaves attached to a homomorphism of `R`-modules.

```lean
lemma exists_etaleCover_restrict_eq_constantSheaf_map_modules {R : Type r} [Ring R]
    [∀ U : X.Etale, HasWeakSheafify ((smallEtaleTopology X).over U) (ModuleCat.{w} R)]
    (F G : Sheaf (smallEtaleTopology X) (ModuleCat.{w} R)) (φ : F ⟶ G)
    (hF : IsFiniteTypeLocallyConstant R (smallEtaleTopology X) F)
    [IsLocallyConstant (smallEtaleTopology X) G] (U : X.Etale) :
    ∃ (I : Type (u + 1)) (V : I → X.Etale) (f : ∀ i, V i ⟶ U),
      Sieve.ofArrows V f ∈ smallEtaleTopology X U ∧ ∀ i,
        ∃ (A B : ModuleCat.{w} R), ModuleCat.isFG R A ∧
          ∃ (g : A ⟶ B)
            (eF : (constantSheaf ((smallEtaleTopology X).over (V i)) (ModuleCat.{w} R)).obj A ≅
              ((smallEtaleTopology X).overPullback (ModuleCat.{w} R) (V i)).obj F)
            (eG : (constantSheaf ((smallEtaleTopology X).over (V i)) (ModuleCat.{w} R)).obj B ≅
              ((smallEtaleTopology X).overPullback (ModuleCat.{w} R) (V i)).obj G),
              (constantSheaf ((smallEtaleTopology X).over (V i)) (ModuleCat.{w} R)).map g ≫
                  eG.hom =
                eF.hom ≫ ((smallEtaleTopology X).overPullback (ModuleCat.{w} R) (V i)).map φ
```

## Tag 03RX, a lemma

[Tag 03RX](https://stacks.math.columbia.edu/tag/03RX) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.ConstantSheaf.isClosedUnderFiniteLimits_isFiniteLocallyConstantSetSheaf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/FiniteLimits.lean#L725), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/SmallEtaleSubcategories.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/SmallEtaleSubcategories.lean#L60) (StacksFrontier): “part (1), finite limits”.
- [`Stacks.ConstantSheaf.isClosedUnderFiniteColimits_isFiniteLocallyConstantSetSheaf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/FiniteLimits.lean#L730), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/SmallEtaleSubcategories.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/SmallEtaleSubcategories.lean#L62) (StacksFrontier): “part (1), finite colimits”.
- [`Stacks.ConstantSheaf.isWeakSerreClass_isFiniteLocallyConstantAbelianSheaf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/AbelianWeakSerre.lean#L439), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/SmallEtaleSubcategories.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/SmallEtaleSubcategories.lean#L64) (StacksFrontier): “part (2)”.
- [`Stacks.ConstantSheaf.isWeakSerreClass_isFiniteTypeLocallyConstantModuleSheaf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyConstantExtensions.lean#L793), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/SmallEtaleSubcategories.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/SmallEtaleSubcategories.lean#L66) (StacksFrontier): “part (3)”.

## Tag 095D, a lemma

[Tag 095D](https://stacks.math.columbia.edu/tag/095D) in the Stacks Project.

**`Stacks.ConstantSheaf.isLocallyConstant_tensor_smallEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocallyConstantSheaves/TensorProduct.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocallyConstantSheaves/TensorProduct.lean#L66). References: SGA 5 VI (1.4.5), “locally constant claim”.

> **Stacks 095D.** The tensor product of two locally constant sheaves of `Λ`-modules on the
> small étale site of a scheme is a locally constant sheaf of `Λ`-modules.

```lean
theorem isLocallyConstant_tensor_smallEtale {X : Scheme.{u}} (Λ : Type w) [CommRing Λ]
    [UnivLE.{u + 1, w}]
    [HasWeakSheafify (smallEtaleTopology X) (ModuleCat.{w} Λ)]
    [∀ U : X.Etale, HasWeakSheafify ((smallEtaleTopology X).over U) (ModuleCat.{w} Λ)]
    (F G : Sheaf (smallEtaleTopology X) (ModuleCat.{w} Λ))
    [IsLocallyConstant (smallEtaleTopology X) F]
    [IsLocallyConstant (smallEtaleTopology X) G] :
    IsLocallyConstant (smallEtaleTopology X) (F ⊗ G)
```

## Tag 09BF, a lemma

[Tag 09BF](https://stacks.math.columbia.edu/tag/09BF) in the Stacks Project.

**`AlgebraicGeometry.exists_etaleCover_constant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocallyConstantSheaves/ConnectedTrivialization.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocallyConstantSheaves/ConnectedTrivialization.lean#L238).

> **Stacks 09BF.** On a connected scheme, a locally constant sheaf of modules becomes the
> constant sheaf associated to one fixed module after an étale covering.

```lean
public theorem exists_etaleCover_constant
    (X : Scheme.{u}) [ConnectedSpace X]
    (Λ : Type v) [Ring Λ]
    [HasWeakSheafify X.smallEtaleTopology (ModuleCat.{v} Λ)]
    [∀ U : X.Etale, HasWeakSheafify (X.smallEtaleTopology.over U) (ModuleCat.{v} Λ)]
    (F : Sheaf X.smallEtaleTopology (ModuleCat.{v} Λ))
    [Stacks.ConstantSheaf.IsLocallyConstant X.smallEtaleTopology F] :
    ∃ (M : ModuleCat.{v} Λ) (I : Type (u + 1)) (U : I → X.Etale),
      ((⋃ i, Set.range (fun x : (U i).left =>
        (((U i).hom : (U i).left ⟶ X) x))) : Set X) = Set.univ ∧
        ∀ i, Nonempty
          ((X.smallEtaleTopology.overPullback (ModuleCat.{v} Λ) (U i)).obj F ≅
            (X.smallEtaleTopology.overPullback (ModuleCat.{v} Λ) (U i)).obj
              ((constantSheaf X.smallEtaleTopology (ModuleCat.{v} Λ)).obj M))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.64, Tag 09Y8](https://stacks.math.columbia.edu/tag/09Y8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
