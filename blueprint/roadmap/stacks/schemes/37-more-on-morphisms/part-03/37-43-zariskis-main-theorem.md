---
declaration: section
origin: cited
lean: AlgebraicGeometry.isOpenImmersion_toNormalization_and_isIntegralHom_fromNormalization, AlgebraicGeometry.isQuasiAffineHom_of_locallyQuasiFinite, AlgebraicGeometry.isSeparated_inf_quasiFinite_le_isQuasiAffineHom, Stacks.FiniteFactorization.exists_isOpenImmersion_isFinite_factorization, Stacks.FiniteFactorization.exists_isOpenImmersion_isFinite_finitePresentation_factorization
statement: formalized
proof: formalized
---

# 37.43 Zariski's Main Theorem

Section 37.43 of the Stacks Project, [Tag 02LQ](https://stacks.math.columbia.edu/tag/02LQ). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02LR, a lemma

[Tag 02LR](https://stacks.math.columbia.edu/tag/02LR) in the Stacks Project.

**`AlgebraicGeometry.isOpenImmersion_toNormalization_and_isIntegralHom_fromNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineQuasiFinite.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineQuasiFinite.lean#L113). The attribute's comment: “the factorization”. References: EGA IV (8.12.11), “sufficiency”.

> **Stacks Project, Tag 02LR, the factorization.** Let `f : X ⟶ S` be a separated quasi-finite
> morphism of schemes. Then the morphism from `X` to the normalization of `S` in `X` is a
> quasi-compact open immersion, and the normalization is integral over `S`.
>
> Both clauses are Mathlib instances; the open immersion is Mathlib's form of Stacks 03GW.

```lean
theorem isOpenImmersion_toNormalization_and_isIntegralHom_fromNormalization [IsSeparated f]
    [LocallyQuasiFinite f] [LocallyOfFiniteType f] [QuasiCompact f] :
    IsOpenImmersion f.toNormalization ∧ QuasiCompact f.toNormalization ∧
      IsIntegralHom f.fromNormalization
```

**`AlgebraicGeometry.isQuasiAffineHom_of_locallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineQuasiFinite.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineQuasiFinite.lean#L132). The attribute's comment: “quasi-affineness”. References: EGA IV (18.12.12); EGA II (6.2.7), “more general”; EGA III (4.4.12), “(i) quasi-affine”; EGA IV (8.11.2), “more general”; SGA 1 VIII (6.2), “more general”.

> **Stacks Project, Tag 02LR, quasi-affineness.** A separated quasi-finite morphism of schemes
> is quasi-affine.
>
> It factors as the morphism to the normalization of the target in the source, which is a
> quasi-compact open immersion and hence quasi-affine, followed by the normalization, which is
> integral and hence affine and hence quasi-affine; quasi-affine morphisms are stable under
> composition by Stacks 01SN.

```lean
theorem isQuasiAffineHom_of_locallyQuasiFinite [IsSeparated f] [LocallyQuasiFinite f]
    [LocallyOfFiniteType f] [QuasiCompact f] : IsQuasiAffineHom f
```

**`AlgebraicGeometry.isSeparated_inf_quasiFinite_le_isQuasiAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineQuasiFinite.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineQuasiFinite.lean#L153). The attribute's comment: “containment of properties”. References: EGA IV (18.12.12); EGA II (6.2.7); EGA III (4.4.12), “(i) quasi-affine”; EGA IV (8.11.2), “more general”; SGA 1 VIII (6.2), “more general”; SGA 3 X (5.4), “more general”.

> **Stacks Project, Tag 02LR** as a containment of morphism properties: the separated
> quasi-finite morphisms of schemes — separated, locally quasi-finite, locally of finite type and
> quasi-compact — are quasi-affine.
>
> This is the shape in which
> `AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isSeparated_inf_quasiFinite`
> takes Stacks 02LR as a hypothesis.

```lean
theorem isSeparated_inf_quasiFinite_le_isQuasiAffineHom :
    (@IsSeparated.{u} ⊓ @LocallyQuasiFinite ⊓ @LocallyOfFiniteType ⊓ @QuasiCompact :
        MorphismProperty Scheme.{u}) ≤ @IsQuasiAffineHom
```

## Tag 05K0, a lemma

[Tag 05K0](https://stacks.math.columbia.edu/tag/05K0) in the Stacks Project.

**`Stacks.FiniteFactorization.exists_isOpenImmersion_isFinite_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteFactorization/Basic.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FiniteFactorization/Basic.lean#L102). References: EGA III (4.4.12), “Quasi-finite case”; EGA III (4.4.3), “more general”; EGA III (4.4.5), “special case”; EGA IV (18.12.13).

> **Zariski's Main Theorem (Stacks Project, Tag 05K0).**  A quasi-finite separated morphism
> `f : X ⟶ S` onto a quasi-compact quasi-separated scheme factors as a quasi-compact open
> immersion `j : X ⟶ T` followed by a finite morphism `π : T ⟶ S`.
>
> Quasi-finiteness is Stacks 02NG, that is, locally quasi-finite and of finite type, which in
> Mathlib's vocabulary is `AlgebraicGeometry.LocallyQuasiFinite`,
> `AlgebraicGeometry.LocallyOfFiniteType` and `AlgebraicGeometry.QuasiCompact` together.
>
> The affine case of the factorization, [Stacks, Tag 03GU], is
> `AlgebraicGeometry.exists_isOpenImmersion_isFinite_factorization`; it is a different statement
> and is not used here.

```lean
theorem exists_isOpenImmersion_isFinite_factorization {X S : Scheme.{u}} (f : X ⟶ S)
    [IsSeparated f] [LocallyQuasiFinite f] [LocallyOfFiniteType f] [QuasiCompact f]
    [CompactSpace S] [QuasiSeparatedSpace S] :
    ∃ (T : Scheme.{u}) (j : X ⟶ T) (π : T ⟶ S),
      IsOpenImmersion j ∧ QuasiCompact j ∧ IsFinite π ∧ f = j ≫ π
```

## Tag 0F2N, a lemma

[Tag 0F2N](https://stacks.math.columbia.edu/tag/0F2N) in the Stacks Project.

**`Stacks.FiniteFactorization.exists_isOpenImmersion_isFinite_finitePresentation_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteFactorization/Basic.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FiniteFactorization/Basic.lean#L181). References: EGA III (4.4.12), “Quasi-finite case”; EGA III (4.4.3), “more general”; EGA III (4.4.5), “special case”; EGA IV (18.12.13), “special case”; EGA IV (8.12.6).

> **Zariski's Main Theorem with finite presentation (Stacks Project, Tag 0F2N).**  Let
> `f : X ⟶ S` be a quasi-finite separated morphism onto a quasi-compact quasi-separated scheme,
> and assume in addition that `f` is locally of finite presentation.  Then the factorization of
> [Stacks, Tag 05K0] into a quasi-compact open immersion `j : X ⟶ T` followed by a finite
> morphism `π : T ⟶ S` may be chosen with `π` of finite presentation as well.
>
> Quasi-finiteness is Stacks 02NG, as for Tag 05K0: `AlgebraicGeometry.LocallyQuasiFinite`,
> `AlgebraicGeometry.LocallyOfFiniteType` and `AlgebraicGeometry.QuasiCompact` together.  Finite
> presentation of `π` is `AlgebraicGeometry.FinitePresentation`, part (3) of [Stacks, Tag 01TP];
> for a finite, hence affine, morphism it is the same as being locally of finite presentation,
> so this is the tag's "finite and of finite presentation over `S`".

```lean
theorem exists_isOpenImmersion_isFinite_finitePresentation_factorization
    {X S : Scheme.{u}} (f : X ⟶ S)
    [IsSeparated f] [LocallyQuasiFinite f] [LocallyOfFiniteType f] [QuasiCompact f]
    [LocallyOfFinitePresentation f] [CompactSpace S] [QuasiSeparatedSpace S] :
    ∃ (T : Scheme.{u}) (j : X ⟶ T) (π : T ⟶ S),
      IsOpenImmersion j ∧ QuasiCompact j ∧ IsFinite π ∧ FinitePresentation π ∧ f = j ≫ π
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.43, Tag 02LQ](https://stacks.math.columbia.edu/tag/02LQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
