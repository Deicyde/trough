---
declaration: section
origin: cited
lean: Deformation.ChangeOfFieldsSituation, Deformation.comparisonFunctor, Deformation.changeOfFieldsProjection, Deformation.changeOfFieldsFiberInclusion_isEquivalence, Deformation.changeOfFieldsProjection_isCofiberedInGroupoids, comparisonFunctor, Deformation.changeOfFieldsIsoClassMap_bijective, Deformation.changeOfFieldsIsoClassMap_naturality
statement: formalized
proof: formalized
---

# 90.29 Change of residue field

Section 90.29 of the Stacks Project, [Tag 07W7](https://stacks.math.columbia.edu/tag/07W7). 7 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07W8, a situation

[Tag 07W8](https://stacks.math.columbia.edu/tag/07W8) in the Stacks Project.

**`Deformation.ChangeOfFieldsSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ResidueField/Basic.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ResidueField/Basic.lean#L104). The attribute's comment: “the standing situation”.

> **Stacks Project, Tag 07W8.** The standing finite tower of fields over the
> Noetherian base ring `Λ`.

```lean
public structure ChangeOfFieldsSituation
```

**`Deformation.comparisonFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ResidueField/Basic.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ResidueField/Basic.lean#L340). The attribute's comment: “the comparison functor”.

> **Stacks Project, Tag 07W8.** The canonical comparison functor sending
> `B` to `B ×_l k`, with its prescribed algebra, residue and morphism maps.

```lean
public noncomputable def comparisonFunctor
    (S : ChangeOfFieldsSituation.{u, v, w}) :
    ComparisonFunctor.{u, v, w, x} S
```

**`Deformation.changeOfFieldsProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ResidueField/Basic.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ResidueField/Basic.lean#L454). The attribute's comment: “the associated projection”.

> **Stacks Project, Tag 07W8.** The projection
> `p_{l/k} : F_{l/k} ⟶ 𝒞_{Λ,l}` associated to `p : F ⟶ 𝒞_{Λ,k}`.

```lean
public def changeOfFieldsProjection (S : ChangeOfFieldsSituation.{u, v, w})
    {F : Type y} [Category.{z} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max x v, v} S.Λ S.k) :
    ChangeOfFieldsCategory S p ⥤
      ArtinianLocalAlgCat.{u, x, w} S.Λ S.l
```

**`Deformation.changeOfFieldsFiberInclusion_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ResidueField/Basic.lean, line 494](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ResidueField/Basic.lean#L494). The attribute's comment: “the fibers”.

> **Stacks Project, Tag 07W8.** The canonical fiber inclusion is an equivalence.
> This fixes the identification of the changed fiber with the original fiber over
> `B ×_l k`, rather than merely asserting existence of an unspecified equivalence.

```lean
public theorem changeOfFieldsFiberInclusion_isEquivalence
    (S : ChangeOfFieldsSituation.{u, v, w})
    {F : Type y} [Category.{z} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max x v, v} S.Λ S.k)
    (hp : IsCofiberedInGroupoids p)
    (B : ArtinianLocalAlgCat.{u, x, w} S.Λ S.l) :
    (changeOfFieldsFiberInclusion S p B).IsEquivalence
```

**`Deformation.changeOfFieldsProjection_isCofiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ResidueField/Basic.lean, line 582](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ResidueField/Basic.lean#L582). The attribute's comment: “cofibered in groupoids”.

> **Stacks Project, Tag 07W8.** The projection obtained by change of residue field is
> cofibered in groupoids whenever the original projection is.

```lean
public theorem changeOfFieldsProjection_isCofiberedInGroupoids
    (S : ChangeOfFieldsSituation.{u, v, w})
    {F : Type y} [Category.{z} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max x v, v} S.Λ S.k)
    (hp : IsCofiberedInGroupoids p) :
    IsCofiberedInGroupoids (changeOfFieldsProjection S p)
