---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.MaximalFunctionAeTendstoZeroWanted.ae_tendsto_maximal_zero_of_ae_tendsto_zero_of_bounded, MathlibExt.MeasureTheory.SingularMeasureMaximalFunctionWanted.measure_setOf_maximalFunction_lt_top_eq_zero_of_mutuallySingular
statement: formalized
---

# Hardy–Littlewood maximal function

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/real-functions/hardy-littlewood-maximal-function/index.html).

## Maximal functions of bounded a.e.-null sequences tend to zero a.e

Let
$(f_n)_{n \in \mathbb{N}}$ be a sequence of functions $f_n : \mathbb{R} \to \mathbb{R}$, each
Lebesgue measurable on $[0,1]$, such that $f_n(x) \in [0,1]$ for every $n$ and every
$x \in [0,1]$, and $f_n(x) \to 0$ as $n \to \infty$ for almost every $x \in [0,1]$. For
$x \in [0,1]$ let

$$Mf_n(x) = \sup_I \frac{1}{|I|} \int_I |f_n(y)|\,dy,$$

where the supremum is taken over all closed intervals $I = [a,b]$ with $a < b$ and
$x \in I \subseteq [0,1]$, and $|I| = b - a$. Then $Mf_n(x) \to 0$ as $n \to \infty$ for almost
every $x \in [0,1]$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Measure and integration; Classical measure theory), problem `ma_proofbench_l2_74`.

Stated but not proved: `MathlibExt.MeasureTheory.MaximalFunctionAeTendstoZeroWanted.ae_tendsto_maximal_zero_of_ae_tendsto_zero_of_bounded` is written with `theorem_wanted` in [WantedExt/MeasureTheory/MaximalFunctionAeTendstoZeroWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/MaximalFunctionAeTendstoZeroWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/real-functions/hardy-littlewood-maximal-function/index.html#ae-tendsto-maximal-zero-of-ae-tendsto-ze).

## The maximal function of a singular measure is infinite almost everywhere for that measure

**The maximal function of a singular measure is infinite almost everywhere for that
measure.** Let $n$ be a natural number and let $\mu$ be a Borel measure on $\mathbb{R}^n$ that is
mutually singular with respect to Lebesgue measure $m_n$. Write $B(x, r)$ for the open ball of
radius $r$ about $x$ and define $M_\mu : \mathbb{R}^n \to [0, \infty]$ by

$$
M_\mu(x) = \sup_{r>0} \frac{\mu(B(x, r))}{m_n(B(x, r))}.
$$

Then $\mu(\{x \in \mathbb{R}^n : M_\mu(x) < \infty\}) = 0$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Measure and integration; Classical measure theory), problem `ma_proofbench_l2_44`.

Stated but not proved: `MathlibExt.MeasureTheory.SingularMeasureMaximalFunctionWanted.measure_setOf_maximalFunction_lt_top_eq_zero_of_mutuallySingular` is written with `theorem_wanted` in [WantedExt/MeasureTheory/SingularMeasureMaximalFunctionWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/SingularMeasureMaximalFunctionWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/real-functions/hardy-littlewood-maximal-function/index.html#measure-set-of-maximal-function-lt-top-e).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hardy–Littlewood maximal function](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/real-functions/hardy-littlewood-maximal-function/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/MeasureTheory/real-functions/hardy-littlewood-maximal-function)
