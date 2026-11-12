---
declaration: section
origin: cited
lean: OAI.FiniteAlgebraicEnvelopes.main, OAI.SimpleFInftyOvergroups.main, OAI.UniversalFInfinity.universal_group_of_type_FInfinity
statement: formalized
proof: formalized
---

# 250. Boone–Higman embeddings with higher finiteness

3 manuscripts and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

A finitely generated group has decidable word problem exactly when it embeds in a finitely presented simple group, proving the Boone–Higman conjecture. The target can have type $F_{∞}$: a classifying space with finitely many cells in each dimension. A single group of type $F_{∞}$ can also contain every finitely presented group.

## Finite algebraic envelopes and the Boone–Higman conjecture

We prove the Boone–Higman conjecture. A finitely generated group has decidable word problem if and only if it embeds in a finitely presented simple group.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## Simple F∞ overgroups of groups with decidable word problem

Every finitely generated group with decidable word problem embeds in a simple group of type $F_{∞}$. This resolves the higher-finiteness strengthening of the Boone–Higman conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Simple-F-infinity-overgroups-of-groups-with-decidable-word-problem-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## A universal group of type F∞

We construct a single group of type $F_{∞}$ containing every finitely presented group. Its finitely generated subgroups, up to isomorphism, are exactly the finitely generated recursively presented groups. This answers the $F_{∞}$ form of the higher-dimensional Higman embedding question.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-universal-group-of-type-F-infinity-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The Boone–Higman conjecture characterizes finitely generated groups with decidable word problem by embeddings into finitely presented simple groups. The formalization proves the equivalence in full: a finitely generated group has a computable word problem for a finite generating set exactly when it embeds by an injective homomorphism into a finitely presented simple group.

The formalization proves the higher-finiteness strengthening of the Boone–Higman conjecture: every finitely generated group with decidable word problem embeds by an injective homomorphism into a nontrivial simple group of type $F_\infty$. Here type $F_\infty$ means that the group has a classifying CW complex with finitely many cells in each dimension. No additional finiteness property of the original group is assumed.

The formalized result constructs one group $H$ of type $F_\infty$ containing every finitely presented group. Here type $F_\infty$ means that $H$ has a classifying space with finitely many cells in each dimension.

The group $H$ is fixed before the groups embedded into it are chosen. No word-problem assumption is imposed, and the classifying space need not be finite-dimensional or have finitely many cells in total. The paper's converse about recursively presented subgroups is not included.

## Lean: Boone–Higman equivalence

Stated in [BooneHigman.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BooneHigman.lean).

```lean
theorem main (GroupType : Type u) [Group GroupType] [Group.FG GroupType] :
    HasDecidableWordProblem GroupType ↔ EmbedsInFinitelyPresentedSimpleGroup GroupType
```

Proved in [lean/OAI/GroupTheory/BooneHigman/Main.lean, line 115](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/GroupTheory/BooneHigman/Main.lean#L115).

## Lean: Simple type $F_\infty$ overgroups of groups with decidable word problem

Stated in [SimpleOvergroups.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SimpleOvergroups.lean).

```lean
theorem main (G : Type u) [Group G] [Group.FG G]
    (hG : HasDecidableWordProblem G) :
    ∃ (H : Type u) (_ : Group H), Nontrivial H ∧ IsSimpleGroup H ∧
      HasTypeFInfty H ∧ ∃ f : G →* H, Function.Injective f
```

Proved in [lean/OAI/GroupTheory/SimpleOvergroups/SourceProducer.lean, line 73](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/GroupTheory/SimpleOvergroups/SourceProducer.lean#L73).

## Lean: Universal group of type $F_\infty$

Stated in [UniversalFInfinity.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/UniversalFInfinity.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem universal_group_of_type_FInfinity :
    ∃ (H : Type u) (groupH : Group H),
      @HasTypeFInfinity H groupH ∧
      ∀ (G : Type u) [Group G] [Group.IsFinitelyPresented G],
        ∃ φ : G →* H, Function.Injective φ
```

Proved in [lean/OAI/GroupTheory/UniversalGroup/Main.lean, line 20](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/GroupTheory/UniversalGroup/Main.lean#L20).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/250.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/250.md)
