---
declaration: section
origin: cited
lean: MetaMathlibExt.bNomialBase, MetaMathlibExt.bNomialCoefficient, MetaMathlibExt.bNomialDigitAtOrZero, MetaMathlibExt.IsBNomialIndispensableDigit, MetaMathlibExt.bNomialIndispensableDigitCount, MetaMathlibExt.bNomialNumberType3
statement: formalized
proof: formalized
---

# b-nomial coefficients

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/b-nomial-coefficients/index.html).

## Base polynomial of the $b$-nomial coefficients

For a natural number $b \ge 2$, this is
the integer polynomial $1 + X + \dots + X^{b-1} = \sum_{i=0}^{b-1} X^i \in \mathbb{Z}[X]$.

Formalized by `MetaMathlibExt.bNomialBase`, a definition declared in [MathlibExt/NumberTheory/BNomialCoefficient.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/BNomialCoefficient.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/b-nomial-coefficients/index.html#b-nomial-base).

## Type-1 $b$-nomial coefficients

For natural numbers $b \ge 2$ and $n$ and an integer
$k$, the type-1 $b$-nomial coefficient in row $n$ and column $k$ is the coefficient of $X^k$ in
$(1 + X + \dots + X^{b-1})^n \in \mathbb{Z}[X]$ when $k \ge 0$, and $0$ when $k < 0$.

Formalized by `MetaMathlibExt.bNomialCoefficient`, a definition declared in [MathlibExt/NumberTheory/BNomialCoefficient.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/BNomialCoefficient.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/b-nomial-coefficients/index.html#b-nomial-coefficient).

## Digits of a string extended by zero

For a $b$-ary string $x = (x_0, \dots, x_{n-1})$ of
length $n$, written from left to right, and a natural number $j$, this is the digit $x_j$ if
$j < n$, and $0$ if $j \ge n$.

Positions in $x$ run from left to right, so $x_0$ represents the source's leftmost digit $a_n$.
In particular, position $n$ represents the stipulated boundary digit $a_0 = 0$.

Formalized by `MetaMathlibExt.bNomialDigitAtOrZero`, a definition declared in [MathlibExt/NumberTheory/BNomialNumberType3.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/BNomialNumberType3.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/b-nomial-coefficients/index.html#b-nomial-digit-at-or-zero).

## Indispensable digits

Let $x = (x_0, \dots, x_{n-1})$ be a $b$-ary string of length $n$,
written from left to right, and extend it by zero on the right, setting $x_j = 0$ for $j \ge n$.
A position $p < n$ is indispensable in $x$ when there is a natural number $r$ with
$1 \le r \le n + 1 - p$ such that $x_{p+t} = x_p$ for every $t$ with $1 \le t < r$, and
$x_{p+r} < x_p$. That is, some nonempty constant run of digits beginning at position $p$ is
followed on the right by a strictly smaller digit.

The paper writes the digit at position $p$ as $a_i$ with $i = n - p$ and prints the witness bound
$r \le i + 1$, although only the boundary digit $a_0$ (position $n$) is defined. With the zero
extension the final case $r = i + 1$ is unsatisfiable, so the predicate agrees with the source in
every case the source defines.

Formalized by `MetaMathlibExt.IsBNomialIndispensableDigit`, a definition declared in [MathlibExt/NumberTheory/BNomialNumberType3.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/BNomialNumberType3.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/b-nomial-coefficients/index.html#is-bnomial-indispensable-digit).

## Number of indispensable digits

For a $b$-ary string $x$ of finite length, $\iota(x)$ is
the number of positions of $x$ that are indispensable.

Formalized by `MetaMathlibExt.bNomialIndispensableDigitCount`, a definition declared in [MathlibExt/NumberTheory/BNomialNumberType3.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/BNomialNumberType3.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/b-nomial-coefficients/index.html#b-nomial-indispensable-digit-count).

## Type-3 b-nomial numbers

For a natural number $b \ge 2$, a natural number $n$ and an
integer $k$, the type-3 $b$-nomial number is the number of $b$-ary strings $x$ of length $n$ with
exactly $k$ indispensable digits, that is, with $\iota(x) = k$. In particular it is zero for
$k < 0$.

At $n = 0$ this gives the source convention: the value is one at $k = 0$ and zero otherwise.

Formalized by `MetaMathlibExt.bNomialNumberType3`, a definition declared in [MathlibExt/NumberTheory/BNomialNumberType3.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/BNomialNumberType3.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/b-nomial-coefficients/index.html#b-nomial-number-type3).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: b-nomial coefficients](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/b-nomial-coefficients/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/b-nomial-coefficients)
