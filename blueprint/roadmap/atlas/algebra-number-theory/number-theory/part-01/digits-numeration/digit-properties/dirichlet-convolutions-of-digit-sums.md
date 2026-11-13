---
declaration: section
origin: cited
lean: MetaMathlibExt.digitSumArith, MetaMathlibExt.digitSumArith_apply, MetaMathlibExt.digitSumArith_sq_apply, MetaMathlibExt.trollopeDelangeIntegral, MetaMathlibExt.trollopeDelangeIntegral_zero, MetaMathlibExt.trollopeDelangeSeries, MetaMathlibExt.trollopeDelangeSeries_zero, MetaMathlibExt.trollopeDelangeFluctuation
statement: formalized
---

# Dirichlet convolutions of digit sums

30 results, 22 proved and 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html).

## Digit-sum arithmetic function

For a natural number $q$, $s_q$ is the arithmetic function
that sends $n$ to $s_q(n)$, the sum of the digits of $n$ in base $q$. Its $k$-th Dirichlet power
is the $k$-fold Dirichlet convolution $s_q^{(k)}$, so $s_q^{(1)} = s_q$ and
$s_q^{(k)} = s_q * s_q^{(k-1)}$ for $k \ge 2$.

For $q \le 1$ the base-$q$ digit expansion is degenerate and $s_q(n) = n$.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Section 1 (definition of `s_q` and of `s_q^{(k)}`).

Formalized by `MetaMathlibExt.digitSumArith`, a definition declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-sum-arith).

## Value of the digit-sum arithmetic function

For natural numbers $q$ and $n$, the
base-$q$ digit-sum arithmetic function $s_q$ takes at $n$ the value $s_q(n)$, the sum of the
digits of $n$ in base $q$.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Section 1.

Formalized by `MetaMathlibExt.digitSumArith_apply`, a theorem declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-sum-arith-apply).

## The second digit-sum convolution

For natural numbers $q$ and $n$, the Dirichlet square
$s_q^{(2)} = s_q * s_q$ of the base-$q$ digit-sum function $s_q$ satisfies
$s_q^{(2)}(n) = \sum_{de = n} s_q(d) \, s_q(e)$, where the sum runs over the pairs $(d, e)$ of
positive integers with $de = n$ (there are none for $n = 0$, and then both sides are $0$).

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Section 1 (definition of `s_q^{(2)}`).

Formalized by `MetaMathlibExt.digitSumArith_sq_apply`, a theorem declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-sum-arith-sq-apply).

## Delange's function

For a natural number $q$, Delange's function in base $q$ is the
function of a real number $x$ given by
$g(x) = \int_0^x \left(\lfloor q t \rfloor - q \lfloor t \rfloor - \frac{q - 1}{2}\right) dt$,
where $\lfloor \cdot \rfloor$ is the floor function.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Theorem 1 (definition of `g`).

Formalized by `MetaMathlibExt.trollopeDelangeIntegral`, a definition declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#trollope-delange-integral).

## Delange's function vanishes at zero

For every natural number $q$, Delange's function $g$
in base $q$ satisfies $g(0) = 0$.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Theorem 1.

Formalized by `MetaMathlibExt.trollopeDelangeIntegral_zero`, a theorem declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#trollope-delange-integral-zero).

## Delange's series

For a natural number $q$, let $g$ be Delange's function in base $q$.
Delange's series in base $q$ is the function of a real number $x$ given by
$h(x) = \sum_{r \ge 0} g(q^r x)/q^r$, where the sum is taken to be $0$ when the series is not
summable.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Theorem 1 (definition of `h`).

Formalized by `MetaMathlibExt.trollopeDelangeSeries`, a definition declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#trollope-delange-series).

## Delange's series vanishes at zero

For every natural number $q$, Delange's series $h$ in
base $q$ satisfies $h(0) = 0$.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Theorem 1.

