---
declaration: section
origin: cited
lean: Specializes, StableUnderSpecialization, StableUnderGeneralization, IsClosed.stableUnderSpecialization, IsOpen.stableUnderGeneralization, stableUnderGeneralization_compl_iff, stableUnderSpecialization_iff_exists_directedOn_sUnion_eq, stableUnderSpecialization_iff_exists_sUnion_eq
statement: formalized
proof: formalized
---

# 5.19 Specialization

Section 5.19 of the Stacks Project, [Tag 0060](https://stacks.math.columbia.edu/tag/0060). 10 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 11 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0061, a definition

[Tag 0061](https://stacks.math.columbia.edu/tag/0061) in the Stacks Project.

Declarations registered for the tag:

- [`Specializes`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Specializes#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Specialization/Defs.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Specialization/Defs.lean#L19) (StacksFrontier): “specialization and generalization of points”. References: EGA I (2.4.2); EGA IV (21.13.15); EGA 0 (2.1.2), “specialization relation”; SGA 1 IV (6.3); SGA 4 IV (4.2.2); SGA 7 IX (3.1).
- [`StableUnderSpecialization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=StableUnderSpecialization#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Specialization/Defs.lean, line 26](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Specialization/Defs.lean#L26) (StacksFrontier): “subsets stable under specialization”. References: EGA IV (5.9.1).
- [`StableUnderGeneralization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=StableUnderGeneralization#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Specialization/Defs.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Specialization/Defs.lean#L28) (StacksFrontier): “subsets stable under generalization”. References: EGA IV (7.4.1), “partial”.

## Tag 0062, a lemma

[Tag 0062](https://stacks.math.columbia.edu/tag/0062) in the Stacks Project.

Declarations registered for the tag:

- [`IsClosed.stableUnderSpecialization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsClosed.stableUnderSpecialization#doc) registered with `add_to_stacks` in [StacksCore/Topology/Specialization/StableSets.lean, line 23](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Specialization/StableSets.lean#L23) (StacksCore): “(1)”. References: EGA II (7.2.2), “Necessity”.
- [`IsOpen.stableUnderGeneralization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsOpen.stableUnderGeneralization#doc) registered with `add_to_stacks` in [StacksCore/Topology/Specialization/StableSets.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Specialization/StableSets.lean#L24) (StacksCore): “(2)”. References: EGA IV (6.11.6.1), “necessity”; SGA 1 IV (6.4), “(a)”.
- [`stableUnderGeneralization_compl_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=stableUnderGeneralization_compl_iff#doc) registered with `add_to_stacks` in [StacksCore/Topology/Specialization/StableSets.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Specialization/StableSets.lean#L25) (StacksCore): “(3)”.

## Tag 0EES, a lemma

[Tag 0EES](https://stacks.math.columbia.edu/tag/0EES) in the Stacks Project.

**`stableUnderSpecialization_iff_exists_directedOn_sUnion_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Specialization/UnionOfClosedDirected.lean, line 29](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Specialization/UnionOfClosedDirected.lean#L29). The attribute's comment: “directed form: (1) ⇔ (2) with the family of closed subsets directed under inclusion; the undirected form is Mathlib's `stableUnderSpecialization_iff_exists_sUnion_eq`”.

> A subset `T` of a topological space is stable under specialization if and only if it is the
> union of a family of closed subsets which is directed under inclusion.

```lean
theorem stableUnderSpecialization_iff_exists_directedOn_sUnion_eq {T : Set X} :
    StableUnderSpecialization T ↔
      ∃ S : Set (Set X), DirectedOn (· ⊆ ·) S ∧ (∀ Z ∈ S, IsClosed Z) ∧ ⋃₀ S = T
```

Declarations registered for the tag:

- [`stableUnderSpecialization_iff_exists_sUnion_eq`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=stableUnderSpecialization_iff_exists_sUnion_eq#doc) registered with `add_to_stacks` in [StacksCore/Topology/Specialization/UnionOfClosed.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Specialization/UnionOfClosed.lean#L21) (StacksCore): “stable under specialization iff a union of closed sets”. References: EGA IV (5.9.1), “Z = union of closeds”.

## Tag 0063, a definition

[Tag 0063](https://stacks.math.columbia.edu/tag/0063) in the Stacks Project.

**`LiftsSpecializations`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Specialization/Lifting.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Specialization/Lifting.lean#L24). References: EGA II (7.2.1).

> **Stacks 0063.** Specializations lift along `f : X → Y` if for every `y' ⤳ y` in `Y` and every
> `x' : X` with `f x' = y'` there is a specialization `x' ⤳ x` in `X` with `f x = y`.

```lean
def LiftsSpecializations (f : X → Y) : Prop
```

**`LiftsGeneralizations`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Specialization/Lifting.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Specialization/Lifting.lean#L30). References: EGA IV (2.3.4).

> **Stacks 0063.** Generalizations lift along `f : X → Y` if for every `y' ⤳ y` in `Y` and every
> `x : X` with `f x = y` there is a generalization `x' ⤳ x` in `X` with `f x' = y'`.

```lean
def LiftsGeneralizations (f : X → Y) : Prop
```

## Tag 0064, a lemma

[Tag 0064](https://stacks.math.columbia.edu/tag/0064) in the Stacks Project.

Declarations registered for the tag:

- [`SpecializingMap.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SpecializingMap.comp#doc) registered with `add_to_stacks` in [StacksCore/Topology/Specialization/LiftingBaseChange.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Specialization/LiftingBaseChange.lean#L21) (StacksCore): “specializations lift along a composition”.
- [`GeneralizingMap.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=GeneralizingMap.comp#doc) registered with `add_to_stacks` in [StacksCore/Topology/Specialization/LiftingBaseChange.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Specialization/LiftingBaseChange.lean#L22) (StacksCore): “generalizations lift along a composition”.

## Tag 0065, a lemma

[Tag 0065](https://stacks.math.columbia.edu/tag/0065) in the Stacks Project.

Declarations registered for the tag:

- [`SpecializingMap.stableUnderSpecialization_image`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SpecializingMap.stableUnderSpecialization_image#doc) registered with `add_to_stacks` in [StacksCore/Topology/Specialization/ImageStable.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Specialization/ImageStable.lean#L25) (StacksCore): “(1) the image is stable under specialization”.
- [`GeneralizingMap.stableUnderGeneralization_image`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=GeneralizingMap.stableUnderGeneralization_image#doc) registered with `add_to_stacks` in [StacksCore/Topology/Specialization/ImageStable.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Specialization/ImageStable.lean#L27) (StacksCore): “(2) the image is stable under generalization”.

## Tag 0066, a lemma

[Tag 0066](https://stacks.math.columbia.edu/tag/0066) in the Stacks Project.

**`specializations_lift_of_isClosedMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Specialization/LiftingClosedOpen.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Specialization/LiftingClosedOpen.lean#L97). The attribute's comment: “(1)”. References: EGA II (7.2.1), “a ⇒ b”.

> **Stacks 0066** (1).
> If `f` is a closed continuous map, then specializations lift along `f`.

```lean
theorem specializations_lift_of_isClosedMap
    (f : X → Y) (hf_cont : Continuous f) (hf_closed : IsClosedMap f) :
    SpecializationsLiftAlong f
```

**`generalizations_lift_of_isOpenMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Specialization/LiftingClosedOpen.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Specialization/LiftingClosedOpen.lean#L111). The attribute's comment: “(2)”. References: EGA IV (1.10.3), “a) ⇒ b)”; EGA IV (1.10.4), “a) ⇒ b), special case”; EGA IV (14.1.6), “special case”; EGA IV (2.3.5), “(i), special case”; SGA 1 IV (6.5), “partial”.

> **Stacks 0066** (2).
> If `f : X → Y` is an open continuous map, `X` is Noetherian with a generic point for every
> irreducible closed subset, and `Y` is `T₀`, then generalizations lift along `f`.

```lean
theorem generalizations_lift_of_isOpenMap
    (f : X → Y) (hf_cont : Continuous f) (hf_open : IsOpenMap f)
    [hX_noeth : NoetherianSpace X]
    (hX_generic : ∀ (Z : Set X), IsIrreducible Z → IsClosed Z →
                    ∃ η : X, IsGenericPoint η Z)
    [hY_t0 : T0Space Y] :
    GeneralizationsLiftAlong f
```

## Tag 06NA, a lemma

[Tag 06NA](https://stacks.math.columbia.edu/tag/06NA) in the Stacks Project.

**`Topology.t0Space_of_isOpenMap_of_finite_fibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Separation/KolmogorovQuotient.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Separation/KolmogorovQuotient.lean#L198).

> If `π : U → X` is an open surjection from a `T0Space`, and `π` identifies exactly the pairs
> related by the image of `(t, s) : R → U × U` for a map `t` with finite fibres, then `X` is
> Kolmogorov.
>
> This generalizes Stacks 06NA: soberness of `U` is weakened to `T0Space U`, only `t` is assumed to
> have finite fibres, and the lifting of generalizations along `s` and `t` is not assumed. See the
> module docstring.

```lean
theorem t0Space_of_isOpenMap_of_finite_fibres {R U X : Type*} [TopologicalSpace U] [T0Space U]
    [TopologicalSpace X] (s t : R → U) (π : U → X) (hπ_open : IsOpenMap π)
    (ht_fin : Function.HasFiniteFibres t) (hπ_surj : Function.Surjective π)
    (hπ_rel : ∀ u u' : U, π u = π u' ↔ Function.SourceTargetRel s t u u') :
    T0Space X
```

## Tag 02JF, a lemma

[Tag 02JF](https://stacks.math.columbia.edu/tag/02JF) in the Stacks Project.

**`Topology.topologicalKrullDim_le_of_surjective_of_specializingMap_or_generalizingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/SpecializingSurjection.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/SpecializingSurjection.lean#L190).

> Let `f : X → Y` be a continuous surjection of topological spaces with `Y`
> sober. If specializations lift along `f`, or generalizations lift along `f`, then the Krull
> dimension of `Y` is at most the Krull dimension of `X`.

```lean
theorem topologicalKrullDim_le_of_surjective_of_specializingMap_or_generalizingMap
    {X Y : Type*} [TopologicalSpace X] [TopologicalSpace Y] [QuasiSober Y] [T0Space Y]
    (f : X → Y) (hf : Continuous f) (hsurj : Function.Surjective f)
    (h : SpecializingMap f ∨ GeneralizingMap f) :
    topologicalKrullDim Y ≤ topologicalKrullDim X
```

## Tag 0542, a lemma

[Tag 0542](https://stacks.math.columbia.edu/tag/0542) in the Stacks Project.

**`isOpen_of_stableUnderGeneralization_of_isConstructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Specialization/Constructible.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Specialization/Constructible.lean#L79). The attribute's comment: “(2)”. References: EGA IV (12.0.2), “more general”; EGA IV (2.3.6), “(i), special case”; EGA IV (7.9.10), “(ii)”; SGA 1 IV (6.3), “special case”; SGA 1 IV (6.4), “special case”; SGA 3 XV (3.3), “special case”; SGA 3 XV (6.6), “special case”.

> **Stacks 0542** (2).
> In a Noetherian sober topological space, every constructible subset that is stable under
> generalization is open.

```lean
theorem isOpen_of_stableUnderGeneralization_of_isConstructible
    (X : Type u) [TopologicalSpace X] [NoetherianSpace X] [QuasiSober X] [T0Space X]
    (E : Set X) (hcon : Topology.IsConstructible E) (hgen : StableUnderGeneralization E) :
    IsOpen E
```

**`isClosed_of_stableUnderSpecialization_of_isConstructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Specialization/Constructible.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Specialization/Constructible.lean#L90). The attribute's comment: “(1)”. References: SGA 3 XV (3.3), “special case”.

> **Stacks 0542** (1).
> In a Noetherian sober topological space, every constructible subset that is stable under
> specialization is closed.

```lean
theorem isClosed_of_stableUnderSpecialization_of_isConstructible
    (X : Type u) [TopologicalSpace X] [NoetherianSpace X] [QuasiSober X] [T0Space X]
    (E : Set X) (hcon : Topology.IsConstructible E) (hspec : StableUnderSpecialization E) :
    IsClosed E
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.19, Tag 0060](https://stacks.math.columbia.edu/tag/0060)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
