---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.EgorovDominatedRealLineWanted.exists_measure_lt_tendstoUniformlyOn_compl_of_ae_tendsto_of_abs_le, MathlibExt.MeasureTheory.Function.Lusin.lusin
statement: formalized
---

# Integration and convergence: its own results

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/index.html).

The Lebesgue integral and its convergence theorems, modes of convergence of measurable functions, approximation by simple functions, product measures, convolution, differentiation under the integral sign and integral inequalities.

## Egorov's theorem on the real line under integrable domination

Let
$f : \mathbb{R} \to \mathbb{R}$ be any function and let $f_n : \mathbb{R} \to \mathbb{R}$,
$n \in \mathbb{N}$, be Borel measurable functions with $f_n(x) \to f(x)$ for almost every
$x \in \mathbb{R}$. Let $g : \mathbb{R} \to \mathbb{R}$ be Lebesgue integrable with
$|f_n(x)| \le g(x)$ for all $n$ and all $x \in \mathbb{R}$. Then for every $\varepsilon > 0$ there
is a Borel set $E \subseteq \mathbb{R}$ of Lebesgue measure less than $\varepsilon$ such that
$f_n \to f$ uniformly on $\mathbb{R} \setminus E$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Measure and integration; Classical measure theory), problem `ma_proofbench_l2_43`.

Stated but not proved: `MathlibExt.MeasureTheory.EgorovDominatedRealLineWanted.exists_measure_lt_tendstoUniformlyOn_compl_of_ae_tendsto_of_abs_le` is written with `theorem_wanted` in [WantedExt/MeasureTheory/EgorovDominatedRealLineWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/EgorovDominatedRealLineWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/index.html#exists-measure-lt-tendsto-uniformly-on-c).

## Lusin's theorem

Let $X$ be a locally compact Hausdorff topological space with its Borel
$\sigma$-algebra, and let $\mu$ be a finite measure on $X$ that is regular: finite on compact
sets, outer regular, and inner regular on open sets by compact sets. Let $Y$ be a
second-countable topological space with its Borel $\sigma$-algebra, and let $f : X \to Y$ be
measurable. Then for every real $\varepsilon > 0$ there is a compact set $K \subseteq X$ with
$\mu(X \setminus K) < \varepsilon$ such that $f$ is continuous on $K$.

## Sources

- G. B. Folland, Real Analysis, 2nd ed., Lusin's theorem.

Formalized by `MathlibExt.MeasureTheory.Function.Lusin.lusin`, a theorem declared in [MathlibExt/MeasureTheory/Function/Lusin.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/Lusin.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/index.html#lusin).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integration and convergence](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/integration)
