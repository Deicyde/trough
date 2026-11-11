---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry12SummableSuccN.ramanujan_part1_ch3_entry12_summable_succ_n_general, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry12SummableSuccN.ramanujan_part1_ch3_entry12_summable_succ_n, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry12.ramanujan_part1_ch3_entry12, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry12SummableRN.ramanujan_part1_ch3_entry12_summable_r_n, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry16.ramanujan_part1_ch3_entry16, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry16Corollary1JensenSeries.ramanujan_part1_ch3_entry16_corollary1_jensen_series, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry16PsiSeries.ramanujan_part1_ch3_entry16_psi_series
statement: formalized
proof: formalized
---

# Abel-type exponential series

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/abel-type-exponential-series/index.html).

## Absolute convergence of the shifted series in Entry 12 for every $n$

Let $r$ be an
integer and let $n$ and $a$ be complex numbers with $|a| > e$, or with $a = e$ and $r \le -2$.
Then

$$\sum_{k=0}^{\infty} \left| \frac{(n+k)^{r+1+k}}{a^k\, k!} \right| < \infty,$$

where integer powers of complex numbers follow the convention $0^m = 0$ for $m < 0$.

Unlike the version that assumes $n + k \ne 0$ whenever $k \ge 0$ and $r + k < 0$, nothing is
assumed about $n$. At an index where $n + k = 0$ and the exponent $r + 1 + k$ is negative, the
term is $0^{r+1+k} = 0$, whereas the source's term is undefined there. Summability depends only
on the tail, where every exponent is nonnegative.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry12SummableSuccN.ramanujan_part1_ch3_entry12_summable_succ_n_general`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry12SummableSuccN.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry12SummableSuccN.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/abel-type-exponential-series/index.html#ramanujan-part1-ch3-entry12-summable-suc).

## Absolute convergence of the shifted series in Entry 12

Let $r$ be an integer and let $n$
and $a$ be complex numbers. Suppose that $|a| > e$, or that $a = e$ and $r \le -2$, and that
$n + k \ne 0$ for every integer $k \ge 0$ with $r + k < 0$. Then

$$\sum_{k=0}^{\infty} \left| \frac{(n+k)^{r+1+k}}{a^k\, k!} \right| < \infty.$$

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, definition (12.1) and Entry 12, printed pp. 66-67 / PDF pp. 76-77.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry12SummableSuccN.ramanujan_part1_ch3_entry12_summable_succ_n`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry12SummableSuccN.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry12SummableSuccN.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/abel-type-exponential-series/index.html#ramanujan-part1-ch3-entry12-summable-suc-2).

## Ramanujan's recurrence for the series in Entry 12

Fix a complex number $a$. For an
integer $r$ and a complex number $n$, let

$$F_r(n) = \sum_{k=0}^{\infty} \frac{(n+k)^{r+k}}{a^k\, k!},$$

where the sum is taken to be $0$ if the series is not summable. Suppose that $|a| > e$, or that
$a = e$ and $r \le -2$, and that $n + k \ne 0$ for every natural number $k$ with $r + k < 0$.
Then

$$F_{r+1}(n) = n F_r(n) + \frac{1}{a} F_{r+1}(n+1).$$

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, definition (12.1) and Entry 12, printed pp. 66-67 / PDF pp. 76-77.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry12.ramanujan_part1_ch3_entry12`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry12.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry12.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/abel-type-exponential-series/index.html#ramanujan-part1-ch3-entry12).

## Absolute convergence of the series in Entry 12

Let $r$ be an integer and let $n$ and $a$
be complex numbers. Suppose that $|a| > e$, or that $a = e$ and $r \le -2$, and that $n + k \ne 0$
for every natural number $k$ with $r + k < 0$. Then

$$\sum_{k=0}^{\infty} \left| \frac{(n+k)^{r+k}}{a^k\, k!} \right| < \infty.$$

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, definition (12.1) and Entry 12, printed pp. 66-67 / PDF pp. 76-77.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry12SummableRN.ramanujan_part1_ch3_entry12_summable_r_n`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry12SummableRN.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry12SummableRN.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/abel-type-exponential-series/index.html#ramanujan-part1-ch3-entry12-summable-r-n).

