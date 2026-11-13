---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry13.ramanujan_part1_ch3_entry13, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry13CorollarySchroder.schroder_abel_binomial, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry13CorollarySchroder.ramanujan_part1_ch3_entry13_corollary_schroder, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry14Cor1Catalanpowerseries.ramanujan_part1_ch3_entry14_cor1_catalanpowerseries, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry14LagrangeSeries.lagrangeSeriesCoefficient, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry14LagrangeSeries.lagrangeSeriesCoefficient_zero, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry14LagrangeSeries.lagrangeSeriesCoefficient_of_ne_zero, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry14LagrangeSeries.lagrangeSeriesCoefficient_add
statement: formalized
proof: formalized
---

# Lagrange inversion series

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/lagrange-inversion-series/index.html).

## Ramanujan's series for powers of a root of $x = a \log x$ (Entry 13)

Let $a$ be a real
number with $|a| \ge e$. Then there is a real number $x > 0$ with $x = a \log x$ such that for
every real number $n$ the series

$$1 + \sum_{k=1}^{\infty} \frac{n (n+k)^{k-1}}{a^k\, k!}$$

is summable with sum $x^n$.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, definition (12.1), printed p. 66 / PDF p. 76, and Entry 13, printed pp. 69--70 / PDF pp. 79--80; historical attribution on printed p. 72 / PDF p. 82.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry13.ramanujan_part1_ch3_entry13`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry13.lean, line 971](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry13.lean#L971). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/lagrange-inversion-series/index.html#ramanujan-part1-ch3-entry13).

## Abel's binomial identity

For a complex number $w$, let $A_0(x) = 1$ and
$A_j(x) = x (x + j w)^{j-1}$ for $j \ge 1$. Then for all complex numbers $x$, $y$ and every
natural number $n$,

$$\sum_{j=0}^{n} \binom{n}{j} A_j(x) A_{n-j}(y) = A_n(x + y).$$

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry13CorollarySchroder.schroder_abel_binomial`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry13CorollarySchroder.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry13CorollarySchroder.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/lagrange-inversion-series/index.html#schroder-abel-binomial).

## Schröder's exponential series

Let $z$ and $w$ be complex numbers with
$|w| \le |e^{w-1}|$ and $|w| \le 1$. Then the series

$$1 + \sum_{k=1}^{\infty} \frac{z (z + k w)^{k-1} e^{-k w}}{k!}$$

converges unconditionally, and its sum is $e^z$.

The set of complex numbers $w$ with $|w| \le |e^{w-1}|$ has a bounded lobe containing $0$ and an
unbounded lobe, which meet only at $w = 1$. The condition $|w| \le 1$ selects the bounded lobe
(given the first condition, it is equivalent to $\operatorname{Re} w \le 1$); on the unbounded
lobe the identity fails in general.

