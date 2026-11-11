---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SumsetGrowthZeroDensityErdosProblem245Wanted.sumsetRatioLimsupAtLeastThree, MathlibExt.Combinatorics.SumsetGrowthZeroDensityErdosProblem245Wanted.sumsetRatioLimsupAtLeastThree_holds
statement: formalized
---

# Sumsets of sets of density zero

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/sumsets-of-sets-of-density-zero/index.html).

## Erdős Problem 245 on sumsets of sets of density zero

For $N \in \mathbb{N}$ write
$[1, N] = \{1, \dots, N\}$, and for $A \subseteq \mathbb{N}$ write
$A + A = \{a + b \mid a, b \in A\}$. This is the statement that for every infinite set
$A \subseteq \mathbb{N}$ with $\lvert A \cap [1, N] \rvert / N \to 0$ as $N \to \infty$ and every
real $\varepsilon > 0$, there are infinitely many $N$ with
$\lvert (A + A) \cap [1, N] \rvert > (3 - \varepsilon) \lvert A \cap [1, N] \rvert$. This expresses
$\limsup_{N \to \infty} \lvert (A + A) \cap [1, N] \rvert / \lvert A \cap [1, N] \rvert \ge 3$.

Formalized by `MathlibExt.Combinatorics.SumsetGrowthZeroDensityErdosProblem245Wanted.sumsetRatioLimsupAtLeastThree`, a definition declared in [WantedExt/Combinatorics/SumsetGrowthZeroDensityErdosProblem245Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SumsetGrowthZeroDensityErdosProblem245Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/sumsets-of-sets-of-density-zero/index.html#sumset-ratio-limsup-at-least-three).

## Freiman's theorem on sumsets of sets of density zero

For $N \in \mathbb{N}$ write
$[1, N] = \{1, \dots, N\}$, and for $A \subseteq \mathbb{N}$ write
$A + A = \{a + b \mid a, b \in A\}$. Let $A \subseteq \mathbb{N}$ be an infinite set with
$\lvert A \cap [1, N] \rvert / N \to 0$ as $N \to \infty$. Then for every real $\varepsilon > 0$
there are infinitely many $N$ with
$\lvert (A + A) \cap [1, N] \rvert > (3 - \varepsilon) \lvert A \cap [1, N] \rvert$; that is,
$\limsup_{N \to \infty} \lvert (A + A) \cap [1, N] \rvert / \lvert A \cap [1, N] \rvert \ge 3$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #245, https://www.erdosproblems.com/245 (status PROVED); resolution: G. A. Freiman, Foundations of a structural theory of set addition, Transl. Math. Monogr. 37, Amer. Math. Soc. (1973), erdosproblems.com/245: proved by Freiman [Fr73], https://doi.org/10.1090/mmono/037.

Stated but not proved: `MathlibExt.Combinatorics.SumsetGrowthZeroDensityErdosProblem245Wanted.sumsetRatioLimsupAtLeastThree_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/SumsetGrowthZeroDensityErdosProblem245Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SumsetGrowthZeroDensityErdosProblem245Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/sumsets-of-sets-of-density-zero/index.html#sumset-ratio-limsup-at-least-three-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sumsets of sets of density zero](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/sumsets-of-sets-of-density-zero/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/additive-bases/sumsets-of-sets-of-density-zero)
