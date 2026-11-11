---
declaration: section
origin: cited
lean: MetaMathlibExt.generalizedFactorial, MetaMathlibExt.IsPositiveSequence, MetaMathlibExt.generalizedFactorial_pos, MetaMathlibExt.generalizedBinomialCoefficient, MetaMathlibExt.generalizedBinomialCoefficient_mul_denominator, MetaMathlibExt.totienomialCoefficient, MetaMathlibExt.totienomial_integral_factorization
statement: formalized
proof: formalized
---

# Totienomial coefficients

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/totienomial-coefficients/index.html).

## Generalized factorial

For a sequence $f \colon \mathbb{N} \to \mathbb{N}$ and a natural
number $n$, the generalized factorial of $f$ at $n$ is the product $f(1) f(2) \cdots f(n)$ of
the values $f(i)$ for $1 \le i \le n$; for $n = 0$ it is the empty product $1$.

## Sources

- https://cs.uwaterloo.ca/journals/JIS/VOL19/Edgar/edgar3.tex

Formalized by `MetaMathlibExt.generalizedFactorial`, a definition declared in [MathlibExt/Combinatorics/Enumerative/TotienomialCoefficient.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/TotienomialCoefficient.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/totienomial-coefficients/index.html#generalized-factorial).

## Positive sequence

A sequence $f \colon \mathbb{N} \to \mathbb{N}$ is positive when
$f(i) > 0$ for every $i > 0$; the value $f(0)$ is unrestricted.

This is the condition on $f$ under which the source defines generalized binomial coefficients.

Formalized by `MetaMathlibExt.IsPositiveSequence`, a definition declared in [MathlibExt/Combinatorics/Enumerative/TotienomialCoefficient.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/TotienomialCoefficient.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/totienomial-coefficients/index.html#is-positive-sequence).

## Generalized factorials of positive sequences are positive

Let $f \colon \mathbb{N} \to
\mathbb{N}$ be a positive sequence, that is $f(i) > 0$ for every $i > 0$. Then for every natural
number $n$, the generalized factorial $f(1) f(2) \cdots f(n)$ is positive.

Formalized by `MetaMathlibExt.generalizedFactorial_pos`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/TotienomialCoefficient.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/TotienomialCoefficient.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/totienomial-coefficients/index.html#generalized-factorial-pos).

## Generalized binomial coefficient

Let $f \colon \mathbb{N} \to \mathbb{N}$ be a sequence and
write $k!_f = f(1) f(2) \cdots f(k)$ for its generalized factorial, so that $0!_f = 1$. For
natural numbers $n$ and $m$, the generalized binomial coefficient of $f$ is the rational number

$$\binom{n+m}{n}_f = \frac{(n+m)!_f}{n!_f \, m!_f},$$

which is taken to be $0$ when the denominator is $0$.

When $f(i) > 0$ for every $i > 0$, the setting of the source, the denominator is never $0$ and
this is the source's quotient.

## Sources

- https://cs.uwaterloo.ca/journals/JIS/VOL19/Edgar/edgar3.tex

Formalized by `MetaMathlibExt.generalizedBinomialCoefficient`, a definition declared in [MathlibExt/Combinatorics/Enumerative/TotienomialCoefficient.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/TotienomialCoefficient.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/totienomial-coefficients/index.html#generalized-binomial-coefficient).

## Defining equation of the generalized binomial coefficient

Let $f \colon \mathbb{N} \to
\mathbb{N}$ be a positive sequence, that is $f(i) > 0$ for every $i > 0$, and write
$k!_f = f(1) f(2) \cdots f(k)$ for its generalized factorial. Then for all natural numbers $n$
and $m$, the generalized binomial coefficient $\binom{n+m}{n}_f$, defined as
$(n+m)!_f / (n!_f \, m!_f)$ with division by $0$ giving $0$, satisfies
$\binom{n+m}{n}_f \cdot n!_f \, m!_f = (n+m)!_f$ in $\mathbb{Q}$.

Formalized by `MetaMathlibExt.generalizedBinomialCoefficient_mul_denominator`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/TotienomialCoefficient.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/TotienomialCoefficient.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/totienomial-coefficients/index.html#generalized-binomial-coefficient-mul-den).

## Totienomial coefficient

Let $\varphi$ be Euler's totient function and write
$k!_\varphi = \varphi(1) \varphi(2) \cdots \varphi(k)$. For natural numbers $n$ and $m$, the
totienomial coefficient is the generalized binomial coefficient of $\varphi$, that is the
rational number

$$\binom{n+m}{n}_\varphi = \frac{(n+m)!_\varphi}{n!_\varphi \, m!_\varphi}.$$

Since $\varphi(i) > 0$ for every $i > 0$, the denominator is never $0$.

## Sources

- https://cs.uwaterloo.ca/journals/JIS/VOL19/Edgar/edgar3.tex

Formalized by `MetaMathlibExt.totienomialCoefficient`, a definition declared in [MathlibExt/Combinatorics/Enumerative/TotienomialCoefficient.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/TotienomialCoefficient.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/totienomial-coefficients/index.html#totienomial-coefficient).

## Integrality and prime factorization of totienomial coefficients

For all natural numbers
$n$ and $m$, the totienomial coefficient $\binom{n+m}{n}_\varphi$ of Euler's totient function
$\varphi$ is a natural number, namely

$$\binom{n+m}{n}_\varphi = \prod_{p \le n+m} (p-1)^{c_p} \, p^{v_p(\binom{n+m}{n}) - c_p},$$

where the product runs over the primes $p \le n+m$, $\binom{n+m}{n}$ is the ordinary binomial
coefficient, $v_p$ is the $p$-adic valuation and
$c_p = \lfloor (n+m)/p \rfloor - \lfloor n/p \rfloor - \lfloor m/p \rfloor$.

Both exponents are natural numbers, since $\lfloor n/p \rfloor + \lfloor m/p \rfloor \le
\lfloor (n+m)/p \rfloor$ and $c_p \le v_p(\binom{n+m}{n})$.

## Sources

- Tom Edgar and Michael Z. Spivey, "Multiplicative Functions, Generalized Binomial Coefficients, and Generalized Catalan Numbers", Journal of Integer Sequences 19 (2016), Article 16.1.6, Corollary `totcor`, lines 244-249, <https://cs.uwaterloo.ca/journals/JIS/VOL19/Edgar/edgar3.tex>.

Formalized by `MetaMathlibExt.totienomial_integral_factorization`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/TotienomialCoefficient.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/TotienomialCoefficient.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/totienomial-coefficients/index.html#totienomial-integral-factorization).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Totienomial coefficients](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/totienomial-coefficients/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/totienomial-coefficients)