```

## Tag 07W9, an equation

[Tag 07W9](https://stacks.math.columbia.edu/tag/07W9) in the Stacks Project.

Declarations registered for the tag:

- [`comparisonFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=comparisonFunctor#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/ResidueField/Basic.lean, line 695](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ResidueField/Basic.lean#L695) (StacksFrontier).

## Tag 07WA, a lemma

[Tag 07WA](https://stacks.math.columbia.edu/tag/07WA) in the Stacks Project.

**`Deformation.changeOfFieldsIsoClassMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ResidueField/Basic.lean, line 720](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ResidueField/Basic.lean#L720). The attribute's comment: “isomorphism\_classes”.

> The canonical fiber inclusion induces a bijection on isomorphism classes,
> without restricting the universe of the total category.

```lean
public theorem changeOfFieldsIsoClassMap_bijective
    (S : ChangeOfFieldsSituation.{u, v, w})
    {F : Type y} [Category.{z} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max x v, v} S.Λ S.k)
    (hp : IsCofiberedInGroupoids p)
    (B : ArtinianLocalAlgCat.{u, x, w} S.Λ S.l) :
    Function.Bijective (changeOfFieldsIsoClassMap S p B)
```

**`Deformation.changeOfFieldsIsoClassMap_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ResidueField/Basic.lean, line 757](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ResidueField/Basic.lean#L757). The attribute's comment: “isomorphism\_classes”.

> Naturality of the canonical identification on representative classes: a
> coCartesian pushforward and the change-of-fields fiber inclusion commute on
> isomorphism classes. This formulation allows the total category to live in
> an arbitrary universe.

```lean
public theorem changeOfFieldsIsoClassMap_naturality
    (S : ChangeOfFieldsSituation.{u, v, w})
    {F : Type y} [Category.{z} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max x v, v} S.Λ S.k)
    (hp : IsCofiberedInGroupoids p)
    {B C : ArtinianLocalAlgCat.{u, x, w} S.Λ S.l}
    (f : B ⟶ C)
    (a : p.Fiber ((comparisonFunctor S).functor.obj B)) :
    letI : p.op.IsFibered := hp.isFibered
    letI : (changeOfFieldsProjection S p).op.IsFibered :=
      (changeOfFieldsProjection_isCofiberedInGroupoids S p hp).isFibered
    let a' : p.Fiber ((comparisonFunctor S).functor.obj C) :=
      ⟨(CategoryTheory.Functor.pullbackFiber p.op
        (⟨Opposite.op a.1, congrArg Opposite.op a.2⟩ :
          p.op.Fiber (Opposite.op ((comparisonFunctor S).functor.obj B)))
        ((comparisonFunctor S).functor.map f).op).1.unop,
        congrArg Opposite.unop (CategoryTheory.Functor.pullbackFiber p.op
          (⟨Opposite.op a.1, congrArg Opposite.op a.2⟩ :
            p.op.Fiber (Opposite.op ((comparisonFunctor S).functor.obj B)))
          ((comparisonFunctor S).functor.map f).op).2⟩
    (changeOfFieldsProjection S p).op.isoClassPresheaf.map f.op.op
      (CategoryTheory.Functor.isoClassMk (changeOfFieldsProjection S p).op
        (⟨Opposite.op ((changeOfFieldsFiberInclusion S p B).obj a).1,
          congrArg Opposite.op ((changeOfFieldsFiberInclusion S p B).obj a).2⟩ :
          (changeOfFieldsProjection S p).op.Fiber (Opposite.op B))) =
      CategoryTheory.Functor.isoClassMk (changeOfFieldsProjection S p).op
        (⟨Opposite.op ((changeOfFieldsFiberInclusion S p C).obj a').1,
          congrArg Opposite.op ((changeOfFieldsFiberInclusion S p C).obj a').2⟩ :
          (changeOfFieldsProjection S p).op.Fiber (Opposite.op C))
```

**`Deformation.changeOfFieldsProjection_isPredeformationCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ResidueField/Basic.lean, line 1025](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ResidueField/Basic.lean#L1025). The attribute's comment: “predeformation”.

> Changing the residue field of a predeformation category along `k → l`
> again gives a predeformation category.

```lean
public theorem changeOfFieldsProjection_isPredeformationCategory
    (S : ChangeOfFieldsSituation.{u, v, w})
    {F : Type y} [Category.{z} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max (max x w) v, v} S.Λ S.k)
    (hp : IsPredeformationCategory.{u, max x w, v, z, y} p) :
    IsPredeformationCategory
      (changeOfFieldsProjection.{u, v, w, max x w, y, z} S p)
