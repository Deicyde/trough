---
declaration: section
origin: cited
lean: OAI.SnakyCertificate.certificate_correct, OAI.SnakyConditional.snaky_winning_strategy_with_legal_states, OAI.SnakyPrototype.snaky_winning_strategy_21_with_legal_states
statement: formalized
proof: formalized
---

# 187. Snaky in 21 Maker moves

1 manuscript and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Settles the Snaky achievement problem: Maker can force the six-cell Snaky shape within 21 of its own moves on the initially empty infinite square board. Maker moves first, each player claims one free cell per turn, and translations, rotations and reflections count as wins.

## Snaky in 21 Maker moves

We prove that Maker can achieve the Snaky hexomino within 21 actual Maker moves against arbitrary legal Breaker play on the initially empty infinite square board. The same bound holds on a $17\times17$ square; in fact, Maker can confine its claims to a fixed 251-cell board.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Snaky-in-21-Maker-moves-September-25-2026/article.pdf); the Lean below formalizes results from it.

## The Lean formalization

In the Snaky Maker–Breaker game, the players alternately claim cells of $\mathbb Z^2$, and Maker seeks a translated, rotated, or reflected copy of the six-cell Snaky shape. The formalization gives a legal strategy that wins within $21$ actual Maker moves against every legal Breaker play from the empty infinite board. The selected theorem checks disjointness and the move counts throughout play; it does not impose the paper's smaller finite-board restriction.

The linked supplements reconstruct the older $35$-move appendix's finite recursive certificate and prove four conditional winning templates from partial positions, assuming the required Maker cells are present and Breaker avoids the corresponding finite envelope.

## Lean: Reconstruction of the 35-move Snaky certificate

Stated in [SnakyCertificate.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SnakyCertificate.lean).

```lean
theorem certificate_correct :
    TableValid ∧ placementCount = 1837 ∧
    Output 557 (-1, 0) 118 19 {p | p.1 ≤ -3 ∧ p.2 ≤ -2} ∧
    Output 595 (-1, 0) 222 27 {p | p.1 = -2 ∧ p.2 ≤ -2} ∧
    Output 603 (-1, 0) 275 27 {p | p.1 ≤ -3 ∧ p.2 = 0} ∧
    Output 615 (1, 0) 686 34 {(1, -1)} ∧
    AllRows
```

Proved in [lean/OAI/Combinatorics/SnakyCertificate/Main.lean, line 50](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/SnakyCertificate/Main.lean#L50).

## Lean: Conditional winning templates from finite partial positions

Stated in [SnakyConditional.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SnakyConditional.lean).

```lean
theorem snaky_winning_strategy_with_legal_states :
    ∃ σ : Policy Cell,
      (∀ r M B, σ r M B ∉ M ∧ σ r M B ∉ B) ∧
      ∀ β : ℕ → Cell, LegalRepliesBeforeFinal σ 35 β ∅ ∅ →
        HasSnaky (playState σ 35 β ∅ ∅ 35).1 ∧
        (playState σ 35 β ∅ ∅ 35).1.card = 35 ∧
        Disjoint (playState σ 35 β ∅ ∅ 35).1 (playState σ 35 β ∅ ∅ 34).2 ∧
        ∀ k, k < 35 →
          Disjoint (playState σ 35 β ∅ ∅ k).1 (playState σ 35 β ∅ ∅ k).2 ∧
          (playState σ 35 β ∅ ∅ k).2.card = k
```

Proved in [lean/OAI/GameTheory/SnakyConditional/OriginalResult.lean, line 16](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/GameTheory/SnakyConditional/OriginalResult.lean#L16).

## Lean: Legal Snaky winning strategy within 21 Maker moves

Stated in [SnakyTwentyOne.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SnakyTwentyOne.lean).

```lean
theorem snaky_winning_strategy_21_with_legal_states :
    ∃ σ : Policy Cell,
      (∀ r M B, σ r M B ∉ M ∧ σ r M B ∉ B) ∧
      ∀ β : ℕ → Cell, LegalRepliesBeforeFinal σ 21 β ∅ ∅ →
        HasSnaky (playState σ 21 β ∅ ∅ 21).1 ∧
        (playState σ 21 β ∅ ∅ 21).1.card = 21 ∧
        Disjoint (playState σ 21 β ∅ ∅ 21).1 (playState σ 21 β ∅ ∅ 20).2 ∧
        ∀ k, k < 21 →
          Disjoint (playState σ 21 β ∅ ∅ k).1 (playState σ 21 β ∅ ∅ k).2 ∧
          (playState σ 21 β ∅ ∅ k).2.card = k
```

Proved in [lean/OAI/GameTheory/SnakyTwentyOne/Main.lean, line 18](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/GameTheory/SnakyTwentyOne/Main.lean#L18).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/187.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/187.md)
