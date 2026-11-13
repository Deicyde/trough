---
declaration: section
origin: cited
lean: OAI.CliqueFreeLog.logarithmic_independence_bound
statement: formalized
proof: formalized
---

# 184. Correspondence coloring with a fixed forbidden subgraph

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the Alon–Krivelevich–Sudakov coloring conjecture in correspondence-coloring form: graphs avoiding any fixed subgraph *F* need $O_F(\Delta/\log\Delta)$ colors when their maximum degree Δ is sufficiently large. Also proves the Ajtai–Erdős–Komlós–Szemerédi independence conjecture: for fixed *r* ≥ 4, every *n*-vertex $K_{r}$-free graph of average degree *d* ≥ 2 has an independent set of size $\Omega_r(n\log d/d)$.

## Correspondence coloring graphs with a forbidden clique

For every fixed integer *r* ≥ 4, we prove that every $K_{r}$-free graph of sufficiently large maximum degree Δ has correspondence chromatic number $O_r(\Delta/\log\Delta)$. This resolves the Alon–Krivelevich–Sudakov coloring conjecture in the stronger correspondence-coloring form. The same bound, with a constant depending on *F*, holds when any fixed graph *F* is excluded as an ordinary subgraph. Ordinary and list coloring satisfy the same bounds.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026/correspondence-coloring-forbidden-clique.pdf).

## A logarithmic independence bound for clique-free graphs

For every fixed integer *r* ≥ 4, every $K_{r}$-free graph on *n* vertices with average degree *d* ≥ 2 has an independent set of size at least $c_r n\log d/d$, where $c_r\gt 0$ depends only on *r*. This proves the fixed-clique-size independence conjecture of Ajtai, Erdős, Komlós and Szemerédi.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Logarithmic-Independence-Bound-for-Clique-Free-Graphs-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result gives a logarithmic improvement in the independence number of clique-free graphs. For every fixed integer $r\ge4$, there is $c_r>0$ such that every finite $K_r$-free simple graph on $n$ vertices with average degree $d\ge2$ has an independent set of size at least $c_r n\log d/d$. The constant depends only on $r$.

## Lean: Logarithmic independence bound for clique-free graphs

```lean
theorem logarithmic_independence_bound (r : ℕ) (hr : 4 ≤ r) :
    ∃ c : ℝ, 0 < c ∧
      ∀ {V : Type} [Fintype V] (G : SimpleGraph V),
        G.CliqueFree r → 2 ≤ averageDegree G →
        c * (Fintype.card V : ℝ) * Real.log (averageDegree G) / averageDegree G ≤
          (G.indepNum : ℝ)
```

Stated in [CliqueFreeLog.lean, line 11](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CliqueFreeLog.lean#L11). Proved in [lean/OAI/Combinatorics/CliqueFree/Main.lean, line 22](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/CliqueFree/Main.lean#L22). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/184.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/184.md)
