---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SidonUpperBoundImprovementGreenProblem31Wanted.maxSidonSubsetSize, MathlibExt.Combinatorics.SidonUpperBoundImprovementGreenProblem31Wanted.sidonUpperBoundImproved, MathlibExt.Combinatorics.SidonUpperBoundImprovementGreenProblem31Wanted.sidonUpperBoundImproved_holds
statement: formalized
---

# Upper bounds for Sidon sets

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/upper-bounds-for-sidon-sets/index.html).

## Largest Sidon subset of $\{1, \dots, N\}$ (Green's Problem 31)

For a natural number
$N$, $F(N)$ is the largest cardinality of a Sidon subset of $[N] = \{1, \dots, N\}$.

Formalized by `MathlibExt.Combinatorics.SidonUpperBoundImprovementGreenProblem31Wanted.maxSidonSubsetSize`, a definition declared in [WantedExt/Combinatorics/SidonUpperBoundImprovementGreenProblem31Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SidonUpperBoundImprovementGreenProblem31Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/upper-bounds-for-sidon-sets/index.html#max-sidon-subset-size).

## Green's Problem 31: improving Lindström's upper bound

Let $F(N)$ be the largest
size of a Sidon subset of $\{1, \dots, N\}$. The statement is that there are a real constant
$c < 1$ and a natural number $N_0$ such that $F(N) \le \sqrt{N} + c N^{1/4}$ for all $N \ge N_0$.

Lindström's bound is $F(N) \le N^{1/2} + N^{1/4} + O(1)$; the statement asks for a constant
below $1$ in the second term.

Formalized by `MathlibExt.Combinatorics.SidonUpperBoundImprovementGreenProblem31Wanted.sidonUpperBoundImproved`, a definition declared in [WantedExt/Combinatorics/SidonUpperBoundImprovementGreenProblem31Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SidonUpperBoundImprovementGreenProblem31Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/upper-bounds-for-sidon-sets/index.html#sidon-upper-bound-improved).

## Lindström's upper bound for Sidon sets can be improved

Let $F(N)$ be the largest size of a
Sidon subset of $\{1, \dots, N\}$. There are a real constant $c < 1$ and a natural number $N_0$
such that $F(N) \le \sqrt{N} + c N^{1/4}$ for all $N \ge N_0$.

Balogh, Füredi and Roy proved this with $c = 0.998$; Carter, Hunter and O'Bryant later lowered
the constant to $0.98183$.

## Sources

- B. Green, 100 open problems, Problem 31 (manuscript, update of December 2025), https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf; resolution: J. Balogh, Z. Füredi and S. Roy, An upper bound on the size of Sidon sets, Amer. Math. Monthly 130 (2023), 437-445, doi:10.1080/00029890.2023.2176667; arXiv:2103.15850, abstract: the maximum size of a Sidon set of {1, ..., n} is at most √n + 0.998 n^{1/4} for sufficiently large n; Green, Problem 31, 'Update 2021' records this bound and its 2023 improvement to 0.98183 (D. Carter, Z. Hunter and K. O'Bryant, Acta Math. Hungar. 175 (2025), 108-126), https://doi.org/10.1080/00029890.2023.2176667.

Stated but not proved: `MathlibExt.Combinatorics.SidonUpperBoundImprovementGreenProblem31Wanted.sidonUpperBoundImproved_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/SidonUpperBoundImprovementGreenProblem31Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SidonUpperBoundImprovementGreenProblem31Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/upper-bounds-for-sidon-sets/index.html#sidon-upper-bound-improved-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Upper bounds for Sidon sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/upper-bounds-for-sidon-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/upper-bounds-for-sidon-sets)
