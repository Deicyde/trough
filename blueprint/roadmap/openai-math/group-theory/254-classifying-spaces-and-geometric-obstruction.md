---
declaration: section
origin: cited
lean: OAI.HarmonicArtin.salvetti_cover_contractible, OAI.ArtinCAT0.main, OAI.HarmonicArtin.ParabolicIntersections.unconditional_parabolic_intersections, OAI.HarmonicArtin.ParabolicIntersections.unconditional_arbitrary_intersections, OAI.HarmonicArtin.ParabolicIntersections.unconditional_parabolic_closure, OAI.HarmonicArtin.ParabolicIntersections.unconditional_nonclique_dynamics
statement: formalized
proof: formalized
---

# 254. Classifying spaces and geometric obstructions for Artin groups

3 manuscripts and 6 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

The Salvetti complex of every finite-rank Artin group is aspherical, proving the Artin $K(\pi,1)$ conjecture. Arbitrary intersections of its parabolic subgroups are parabolic, proving the Parabolic Intersection Conjecture. An explicit Artin group admits no proper cocompact isometric action on any nonempty proper CAT$(0)$ space.

## Harmonic heights and the Artin K(pi,1) conjecture

We prove that the standard Salvetti complex of every Artin group with finitely many standard generators is aspherical. This resolves the Artin $K(\pi,1)$ conjecture in finite rank.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Harmonic-heights-and-the-Artin-K-pi-1-conjecture-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## An Artin group with no geometric CAT(0) action

We construct an Artin group on 116 generators that admits no proper, cocompact isometric action on a nonempty proper CAT(0) space. This refutes the CAT(0) conjecture for Artin groups.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-Artin-group-with-no-geometric-CAT-0-action-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## Parabolic intersections in Artin groups

We prove that every intersection of parabolic subgroups of any finite-rank Artin group, with arbitrary finite or infinite Coxeter labels, is parabolic. This resolves the Parabolic Intersection Conjecture affirmatively.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Parabolic-intersections-in-Artin-groups-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The Artin $K(\pi,1)$ conjecture asserts that the standard Salvetti complex of every finite-rank Artin group is aspherical. The formalized result proves the equivalent statement that its universal cover is contractible.

It applies to every Coxeter matrix on a finite generating set, including empty and disconnected diagrams and infinite edge labels. The associated Coxeter and Artin groups may be infinite. Later corollaries in the manuscript are not included.

The geometric-action question asks whether every Artin group acts properly and cocompactly by isometries on a proper CAT(0) space. The formalized result gives a counterexample: an Artin group defined by a symmetric matrix on $116$ generators, with diagonal entries $1$ and off-diagonal entries in $\{2,3,\infty\}$.

It admits no such action on any nonempty proper CAT(0) space, in any dimension.

The formalization proves that the intersection of any family of parabolic subgroups of a finite-rank Artin group is parabolic. Every such intersection is already the intersection of at most the rank many members, and every subset has a unique parabolic closure. Both finite and infinite Coxeter labels are allowed.

For irreducible Artin groups with an infinite Coxeter label, it also proves acylindrical hyperbolicity and weak malnormality of every proper parabolic subgroup. These are the intersection and structural consequences selected from the paper.

## Lean: Contractibility of the Salvetti cover

```lean
theorem salvetti_cover_contractible [Finite S] (M : CoxeterMatrix S) :
    ContractibleSpace (SalvettiCover M)
```

Stated in [HarmonicArtin.lean, line 59](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HarmonicArtin.lean#L59). Proved in [lean/OAI/Topology/ArtinGroups/Realizations/SalvettiCoverContractible.lean, line 11](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Topology/ArtinGroups/Realizations/SalvettiCoverContractible.lean#L11). formalization.yaml lists it as one of the repository's main results.

## Lean: Artin group with no geometric $\mathrm{CAT}(0)$ action

```lean
theorem main :
    (∀ s t : Letters, explicitMatrix s t = explicitMatrix t s) ∧
    (∀ s : Letters, explicitMatrix s s = 1) ∧
    (∀ s t : Letters, s ≠ t →
      explicitMatrix s t = 2 ∨ explicitMatrix s t = 3 ∨ explicitMatrix s t = ⊤) ∧
    (∀ (X : Type u) [MetricSpace X] [ProperSpace X] [Nonempty X]
      [MulAction (ArtinGroup explicitMatrix) X],
      ¬ GeometricAction (ArtinGroup explicitMatrix) X)
```

Stated in [ArtinCAT0.lean, line 65](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ArtinCAT0.lean#L65). Proved in [lean/OAI/GroupTheory/ArtinCAT0/Main.lean, line 53](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/GroupTheory/ArtinCAT0/Main.lean#L53). formalization.yaml lists it as one of the repository's main results.

## Lean: Parabolic intersections, closures, and structural consequences

```lean
theorem unconditional_parabolic_intersections
    (X Y : Set S) (g h : Artin M) :
    ∃ (Z : Set S) (k : Artin M),
      conjugate g (artinParabolic M X) ⊓ conjugate h (artinParabolic M Y) =
        conjugate k (artinParabolic M Z)
```

Stated in [ArtinParabolicIntersections.lean, line 98](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ArtinParabolicIntersections.lean#L98). Proved in [lean/OAI/Topology/ArtinGroups/ParabolicIntersections/UnconditionalMain.lean, line 31](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Topology/ArtinGroups/ParabolicIntersections/UnconditionalMain.lean#L31).

```lean
theorem unconditional_arbitrary_intersections
    (F : Set (Subgroup (Artin M))) (hF : ∀ P ∈ F, IsParabolic M P) :
    (∃ F₀ : Finset (Subgroup (Artin M)),
      (↑F₀ : Set (Subgroup (Artin M))) ⊆ F ∧ F₀.card ≤ Nat.card S ∧
        sInf F = sInf (↑F₀ : Set (Subgroup (Artin M)))) ∧ IsParabolic M (sInf F)
```

Stated in [ArtinParabolicIntersections.lean, line 106](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ArtinParabolicIntersections.lean#L106). Proved in [lean/OAI/Topology/ArtinGroups/ParabolicIntersections/UnconditionalMain.lean, line 39](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Topology/ArtinGroups/ParabolicIntersections/UnconditionalMain.lean#L39).

```lean
theorem unconditional_parabolic_closure (E : Set (Artin M)) :
    ∃! P : Subgroup (Artin M), IsParabolic M P ∧ E ⊆ P ∧
      ∀ Q : Subgroup (Artin M), IsParabolic M Q → E ⊆ Q → P ≤ Q
```

Stated in [ArtinParabolicIntersections.lean, line 114](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ArtinParabolicIntersections.lean#L114). Proved in [lean/OAI/Topology/ArtinGroups/ParabolicIntersections/UnconditionalMain.lean, line 47](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Topology/ArtinGroups/ParabolicIntersections/UnconditionalMain.lean#L47).

```lean
theorem unconditional_nonclique_dynamics
    (hIrred : IsIrreducible M) (hInf : ∃ s t : S, s ≠ t ∧ M s t = 0) :
    AcylindricallyHyperbolic (Artin M) ∧
      ∀ P : Subgroup (Artin M), IsParabolic M P → P ≠ ⊤ → WeaklyMalnormal P
```

Stated in [ArtinParabolicIntersections.lean, line 121](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ArtinParabolicIntersections.lean#L121). Proved in [lean/OAI/Topology/ArtinGroups/ParabolicIntersections/DynamicsUnconditional.lean, line 20](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Topology/ArtinGroups/ParabolicIntersections/DynamicsUnconditional.lean#L20).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/254.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/254.md)
