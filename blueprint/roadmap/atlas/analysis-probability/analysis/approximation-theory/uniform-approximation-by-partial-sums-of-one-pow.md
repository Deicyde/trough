---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ScottishBook159Wanted.ScottishBookProblem159Claim, MathlibExt.Analysis.ScottishBook159Wanted.problem159Refuted
statement: formalized
---

# Uniform approximation by partial sums of one power series

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/uniform-approximation-by-partial-sums-of-one-pow/index.html).

## The claim of Scottish Book Problem 159

There is a sequence of real numbers
$a_0, a_1, a_2, \dots$ such that for every $\varepsilon > 0$ there is a natural number $N$ with the
following property: for every function $f : \mathbb{R} \to \mathbb{R}$ that is continuous on
$[0, 1]$ and satisfies $f(0) = 0$ and $0 \le f(x) \le 1$ for all $x \in [0, 1]$, there is a natural
number $n \le N$ with $|f(x) - P_n(x)| < \varepsilon$ for all $x \in [0, 1]$, where
$P_n(x) = \sum_{k=0}^{n} a_k x^k$ is the $n$-th partial sum of the power series $\sum a_k x^k$.

Formalized by `MathlibExt.Analysis.ScottishBook159Wanted.ScottishBookProblem159Claim`, a definition declared in [WantedExt/Analysis/ScottishBook159Wanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ScottishBook159Wanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/uniform-approximation-by-partial-sums-of-one-pow/index.html#scottish-book-problem159-claim).

## Scottish Book Problem 159 has a negative answer

There is no sequence of real numbers
$a_0, a_1, a_2, \dots$ with the following property: for every $\varepsilon > 0$ there is a natural
number $N$ such that for every function $f : \mathbb{R} \to \mathbb{R}$ that is continuous on
$[0, 1]$ and satisfies $f(0) = 0$ and $0 \le f(x) \le 1$ for all $x \in [0, 1]$, there is a natural
number $n \le N$ with $\left|f(x) - \sum_{k=0}^{n} a_k x^k\right| < \varepsilon$ for all
$x \in [0, 1]$.

Sternbach's argument in the addendum Ad 159 uses the functions $\sin^2(2^n \pi x)$. Mazur showed
that for an arbitrary family $\Phi$ of functions of this kind, a power series with this property
exists exactly when the functions of $\Phi$ are equicontinuous.

## Sources

- S. Ruziewicz, Problem 159 of the Scottish Book; Ad 159 in the typescript (Sternbach's negative argument; Mazur's equicontinuity criterion).

Stated but not proved: `MathlibExt.Analysis.ScottishBook159Wanted.problem159Refuted` is written with `theorem_wanted` in [WantedExt/Analysis/ScottishBook159Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ScottishBook159Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/uniform-approximation-by-partial-sums-of-one-pow/index.html#problem159-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Uniform approximation by partial sums of one power series](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/uniform-approximation-by-partial-sums-of-one-pow/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/approximation-theory/uniform-approximation-by-partial-sums-of-one-pow)
