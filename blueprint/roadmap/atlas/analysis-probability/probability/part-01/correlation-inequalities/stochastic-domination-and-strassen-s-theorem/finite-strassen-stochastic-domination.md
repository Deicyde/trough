---
declaration: section
origin: cited
lean: MathlibExt.Probability.StrassenCouplingWanted.IsUpperSet, MathlibExt.Probability.StrassenCouplingWanted.forall_isUpperSet_sum_le_iff_exists_coupling, MathlibExt.Probability.StrassenCouplingWanted.strassen_coupling_finite_poset
statement: formalized
proof: formalized
---

# Finite Strassen stochastic domination

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/finite-strassen-stochastic-domination/index.html).

## Finite upper sets

A finite subset $U$ of a preordered set $\alpha$ is an upper set (is
upward closed) if for all $x, y \in \alpha$ with $x \in U$ and $x \le y$, also $y \in U$.

Formalized by `MathlibExt.Probability.StrassenCouplingWanted.IsUpperSet`, a definition declared in [MathlibExt/Probability/StrassenCoupling.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/StrassenCoupling.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/finite-strassen-stochastic-domination/index.html#is-upper-set).

## Strassen's theorem on a finite poset, equal-mass form

Let $\alpha$ be a finite partially
ordered set and let $p, q : \alpha \to \mathbb{R}$ be nonnegative functions with
$\sum_{x \in \alpha} p(x) = \sum_{x \in \alpha} q(x)$. Then
$\sum_{x \in U} p(x) \le \sum_{x \in U} q(x)$ for every upper set $U \subseteq \alpha$ if and only
if there is a function $\pi : \alpha \times \alpha \to \mathbb{R}$ such that $\pi(x, y) \ge 0$
for all $x, y \in \alpha$, $\sum_{y \in \alpha} \pi(x, y) = p(x)$ for every $x \in \alpha$,
$\sum_{x \in \alpha} \pi(x, y) = q(y)$ for every $y \in \alpha$, and $\pi(x, y) = 0$ whenever
$x \not\le y$.

Formalized by `MathlibExt.Probability.StrassenCouplingWanted.forall_isUpperSet_sum_le_iff_exists_coupling`, a theorem declared in [MathlibExt/Probability/StrassenCoupling.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/StrassenCoupling.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/finite-strassen-stochastic-domination/index.html#forall-is-upper-set-sum-le-iff-exists-co).

## Strassen's theorem on a finite poset

Let $\alpha$ be a finite partially ordered set and let
$p, q : \alpha \to \mathbb{R}$ be probability mass functions, that is, nonnegative functions with
$\sum_{x \in \alpha} p(x) = 1$ and $\sum_{x \in \alpha} q(x) = 1$. Then
$\sum_{x \in U} p(x) \le \sum_{x \in U} q(x)$ for every upper set $U \subseteq \alpha$ if and only
if there is a function $\pi : \alpha \times \alpha \to \mathbb{R}$ such that $\pi(x, y) \ge 0$
for all $x, y \in \alpha$, $\sum_{y \in \alpha} \pi(x, y) = p(x)$ for every $x \in \alpha$,
$\sum_{x \in \alpha} \pi(x, y) = q(y)$ for every $y \in \alpha$, and $\pi(x, y) = 0$ whenever
$x \not\le y$.

## Sources

- V. Strassen, "The Existence of Probability Measures with Given Marginals", Ann. Math. Statist. 36 (1965), 423-439, DOI 10.1214/aoms/1177700153.

Formalized by `MathlibExt.Probability.StrassenCouplingWanted.strassen_coupling_finite_poset`, a theorem declared in [MathlibExt/Probability/StrassenCoupling.lean, line 563](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/StrassenCoupling.lean#L563). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/finite-strassen-stochastic-domination/index.html#strassen-coupling-finite-poset).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite Strassen stochastic domination](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/finite-strassen-stochastic-domination/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/correlation-inequalities/stochastic-domination-and-strassen-s-theorem/finite-strassen-stochastic-domination)
