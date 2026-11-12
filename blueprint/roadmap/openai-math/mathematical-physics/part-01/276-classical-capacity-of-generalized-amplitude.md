---
declaration: section
origin: cited
lean: OAI.GAD.main
statement: formalized
proof: formalized
---

# 276. Classical capacity of generalized amplitude damping

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Determines the unassisted classical capacity of every qubit generalized amplitude-damping channel, including all damping and thermal parameters. An explicit one-variable optimization gives the capacity, attained by independent two-state signal ensembles with collective decoding. Holevo capacity, minimum output entropy and regularized classical capacity are additive when tensoring with any finite-dimensional quantum channel.

## Classical capacity and entropy inequalities for generalized amplitude damping

We determine the unassisted classical capacity of every qubit generalized amplitude-damping channel, for all damping strengths and thermal occupations. It equals the one-shot Holevo capacity and is given by a one-variable maximum. A binary pure-state ensemble attains the one-use optimum, and its independent products attain the optimum at every block length. We also prove that one-shot Holevo capacity, minimum output entropy, and regularized unassisted classical capacity are additive under tensor product with every finite-dimensional completely positive trace-preserving partner channel.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result determines the unassisted classical capacity of every generalized amplitude-damping channel with parameters in $[0,1]^2$. Its unrestricted Holevo information is additive across every number of repeated uses, equals an attained scalar maximum, and agrees with the operational capacity per use. Every maximizing equiprobable phase-pair product ensemble attains the corresponding block value. Additivity with an arbitrary different partner channel and decoding by separate measurements are not included.

## Lean: Additivity and capacity for generalized amplitude damping

Stated in [AmplitudeDamping.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/AmplitudeDamping.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main (γ ν : ℝ) (hγ : γ ∈ Set.Icc (0 : ℝ) 1)
    (hν : ν ∈ Set.Icc (0 : ℝ) 1) :
    (∀ n : ℕ, 1 ≤ n → holevo γ ν n = (n : ℝ) * holevo γ ν 1) ∧
    (∃ p : ℝ, Maximizes γ ν p ∧
      ∀ n : ℕ, 1 ≤ n → holevo γ ν n = (n : ℝ) / Real.log 2 * objective γ ν p) ∧
    capacity γ ν = holevo γ ν 1 ∧
    (∀ p : ℝ, Maximizes γ ν p → ∀ n : ℕ, 1 ≤ n →
      (∀ s : Basis n, IsState (phaseState p s)) ∧
      holevo γ ν n = phaseValue γ ν p n)
```

Proved in [lean/OAI/InformationTheory/AmplitudeDamping/Main.lean, line 38](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/InformationTheory/AmplitudeDamping/Main.lean#L38).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/276.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/276.md)
