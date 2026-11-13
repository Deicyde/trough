---
declaration: section
origin: cited
lean: MetaMathlibExt.symmetricPeakCount, MetaMathlibExt.symmetricPeakHeightSum, MetaMathlibExt.symmetricValleyCount, MetaMathlibExt.symmetricValleyDepthSum, MetaMathlibExt.symmetricPeakHeightSum_examples, MetaMathlibExt.symmetricValleyDepthSum_examples, MetaMathlibExt.symmetricPeakHeightSum_compositions_genFun, MetaMathlibExt.symmetricPeakHeightSum_compositions_bivariate_genFun
statement: formalized
---

# Symmetric peaks and valleys in compositions

17 results, 6 proved and 11 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/symmetric-peaks-and-valleys-in-compositions/index.html).

## Number of symmetric peaks

For a finite word $w = w_1 w_2 \cdots w_m$ of natural
numbers, a symmetric peak is a factor $w_i w_{i+1} w_{i+2}$ of three consecutive letters with
$w_i = w_{i+2} < w_{i+1}$. The number of symmetric peaks of $w$ is the number of indices $i$
with $1 \le i \le m - 2$ at which $w$ has a symmetric peak (overlapping peaks all count); it
is $0$ when $m < 3$.

## Sources

- Walaa Asakly and Noor Kezil, *The Heights of Symmetric Peaks and the Depths of Symmetric Valleys over Compositions of an Integer*, INTEGERS 26 (2026), Article A65, Section 1 (symmetric peaks).

Formalized by `MetaMathlibExt.symmetricPeakCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/symmetric-peaks-and-valleys-in-compositions/index.html#symmetric-peak-count).

## Sum of the heights of symmetric peaks

For a finite word $w = w_1 w_2 \cdots w_m$ of
natural numbers, a symmetric peak is a factor $w_i w_{i+1} w_{i+2}$ of three consecutive
letters with $w_i = w_{i+2} < w_{i+1}$, and its height is $w_{i+1} - w_i$. The symmetric peak
height sum of $w$ is the sum of the heights of the symmetric peaks of $w$ over all indices $i$
with $1 \le i \le m - 2$ at which one occurs; it is $0$ when $m < 3$.

## Sources

- Walaa Asakly and Noor Kezil, *The Heights of Symmetric Peaks and the Depths of Symmetric Valleys over Compositions of an Integer*, INTEGERS 26 (2026), Article A65, Section 1 (heights of symmetric peaks).

Formalized by `MetaMathlibExt.symmetricPeakHeightSum`, a definition declared in [WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/symmetric-peaks-and-valleys-in-compositions/index.html#symmetric-peak-height-sum).

## Number of symmetric valleys of a word

For a word $w = w_1 w_2 \cdots w_\ell$ of natural
numbers, a symmetric valley is a position $i$ with $1 < i < \ell$ such that $w_{i-1} = w_{i+1}$
and $w_i < w_{i-1}$, that is, a factor $a\,b\,a$ with $b < a$. The symmetric valley count of $w$
is the number of such positions; in particular it is $0$ when $\ell < 3$.

## Sources

- Walaa Asakly and Noor Kezil, *The Heights of Symmetric Peaks and the Depths of Symmetric Valleys over Compositions of an Integer*, INTEGERS 26 (2026), Article A65, Section 1 (symmetric valleys).

Formalized by `MetaMathlibExt.symmetricValleyCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/symmetric-peaks-and-valleys-in-compositions/index.html#symmetric-valley-count).

## Total depth of the symmetric valleys of a word

For a word $w = w_1 w_2 \cdots w_\ell$ of
natural numbers, a symmetric valley is a position $i$ with $1 < i < \ell$ such that
$w_{i-1} = w_{i+1}$ and $w_i < w_{i-1}$; its depth is $w_{i-1} - w_i$. The symmetric valley depth
sum of $w$ is the sum of the depths of all its symmetric valleys; in particular it is $0$ when
$\ell < 3$.

## Sources

- Walaa Asakly and Noor Kezil, *The Heights of Symmetric Peaks and the Depths of Symmetric Valleys over Compositions of an Integer*, INTEGERS 26 (2026), Article A65, Section 1 (depths of symmetric valleys).

