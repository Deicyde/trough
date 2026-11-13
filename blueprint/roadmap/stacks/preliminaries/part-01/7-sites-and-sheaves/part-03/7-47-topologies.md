---
declaration: section
origin: cited
lean: CategoryTheory.Sieve, CategoryTheory.Sieve.downward_closed, CategoryTheory.sieveSetEmbedding, CategoryTheory.Sieve.le_iff_forall_subset, CategoryTheory.Sieve.iSup_apply, CategoryTheory.Sieve.iInf_apply, CategoryTheory.Sieve.isLeast_ofArrows, CategoryTheory.Sieve.existsUnique_isLeast_arrows_mem
statement: formalized
proof: formalized
---

# 7.47 Topologies

Section 7.47 of the Stacks Project, [Tag 00YW](https://stacks.math.columbia.edu/tag/00YW). 8 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 15 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00YX, a definition

[Tag 00YX](https://stacks.math.columbia.edu/tag/00YX) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Sieve`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sieve#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Topology/TopologyDefs.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/TopologyDefs.lean#L21) (StacksFrontier): “a sieve on `U`, i.e. a subpresheaf of `h_U`”. References: SGA 3 IV (4.1.1), “special case”; SGA 4 I (4.1); SGA 4 I (4.3); SGA 4½ Arcata (1.1); SGA 4½ Arcata (1.3.4), “more general”; SGA 4½ Arcata (1.4.3); SGA 4½ Arcata (1.6.1); SGA 3 IV (4.1.7).
- [`CategoryTheory.Sieve.downward_closed`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sieve.downward_closed#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Topology/TopologyDefs.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/TopologyDefs.lean#L30) (StacksFrontier): “the closure condition that makes a collection of arrows into `U` a sieve: stability under precomposition”. References: SGA 3 IV (4.1.7), “downward closed”.

## Tag 00YY, an equation

[Tag 00YY](https://stacks.math.columbia.edu/tag/00YY) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Sieve.downward_closed`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sieve.downward_closed#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Topology/TopologyOrder.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/TopologyOrder.lean#L19) (StacksFrontier): “a sieve on `U` is stable under precomposition”. References: SGA 3 IV (4.1.7), “downward closed”.

## Tag 00YZ, a lemma

[Tag 00YZ](https://stacks.math.columbia.edu/tag/00YZ) in the Stacks Project.

**`CategoryTheory.sieveSetEmbedding`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topology/SieveLattice.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/SieveLattice.lean#L49). The attribute's comment: “(1)”.

> **Stacks 00YZ (1).** A sieve on `U` is a subpresheaf of `h_U`, so it is determined by the
> family of subsets `{f : V ⟶ U | f ∈ S}` of `h_U(V) = Hom(V, U)`. Thus the collection of sieves on
> `U` injects into `∏_V 𝒫(Hom(V, U))`, which is the source's proof that it is a set.

```lean
def sieveSetEmbedding (U : C) : Sieve U ↪ ∀ V : C, Set (V ⟶ U)
```

**`CategoryTheory.Sieve.le_iff_forall_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topology/SieveLattice.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/SieveLattice.lean#L59). The attribute's comment: “(2)”. References: SGA 3 IV (4.1.1), “special case”; SGA 4 I (4.3.2).

> **Stacks 00YZ (2).** The partial order on sieves on `U` is inclusion: `S ≤ T` holds exactly
> when the subset of `Hom(V, U)` cut out by `S` is contained in the one cut out by `T`, for every
> `V`.

```lean
theorem le_iff_forall_subset {S T : Sieve U} :
    S ≤ T ↔ ∀ V : C, sieveSetEmbedding U S V ⊆ sieveSetEmbedding U T V
```

**`CategoryTheory.Sieve.iSup_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topology/SieveLattice.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/SieveLattice.lean#L66). The attribute's comment: “(3)”. References: SGA 4 I (4.3.2), “union”.

> **Stacks 00YZ (3).** The union of a family of sieves on `U` is a sieve, namely their
> supremum: an arrow lies in `⨆ i, S i` exactly when it lies in some `S i`.

```lean
theorem iSup_apply {I : Type w} (S : I → Sieve U) {V : C} (f : V ⟶ U) :
    (⨆ i, S i) f ↔ ∃ i, S i f
```

**`CategoryTheory.Sieve.iInf_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topology/SieveLattice.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/SieveLattice.lean#L73). The attribute's comment: “(3)”. References: SGA 4 I (4.3.2), “intersection”.

> **Stacks 00YZ (3).** The intersection of a family of sieves on `U` is a sieve, namely their
> infimum: an arrow lies in `⨅ i, S i` exactly when it lies in every `S i`.

```lean
theorem iInf_apply {I : Type w} (S : I → Sieve U) {V : C} (f : V ⟶ U) :
    (⨅ i, S i) f ↔ ∀ i, S i f
```

**`CategoryTheory.Sieve.isLeast_ofArrows`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topology/SieveLattice.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/SieveLattice.lean#L81). The attribute's comment: “(4)”.

> **Stacks 00YZ (4).** Given a family `{Y i ⟶ U}` of morphisms with target `U`, the sieve
> `Sieve.ofArrows` it generates — the union of the images of the maps `h_{Y i} → h_U` — is the
> smallest sieve on `U` containing every `f i`.

```lean
theorem isLeast_ofArrows {I : Type w} (Y : I → C) (f : ∀ i, Y i ⟶ U) :
    IsLeast {S : Sieve U | ∀ i, S (f i)} (Sieve.ofArrows Y f)
```

**`CategoryTheory.Sieve.existsUnique_isLeast_arrows_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topology/SieveLattice.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/SieveLattice.lean#L93). The attribute's comment: “(4)”. References: SGA 4 I (4.3.3), “generated sieve”; SGA 4½ Arcata (1.6.1), “sieve generated by U\_i”.

> **Stacks 00YZ (4).** The smallest sieve on `U` containing a given family `{Y i ⟶ U}` of
> morphisms with target `U` is unique.

```lean
theorem existsUnique_isLeast_arrows_mem {I : Type w} (Y : I → C) (f : ∀ i, Y i ⟶ U) :
    ∃! S : Sieve U, IsLeast {S : Sieve U | ∀ i, S (f i)} S
```

**`CategoryTheory.Sieve.isGreatest_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topology/SieveLattice.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/SieveLattice.lean#L100). The attribute's comment: “(5)”.

> **Stacks 00YZ (5).** The sieve `h_U`, which contains every arrow with target `U`
> (`CategoryTheory.Sieve.top_apply`), is the maximal sieve on `U`.

```lean
theorem isGreatest_top : IsGreatest (Set.univ : Set (Sieve U)) ⊤
```

**`CategoryTheory.Sieve.isLeast_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topology/SieveLattice.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/SieveLattice.lean#L106). The attribute's comment: “(6)”.

> **Stacks 00YZ (6).** The empty subpresheaf of `h_U`, which contains no arrow at all
> (`CategoryTheory.Sieve.bot_apply`), is the minimal sieve on `U`.

```lean
theorem isLeast_bot : IsLeast (Set.univ : Set (Sieve U)) ⊥
```

Declarations registered for the tag:

- [`CategoryTheory.Sieve.top_apply`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sieve.top_apply#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Topology/SieveLattice.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/SieveLattice.lean#L116) (StacksFrontier): “(5)”.
- [`CategoryTheory.Sieve.bot_apply`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sieve.bot_apply#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Topology/SieveLattice.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/SieveLattice.lean#L117) (StacksFrontier): “(6)”.

## Tag 00Z1, a definition

[Tag 00Z1](https://stacks.math.columbia.edu/tag/00Z1) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Presieve.ofArrows`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Presieve.ofArrows#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Topology/TopologyInf.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/TopologyInf.lean#L21) (StacksFrontier): “the family of morphisms `{f i : U i ⟶ U}` as a presieve on `U`”.
- [`CategoryTheory.Sieve.generate`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sieve.generate#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Topology/TopologyInf.lean, line 23](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/TopologyInf.lean#L23) (StacksFrontier): “the sieve generated by a presieve on `U`”. References: SGA 3 IV (4.1.1), “special case”; SGA 3 IV (4.2.6); SGA 4 II (1.4); SGA 4½ Arcata (1.3.4), “more general”; SGA 4½ Arcata (1.6.1), “generated sieve”; SGA 4½ Arcata (1.4.3), “generated sieve”; SGA 4½ Arcata (1.1), “generated sieve”; SGA 4 I (4.3.3), “generated sieve”.
- [`CategoryTheory.Sieve.ofArrows`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sieve.ofArrows#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Topology/TopologyInf.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/TopologyInf.lean#L32) (StacksFrontier): “the sieve on `U` generated by a family of morphisms `{f i : U i ⟶ U}`, defined as the sieve generated by the corresponding presieve”. References: SGA 3 IV (4.1.1), “special case”; SGA 4 II (1.4); SGA 4½ Arcata (1.3.4), “more general”; SGA 4½ Arcata (1.6.1), “generated sieve”; SGA 4½ Arcata (1.4.3), “generated sieve”; SGA 4½ Arcata (1.1), “generated sieve”; SGA 4 I (4.3.3), “generated sieve”.

## Tag 00Z2, a definition

[Tag 00Z2](https://stacks.math.columbia.edu/tag/00Z2) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Sieve.pullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sieve.pullback#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Topology/TopologySup.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/TopologySup.lean#L20) (StacksFrontier): “the pullback `S ×_U V` of a sieve `S` on `U` along `f : V ⟶ U`”. References: SGA 4½ Arcata (1.6.1), “restriction U\_V”; SGA 4 I (4.3.1), “base change sieve”.
- [`CategoryTheory.Sieve.pullback_apply`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sieve.pullback_apply#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Topology/TopologySup.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/TopologySup.lean#L24) (StacksFrontier): “the defining rule `α ∈ S ×_U V ↔ α ≫ f ∈ S` for the pullback of a sieve”. References: SGA 4½ Arcata (1.6.1), “restriction U\_V”; SGA 4 I (4.3.1), “membership rule”.

## Tag 00Z3, a lemma

[Tag 00Z3](https://stacks.math.columbia.edu/tag/00Z3) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Sieve.pullback_eq_top_of_mem`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sieve.pullback_eq_top_of_mem#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Topology/TopologyGenerated.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/TopologyGenerated.lean#L19) (StacksFrontier): “pulling a sieve back along one of its own members gives the maximal sieve”.

## Tag 00Z8, a definition

[Tag 00Z8](https://stacks.math.columbia.edu/tag/00Z8) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Presheaf.IsSheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Presheaf.IsSheaf#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Stacks00Z8.lean, line 9](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Stacks00Z8.lean#L9) (StacksFrontier). References: EGA 0 (3.1.2); EGA 0 (3.1.4); SGA 3 IV (4.3.1), “more general”; SGA 3 IV (4.3.18); SGA 4 II (2.1), “more general”; SGA 4 II (2.7); SGA 4 II (6.1); SGA 4 II (6.2); SGA 4 II (6.3.2), “partial”; SGA 4½ Arcata (1.2.3), “more general”; SGA 7 VI (3.1(a)), “partial”.

## Tag 00Z9, a lemma

[Tag 00Z9](https://stacks.math.columbia.edu/tag/00Z9) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Sheaf.mem_finestTopology_of_forall_isSheafFor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.mem_finestTopology_of_forall_isSheafFor#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch07.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch07.lean#L45) (StacksFrontier): “Every sieve whose pullbacks along all V → U satisfy the sheaf condition for every F\_i lies in J; with sheaf\_for\_finestTopology and pullback stability this identifies J(U) with exactly the sieves of the Stacks construction.”. References: SGA 4 II (2.2), “partial”.
- [`CategoryTheory.Sheaf.sheaf_for_finestTopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.sheaf_for_finestTopology#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch07.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch07.lean#L49) (StacksFrontier): “All of the F\_i are sheaves for the topology J.”. References: SGA 3 IV (4.3.6), “more general”; SGA 4 II (2.2), “partial”; SGA 4 II (2.5), “more general”; SGA 4 IV (9.1.2), “9.1.2 d)”.
- [`CategoryTheory.Sheaf.le_finestTopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.le_finestTopology#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch07.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch07.lean#L51) (StacksFrontier): “J is the finest topology in which all of the F\_i are sheaves: every topology for which each F\_i is a sheaf is contained in J.”. References: SGA 3 IV (4.3.6), “more general”; SGA 4 II (2.2), “partial”; SGA 4 II (2.5), “more general”; SGA 4 II (2.5.1), “partial”; SGA 4 IV (9.1.2), “9.1.2 d)”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.47, Tag 00YW](https://stacks.math.columbia.edu/tag/00YW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