Formalized by `MetaMathlibExt.trollopeDelangeSeries_zero`, a theorem declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#trollope-delange-series-zero).

## Trollope–Delange fluctuation

Let $q$ be a natural number and let $h$ be Delange's series
in base $q$. The Trollope–Delange fluctuation in base $q$ is the function of a real number $x$
given by $F(x) = \frac{q - 1}{2}(1 + \lfloor x \rfloor - x) +
q^{1 + \lfloor x \rfloor - x}\, h(q^{x - \lfloor x \rfloor - 1})$, where $\lfloor x \rfloor$ is
the floor of $x$.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Theorem 1 (definition of `F`).

Formalized by `MetaMathlibExt.trollopeDelangeFluctuation`, a definition declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#trollope-delange-fluctuation).

## Periodicity of the Trollope–Delange fluctuation

For every natural number $q$ and every
real number $x$, the Trollope–Delange fluctuation $F$ in base $q$ satisfies $F(x + 1) = F(x)$.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Theorem 1 (`F` is `1`-periodic).

Formalized by `MetaMathlibExt.trollopeDelangeFluctuation_add_one`, a theorem declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#trollope-delange-fluctuation-add-one).

## Trollope–Delange remainder

Let $q$ be a natural number, write $s_q(n)$ for the sum of the
base-$q$ digits of a natural number $n$ (with $s_q(n) = n$ when $q \le 1$), and let $h$ be
Delange's series in base $q$. For a real number $x$, let $n_x$ be the floor of $x$ when
$x \ge 0$ and $n_x = 0$ when $x < 0$. The remainder of the Trollope–Delange formula is
$J(x) = (1 + n_x - x)\, s_q(n_x) - h(x)$.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Lemma 1 (definition of `J`).

Formalized by `MetaMathlibExt.digitSumRemainder`, a definition declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-sum-remainder).

## The Trollope–Delange remainder vanishes at zero

For every natural number $q$, the
remainder $J$ of the Trollope–Delange formula in base $q$ satisfies $J(0) = 0$.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Lemma 1.

Formalized by `MetaMathlibExt.digitSumRemainder_zero`, a theorem declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-sum-remainder-zero).

## Integral of the Trollope–Delange fluctuation

For a natural number $q$ and a real number
$x$, let $F$ be the Trollope–Delange fluctuation in base $q$. Then $G(x)$ is the real number

$$G(x) = \int_1^x \frac{F(\log u / \log q)}{u} \, du,$$

where the integral is oriented, so that $\int_1^x = -\int_x^1$ when $x < 1$.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Lemma 1 (definition of `G`).

Formalized by `MetaMathlibExt.digitSumFluctuationIntegral`, a definition declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-sum-fluctuation-integral).

## The fluctuation integral vanishes at $1$

For every natural number $q$, let $F$ be the
Trollope–Delange fluctuation in base $q$ and $G(x) = \int_1^x F(\log u / \log q) \, du / u$.
Then $G(1) = 0$.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Lemma 1.

Formalized by `MetaMathlibExt.digitSumFluctuationIntegral_one`, a theorem declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-sum-fluctuation-integral-one).

## Double integral of the Trollope–Delange fluctuation

For a natural number $q$ and a real
number $x$, let $F$ be the Trollope–Delange fluctuation in base $q$. Then $H(x)$ is the real number

$$H(x) = \int_1^x \frac{1}{u} \left( \int_1^u \frac{F(\log v / \log q)}{v} \, dv \right) du,$$

where the integrals are oriented, so that $\int_a^b = -\int_b^a$ when $b < a$.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Lemma 1 (definition of `H`).

Formalized by `MetaMathlibExt.digitSumFluctuationDoubleIntegral`, a definition declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-sum-fluctuation-double-integral).

## The double fluctuation integral vanishes at 1

