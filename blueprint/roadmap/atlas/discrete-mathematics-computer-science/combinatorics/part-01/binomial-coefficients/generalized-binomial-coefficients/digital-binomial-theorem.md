---
declaration: section
origin: cited
lean: MetaMathlibExt.base_b_generalized_digital_binomial_theorem, MetaMathlibExt.binDigitSum, MetaMathlibExt.binDigitSum_zero, MetaMathlibExt.binDigitSum_two_mul, MetaMathlibExt.binDigitSum_two_mul_add_one, MetaMathlibExt.binDigitSum_one, MetaMathlibExt.digital_binomial_theorem_general, MetaMathlibExt.digital_binomial_theorem
statement: formalized
proof: formalized
---

# Digital binomial theorem

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/digital-binomial-theorem/index.html).

## Base-$b$ generalized digital binomial theorem

Let $b \ge 2$, let $N$ and $n$ be natural
numbers with $n < b^N$, and let $x$ and $y$ be real numbers. For a natural number $m$ write
$m_i = \lfloor m / b^i \rfloor \bmod b$ for its $i$-th base-$b$ digit, and write
$z^{\overline{j}} = z(z+1)\cdots(z+j-1)$ for the rising factorial. Then

$$\prod_{i=0}^{N-1} \frac{(x+y)^{\overline{n_i}}}{n_i!} = \sum_{m} \left(\prod_{i=0}^{N-1}
\frac{x^{\overline{m_i}}}{m_i!}\right) \left(\prod_{i=0}^{N-1}
\frac{y^{\overline{(n-m)_i}}}{(n-m)_i!}\right),$$

where the sum runs over the natural numbers $m \le n$ with $m_i \le n_i$ for every $i < N$.

## Sources

- Hieu D. Nguyen, "A Generalization of the Digital Binomial Theorem," Journal of Integer Sequences 18 (2015), Article 15.5.7, Theorem, equation (eq:digital-binomial-theorem-non-binary), lines 122–127, https://cs.uwaterloo.ca/journals/JIS/VOL18/Nguyen/nguyen6.tex

Formalized by `MetaMathlibExt.base_b_generalized_digital_binomial_theorem`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BaseBGeneralizedDigitalBinomial.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/BaseBGeneralizedDigitalBinomial.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/digital-binomial-theorem/index.html#base-b-generalized-digital-binomial-theo).

## Binary digit sum

For a natural number $n$, the binary digit sum $s(n)$ is the sum of the
digits of $n$ in base $2$, that is, the number of ones in the binary expansion of $n$.

Formalized by `MetaMathlibExt.binDigitSum`, a definition declared in [MathlibExt/Combinatorics/Enumerative/DigitalBinomialTheorem.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/DigitalBinomialTheorem.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/digital-binomial-theorem/index.html#bin-digit-sum).

## Binary digit sum of zero

The binary digit sum of $0$ is $0$.

Formalized by `MetaMathlibExt.binDigitSum_zero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/DigitalBinomialTheorem.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/DigitalBinomialTheorem.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/digital-binomial-theorem/index.html#bin-digit-sum-zero).

## Binary digit sum of an even number

For every natural number $k$, the binary digit sum of
$2k$ equals the binary digit sum of $k$: doubling appends the binary digit $0$.

Formalized by `MetaMathlibExt.binDigitSum_two_mul`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/DigitalBinomialTheorem.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/DigitalBinomialTheorem.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/digital-binomial-theorem/index.html#bin-digit-sum-two-mul).

## Binary digit sum of an odd number

For every natural number $k$, the binary digit sum of
$2k + 1$ is one more than the binary digit sum of $k$: the binary expansion of $2k + 1$ is that
of $k$ followed by the digit $1$.

Formalized by `MetaMathlibExt.binDigitSum_two_mul_add_one`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/DigitalBinomialTheorem.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/DigitalBinomialTheorem.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/digital-binomial-theorem/index.html#bin-digit-sum-two-mul-add-one).

## Binary digit sum of one

The binary digit sum of $1$ is $1$.

Formalized by `MetaMathlibExt.binDigitSum_one`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/DigitalBinomialTheorem.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/DigitalBinomialTheorem.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/digital-binomial-theorem/index.html#bin-digit-sum-one).

## Digital binomial theorem over a commutative semiring

Let $s(m)$ denote the binary digit sum
of a natural number $m$. For every natural number $n$ and all elements $x$, $y$ of a commutative
semiring, $(x + y)^{s(n)}$ equals the sum of $x^{s(m)} y^{s(n - m)}$ over all $m$ with
$0 \le m \le n$ and $s(m) + s(n - m) = s(n)$.

Formalized by `MetaMathlibExt.digital_binomial_theorem_general`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/DigitalBinomialTheorem.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/DigitalBinomialTheorem.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/digital-binomial-theorem/index.html#digital-binomial-theorem-general).

## Digital binomial theorem

Let $s(m)$ denote the binary digit sum of a natural number $m$. For
every natural number $n$ and all elements $x$, $y$ of a commutative ring, $(x + y)^{s(n)}$ equals
the sum of $x^{s(m)} y^{s(n - m)}$ over all $m$ with $0 \le m \le n$ and
$s(m) + s(n - m) = s(n)$.

The condition $s(m) + s(n - m) = s(n)$ says that adding $m$ and $n - m$ in binary produces no
carries; equivalently, $m$ has a binary digit $1$ only in positions where $n$ has one.

## Sources

- Hieu D. Nguyen, "A Generalization of the Digital Binomial Theorem," Journal of Integer Sequences 18 (2015), Article 15.5.7, Theorem, equation, lines 107–113, https://cs.uwaterloo.ca/journals/JIS/VOL18/Nguyen/nguyen6.tex

Formalized by `MetaMathlibExt.digital_binomial_theorem`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/DigitalBinomialTheorem.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/DigitalBinomialTheorem.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/digital-binomial-theorem/index.html#digital-binomial-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Digital binomial theorem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/digital-binomial-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/digital-binomial-theorem)
