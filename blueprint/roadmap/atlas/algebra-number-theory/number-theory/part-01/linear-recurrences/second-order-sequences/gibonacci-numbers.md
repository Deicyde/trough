---
declaration: section
origin: cited
lean: MetaMathlibExt.gibonacciNumber, MetaMathlibExt.gibonacci_zero_one_eq_fib, MetaMathlibExt.gibonacci_cassini_of_pos, MetaMathlibExt.melham_fibonacci_gibonacci_sum_of_squares_general, MetaMathlibExt.melham_fibonacci_gibonacci_sum_of_squares, MetaMathlibExt.gibonacci_sq_recurrence
statement: formalized
proof: formalized
---

# Gibonacci numbers

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/gibonacci-numbers/index.html).

## Gibonacci numbers

For integers $G_0$ and $G_1$, the Gibonacci sequence with initial
values $G_0$ and $G_1$ is the integer sequence $(G_n)_{n \ge 0}$ that starts with $G_0, G_1$ and
satisfies $G_{n+2} = G_{n+1} + G_n$ for every $n \ge 0$.

Formalized by `MetaMathlibExt.gibonacciNumber`, a definition declared in [MathlibExt/NumberTheory/GibonacciNumber.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GibonacciNumber.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/gibonacci-numbers/index.html#gibonacci-number).

## Gibonacci numbers starting from 0 and 1 are the Fibonacci numbers

For every natural
number $n$, the $n$-th Gibonacci number with initial values $G_0 = 0$ and $G_1 = 1$ equals the
$n$-th Fibonacci number $F_n$ (where $F_0 = 0$, $F_1 = 1$ and $F_{n+2} = F_{n+1} + F_n$).

Formalized by `MetaMathlibExt.gibonacci_zero_one_eq_fib`, a theorem declared in [MathlibExt/NumberTheory/GibonacciNumber.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GibonacciNumber.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/gibonacci-numbers/index.html#gibonacci-zero-one-eq-fib).

## Cassini identity for Gibonacci numbers

Let $G_0$ and $G_1$ be integers and let $(G_n)$ be
the Gibonacci sequence with these initial values, so that $G_{n+2} = G_{n+1} + G_n$ for all
$n \ge 0$. Then for every natural number $n \ge 1$,
$G_{n+1} G_{n-1} - G_n^2 = (-1)^n (G_1^2 - G_0 G_1 - G_0^2)$.

## Sources

- Guyer and Mbirika, "GCD of Sums of k Consecutive Fibonacci, Lucas, and Generalized Fibonacci Numbers," Journal of Integer Sequences 24 (2021), Article 21.9.8, Proposition 2.5.

Formalized by `MetaMathlibExt.gibonacci_cassini_of_pos`, a theorem declared in [MathlibExt/NumberTheory/GibonacciCassini.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GibonacciCassini.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/gibonacci-numbers/index.html#gibonacci-cassini-of-pos).

## Melham's gibonacci sum-of-squares identity, general form

Let
$G : \mathbb{Z} \to \mathbb{Z}$ satisfy $G(j+2) = G(j+1) + G(j)$ for every integer $j$, and let
$F_m$ denote the $m$-th Fibonacci number. Then for every integer $k$ and every natural number $n$,

$$6\Bigl(\sum_{j=0}^{2n-1} G(k+j)^2\Bigr)^2 =
F_{2n}^2\bigl(G(k+n-2)^4 + 4G(k+n-1)^4 + 4G(k+n)^4 + G(k+n+1)^4\bigr).$$

The source states this identity with the additional hypotheses that $G(0) \ne 0$ or $G(1) \ne 0$
and that $n \ge 1$.

Formalized by `MetaMathlibExt.melham_fibonacci_gibonacci_sum_of_squares_general`, a theorem declared in [MathlibExt/NumberTheory/MelhamGibonacci.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MelhamGibonacci.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/gibonacci-numbers/index.html#melham-fibonacci-gibonacci-sum-of-square).

## Melham's gibonacci sum-of-squares identity

Let $G : \mathbb{Z} \to \mathbb{Z}$ satisfy
$G(j+2) = G(j+1) + G(j)$ for every integer $j$, with $G(0) \ne 0$ or $G(1) \ne 0$, and let $F_m$
denote the $m$-th Fibonacci number. Then for every integer $k$ and every natural number $n \ge 1$,

$$6\Bigl(\sum_{j=0}^{2n-1} G(k+j)^2\Bigr)^2 =
F_{2n}^2\bigl(G(k+n-2)^4 + 4G(k+n-1)^4 + 4G(k+n)^4 + G(k+n+1)^4\bigr).$$

The hypotheses $G(0) \ne 0$ or $G(1) \ne 0$ and $n \ge 1$ are not needed; they keep the shape of
the source.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL27/Adegoke/adegoke12.tex>, lines 92–103, 877–880, and 1824–1828.

Formalized by `MetaMathlibExt.melham_fibonacci_gibonacci_sum_of_squares`, a theorem declared in [MathlibExt/NumberTheory/MelhamGibonacci.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MelhamGibonacci.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/gibonacci-numbers/index.html#melham-fibonacci-gibonacci-sum-of-square-2).

## Gibonacci squares recurrence

Let $g : \mathbb{N} \to \mathbb{Z}$ satisfy
$g(n+2) = g(n+1) + g(n)$ for every $n \in \mathbb{N}$, and let $F_3 = 2$ be the third Fibonacci
number. Then for every $n \in \mathbb{N}$,

$$g(n+3)^2 = F_3\, g(n+2)^2 + F_3\, g(n+1)^2 - g(n)^2.$$

The characteristic polynomial $x^3 - 2x^2 - 2x + 1$ of this recurrence has roots $\alpha^2$,
$\beta^2$ and $-1$, where $\alpha$ and $\beta$ are the roots of $x^2 - x - 1$.

## Sources

- Thomas Koshy, "A Graph-Theoretic Model for a Generalized Fibonacci Gem," Journal of Integer Sequences 22 (2019), Article 19.4.1, Theorem 2, lines 149–153, https://cs.uwaterloo.ca/journals/JIS/VOL22/Koshy/koshy7.tex

Formalized by `MetaMathlibExt.gibonacci_sq_recurrence`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/GibonacciSquaresRecurrence.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/GibonacciSquaresRecurrence.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/gibonacci-numbers/index.html#gibonacci-sq-recurrence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gibonacci numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/gibonacci-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/second-order-sequences/gibonacci-numbers)