For every natural number $q$, the double
integral $H(x) = \int_1^x \int_1^u F(\log v / \log q) \, dv/v \, du/u$ of the Trollope–Delange
fluctuation $F$ for base $q$ satisfies $H(1) = 0$.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Lemma 1.

Formalized by `MetaMathlibExt.digitSumFluctuationDoubleIntegral_one`, a theorem declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-sum-fluctuation-double-integral-on).

## Weighted integral of the Trollope–Delange remainder

For a natural number $q$, let $J$
be the remainder of the Trollope–Delange formula in base $q$. For a real number $x$, define
$K(x) = \int_1^x J(u)/u^2 \, du$, an oriented interval integral (so
$K(x) = -\int_x^1 J(u)/u^2 \, du$ when $x < 1$) that is taken to be $0$ when $J(u)/u^2$ is not
integrable on the interval between $1$ and $x$.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Lemma 1 (definition of `K`).

Formalized by `MetaMathlibExt.digitSumRemainderIntegral`, a definition declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-sum-remainder-integral).

## The remainder integral vanishes at $1$

For every natural number $q$, let $J$ be the
remainder of the Trollope–Delange formula in base $q$ and $K(x) = \int_1^x J(u) \, du / u^2$.
Then $K(1) = 0$.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Lemma 1.

Formalized by `MetaMathlibExt.digitSumRemainderIntegral_one`, a theorem declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-sum-remainder-integral-one).

## Double integral of the Trollope–Delange remainder

For a natural number $q$ and a real
number $x$, let $J$ be the remainder of the Trollope–Delange formula in base $q$. Then $L(x)$ is
the real number

$$L(x) = \int_1^x \frac{1}{u} \left( \int_1^u \frac{J(v)}{v^2} \, dv \right) du,$$

where the integrals are oriented, so that $\int_a^b = -\int_b^a$ when $b < a$.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Lemma 1 (definition of `L`).

Formalized by `MetaMathlibExt.digitSumRemainderDoubleIntegral`, a definition declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-sum-remainder-double-integral).

## The double remainder integral vanishes at $1$

For every natural number $q$, let $J$ be
the remainder of the Trollope–Delange formula in base $q$ and
$L(x) = \int_1^x \frac{1}{u} \int_1^u \frac{J(v)}{v^2} \, dv \, du$. Then $L(1) = 0$.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Lemma 1.

Formalized by `MetaMathlibExt.digitSumRemainderDoubleIntegral_one`, a theorem declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-sum-remainder-double-integral-one).

## Digit-convolution coefficients

For a natural number $q$, the base-$q$ digit-convolution
coefficients are the real numbers $a(k)$, $k \ge 0$, given by $a(0) = a(1) = 0$,
$a(2) = \frac{(q - 1)^2}{24 \log^2 q}$ and, for every $k \ge 3$,

$$a(k) = a(k - 1) \cdot \frac{q - 1}{2 \log q}
\sum_{j=0}^{2k-3} \binom{2k-3}{j} \frac{(-1)^j}{j + 2},$$

where $\log$ is the natural logarithm and division by $0$ is read as $0$ (this matters only for
$q \le 1$). The values $a(0)$ and $a(1)$ are placeholders; only $a(k)$ with $k \ge 2$ is used.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Theorem 3 (definition of `a(k)`).

Formalized by `MetaMathlibExt.digitConvolutionCoeff`, a definition declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-convolution-coeff).

## Second digit-convolution coefficient

For every natural number $q$, the base-$q$
digit-convolution coefficient $a(2)$ equals $\frac{(q - 1)^2}{24 \log^2 q}$, with division by
$0$ read as $0$ (this matters only for $q \le 1$).

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Theorem 3.

Formalized by `MetaMathlibExt.digitConvolutionCoeff_two`, a theorem declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-convolution-coeff-two).

## Recurrence for the digit-convolution coefficients

For every natural number $q$ and
every integer $k \ge 2$, the base-$q$ digit-convolution coefficients $a(k)$ satisfy

