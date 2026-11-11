---
declaration: section
origin: cited
lean: AlgebraicGeometry.nonempty_discreteValuationSpecialization, AlgebraicGeometry.ValuativeCommSq, AlgebraicGeometry.isSeparated_tfae_of_locallyOfFiniteType, AlgebraicGeometry.isProper_of_genericDiscreteValuativeCriterion, AlgebraicGeometry.isProper_tfae_genericDiscreteValuativeCriterion, AlgebraicGeometry.isProper_tfae_of_isFiniteType, AlgebraicGeometry.universallyClosed_tfae_valuative
statement: formalized
proof: formalized
---

# 32.15 Noetherian valuative criterion

Section 32.15 of the Stacks Project, [Tag 0CM1](https://stacks.math.columbia.edu/tag/0CM1). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CM2, a lemma

[Tag 0CM2](https://stacks.math.columbia.edu/tag/0CM2) in the Stacks Project.

**`AlgebraicGeometry.nonempty_discreteValuationSpecialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/NoetherianValuativeCriterion/DiscreteValuationSpecialization.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/NoetherianValuativeCriterion/DiscreteValuationSpecialization.lean#L356).

> A point in the closure of the image of a finite-type morphism into a locally Noetherian
> scheme is reached by a discrete valuation ring, with generic point on a generic component of the
> source.

```lean
theorem nonempty_discreteValuationSpecialization {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] [QuasiCompact f] [IsLocallyNoetherian Y] (y : Y)
    (y_mem_closure : y ∈ closure (Set.range f.base)) :
    Nonempty (DiscreteValuationSpecialization f y)
```

## Tag 0206, an equation

[Tag 0206](https://stacks.math.columbia.edu/tag/0206) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.ValuativeCommSq`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.ValuativeCommSq#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch32.lean, line 13](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch32.lean#L13) (StacksFrontier).

## Tag 0207, a lemma

[Tag 0207](https://stacks.math.columbia.edu/tag/0207) in the Stacks Project.

**`AlgebraicGeometry.isSeparated_tfae_of_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/NoetherianValuativeCriterion/Separatedness.lean, line 626](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/NoetherianValuativeCriterion/Separatedness.lean#L626). References: EGA II (7.2.3), “Noetherian/DVR case”.

> **Stacks Project, Tag 0207.** For a morphism locally of finite type over a locally
> Noetherian scheme, separatedness is equivalent to uniqueness in the valuative criterion; it
> suffices to use discrete valuation rings, and even the discrete valuation subrings of the
> function fields of the irreducible components of the source.

```lean
theorem isSeparated_tfae_of_locallyOfFiniteType {X S : Scheme.{u}} (f : X ⟶ S)
    [IsLocallyNoetherian S] [LocallyOfFiniteType f] :
    List.TFAE
      [ IsSeparated f,
        ValuativeCriterion.Uniqueness f,
        ∀ (D : ValuativeCommSq f),
          IsDiscreteValuationRing D.R → Subsingleton D.commSq.LiftStruct,
        ∀ (η : X), η ∈ genericPoints X →
          ∀ (A : Subring (X.residueField η)),
            IsDiscreteValuationRing A →
              IsFractionRing A (X.residueField η) →
                ∀ (i₂ : Spec (.of A) ⟶ S)
                  (sq : CommSq (X.fromSpecResidueField η)
                    (Spec.map (CommRingCat.ofHom A.subtype)) f i₂),
                  Subsingleton sq.LiftStruct ]
```

## Tag 0208, a lemma

[Tag 0208](https://stacks.math.columbia.edu/tag/0208) in the Stacks Project.

**`AlgebraicGeometry.isProper_of_genericDiscreteValuativeCriterion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/NoetherianValuativeCriterion/GenericProperness.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/NoetherianValuativeCriterion/GenericProperness.lean#L289). The attribute's comment: “condition (4) implies condition (1)”. References: EGA II (7.3.8), “(b)⇒(a)”; EGA IV (15.7.5), “c⇒a”; EGA IV (18.10.20), “partial”.

> **[Stacks, Tag 0208], condition (4) implies condition (1).** A morphism of finite type to a
> locally Noetherian scheme is proper as soon as every valuative diagram whose valuation ring is a
> discrete valuation subring of the residue field at a generic point of an irreducible component
> of the source, with that residue field as its fraction field, and whose generic arrow is the
> canonical one, has exactly one dotted arrow.

```lean
theorem isProper_of_genericDiscreteValuativeCriterion (p : V ⟶ W)
    [IsLocallyNoetherian W] [LocallyOfFiniteType p] [QuasiCompact p]
    (h : GenericDiscreteValuativeCriterion p) : IsProper p
```

**`AlgebraicGeometry.isProper_tfae_genericDiscreteValuativeCriterion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/NoetherianValuativeCriterion/GenericProperness.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/NoetherianValuativeCriterion/GenericProperness.lean#L342). References: EGA II (7.3.8); EGA IV (15.7.5), “a⇔c”.

> **[Stacks, Tag 0208].** Let `S` be locally Noetherian and `f : X ⟶ S` of finite type. The
> following are equivalent:
>
> 1. `f` is proper;
> 2. every valuative diagram for `f` has exactly one dotted arrow;
> 3. every valuative diagram for `f` whose valuation ring is a discrete valuation ring has exactly
>    one dotted arrow;
> 4. for every generic point `η` of an irreducible component of `X` and every discrete valuation
>    subring `A` of `κ(η)` with fraction field `κ(η)`, every valuative diagram whose generic arrow
>    is the canonical `Spec κ(η) ⟶ X` has exactly one dotted arrow, that is,
>    `AlgebraicGeometry.GenericDiscreteValuativeCriterion f`.
>
> Conditions (1) to (3) are `AlgebraicGeometry.isProper_tfae_of_isFiniteType`; (3) implies (4)
> because such a diagram is a valuative diagram over a discrete valuation ring, and (4) implies (1)
> is `AlgebraicGeometry.isProper_of_genericDiscreteValuativeCriterion`.

```lean
theorem isProper_tfae_genericDiscreteValuativeCriterion {X S : Scheme.{u}} (f : X ⟶ S)
    [IsLocallyNoetherian S] [LocallyOfFiniteType f] [QuasiCompact f] :
    List.TFAE
      [ IsProper f,
        ValuativeCriterion f,
        ∀ D : ValuativeCommSq f,
          IsDiscreteValuationRing D.R → Nonempty (Unique D.commSq.LiftStruct),
        GenericDiscreteValuativeCriterion f ]
```

**`AlgebraicGeometry.isProper_tfae_of_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/NoetherianValuativeCriterion/Properness.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/NoetherianValuativeCriterion/Properness.lean#L58). The attribute's comment: “conditions (1), (2) and (3)”. References: EGA II (7.3.3), “Noetherian, finite type”; EGA II (7.3.8), “proper/DVR case”; EGA I (3.7.3), “more general”.

> **Stacks Project, Tag 0208, conditions (1), (2) and (3).** For a morphism of finite type to a
> locally Noetherian scheme, properness, the existence of exactly one dotted arrow in every
> valuative square, and the existence of exactly one dotted arrow in every valuative square over a
> discrete valuation ring are equivalent.

```lean
theorem isProper_tfae_of_isFiniteType {X S : Scheme.{u}} (f : X ⟶ S)
    [IsLocallyNoetherian S] [LocallyOfFiniteType f] [QuasiCompact f] :
    List.TFAE
      [ IsProper f,
        ValuativeCriterion f,
        ∀ D : ValuativeCommSq f,
          IsDiscreteValuationRing D.R → Nonempty (Unique D.commSq.LiftStruct) ]
```

## Tag 05JY, a lemma

[Tag 05JY](https://stacks.math.columbia.edu/tag/05JY) in the Stacks Project.

**`AlgebraicGeometry.universallyClosed_tfae_valuative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/UniversallyClosedValuative/Basic.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/UniversallyClosedValuative/Basic.lean#L166). References: EGA II (7.3.8), “fin. type, Noeth. base”.

> For a finite type morphism to a locally Noetherian scheme, universal closedness, closedness
> after adjoining any finite number of affine coordinates, the existence part of the valuative
> criterion, and its restriction to discrete valuation rings are equivalent.

```lean
theorem universallyClosed_tfae_valuative {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [QuasiCompact f] [IsLocallyNoetherian S] :
    List.TFAE
      [ UniversallyClosed f,
        ∀ n : ℕ, IsClosedMap (AffineSpace.map (ULift.{u} (Fin n)) f),
        ValuativeCriterion.Existence f,
        ∀ (D : ValuativeCommSq f), IsDiscreteValuationRing D.R → D.commSq.HasLift ]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.15, Tag 0CM1](https://stacks.math.columbia.edu/tag/0CM1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
