---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.PrimeDistribution.discrepancy, MathlibExt.NumberTheory.PrimeDistribution.discrepancy_single_zero, MathlibExt.NumberTheory.PrimeDistribution.discrepancy_single, MathlibExt.NumberTheory.PrimeDistribution.primitiveDiscrepancy, MathlibExt.NumberTheory.PrimeDistribution.primitiveDiscrepancy_attained, MathlibExt.NumberTheory.PrimeDistribution.abs_discrepancy_le_primitiveDiscrepancy, MathlibExt.NumberTheory.PrimeDistribution.averagedDiscrepancy, MathlibExt.NumberTheory.PrimeDistribution.averagedDiscrepancy_zero
statement: formalized
proof: formalized
---

# Discrepancy of sequences in residue classes

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/discrepancy-of-sequences-in-residue-classes/index.html).

## Discrepancy in a residue class

Let $K$ be a field of characteristic zero, let
$\alpha : \mathbb{N} \to K$ be finitely supported, let $q$ be a positive integer and let $a$ be a
natural number. The discrepancy of $\alpha$ in the residue class of $a$ modulo $q$ is

$$\Delta(\alpha; a \bmod q) = \sum_{\substack{n \ge 1 \\ n \equiv a \pmod{q}}} \alpha(n) -
\frac{1}{\varphi(q)} \sum_{\substack{n \ge 1 \\ \gcd(n, q) = 1}} \alpha(n),$$

where $\varphi$ is Euler's totient function. The value $\alpha(0)$ does not contribute.