$$a(k + 1) = a(k) \cdot \frac{q - 1}{2 \log q}
\sum_{j=0}^{2k-1} \binom{2k-1}{j} \frac{(-1)^j}{j + 2},$$

where division by $0$ is read as $0$ (this matters only for $q \le 1$).

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Theorem 3.

Formalized by `MetaMathlibExt.digitConvolutionCoeff_succ`, a theorem declared in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-convolution-coeff-succ).

## Trollope–Delange formula for real $x$

Let $q \ge 2$ be an integer, let $s_q(n)$ denote
the sum of the base-$q$ digits of $n$, and let $F$ be the Trollope–Delange fluctuation and $h$
Delange's series in base $q$. For every real number $x \ge 1$,

$$\sum_{n=1}^{\lfloor x \rfloor} s_q(n) = \frac{q - 1}{2 \log q} \, x \log x +
x F\left(\frac{\log x}{\log q}\right) - h(x) +
(1 + \lfloor x \rfloor - x) \, s_q(\lfloor x \rfloor).$$

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Theorem 1, equation (1).

Stated but not proved: `MetaMathlibExt.digitSum_partialSum_trollopeDelange` is written with `theorem_wanted` in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-sum-partial-sum-trollope-delange).

## Delange's function is eventually bounded

For every natural number $q \ge 2$, Delange's
function $g$ in base $q$ satisfies $g(x) = O(1)$ as $x \to +\infty$.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Lemma 2.

Stated but not proved: `MetaMathlibExt.trollopeDelangeIntegral_isBigO_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#trollope-delange-integral-is-big-o-one).

## Exact formulas for the reciprocal digit sums

Let $q \ge 2$ be an integer and let $s_q(n)$
denote the sum of the base-$q$ digits of $n$. Let $F$ be the Trollope–Delange fluctuation and $J$
the remainder of the Trollope–Delange formula in base $q$, and for real $x$ put
$G(x) = \int_1^x F(\log u / \log q) \, du / u$, $H(x) = \int_1^x G(u) \, du / u$,
$K(x) = \int_1^x J(u) \, du / u^2$ and $L(x) = \int_1^x K(u) \, du / u$. Then for every real
number $x \ge 1$,

$$\sum_{n=1}^{\lfloor x \rfloor} \frac{s_q(n)}{n} = \frac{(q - 1) \log^2 x}{4 \log q} +
\frac{(q - 1) \log x}{2 \log q} + F\left(\frac{\log x}{\log q}\right) + G(x) + \frac{J(x)}{x} +
K(x)$$

and

$$\sum_{n=1}^{\lfloor x \rfloor} \frac{s_q(n) \log n}{n} = \frac{(q - 1) \log^3 x}{6 \log q} +
\frac{(q - 1) \log^2 x}{4 \log q} + \log x \cdot F\left(\frac{\log x}{\log q}\right) +
(\log x - 1) \, G(x) - H(x) + \frac{J(x) \log x}{x} + (\log x - 1) \, K(x) - L(x).$$

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Lemma 1, equations (4) and (5).

Stated but not proved: `MetaMathlibExt.digitSum_reciprocal_sums_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-sum-reciprocal-sums-eq).

## Size bounds for the Trollope–Delange auxiliary functions

Let $q \ge 2$ be an integer.
For base $q$, let $h$ be Delange's series, $F$ the Trollope–Delange fluctuation, $J$ the
remainder of the Trollope–Delange formula, and
$G(x) = \int_1^x F(\log u / \log q) \, du/u$,
$H(x) = \int_1^x \int_1^u F(\log v / \log q) \, dv/v \, du/u$,
$K(x) = \int_1^x J(u) \, du/u^2$ and $L(x) = \int_1^x \int_1^u J(v) \, dv/v^2 \, du/u$.
Then $F$ is bounded on $\mathbb{R}$, and as $x \to \infty$ through the reals, $h(x) = O(1)$,
$J(x) = O(\log x)$, $G(x) = O(\log x)$, $H(x) = O(\log^2 x)$, $K(x) = O(1)$ and
$L(x) = O(\log x)$.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Lemma 3.