```

**`Deformation.schlessingerConditionS1_changeOfFields`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/VersalObject/ChangeOfFieldsConditionS2.lean, line 688](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/VersalObject/ChangeOfFieldsConditionS2.lean#L688). The attribute's comment: “condition (S1)”.

> A change of residue field preserves Schlessinger's condition (S1).

```lean
public theorem schlessingerConditionS1_changeOfFields
    (S : ChangeOfFieldsSituation.{u, v, w})
    {F : Type y} [Category.{z} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max x v, v} S.Λ S.k)
    (hS1 : SchlessingerConditionS1 p) :
    SchlessingerConditionS1
      (changeOfFieldsProjection S p)
```

**`Deformation.schlessingerConditionS2_changeOfFields`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/VersalObject/ChangeOfFieldsConditionS2.lean, line 707](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/VersalObject/ChangeOfFieldsConditionS2.lean#L707). The attribute's comment: “condition (S2)”.

> A change of residue field preserves Schlessinger's condition (S2) for a functor cofibered
> in groupoids.

```lean
public theorem schlessingerConditionS2_changeOfFields
    (S : ChangeOfFieldsSituation.{u, v, w})
    {F : Type y} [Category.{z} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max x v, v} S.Λ S.k)
    (hp : IsCofiberedInGroupoids p)
    (hS2 : SchlessingerConditionS2 p) :
    SchlessingerConditionS2
      (changeOfFieldsProjection S p)
```

**`Deformation.changeOfFieldsProjection_satisfiesRS`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/VersalObject/ChangeOfFieldsConditionS2.lean, line 881](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/VersalObject/ChangeOfFieldsConditionS2.lean#L881). The attribute's comment: “condition (RS)”.

> A change of residue field preserves the Rim-Schlessinger condition (RS).

```lean
public theorem changeOfFieldsProjection_satisfiesRS
    (S : ChangeOfFieldsSituation.{u, v, w})
    {F : Type y} [Category.{z} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max x v, v} S.Λ S.k)
    (hp : SatisfiesRS p) :
    SatisfiesRS (changeOfFieldsProjection S p)