Proof: Following Berndt's formula (13.8), we use Abel's binomial identity, a Cauchy product and a
holomorphic ODE; radial continuity selects the unit-disk branch of $u \mapsto u e^{-u}$.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Corollary to Entry 13, formula (13.8), printed p. 70 / PDF p. 80.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry13CorollarySchroder.ramanujan_part1_ch3_entry13_corollary_schroder`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry13CorollarySchroder.lean, line 788](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry13CorollarySchroder.lean#L788). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/lagrange-inversion-series/index.html#ramanujan-part1-ch3-entry13-corollary-sc).

## Ramanujan's series for powers of the Catalan generating function

Let $n$ and $a$ be real
numbers with $|a| \le 1/4$. For a natural number $k$ put $t_k = 0$ if $k < 2$, and

$$t_k = \frac{a^k}{k!} \prod_{j=k+1}^{2k-1} (n + j)$$

if $k \ge 2$. Then the series $\sum_k t_k$ is summable and

$$\left(\frac{2}{1 + \sqrt{1 - 4a}}\right)^{n} = 1 + n a + n \sum_{k=0}^{\infty} t_k.$$

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 14, Corollary 1, printed p. 71; scan PDF p. 81.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry14Cor1Catalanpowerseries.ramanujan_part1_ch3_entry14_cor1_catalanpowerseries`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry14Cor1Catalanpowerseries.lean, line 740](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry14Cor1Catalanpowerseries.lean#L740). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/lagrange-inversion-series/index.html#ramanujan-part1-ch3-entry14-cor1-catalan).

## Lagrange series coefficients

For real numbers $p$, $q$, $n$ and a natural number $k$,
the Lagrange series coefficient $C_{p,q}(n, k)$ is $1$ if $k = 0$, and for $k \ge 1$ it is

$$C_{p,q}(n, k) = n \prod_{j=1}^{k-1} (n + k p - j q)$$

(an empty product when $k = 1$).

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry14LagrangeSeries.lagrangeSeriesCoefficient`, a definition declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry14LagrangeSeries.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry14LagrangeSeries.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/lagrange-inversion-series/index.html#lagrange-series-coefficient).

## Lagrange series coefficient of degree zero

For all real numbers $p$, $q$, $n$, the
Lagrange series coefficient $C_{p,q}(n, 0)$ of degree $0$ equals $1$.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry14LagrangeSeries.lagrangeSeriesCoefficient_zero`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry14LagrangeSeries.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry14LagrangeSeries.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/lagrange-inversion-series/index.html#lagrange-series-coefficient-zero).

## Lagrange series coefficients of positive degree

For all real numbers $p$, $q$, $n$ and
every natural number $k \ne 0$, the Lagrange series coefficient of degree $k$ is

$$C_{p,q}(n, k) = n \prod_{j=1}^{k-1} (n + k p - j q).$$

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry14LagrangeSeries.lagrangeSeriesCoefficient_of_ne_zero`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry14LagrangeSeries.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry14LagrangeSeries.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/lagrange-inversion-series/index.html#lagrange-series-coefficient-of-ne-zero).

## Hagen–Rothe convolution for Lagrange series coefficients

For all real numbers $p$, $q$,
$r$, $s$ and every natural number $m$, the Lagrange series coefficients $C_{p,q}$ satisfy

$$C_{p,q}(r + s, m) = \sum_{k=0}^{m} \binom{m}{k} C_{p,q}(r, k) \, C_{p,q}(s, m - k).$$

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry14LagrangeSeries.lagrangeSeriesCoefficient_add`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry14LagrangeSeries.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry14LagrangeSeries.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/lagrange-inversion-series/index.html#lagrange-series-coefficient-add).

## Ramanujan's Lagrange series

Let $p > 0$ and $q > 0$ be real numbers with $p \ne q$, and
let $a$ be a complex number with $|a| \le p^{-p/q} |p - q|^{(p - q)/q}$. Then there is a complex
number $L$ with $a q e^{p L} - e^{q L} + 1 = 0$ such that, for every real number $n$, the series

$$1 + \sum_{k=1}^{\infty} \frac{n a^k}{k!} \prod_{j=1}^{k-1} (n + k p - j q)$$

converges unconditionally to $e^{n L}$.

Proof: The argument uses the Hagen--Rothe convolution, a Stirling-type coefficient bound uniform
through the boundary circle, and a continuous exponential lift.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 14, formulas (14.1)--(14.5), printed pp. 70--71 / PDF pp. 80--81; attribution on printed p. 72 / PDF p. 82.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry14LagrangeSeries.ramanujan_part1_ch3_entry14_lagrange_series`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry14LagrangeSeries.lean, line 1925](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry14LagrangeSeries.lean#L1925). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/lagrange-inversion-series/index.html#ramanujan-part1-ch3-entry14-lagrange-ser).

## Ramanujan's exponential series for powers of two

Let $m$ and $n$ be real numbers with
$0 < n \le 2$. Then the series

$$1 + \sum_{k=1}^{\infty} \frac{m}{2^{k n} \, k!} \prod_{j=1}^{k-1} (m + k n - j)$$

converges unconditionally to $2^m$.

Proof: Following Berndt and the generalized binomial series of Graham, Knuth, and Patashnik,
the series is realized as $B_n(z)^m$, where $B_n = 1 + z B_n^n$; root selection at
$z = 2^{-n}$, with the endpoint supplied by Entry 14's Catalan-power series, gives $B_n = 2$.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 15, Example 1, printed pp. 73-75 / PDF pp. 83-85.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry15Example1ExponentialSeries.ramanujan_part1_ch3_entry15_example1_exponential_series`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry15Example1ExponentialSeries.lean, line 1771](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry15Example1ExponentialSeries.lean#L1771). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/lagrange-inversion-series/index.html#ramanujan-part1-ch3-entry15-example1-exp).

## Ramanujan's inverse series for $u - \log u$

There exist a real number $r > 0$ and real
coefficients $b_0, b_1, b_2, \dots$ with $b_0 = 1$, $b_1 = -1$, $b_2 = 1/3$, $b_3 = -1/36$ and
$b_4 = -1/270$ such that the power series $\sum_k b_k x^k$ is summable for every real $x$ with
$|x| < r$, and for every real $x$ with $0 < x < r$ the sum $u$ of this series satisfies
$0 < u < 1$ and $u - \log u = 1 + x^2/2$, and the series $\sum_{j \ge 2} (1 - u)^j / j$ converges
unconditionally to $x^2/2$.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 15, local inverse-series clause, printed p. 73 / PDF p. 83.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry15InverseSeries.ramanujan_part1_ch3_entry15_inverse_series`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry15InverseSeries.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry15InverseSeries.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/lagrange-inversion-series/index.html#ramanujan-part1-ch3-entry15-inverse-seri).

## Ramanujan's tree-function series (Chapter 3, Entry 15)

Let $x$ and $u$ be real numbers
with $0 < u < 1$ and $u - \log u = 1 + x^2/2$. Then the series

$$\sum_{k=0}^{\infty} \frac{(k+1)^{k-1}}{k!}\, e^{-k(1 + x^2/2)}$$

converges to $u\, e^{1 + x^2/2}$.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 15, formulas (15.1)-(15.2), printed p. 73; scan PDF p. 83.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry15Treeseries.ramanujan_part1_ch3_entry15_treeseries`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry15Treeseries.lean, line 1084](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry15Treeseries.lean#L1084). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/lagrange-inversion-series/index.html#ramanujan-part1-ch3-entry15-treeseries).

## Taylor coefficients of the solution of $x^x = a^a e^h$ (Chapter 3, Entry 17)

For every
real number $a > 1/e$ there exist a real number $R > 0$ and a function
$x : \mathbb{R} \to \mathbb{R}$, analytic at $0$, with $x(0) = a$, such that $x(h) > 0$ and
$x(h)^{x(h)} = a^a e^h$ for all real $h$ with $|h| < R$, and such that the numbers
$A_k = (-a)^{k-1} x^{(k)}(0)$ for $k \ge 1$ satisfy, for every integer $r \ge 2$,

$$A_r = \frac{(r - 2)\, A_{r-1} + \sum_{k=1}^{r-1} \binom{r-1}{k} A_k A_{r-k}}{1 + \log a}.$$

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, corrected Entry 17, formulas (17.1)--(17.7), printed pp. 81--83 / PDF pp. 91--93.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry17.ramanujan_part1_ch3_entry17`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry17.lean, line 623](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry17.lean#L623). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/lagrange-inversion-series/index.html#ramanujan-part1-ch3-entry17).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lagrange inversion series](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/lagrange-inversion-series/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/sequences-and-series/power-series/lagrange-inversion-series)
