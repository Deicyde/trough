---
declaration: section
origin: cited
lean: OAI.Problem313.sharp_threshold_width
statement: formalized
proof: formalized
---

# 186. Uniform influence and sharp thresholds for graph and hypergraph properties

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the Friedgut–Kalai threshold-width conjectures for graphs and fixed-uniformity hypergraphs. For fixed $0\lt \varepsilon\lt 1/2$, every nontrivial increasing relabeling-invariant property crosses from probability *ε* to $1-\varepsilon$ within width $O((\log n)^{-2})$ for graphs and $O_r((\log n)^{-r/(r-1)})$ for *r*-uniform hypergraphs, *r* ≥ 3. The hypergraph influence bound also applies to nonmonotone properties.

## A uniform influence bound for hypergraph properties

For every fixed integer *r* ≥ 3, we prove that every relabeling-invariant Boolean property of simple *r*-uniform hypergraphs on *n* vertices satisfies $\mathop{\mathrm{Var}}\nolimits _p(f)\le C_r I_p(f)/(\log n)^{r/(r-1)}$. The constant depends only on *r*, and the bound holds uniformly for all $0\lt p\lt 1$ without a monotonicity assumption. For increasing properties, it gives the corresponding threshold-width bound with exponent $r/(r-1)$, proving the hypergraph threshold-width conjecture of Friedgut and Kalai.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026/hypergraph-influences.pdf).

## A Sharp Threshold Bound for Monotone Graph Properties

We prove the Friedgut–Kalai sharp-threshold conjecture. For every integer *n* ≥ 2, every nontrivial increasing family of graphs on *n* vertices invariant under all vertex permutations, and every $0\lt \varepsilon\lt 1/2$, the edge probabilities at which its probability equals *ε* and $1-\varepsilon$ differ by at most $C\log(1/(2\varepsilon))/(\log n)^2$, for a universal constant *C*.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The Friedgut–Kalai sharp-threshold conjecture concerns how quickly a nontrivial increasing graph property appears in the independent-edge random graph. For every $n\ge2$, every such property invariant under vertex relabeling, and $0<\varepsilon<1/2$, the formalization proves that the edge-probability interval between probabilities $\varepsilon$ and $1-\varepsilon$ has width at most $2^{19}\log(1/(2\varepsilon))/(\log n)^2$. The constant is uniform over the graph property, $n$, and $\varepsilon$.

## Lean: Sharp threshold width for monotone graph properties

```lean
theorem sharp_threshold_width :
    ∀ (n : ℕ) (f : GraphConfig n → Bool) (ε : ℝ),
      2 ≤ n → VertexInvariant f → IncreasingGraphProperty f →
      NontrivialGraphProperty f → 0 < ε → ε < (1 / 2 : ℝ) →
      graphQuantile (1 - ε) f - graphQuantile ε f ≤
        ((2 : ℝ) ^ 19 / (Real.log (n : ℝ)) ^ 2) * Real.log (1 / (2 * ε))
```

Stated in [SharpThreshold.lean, line 51](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SharpThreshold.lean#L51). Proved in [lean/OAI/Combinatorics/SharpThreshold/Main.lean, line 28](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/SharpThreshold/Main.lean#L28).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/186.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/186.md)