```

## Tag 07WB, a lemma

[Tag 07WB](https://stacks.math.columbia.edu/tag/07WB) in the Stacks Project.

**`Deformation.tangentSpaceChangeOfFields`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/VersalObject/ChangeOfFieldsTangentSpace.lean, line 1567](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/VersalObject/ChangeOfFieldsTangentSpace.lean#L1567).

```lean
public noncomputable def tangentSpaceChangeOfFields
    (S : ChangeOfFieldsSituation.{u, v, v})
    (𝓕 : BasedCategory.{z, y} (ArtinianLocalAlgCat.{u, v, v} S.Λ S.k))
    (hp : IsPredeformationCategory 𝓕.p)
    (hS2 : SchlessingerConditionS2
      (CategoryOfElements.π (isomorphismClasses 𝓕 hp.cofibered))) :
    let q := changeOfFieldsProjection.{u, v, v, v, y, z} S 𝓕.p
    let hq := changeOfFieldsProjection_isPredeformationCategory
      S 𝓕.p hp
    let 𝓖 : BasedCategory.{max v z, max (max u (v + 1)) y}
        (ArtinianLocalAlgCat.{u, v, v} S.Λ S.l) :=
      ⟨ChangeOfFieldsCategory S 𝓕.p, inferInstance, q⟩
    letI : Fact (IsPredeformationCategory 𝓕.p) := ⟨hp⟩
    letI : Fact (SchlessingerConditionS2
      (CategoryOfElements.π (isomorphismClasses
        𝓕 hp.cofibered))) := ⟨hS2⟩
    letI : Fact (IsPredeformationCategory 𝓖.p) := ⟨hq⟩
    letI : Fact (SchlessingerConditionS2
      (CategoryOfElements.π (isomorphismClasses
        𝓖 hq.cofibered))) :=
      ⟨associatedSchlessingerConditionS2_changeOfFields S 𝓕 hp hS2⟩
    letI : AddCommGroup (artinianTangentSpace S.Λ S.k
      (isomorphismClasses 𝓕 hp.cofibered)) :=
      associatedTangentSpaceAddCommGroupUnlifted 𝓕
    letI : Module S.k (artinianTangentSpace S.Λ S.k
      (isomorphismClasses 𝓕 hp.cofibered)) :=
      associatedTangentSpaceModuleUnlifted 𝓕
    letI : AddCommGroup (artinianTangentSpace S.Λ S.l
      (isomorphismClasses 𝓖 hq.cofibered)) :=
      associatedTangentSpaceAddCommGroupUnlifted 𝓖
    letI : Module S.l (artinianTangentSpace S.Λ S.l
      (isomorphismClasses 𝓖 hq.cofibered)) :=
      associatedTangentSpaceModuleUnlifted 𝓖
    TensorProduct S.k S.l
      (artinianTangentSpace S.Λ S.k
        (isomorphismClasses 𝓕 hp.cofibered)) ≃ₗ[S.l]
      artinianTangentSpace S.Λ S.l
        (isomorphismClasses 𝓖 hq.cofibered)
