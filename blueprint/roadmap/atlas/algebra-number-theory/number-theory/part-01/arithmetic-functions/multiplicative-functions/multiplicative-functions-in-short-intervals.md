---
declaration: section
origin: cited
lean: ArithmeticFunction.intExtension, MathlibExt.NumberTheory.BoundedMultiplicativeFunctionsWanted.BoundedMultiplicativeFunctions.IsOneBounded, MathlibExt.NumberTheory.BoundedMultiplicativeFunctionsWanted.BoundedMultiplicativeFunctions.theorem_1_3, MathlibExt.NumberTheory.BoundedMultiplicativeFunctionsWanted.BoundedMultiplicativeFunctions.corollary_1_1
statement: formalized
---

# Multiplicative functions in short intervals

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/multiplicative-functions-in-short-intervals/index.html).

## Extension of an arithmetic function to the integers

Let $R$ be a type with a zero
element $0$ and let $f$ be an arithmetic function with values in $R$. The extension of $f$ to the
integers is the function on $\mathbb{Z}$ that sends an integer $z$ to $f(z)$ if $z > 0$ and to
$0$ if $z \le 0$.

Formalized by `ArithmeticFunction.intExtension`, a definition declared in [WantedExt/NumberTheory/BoundedMultiplicativeFunctionsWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BoundedMultiplicativeFunctionsWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/multiplicative-functions-in-short-intervals/index.html#int-extension).

## 1-bounded function

A function $f \colon \mathbb{N} \to \mathbb{C}$ is 1-bounded if
$|f(n)| \le 1$ for every natural number $n$.

Formalized by `MathlibExt.NumberTheory.BoundedMultiplicativeFunctionsWanted.BoundedMultiplicativeFunctions.IsOneBounded`, an abbreviation declared in [WantedExt/NumberTheory/BoundedMultiplicativeFunctionsWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BoundedMultiplicativeFunctionsWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/multiplicative-functions-in-short-intervals/index.html#is-one-bounded).

## Non-pretentious multiplicative functions do not correlate with polynomial phases on short intervals on average

**Non-pretentious multiplicative functions do not correlate with polynomial phases on short
intervals on average.** For a function $g$ on the integers, a natural number $k$, a real $x$ and a
real $H > 0$ write

$$
\|g\|_{u^{k+1}[x, x+H]} = \sup_{\deg P \le k} \frac{1}{H}
\Bigl| \sum_{\lceil x \rceil \le n \le \lfloor x + H \rfloor} g(n) e^{-2\pi i P(n)} \Bigr|,
$$

the supremum taken over real polynomials $P$ of degree at most $k$. For functions
$f, g \colon \mathbb{N} \to \mathbb{C}$ and a real $X$ let

$$
\mathbb{D}(f, g; X) =
\Bigl( \sum_{p \le X} \frac{1 - \operatorname{Re}\bigl(f(p) \overline{g(p)}\bigr)}{p} \Bigr)^{1/2},
$$

the sum taken over primes $p \le X$, and for a positive integer $Q$ let $M(f; X, Q)$ be the
infimum of $\mathbb{D}(f, n \mapsto \chi(n) n^{it}; X)$ over real $t$ with $|t| \le X$, positive
integers $q \le Q$ and Dirichlet characters $\chi$ modulo $q$.

Let $k$ be a natural number, $\theta$ a real number with $0 < \theta < 1/2$ and $\eta > 0$ a real
number. Then there are a positive integer $Q$ and real numbers $C > 0$ and $B$ such that the
following holds for every multiplicative arithmetic function $f \colon \mathbb{N} \to \mathbb{C}$
with $|f(n)| \le 1$ for all $n$, extended to the integers by $f(n) = 0$ for $n \le 0$, every real
$X \ge 1$ and every real $H$ with $X^\theta \le H \le X^{1-\theta}$: if

$$
\int_X^{2X} \|f\|_{u^{k+1}[x, x+H]} \, dx \ge \eta X,
$$

then $M(f; C X^{k+1} / H^{k+1}, Q) \le B$.

## Sources

- K. Matomäki, M. Radziwiłł, T. Tao, J. Teräväinen, and T. Ziegler, `Higher uniformity of bounded multiplicative functions in short intervals on average`, Annals of Math, 197 (2) 2023. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_bounded_multiplicative_functions` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.BoundedMultiplicativeFunctionsWanted.BoundedMultiplicativeFunctions.theorem_1_3` is written with `theorem_wanted` in [WantedExt/NumberTheory/BoundedMultiplicativeFunctionsWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BoundedMultiplicativeFunctionsWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/multiplicative-functions-in-short-intervals/index.html#theorem-1-3).

## Liouville's function does not correlate with polynomial phases on short intervals on average

Let $\lambda$ be the Liouville function, extended to the integers by $\lambda(n) = 0$ for
$n \le 0$, let $k$ be a natural number and let $\theta$ be a real number with $0 < \theta < 1$.
For real $x$ and $H > 0$ write

$$
\|\lambda\|_{u^{k+1}[x, x+H]} = \sup_{\deg P \le k} \frac{1}{H}
\Bigl| \sum_{\lceil x \rceil \le n \le \lfloor x + H \rfloor} \lambda(n) e^{-2\pi i P(n)} \Bigr|,
$$

the supremum taken over real polynomials $P$ of degree at most $k$. Then

$$
\int_X^{2X} \|\lambda\|_{u^{k+1}[x, x + X^\theta]} \, dx = o(X)
$$

as the real number $X$ tends to infinity.

## Sources

- K. Matomäki, M. Radziwiłł, T. Tao, J. Teräväinen, and T. Ziegler, `Higher uniformity of bounded multiplicative functions in short intervals on average`, Annals of Math, 197 (2) 2023. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_bounded_multiplicative_functions` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.BoundedMultiplicativeFunctionsWanted.BoundedMultiplicativeFunctions.corollary_1_1` is written with `theorem_wanted` in [WantedExt/NumberTheory/BoundedMultiplicativeFunctionsWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BoundedMultiplicativeFunctionsWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/multiplicative-functions-in-short-intervals/index.html#corollary-1-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multiplicative functions in short intervals](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/multiplicative-functions-in-short-intervals/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/multiplicative-functions-in-short-intervals)