Stated but not proved: `MetaMathlibExt.digitSum_auxiliary_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-sum-auxiliary-is-big-o).

## Bound for a weighted sum of the fluctuation

Let $q \ge 2$ be an integer, let $s_q(n)$
denote the sum of the base-$q$ digits of $n$, let $F$ be the Trollope–Delange fluctuation in base
$q$, and let $F_M = \sup_{t \in \mathbb{R}} |F(t)|$ (taken to be $0$ if $|F|$ is unbounded). For
all real numbers $x > 0$ and $y$,

$$\sum_{n=1}^{\lfloor y \rfloor} \frac{s_q(n)}{n} \, F\left(\frac{\log(x/n)}{\log q}\right) \le
F_M \sum_{n=1}^{\lfloor y \rfloor} \frac{s_q(n)}{n}.$$

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Lemma 4.

Stated but not proved: `MetaMathlibExt.digitSum_reciprocal_fluctuation_sum_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-sum-reciprocal-fluctuation-sum-le).

## Reciprocal digit sums weighted by powers of the logarithm

Let $q \ge 2$ and $j \ge 1$ be
integers, and let $s_q(n)$ denote the sum of the base-$q$ digits of $n$. As the real number $x$
tends to infinity,

$$\sum_{n=1}^{\lfloor x \rfloor} \frac{s_q(n)}{n} \log^j n =
\frac{(q - 1) \log^{j+2} x}{2 (j + 2) \log q} + O\left(\log^{j+1} x\right).$$

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Lemma 5.

Stated but not proved: `MetaMathlibExt.digitSum_reciprocal_log_pow_sum_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-sum-reciprocal-log-pow-sum-is-big).

## Partial sums of the second digit-sum convolution

Let $q \ge 2$ be an integer, let
$s_q(n)$ be the sum of the base-$q$ digits of $n$, and let $s_q^{(2)} = s_q * s_q$ be its
Dirichlet square, so $s_q^{(2)}(n) = \sum_{de = n} s_q(d) \, s_q(e)$. Then

$$\sum_{1 \le n \le x} s_q^{(2)}(n) = \frac{(q - 1)^2}{24 \log^2 q} \, x \log^3 x + O(x \log^2 x)$$

as $x \to \infty$ through the reals.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Theorem 2.

Stated but not proved: `MetaMathlibExt.digitSumArith_sq_partialSum_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-sum-arith-sq-partial-sum-is-big-o).

## Partial sums of the iterated digit-sum convolutions

Let $q \ge 2$ be an integer, let
$s_q(n)$ be the sum of the base-$q$ digits of $n$, let $s_q^{(k)}$ be the $k$-fold Dirichlet
convolution $s_q * \cdots * s_q$, and let $a(k)$ be the base-$q$ digit-convolution coefficients.
For every integer $k \ge 2$,

$$\sum_{1 \le n \le x} s_q^{(k)}(n) = a(k) \, x \log^{2k-1} x + O(x \log^{2k-2} x)$$

as $x \to \infty$ through the reals.

## Sources

- Ka Lun Wong and Erdenebileg Erdenebat, *Asymptotics of Partial Sums of Dirichlet Convolutions of Digital Sum Functions in Arbitrary Bases*, INTEGERS 26 (2026), Article A43, Theorem 3, equation (2).

Stated but not proved: `MetaMathlibExt.digitSumArith_pow_partialSum_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DigitSumDirichletConvolutionWanted.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html#digit-sum-arith-pow-partial-sum-is-big-o).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dirichlet convolutions of digit sums](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/digits-numeration/digit-properties/dirichlet-convolutions-of-digit-sums)
