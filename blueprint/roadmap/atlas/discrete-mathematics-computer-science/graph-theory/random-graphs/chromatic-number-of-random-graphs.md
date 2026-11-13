---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ErdosProblem625Wanted.probDiffGT, MathlibExt.Combinatorics.ErdosProblem625Wanted.conjecture, MathlibExt.Combinatorics.ErdosProblem625Wanted.conjecture_holds
statement: formalized
---

# Chromatic number of random graphs

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/chromatic-number-of-random-graphs/index.html).

## Probability of a large chromatic–cochromatic gap

For natural numbers $C$ and $n$, the
proportion of simple graphs $G$ on the vertex set $\{0, \dots, n - 1\}$ with
$\chi(G) - \zeta(G) > C$, where $\chi$ is the chromatic number and $\zeta$ the cochromatic
number; equivalently, the probability of this event for a uniformly random labelled graph,
$G \sim G(n, 1/2)$.

Formalized by `MathlibExt.Combinatorics.ErdosProblem625Wanted.probDiffGT`, a definition declared in [WantedExt/Combinatorics/ErdosProblem625Wanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosProblem625Wanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/chromatic-number-of-random-graphs/index.html#prob-diff-gt).

## Erdős Problem 625

The statement that for every natural number $C$, the probability
that a uniformly random simple graph $G$ on the vertex set $\{0, \dots, n - 1\}$ (that is,
$G \sim G(n, 1/2)$) satisfies $\chi(G) - \zeta(G) > C$ tends to $1$ as $n \to \infty$, where
$\chi$ is the chromatic number and $\zeta$ the cochromatic number. In other words,
$\chi(G) - \zeta(G) \to \infty$ with high probability.

Formalized by `MathlibExt.Combinatorics.ErdosProblem625Wanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ErdosProblem625Wanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosProblem625Wanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/chromatic-number-of-random-graphs/index.html#conjecture).

## Chromatic minus cochromatic number of a random graph tends to infinity

For every natural
number $C$, the probability that a uniformly random simple graph $G$ on the vertex set
$\{0, \dots, n - 1\}$ (that is, $G \sim G(n, 1/2)$) satisfies $\chi(G) - \zeta(G) > C$
tends to $1$ as $n \to \infty$, where $\chi$ is the chromatic number and $\zeta$ the
cochromatic number.

Petkov and GPT-5.6 improved Heckel's bounds to $\chi(G) - \zeta(G) \gg n / (\log n)^3$ with
high probability for $G \sim G(n, 1/2)$, as Heckel predicted; this answers Erdős Problem 625 in
the affirmative.

## Sources

- T. F. Bloom, Erdős Problem #625, erdosproblems.com (live page, LaTeX source and forum threads read 2026-10-22), https://www.erdosproblems.com/625; S. Petkov (with GPT-5.6), proof for Erdős Problem #625, https://github.com/SamPetkov/Erdos/blob/main/625/arxiv_625.pdf.

Stated but not proved: `MathlibExt.Combinatorics.ErdosProblem625Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosProblem625Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosProblem625Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/chromatic-number-of-random-graphs/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Chromatic number of random graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/chromatic-number-of-random-graphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/random-graphs/chromatic-number-of-random-graphs)
