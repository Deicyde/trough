---
declaration: section
origin: cited
lean: MathlibExt.GraphTheory.AMR11Problem33Wanted.AMR11Q33.RegularCayleyGraph, MathlibExt.GraphTheory.AMR11Problem33Wanted.AMR11Q33.firstReturnProb, MathlibExt.GraphTheory.AMR11Problem33Wanted.AMR11Q33.returnProb, MathlibExt.GraphTheory.AMR11Problem33Wanted.AMR11Q33.returnProbUniformGap, MathlibExt.GraphTheory.AMR11Problem33Wanted.returnProbUniformGap_holds
statement: formalized
---

# Return probabilities of random walks on Cayley graphs

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-walks/return-probabilities-of-random-walks-on-cayley-g/index.html).

## AMR11 Q33

## Regular Cayley graph

For a group $G$ and a natural number $k$, the data of a $k$-regular
Cayley graph on $G$ is a finite set $S \subseteq G$ of generators such that $S$ is closed under
inverses ($s \in S$ implies $s^{-1} \in S$), the identity $1$ does not belong to $S$, every
element of $G$ is the product of a finite (possibly empty) list of elements of $S$, and $S$ has
exactly $k$ elements.

Formalized by `MathlibExt.GraphTheory.AMR11Problem33Wanted.AMR11Q33.RegularCayleyGraph`, a structure declared in [WantedExt/GraphTheory/AMR11Problem33Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/AMR11Problem33Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-walks/return-probabilities-of-random-walks-on-cayley-g/index.html#regular-cayley-graph).

## First-return probability

Let $\Gamma$ be a $k$-regular Cayley graph on a group $G$ with
generating set $S$. For $n \ge 1$, the first-return probability of $\Gamma$ at time $n$ is the
real number obtained by dividing by $k^n$ the number of words $(s_1, \dots, s_n) \in S^n$ with
$s_1 s_2 \cdots s_n = 1$ and $s_1 \cdots s_m \ne 1$ for every $0 < m < n$; at time $n = 0$ it
is $0$.

Since $S$ has $k$ elements, this is the probability that the walk $1, s_1, s_1 s_2, \dots$ with
independent uniform steps in $S$ is back at $1$ for the first time at step $n$.

Formalized by `MathlibExt.GraphTheory.AMR11Problem33Wanted.AMR11Q33.firstReturnProb`, a definition declared in [WantedExt/GraphTheory/AMR11Problem33Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/AMR11Problem33Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-walks/return-probabilities-of-random-walks-on-cayley-g/index.html#first-return-prob).

## Return probability

The return probability of a $k$-regular Cayley graph $\Gamma$ is the
sum $\sum_{n \ge 0} p_n$, where $p_n$ is the first-return probability of $\Gamma$ at time $n$.

It is the probability that simple random walk on $\Gamma$ started at the identity ever returns
to the identity.

Formalized by `MathlibExt.GraphTheory.AMR11Problem33Wanted.AMR11Q33.returnProb`, a definition declared in [WantedExt/GraphTheory/AMR11Problem33Wanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/AMR11Problem33Wanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-walks/return-probabilities-of-random-walks-on-cayley-g/index.html#return-prob).

## Uniform return-probability gap

The statement that for every natural number $k > 1$ there
is a real number $C < 1$ such that for every group $G$ and every $k$-regular Cayley graph
$\Gamma$ on $G$, if the return probability of $\Gamma$ is less than $1$ (that is, $\Gamma$ is
transient), then it is at most $C$.

Formalized by `MathlibExt.GraphTheory.AMR11Problem33Wanted.AMR11Q33.returnProbUniformGap`, a definition declared in [WantedExt/GraphTheory/AMR11Problem33Wanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/AMR11Problem33Wanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-walks/return-probabilities-of-random-walks-on-cayley-g/index.html#return-prob-uniform-gap).

## Uniform return-probability gap for transient Cayley graphs

For every natural number
$k > 1$ there is a real number $C < 1$ such that for every group $G$ and every $k$-regular Cayley
graph $\Gamma$ on $G$ whose return probability is less than $1$, the return probability of
$\Gamma$ is at most $C$.

This follows from Tessera and Tointon, Corollary 1.3: there is a universal $c > 0$ such that
simple random walk on every connected, locally finite, vertex-transitive graph is recurrent or
escapes with probability at least $c$, so $C = 1 - c$ works for every $k$.

## Sources

- Romain Tessera and Matthew Tointon, Sharp relations between volume growth, isoperimetry and escape probability in vertex-transitive graphs, arXiv preprint (2020, v2 2024), arXiv:2001.01467, https://arxiv.org/abs/2001.01467.

Stated but not proved: `MathlibExt.GraphTheory.AMR11Problem33Wanted.returnProbUniformGap_holds` is written with `theorem_wanted` in [WantedExt/GraphTheory/AMR11Problem33Wanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/AMR11Problem33Wanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-walks/return-probabilities-of-random-walks-on-cayley-g/index.html#return-prob-uniform-gap-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Return probabilities of random walks on Cayley graphs](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-walks/return-probabilities-of-random-walks-on-cayley-g/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/random-walks/return-probabilities-of-random-walks-on-cayley-g)
