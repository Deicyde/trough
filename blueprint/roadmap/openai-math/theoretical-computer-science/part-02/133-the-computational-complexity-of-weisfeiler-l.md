---
declaration: section
origin: cited
lean: OAI.ParityWL.parity_reduction, OAI.WLIdentification.main, OAI.WLTime.unconditional_time_lower_bound, OAI.VariableWL.main
statement: formalized
proof: formalized
---

# 133. The computational complexity of Weisfeiler–Leman refinement

4 manuscripts and 4 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves unconditional $n^{\Omega(k)}$ deterministic time lower bounds for joint and separate *k*-dimensional Weisfeiler–Leman equivalence, for sufficiently large fixed *k* in the specified sequential adjacency-matrix models. With dimension as input, joint equivalence is EXPTIME-complete even on subcubic graphs; deciding whether refinement identifies a graph is also EXPTIME-complete.

## Parity lifts and bounded-treewidth witnesses for Weisfeiler–Leman equivalence

For *k* ≥ 4, we construct two uncolored graphs that are *k*-dimensional Weisfeiler–Leman equivalent exactly when a prescribed finite-domain choice system has no compatible choice. The system has $k+1$ domains for joint refinement and *k* for separate-coordinate refinement. A successful choice is detected after two joint rounds or one separate round. Applied to sparse satisfiability, the reduction gives fixed-dimension $n^{\Omega(k)}$ time exclusions under positive-rate ETH, even for deciding equality of these early histograms.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The complexity of identifying a graph by Weisfeiler–Leman refinement

We prove that deciding whether Weisfeiler–Leman refinement of an input dimension identifies a given graph is EXPTIME-complete. The input is a nonempty finite simple uncolored graph in adjacency-matrix form and a positive binary-encoded dimension. Identification quantifies over every comparison graph.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-complexity-of-identifying-a-graph-by-Weisfeiler-Leman-refinement-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## Unconditional time lower bounds for Weisfeiler–Leman equivalence

For every sufficiently large fixed *k*, deciding whether two *n*-vertex graphs are *k*-Weisfeiler–Leman equivalent requires $n^{\Omega(k)}$ deterministic sequential time in the worst case. The bound holds at every sufficiently large graph order, even for simple connected uncolored graphs of diameter at most two, without a complexity assumption. Inputs are explicit adjacency matrices; the models are multitape Turing machines and sequential logarithmic-word RAMs with fixed polynomial-bit-time instructions. Both joint and separate replacement conventions are covered.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## Variable-dimension Weisfeiler–Leman equivalence on general and subcubic graphs

Deciding joint-update *k*-dimensional Weisfeiler–Leman equivalence is $\mathsf{EXPTIME}$-complete when the two graphs are given by explicit adjacency matrices and *k* ≥ 2 is encoded in binary. The result holds even for connected simple uncolored graphs of equal positive order and maximum degree at most three.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization gives the paper's parity-lift graph construction for every Weisfeiler–Leman dimension $k\ge4$, under both joint and separate conventions. From a finite choice system it constructs two equal-size uncolored graphs that are Weisfeiler–Leman equivalent exactly when the system has no successful compatible choice. The same equivalence holds for the pure variant.

A successful choice is detected by the specified early round: round two in the joint convention and round one in the separate convention. The graph-size bound is linear in the choice-system size with a factor depending on $k$. The paper's conditional running-time exclusions are outside these selected construction statements.

The formalization proves that deciding whether Weisfeiler–Leman refinement of a supplied dimension identifies a graph is EXPTIME-complete under polynomial-time many-one reductions. The input is a nonempty finite simple uncolored graph encoded by its adjacency matrix together with a positive binary-encoded dimension. Identification quantifies over every comparison graph, and the statement includes both the exponential-time upper bound and hardness.

The formalization proves an unconditional deterministic time lower bound for deciding $k$-dimensional Weisfeiler–Leman equivalence. For every sufficiently large fixed $k$, every deciding algorithm in the stated multitape Turing-machine or sequential logarithmic-word RAM model requires at least $n^{ck}$ worst-case time for all sufficiently large graph orders $n$, for one absolute $c>0$.

The bound covers both joint and separate replacement conventions and remains valid for explicit adjacency-matrix inputs restricted to simple connected uncolored graphs of diameter at most two.

The formalization proves EXPTIME-completeness of deciding joint-update $k$-dimensional Weisfeiler–Leman equivalence when $k\ge2$ is part of the input in binary and the graphs are encoded by explicit adjacency matrices. It proves both the general result and the restriction to connected simple uncolored graphs of equal positive order and maximum degree at most three. Completeness uses polynomial-time many-one reductions.

## Lean: Parity-lift characterization of Weisfeiler–Leman equivalence

Stated in [ParityLifts.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ParityLifts.lean).

```lean
theorem parity_reduction : ParityReductionStatement
```

Proved in [lean/OAI/Combinatorics/ParityLifts/Main.lean, line 103](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/ParityLifts/Main.lean#L103).

## Lean: EXPTIME-completeness of Weisfeiler–Leman graph identification

Stated in [WLIdentification.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/WLIdentification.lean).

```lean
theorem main : EXPTIMEComplete dimensionLanguage
```

Proved in [lean/OAI/Computability/WLIdentification/Main.lean, line 7](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/WLIdentification/Main.lean#L7).

## Lean: Unconditional sequential time lower bounds for Weisfeiler–Leman equivalence

Stated in [WeisfeilerLeman.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/WeisfeilerLeman.lean).

```lean
theorem WLTime.unconditional_time_lower_bound : WLTime.MainClaim
```

Proved in [lean/OAI/Computability/WeisfeilerLeman/Main.lean, line 64](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/WeisfeilerLeman/Main.lean#L64).

## Lean: EXPTIME-completeness of variable-dimension Weisfeiler–Leman equivalence

Stated in [VariableWL.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/VariableWL.lean).

```lean
theorem main : EXPTIMEComplete WL ∧ EXPTIMEComplete SubWL
```

Proved in [lean/OAI/Combinatorics/VariableWL/Completeness.lean, line 315](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/VariableWL/Completeness.lean#L315).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/133.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/133.md)
