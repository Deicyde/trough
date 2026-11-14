---
declaration: section
origin: cited
lean: OAI.Problem315.switch_chain_main, OAI.Problem315.switch_chain_tv_bound, OAI.Problem315.switch_connectivity
statement: formalized
proof: formalized
---

# 131. Rapid mixing of graph switches for every degree sequence

1 manuscript and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the simple-undirected Kannan–Tetali–Vempala conjecture: the lazy edge-switch chain mixes in $O(n^8)$ time for every graphical labeled degree sequence. The same degree-constrained graphs can also be sampled exactly uniformly by an almost-surely terminating algorithm with expected polynomial bit running time.

## Polynomial mixing of the switch chain for every graphical degree sequence

We prove the simple-undirected form of the Kannan–Tetali–Vempala conjecture: the switch chain on simple undirected graphs mixes in polynomial time for every graphical degree sequence. For a lazy chain that proposes switches uniformly on four vertices, the total-variation mixing time at distance 1/4 is at most $2n^8$. We also give an exactly uniform sampler for every graphical labeled degree vector. It uses unbiased random bits, terminates almost surely, and has expected polynomial bit running time.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Polynomial-Mixing-of-the-Switch-Chain-for-Every-Graphical-Degree-Sequence-September-25-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The Kannan–Tetali–Vempala conjecture asks for polynomial mixing of the switch chain for every graphical degree sequence. The formalization proves the simple undirected case: for $n\ge4$, the lazy chain that proposes switches on four vertices has total-variation mixing time at distance $1/4$ at most $2n^8$. It also proves switch connectivity, the stated exponential total-variation bound, and a spectral gap of at least $1/(24n^2\binom n4)$ when more than one graph realizes the degree sequence.

The paper's exactly uniform sampling algorithm is outside these selected chain estimates.

## Lean: Polynomial mixing and connectivity for every graphical degree sequence

```lean
theorem switch_chain_main :
    ∀ (n : Nat) (d : Fin n → Nat), 4 ≤ n → (∀ v, d v ≤ n - 1) → Graphical n d → ((∃ h : (∃ t : Nat, MixedAt n d t), mixingTime n d h ≤ 2 * n ^ 8) ∧ (stateCount n d = 1 → (MixedAt n d 0 ∧ ∀ h : (∃ t : Nat, MixedAt n d t), mixingTime n d h = 0)) ∧ (1 < stateCount n d → hasSpectralGapAtLeast n d ((1 : ℝ) / (24 * (n : ℝ) ^ 2 * (Nat.choose n 4 : ℝ)))))
```

Stated in [SwitchChain.lean, line 155](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SwitchChain.lean#L155). Proved in [lean/OAI/Probability/SwitchChain/Main.lean, line 18](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/SwitchChain/Main.lean#L18).

```lean
theorem switch_chain_tv_bound :
    ∀ (n : Nat) (d : Fin n → Nat), 4 ≤ n → (∀ v, d v ≤ n - 1) → Graphical n d → 1 < stateCount n d → ∀ (t : Nat) (G : GraphState n d), tvDistanceFrom n d t G ≤ Real.sqrt (stateCount n d : ℝ) / 2 * Real.exp (- (t : ℝ) / (24 * (n : ℝ) ^ 2 * (Nat.choose n 4 : ℝ)))
```

Stated in [SwitchChain.lean, line 159](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SwitchChain.lean#L159). Proved in [lean/OAI/Probability/SwitchChain/Main.lean, line 30](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/SwitchChain/Main.lean#L30).

```lean
theorem switch_connectivity :
    ∀ (n : Nat) (d : Fin n → Nat), 4 ≤ n → (∀ v, d v ≤ n - 1) → Graphical n d → ∀ G H : GraphState n d, Relation.ReflTransGen (SwitchStep n d) G H
```

Stated in [SwitchChain.lean, line 163](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SwitchChain.lean#L163). Proved in [lean/OAI/Probability/SwitchChain/Main.lean, line 36](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/SwitchChain/Main.lean#L36).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/131.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/131.md)
