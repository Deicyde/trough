---
declaration: section
origin: cited
lean: MetaMathlibExt.glaisherKinkelinConstant, MetaMathlibExt.log_glaisherKinkelinConstant, MetaMathlibExt.factorialProductConstant, MetaMathlibExt.log_factorialProductConstant_one, MetaMathlibExt.factorialProductConstant_pos, MetaMathlibExt.factorialProductComparison, MetaMathlibExt.factorialProductComparison_one, MetaMathlibExt.binomialProductComparison
statement: formalized
---

# Products of factorials and binomial coefficients

19 results, 9 proved and 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html).

## Glaisher–Kinkelin constant

The Glaisher–Kinkelin constant is the real number

$$A = \exp\left(\frac{1}{12} - \operatorname{Re} \zeta'(-1)\right),$$

where $\zeta'$ is the complex derivative of the Riemann zeta function $\zeta$. Since $\zeta'(-1)$
is real, $\log A = \frac{1}{12} - \zeta'(-1)$.

## Sources

- Bernd C. Kellner, *Asymptotic Products of Binomial and Multinomial Coefficients Revisited*, INTEGERS 24 (2024), Article A59, Section 2.

Formalized by `MetaMathlibExt.glaisherKinkelinConstant`, a definition declared in [WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html#glaisher-kinkelin-constant).

## Logarithm of the Glaisher–Kinkelin constant

The Glaisher–Kinkelin constant $A$ satisfies
$\log A = \frac{1}{12} - \operatorname{Re} \zeta'(-1)$, where $\zeta'$ is the complex derivative
of the Riemann zeta function.

## Sources

- Bernd C. Kellner, *Asymptotic Products of Binomial and Multinomial Coefficients Revisited*, INTEGERS 24 (2024), Article A59, Section 2.

Formalized by `MetaMathlibExt.log_glaisherKinkelinConstant`, a theorem declared in [WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html#log-glaisher-kinkelin-constant).

## Factorial-product constants

For a natural number $k \ge 1$, the constant $F_k$ is the
positive real number defined by

$$\log F_k = \frac{k}{4} \log(2\pi) - \frac{k^2+1}{k} \log A + \frac{1 - \log k}{12k} -
\sum_{\nu=1}^{k-1} \frac{\nu}{k} \log \Gamma\left(\frac{\nu}{k}\right),$$

where $A$ is the Glaisher–Kinkelin constant and $\Gamma$ is the gamma function. For $k = 0$ the
definition gives $F_0 = 1$.

The constant $F_k$ appears in the asymptotic formula for $\prod_{\nu=1}^{n} (k\nu)!$ as
$n \to \infty$; that formula is a separate statement.

## Sources

- Bernd C. Kellner, *Asymptotic Products of Binomial and Multinomial Coefficients Revisited*, INTEGERS 24 (2024), Article A59, equation (3) (Kellner 2009, Theorems 12 and 13).

Formalized by `MetaMathlibExt.factorialProductConstant`, a definition declared in [WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html#factorial-product-constant).

## Logarithm of the first factorial product constant

The factorial product constant $F_1$
satisfies $\log F_1 = \frac{1}{4} \log(2\pi) + \frac{1}{12} - 2 \log A$, where $A$ is the
Glaisher–Kinkelin constant.

Equivalently, $F_1 = (2\pi)^{1/4} e^{1/12} A^{-2}$.

## Sources

- Bernd C. Kellner, *Asymptotic Products of Binomial and Multinomial Coefficients Revisited*, INTEGERS 24 (2024), Article A59, Table 1.

Formalized by `MetaMathlibExt.log_factorialProductConstant_one`, a theorem declared in [WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html#log-factorial-product-constant-one).

## Positivity of the factorial-product constants

For every natural number $k$, the
factorial-product constant $F_k$ is positive.

## Sources

- Bernd C. Kellner, *Asymptotic Products of Binomial and Multinomial Coefficients Revisited*, INTEGERS 24 (2024), Article A59, Section 2.

Formalized by `MetaMathlibExt.factorialProductConstant_pos`, a theorem declared in [WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html#factorial-product-constant-pos).

## Comparison function for products of factorials

For a natural number $k$, the comparison
function $P_k \colon \mathbb{R} \to \mathbb{R}$ is defined by

$$P_k(x) = (k^k)^{x(x+1)/2} \left(\frac{2\pi k x}{e}\right)^{x/2} x^{(3k+1)/(12k)}.$$

## Sources

- Bernd C. Kellner, *Asymptotic Products of Binomial and Multinomial Coefficients Revisited*, INTEGERS 24 (2024), Article A59, Theorem 5.

Formalized by `MetaMathlibExt.factorialProductComparison`, a definition declared in [WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html#factorial-product-comparison).

## Value of the factorial-product comparison function at $1$

For every natural number
$k$, the factorial-product comparison function $P_k$ satisfies $P_k(1) = k^k (2\pi k/e)^{1/2}$.

## Sources

- Bernd C. Kellner, *Asymptotic Products of Binomial and Multinomial Coefficients Revisited*, INTEGERS 24 (2024), Article A59, Theorem 5.

Formalized by `MetaMathlibExt.factorialProductComparison_one`, a theorem declared in [WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html#factorial-product-comparison-one).

## Comparison function for products of binomial coefficients

For natural numbers $a$ and
$b$, let $c = a - b$ if $b \le a$ and $c = 0$ otherwise. The comparison function
$P_{a,b} \colon \mathbb{R} \to \mathbb{R}$ is defined by

$$P_{a,b}(x) = \left(\frac{a^a}{b^b c^c}\right)^{x(x+1)/2} x^{(1/a - a/(bc))/12 - 1/4} \Big/
\left(\frac{2\pi}{e} \cdot \frac{bc}{a} \cdot x\right)^{x/2}.$$

## Sources

- Bernd C. Kellner, *Asymptotic Products of Binomial and Multinomial Coefficients Revisited*, INTEGERS 24 (2024), Article A59, Theorem 6.

Formalized by `MetaMathlibExt.binomialProductComparison`, a definition declared in [WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html#binomial-product-comparison).

## Value of the binomial-product comparison function at $1$

For natural numbers $a$ and
$b$, let $c = a - b$ if $b \le a$ and $c = 0$ otherwise. Then the binomial-product comparison
function $P_{a,b}$ satisfies

$$P_{a,b}(1) = \frac{a^a / (b^b c^c)}{\bigl((2\pi/e)(bc/a)\bigr)^{1/2}}.$$

## Sources

- Bernd C. Kellner, *Asymptotic Products of Binomial and Multinomial Coefficients Revisited*, INTEGERS 24 (2024), Article A59, Theorem 6.

Formalized by `MetaMathlibExt.binomialProductComparison_one`, a theorem declared in [WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html#binomial-product-comparison-one).

## Asymptotics of products of factorials of multiples

Let $k \ge 1$ be a natural number, let
$F_k$ be the $k$-th factorial product constant and $A$ the Glaisher–Kinkelin constant. As
$n \to \infty$, the ratio of $\prod_{\nu=1}^{n} (k\nu)!$ to

$$A^k (2\pi)^{1/4} \left(k e^{-3/2} n\right)^{k n(n+1)/2}
\left(2\pi k e^{k/2-1} n\right)^{n/2} n^{(k^2+3k+1)/(12k)}$$

tends to $F_k$.

The divergent asymptotic expansion (4) of the source is not part of this statement.

## Sources

- Bernd C. Kellner, *Asymptotic Products of Binomial and Multinomial Coefficients Revisited*, INTEGERS 24 (2024), Article A59, Theorem 1 (Kellner 2009, Theorems 12 and 13).

Stated but not proved: `MetaMathlibExt.tendsto_prod_factorial_mul_div` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html#tendsto-prod-factorial-mul-div).

## The factorial-product constants decrease strictly to $1$

The sequence
$(F_k)_{k \ge 1}$ of factorial-product constants is strictly decreasing, and $F_k \to 1$ as
$k \to \infty$.

## Sources

- Bernd C. Kellner, *Asymptotic Products of Binomial and Multinomial Coefficients Revisited*, INTEGERS 24 (2024), Article A59, Corollary 2.

Stated but not proved: `MetaMathlibExt.factorialProductConstant_strictAnti_tendsto_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html#factorial-product-constant-strict-anti-t).

## Bounds for $1/a + 1/b - 1/(a+b)$

Let $a$ and $b$ be natural numbers with $a, b \ge 1$
and $a + b \ge 3$, and put $g(a,b) = 1/a + 1/b - 1/(a+b)$. Then $0 < g(a,b) \le 7/6$.

## Sources

- Bernd C. Kellner, *Asymptotic Products of Binomial and Multinomial Coefficients Revisited*, INTEGERS 24 (2024), Article A59, Lemma 3.

Stated but not proved: `MetaMathlibExt.inv_add_inv_sub_inv_add_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html#inv-add-inv-sub-inv-add-bounds).

## Bounds for the binomial-product constants

Let $a$ and $b$ be natural numbers with
$1 \le b < a$, and let $F_k$ denote the factorial-product constants. Then
$c_{a,b} = F_a / (F_b F_{a-b})$ satisfies

$$\frac{F_2}{F_1^2} \le c_{a,b} < 1,$$

that is, $c_{2,1} \le c_{a,b} < 1$.

## Sources

- Bernd C. Kellner, *Asymptotic Products of Binomial and Multinomial Coefficients Revisited*, INTEGERS 24 (2024), Article A59, Lemma 4.

Stated but not proved: `MetaMathlibExt.factorialProductConstant_ratio_mem_Ico` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html#factorial-product-constant-ratio-mem-ico).

## Asymptotics of products of multinomial coefficients

Let $r \ge 2$, let
$b_1, \dots, b_r \ge 1$ be natural numbers with $a = b_1 + \dots + b_r$, let $F_k$ denote the
factorial product constants and $P_k$ the factorial comparison functions, and put
$c_{a,b} = F_a / (F_{b_1} \cdots F_{b_r})$. As $m \to \infty$, the ratio of
$\prod_{n=1}^{m} \binom{an}{b_1 n, \dots, b_r n}$ to $P_a(m) / (P_{b_1}(m) \cdots P_{b_r}(m))$
tends to $c_{a,b} (2\pi)^{(1-r)/4}$; moreover $0 < c_{a,b} < 1$.

## Sources

- Bernd C. Kellner, *Asymptotic Products of Binomial and Multinomial Coefficients Revisited*, INTEGERS 24 (2024), Article A59, Theorem 5.

Stated but not proved: `MetaMathlibExt.tendsto_prod_multinomial_div` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html#tendsto-prod-multinomial-div).

## Asymptotics of products of binomial coefficients $\binom{an}{bn}$

Let $a > b \ge 1$ be
natural numbers, let $F_k$ denote the factorial product constants and $P_{a,b}$ the binomial
comparison function, and put $c_{a,b} = F_a / (F_b F_{a-b})$ and
$C_{a,b} = c_{a,b} (2\pi)^{-1/4}$. Then $\prod_{n=1}^{m} \binom{an}{bn} / P_{a,b}(m) \to C_{a,b}$
as $m \to \infty$; moreover $C_{2,1} \le C_{a,b} < (2\pi)^{-1/4}$ and $c_{2,1} \le c_{a,b} < 1$,
where $c_{2,1} = F_2 / F_1^2$ and $C_{2,1} = c_{2,1} (2\pi)^{-1/4}$.

The decimal approximations of the constants are not part of this statement.

## Sources

- Bernd C. Kellner, *Asymptotic Products of Binomial and Multinomial Coefficients Revisited*, INTEGERS 24 (2024), Article A59, Theorem 6.

Stated but not proved: `MetaMathlibExt.tendsto_prod_choose_div` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html#tendsto-prod-choose-div).

## Asymptotics of products of central binomial coefficients and Catalan numbers

Let $A$ be
the Glaisher–Kinkelin constant, let $\mathrm{Cat}_n$ denote the $n$-th Catalan number, and put
$C_{2,1} = 2^{5/24} A^{3/2} / \left((2\pi)^{1/2} e^{1/8}\right)$. As $m \to \infty$, the ratio of
$\prod_{n=1}^{m} \binom{2n}{n}$ to $2^{m^2} (4e/\pi)^{m/2} / m^{m/2 + 3/8}$ tends to $C_{2,1}$,
and the ratio of $\prod_{n=1}^{m} \mathrm{Cat}_n$ to
$2^{m^2} (4e^3/\pi)^{m/2} / m^{3m/2 + 15/8}$ tends to $C_{2,1} (2\pi)^{-1/2}$.

The decimal approximations of the constants are not part of this statement.

## Sources

- Bernd C. Kellner, *Asymptotic Products of Binomial and Multinomial Coefficients Revisited*, INTEGERS 24 (2024), Article A59, Corollary 7.

Stated but not proved: `MetaMathlibExt.tendsto_prod_centralBinom_catalan_div` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html#tendsto-prod-central-binom-catalan-div).

## Asymptotics of the product of a row of Pascal's triangle

Let $F_1$ be the first factorial
product constant and $A$ the Glaisher–Kinkelin constant, and put
$C_{\mathrm{row}} = \left(F_1 (2\pi)^{1/4}\right)^{-1}$. As $n \to \infty$, the ratio of
$\prod_{\nu=0}^{n} \binom{n}{\nu}$ to $e^{n^2/2 + n} / \left((2\pi)^{n/2} n^{n/2 + 1/3}\right)$
tends to $C_{\mathrm{row}}$, and $C_{\mathrm{row}} = A^2 / \left((2\pi)^{1/2} e^{1/12}\right)$.

## Sources

- Bernd C. Kellner, *Asymptotic Products of Binomial and Multinomial Coefficients Revisited*, INTEGERS 24 (2024), Article A59, Theorem 10.

Stated but not proved: `MetaMathlibExt.tendsto_prod_choose_row_div` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html#tendsto-prod-choose-row-div).

## Pascal-row asymptotics as a limit of binomial-product asymptotics

Let $F_k$ denote the
factorial product constants and $P_{a,b}$ the binomial comparison functions, and let $n \ge 1$
be a natural number and $x > 0$ a real number. Then, as $a \to \infty$ through the natural
numbers, $\frac{F_a}{F_1 F_{a-1}} (2\pi)^{-1/4} \to \left(F_1 (2\pi)^{1/4}\right)^{-1}$,
$a^{-n(n+1)/2} \prod_{\nu=1}^{n} \binom{a\nu}{\nu} \to \prod_{\nu=1}^{n} \binom{n}{\nu}$, and
$a^{-x(x+1)/2} P_{a,1}(x) \to e^{x^2/2 + x} / \left((2\pi)^{x/2} x^{x/2 + 1/3}\right)$.

The source does not state the range of $x$; the hypothesis $x > 0$ is added here.

## Sources

- Bernd C. Kellner, *Asymptotic Products of Binomial and Multinomial Coefficients Revisited*, INTEGERS 24 (2024), Article A59, Theorem 11.

Stated but not proved: `MetaMathlibExt.tendsto_binomialProduct_limit_row` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html#tendsto-binomial-product-limit-row).

## Hirschhorn's constant

Let $A$ be the Glaisher–Kinkelin constant and $F_1$ the first
factorial product constant. As $n \to \infty$,

$$n^{-1/12} \prod_{k=1}^{n} \frac{k!}{\sqrt{2\pi k}\,(k/e)^k}
\to \frac{(2\pi)^{1/4} e^{1/12}}{A^2},$$

and this limit equals $F_1$.

Hirschhorn's asymptotic expansion with divergent Bernoulli sums is not part of this statement.

## Sources

- Bernd C. Kellner, *Asymptotic Products of Binomial and Multinomial Coefficients Revisited*, INTEGERS 24 (2024), Article A59, Theorem 12 (Hirschhorn) and the discussion after it.

Stated but not proved: `MetaMathlibExt.tendsto_hirschhorn_constant` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialProductAsymptoticsWanted.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html#tendsto-hirschhorn-constant).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Products of factorials and binomial coefficients](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/special-numbers/binomial-coefficients/products-of-factorials-and-binomial-coefficients)
