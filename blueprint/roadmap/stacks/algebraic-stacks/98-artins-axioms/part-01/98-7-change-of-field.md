---
declaration: section
origin: cited
lean: Deformation.Artin.changeOfFieldFunctor, Deformation.Artin.changeOfFieldFunctor_projection_comm, Deformation.Artin.changeOfFieldFunctor_isEquivalence, Deformation.Artin.Site.changeOfFieldFunctor_isEquivalence, Deformation.Artin.Site.changeOfFieldFunctor
statement: formalized
proof: formalized
---

# 98.7 Change of field

Section 98.7 of the Stacks Project, [Tag 07WW](https://stacks.math.columbia.edu/tag/07WW). 1 tag here is carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07WX, a lemma

[Tag 07WX](https://stacks.math.columbia.edu/tag/07WX) in the Stacks Project.

**`Deformation.Artin.changeOfFieldFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/ChangeOfField.lean, line 770](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/ChangeOfField.lean#L770). The attribute's comment: “the canonical functor; the ambient base category is the category of all S-schemes rather than the big fppf site”.

> **Stacks Project, Tag 07WX.** The canonical functor from the change of residue field of the
> predeformation category of `x₀` to the predeformation category of its restriction `x_{l,0}`.

```lean
def changeOfFieldFunctor :
    Deformation.ChangeOfFieldsCategory T D.projection ⥤ E.carrier
```

**`Deformation.Artin.changeOfFieldFunctor_projection_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/ChangeOfField.lean, line 841](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/ChangeOfField.lean#L841). The attribute's comment: “the canonical functor lies over 𝒞\_\{Λ,l}; the ambient base category is the category of all S-schemes rather than the big fppf site”.

> **Stacks Project, Tag 07WX.** The canonical functor is a functor of categories over
> `𝒞_{Λ,l}`.

```lean
theorem changeOfFieldFunctor_projection_comm :
    changeOfFieldFunctor T iΛ hxₗ hη c D E ⋙ E.projection =
      Deformation.changeOfFieldsProjection T D.projection
```

**`Deformation.Artin.changeOfFieldFunctor_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/ChangeOfField/Equivalence.lean, line 1357](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/ChangeOfField/Equivalence.lean#L1357). The attribute's comment: “the functor is an equivalence under (RS); the ambient base category is the category of all S-schemes rather than the big fppf site, and (RS) is taken in the matching form over that category”.

> **Stacks Project, Tag 07WX.** The canonical functor
> `(𝓕_{𝒳,k,x₀})_{l/k} ⥤ 𝓕_{𝒳,l,x_{l,0}}` of Tag 07WX is an equivalence when `𝒳` satisfies the
> Rim–Schlessinger condition (RS).

```lean
public theorem changeOfFieldFunctor_isEquivalence
    (hq : q.IsFiberedInGroupoids) (hRS : SatisfiesRSOver q c)
    (hfinK : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap T.Λ T.k)) ≫ iΛ))
    (hqcK : QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap T.Λ T.k)) ≫ iΛ))
    (hfinL : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap T.Λ T.l)) ≫ iΛ))
    (hqcL : QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap T.Λ T.l)) ≫ iΛ)) :
    (changeOfFieldFunctor T iΛ hxₗ hη c D E).IsEquivalence
```

**`Deformation.Artin.Site.changeOfFieldFunctor_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/ChangeOfField/SiteRestriction/Equivalence.lean, line 571](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/ChangeOfField/SiteRestriction/Equivalence.lean#L571). The attribute's comment: “the canonical functor is an equivalence under (RS), for a category fibred in groupoids over the big fppf site”.

> Under (RS), restriction of deformations is an equivalence over the Artinian local algebras
> with residue field `l`.

```lean
public theorem changeOfFieldFunctor_isEquivalence
    (hp : p.IsFiberedInGroupoids)
    (hη : p.IsCartesian (p.map η) η)
    (hηbase : eqToHom (congrArg Over.left hxₗ).symm ≫
      ((p ⋙ Over.post B.inclusion).map η).left ≫
      eqToHom (congrArg Over.left hx₀) =
        Spec.map (CommRingCat.ofHom (algebraMap T.k T.l)))
    (hfinite : LocallyOfFiniteType
        (Spec.map (CommRingCat.ofHom (algebraMap T.Λ T.k)) ≫ iΛ) ∧
      QuasiCompact
        (Spec.map (CommRingCat.ofHom (algebraMap T.Λ T.k)) ≫ iΛ))
    (hRS : Deformation.Artin.SatisfiesRS B S hS p hp) :
    (changeOfFieldFunctor T iΛ B hS p x₀ xₗ hx₀ hxₗ η hp hη hηbase).toFunctor.IsEquivalence
```

**`Deformation.Artin.Site.changeOfFieldFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/ChangeOfField/SiteRestriction/Functor.lean, line 693](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/ChangeOfField/SiteRestriction/Functor.lean#L693). The attribute's comment: “the canonical functor, for a category fibred in groupoids over the big fppf site”.

> The canonical functor `(𝓕_{𝒳,k,x₀})_{l/k} ⥤ 𝓕_{𝒳,l,x_{l,0}}` over `𝒞_{Λ,l}`, restricting
> deformations along `Spec A ⟶ Spec (A ×_l k)`.

```lean
public noncomputable def changeOfFieldFunctor
    (hp : p.IsFiberedInGroupoids)
    (_hη : p.IsCartesian (p.map η) η)
    (hηbase : eqToHom (congrArg Over.left hxₗ).symm ≫
      ((p ⋙ Over.post B.inclusion).map η).left ≫
      eqToHom (congrArg Over.left hx₀) =
        Spec.map (CommRingCat.ofHom (algebraMap T.k T.l))) :
    ChangeOfFieldFunctor T iΛ B hS p x₀ xₗ hx₀ hxₗ η
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.7, Tag 07WW](https://stacks.math.columbia.edu/tag/07WW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