## Ramanujan's three-term recurrence (Chapter 3, Entry 16(a))

Let $a$, $x$, $n$ be complex
numbers and $r$ an integer, where $x \ne 0$ and $x = a \log x$ with $\log$ the principal branch of
the complex logarithm. Suppose that $|a| > e$, or that $a = e$ and $r \le -2$, and that
$n + k \ne 0$ for every natural number $k$ with $r + k < 0$. For an integer $s$ and a complex
number $m$ put

$$\varphi(s, m) = e^{-m \log x} \sum_{k=0}^{\infty} \frac{(m + k)^{s + k}}{a^k\, k!};$$

the three series used below converge absolutely under these hypotheses. Then

$$n\, \varphi(r, n) = \varphi(r + 1, n) - \log x \cdot \varphi(r + 1, n + 1).$$

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, definition (12.1) printed p. 66 / PDF p. 76, Entry 12 p. 67 / PDF p. 77, and Entry 16(a) p. 78 / PDF p. 88. The series is `Entry12.F`, and the recurrence is `Entry12.ramanujan_part1_ch3_entry12` multiplied by `exp (-n * log x)`.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry16.ramanujan_part1_ch3_entry16`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry16.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry16.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/abel-type-exponential-series/index.html#ramanujan-part1-ch3-entry16).

## Jensen's series (Chapter 3, Entry 16, Corollary 1)

Let $\rho$ be a positive real number
with $\rho e^{\rho + 1} = 1$, let $n$ be a real number with $-\rho < n < 1$, and let $x$ be a
complex number. Then the series

$$\sum_{k=0}^{\infty} \frac{(x + kn)^k}{k!\, e^{kn}}$$

converges unconditionally to $e^x / (1 - n)$.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Corollary 1, formula (16.6), printed pp. 80--81 / PDF pp. 90--91.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry16Corollary1JensenSeries.ramanujan_part1_ch3_entry16_corollary1_jensen_series`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry16Corollary1JensenSeries.lean, line 1490](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry16Corollary1JensenSeries.lean#L1490). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/abel-type-exponential-series/index.html#ramanujan-part1-ch3-entry16-corollary1-j).

## Ramanujan's $\psi$-series (Chapter 3, Entry 16)

For natural numbers $r$, $k$ and a complex
number $n$ define $\psi(r, k, n)$ recursively by $\psi(0, 1, n) = 1$, $\psi(0, k, n) = 0$ for
$k \ne 1$, and

$$\psi(r + 1, k, n) = (n - r - k)\, \psi(r, k, n) + (r + k - 1)\, \psi(r, k - 1, n),$$

where the last term is read as $0$ when $k = 0$. Let $r$ be a natural number and let $n$, $u$ be
complex numbers with $|u e^{1-u}| < 1$ and $|u| < 1$. Then the series

$$\sum_{j=0}^{\infty} \frac{(n + j)^{r+j}\, e^{-u(n+j)}\, u^j}{j!}$$

converges unconditionally to

$$\sum_{k=1}^{r+1} \frac{\psi(r, k, n)}{(1 - u)^{r+k}}.$$

The hypothesis $|u| < 1$ selects the component of $\{u : |u e^{1-u}| < 1\}$ containing $0$;
given $|u e^{1-u}| < 1$, it is equivalent to $\operatorname{Re} u < 1$. On the other component
the series converges to a different value.

Proof: Entry 12 gives absolute and locally uniform convergence, and termwise
differentiation gives the recurrence in Berndt (16.4)-(16.5). The Jensen-series
base case from Berndt (16.6) extends to the star-convex domain by analytic uniqueness.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, construction and formulas (16.4)-(16.5), printed pp. 78-79 / PDF pp. 88-89.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry16PsiSeries.ramanujan_part1_ch3_entry16_psi_series`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry16PsiSeries.lean, line 773](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry16PsiSeries.lean#L773). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/abel-type-exponential-series/index.html#ramanujan-part1-ch3-entry16-psi-series).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Abel-type exponential series](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/abel-type-exponential-series/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/sequences-and-series/power-series/abel-type-exponential-series)
