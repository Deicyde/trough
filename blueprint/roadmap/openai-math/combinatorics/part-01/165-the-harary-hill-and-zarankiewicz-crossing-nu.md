---
declaration: section
origin: cited
lean: OAI.Paper170.complete_graph_crossing_number, OAI.Zarankiewicz.mainTarget_proof
statement: formalized
proof: formalized
---

# 165. The Harary–Hill and Zarankiewicz crossing-number formulas

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the Harary–Hill conjecture and Turán's brickyard problem in the Zarankiewicz formulation, determining the crossing numbers of every complete and complete bipartite graph. The result proves the optimality of the classical drawings among all plane drawings with continuous edge arcs.

## The crossing number of complete graphs

We prove the Harary–Hill conjecture: for every positive integer *n*, the ordinary crossing number of the complete graph $K_{n}$ is

$\displaystyle \frac14\left\lfloor\frac n2\right\rfloor \left\lfloor\frac{n-1}{2}\right\rfloor \left\lfloor\frac{n-2}{2}\right\rfloor \left\lfloor\frac{n-3}{2}\right\rfloor.$

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-crossing-number-of-complete-graphs-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The crossing number of complete bipartite graphs

We prove the Zarankiewicz crossing-number conjecture, resolving Turán's brickyard problem. For all positive integers *m*, *n*, the ordinary crossing number of the complete bipartite graph $K_{m,n}$ is

$\displaystyle \left\lfloor\frac m2\right\rfloor \left\lfloor\frac{m-1}{2}\right\rfloor \left\lfloor\frac n2\right\rfloor \left\lfloor\frac{n-1}{2}\right\rfloor.$

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-crossing-number-of-complete-bipartite-graphs-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result proves Hill's proposed formula for the crossing number of the complete graph: for every $n\ge3$, $\mathrm{cr}(K_n)=\frac14\lfloor n/2\rfloor\lfloor(n-1)/2\rfloor\lfloor(n-2)/2\rfloor\lfloor(n-3)/2\rfloor$. It proves the lower bound and constructs a matching two-page drawing. Crossings are spatial points, so repeated crossings of one edge pair count separately.

Zarankiewicz's crossing-number conjecture predicts $\mathrm{cr}(K_{m,n})=\lfloor m/2\rfloor\lfloor(m-1)/2\rfloor\lfloor n/2\rfloor\lfloor(n-1)/2\rfloor$. The formalized result proves this equality for every positive $m,n$ and constructs a drawing attaining it. Crossings are counted as spatial points for continuous simple edge paths, including repeated crossings between the same pair of edges.

## Lean: Crossing number of complete graphs

Stated in [CompleteCrossing.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CompleteCrossing.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem complete_graph_crossing_number (order : ℕ) (at_least_three : 3 ≤ order) :
    ordinaryCrossingNumber (completeGraph order) = hill order
```

Proved in [lean/OAI/Combinatorics/CompleteCrossing/Main.lean, line 76](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/CompleteCrossing/Main.lean#L76).

## Lean: Crossing number of complete bipartite graphs

Stated in [BipartiteCrossing.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BipartiteCrossing.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem mainTarget_proof : MainTarget
```

Proved in [lean/OAI/Combinatorics/Crossing/Main.lean, line 8](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/Crossing/Main.lean#L8).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/165.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/165.md)
