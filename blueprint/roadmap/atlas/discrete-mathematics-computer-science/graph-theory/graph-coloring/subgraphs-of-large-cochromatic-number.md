---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ErdosProblem760Wanted.conjecture, MathlibExt.Combinatorics.ErdosProblem760Wanted.conjecture_holds
statement: formalized
---

# Subgraphs of large cochromatic number

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/subgraphs-of-large-cochromatic-number/index.html).

## Erdős Problem 760: subgraphs of large cochromatic number

The proposition asserts two
statements. First, there is a real number $c > 0$ such that for every simple graph $G$ on a finite
vertex set with chromatic number $m$ there are a subgraph $H$ of $G$ and a natural number $k$ with
$k \ge c\,m / \log m$ such that the cochromatic number of $H$ is at least $k$. Second, there is a
real number $c > 0$ with the same property for the bound $k \ge c\sqrt{m / \log m}$.

Here $\log$ is the natural logarithm, with the conventions $\log 0 = 0$ and $x / 0 = 0$, so both
bounds are $0$ when $m \le 1$. The second statement is the Erdős–Gimbel form.

Formalized by `MathlibExt.Combinatorics.ErdosProblem760Wanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ErdosProblem760Wanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosProblem760Wanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/subgraphs-of-large-cochromatic-number/index.html#conjecture).

## Alon–Krivelevich–Sudakov theorem on subgraphs of large cochromatic number

There is a real
number $c > 0$ such that for every simple graph $G$ on a finite vertex set with chromatic number
$m$ there are a subgraph $H$ of $G$ and a natural number $k$ with $k \ge c\,m / \log m$ such that
the cochromatic number of $H$ is at least $k$. Moreover, there is a real number $c > 0$ with the
same property for the bound $k \ge c\sqrt{m / \log m}$.

Here $\log$ is the natural logarithm, with the conventions $\log 0 = 0$ and $x / 0 = 0$, so both
bounds are $0$ when $m \le 1$. This answers Erdős Problem 760 affirmatively.

## Sources

- plby/lean-proofs (following Alon, Krivelevich and Sudakov, Subgraphs with a large cochromatic number, 1997), https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.29.1/ErdosProblems/Erdos760.lean#L1306.

Stated but not proved: `MathlibExt.Combinatorics.ErdosProblem760Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosProblem760Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosProblem760Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/subgraphs-of-large-cochromatic-number/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Subgraphs of large cochromatic number](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/subgraphs-of-large-cochromatic-number/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/graph-coloring/part-01/subgraphs-of-large-cochromatic-number)
