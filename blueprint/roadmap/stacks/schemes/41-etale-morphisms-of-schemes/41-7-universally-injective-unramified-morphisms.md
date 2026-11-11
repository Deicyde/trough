---
declaration: section
origin: cited
lean: AlgebraicGeometry.universallyInjective_unramified_tfae, AlgebraicGeometry.closedImmersion_conditions_tfae, AlgebraicGeometry.exists_open_restrict_isClosedImmersion_of_finite_unramified_fiber_eq_singleton
statement: formalized
proof: formalized
---

# 41.7 Universally injective, unramified morphisms

Section 41.7 of the Stacks Project, [Tag 06ND](https://stacks.math.columbia.edu/tag/06ND). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05VH, a lemma

[Tag 05VH](https://stacks.math.columbia.edu/tag/05VH) in the Stacks Project.

**`AlgebraicGeometry.universallyInjective_unramified_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/UniversallyInjectiveUnramified/Basic.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/UniversallyInjectiveUnramified/Basic.lean#L87). References: EGA IV (17.2.6); EGA IV (8.11.5.1), “loc. finite type case”.

> The equivalent characterizations of an unramified universally injective morphism of
> schemes.

```lean
public theorem universallyInjective_unramified_tfae {X S : Scheme.{u}} (f : X ⟶ S) :
    List.TFAE
      [ Unramified f ∧ Mono f,
        Unramified f ∧ UniversallyInjective f,
        LocallyOfFiniteType f ∧ Mono f,
        UniversallyInjective f ∧
          (LocallyOfFiniteType f ∧ FormallyUnramified f),
        LocallyOfFiniteType f ∧
          ∀ s : S, IsEmpty (f.fiber s) ∨ IsIso (f.fiberToSpecResidueField s) ]
```

## Tag 04XV, a lemma

[Tag 04XV](https://stacks.math.columbia.edu/tag/04XV) in the Stacks Project.

**`AlgebraicGeometry.closedImmersion_conditions_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/UniversallyInjectiveUnramified/ClosedImmersion.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/UniversallyInjectiveUnramified/ClosedImmersion.lean#L60). The attribute's comment: “(2) <=> (3) <=> (4) <=> (5) <=> (6) <=> (7)”. References: EGA IV (18.12.6), “b) <=> c)”; EGA IV (8.11.5), “b) <=> c)”.

> The six equivalent characterizations of a proper monomorphism, hence of a closed immersion,
> in parts (2) through (7).

```lean
public theorem closedImmersion_conditions_tfae {X S : Scheme.{u}} (f : X ⟶ S) :
    List.TFAE
      [ IsProper f ∧ Mono f,
        IsProper f ∧ (Unramified f ∧ UniversallyInjective f),
        UniversallyClosed f ∧ (Unramified f ∧ Mono f),
        UniversallyClosed f ∧ (Unramified f ∧ UniversallyInjective f),
        UniversallyClosed f ∧ (LocallyOfFiniteType f ∧ Mono f),
        UniversallyClosed f ∧
          (UniversallyInjective f ∧ (LocallyOfFiniteType f ∧ FormallyUnramified f)) ]
```

## Tag 04DG, a lemma

[Tag 04DG](https://stacks.math.columbia.edu/tag/04DG) in the Stacks Project.

**`AlgebraicGeometry.exists_open_restrict_isClosedImmersion_of_finite_unramified_fiber_eq_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/UniversallyInjectiveUnramified/FiniteUnramified.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/UniversallyInjectiveUnramified/FiniteUnramified.lean#L147).

> A finite unramified morphism with a singleton fibre and purely inseparable residue-field
> extension is a closed immersion over some neighbourhood of the point in the target.

```lean
public theorem exists_open_restrict_isClosedImmersion_of_finite_unramified_fiber_eq_singleton
    {X S : Scheme.{u}} (f : X ⟶ S) [IsFinite f] [Unramified f]
    (s : S) (x : X) (hfiber : f ⁻¹' {s} = {x})
    (hpure :
      let hxs : f x = s := by
        have : x ∈ f ⁻¹' {s} := by simp [hfiber]
        simpa only [Set.mem_preimage, Set.mem_singleton_iff] using this
      letI := ((S.residueFieldCongr hxs).inv ≫ f.residueFieldMap x).hom.toAlgebra
      IsPurelyInseparable (S.residueField s) (X.residueField x)) :
    ∃ U : S.Opens, s ∈ U ∧ IsClosedImmersion (f ∣_ U)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 41.7, Tag 06ND](https://stacks.math.columbia.edu/tag/06ND)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
