---
declaration: section
origin: cited
lean: MetaMathlibExt.isolation_lemma, MathlibExt.Probability.Combinatorics.LovaszLocalLemma.lovasz_local_lemma_symmetric_finite
statement: formalized
proof: formalized
---

# Probabilistic combinatorics: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/index.html).

Probabilistic methods and random discrete structures outside random graphs: the Lovász local lemma, Littlewood–Offord and Tomaszewski anti-concentration for signed sums, concentration of subset sums, the isolation lemma, thresholds and expectation thresholds, random k-SAT thresholds, perfect matchings in random hypergraphs, the Chvátal–Sankoff constant for longest common subsequences, and moment-based counting bounds.

## Isolation lemma

Let $n \ge 1$ and let $\mathcal{F}$ be a nonempty family of subsets of
$\{0, 1, \dots, n - 1\}$. Assign each element $i$ a weight $w(i) \in \{1, 2, \dots, 2n\}$ and give
a set $S$ the weight $w(S) = \sum_{i \in S} w(i)$. Then, among all $(2n)^n$ weight functions $w$,
the fraction for which exactly one member of $\mathcal{F}$ has minimum weight is at least $1/2$.

Equivalently, if the weights are chosen independently and uniformly at random, the
minimum-weight member of $\mathcal{F}$ is unique with probability at least $1/2$.

## Sources

- https://en.wikipedia.org/wiki/Isolation_lemma

Formalized by `MetaMathlibExt.isolation_lemma`, a theorem declared in [MathlibExt/Combinatorics/IsolationLemma.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsolationLemma.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/index.html#isolation-lemma).

## Symmetric Lovász Local Lemma

Let $\Omega$ be a finite set with a probability mass function
$P$, that is, $P(\omega) \ge 0$ for every $\omega \in \Omega$ and
$\sum_{\omega \in \Omega} P(\omega) = 1$, and write $\Pr[E] = \sum_{\omega \in E} P(\omega)$ for
$E \subseteq \Omega$. Let $(A_i)_{i \in I}$ be a family of events indexed by a finite set $I$,
let $G$ be a simple graph on $I$ whose maximum degree is at most a natural number $d$, and let
$p \ge 0$ be a real number. Suppose that $\Pr[A_i] \le p$ for every $i \in I$, and that for every
$i \in I$ and every set $S \subseteq I$ containing neither $i$ nor any neighbour of $i$ in $G$,
$\Pr[A_i \cap \bigcap_{j \in S} A_j] = \Pr[A_i] \cdot \Pr[\bigcap_{j \in S} A_j]$.
If $e \cdot p \cdot (d + 1) \le 1$, then $\Pr[\bigcap_{i \in I} (\Omega \setminus A_i)] > 0$,
that is, with positive probability none of the events $A_i$ occurs.

The independence hypothesis, taken over all such $S$ (including $S = \emptyset$), says that
each $A_i$ is mutually independent of the family of events $A_j$ with $j$ neither $i$ nor a
neighbour of $i$.

## Sources

- N. Alon and J. H. Spencer, The Probabilistic Method, third edition, Wiley, 2008, Corollary 5.1.2, for the criterion $e p (d + 1) \le 1$; the original local lemma of P. Erdős and L. Lovász (1975) gives the earlier weaker criterion $4 p d \le 1$.

Formalized by `MathlibExt.Probability.Combinatorics.LovaszLocalLemma.lovasz_local_lemma_symmetric_finite`, a theorem declared in [MathlibExt/Probability/Combinatorics/LovaszLocalLemma.lean, line 805](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Combinatorics/LovaszLocalLemma.lean#L805). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/index.html#lovasz-local-lemma-symmetric-finite).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Probabilistic combinatorics](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/probabilistic-combinatorics)