Formalized by `MetaMathlibExt.symmetricValleyDepthSum`, a definition declared in [WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/symmetric-peaks-and-valleys-in-compositions/index.html#symmetric-valley-depth-sum).

## Symmetric peak examples among the compositions of 5

The symmetric peak height sums of
the words $1\,3\,1$, $1\,2\,1\,1$, $1\,1\,2\,1$ and $1\,1\,1\,1\,1$ are $2$, $1$, $1$ and $0$
respectively, and the word $1\,3\,1$ has exactly one symmetric peak.

## Sources

- Walaa Asakly and Noor Kezil, *The Heights of Symmetric Peaks and the Depths of Symmetric Valleys over Compositions of an Integer*, INTEGERS 26 (2026), Article A65, example after Corollary 1.

Formalized by `MetaMathlibExt.symmetricPeakHeightSum_examples`, a theorem declared in [WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/symmetric-peaks-and-valleys-in-compositions/index.html#symmetric-peak-height-sum-examples).

## Symmetric valleys in three compositions of eight

The word $2\,1\,2\,1\,2$ has two
symmetric valleys and total symmetric valley depth $2$, the word $3\,1\,3\,1$ has total symmetric
valley depth $2$, and the word $3\,2\,3$ has total symmetric valley depth $1$.

## Sources

- Walaa Asakly and Noor Kezil, *The Heights of Symmetric Peaks and the Depths of Symmetric Valleys over Compositions of an Integer*, INTEGERS 26 (2026), Article A65, example after Corollary 2.

Formalized by `MetaMathlibExt.symmetricValleyDepthSum_examples`, a theorem declared in [WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/symmetric-peaks-and-valleys-in-compositions/index.html#symmetric-valley-depth-sum-examples).

## Generating function of the total symmetric peak height over compositions

For
$n \ge 0$ let $\mathrm{hsp}(n)$ be the sum, over all compositions $c$ of $n$, of the symmetric
peak height sum of the sequence of parts of $c$. Then in $\mathbb{Z}[[x]]$

$$
\left(\sum_{n \ge 0} \mathrm{hsp}(n)\, x^n\right)(1 - 2x)^2 (1 - x^3) = x^4,
$$

that is, $\sum_{n \ge 0} \mathrm{hsp}(n)\, x^n = x^4 / ((1 - 2x)^2 (1 - x^3))$.

## Sources

- Walaa Asakly and Noor Kezil, *The Heights of Symmetric Peaks and the Depths of Symmetric Valleys over Compositions of an Integer*, INTEGERS 26 (2026), Article A65, Lemma 1, (5).

Stated but not proved: `MetaMathlibExt.symmetricPeakHeightSum_compositions_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/symmetric-peaks-and-valleys-in-compositions/index.html#symmetric-peak-height-sum-compositions-g).

## Bivariate generating function of the total symmetric peak height over compositions

For $n, k \ge 0$ let $\mathrm{hsp}(n, k)$ be the sum, over all compositions $c$ of $n$ with
exactly $k$ parts, of the symmetric peak height sum of the sequence of parts of $c$. Then in
the ring $\mathbb{Z}[y][[x]]$ of formal power series in $x$ over $\mathbb{Z}[y]$,

$$
\left(\sum_{n \ge 0} \sum_{k \ge 0} \mathrm{hsp}(n, k)\, y^k x^n\right)
(1 - x^3)(1 - x - yx)^2 = y^3 x^4,
$$

that is, $\sum_{n, k \ge 0} \mathrm{hsp}(n, k)\, x^n y^k = y^3 x^4 / ((1 - x^3)(1 - x - yx)^2)$.

## Sources

- Walaa Asakly and Noor Kezil, *The Heights of Symmetric Peaks and the Depths of Symmetric Valleys over Compositions of an Integer*, INTEGERS 26 (2026), Article A65, Lemma 1.

Stated but not proved: `MetaMathlibExt.symmetricPeakHeightSum_compositions_bivariate_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/symmetric-peaks-and-valleys-in-compositions/index.html#symmetric-peak-height-sum-compositions-b).

## Generating function for the total depth of symmetric valleys over compositions

For
$n \ge 0$, let $\operatorname{dsv}(n)$ be the sum, over all compositions $c$ of $n$, of the total
depth of the symmetric valleys of the sequence of parts of $c$. Then in the ring $\mathbb{Z}[[x]]$
of formal power series,

$$\Big(\sum_{n \ge 0} \operatorname{dsv}(n)\, x^n\Big)(1-2x)^2(1-x^3)(1-x^2)^2 = x^5 - 2x^6 + x^7,$$

that is, $\sum_{n \ge 0} \operatorname{dsv}(n)\, x^n$ equals
$(x^5 - 2x^6 + x^7)/((1-2x)^2(1-x^3)(1-x^2)^2)$.

## Sources

- Walaa Asakly and Noor Kezil, *The Heights of Symmetric Peaks and the Depths of Symmetric Valleys over Compositions of an Integer*, INTEGERS 26 (2026), Article A65, Lemma 2, (11).

Stated but not proved: `MetaMathlibExt.symmetricValleyDepthSum_compositions_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/symmetric-peaks-and-valleys-in-compositions/index.html#symmetric-valley-depth-sum-compositions).

## Closed form for the total symmetric peak height over compositions

For $n \ge 0$ let
$\mathrm{hsp}(n)$ be the sum, over all compositions $c$ of $n$, of the symmetric peak height
sum of the sequence of parts of $c$, and let $\omega_\pm = 1 \pm i\sqrt{3}$. Then for every
$n \ge 0$, as complex numbers,

$$
\mathrm{hsp}(n) = \frac{2^n}{2} \cdot \frac{7n - 24}{49} +
\frac{(-33 - 15 i \sqrt{3})(-2)^n}{441\, \omega_+^{n+1}} +
\frac{(-33 + 15 i \sqrt{3})(-2)^n}{441\, \omega_-^{n+1}} + \frac{1}{3}.
$$

## Sources

- Walaa Asakly and Noor Kezil, *The Heights of Symmetric Peaks and the Depths of Symmetric Valleys over Compositions of an Integer*, INTEGERS 26 (2026), Article A65, Corollary 1, (6).

Stated but not proved: `MetaMathlibExt.symmetricPeakHeightSum_compositions_closed_form` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/symmetric-peaks-and-valleys-in-compositions/index.html#symmetric-peak-height-sum-compositions-c).

## Closed form for the total depth of symmetric valleys over compositions

For $n \ge 0$,
let $\operatorname{dsv}(n)$ be the sum, over all compositions $c$ of $n$, of the total depth of
the symmetric valleys of the sequence of parts of $c$, and write $\omega_\pm = 1 \pm i\sqrt{3}$.
Then, as complex numbers,

$$\operatorname{dsv}(n) = \frac{(-6n+7)(-1)^n}{108} + \frac{2^n(21n-79)}{1323} +
\frac{(-33-15\sqrt{3}\,i)(-2)^n}{441\,\omega_+^{n+1}} +
\frac{(-33+15\sqrt{3}\,i)(-2)^n}{441\,\omega_-^{n+1}} + \frac{1}{12}.$$

## Sources

- Walaa Asakly and Noor Kezil, *The Heights of Symmetric Peaks and the Depths of Symmetric Valleys over Compositions of an Integer*, INTEGERS 26 (2026), Article A65, Corollary 2, (12).

Stated but not proved: `MetaMathlibExt.symmetricValleyDepthSum_compositions_closed_form` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/symmetric-peaks-and-valleys-in-compositions/index.html#symmetric-valley-depth-sum-compositions-2).

## Total symmetric peak height over compositions with a fixed number of parts

For
$n, k \ge 0$ let $\mathrm{hsp}(n, k)$ be the sum, over all compositions $c$ of $n$ with exactly
$k$ parts, of the symmetric peak height sum of the sequence of parts of $c$. If $k > 3$, then
for every $n \ge 0$

$$
\mathrm{hsp}(n, k) = (k - 2) \sum_{m=2}^{n-k+1} \sum_{b=1}^{\min(m-1,\, t_m)}
\binom{n - 2b - m - 1}{k - 4} (m - b),
\qquad t_m = \left\lfloor \frac{n - m - k + 3}{2} \right\rfloor,
$$

where an empty sum is $0$.

## Sources

- Walaa Asakly and Noor Kezil, *The Heights of Symmetric Peaks and the Depths of Symmetric Valleys over Compositions of an Integer*, INTEGERS 26 (2026), Article A65, Theorem 2(a).

Stated but not proved: `MetaMathlibExt.symmetricPeakHeightSum_compositions_length` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/symmetric-peaks-and-valleys-in-compositions/index.html#symmetric-peak-height-sum-compositions-l).

## Total depth of symmetric valleys over compositions with $k > 3$ parts

For natural
numbers $n$ and $k$ with $k > 3$, the sum, over all compositions $c$ of $n$ with exactly $k$
parts, of the total depth of the symmetric valleys of the sequence of parts of $c$ equals

$$(k-2) \sum_{m=1}^{\lfloor (n-k+1)/3 \rfloor} \sum_{b=m+1}^{\lfloor (n-m-(k-3))/2 \rfloor}
\binom{n-2b-m-1}{k-4}(b-m),$$

where a difference of natural numbers that would be negative is read as $0$.

## Sources

- Walaa Asakly and Noor Kezil, *The Heights of Symmetric Peaks and the Depths of Symmetric Valleys over Compositions of an Integer*, INTEGERS 26 (2026), Article A65, Theorem 4(a).

Stated but not proved: `MetaMathlibExt.symmetricValleyDepthSum_compositions_length` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/symmetric-peaks-and-valleys-in-compositions/index.html#symmetric-valley-depth-sum-compositions-3).

## Total depth of symmetric valleys over compositions with three parts

For every natural
number $n$, the sum, over all compositions $c$ of $n$ with exactly three parts, of the total
depth of the symmetric valleys of the sequence of parts of $c$ equals
$\sum_{m=1}^{\lfloor (n-2)/3 \rfloor} d_m$, where $d_m = (n-3m)/2$ if $n - m$ is even and
$d_m = 0$ otherwise.

## Sources

- Walaa Asakly and Noor Kezil, *The Heights of Symmetric Peaks and the Depths of Symmetric Valleys over Compositions of an Integer*, INTEGERS 26 (2026), Article A65, Theorem 4(b).

Stated but not proved: `MetaMathlibExt.symmetricValleyDepthSum_compositions_length_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/symmetric-peaks-and-valleys-in-compositions/index.html#symmetric-valley-depth-sum-compositions-4).

## Expected symmetric peaks and valleys in geometric words

Let $n \ge 2$, let
$0 < p < 1$ and $q = 1 - p$, and let $X_1, \dots, X_n$ be independent random variables, each
geometric on $\{0, 1, 2, \dots\}$ with $\Pr(X_i = k) = q^k p$, and consider the word
$X_1 X_2 \cdots X_n$. The expected number of its symmetric peaks is
$p^2 q (n - 2)/(1 - q^3)$, the expected number of its symmetric valleys is
$p^2 \left(\frac{1}{1 - q^2} - \frac{1}{1 - q^3}\right)(n - 2)$, the expected sum of the
heights of its symmetric peaks is $p q (n - 2)/(1 - q^3)$, and the expected sum of the depths
of its symmetric valleys is $q \left(\frac{p}{1 - q^3} - \frac{1}{(1 + q)^2}\right)(n - 2)$.

## Sources

- Walaa Asakly and Noor Kezil, *The Heights of Symmetric Peaks and the Depths of Symmetric Valleys over Compositions of an Integer*, INTEGERS 26 (2026), Article A65, Theorem 5.

Stated but not proved: `MetaMathlibExt.integral_symmetricPeakValley_geometric` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/symmetric-peaks-and-valleys-in-compositions/index.html#integral-symmetric-peak-valley-geometric).

## Trivariate generating function for symmetric peaks in compositions

For a composition
$c$ write $\ell(c)$ for its number of parts, $\mathrm{sp}(c)$ for the number of symmetric peaks
and $\mathrm{hsp}(c)$ for the symmetric peak height sum of its sequence of parts. In the ring
$\mathbb{Z}[y, q, h][[x]]$ of formal power series in $x$ whose coefficients are polynomials in
$y, q, h$ with integer coefficients,

$$
\sum_{n \ge 0} \sum_{c \models n} x^n y^{\ell(c)} q^{\mathrm{sp}(c)} h^{\mathrm{hsp}(c)} =
\frac{1}{1 - \sum_{a \ge 1} \frac{x^a y}{1 - y^2 x^{2a+1} \left(\frac{qh}{1 - hx} -
\frac{1}{1 - x}\right)}},
$$

where $c \models n$ ranges over the compositions of $n$ and
$\frac{qh}{1 - hx} - \frac{1}{1 - x}$ stands for the series $\sum_{j \ge 0} (q h^{j+1} - 1) x^j$.
Precisely: for every $n \ge 0$ the coefficients of $x^n$ on the two sides agree when the sum
over $a$ is restricted to $1 \le a \le n$ (the terms with $a > n$ do not contribute to them).

## Sources

- Walaa Asakly and Noor Kezil, *The Heights of Symmetric Peaks and the Depths of Symmetric Valleys over Compositions of an Integer*, INTEGERS 26 (2026), Article A65, Theorem 1.

Stated but not proved: `MetaMathlibExt.symmetricPeak_compositions_trivariate_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/symmetric-peaks-and-valleys-in-compositions/index.html#symmetric-peak-compositions-trivariate-g).

## Trivariate generating function for symmetric valleys in compositions

For a composition
$c$ write $\ell(c)$ for its number of parts, $\mathrm{sv}(c)$ for the number of symmetric
valleys and $\mathrm{dsv}(c)$ for the symmetric valley depth sum of its sequence of parts. In
the ring $\mathbb{Z}[y, p, d][[x]]$ of formal power series in $x$ whose coefficients are
polynomials in $y, p, d$ with integer coefficients,

$$
\sum_{n \ge 0} \sum_{c \models n} x^n y^{\ell(c)} p^{\mathrm{sv}(c)} d^{\mathrm{dsv}(c)} =
\frac{1}{1 - \sum_{a \ge 1} \frac{x^a y}{1 - y^2 x^{a+1}
\sum_{b=1}^{a-1} (p d^{a-b} - 1) x^{b-1}}},
$$

where $c \models n$ ranges over the compositions of $n$. Precisely: for every $n \ge 0$ the
coefficients of $x^n$ on the two sides agree when the sum over $a$ is restricted to
$1 \le a \le n$ (the terms with $a > n$ do not contribute to them). The inner sum equals
$p(x^{a-1} - d^{a-1})/(x/d - 1) - (x^{a-1} - 1)/(x - 1)$.

Corrected reading: the paper prints $(p x^{a-1} - d^{a-1})/(x/d - 1)$, with $p$ on the first
term only; that is false (at $n = 3$ it gives the composition $111$ a symmetric valley of depth
$0$). The corrected term $p(x^{a-1} - d^{a-1})/(x/d - 1)$ is the penultimate line of the
paper's proof, $x^a y^2 p d^a ((x/d)^a - x/d)/(x/d - 1)$, and agrees with the paper's
specialization $d = 1$, $(x^{a-1} - 1)(p - 1)/(x - 1)$.

## Sources

- Walaa Asakly and Noor Kezil, *The Heights of Symmetric Peaks and the Depths of Symmetric Valleys over Compositions of an Integer*, INTEGERS 26 (2026), Article A65, Theorem 3.

Stated but not proved: `MetaMathlibExt.symmetricValley_compositions_trivariate_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SymmetricPeaksCompositionsWanted.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/symmetric-peaks-and-valleys-in-compositions/index.html#symmetric-valley-compositions-trivariate).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Symmetric peaks and valleys in compositions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/symmetric-peaks-and-valleys-in-compositions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/integer-compositions/symmetric-peaks-and-valleys-in-compositions)
