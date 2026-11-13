---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.RandomSubsetSumsBalancedErdosProblem1179Wanted.subsetSumCount, MathlibExt.Combinatorics.RandomSubsetSumsBalancedErdosProblem1179Wanted.IsBalanced, MathlibExt.Combinatorics.RandomSubsetSumsBalancedErdosProblem1179Wanted.balancedProbability, MathlibExt.Combinatorics.RandomSubsetSumsBalancedErdosProblem1179Wanted.balancedSubsetSumsThresholdLogTwo, MathlibExt.Combinatorics.RandomSubsetSumsBalancedErdosProblem1179Wanted.balancedSubsetSumsThresholdLogTwo_holds
statement: formalized
---

# Balanced subset sums in finite abelian groups

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/balanced-subset-sums-in-finite-abelian-groups/index.html).

## Number of subsets with a given sum

For a finite subset $A$ of an abelian group $G$ and an
element $g \in G$, $F_A(g)$ is the number of subsets $S \subseteq A$, the empty set included, whose
elements sum to $g$, that is, with $\sum_{x \in S} x = g$.

Formalized by `MathlibExt.Combinatorics.RandomSubsetSumsBalancedErdosProblem1179Wanted.subsetSumCount`, a definition declared in [WantedExt/Combinatorics/RandomSubsetSumsBalancedErdosProblem1179Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/RandomSubsetSumsBalancedErdosProblem1179Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/balanced-subset-sums-in-finite-abelian-groups/index.html#subset-sum-count).

## $\varepsilon$-balanced subsets of a finite abelian group

Let $G$ be a finite abelian group
with $N = |G|$ elements and let $\varepsilon$ be a real number. A subset $A \subseteq G$ is
$\varepsilon$-balanced when, for every $g \in G$, the number $F_A(g)$ of subsets of $A$ whose
elements sum to $g$ satisfies
$\left| F_A(g) - 2^{|A|}/N \right| \le \varepsilon \cdot 2^{|A|}/N$.

Formalized by `MathlibExt.Combinatorics.RandomSubsetSumsBalancedErdosProblem1179Wanted.IsBalanced`, a definition declared in [WantedExt/Combinatorics/RandomSubsetSumsBalancedErdosProblem1179Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/RandomSubsetSumsBalancedErdosProblem1179Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/balanced-subset-sums-in-finite-abelian-groups/index.html#is-balanced).

## Probability that a random subset is balanced

For a finite abelian group $G$, a real
number $\varepsilon$ and a natural number $k$, this is the number of $\varepsilon$-balanced
$k$-element subsets of $G$ divided by the number of all $k$-element subsets of $G$, that is, the
probability that a uniformly random $k$-element subset of $G$ is $\varepsilon$-balanced. When
$k > |G|$ there are no $k$-element subsets and the value is $0$.

Formalized by `MathlibExt.Combinatorics.RandomSubsetSumsBalancedErdosProblem1179Wanted.balancedProbability`, a definition declared in [WantedExt/Combinatorics/RandomSubsetSumsBalancedErdosProblem1179Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/RandomSubsetSumsBalancedErdosProblem1179Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/balanced-subset-sums-in-finite-abelian-groups/index.html#balanced-probability).

## Erdős Problem 1179 (balanced subset sums of random subsets)

The statement of Erdős
Problem 1179 is the proposition that, for every real $\varepsilon$ with $0 < \varepsilon < 1$, the
following two bounds hold. Upper bound: there is a function $k : \mathbb{N} \to \mathbb{N}$ with
$k(N) / \log_2 N \to 1$ as $N \to \infty$ such that, for every sequence $(G_i)_{i \in \mathbb{N}}$
of finite abelian groups with $|G_i| \to \infty$, the probability that a uniformly random
$k(|G_i|)$-element subset of $G_i$ is $\varepsilon$-balanced tends to $1$ as $i \to \infty$. Lower
bound: for every finite abelian group $G$, every $\varepsilon$-balanced subset $A \subseteq G$
satisfies $|G| \le 2^{|A|}$.

Formalized by `MathlibExt.Combinatorics.RandomSubsetSumsBalancedErdosProblem1179Wanted.balancedSubsetSumsThresholdLogTwo`, a definition declared in [WantedExt/Combinatorics/RandomSubsetSumsBalancedErdosProblem1179Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/RandomSubsetSumsBalancedErdosProblem1179Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/balanced-subset-sums-in-finite-abelian-groups/index.html#balanced-subset-sums-threshold-log-two).

## Erdős Problem 1179 holds

For every real $\varepsilon$ with $0 < \varepsilon < 1$, the
following two bounds hold. Upper bound: there is a function $k : \mathbb{N} \to \mathbb{N}$ with
$k(N) / \log_2 N \to 1$ as $N \to \infty$ such that, for every sequence $(G_i)_{i \in \mathbb{N}}$
of finite abelian groups with $|G_i| \to \infty$, the probability that a uniformly random
$k(|G_i|)$-element subset of $G_i$ is $\varepsilon$-balanced tends to $1$ as $i \to \infty$. Lower
bound: for every finite abelian group $G$, every $\varepsilon$-balanced subset $A \subseteq G$
satisfies $|G| \le 2^{|A|}$.

Writing $g_\varepsilon(N)$ for the least size for which a uniformly random subset of a group of
order $N$ is $\varepsilon$-balanced with probability tending to $1$, Erdős and Hall proved
$g_\varepsilon(N) \le (1 + O_\varepsilon(\log \log \log N / \log \log N)) \log_2 N$, improving the
bound $(2 + o(1)) \log_2 N + O_\varepsilon(1)$ of Erdős and Rényi; the lower bound holds because
an $\varepsilon$-balanced set with $\varepsilon < 1$ has every element of $G$ as a subset sum.
erdosproblems.com/1179 lists the problem as proved.

## Sources

- T. F. Bloom, Erdős Problems, Problem #1179, https://www.erdosproblems.com/1179 (status PROVED); resolution: P. Erdős and R. R. Hall, Probabilistic methods in group theory. II, Houston J. Math. 2 (1976), 173-180, erdosproblems.com/1179: g_ε(N) ≤ (1 + O_ε(log log log N / log log N)) log₂ N for all 0 < ε < 1.

Stated but not proved: `MathlibExt.Combinatorics.RandomSubsetSumsBalancedErdosProblem1179Wanted.balancedSubsetSumsThresholdLogTwo_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/RandomSubsetSumsBalancedErdosProblem1179Wanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/RandomSubsetSumsBalancedErdosProblem1179Wanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/balanced-subset-sums-in-finite-abelian-groups/index.html#balanced-subset-sums-threshold-log-two-h).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Balanced subset sums in finite abelian groups](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/balanced-subset-sums-in-finite-abelian-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/balanced-subset-sums-in-finite-abelian-groups)
