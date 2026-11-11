---
declaration: section
origin: cited
lean: MetaMathlibExt.gcdUnitary, MetaMathlibExt.gcdUnitary_comm, MetaMathlibExt.gcdUnitary_zero_left, MetaMathlibExt.gcdUnitary_zero_right, MetaMathlibExt.le_gcdUnitary, MetaMathlibExt.gcdUnitary_mem_unitaryDivisors, MetaMathlibExt.gcdUnitary_dvd_left, MetaMathlibExt.gcdUnitary_dvd_right
statement: formalized
proof: formalized
---

# Biunitary divisors

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html).

## Greatest common unitary divisor

For natural numbers $a$ and $b$, $\gcd_1(a, b)$ is the
largest natural number that is a unitary divisor of both $a$ and $b$, where a unitary divisor of
$n$ is a divisor $d$ of $n \neq 0$ with $\gcd(d, n / d) = 1$. If $a = 0$ or $b = 0$, there is no
common unitary divisor and $\gcd_1(a, b) = 0$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Section 1 (after Wall).

Formalized by `MetaMathlibExt.gcdUnitary`, a definition declared in [MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html#gcd-unitary).

## Symmetry of the greatest common unitary divisor

For all natural numbers $a$ and $b$, the
greatest common unitary divisor satisfies $\gcd_1(a, b) = \gcd_1(b, a)$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Section 1 (after Wall).

Formalized by `MetaMathlibExt.gcdUnitary_comm`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html#gcd-unitary-comm).

## Greatest common unitary divisor with zero on the left

For every natural number $b$, the
greatest common unitary divisor satisfies $\gcd_1(0, b) = 0$, since $0$ has no unitary divisors.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Section 1 (after Wall).

Formalized by `MetaMathlibExt.gcdUnitary_zero_left`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html#gcd-unitary-zero-left).

## Greatest common unitary divisor with zero on the right

For every natural number $a$,
the greatest common unitary divisor satisfies $\gcd_1(a, 0) = 0$, since $0$ has no unitary
divisors.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Section 1 (after Wall).

Formalized by `MetaMathlibExt.gcdUnitary_zero_right`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html#gcd-unitary-zero-right).

## Common unitary divisors are at most the greatest one

For natural numbers $a$, $b$ and $d$,
if $d$ is a unitary divisor of both $a$ and $b$, then $d \le \gcd_1(a, b)$, where $\gcd_1(a, b)$ is
the greatest common unitary divisor of $a$ and $b$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Section 1 (after Wall).

Formalized by `MetaMathlibExt.le_gcdUnitary`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html#le-gcd-unitary).

## The greatest common unitary divisor is a common unitary divisor

For positive natural
numbers $a$ and $b$, the greatest common unitary divisor $\gcd_1(a, b)$ is a unitary divisor of
$a$ and a unitary divisor of $b$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Section 1 (after Wall).

Formalized by `MetaMathlibExt.gcdUnitary_mem_unitaryDivisors`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html#gcd-unitary-mem-unitary-divisors).

## The greatest common unitary divisor divides its first argument

For positive natural
numbers $a$ and $b$, the greatest common unitary divisor $\gcd_1(a, b)$ divides $a$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Section 1 (after Wall).

Formalized by `MetaMathlibExt.gcdUnitary_dvd_left`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html#gcd-unitary-dvd-left).

## The greatest common unitary divisor divides its second argument

For positive natural
numbers $a$ and $b$, the greatest common unitary divisor $\gcd_1(a, b)$ divides $b$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Section 1 (after Wall).

Formalized by `MetaMathlibExt.gcdUnitary_dvd_right`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html#gcd-unitary-dvd-right).

## Positivity of the greatest common unitary divisor

For positive natural numbers $a$ and
$b$, the greatest common unitary divisor $\gcd_1(a, b)$ is positive.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Section 1 (after Wall).

Formalized by `MetaMathlibExt.gcdUnitary_pos`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html#gcd-unitary-pos).

## Biunitary divisors

For a natural number $n$, the biunitary divisors of $n$ are the
divisors $d$ of $n$ with $\gcd_1(d, n/d) = 1$, where $\gcd_1(a, b)$ denotes the greatest common
unitary divisor of $a$ and $b$. For $n = 0$ the set is empty.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Section 1 (after Wall).

Formalized by `MetaMathlibExt.biunitaryDivisors`, a definition declared in [MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html#biunitary-divisors).

## Biunitary divisor sum

For a natural number $n$, $\sigma^{**}(n)$ is the sum of the
biunitary divisors of $n$, that is, of the divisors $d$ of $n$ with $\gcd_1(d, n / d) = 1$, where
$\gcd_1$ denotes the greatest common unitary divisor. Since $0$ has no biunitary divisors,
$\sigma^{**}(0) = 0$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Section 1 (after Wall).

Formalized by `MetaMathlibExt.sigmaBiunitary`, a definition declared in [MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html#sigma-biunitary).

## Characterization of biunitary divisors

For natural numbers $n$ and $d$, $d$ is a biunitary
divisor of $n$ if and only if $d$ divides $n$, $n \neq 0$ and $\gcd_1(d, n / d) = 1$, where
$\gcd_1$ denotes the greatest common unitary divisor.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Section 1 (after Wall).

Formalized by `MetaMathlibExt.mem_biunitaryDivisors`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html#mem-biunitary-divisors).

## Zero has no biunitary divisors

The set of biunitary divisors of $0$ is empty.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Section 1 (after Wall).

Formalized by `MetaMathlibExt.biunitaryDivisors_zero`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html#biunitary-divisors-zero).

## The biunitary divisor sum of $0$

The sum $\sigma^{**}(0)$ of the biunitary divisors of $0$
equals $0$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Section 1 (after Wall).

Formalized by `MetaMathlibExt.sigmaBiunitary_zero`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html#sigma-biunitary-zero).

## Biunitary divisors divide

For natural numbers $n$ and $d$, if $d$ is a biunitary
divisor of $n$, then $d$ divides $n$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Section 1 (after Wall).

Formalized by `MetaMathlibExt.dvd_of_mem_biunitaryDivisors`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html#dvd-of-mem-biunitary-divisors).

## The biunitary divisor sum of $1$

The sum $\sigma^{**}(1)$ of the biunitary divisors of $1$
equals $1$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Section 1 (after Wall).

Formalized by `MetaMathlibExt.sigmaBiunitary_one`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html#sigma-biunitary-one).

## The biunitary divisor sum of $4$

The sum $\sigma^{**}(4)$ of the biunitary divisors of $4$
equals $5$.

The biunitary divisors of $4$ are $1$ and $4$: the divisor $2$ is not biunitary, since the greatest
common unitary divisor of $2$ and $2$ is $2$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 3.1 (`σ**(2²) = 5`).

Formalized by `MetaMathlibExt.sigmaBiunitary_four`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html#sigma-biunitary-four).

## The biunitary divisor sum of $16$

The sum $\sigma^{**}(16)$ of the biunitary divisors of
$16$ equals $1 + 2 + 8 + 16 = 27$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, formula (1) at `p = 2`, `e = 4`.

Formalized by `MetaMathlibExt.sigmaBiunitary_sixteen`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html#sigma-biunitary-sixteen).

## The biunitary divisor sum of $27$

The sum $\sigma^{**}(27)$ of the biunitary divisors of
$27$ equals $1 + 3 + 9 + 27 = 40$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Lemma 3.6 (`σ**(3³) = 2³ · 5`).

Formalized by `MetaMathlibExt.sigmaBiunitary_twentySeven`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html#sigma-biunitary-twenty-seven).

## $120$ is biunitary triperfect

The sum $\sigma^{**}(120)$ of the biunitary divisors of
$120$ equals $3 \cdot 120 = 360$.

## Sources

- Tomohiro Yamada, *Determining all Biunitary Triperfect Numbers of a Certain Form*, Journal of Integer Sequences 28 (2025), Article 25.4.5, Section 1 (smallest instances `120, 672, 2160` with `k = 3`).

Formalized by `MetaMathlibExt.sigmaBiunitary_oneHundredTwenty`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/BiunitaryDivisor.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html#sigma-biunitary-one-hundred-twenty).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Biunitary divisors](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/biunitary-divisors)
