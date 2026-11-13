---
declaration: section
origin: cited
lean: OAI.UniqueGamesTheorem.theorem11, OAI.OptimalMaxCut.main, OAI.VertexCover.explicit_cover_gap, OAI.VertexCover.every_fixed_factor_below_two, OAI.MinUncut.main, OAI.DirectedFeedback.main
statement: formalized
proof: formalized
---

# 102. The Unique Games Conjecture and optimal approximation thresholds

5 manuscripts and 6 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves Khot's Unique Games Conjecture. Independent direct reductions also establish NP-hardness, on unweighted graphs, of approximation beyond the Goemans–Williamson ratio for Max-Cut, below factor two for Vertex Cover, and within any fixed constant factor for Min-UnCut and directed feedback vertex set. These direct proofs use established PCP and Label Cover hardness results.

## The Unique Games Theorem

We prove the Unique Games Conjecture. For every fixed $\varepsilon,\delta\in(0,1/2)$, we give a deterministic polynomial-time reduction from 3SAT to Unique Games over a fixed finite alphabet, with completeness at least $1-\varepsilon$ and soundness at most *δ*.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Unique-Games-Theorem-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## A Direct Proof of Optimal Max-Cut Hardness

We prove that approximating Max-Cut on simple unweighted graphs within any fixed factor greater than the Goemans–Williamson constant is NP-hard.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Direct-Proof-of-Optimal-Max-Cut-Hardness-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Factor-Two Hardness Threshold for Vertex Cover

We prove that minimum Vertex Cover is NP-hard to approximate within every fixed factor below two, even on simple unweighted graphs.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Factor-Two-Hardness-Threshold-for-Vertex-Cover-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## Constant-factor hardness of Min-UnCut

For every fixed *C* > 1, approximating Min-UnCut within factor *C* is NP-hard, even on simple undirected unweighted graphs.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Constant-factor-hardness-of-Min-UnCut-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## Constant-factor hardness of directed feedback vertex set

Approximating minimum directed feedback vertex set within any fixed constant factor is NP-hard, even on unweighted digraphs.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Constant-factor-hardness-of-directed-feedback-vertex-set-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The Unique Games conjecture asks for hardness of distinguishing nearly satisfiable unique games from games of very small value. The formalized result gives, for every fixed $0<\varepsilon,\delta<1/2$, a deterministic polynomial-time reduction from binary 3SAT to nonempty unweighted simple bipartite unique games. Satisfiable inputs have value at least $1-\varepsilon$ and unsatisfiable inputs have value at most $\delta$. The alphabet is a fixed $\mathbb F_2^s$ depending only on the errors, and every constraint is a translation.

The formalized result establishes hardness of approximating Max-Cut beyond the Goemans–Williamson constant $\alpha_{\mathrm{GW}}$. For every fixed $\alpha_{\mathrm{GW}}<\alpha\le1$, it gives a deterministic polynomial-time reduction from binary 3SAT to a strictly separated Max-Cut gap on finite simple unweighted graphs. The reduction includes the explicit positive integer scaling used in the gap statement.

The formalized result gives the factor-two hardness threshold for Vertex Cover. For each integer $m\ge4$, a polynomial-time reduction from binary 3SAT produces simple unweighted graphs with cover density below $1/2+1/m$ on satisfiable inputs and above $1-1/m$ on unsatisfiable inputs. Consequently, any polynomial-time approximation with a fixed factor $1\le\alpha<2$ would give a polynomial-time decision algorithm for 3SAT. No assumption that $P\ne NP$ is built into the statement.

Min-UnCut minimizes the number of edges left uncut by a bipartition. The formalization constructs a deterministic reduction from encoded $3$-SAT formulas to finite simple unweighted Min-UnCut instances with arbitrarily large fixed multiplicative gaps. For every integer $K\ge2$, satisfiable formulas give optimum at most the output threshold, while unsatisfiable formulas give optimum strictly greater than $K$ times that threshold. Runtime and output length are polynomial for each fixed $K$, establishing hardness for every fixed approximation factor greater than one.

A directed feedback vertex set meets every directed cycle. The formalization proves hardness of approximating the minimum such set within any fixed constant factor. For every real factor $A\ge1$ and every language in NP, it constructs a polynomial-time gap reduction to unweighted directed graphs with the stated completeness and soundness separation. Thus a fixed-factor polynomial-time approximation would imply a polynomial-time algorithm for every NP language.

## Lean: Unique Games gap reduction

```lean
theorem theorem11 (ε δ : ℝ)
    (hε : 0 < ε) (hεhalf : ε < 1 / 2)
    (hδ : 0 < δ) (hδhalf : δ < 1 / 2) :
    Nonempty (Explicit.MachineOutputContract.BinaryGapReduction ε δ)
```

Stated in [UniqueGamesTheorem.lean, line 231](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/UniqueGamesTheorem.lean#L231). Proved in [lean/OAI/Computability/UniqueGames/Theorem.lean, line 26](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/UniqueGames/Theorem.lean#L26). formalization.yaml lists it as one of the repository's main results.

## Lean: Optimal Max-Cut hardness gap

```lean
theorem OptimalMaxCut.main : OptimalMaxCut.MainStatement
```

Stated in [OptimalMaxCut.lean, line 153](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/OptimalMaxCut.lean#L153). Proved in [lean/OAI/Computability/MaxCut/Main.lean, line 53](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/MaxCut/Main.lean#L53). formalization.yaml lists it as one of the repository's main results.

## Lean: Vertex Cover gap and factor-two hardness

```lean
theorem explicit_cover_gap (m : ℕ) (hm : 4 ≤ m) : Nonempty (GapReduction m)
```

Stated in [VertexCover.lean, line 145](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/VertexCover.lean#L145). Proved in [lean/OAI/Computability/VertexCover/Main.lean, line 113](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/VertexCover/Main.lean#L113).

```lean
theorem every_fixed_factor_below_two (α : ℝ) (hα : 1 ≤ α) (hα2 : α < 2)
    (algorithm : Approximation α) : Nonempty ThreeSATDecision
```

Stated in [VertexCover.lean, line 148](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/VertexCover.lean#L148). Proved in [lean/OAI/Computability/VertexCover/Main.lean, line 115](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/VertexCover/Main.lean#L115). formalization.yaml lists it as one of the repository's main results.

## Lean: Arbitrary constant-factor hardness of Min-UnCut

```lean
theorem main : Nonempty Reduction
```

Stated in [MinUncut.lean, line 125](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MinUncut.lean#L125). Proved in [lean/OAI/Computability/MinUncut/Main.lean, line 106](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/MinUncut/Main.lean#L106).

## Lean: Constant-factor hardness of directed feedback vertex set

```lean
theorem DirectedFeedback.main : DirectedFeedback.MainStatement
```

Stated in [DirectedFeedback.lean, line 98](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DirectedFeedback.lean#L98). Proved in [lean/OAI/Computability/DirectedFeedback/Main.lean, line 1132](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/DirectedFeedback/Main.lean#L1132).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/102.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/102.md)
