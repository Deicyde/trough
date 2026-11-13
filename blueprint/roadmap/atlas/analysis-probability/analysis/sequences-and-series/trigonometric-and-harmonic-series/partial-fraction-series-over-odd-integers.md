---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry1Logratio.ramanujan_part1_ch9_entry1_logratio, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry2.ramanujan_part1_ch9_entry2
statement: formalized
proof: formalized
---

# Partial-fraction series over odd integers

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/partial-fraction-series-over-odd-integers/index.html).

## Difference series over $2k+1 \pm a$ that are polynomials on $(-\pi, \pi)$

Let $r$ be a
positive integer, $a$ a real number that is not an odd integer, and $x$ a real number with
$|x| < \pi$. For a natural number $s$ let $c_k(s) = (2k+1-a)^{-s} - (2k+1+a)^{-s}$ and
$C_s(a) = \sum_{k=0}^{\infty} c_k(s)$. Then $\sum_k c_k(r)$ is summable, and either $r$ is odd,
$\sum_k c_k(r-2j)$ is summable for $0 \le j \le (r-1)/2$, and the partial sums of
$\sum_{k=0}^{\infty} \bigl(\frac{\cos((2k+1-a)x)}{(2k+1-a)^r} -
\frac{\cos((2k+1+a)x)}{(2k+1+a)^r}\bigr)$ converge to
$\sum_{j=0}^{(r-1)/2} (-1)^j C_{r-2j}(a) \frac{x^{2j}}{(2j)!}$; or $r$ is even,
$\sum_k c_k(r-2j-1)$ is summable for $0 \le j < r/2$, and the partial sums of
$\sum_{k=0}^{\infty} \bigl(\frac{\sin((2k+1-a)x)}{(2k+1-a)^r} -
\frac{\sin((2k+1+a)x)}{(2k+1+a)^r}\bigr)$ converge to
$\sum_{0 \le j < r/2} (-1)^j C_{r-2j-1}(a) \frac{x^{2j+1}}{(2j+1)!}$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9, Entry 1, pp. 233–235.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry1Logratio.ramanujan_part1_ch9_entry1_logratio`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry1Logratio.lean, line 1621](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry1Logratio.lean#L1621). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/partial-fraction-series-over-odd-integers/index.html#ramanujan-part1-ch9-entry1-logratio).

## Sum series over $2k+1 \pm a$ on $(0, \pi)$

Let $r \ge 2$ be an integer, $a$ a real
number that is not an odd integer, and $x$ a real number with $0 < x < \pi$. For a natural
number $s$ let $d_k(s) = (2k+1-a)^{-s} + (2k+1+a)^{-s}$ and
$D_s(a) = \sum_{k=0}^{\infty} d_k(s)$. Then $\sum_k d_k(r)$ is summable, and either $r$ is
even, $\sum_k d_k(r-2j)$ is summable for $0 \le j < r/2$, and the partial sums of
$\sum_{k=0}^{\infty} \bigl(\frac{\cos((2k+1-a)x)}{(2k+1-a)^r} +
\frac{\cos((2k+1+a)x)}{(2k+1+a)^r}\bigr)$ converge to
$\sum_{0 \le j < r/2} (-1)^j D_{r-2j}(a) \frac{x^{2j}}{(2j)!} +
(-1)^{r/2} \frac{\pi x^{r-1}}{2 (r-1)!}$; or $r$ is odd, $\sum_k d_k(r-1-2j)$ is summable
for $0 \le j < (r-1)/2$, and the partial sums of
$\sum_{k=0}^{\infty} \bigl(\frac{\sin((2k+1-a)x)}{(2k+1-a)^r} +
\frac{\sin((2k+1+a)x)}{(2k+1+a)^r}\bigr)$ converge to
$\sum_{0 \le j < (r-1)/2} (-1)^j D_{r-1-2j}(a) \frac{x^{2j+1}}{(2j+1)!} +
(-1)^{(r-1)/2} \frac{\pi x^{r-1}}{2 (r-1)!}$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry2.ramanujan_part1_ch9_entry2`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry2.lean, line 1505](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry2.lean#L1505). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/partial-fraction-series-over-odd-integers/index.html#ramanujan-part1-ch9-entry2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partial-fraction series over odd integers](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/partial-fraction-series-over-odd-integers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/partial-fraction-series-over-odd-integers)
