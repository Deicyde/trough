---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SidonSubsetCountErdosProblem861Wanted.sidonSubsetsUpTo, MathlibExt.Combinatorics.SidonSubsetCountErdosProblem861Wanted.maxSidonSize, MathlibExt.Combinatorics.SidonSubsetCountErdosProblem861Wanted.sidonCountOverTwoPowMaxDiverges, MathlibExt.Combinatorics.SidonSubsetCountErdosProblem861Wanted.sidonCountExponentAsymptotic, MathlibExt.Combinatorics.SidonSubsetCountErdosProblem861Wanted.sidonCountOverTwoPowMaxDiverges_holds, MathlibExt.Combinatorics.SidonSubsetCountErdosProblem861Wanted.sidonCountExponentAsymptotic_refuted
statement: formalized
---

# Number of Sidon sets

6 results, 4 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/number-of-sidon-sets/index.html).

## Sidon subsets of $\{1, \dots, N\}$

For a natural number $N$, this is the finite family
of all subsets of $\{1, \dots, N\}$ that are Sidon sets of natural numbers, including the empty
set and the singletons.

Formalized by `MathlibExt.Combinatorics.SidonSubsetCountErdosProblem861Wanted.sidonSubsetsUpTo`, a definition declared in [WantedExt/Combinatorics/SidonSubsetCountErdosProblem861Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SidonSubsetCountErdosProblem861Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/number-of-sidon-sets/index.html#sidon-subsets-up-to).

## Largest Sidon subset of $\{1, \dots, N\}$ (Erdős Problem 861)

For a natural number $N$,
$f(N)$ is the largest cardinality of a Sidon subset of $\{1, \dots, N\}$.

Formalized by `MathlibExt.Combinatorics.SidonSubsetCountErdosProblem861Wanted.maxSidonSize`, a definition declared in [WantedExt/Combinatorics/SidonSubsetCountErdosProblem861Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SidonSubsetCountErdosProblem861Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/number-of-sidon-sets/index.html#max-sidon-size).

## Erdős Problem 861, first question

Let $A(N)$ be the number of Sidon subsets of
$\{1, \dots, N\}$, including the empty set and the singletons, and let $f(N)$ be the
largest size of a Sidon subset of $\{1, \dots, N\}$. The statement is that
$A(N) / 2^{f(N)} \to \infty$ as $N \to \infty$.

Formalized by `MathlibExt.Combinatorics.SidonSubsetCountErdosProblem861Wanted.sidonCountOverTwoPowMaxDiverges`, a definition declared in [WantedExt/Combinatorics/SidonSubsetCountErdosProblem861Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SidonSubsetCountErdosProblem861Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/number-of-sidon-sets/index.html#sidon-count-over-two-pow-max-diverges).

## Erdős Problem 861, second question

Let $A(N)$ be the number of Sidon subsets of
$\{1, \dots, N\}$, including the empty set and the singletons, and let $f(N)$ be the
largest size of a Sidon subset of $\{1, \dots, N\}$. The statement is that
$\log_2 A(N) / f(N) \to 1$ as $N \to \infty$, that is, $A(N) = 2^{(1 + o(1)) f(N)}$.

Formalized by `MathlibExt.Combinatorics.SidonSubsetCountErdosProblem861Wanted.sidonCountExponentAsymptotic`, a definition declared in [WantedExt/Combinatorics/SidonSubsetCountErdosProblem861Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SidonSubsetCountErdosProblem861Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/number-of-sidon-sets/index.html#sidon-count-exponent-asymptotic).

## Erdős Problem 861, first question: positive answer

Let $A(N)$ be the number of Sidon
subsets of $\{1, \dots, N\}$, including the empty set and the singletons, and let $f(N)$ be the
largest size of a Sidon subset of $\{1, \dots, N\}$. Then $A(N) / 2^{f(N)} \to \infty$ as
$N \to \infty$.

Saxton and Thomason proved $A(N) \ge 2^{(1.16 + o(1)) \sqrt{N}}$ (Theorem 2.11), and
$f(N) \sim \sqrt{N}$, so $A(N) / 2^{f(N)} \ge 2^{(0.16 + o(1)) \sqrt{N}} \to \infty$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #861, https://www.erdosproblems.com/861 (status SOLVED); resolution: D. Saxton and A. Thomason, Hypergraph containers, Invent. Math. (2015), 925-992, arXiv:1204.6595 (lower bound); Y. Kohayakawa, S. J. Lee, V. Rödl and W. Samotij, The number of Sidon sets and the maximum size of Sidon sets contained in a sparse random set of integers, Random Structures Algorithms (2015), 1-25 (upper bound), Saxton-Thomason Theorem 2.11: there are between 2^{(1.16 + o(1)) √n} and 2^{(55 + o(1)) √n} Sidon subsets of [n], the lower bound answering negatively whether there are only 2^{(1 + o(1)) √n}; erdosproblems.com/861: f(N) ∼ N^{1/2}, both questions are settled, the first positively and the second negatively, and 2^{1.16 f(N)} ≤ A(N) ≤ 2^{6.442 f(N)} for large N, https://arxiv.org/abs/1204.6595.

Stated but not proved: `MathlibExt.Combinatorics.SidonSubsetCountErdosProblem861Wanted.sidonCountOverTwoPowMaxDiverges_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/SidonSubsetCountErdosProblem861Wanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SidonSubsetCountErdosProblem861Wanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/number-of-sidon-sets/index.html#sidon-count-over-two-pow-max-diverges-ho).

## Erdős Problem 861, second question: negative answer

Let $A(N)$ be the number of Sidon
subsets of $\{1, \dots, N\}$, including the empty set and the singletons, and let $f(N)$ be the
largest size of a Sidon subset of $\{1, \dots, N\}$. Then the ratio $\log_2 A(N) / f(N)$ does not
tend to $1$ as $N \to \infty$; that is, $A(N) = 2^{(1 + o(1)) f(N)}$ fails.

Saxton and Thomason proved $A(N) \ge 2^{(1.16 + o(1)) \sqrt{N}}$ (Theorem 2.11), and
$f(N) \sim \sqrt{N}$, so $\log_2 A(N) / f(N) \ge 1.16 + o(1)$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #861, https://www.erdosproblems.com/861 (status SOLVED); resolution: D. Saxton and A. Thomason, Hypergraph containers, Invent. Math. (2015), 925-992, arXiv:1204.6595 (lower bound); Y. Kohayakawa, S. J. Lee, V. Rödl and W. Samotij, The number of Sidon sets and the maximum size of Sidon sets contained in a sparse random set of integers, Random Structures Algorithms (2015), 1-25 (upper bound), Saxton-Thomason Theorem 2.11: there are between 2^{(1.16 + o(1)) √n} and 2^{(55 + o(1)) √n} Sidon subsets of [n], the lower bound answering negatively whether there are only 2^{(1 + o(1)) √n}; erdosproblems.com/861: f(N) ∼ N^{1/2}, both questions are settled, the first positively and the second negatively, and 2^{1.16 f(N)} ≤ A(N) ≤ 2^{6.442 f(N)} for large N, https://arxiv.org/abs/1204.6595.

Stated but not proved: `MathlibExt.Combinatorics.SidonSubsetCountErdosProblem861Wanted.sidonCountExponentAsymptotic_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/SidonSubsetCountErdosProblem861Wanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SidonSubsetCountErdosProblem861Wanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/number-of-sidon-sets/index.html#sidon-count-exponent-asymptotic-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Number of Sidon sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/number-of-sidon-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/number-of-sidon-sets)
