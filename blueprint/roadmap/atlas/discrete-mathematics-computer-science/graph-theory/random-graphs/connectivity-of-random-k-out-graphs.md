---
declaration: section
origin: cited
lean: MathlibExt.Probability.ScottishBook38Wanted.KOutReachable, MathlibExt.Probability.ScottishBook38Wanted.KOutConnected, MathlibExt.Probability.ScottishBook38Wanted.KOutConnectedProb, MathlibExt.Probability.ScottishBook38Wanted.k_out_connectivity_threshold
statement: formalized
---

# Connectivity of random k-out graphs

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/connectivity-of-random-k-out-graphs/index.html).

## Reachability by a chain of friends

Let $c$ assign to each person $i$ among $N$ people a
set $c(i)$ of people, the friends of $i$. A person $b$ is reachable from a person $a$ if there are
$m \ge 0$ and people $p_0 = a, p_1, \dots, p_m = b$ such that for each $j < m$, $p_j$ is a friend
of $p_{j+1}$ or $p_{j+1}$ is a friend of $p_j$.

Formalized by `MathlibExt.Probability.ScottishBook38Wanted.KOutReachable`, a definition declared in [WantedExt/Probability/ScottishBook38Wanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ScottishBook38Wanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/connectivity-of-random-k-out-graphs/index.html#kout-reachable).

## Assignments that connect everyone

Let $c$ assign to each person $i$ among $N$ people a
set $c(i)$ of people, the friends of $i$. The assignment $c$ connects all $N$ people when, for
all people $a$ and $b$, there are $m \ge 0$ and people $p_0 = a, p_1, \dots, p_m = b$ such that
for each $j < m$, $p_j$ is a friend of $p_{j+1}$ or $p_{j+1}$ is a friend of $p_j$.

Formalized by `MathlibExt.Probability.ScottishBook38Wanted.KOutConnected`, a definition declared in [WantedExt/Probability/ScottishBook38Wanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ScottishBook38Wanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/connectivity-of-random-k-out-graphs/index.html#kout-connected).

## Probability that a random $k$-out assignment connects everyone

For natural numbers $k$
and $N$, $P_{kN}$ is the number of assignments that give each of $N$ people a set of exactly $k$
friends other than themselves and connect all $N$ people, divided by the number of all
assignments that give each person a set of exactly $k$ friends other than themselves. When there
is no such assignment, $P_{kN} = 0$.

Formalized by `MathlibExt.Probability.ScottishBook38Wanted.KOutConnectedProb`, a definition declared in [WantedExt/Probability/ScottishBook38Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ScottishBook38Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/connectivity-of-random-k-out-graphs/index.html#kout-connected-prob).

## Connectivity threshold for random $k$-out friendship graphs

For natural numbers $k$ and $N$,
let $P_{kN}$ be the proportion of the assignments giving each of $N$ people exactly $k$ friends
other than themselves that connect all $N$ people. Then $P_{kN} \to 1$ as $N \to \infty$ for
every $k \ge 2$, and $P_{1N} \to 0$ as $N \to \infty$.

Friendship need not be symmetric: two people are joined when either one chose the other, so a
chain of friends is a path in the underlying undirected graph. Ulam asked for $P_{kN}$ and for
its limit as $N \to \infty$, $0$ or $1$.

## Sources

- S. Ulam, Problem 38 of the Scottish Book; the symmetric case was solved by Erdős for `k ≥ 2`, and D. S. Jungreis gave a detailed general solution; see the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Probability.ScottishBook38Wanted.k_out_connectivity_threshold` is written with `theorem_wanted` in [WantedExt/Probability/ScottishBook38Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ScottishBook38Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/connectivity-of-random-k-out-graphs/index.html#k-out-connectivity-threshold).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Connectivity of random k-out graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/connectivity-of-random-k-out-graphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/random-graphs/connectivity-of-random-k-out-graphs)
