---
declaration: section
origin: cited
lean: MetaMathlibExt.NormalNumber.digitSeq, MetaMathlibExt.NormalNumber.IsSimplyNormalInBase, MetaMathlibExt.NormalNumber.IsNormalInBase, MetaMathlibExt.NormalNumber.IsNormalInBase.isSimplyNormalInBase, MetaMathlibExt.NormalNumber.IsAbsolutelyNormal, MetaMathlibExt.campbellH1, MetaMathlibExt.campbellH1_small, MetaMathlibExt.campbellH2
statement: formalized
---

# Normal numbers

24 results, 17 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html).

## Base-$b$ digits of a real number

For natural numbers $b$ and $n$ and a real number $x$, the
$n$-th digit of $x$ in base $b$, counting from $n = 0$ just after the radix point, is
$\lfloor b^{n+1} \{x\} \rfloor \bmod b$, where $\{x\} = x - \lfloor x \rfloor$ is the fractional
part of $x$.

For $b \ge 2$ these are the digits of the base-$b$ expansion of $\{x\}$ that does not end in an
infinite run of the digit $b - 1$. The formula is intended only for bases $b \ge 2$.

Formalized by `MetaMathlibExt.NormalNumber.digitSeq`, a definition declared in [MathlibExt/NumberTheory/NormalNumber.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NormalNumber.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#digit-seq).

## Simply normal numbers

For a natural number $b$ and a real number $x$, write $a_k$ for the
$k$-th base-$b$ digit of $x$ after the radix point, counting from $k = 0$. Then $x$ is simply
normal in base $b$ if for every natural number $d < b$ the proportion
$\#\{k < n : a_k = d\} / n$ tends to $1/b$ as $n \to \infty$.

This predicate is intended for bases $b \ge 2$.

Formalized by `MetaMathlibExt.NormalNumber.IsSimplyNormalInBase`, a definition declared in [MathlibExt/NumberTheory/NormalNumber.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NormalNumber.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#is-simply-normal-in-base).

## Normal numbers

For a natural number $b$ and a real number $x$, write $a_i$ for the $i$-th
base-$b$ digit of $x$ after the radix point, counting from $i = 0$. Then $x$ is normal in base $b$
if for every natural number $k$ and all natural numbers $w_0, \dots, w_{k-1} < b$ the proportion
$\#\{i < n : a_{i+j} = w_j \text{ for all } j < k\} / n$ tends to $1/b^k$ as $n \to \infty$.

This predicate is intended for bases $b \ge 2$.

Formalized by `MetaMathlibExt.NormalNumber.IsNormalInBase`, a definition declared in [MathlibExt/NumberTheory/NormalNumber.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NormalNumber.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#is-normal-in-base).

## Normal numbers are simply normal

If a real number $x$ is normal in base $b$, then $x$ is
simply normal in base $b$.

Formalized by `MetaMathlibExt.NormalNumber.IsNormalInBase.isSimplyNormalInBase`, a theorem declared in [MathlibExt/NumberTheory/NormalNumber.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NormalNumber.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#is-simply-normal-in-base-2).

## Absolutely normal numbers

A real number is absolutely normal if it is normal in every
base at least two.

Formalized by `MetaMathlibExt.NormalNumber.IsAbsolutelyNormal`, a definition declared in [MathlibExt/NumberTheory/NormalNumber.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NormalNumber.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#is-absolutely-normal).

## Campbell's sequence $h_1$

For a natural number $n$, $h_1(n) = 0$ if $n < 10$ and
$h_1(n) = 10^{\lfloor \log_{10} n \rfloor}$ if $n \ge 10$; thus for $n \ge 10$, $h_1(n)$ is the
largest power of $10$ that is at most $n$.

## Sources

- John M. Campbell, *A Counterexample to a Purported Construction of Normal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.3.4, Section 2 (definition of `h₁`).

Formalized by `MetaMathlibExt.campbellH1`, a definition declared in [WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#campbell-h1).

## Small values of $h_1$

Campbell's auxiliary sequence $h_1$ satisfies $h_1(9) = 0$,
$h_1(10) = 10$, $h_1(99) = 10$ and $h_1(100) = 100$.

## Sources

- John M. Campbell, *A Counterexample to a Purported Construction of Normal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.3.4, Section 2.

Formalized by `MetaMathlibExt.campbellH1_small`, a theorem declared in [WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#campbell-h1-small).

## Campbell's sequence $h_2$

For a natural number $n$, let $k = \lfloor \log_{10} n \rfloor$
(with $k = 0$ for $n = 0$), let $h_1$ be Campbell's sequence and let
$S_k = \sum_{i=1}^{10^k} h_1(i)$. Then
$h_2(n) = 10^k \lfloor S_k / 10^k \rfloor + \sum_{i=10^k+1}^{n} h_1(i)$, where the last sum is
empty when $n \le 10^k$.

This is OEIS A380904.

## Sources

- John M. Campbell, *A Counterexample to a Purported Construction of Normal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.3.4, Section 2, Equation (6) (definition of `h₂`).

Formalized by `MetaMathlibExt.campbellH2`, a definition declared in [WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#campbell-h2).

## Small values of Campbell's sequence $h_2$

The sequence $h_2$ satisfies $h_2(9) = 0$,
$h_2(10) = 10$, $h_2(21) = 120$, $h_2(99) = 900$ and $h_2(100) = 1000$.

## Sources

- John M. Campbell, *A Counterexample to a Purported Construction of Normal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.3.4, Example 1 and Section 2.1.

Formalized by `MetaMathlibExt.campbellH2_small`, a theorem declared in [WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#campbell-h2-small).

## Campbell's auxiliary function $h_3^{(m)}$

For a natural number $m$, let
$H(m) = h_2(10^m) - h_2(10^m - 1)$, where $h_2$ is Campbell's sequence (in the paper's notation
$H(m) = y_1(m + 1) - y_2(m)$ with $y_1(n) = h_2(10^{n-1})$ and $y_2(n) = h_2(10^n - 1)$). Define
$h_3^{(m)} : \mathbb{R} \to \mathbb{R}$ by $h_3^{(m)}(t) = a(m)\,t + b(m)$ for
$t \le 10^m - 1/10$ and $h_3^{(m)}(t) = c(m)\,t + d(m)$ for $t > 10^m - 1/10$, where
$a(m) = (20H(m) - 11 \cdot 10^m)/9 + 9 \cdot 10^{m-1}$,
$b(m) = (10^m - 1)(-20H(m) + 11 \cdot 10^m)/9 + 10^m - 9 \cdot 10^{2m-1}$,
$c(m) = -20H(m) + 9 \cdot 10^{m-1} + 11 \cdot 10^m$ and
$d(m) = 20 \cdot 10^m H(m) - 11 \cdot 10^{2m} - 9 \cdot 10^{2m-1} + 10^m$, with the exponents
$m - 1$ and $2m - 1$ read as $0$ when $m = 0$.

The paper uses $h_3^{(m)}$ only on $[10^m - 1, 10^m]$ for $m \ge 2$.

## Sources

- John M. Campbell, *A Counterexample to a Purported Construction of Normal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.3.4, Section 2.2, Equations (16)-(20).

Formalized by `MetaMathlibExt.campbellH3`, a definition declared in [WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#campbell-h3).

## First piece of Campbell's auxiliary function $h_3^{(m)}$

For every natural number $m$
and every real number $t \le 10^m - 1/10$, $h_3^{(m)}(t) = a(m)\,t + b(m)$, where
$H(m) = h_2(10^m) - h_2(10^m - 1)$ with $h_2$ Campbell's sequence,
$a(m) = (20H(m) - 11 \cdot 10^m)/9 + 9 \cdot 10^{m-1}$ and
$b(m) = (10^m - 1)(-20H(m) + 11 \cdot 10^m)/9 + 10^m - 9 \cdot 10^{2m-1}$, with the exponents
$m - 1$ and $2m - 1$ read as $0$ when $m = 0$.

## Sources

- John M. Campbell, *A Counterexample to a Purported Construction of Normal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.3.4, Section 2.2.

Formalized by `MetaMathlibExt.campbellH3_of_le`, a theorem declared in [WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#campbell-h3-of-le).

## Campbell's interpolation

Let $h_2$ be Campbell's sequence and $h_3^{(m)}$ the auxiliary
piecewise-linear functions of the construction, and for $n \ge 1$ put $y_1(n) = h_2(10^{n-1})$ and
$y_2(n) = h_2(10^n - 1)$. Campbell's interpolation is the function $f : \mathbb{R} \to \mathbb{R}$
with $f(x) = \frac{89}{110} e^{(100/89)(11x - 100)} + \frac{1}{10}$ for $x \le 100/11$ and
$f(x) = 10x - 90$ for $100/11 < x \le 10$. For $x > 10$ put
$m = \lfloor \log_{10} \lfloor x \rfloor \rfloor + 1$, so that $m \ge 2$ and
$10^{m-1} \le x < 10^m$; then

$$
f(x) = \frac{x (y_2(m) - y_1(m)) - (y_1(m) + 10^{m-1} y_2(m) - 10^m y_1(m))}{9 \cdot 10^{m-1} - 1}
$$

if $x \le 10^m - 1$, and $f(x) = h_2(10^m - 1) + \int_{10^m - 1}^{x} h_3^{(m)}(t) \, dt$ if
$x > 10^m - 1$.

The paper defines $f$ on $[0, \infty)$ only; here the first formula is used for every
$x \le 100/11$. At a power of ten $x = 10^{m-1} > 10$ the formula for index $m$ is used; the piece
to its left takes the same value there.

## Sources

- John M. Campbell, *A Counterexample to a Purported Construction of Normal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.3.4, Section 2.2, Equations (15) and (21).

Formalized by `MetaMathlibExt.campbellF`, a definition declared in [WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#campbell-f).

## Campbell's interpolation on $(100/11, 10)$

For every real $x$ with $100/11 < x \le 10$,
Campbell's interpolation satisfies $f(x) = 10x - 90$.

## Sources

- John M. Campbell, *A Counterexample to a Purported Construction of Normal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.3.4, Section 2.2.

Formalized by `MetaMathlibExt.campbellF_of_mem`, a theorem declared in [WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#campbell-f-of-mem).

## Decimal digit block of $h_2(n)$

For a natural number $n$, the block of $n$ is the list of
base-$10$ digits of $h_2(n)$, where $h_2$ is Campbell's sequence, written most significant digit
first; when $h_2(n) = 0$ the block is the single digit $0$.

## Sources

- John M. Campbell, *A Counterexample to a Purported Construction of Normal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.3.4, Section 1.1 (the expansion `0.b₁b₂…` with `b_n` the base-`g` expansion of `⌊f(n)⌋`).

Formalized by `MetaMathlibExt.campbellBlock`, a definition declared in [WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#campbell-block).

## Digits of the concatenation $0.h_2(1)h_2(2)\ldots$

Let $h_2$ be Campbell's sequence.
For $j \ge 0$, $d_j$ is the digit in position $j$ (counting from $0$) after the decimal point of
$0.h_2(1)h_2(2)\ldots$, the string obtained by writing the blocks of $h_2(1), h_2(2), \ldots$ one
after another, where the block of $h_2(n)$ is its list of base-$10$ digits, most significant
first, with $0$ written as the single digit $0$.

Every block is nonempty, so $d_j$ already lies in the first $j + 1$ blocks.

## Sources

- John M. Campbell, *A Counterexample to a Purported Construction of Normal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.3.4, Theorem 8 (the concatenation `0.h₂(1)h₂(2)…`).

Formalized by `MetaMathlibExt.campbellConcatDigit`, a definition declared in [WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#campbell-concat-digit).

## The first eleven digits of the concatenation $0.h_2(1)h_2(2)\ldots$

Let $h_2$ be
Campbell's sequence and let $d_0, d_1, d_2, \ldots$ be the digits after the decimal point of
$0.h_2(1)h_2(2)\ldots$, the concatenation of the base-$10$ digit blocks of $h_2(1), h_2(2), \ldots$
(with $0$ written as the single digit $0$). Then
$(d_0, d_1, \ldots, d_{10}) = (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0)$: nine zero blocks from
$h_2(1) = \cdots = h_2(9) = 0$, then the block of $h_2(10) = 10$.

## Sources

- John M. Campbell, *A Counterexample to a Purported Construction of Normal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.3.4, Example 1.

Formalized by `MetaMathlibExt.campbellConcatDigit_small`, a theorem declared in [WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#campbell-concat-digit-small).

## Campbell's constant

Let $h_2$ be Campbell's sequence. Campbell's constant is the real
number $\sum_{j \ge 0} d_j \, 10^{-(j+1)} = 0.d_0 d_1 d_2 \ldots$, where $d_0, d_1, d_2, \ldots$
are the digits after the decimal point of the concatenation $0.h_2(1)h_2(2)\ldots$ of the
base-$10$ digit blocks of $h_2(1), h_2(2), \ldots$ (with $0$ written as the single digit $0$).

## Sources

- John M. Campbell, *A Counterexample to a Purported Construction of Normal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.3.4, Theorem 8.

Formalized by `MetaMathlibExt.campbellConstant`, a definition declared in [WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#campbell-constant).

## Sums of $h_1$ and the jumps of $h_2$ at powers of ten

Let $h_1$ be Campbell's auxiliary
sequence and $h_2$ Campbell's sequence. For every integer $\ell \ge 1$,
$\sum_{i=1}^{10^{\ell+1}-1} h_1(i) = \sum_{j=0}^{\ell-1} 900 \cdot 100^j$, the number written
$9090\cdots900$ ($\ell$ blocks $90$, then $0$). Moreover, writing $y_1(n) = h_2(10^{n-1})$ and
$y_2(n) = h_2(10^n - 1)$, for every integer $\ell \ge 2$ we have
$(y_2(\ell) - y_1(\ell)) / (9 \cdot 10^{\ell-1} - 1) = 10^{\ell-1}$ and
$y_1(\ell + 1) - y_2(\ell) = 10^{2\lfloor \ell/2 \rfloor}$.

## Sources

- John M. Campbell, *A Counterexample to a Purported Construction of Normal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.3.4, Lemma 2 (`jis-2026-26.3.4-lem-2`).

Stated but not proved: `MetaMathlibExt.campbellH1_sum_and_y_relations` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#campbell-h1-sum-and-y-relations).

## The floor of Campbell's interpolation at positive integers is Campbell's sequence $h_2$

Let $f$ be Campbell's interpolation and $h_2$ Campbell's sequence. For every integer $n \ge 1$,
$\lfloor f(n) \rfloor = h_2(n)$, and for every integer $n \ge 10$, $f(n) = h_2(n)$.

## Sources

- John M. Campbell, *A Counterexample to a Purported Construction of Normal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.3.4, Lemma 3 (`jis-2026-26.3.4-lem-3`).

Stated but not proved: `MetaMathlibExt.floor_campbellF_eq_campbellH2` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#floor-campbell-f-eq-campbell-h2).

## Differentiability of Campbell's interpolation

Campbell's interpolation $f$ is
differentiable at every real $x > 0$.

## Sources

- John M. Campbell, *A Counterexample to a Purported Construction of Normal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.3.4, Lemma 4 (`jis-2026-26.3.4-lem-4`).

Stated but not proved: `MetaMathlibExt.campbellF_differentiableOn` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#campbell-f-differentiable-on).

## Monotonicity of Campbell's interpolation

Campbell's interpolation $f$ is monotone
(non-decreasing) on $[0, \infty)$: for all real numbers $x$ and $y$ with $0 \le x \le y$,
$f(x) \le f(y)$.

## Sources

- John M. Campbell, *A Counterexample to a Purported Construction of Normal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.3.4, Lemma 5 (`jis-2026-26.3.4-lem-5`).

Stated but not proved: `MetaMathlibExt.campbellF_monotoneOn` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#campbell-f-monotone-on).

## Growth exponent of Campbell's interpolation

For Campbell's interpolation $f$,
$\log f(x) / \log x \to 2$ as $x \to \infty$ over the reals; that is, $\eta(f) = 2$, where
$\eta(h) = \lim_{x \to \infty} \log h(x) / \log x$.

## Sources

- John M. Campbell, *A Counterexample to a Purported Construction of Normal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.3.4, Lemma 6 (`jis-2026-26.3.4-lem-6`).

Stated but not proved: `MetaMathlibExt.tendsto_log_campbellF_div_log` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#tendsto-log-campbell-f-div-log).

## Growth exponent of the derivative of Campbell's interpolation

For Campbell's
interpolation $f$, $\log f'(x) / \log x \to 1$ as $x \to \infty$ over the reals; that is,
$\eta(f') = 1$, where $\eta(h) = \lim_{x \to \infty} \log h(x) / \log x$. Here $f'(x)$ is taken
to be $0$ at any point where $f$ is not differentiable, and $\log 0 = 0$.

## Sources

- John M. Campbell, *A Counterexample to a Purported Construction of Normal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.3.4, Lemma 7 (`jis-2026-26.3.4-lem-7`).

Stated but not proved: `MetaMathlibExt.tendsto_log_deriv_campbellF_div_log` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#tendsto-log-deriv-campbell-f-div-log).

## Campbell's concatenation of $h_2$ is not normal in base $10$

Let $h_2$ be Campbell's
sequence and let $c_0, c_1, c_2, \ldots$ be the base-$10$ digits of $h_2(1), h_2(2), \ldots$,
each number written most significant digit first and the numbers written one after another (with
$h_2(n) = 0$ written as the single digit $0$). The real number
$\sum_{j \ge 0} c_j 10^{-(j+1)} = 0.c_0c_1c_2\ldots$ is not normal in base $10$.

## Sources

- John M. Campbell, *A Counterexample to a Purported Construction of Normal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.3.4, Theorem 8 (`jis-2026-26.3.4-thm-8`).

Stated but not proved: `MetaMathlibExt.not_isNormalInBase_campbellConstant` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SzuszVolkmannCounterexampleWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html#not-is-normal-in-base-campbell-constant).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Normal numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/normal-numbers)