```

**`Deformation.tangentSpaceChangeOfFields_tmul_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/VersalObject/ChangeOfFieldsTangentSpace.lean, line 1859](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/VersalObject/ChangeOfFieldsTangentSpace.lean#L1859). The attribute's comment: “canonical pure-tensor formula”.

> The scalar-extension equivalence sends a tangent vector tensored with `1`
> to its image under the canonical map on square-zero extensions and the
> change-of-field identification of fibrewise isomorphism classes.

```lean
public theorem tangentSpaceChangeOfFields_tmul_one
    (S : ChangeOfFieldsSituation.{u, v, v})
    (𝓕 : BasedCategory.{z, y} (ArtinianLocalAlgCat.{u, v, v} S.Λ S.k))
    (hp : IsPredeformationCategory 𝓕.p)
    (hS2 : SchlessingerConditionS2
      (CategoryOfElements.π (isomorphismClasses 𝓕 hp.cofibered))) :
    let q := changeOfFieldsProjection.{u, v, v, v, y, z} S 𝓕.p
    let hq := changeOfFieldsProjection_isPredeformationCategory
      S 𝓕.p hp
    let 𝓖 : BasedCategory.{max v z, max (max u (v + 1)) y}
        (ArtinianLocalAlgCat.{u, v, v} S.Λ S.l) :=
      ⟨ChangeOfFieldsCategory S 𝓕.p, inferInstance, q⟩
    let A := (artinianSquareZeroExtensionFunctor S.Λ S.k).obj
      (FGModuleCat.of S.k S.k)
    let B := (artinianSquareZeroExtensionFunctor S.Λ S.l).obj
      (FGModuleCat.of S.l S.l)
    let C := (comparisonFunctor S).functor.obj B
    let j : A ⟶ C := (canonicalDualNumberInclusion S).val
    letI : Fact (IsPredeformationCategory 𝓕.p) := ⟨hp⟩
    letI : Fact (SchlessingerConditionS2
      (CategoryOfElements.π (isomorphismClasses
        𝓕 hp.cofibered))) := ⟨hS2⟩
    letI : AddCommGroup (artinianTangentSpace S.Λ S.k
      (isomorphismClasses 𝓕 hp.cofibered)) :=
      associatedTangentSpaceAddCommGroupUnlifted 𝓕
    letI : Module S.k (artinianTangentSpace S.Λ S.k
      (isomorphismClasses 𝓕 hp.cofibered)) :=
      associatedTangentSpaceModuleUnlifted 𝓕
    ∀ (t : artinianTangentSpace S.Λ S.k
        (isomorphismClasses 𝓕 hp.cofibered)),
      (tangentSpaceChangeOfFields S 𝓕 hp hS2) (1 ⊗ₜ[S.k] t) =
        cast (isomorphismClasses_obj 𝓖 hq.cofibered B).symm
          (changeOfFieldsIsoClassMap S 𝓕.p B
            (cast (isomorphismClasses_obj 𝓕 hp.cofibered C)
              ((isomorphismClasses 𝓕 hp.cofibered).map j t)))
```

## Tag 07WC, a lemma

[Tag 07WC](https://stacks.math.columbia.edu/tag/07WC) in the Stacks Project.

**`Deformation.existsUnique_infinitesimalAutomorphismsChangeOfFields`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/ChangeOfFields.lean, line 1765](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/ChangeOfFields.lean#L1765).

> **Stacks Project, Tag 07WC.** For a deformation category over the residue field `k`, the
> space of infinitesimal automorphisms extends by scalars along `k → l` to the space of
> infinitesimal automorphisms of the change of residue field. The equivalence is pinned by its
> action on dual-number automorphisms, read through a comparison of pushforwards whose base
> morphism has the prescribed pullback coordinates.

```lean
public theorem existsUnique_infinitesimalAutomorphismsChangeOfFields
    (S : Deformation.ChangeOfFieldsSituation.{u, v, w})
    {F : Type y} [Category.{z} F]
    (p : F ⥤ Deformation.ArtinianLocalAlgCat.{u, max v w, v} S.Λ S.k)
    (hp : Deformation.IsDeformationCategory p)
    (x₀ : p.Fiber (residueFieldObject.{u, w, v} S.Λ S.k))
    (P : ChosenPushforwardsAt p x₀.1)
    (xₗ : (Deformation.changeOfFieldsProjection S p).Fiber
      (residueFieldObject.{u, v, w} S.Λ S.l))
    (Q : ChosenPushforwardsAt
      (Deformation.changeOfFieldsProjection S p) xₗ.1) :
    let hq := changeOfFieldsProjection_satisfiesRS
      S p hp.satisfiesRS
    letI : AddCommGroup (localizedAutomorphismFunctorTangent P) :=
      naturalLocalizedTangentAddCommGroup P hp.satisfiesRS
    letI : Module S.k (localizedAutomorphismFunctorTangent P) :=
      naturalLocalizedTangentModule P hp.satisfiesRS
    letI : AddCommGroup (localizedAutomorphismFunctorTangent Q) :=
      naturalLocalizedTangentAddCommGroup Q hq
    letI : Module S.l (localizedAutomorphismFunctorTangent Q) :=
      naturalLocalizedTangentModule Q hq
    let Uε := dualNumbersUnder (p := p) (x := x₀.1)
    let Vε := dualNumbersUnder
      (p := Deformation.changeOfFieldsProjection S p) (x := xₗ.1)
    ∃! E : TensorProduct S.k S.l
        (localizedAutomorphismFunctorTangent P) ≃ₗ[S.l]
        localizedAutomorphismFunctorTangent Q,
      ∃ (j : x₀.1 ⟶ xₗ.1.fst) (h : (P.obj Uε).1 ⟶ (Q.obj Vε).1.fst),
        let b : Uε.right ⟶
            (Deformation.comparisonFunctor.{u, v, w, max v w} S).functor.obj Vε.right :=
          eqToHom (P.obj Uε).2.symm ≫ p.map h ≫ (Q.obj Vε).1.iso.hom ≫
            (Deformation.comparisonFunctor.{u, v, w, max v w} S).functor.map (eqToHom (Q.obj Vε).2)
        (P.inclusion Uε ≫ h = j ≫ (Q.inclusion Vε).fst) ∧
        (∀ a : Uε.right,
          ((((Deformation.comparisonFunctor.{u, v, w, max v w} S).pullbackEquiv
              Vε.right) (b.hom a)).val.1).fst = algebraMap S.k S.l a.fst ∧
          ((((Deformation.comparisonFunctor.{u, v, w, max v w} S).pullbackEquiv
              Vε.right) (b.hom a)).val.1).snd =
            ULift.up (algebraMap S.k S.l a.snd.down) ∧
          (((Deformation.comparisonFunctor.{u, v, w, max v w} S).pullbackEquiv
              Vε.right) (b.hom a)).val.2 = a.fst) ∧
        (∀ t : localizedAutomorphismFunctorTangent P,
          (localizedTangentEquivKernel P t).1.asIso.hom.val ≫ h =
            h ≫ (localizedTangentEquivKernel Q
              (E (1 ⊗ₜ[S.k] t))).1.asIso.hom.val.fst)
```

## Tag 07WD, a lemma

[Tag 07WD](https://stacks.math.columbia.edu/tag/07WD) in the Stacks Project.

**`Deformation.isSmooth_changeOfFields`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ResidueField/Comparison.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ResidueField/Comparison.lean#L329).

> **Stacks Project, Tag 07WD.** A smooth morphism of categories over the
> Artinian algebras with residue field `k` remains smooth after changing the
> residue field to `l`.

```lean
public theorem isSmooth_changeOfFields
    (S : ChangeOfFieldsSituation.{u, v, w})
    {𝓕 : BasedCategory.{v₁, u₁}
      (ArtinianLocalAlgCat.{u, max x v, v} S.Λ S.k)}
    {𝓖 : BasedCategory.{v₂, u₂}
      (ArtinianLocalAlgCat.{u, max x v, v} S.Λ S.k)}
    (φ : BasedFunctor 𝓕 𝓖) (hφ : IsSmooth φ) :
    IsSmooth (changeOfFieldsBasedFunctor S φ)
```

## Tag 0DQF, a lemma

[Tag 0DQF](https://stacks.math.columbia.edu/tag/0DQF) in the Stacks Project.

**`Deformation.exists_versal_formalObject_changeOfFields`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/VersalObject/ChangeOfFields.lean, line 1022](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/VersalObject/ChangeOfFields.lean#L1022).

> **Stacks Project, Tag 0DQF.** For a versal formal object `ξ` of a category cofibered in
> groupoids over `𝒞_{Λ,k}`, there is a Noetherian complete local `Λ`-algebra with residue field
> `l`, receiving a local `Λ`-algebra map from the base of `ξ` which is formally smooth for its
> maximal-ideal-adic topology and induces the extension `l/k` on residue fields, and carrying a
> versal formal object of the change-of-residue-field category.

```lean
public theorem exists_versal_formalObject_changeOfFields
    (S : ChangeOfFieldsSituation.{u, v, w})
    {F : Type y} [Category.{z} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max x v w, v} S.Λ S.k)
    (hp : IsCofiberedInGroupoids p)
    (ξ : FormalObject p)
    (hξ : IsVersal hp ξ) :
    ∃ (T : CompleteLocalAlgCat.{u, max x v w, w} S.Λ S.l)
      (f : ξ.base →ₐ[S.Λ] T),
      IsLocalHom f.toRingHom ∧
        (∀ a : ξ.base,
          T.residueEquiv (residue T (f a)) =
            algebraMap S.k S.l (ξ.base.residueEquiv (residue ξ.base a))) ∧
        RingHom.FormallySmoothNAdic.{max x v w} f.toRingHom (maximalIdeal T) ∧
        ∃ ξ' : FormalObject
            (changeOfFieldsProjection.{u, v, w, max x v w} S p),
          ξ'.base = T ∧
            IsVersal (changeOfFieldsProjection_isCofiberedInGroupoids S p hp) ξ'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.29, Tag 07W7](https://stacks.math.columbia.edu/tag/07W7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
