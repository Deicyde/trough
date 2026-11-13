---
declaration: section
origin: cited
lean: sieve_sheafification_iff, CategoryTheory.topology_eq_iff_same_sheaves, le_iff_isSheaf_imp_isSheaf
statement: formalized
proof: formalized
---

# 7.50 Topologies and sheaves

Section 7.50 of the Stacks Project, [Tag 00ZN](https://stacks.math.columbia.edu/tag/00ZN). 3 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00ZO, a lemma

[Tag 00ZO](https://stacks.math.columbia.edu/tag/00ZO) in the Stacks Project.

**`sieve_sheafification_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topology/SieveSheafification.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/SieveSheafification.lean#L42). References: SGA 4 II (5.3), “sieve inclusion S→h\_U”; SGA 3 IV (4.3.12), “special case”; SGA 4 II (4.6.1), “more general”; SGA 4 II (5.1), “special case”; SGA 4 II (5.5), “Ψ ∘ Φ = id”.

> **Stacks 00ZO.** A sieve `S` on `U` is a covering sieve for the topology `J` if and only if
> the sheafification `S^# ⟶ h_U^#` of its inclusion `S ↪ h_U` (i.e. the image under the
> associated-sheaf functor of `S.functorInclusion`) is an isomorphism.

```lean
theorem sieve_sheafification_iff {C : Type u} [SmallCategory C] (J : GrothendieckTopology C)
    (U : C) (S : Sieve U) :
    S ∈ J U ↔ IsIso ((presheafToSheaf J (Type u)).map S.functorInclusion)
```

## Tag 00ZP, a theorem

[Tag 00ZP](https://stacks.math.columbia.edu/tag/00ZP) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.topology_eq_iff_same_sheaves`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.topology_eq_iff_same_sheaves#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Topology/ContinuousForTopology.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/ContinuousForTopology.lean#L19) (StacksFrontier): “two topologies are equal exactly when they have the same `Type`-valued sheaves”. References: SGA 4 IV (9.1.2), “9.1.2 c)”.

## Tag 00ZQ, a lemma

[Tag 00ZQ](https://stacks.math.columbia.edu/tag/00ZQ) in the Stacks Project.

**`le_iff_isSheaf_imp_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topology/SupOfSheaves.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/SupOfSheaves.lean#L55).

> **Stacks 00ZQ.** For Grothendieck topologies `J`, `J'` on a category `C`, we have `J ≤ J'`
> (every `J`-covering sieve is `J'`-covering) if and only if every sheaf for `J'` is a sheaf
> for `J`.

```lean
theorem le_iff_isSheaf_imp_isSheaf :
    J ≤ J' ↔
      ∀ (P : Cᵒᵖ ⥤ Type (max u v)),
        Presheaf.IsSheaf J' P → Presheaf.IsSheaf J P
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.50, Tag 00ZN](https://stacks.math.columbia.edu/tag/00ZN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
