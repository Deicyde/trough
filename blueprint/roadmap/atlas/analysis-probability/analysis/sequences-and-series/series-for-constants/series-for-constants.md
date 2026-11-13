---
declaration: section
origin: cited
lean: MathlibExt.Analysis.SpecialFunctions.CatalanSqrtTwo.catalan_hasProd_sqrt_two, MathlibExt.Analysis.SpecificLimits.ExpOneTaylorRemainderBoundWanted.exp_one_sub_sum_inv_factorial_pos_and_lt, MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry16Eulerconstantseries.ramanujan_part1_ch8_entry16_eulerconstantseries, MetaMathlibExt.reciprocal_central_binomial_sums
statement: formalized
---

# Series for π, ζ(3) and other constants: its own results

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/series-for-constants/index.html).

Series and infinite products evaluating constants: π, Catalan's constant, Euler's constant, √2, ζ(3), reciprocal central binomial sums.

## Catalan's product for $\sqrt{2}$

The infinite product over all natural numbers $m \ge 0$
of $\frac{(4m+2)^2}{(4m+1)(4m+3)}$ converges unconditionally to $\sqrt{2}$; that is,
$\frac{2 \cdot 2}{1 \cdot 3} \cdot \frac{6 \cdot 6}{5 \cdot 7} \cdot \frac{10 \cdot 10}{9 \cdot 11}
\cdots = \sqrt{2}$.

## Sources

- László Tóth, Journal of Integer Sequences 23, `toth46.tex`, lines 157-161. URL: <https://cs.uwaterloo.ca/journals/JIS/VOL23/Toth/toth46.tex>.

Formalized by `MathlibExt.Analysis.SpecialFunctions.CatalanSqrtTwo.catalan_hasProd_sqrt_two`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/CatalanSqrtTwo.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/CatalanSqrtTwo.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/series-for-constants/index.html#catalan-has-prod-sqrt-two).

## Error bound for the partial sums of the series for $e$

For every integer $n \ge 1$,

$$0 < e - \sum_{k=0}^{n} \frac{1}{k!} < \frac{1}{n \cdot n!}.$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_73`.

Stated but not proved: `MathlibExt.Analysis.SpecificLimits.ExpOneTaylorRemainderBoundWanted.exp_one_sub_sum_inv_factorial_pos_and_lt` is written with `theorem_wanted` in [WantedExt/Analysis/SpecificLimits/ExpOneTaylorRemainderBoundWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/SpecificLimits/ExpOneTaylorRemainderBoundWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/series-for-constants/index.html#exp-one-sub-sum-inv-factorial-pos-and-lt).

## Ramanujan's series for Euler's constant

For $k \ge 0$ let $A_k = (3^k - 1)/2$. Then the
series

$$S = \sum_{k=0}^{\infty} (k+1) \sum_{j=A_k+1}^{A_{k+1}} \frac{1}{(3j)^3 - 3j}$$

converges, and $\gamma = \log 2 - 2S$, where $\gamma$ is Euler's constant.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 8, Entry 16.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch8.Entry16Eulerconstantseries.ramanujan_part1_ch8_entry16_eulerconstantseries`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch8Entry16EulerConstantSeries.lean, line 689](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch8Entry16EulerConstantSeries.lean#L689). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/series-for-constants/index.html#ramanujan-part1-ch8-entry16-eulerconstan).

## Sums of reciprocals of central binomial coefficients

The following three series converge
absolutely, with the stated sums:

$$\sum_{n=1}^{\infty} \frac{1}{n \binom{2n}{n}} = \frac{\pi \sqrt{3}}{9},$$



$$\sum_{n=1}^{\infty} \frac{1}{\binom{2n}{n}} = \frac{1}{3} + \frac{2\pi}{9\sqrt{3}},$$



$$\sum_{n=1}^{\infty} \frac{1}{n^2 \binom{2n}{n}} = \frac{\pi^2}{18}.$$

## Sources

- B. Sury, Tianming Wang, and Feng-Zhen Zhao, "Identities Involving Reciprocals of Binomial Coefficients," Journal of Integer Sequences 7 (2004), Article 04.2.8, Corollary, lines 392–398, <https://cs.uwaterloo.ca/journals/JIS/VOL7/Sury/sury99.tex>.

Formalized by `MetaMathlibExt.reciprocal_central_binomial_sums`, a theorem declared in [MathlibExt/Analysis/Series/ReciprocalCentralBinomialSums.lean, line 617](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Series/ReciprocalCentralBinomialSums.lean#L617). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/series-for-constants/index.html#reciprocal-central-binomial-sums).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Series for π, ζ(3) and other constants](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/series-for-constants/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/sequences-and-series/series-for-constants)
