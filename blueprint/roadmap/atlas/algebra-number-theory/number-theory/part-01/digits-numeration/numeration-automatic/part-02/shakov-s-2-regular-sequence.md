---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ShakovTwoRegularWanted.shakovSeq, MathlibExt.NumberTheory.ShakovTwoRegularWanted.shakovA, MathlibExt.NumberTheory.ShakovTwoRegularWanted.fiber_card, MathlibExt.NumberTheory.ShakovTwoRegularWanted.block_average, MathlibExt.NumberTheory.ShakovTwoRegularWanted.prime_iff_fiber, MathlibExt.NumberTheory.ShakovTwoRegularWanted.shakovSeq_shakovA, MathlibExt.NumberTheory.ShakovTwoRegularWanted.fib_sq_add_one_composite
statement: formalized
---

# Shakov's 2-regular sequence

7 results, 2 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/shakov-s-2-regular-sequence/index.html).

## Shakov's $2$-regular sequence

The integer sequence $s$ with $s(0) = s(1) = 0$,
$s(2) = s(3) = 1$ and, for every $k \ge 1$, $s(4k) = 2s(2k) - s(k)$,
$s(4k+1) = 2s(2k) + s(2k+1)$, $s(4k+2) = 2s(2k+1) + s(2k)$ and $s(4k+3) = 2s(2k+1) - s(k)$.

The value $s(0)$ plays no role in the recursion; the source's sequence starts at $n = 1$.

Formalized by `MathlibExt.NumberTheory.ShakovTwoRegularWanted.shakovSeq`, a definition declared in [WantedExt/NumberTheory/ShakovTwoRegularWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ShakovTwoRegularWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/shakov-s-2-regular-sequence/index.html#shakov-seq).

## Shakov's auxiliary sequence

The integer sequence $a$ with $a(0) = 0$, $a(1) = 1$ and,
for every $n \ge 2$, $a(n) = 2a(n-1)$ if $n \equiv 0 \pmod 4$, $a(n) = a(n-1) + 1$ if
$n \equiv 1 \pmod 4$, $a(n) = 2a(n-1) + 1$ if $n \equiv 2 \pmod 4$, and $a(n) = a(n-1) - 1$ if
$n \equiv 3 \pmod 4$.

The value $a(0)$ plays no role in the recursion; the source's sequence starts at $n = 1$.

Formalized by `MathlibExt.NumberTheory.ShakovTwoRegularWanted.shakovA`, a definition declared in [WantedExt/NumberTheory/ShakovTwoRegularWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ShakovTwoRegularWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/shakov-s-2-regular-sequence/index.html#shakov-a).

## Shakov's sequence counts the divisors of $m^2 + 1$

Let $s$ be Shakov's $2$-regular
sequence and let $\tau(N)$ denote the number of positive divisors of $N$. Then $s(n) \ge 0$ for
every $n \ge 1$, and for every natural number $m$ the set $\{n \ge 1 : s(n) = m\}$ is finite
and has exactly $\tau(m^2 + 1)$ elements.

This is the coefficientwise form of the identity
$\sum_{m \ge 0} \tau(m^2 + 1) x^m = \sum_{n \ge 1} x^{s(n)}$ of formal power series.

## Sources

- Anton Shakov, "A 2-Regular Sequence That Counts The Divisors of `n^2 + 1`", Theorem 4.

Stated but not proved: `MathlibExt.NumberTheory.ShakovTwoRegularWanted.fiber_card` is written with `theorem_wanted` in [WantedExt/NumberTheory/ShakovTwoRegularWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ShakovTwoRegularWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/shakov-s-2-regular-sequence/index.html#fiber-card).

## Block averages of Shakov's sequence

Let $s$ be Shakov's $2$-regular sequence.
For every natural number $n$,

$$
\frac{1}{2^n} \sum_{2^n \le t < 2^{n+1}} s(t) =
\frac{(5 + \sqrt{17})^n - (5 - \sqrt{17})^n}{2^{2n-1} \sqrt{17}},
$$

where the exponent $2n - 1$ is read as $0$ when $n = 0$ (both sides are then $0$).

## Sources

- Anton Shakov, "A 2-Regular Sequence That Counts The Divisors of `n^2 + 1`", Proposition 7.

Stated but not proved: `MathlibExt.NumberTheory.ShakovTwoRegularWanted.block_average` is written with `theorem_wanted` in [WantedExt/NumberTheory/ShakovTwoRegularWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ShakovTwoRegularWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/shakov-s-2-regular-sequence/index.html#block-average).

## Primality of $n^2 + 1$ from the fibers of Shakov's sequence

Let $s$ be Shakov's
$2$-regular sequence. For every natural number $n \ge 1$, the number $n^2 + 1$ is prime if and
only if the set of natural numbers $m$ with $s(m) = n$ is exactly $\{2^n, 2^{n+1} - 1\}$.

## Sources

- Anton Shakov, "A 2-Regular Sequence That Counts The Divisors of `n^2 + 1`", Proposition 8.

Stated but not proved: `MathlibExt.NumberTheory.ShakovTwoRegularWanted.prime_iff_fiber` is written with `theorem_wanted` in [WantedExt/NumberTheory/ShakovTwoRegularWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ShakovTwoRegularWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/shakov-s-2-regular-sequence/index.html#prime-iff-fiber).

## Shakov's sequence takes Fibonacci values along the auxiliary sequence

Let $s$ be
Shakov's $2$-regular sequence, let $a$ be Shakov's auxiliary sequence, and let $F_k$ denote the
$k$-th Fibonacci number, with $F_0 = 0$ and $F_1 = 1$. For every natural number $n \ge 1$,
$s(\max(a(n), 0)) = F_{n-1}$.

The source shows that $a(n)$ is a positive integer and numbers the Fibonacci numbers so that
this reads $s(a(n)) = F_n$.

## Sources

- Anton Shakov, "A 2-Regular Sequence That Counts The Divisors of `n^2 + 1`", Proposition 9.

Stated but not proved: `MathlibExt.NumberTheory.ShakovTwoRegularWanted.shakovSeq_shakovA` is written with `theorem_wanted` in [WantedExt/NumberTheory/ShakovTwoRegularWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ShakovTwoRegularWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/shakov-s-2-regular-sequence/index.html#shakov-seq-shakov-a).

## Fibonacci squares plus one are eventually composite

Let $F_k$ denote the $k$-th
Fibonacci number, with $F_0 = 0$ and $F_1 = 1$. For every natural number $k \ge 4$, the number
$F_k^2 + 1$ is composite.

In the source's numbering of the Fibonacci numbers, which is shifted by one, this reads
"$F_n^2 + 1$ is composite for $n > 4$".

## Sources

- Anton Shakov, "A 2-Regular Sequence That Counts The Divisors of `n^2 + 1`", Corollary 10.

Stated but not proved: `MathlibExt.NumberTheory.ShakovTwoRegularWanted.fib_sq_add_one_composite` is written with `theorem_wanted` in [WantedExt/NumberTheory/ShakovTwoRegularWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ShakovTwoRegularWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/shakov-s-2-regular-sequence/index.html#fib-sq-add-one-composite).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Shakov's 2-regular sequence](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/shakov-s-2-regular-sequence/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/digits-numeration/numeration-automatic/shakov-s-2-regular-sequence)