Formalized by `MathlibExt.NumberTheory.PrimeDistribution.discrepancy`, a definition declared in [MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/discrepancy-of-sequences-in-residue-classes/index.html#discrepancy).

## A sequence supported at index zero has zero discrepancy

Let $K$ be a field of
characteristic zero, let $v \in K$, let $q$ be a positive integer and let $a \in \mathbb{N}$. The
sequence with value $v$ at index $0$ and $0$ at every other index has discrepancy $0$ at
modulus $q$ and residue $a$.

Formalized by `MathlibExt.NumberTheory.PrimeDistribution.discrepancy_single_zero`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/discrepancy-of-sequences-in-residue-classes/index.html#discrepancy-single-zero).

## Discrepancy of a single positive term

Let $K$ be a field of characteristic zero, let $n$
be a positive integer, let $v \in K$, let $q$ be a positive integer and let $a \in \mathbb{N}$.
Let $e$ be the sequence with value $v$ at index $n$ and $0$ at every other index. Then the
discrepancy of $e$ at modulus $q$ and residue $a$ equals $A - B/\varphi(q)$, where $A = v$ if
$n \equiv a \pmod{q}$ and $A = 0$ otherwise, $B = v$ if $\gcd(n, q) = 1$ and $B = 0$ otherwise,
and $\varphi$ is Euler's totient function.

Formalized by `MathlibExt.NumberTheory.PrimeDistribution.discrepancy_single`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/discrepancy-of-sequences-in-residue-classes/index.html#discrepancy-single).

## Primitive discrepancy

For a finitely supported sequence
$\alpha : \mathbb{N} \to \mathbb{R}$ and a positive integer $q$, the primitive discrepancy of
$\alpha$ modulo $q$ is the maximum, over the residue classes $a$ modulo $q$ that are coprime to
$q$, of $|\Delta(\alpha; a \bmod q)|$, where $\Delta(\alpha; a \bmod q)$ is the discrepancy of
$\alpha$ in the residue class of $a$ modulo $q$.

Formalized by `MathlibExt.NumberTheory.PrimeDistribution.primitiveDiscrepancy`, a definition declared in [MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/discrepancy-of-sequences-in-residue-classes/index.html#primitive-discrepancy).

## The primitive discrepancy is attained

For every finitely supported sequence
$\alpha : \mathbb{N} \to \mathbb{R}$ and every positive integer $q$, there is a residue class $a$
modulo $q$ coprime to $q$ such that the primitive discrepancy of $\alpha$ modulo $q$ equals
$|\Delta(\alpha; a \bmod q)|$, the absolute value of the discrepancy of $\alpha$ in the residue
class of $a$ modulo $q$.

Formalized by `MathlibExt.NumberTheory.PrimeDistribution.primitiveDiscrepancy_attained`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/discrepancy-of-sequences-in-residue-classes/index.html#primitive-discrepancy-attained).

## Primitive residue-class discrepancies are bounded by the primitive discrepancy

Let
$\alpha$ be a finitely supported real sequence indexed by $\mathbb{N}$, let $q$ be a positive
integer, and let $a$ be a unit of $\mathbb{Z}/q\mathbb{Z}$, represented by its least nonnegative
residue. Then the absolute value of the discrepancy of $\alpha$ at modulus $q$ and residue $a$ is
at most the primitive discrepancy of $\alpha$ at modulus $q$.

Formalized by `MathlibExt.NumberTheory.PrimeDistribution.abs_discrepancy_le_primitiveDiscrepancy`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/discrepancy-of-sequences-in-residue-classes/index.html#abs-discrepancy-le-primitive-discrepancy).

## Averaged discrepancy

For a finitely supported real sequence $\alpha$ indexed by
$\mathbb{N}$ and a natural number $Q$, the averaged discrepancy of $\alpha$ up to $Q$ is the sum
$\sum_{q=1}^{Q} \Delta^*(\alpha; q)$, where $\Delta^*(\alpha; q)$ is the primitive discrepancy
of $\alpha$ at modulus $q$.

The sum is not divided by $Q$.

Formalized by `MathlibExt.NumberTheory.PrimeDistribution.averagedDiscrepancy`, a definition declared in [MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/discrepancy-of-sequences-in-residue-classes/index.html#averaged-discrepancy).

## The averaged discrepancy with cutoff zero vanishes

For every finitely supported real
sequence $\alpha$ indexed by $\mathbb{N}$, the averaged discrepancy of $\alpha$ with cutoff
$Q = 0$ equals $0$, since there are no positive moduli $q \le 0$.

Formalized by `MathlibExt.NumberTheory.PrimeDistribution.averagedDiscrepancy_zero`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/discrepancy-of-sequences-in-residue-classes/index.html#averaged-discrepancy-zero).

## Multiplicative convolution of finitely supported sequences

Let $R$ be a semiring and let
$\alpha, \beta \colon \mathbb{N} \to R$ be finitely supported. Their convolution
$\alpha \star \beta$ is the finitely supported sequence whose value at $n$ is
$\sum_{a, b \ge 1,\ ab = n} \alpha(a)\beta(b)$; the values of $\alpha$ and $\beta$ at index $0$
are discarded.

Formalized by `MathlibExt.NumberTheory.PrimeDistribution.convolution`, a definition declared in [MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/discrepancy-of-sequences-in-residue-classes/index.html#convolution).

## Coefficients of the multiplicative convolution

Let $R$ be a semiring and let
$\alpha, \beta \colon \mathbb{N} \to R$ be finitely supported, with convolution
$\alpha \star \beta$. For every $n \in \mathbb{N}$,

$$(\alpha \star \beta)(n) = \sum_{a} \sum_{b} [ab = n]\, \alpha(a)\beta(b),$$

where $a$ ranges over the positive indices with $\alpha(a) \ne 0$, $b$ ranges over the positive
indices with $\beta(b) \ne 0$, and $[ab = n]$ is $1$ if $ab = n$ and $0$ otherwise.

Formalized by `MathlibExt.NumberTheory.PrimeDistribution.convolution_apply`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/discrepancy-of-sequences-in-residue-classes/index.html#convolution-apply).

## The multiplicative convolution vanishes at index zero

Let $R$ be a semiring and let
$\alpha, \beta \colon \mathbb{N} \to R$ be finitely supported. Then their convolution
$\alpha \star \beta$ has value $0$ at index $0$.

Formalized by `MathlibExt.NumberTheory.PrimeDistribution.convolution_apply_zero`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/discrepancy-of-sequences-in-residue-classes/index.html#convolution-apply-zero).

## Convolving a sequence supported at zero gives zero

Let $R$ be a semiring, let $v \in R$,
and let $\beta \colon \mathbb{N} \to R$ be finitely supported. If $e$ is the sequence with value
$v$ at index $0$ and $0$ at every other index, then the convolution $e \star \beta$ is the zero
sequence.

Formalized by `MathlibExt.NumberTheory.PrimeDistribution.convolution_single_zero_left`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/discrepancy-of-sequences-in-residue-classes/index.html#convolution-single-zero-left).

## Convolving with a sequence supported at zero gives zero

Let $R$ be a semiring, let
$\alpha \colon \mathbb{N} \to R$ be finitely supported, and let $v \in R$. If $e$ is the sequence
with value $v$ at index $0$ and $0$ at every other index, then the convolution
$\alpha \star e$ is the zero sequence.

Formalized by `MathlibExt.NumberTheory.PrimeDistribution.convolution_single_zero_right`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/discrepancy-of-sequences-in-residue-classes/index.html#convolution-single-zero-right).

## Von Mangoldt function on a dyadic interval

For a real number $x$, this is the finitely
supported function on $\mathbb{N}$ whose value at $n$ is $\Lambda(n)$ when $n \ge 1$ and
$x \le n \le 2x$, and $0$ otherwise, where $\Lambda$ is the von Mangoldt function.

## Sources

- Polymath8b v4, Claim 2.2 and the positive-integer convention before Definition 1.6.

Formalized by `MathlibExt.NumberTheory.PrimeDistribution.dyadicVonMangoldt`, a definition declared in [MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/discrepancy-of-sequences-in-residue-classes/index.html#dyadic-von-mangoldt).

## Values of the dyadic von Mangoldt function

For every real $x > 0$ and every natural
number $n$, the von Mangoldt function on the dyadic interval for $x$ takes at $n$ the value
$\Lambda(n)$ if $x \le n \le 2x$, and $0$ otherwise, where $\Lambda$ is the von Mangoldt function.

## Sources

- Polymath8b v4, Claim 2.2.

Formalized by `MathlibExt.NumberTheory.PrimeDistribution.dyadicVonMangoldt_apply`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/PrimeDistribution.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/discrepancy-of-sequences-in-residue-classes/index.html#dyadic-von-mangoldt-apply).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Discrepancy of sequences in residue classes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/discrepancy-of-sequences-in-residue-classes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/discrepancy-of-sequences-in-residue-classes)
