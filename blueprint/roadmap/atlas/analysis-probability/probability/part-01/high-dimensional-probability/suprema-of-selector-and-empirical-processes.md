---
declaration: section
origin: cited
lean: MathlibExt.Analysis.SupremumOfSelectorProcessesWanted.SupremumOfSelectorProcesses.binomialSetDistribution, MathlibExt.Analysis.SupremumOfSelectorProcessesWanted.SupremumOfSelectorProcesses.IsSmall, MathlibExt.Analysis.SupremumOfSelectorProcessesWanted.SupremumOfSelectorProcesses.theorem_1_2, MathlibExt.Analysis.SupremumOfSelectorProcessesWanted.SupremumOfSelectorProcesses.Z, MathlibExt.Analysis.SupremumOfSelectorProcessesWanted.SupremumOfSelectorProcesses.theorem_1_3
statement: formalized
---

# Suprema of selector and empirical processes

5 results, 3 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/suprema-of-selector-and-empirical-processes/index.html).

## Binomial random subset

For a type $X$ and $p \in [0, 1]$, the binomial random subset
distribution on $X$ with parameter $p$ is the probability measure on the subsets of $X$ under
which each element of $X$ belongs to the random subset independently with probability $p$. A
random subset with this law is denoted $X_p$.

Formalized by `MathlibExt.Analysis.SupremumOfSelectorProcessesWanted.SupremumOfSelectorProcesses.binomialSetDistribution`, a definition declared in [WantedExt/Analysis/SupremumOfSelectorProcessesWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SupremumOfSelectorProcessesWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/suprema-of-selector-and-empirical-processes/index.html#binomial-set-distribution).

## $p$-small families of sets

Let $X$ be a finite type and $p \in [0, 1]$. A family
$\mathcal{F}$ of subsets of $X$ is $p$-small when there is a family $\mathcal{G}$ of subsets of
$X$ such that every member of $\mathcal{F}$ contains some member of $\mathcal{G}$ and
$\sum_{S \in \mathcal{G}} p^{|S|} \le 1/2$.

Formalized by `MathlibExt.Analysis.SupremumOfSelectorProcessesWanted.SupremumOfSelectorProcesses.IsSmall`, a definition declared in [WantedExt/Analysis/SupremumOfSelectorProcessesWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SupremumOfSelectorProcessesWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/suprema-of-selector-and-empirical-processes/index.html#is-small).

## Park–Pham theorem on selector processes (Talagrand's selector process conjecture)

There is
a real number $L > 0$ with the following property. Let $0 < p < 1$, let $X$ be a finite type,
let $\Lambda$ be a set of functions from $X$ to $[0, \infty)$, and let $X_p$ be a binomial random
subset of $X$ with parameter $p$. Write
$E = \mathbb{E}\bigl[\sup_{f \in \Lambda} \sum_{i \in X_p} f(i)\bigr]$, computed in
$[0, \infty]$. If $0 < E < \infty$, then the family of subsets $s \subseteq X$ with
$\sup_{f \in \Lambda} \sum_{i \in s} f(i) \ge L E$ is $p$-small.

The hypothesis $0 < E < \infty$ is not stated explicitly in the paper's theorem, but it is used
in the last step of the proof, which derives a contradiction from an inequality $E \ge c E$
with a constant $c > 1$.

## Sources

- J. Park and H. T. Pham, `On a conjecture of Talagrand on selector processes and a consequence on positive empirical processes`, Annals of Math, 199 (3) 2024. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_supremum_of_selector_processes` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.SupremumOfSelectorProcessesWanted.SupremumOfSelectorProcesses.theorem_1_2` is written with `theorem_wanted` in [WantedExt/Analysis/SupremumOfSelectorProcessesWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SupremumOfSelectorProcessesWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/suprema-of-selector-and-empirical-processes/index.html#theorem-1-2).

## Empirical averages

Given random variables $Y_1, \dots, Y_N$ on $\Omega$ with values in
$\mathbb{T}$ and a function $f : \mathbb{T} \to [0, \infty)$, $Z_N(f)$ is the random variable
$Z_N(f)(\omega) = \frac{1}{N} \sum_{i=1}^{N} f(Y_i(\omega))$, which is $0$ when $N = 0$.

When $Y_1, \dots, Y_N$ are i.i.d., $Z_N(f)$ is called an empirical process.

Formalized by `MathlibExt.Analysis.SupremumOfSelectorProcessesWanted.SupremumOfSelectorProcesses.Z`, a definition declared in [WantedExt/Analysis/SupremumOfSelectorProcessesWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SupremumOfSelectorProcessesWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/suprema-of-selector-and-empirical-processes/index.html#z).

## Park–Pham theorem on positive empirical processes

There is a real number $L > 0$ with the
following property. Let $N > 0$, let $\mathbb{T}$ be a Polish space with its Borel
$\sigma$-algebra and a probability measure $\nu$, and let $Y_1, \dots, Y_N$ be independent random
variables on a measure space $(\Omega, P)$ with values in $\mathbb{T}$, each with law $\nu$. For
$f : \mathbb{T} \to [0, \infty)$ let $Z_f = \frac{1}{N} \sum_{i=1}^{N} f(Y_i)$. Let
$\mathcal{F}$ be a finite set of measurable functions from $\mathbb{T}$ to $[0, \infty)$ that are
essentially bounded with respect to $\nu$, and write
$E = \mathbb{E}\bigl[\sup_{f \in \mathcal{F}} Z_f\bigr]$, computed in $[0, \infty]$. If
$0 < E < \infty$, then there is a finite collection $\mathcal{C}$ of pairs $(g, t)$, where
$g : \mathbb{T} \to [0, \infty)$ is measurable and $t > 0$ is real, such that every $\omega$
with $\sup_{f \in \mathcal{F}} Z_f(\omega) \ge L E$ satisfies $Z_g(\omega) \ge t$ for some
$(g, t) \in \mathcal{C}$, and $\sum_{(g, t) \in \mathcal{C}} P(Z_g \ge t) \le 1/2$.

The paper does not state explicitly that $\mathcal{C}$ is finite. It must at least be countable
for the sum to make sense, and the collections produced by the proof are finite.

## Sources

- J. Park and H. T. Pham, `On a conjecture of Talagrand on selector processes and a consequence on positive empirical processes`, Annals of Math, 199 (3) 2024. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_supremum_of_selector_processes` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.SupremumOfSelectorProcessesWanted.SupremumOfSelectorProcesses.theorem_1_3` is written with `theorem_wanted` in [WantedExt/Analysis/SupremumOfSelectorProcessesWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SupremumOfSelectorProcessesWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/suprema-of-selector-and-empirical-processes/index.html#theorem-1-3).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Suprema of selector and empirical processes](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/suprema-of-selector-and-empirical-processes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/high-dimensional-probability/suprema-of-selector-and-empirical-processes)
