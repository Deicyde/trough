---
declaration: section
origin: cited
lean: AlgebraicGeometry.isCohenMacaulayLocalRing_stalk_iff_of_finiteType_fieldExtension, AlgebraicGeometry.isCohenMacaulayLocalRing_stalk_iff_of_locallyOfFiniteType
statement: formalized
proof: formalized
---

# 33.13 Change of fields and the Cohen-Macaulay property

Section 33.13 of the Stacks Project, [Tag 045O](https://stacks.math.columbia.edu/tag/045O). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 045P, a lemma

[Tag 045P](https://stacks.math.columbia.edu/tag/045P) in the Stacks Project.

**`AlgebraicGeometry.isCohenMacaulayLocalRing_stalk_iff_of_finiteType_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/CohenMacaulayFieldChange/FieldExtension.lean, line 374](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/CohenMacaulayFieldChange/FieldExtension.lean#L374). The attribute's comment: “finitely generated field extension”. References: EGA IV (6.7.8), “(ii)”; EGA IV (6.7.1), “F = O\_X, CM clause”; EGA IV (6.7.2), “special case”; SGA 3 VIA (1.1.1), “more general”.

> **Stacks Project, Tag 045P.** Cohen-Macaulayness of local rings is unchanged after a
> finitely generated extension of the ground field of a locally Noetherian scheme.
>
> The extension may be transcendental: `K = k(x₁, …, xₙ)` is finitely generated as a field
> extension, which is `Algebra.EssFiniteType k K` by `IntermediateField.fg_top_iff`, and not
> finitely generated as a `k`-algebra. The base change is again locally Noetherian, by Tag 038R;
> that is what makes the local ring on the right a Noetherian local ring.

```lean
public theorem isCohenMacaulayLocalRing_stalk_iff_of_finiteType_fieldExtension
    (k K : Type u) [Field k] [Field K] [Algebra k K] [Algebra.EssFiniteType k K]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [IsLocallyNoetherian X] (x : X)
    (x' : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme))
    (hx' : (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base x' = x) :
    letI : IsLocallyNoetherian
        (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme) :=
      (isLocallyNoetherian_baseChange_iff k K X f).mp inferInstance
    IsCohenMacaulayLocalRing (X.presheaf.stalk x) ↔
      IsCohenMacaulayLocalRing
        ((pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).presheaf.stalk x')
```

**`AlgebraicGeometry.isCohenMacaulayLocalRing_stalk_iff_of_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/CohenMacaulayFieldChange/FieldExtension.lean, line 398](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/CohenMacaulayFieldChange/FieldExtension.lean#L398). The attribute's comment: “arbitrary field extension for a locally finite type scheme”. References: EGA IV (6.7.8), “(ii)”; EGA IV (6.7.1), “F = O\_X, CM clause”.

> **Stacks Project, Tag 045P.** Cohen-Macaulayness of local rings is unchanged after an
> arbitrary extension of the ground field when the scheme is locally of finite type over that
> field.

```lean
public theorem isCohenMacaulayLocalRing_stalk_iff_of_locallyOfFiniteType
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f] (x : X)
    (x' : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme))
    (hx' : (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base x' = x) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    IsCohenMacaulayLocalRing (X.presheaf.stalk x) ↔
      IsCohenMacaulayLocalRing
        ((pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).presheaf.stalk x')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.13, Tag 045O](https://stacks.math.columbia.edu/tag/045O)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
