---
declaration: section
origin: cited
lean: OAI.BinPackingGap.main_results
statement: formalized
proof: formalized
---

# 118. Bin packing and unbounded configuration-LP gaps

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Disproves the modified integer round-up conjecture of Scheithauer and Terno: the integral bin-packing optimum can exceed its configuration linear-programming value by an arbitrarily large additive constant. Approximating the optimum within any fixed additive constant is also NP-hard, even when every item exceeds 1/6 and each bin holds at most five items.

## Additive hardness and unbounded configuration gaps in bin packing

We disprove the Modified Integer Round-Up Conjecture for bin packing by constructing instances with arbitrarily large additive gaps between the configuration-LP value and the integral optimum. We also prove that, for every fixed nonnegative integer *c*, distinguishing instances that fit in *B* bins from those requiring more than $B+c$ bins is NP-hard. Both results hold with rational item sizes greater than 1/6, so each bin contains at most five items.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized results rule out a universal additive bound for the configuration linear program in bin packing. For every integer $c\ge0$, there are an integer $B$ and a rational instance with $5B$ items whose individual-copy and size-type configuration-LP values both equal $B$, but whose integral optimum is greater than $B+c$. Distinguishing a packing in $B$ bins from the absence of one in $B+c$ bins is NP-hard for each fixed $c$. A deterministic polynomial-time algorithm with a fixed absolute additive allowance exists exactly when $P=NP$; under that equality, an optimal algorithm is constructed.

## Lean: Unbounded configuration gaps and additive hardness

Stated in [BinPackingGap.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BinPackingGap.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main_results :
    (∀ c : ℕ, ∃ I : Instance, ∃ B : ℕ,
      I.n = 5 * B ∧
      (∀ i, (1 / 6 : ℚ) < I.size i ∧ I.size i < 1) ∧
      B + c < opt I ∧ individualLP I = (B : ℝ) ∧ typeLP I = (B : ℝ)) ∧
    (∀ c : Nat, PackingGapNPHard c) ∧
    ((∃ c : Nat, Nonempty (AbsoluteAdditiveAlgorithm c)) ↔ PEqualsNP) ∧
    (PEqualsNP → ∃ algorithm : AbsoluteAdditiveAlgorithm 0,
    (∀ (items : RawInstance) (valid : items.Valid), ∃ packing : RawPacking,
      algorithm.run (BinaryEncoding.rawInstanceBits items) = some packing ∧
      packing.Feasible items ∧ packing.bins = opt (items.toInstance valid)) ∧
    algorithm.run (BinaryEncoding.rawInstanceBits []) = some ⟨0, []⟩ ∧
    (∀ input : List Bool, BinaryEncoding.decodeRawInstance input = none →
      algorithm.run input = none) ∧
    (∀ items : RawInstance, ¬ items.Valid →
      algorithm.run (BinaryEncoding.rawInstanceBits items) = none))
```

Proved in [lean/OAI/Computability/BinPacking/Main.lean, line 7](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/BinPacking/Main.lean#L7).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/118.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/118.md)
