---
declaration: section
origin: cited
lean: Stacks.Etale.tfae_isOpenImmersion, AlgebraicGeometry.IsOpenImmersion.mono, AlgebraicGeometry.instUniversallyInjectiveOfMonoScheme, AlgebraicGeometry.Etale.instOfIsOpenImmersion, AlgebraicGeometry.Flat.instOfIsOpenImmersion, AlgebraicGeometry.locallyOfFinitePresentation_of_isOpenImmersion, AlgebraicGeometry.isOpenImmersion_of_etale_universallyInjective, AlgebraicGeometry.IsOpenImmersion.of_flat_of_mono
statement: formalized
proof: formalized
---

# 41.14 Topological properties of étale morphisms

Section 41.14 of the Stacks Project, [Tag 025F](https://stacks.math.columbia.edu/tag/025F). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 025G, a theorem

[Tag 025G](https://stacks.math.columbia.edu/tag/025G) in the Stacks Project.

**`Stacks.Etale.tfae_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvariance/MorphismDescent.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvariance/MorphismDescent.lean#L94). References: EGA IV (17.9.1); SGA 1 I (5.1), “more general”; SGA 3 X (3.7), “partial”; SGA 3 XXII (5.4.10), “Footnote (36)”; SGA 7 IX (3.1.3), “more general”.

> **Stacks Project, Tag 025G.** For a morphism of schemes, being an open immersion, being
> universally injective and étale, and being a flat monomorphism locally of finite presentation
> are all equivalent.

```lean
theorem tfae_isOpenImmersion {A B : Scheme.{u}} (g : A ⟶ B) :
    List.TFAE [IsOpenImmersion g, UniversallyInjective g ∧ Etale g,
      Flat g ∧ Mono g ∧ LocallyOfFinitePresentation g]
```

Declarations registered for the tag:

- [`AlgebraicGeometry.IsOpenImmersion.mono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsOpenImmersion.mono#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Etale/TopologicalProperties/OpenImmersion.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/TopologicalProperties/OpenImmersion.lean#L45) (StacksFrontier): “(1) implies (2) and (3): monomorphism”. References: EGA I (2.2.3), “more general”; EGA IV (17.11.5), “necessity”; EGA IV (17.9.1), “(a)”; EGA IV (18.10.5), “necessity”; SGA 1 V (3.6), “monomorphism”.
- [`AlgebraicGeometry.instUniversallyInjectiveOfMonoScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instUniversallyInjectiveOfMonoScheme#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Etale/TopologicalProperties/OpenImmersion.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/TopologicalProperties/OpenImmersion.lean#L52) (StacksFrontier): “(1) implies (2): universal injectivity”. References: EGA IV (17.2.6), “a) ⇒ radicial part of b)”; SGA 3 VIB (2.6).
- [`AlgebraicGeometry.Etale.instOfIsOpenImmersion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Etale.instOfIsOpenImmersion#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Etale/TopologicalProperties/OpenImmersion.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/TopologicalProperties/OpenImmersion.lean#L57) (StacksFrontier): “(1) implies (2): étale”. References: EGA IV (17.1.3), “more general”; EGA IV (17.3.3); EGA IV (17.9.1), “(a) ⇒ étaleness in (c)”; SGA 1 I (4.6); SGA 1 I (5.1), “necessity”; SGA 1 IX (1.4), “Necessity”.
- [`AlgebraicGeometry.Flat.instOfIsOpenImmersion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Flat.instOfIsOpenImmersion#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Etale/TopologicalProperties/OpenImmersion.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/TopologicalProperties/OpenImmersion.lean#L64) (StacksFrontier): “(1) implies (3): flat”. References: EGA IV (17.9.1), “(a) ⇒ flatness in (b)”; EGA IV (8.1.2), “partial”.
- [`AlgebraicGeometry.locallyOfFinitePresentation_of_isOpenImmersion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.locallyOfFinitePresentation_of_isOpenImmersion#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Etale/TopologicalProperties/OpenImmersion.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/TopologicalProperties/OpenImmersion.lean#L67) (StacksFrontier): “(1) implies (3): locally of finite presentation”. References: EGA IV (1.4.3), “(i), open immersions”; EGA IV (17.9.1), “(a)”.
- [`AlgebraicGeometry.isOpenImmersion_of_etale_universallyInjective`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FpqcDescentApplication/OpenImmersion.lean#L53), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Etale/TopologicalProperties/OpenImmersion.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/TopologicalProperties/OpenImmersion.lean#L72) (StacksFrontier): “(2) implies (1)”.
- [`AlgebraicGeometry.IsOpenImmersion.of_flat_of_mono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsOpenImmersion.of_flat_of_mono#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Etale/TopologicalProperties/OpenImmersion.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/TopologicalProperties/OpenImmersion.lean#L74) (StacksFrontier): “(3) implies (1)”. References: EGA IV (17.9.1), “(b) ⇒ (a)”; EGA IV (17.9.2), “partial”; SGA 1 I (5.1), “special case”; SGA 3 X (3.7), “partial”; SGA 3 XXII (5.4.10), “more general”.

## Tag 04DH, a lemma

[Tag 04DH](https://stacks.math.columbia.edu/tag/04DH) in the Stacks Project.

**`AlgebraicGeometry.exists_open_restrict_isIso_of_finite_etale_fiber_eq_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/SingletonFibre.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/SingletonFibre.lean#L166).

> **Stacks Project, Tag 04DH.** A finite étale morphism with a singleton fibre and purely
> inseparable residue-field extension is an isomorphism over some open neighbourhood of the
> point in the target.

```lean
theorem exists_open_restrict_isIso_of_finite_etale_fiber_eq_singleton
    {X S : Scheme.{u}} (f : X ⟶ S) [IsFinite f] [Etale f]
    (s : S) (x : X) (hfiber : f ⁻¹' {s} = {x})
    (hpure :
      let hxs : f x = s := by
        have : x ∈ f ⁻¹' {s} := by simp [hfiber]
        simpa only [Set.mem_preimage, Set.mem_singleton_iff] using this
      letI := ((S.residueFieldCongr hxs).inv ≫ f.residueFieldMap x).hom.toAlgebra
      IsPurelyInseparable (S.residueField s) (X.residueField x)) :
    ∃ U : S.Opens, s ∈ U ∧ IsIso (f ∣_ U)
```

## Tag 0EBS, a lemma

[Tag 0EBS](https://stacks.math.columbia.edu/tag/0EBS) in the Stacks Project.

**`AlgebraicGeometry.isIso_relativeFrobenius_of_etale`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/TopologicalProperties/RelativeFrobenius.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/TopologicalProperties/RelativeFrobenius.lean#L34). References: SGA 4½ Fonctions L (3.4); SGA 5 XV (1.Proposition2), “Clause c) 2)”.

> The relative Frobenius of an étale scheme is an isomorphism.

```lean
public instance isIso_relativeFrobenius_of_etale (X : Scheme.{u}) (p : ℕ)
    [Fact p.Prime] (hX : IsInCharacteristic X p) (U : Over X) [Etale U.hom] :
    IsIso (relativeFrobenius X p hX U)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 41.14, Tag 025F](https://stacks.math.columbia.edu/tag/025F)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
