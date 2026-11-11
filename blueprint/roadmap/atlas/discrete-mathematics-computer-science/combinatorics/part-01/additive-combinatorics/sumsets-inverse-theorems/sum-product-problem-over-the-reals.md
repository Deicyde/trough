---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.RealSumProductExponentWanted.sumProductMaxCard, MathlibExt.Combinatorics.RealSumProductExponentWanted.sumProductRatio, MathlibExt.Combinatorics.RealSumProductExponentWanted.fixedCardinalityRatios, MathlibExt.Combinatorics.RealSumProductExponentWanted.sumProductLevelMinimum, MathlibExt.Combinatorics.RealSumProductExponentWanted.sumProductLevelMinimum_isLeast, MathlibExt.Combinatorics.RealSumProductExponentWanted.sumProductRatio_nonneg, MathlibExt.Combinatorics.RealSumProductExponentWanted.sumProductRatio_le_two, MathlibExt.Combinatorics.RealSumProductExponentWanted.sumProductLevelMinimum_nonneg
statement: formalized
---

# Sum-product problem over the reals

41 results, 28 proved and 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html).

## Size of the larger of the sumset and the product set

For a finite set $A$ of real
numbers, this is the natural number $\max(|A+A|, |AA|)$, where $A+A = \{a+b : a, b \in A\}$ is the
sumset and $AA = \{ab : a, b \in A\}$ is the product set of $A$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.sumProductMaxCard`, a definition declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#sum-product-max-card).

## Sum-product ratio

For a finite set $A$ of real numbers, the sum-product ratio of $A$ is
$\log \max(|A+A|, |AA|) / \log |A|$, where $A+A$ and $AA$ are the sumset and the product set of
$A$. With the conventions $\log 0 = 0$ and $x / 0 = 0$, the ratio is $0$ when $|A| \le 1$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.sumProductRatio`, a definition declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#sum-product-ratio).

## Sum-product ratios at a fixed cardinality

For a finite set $A \subset \mathbb{R}$ write
$A + A$ and $AA$ for the sets of all sums $a + b$ and all products $ab$ with $a, b \in A$. For a
natural number $n \ge 2$, this is the set of the real numbers
$\log \max(|A + A|, |AA|) / \log |A|$ for all sets $A \subset \mathbb{R}$ with $|A| = n$; for
$n \le 1$ it consists of the single number $0$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.fixedCardinalityRatios`, a definition declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#fixed-cardinality-ratios).

## Least sum-product ratio at a fixed cardinality

For a natural number $n$, the level
minimum $m(n)$ is the infimum of the sum-product ratios $\log \max(|A+A|, |AA|) / \log |A|$ over
all sets $A$ of $n$ real numbers, where $A+A$ and $AA$ are the sumset and the product set of $A$,
and the ratio is taken to be $0$ when $|A| \le 1$ (conventions $\log 0 = 0$ and $x / 0 = 0$).

The set of these ratios is finite and nonempty, so the infimum is attained.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.sumProductLevelMinimum`, a definition declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#sum-product-level-minimum).

## The level minimum is attained

For every natural number $n$, let $m(n)$ be the infimum of
the sum-product ratios $\log \max(|A+A|, |AA|) / \log |A|$ over all sets $A$ of $n$ real numbers,
where $A+A$ and $AA$ are the sumset and the product set of $A$ and the ratio is taken to be $0$
when $|A| \le 1$ (conventions $\log 0 = 0$ and $x / 0 = 0$). Then $m(n)$ is the least element of
the set of these ratios: it is the ratio of some set of $n$ real numbers, and no set of $n$ real
numbers has a smaller ratio.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.sumProductLevelMinimum_isLeast`, a theorem declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#sum-product-level-minimum-is-least).

## The sum-product ratio is nonnegative

For every nonempty finite set $A$ of real numbers,
the sum-product ratio $\log \max(|A+A|, |AA|) / \log |A|$ is at least $0$, where $A+A$ and $AA$
are the sumset and the product set of $A$, and the ratio is taken to be $0$ when $|A| = 1$
(conventions $\log 0 = 0$ and $x / 0 = 0$).

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.sumProductRatio_nonneg`, a theorem declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#sum-product-ratio-nonneg).

## The sum-product ratio is at most two

For every finite set $A$ of real numbers with
$|A| \ge 2$, the sum-product ratio $\log \max(|A+A|, |AA|) / \log |A|$ is at most $2$, where $A+A$
and $AA$ are the sumset and the product set of $A$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.sumProductRatio_le_two`, a theorem declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#sum-product-ratio-le-two).

## The level minimum is nonnegative

For every natural number $n \ge 1$, the level minimum
$m(n)$, the infimum of the sum-product ratios $\log \max(|A+A|, |AA|) / \log |A|$ over all sets $A$
of $n$ real numbers, satisfies $m(n) \ge 0$. Here $A+A$ and $AA$ are the sumset and the product set
of $A$, and the ratio is taken to be $0$ when $|A| = 1$ (conventions $\log 0 = 0$, $x / 0 = 0$).

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.sumProductLevelMinimum_nonneg`, a theorem declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#sum-product-level-minimum-nonneg).

## The level minimum is at most two

For every natural number $n \ge 2$, the level minimum
$m(n)$, the infimum of the sum-product ratios $\log \max(|A+A|, |AA|) / \log |A|$ over all sets $A$
of $n$ real numbers, where $A+A$ and $AA$ are the sumset and the product set of $A$, satisfies
$m(n) \le 2$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.sumProductLevelMinimum_le_two`, a theorem declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#sum-product-level-minimum-le-two).

## The sum-product level minima eventually lie in $(0, 2)$

For a finite set
$A \subset \mathbb{R}$ write $A + A$ and $AA$ for the sets of all sums $a + b$ and all products
$ab$ with $a, b \in A$. For a natural number $n \ge 2$ let $m_n$ be the least value of
$\log \max(|A + A|, |AA|) / \log n$ over sets $A \subset \mathbb{R}$ with $|A| = n$. Then
$0 \le m_n \le 2$ for every sufficiently large $n$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.eventually_sumProductLevelMinimum_mem_Icc`, a theorem declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#eventually-sum-product-level-minimum-mem).

## The level minima are eventually bounded above

There is a real number $b$ such that
$m(n) \le b$ for all sufficiently large natural numbers $n$, where the level minimum $m(n)$ is the
infimum of the sum-product ratios $\log \max(|A+A|, |AA|) / \log |A|$ over all sets $A$ of $n$
real numbers, and $A+A$ and $AA$ are the sumset and the product set of $A$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.sumProductLevelMinimum_isBoundedUnder_le`, a theorem declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#sum-product-level-minimum-is-bounded-und).

## The sum-product level minima are eventually bounded below

There is a real number $b$
such that the sum-product level minimum $m(n)$ satisfies $m(n) \ge b$ for all sufficiently large
$n$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.sumProductLevelMinimum_isBoundedUnder_ge`, a theorem declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#sum-product-level-minimum-is-bounded-und-2).

## Sum-product exponent of the reals

For $n \in \mathbb{N}$ let $m(n)$ be the sum-product
level minimum: the least value of $\log \max(|A + A|, |AA|) / \log |A|$ over sets
$A \subset \mathbb{R}$ with $n$ elements, where $A + A$ and $AA$ are the sets of sums $a + b$ and
products $ab$ of elements $a, b \in A$. The real sum-product exponent is
$\liminf_{n \to \infty} m(n)$.

For $n \le 1$ the conventions $\log 0 = 0$ and $x / 0 = 0$ give $m(n) = 0$; these levels do not
affect the limit inferior.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.sumProductExponent`, a definition declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#sum-product-exponent).

## The sum-product exponent ignores sets of size $0$ and $1$

Let $m(n)$ be the sum-product
level minimum at $n$. The real sum-product exponent equals $\liminf_{n \to \infty} m(n + 2)$, so
the levels $n = 0$ and $n = 1$ do not affect it.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.sumProductExponent_eq_liminf_add_two`, a theorem declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#sum-product-exponent-eq-liminf-add-two).

## Uniform sum-product lower growth at rate $s$

A real number $s$ has uniform sum-product
lower growth when for every $\varepsilon > 0$ there is a constant $K > 0$ such that every
nonempty finite set $A \subset \mathbb{R}$ satisfies
$K \cdot |A|^{s - \varepsilon} \le \max(|A + A|, |AA|)$, where $A + A$ and $AA$ are the sets of
sums $a + b$ and products $ab$ of elements $a, b \in A$.

The constant $K$ may depend on $\varepsilon$ but not on $A$. Requiring $A$ to be nonempty
avoids giving a meaning to $0^{s - \varepsilon}$; singleton sets are included.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.HasUniformSumProductLowerGrowth`, a definition declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#has-uniform-sum-product-lower-growth).

## Statement of the uniform-growth characterization of the real sum-product exponent

For a
finite set $A \subset \mathbb{R}$ write $A + A$ and $AA$ for the sets of all sums $a + b$ and all
products $ab$ with $a, b \in A$, and let the real sum-product exponent $C_{84b}$ be the limit
inferior, as $n \to \infty$, of the least value of $\log \max(|A + A|, |AA|) / \log n$ over sets
$A \subset \mathbb{R}$ with $|A| = n$. This is the proposition that $C_{84b}$ is the largest real
number $s$ with the following property: for every $\varepsilon > 0$ there is a constant $K > 0$
such that $K |A|^{s - \varepsilon} \le \max(|A + A|, |AA|)$ for every nonempty finite set
$A \subset \mathbb{R}$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.epsilonUniformLowerGrowthCharacterization`, a definition declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#epsilon-uniform-lower-growth-characteriz).

## Statement of the Erdős–Szemerédi conjecture for real sets

For a finite set
$A \subset \mathbb{R}$ write $A + A$ and $AA$ for the sets of all sums $a + b$ and all products
$ab$ with $a, b \in A$, and let the real sum-product exponent $C_{84b}$ be the limit inferior, as
$n \to \infty$, of the least value of $\log \max(|A + A|, |AA|) / \log n$ over sets
$A \subset \mathbb{R}$ with $|A| = n$. This is the proposition that $C_{84b} = 2$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.erdosSzemerediHistoricalConjecture`, a definition declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#erdos-szemeredi-historical-conjecture).

## Statement of the Bloom–Sawin–Schildkraut–Zhelezov refutation

The statement that the real
sum-product exponent $C$ satisfies $C < 2$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.bloomSawinSchildkrautZhelezovRefutation`, a definition declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#bloom-sawin-schildkraut-zhelezov-refutat).

## Statement of the upper bound two for the real sum-product exponent

For a finite set
$A \subset \mathbb{R}$ write $A + A$ and $AA$ for the sets of all sums $a + b$ and all products
$ab$ with $a, b \in A$, and let the real sum-product exponent $C_{84b}$ be the limit inferior, as
$n \to \infty$, of the least value of $\log \max(|A + A|, |AA|) / \log n$ over sets
$A \subset \mathbb{R}$ with $|A| = n$. This is the proposition that $C_{84b} \le 2$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.erdosSzemerediHistoricalUpperBound`, a definition declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#erdos-szemeredi-historical-upper-bound).

## Statement of the Bloom–Sawin–Schildkraut–Zhelezov upper bound

The statement that there is a
real number $c > 0$ such that the real sum-product exponent $C$ satisfies $C \le 2 - c$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.bloomSawinSchildkrautZhelezovUpperBound`, a definition declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#bloom-sawin-schildkraut-zhelezov-upper-b).

## Statement of the Bloom–Sawin–Schildkraut–Zhelezov numerical upper bound

The statement that
the real sum-product exponent $C$ satisfies $C \le 199999913/100000000$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.bloomSawinSchildkrautZhelezovNumericalUpperBound`, a definition declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#bloom-sawin-schildkraut-zhelezov-numeric).

## Statement of the trivial lower bound for the real sum-product exponent

For a finite set
$A \subset \mathbb{R}$ write $A + A$ and $AA$ for the sets of all sums $a + b$ and all products
$ab$ with $a, b \in A$. This is the proposition that the real sum-product exponent, the limit
inferior, as $n \to \infty$, of the least value of $\log \max(|A + A|, |AA|) / \log n$ over sets
$A \subset \mathbb{R}$ with $|A| = n$, is at least $1$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.trivialLowerBound`, a definition declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#trivial-lower-bound).

## Statement of Elekes's lower bound

For a finite set $A \subset \mathbb{R}$ write $A + A$
and $AA$ for the sets of all sums $a + b$ and all products $ab$ with $a, b \in A$, and let the real
sum-product exponent $C_{84b}$ be the limit inferior, as $n \to \infty$, of the least value of
$\log \max(|A + A|, |AA|) / \log n$ over sets $A \subset \mathbb{R}$ with $|A| = n$. This is the
proposition that $C_{84b} \ge 5/4$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.elekesLowerBound`, a definition declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#elekes-lower-bound).

## Statement of Solymosi's $14/11$ lower bound

The proposition that the real sum-product
exponent is at least $14/11$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.solymosiFourteenEleventhsLowerBound`, a definition declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#solymosi-fourteen-elevenths-lower-bound).

## Statement of Solymosi's $4/3$ lower bound

The proposition that the real sum-product
exponent is at least $4/3$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.solymosiFourThirdsLowerBound`, a definition declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#solymosi-four-thirds-lower-bound).

## Statement of the Rudnev–Stevens lower bound

The proposition that the real sum-product
exponent is at least $1558/1167 = 4/3 + 2/1167$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.rudnevStevensLowerBound`, a definition declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#rudnev-stevens-lower-bound).

## Statement of Bloom's lower bound for the real sum-product exponent

The statement that the
real sum-product exponent $C$ satisfies $1270/951 \le C$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.bloomLowerBound`, a definition declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#bloom-lower-bound).

## Statement of Cushman's lower bound for the real sum-product exponent

The statement that the
real sum-product exponent $C$ satisfies $4/3 + 10/4407 \le C$.

Formalized by `MathlibExt.Combinatorics.RealSumProductExponentWanted.cushmanCurrentLowerBound`, a definition declared in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#cushman-current-lower-bound).

## The real sum-product exponent is the largest uniform growth rate

For a finite set
$A \subset \mathbb{R}$ write $A + A$ and $AA$ for the sets of all sums $a + b$ and all products
$ab$ with $a, b \in A$, and let the real sum-product exponent $C_{84b}$ be the limit inferior, as
$n \to \infty$, of the least value of $\log \max(|A + A|, |AA|) / \log n$ over sets
$A \subset \mathbb{R}$ with $|A| = n$. Then $C_{84b}$ is the largest real number $s$ with the
following property: for every $\varepsilon > 0$ there is a constant $K > 0$ such that
$K |A|^{s - \varepsilon} \le \max(|A + A|, |AA|)$ for every nonempty finite set
$A \subset \mathbb{R}$.

Optimization Problems 84b gives this as an equivalent definition of $C_{84b}$.

## Sources

- Paul Erdős and Endre Szemerédi, On sums and products of integers, Studies in Pure Mathematics (1983), 213-218, https://doi.org/10.1007/978-3-0348-5438-2_19; György Elekes, On the number of sums and products, Acta Arithmetica 81 (1997), no. 4, 365-367, https://doi.org/10.4064/aa-81-4-365-367; József Solymosi, On the number of sums and products, Bulletin of the London Mathematical Society 37 (2005), no. 4, 491-494, https://doi.org/10.1112/S0024609305004261; József Solymosi, Bounding multiplicative energy by the sumset, Advances in Mathematics 222 (2009), no. 2, 402-408, https://doi.org/10.1016/j.aim.2009.04.006; Misha Rudnev and Sophie Stevens, An update on the sum-product problem, Mathematical Proceedings of the Cambridge Philosophical Society 173 (2022), no. 2, 411-430, https://arxiv.org/abs/2005.11145; Thomas F. Bloom, A history of the sum-product problem, https://thomasbloom.org/notes/sumproduct.html; Adam Cushman, A note on the sum-product problem and the convex sumset problem, arXiv:2512.13849 (2025), https://arxiv.org/abs/2512.13849; Thomas F. Bloom, Will Sawin, Carl Schildkraut, and Dmitrii Zhelezov, The sum-product conjecture is false for real numbers, arXiv:2605.28781 (2026), https://arxiv.org/abs/2605.28781; Optimization Problems, record 84b, Sum-product exponent for the reals, tables of known upper and lower bounds, https://github.com/teorth/optimizationproblems/blob/2c1968cd520b60f1cf3cf50749f7285e800e4e15/constants/84b.md.

Stated but not proved: `MathlibExt.Combinatorics.RealSumProductExponentWanted.epsilonUniformLowerGrowthCharacterization_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#epsilon-uniform-lower-growth-characteriz-2).

## The Erdős–Szemerédi conjecture fails for real sets

For a finite set $A \subset \mathbb{R}$
write $A + A$ and $AA$ for the sets of all sums $a + b$ and all products $ab$ with $a, b \in A$,
and let the real sum-product exponent $C_{84b}$ be the limit inferior, as $n \to \infty$, of the
least value of $\log \max(|A + A|, |AA|) / \log n$ over sets $A \subset \mathbb{R}$ with
$|A| = n$. Then $C_{84b} \ne 2$.

Bloom, Sawin, Schildkraut and Zhelezov construct arbitrarily large finite sets
$A \subset \mathbb{R}$ with $\max(|A + A|, |AA|) \le |A|^{2 - c}$ for an absolute constant $c > 0$,
so $C_{84b} \le 2 - c$.

## Sources

- Paul Erdős and Endre Szemerédi, On sums and products of integers, Studies in Pure Mathematics (1983), 213-218, https://doi.org/10.1007/978-3-0348-5438-2_19; György Elekes, On the number of sums and products, Acta Arithmetica 81 (1997), no. 4, 365-367, https://doi.org/10.4064/aa-81-4-365-367; József Solymosi, On the number of sums and products, Bulletin of the London Mathematical Society 37 (2005), no. 4, 491-494, https://doi.org/10.1112/S0024609305004261; József Solymosi, Bounding multiplicative energy by the sumset, Advances in Mathematics 222 (2009), no. 2, 402-408, https://doi.org/10.1016/j.aim.2009.04.006; Misha Rudnev and Sophie Stevens, An update on the sum-product problem, Mathematical Proceedings of the Cambridge Philosophical Society 173 (2022), no. 2, 411-430, https://arxiv.org/abs/2005.11145; Thomas F. Bloom, A history of the sum-product problem, https://thomasbloom.org/notes/sumproduct.html; Adam Cushman, A note on the sum-product problem and the convex sumset problem, arXiv:2512.13849 (2025), https://arxiv.org/abs/2512.13849; Thomas F. Bloom, Will Sawin, Carl Schildkraut, and Dmitrii Zhelezov, The sum-product conjecture is false for real numbers, arXiv:2605.28781 (2026), https://arxiv.org/abs/2605.28781; Optimization Problems, record 84b, Sum-product exponent for the reals, tables of known upper and lower bounds, https://github.com/teorth/optimizationproblems/blob/2c1968cd520b60f1cf3cf50749f7285e800e4e15/constants/84b.md.

Stated but not proved: `MathlibExt.Combinatorics.RealSumProductExponentWanted.erdosSzemerediHistoricalConjecture_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#erdos-szemeredi-historical-conjecture-re).

## The real sum-product exponent is less than 2 (Bloom–Sawin–Schildkraut–Zhelezov)

The real
sum-product exponent $C$ satisfies $C < 2$. Here, for a finite set $A \subset \mathbb{R}$,
$A + A$ and $A \cdot A$ are the sets of sums $a + b$ and products $ab$ with $a, b \in A$, and
$M(A) = \max(|A + A|, |A \cdot A|)$; for $n \ge 2$, $m(n)$ is the minimum of
$\log M(A) / \log |A|$ over all $A \subset \mathbb{R}$ with $|A| = n$; and
$C = \liminf_{n \to \infty} m(n)$.

This refutes the historical Erdős–Szemerédi conjecture $C = 2$ for real sets: Bloom, Sawin,
Schildkraut and Zhelezov (arXiv:2605.28781) construct arbitrarily large finite sets
$A \subset \mathbb{R}$ with $M(A) \le |A|^{2 - c}$ for an absolute constant $c > 0$.

## Sources

- Paul Erdős and Endre Szemerédi, On sums and products of integers, Studies in Pure Mathematics (1983), 213-218, https://doi.org/10.1007/978-3-0348-5438-2_19; György Elekes, On the number of sums and products, Acta Arithmetica 81 (1997), no. 4, 365-367, https://doi.org/10.4064/aa-81-4-365-367; József Solymosi, On the number of sums and products, Bulletin of the London Mathematical Society 37 (2005), no. 4, 491-494, https://doi.org/10.1112/S0024609305004261; József Solymosi, Bounding multiplicative energy by the sumset, Advances in Mathematics 222 (2009), no. 2, 402-408, https://doi.org/10.1016/j.aim.2009.04.006; Misha Rudnev and Sophie Stevens, An update on the sum-product problem, Mathematical Proceedings of the Cambridge Philosophical Society 173 (2022), no. 2, 411-430, https://arxiv.org/abs/2005.11145; Thomas F. Bloom, A history of the sum-product problem, https://thomasbloom.org/notes/sumproduct.html; Adam Cushman, A note on the sum-product problem and the convex sumset problem, arXiv:2512.13849 (2025), https://arxiv.org/abs/2512.13849; Thomas F. Bloom, Will Sawin, Carl Schildkraut, and Dmitrii Zhelezov, The sum-product conjecture is false for real numbers, arXiv:2605.28781 (2026), https://arxiv.org/abs/2605.28781; Optimization Problems, record 84b, Sum-product exponent for the reals, tables of known upper and lower bounds, https://github.com/teorth/optimizationproblems/blob/2c1968cd520b60f1cf3cf50749f7285e800e4e15/constants/84b.md.

Stated but not proved: `MathlibExt.Combinatorics.RealSumProductExponentWanted.bloomSawinSchildkrautZhelezovRefutation_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#bloom-sawin-schildkraut-zhelezov-refutat-2).

## The real sum-product exponent is at most two

For a finite set $A \subset \mathbb{R}$ write
$A + A$ and $AA$ for the sets of all sums $a + b$ and all products $ab$ with $a, b \in A$, and
let the real sum-product exponent $C_{84b}$ be the limit inferior, as $n \to \infty$, of the least
value of $\log \max(|A + A|, |AA|) / \log n$ over sets $A \subset \mathbb{R}$ with $|A| = n$.
Then $C_{84b} \le 2$.

This follows from $|A + A| \le |A|^2$ and $|AA| \le |A|^2$; Optimization Problems 84b records it
as the upper bound of Erdős and Szemerédi (1983).

## Sources

- Paul Erdős and Endre Szemerédi, On sums and products of integers, Studies in Pure Mathematics (1983), 213-218, https://doi.org/10.1007/978-3-0348-5438-2_19; György Elekes, On the number of sums and products, Acta Arithmetica 81 (1997), no. 4, 365-367, https://doi.org/10.4064/aa-81-4-365-367; József Solymosi, On the number of sums and products, Bulletin of the London Mathematical Society 37 (2005), no. 4, 491-494, https://doi.org/10.1112/S0024609305004261; József Solymosi, Bounding multiplicative energy by the sumset, Advances in Mathematics 222 (2009), no. 2, 402-408, https://doi.org/10.1016/j.aim.2009.04.006; Misha Rudnev and Sophie Stevens, An update on the sum-product problem, Mathematical Proceedings of the Cambridge Philosophical Society 173 (2022), no. 2, 411-430, https://arxiv.org/abs/2005.11145; Thomas F. Bloom, A history of the sum-product problem, https://thomasbloom.org/notes/sumproduct.html; Adam Cushman, A note on the sum-product problem and the convex sumset problem, arXiv:2512.13849 (2025), https://arxiv.org/abs/2512.13849; Thomas F. Bloom, Will Sawin, Carl Schildkraut, and Dmitrii Zhelezov, The sum-product conjecture is false for real numbers, arXiv:2605.28781 (2026), https://arxiv.org/abs/2605.28781; Optimization Problems, record 84b, Sum-product exponent for the reals, tables of known upper and lower bounds, https://github.com/teorth/optimizationproblems/blob/2c1968cd520b60f1cf3cf50749f7285e800e4e15/constants/84b.md.

Stated but not proved: `MathlibExt.Combinatorics.RealSumProductExponentWanted.erdosSzemerediHistoricalUpperBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#erdos-szemeredi-historical-upper-bound-h).

## Bloom–Sawin–Schildkraut–Zhelezov upper bound for the real sum-product exponent

There is a
real number $c > 0$ such that the real sum-product exponent $C$ satisfies $C \le 2 - c$. Here,
for a finite set $A \subset \mathbb{R}$, $A + A$ and $A \cdot A$ are the sets of sums $a + b$
and products $ab$ with $a, b \in A$, and $M(A) = \max(|A + A|, |A \cdot A|)$; for $n \ge 2$,
$m(n)$ is the minimum of $\log M(A) / \log |A|$ over all $A \subset \mathbb{R}$ with
$|A| = n$; and $C = \liminf_{n \to \infty} m(n)$.

Bloom, Sawin, Schildkraut and Zhelezov (arXiv:2605.28781) construct arbitrarily large finite
sets $A \subset \mathbb{R}$ with $M(A) \le |A|^{2 - c}$ for an absolute constant $c > 0$;
Optimization Problems 84b lists the resulting upper bound $2 - c$.

## Sources

- Paul Erdős and Endre Szemerédi, On sums and products of integers, Studies in Pure Mathematics (1983), 213-218, https://doi.org/10.1007/978-3-0348-5438-2_19; György Elekes, On the number of sums and products, Acta Arithmetica 81 (1997), no. 4, 365-367, https://doi.org/10.4064/aa-81-4-365-367; József Solymosi, On the number of sums and products, Bulletin of the London Mathematical Society 37 (2005), no. 4, 491-494, https://doi.org/10.1112/S0024609305004261; József Solymosi, Bounding multiplicative energy by the sumset, Advances in Mathematics 222 (2009), no. 2, 402-408, https://doi.org/10.1016/j.aim.2009.04.006; Misha Rudnev and Sophie Stevens, An update on the sum-product problem, Mathematical Proceedings of the Cambridge Philosophical Society 173 (2022), no. 2, 411-430, https://arxiv.org/abs/2005.11145; Thomas F. Bloom, A history of the sum-product problem, https://thomasbloom.org/notes/sumproduct.html; Adam Cushman, A note on the sum-product problem and the convex sumset problem, arXiv:2512.13849 (2025), https://arxiv.org/abs/2512.13849; Thomas F. Bloom, Will Sawin, Carl Schildkraut, and Dmitrii Zhelezov, The sum-product conjecture is false for real numbers, arXiv:2605.28781 (2026), https://arxiv.org/abs/2605.28781; Optimization Problems, record 84b, Sum-product exponent for the reals, tables of known upper and lower bounds, https://github.com/teorth/optimizationproblems/blob/2c1968cd520b60f1cf3cf50749f7285e800e4e15/constants/84b.md.

Stated but not proved: `MathlibExt.Combinatorics.RealSumProductExponentWanted.bloomSawinSchildkrautZhelezovUpperBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#bloom-sawin-schildkraut-zhelezov-upper-b-2).

## Bloom–Sawin–Schildkraut–Zhelezov numerical upper bound for the real sum-product exponent

The
real sum-product exponent $C$ satisfies $C \le 199999913/100000000 = 1.99999913$. Here, for a
finite set $A \subset \mathbb{R}$, $A + A$ and $A \cdot A$ are the sets of sums $a + b$ and
products $ab$ with $a, b \in A$, and $M(A) = \max(|A + A|, |A \cdot A|)$; for $n \ge 2$, $m(n)$
is the minimum of $\log M(A) / \log |A|$ over all $A \subset \mathbb{R}$ with $|A| = n$; and
$C = \liminf_{n \to \infty} m(n)$.

Bloom, Sawin, Schildkraut and Zhelezov sketch, in the section "Numerical estimates" of
arXiv:2605.28781, a quantified version of their construction that gives arbitrarily large finite
sets $A \subset \mathbb{R}$ with $M(A) \le |A|^{2 - 0.00000087}$; they call this value
non-optimized. Optimization Problems 84b lists it as the explicit upper bound $1.99999913$.

## Sources

- Paul Erdős and Endre Szemerédi, On sums and products of integers, Studies in Pure Mathematics (1983), 213-218, https://doi.org/10.1007/978-3-0348-5438-2_19; György Elekes, On the number of sums and products, Acta Arithmetica 81 (1997), no. 4, 365-367, https://doi.org/10.4064/aa-81-4-365-367; József Solymosi, On the number of sums and products, Bulletin of the London Mathematical Society 37 (2005), no. 4, 491-494, https://doi.org/10.1112/S0024609305004261; József Solymosi, Bounding multiplicative energy by the sumset, Advances in Mathematics 222 (2009), no. 2, 402-408, https://doi.org/10.1016/j.aim.2009.04.006; Misha Rudnev and Sophie Stevens, An update on the sum-product problem, Mathematical Proceedings of the Cambridge Philosophical Society 173 (2022), no. 2, 411-430, https://arxiv.org/abs/2005.11145; Thomas F. Bloom, A history of the sum-product problem, https://thomasbloom.org/notes/sumproduct.html; Adam Cushman, A note on the sum-product problem and the convex sumset problem, arXiv:2512.13849 (2025), https://arxiv.org/abs/2512.13849; Thomas F. Bloom, Will Sawin, Carl Schildkraut, and Dmitrii Zhelezov, The sum-product conjecture is false for real numbers, arXiv:2605.28781 (2026), https://arxiv.org/abs/2605.28781; Optimization Problems, record 84b, Sum-product exponent for the reals, tables of known upper and lower bounds, https://github.com/teorth/optimizationproblems/blob/2c1968cd520b60f1cf3cf50749f7285e800e4e15/constants/84b.md.

Stated but not proved: `MathlibExt.Combinatorics.RealSumProductExponentWanted.bloomSawinSchildkrautZhelezovNumericalUpperBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#bloom-sawin-schildkraut-zhelezov-numeric-2).

## Trivial lower bound for the real sum-product exponent

The real sum-product exponent is at
least $1$. Here the exponent is $\liminf_{n \to \infty} m(n)$, where $m(n)$ is the infimum of
$\log \max(|A+A|, |AA|) / \log |A|$ over all sets $A$ of $n$ real numbers, and $A+A$ and $AA$ are
the sumset and the product set of $A$.

Optimization Problems 84b lists this bound as trivial, since $|A+A| \ge 2|A| - 1$.

## Sources

- Paul Erdős and Endre Szemerédi, On sums and products of integers, Studies in Pure Mathematics (1983), 213-218, https://doi.org/10.1007/978-3-0348-5438-2_19; György Elekes, On the number of sums and products, Acta Arithmetica 81 (1997), no. 4, 365-367, https://doi.org/10.4064/aa-81-4-365-367; József Solymosi, On the number of sums and products, Bulletin of the London Mathematical Society 37 (2005), no. 4, 491-494, https://doi.org/10.1112/S0024609305004261; József Solymosi, Bounding multiplicative energy by the sumset, Advances in Mathematics 222 (2009), no. 2, 402-408, https://doi.org/10.1016/j.aim.2009.04.006; Misha Rudnev and Sophie Stevens, An update on the sum-product problem, Mathematical Proceedings of the Cambridge Philosophical Society 173 (2022), no. 2, 411-430, https://arxiv.org/abs/2005.11145; Thomas F. Bloom, A history of the sum-product problem, https://thomasbloom.org/notes/sumproduct.html; Adam Cushman, A note on the sum-product problem and the convex sumset problem, arXiv:2512.13849 (2025), https://arxiv.org/abs/2512.13849; Thomas F. Bloom, Will Sawin, Carl Schildkraut, and Dmitrii Zhelezov, The sum-product conjecture is false for real numbers, arXiv:2605.28781 (2026), https://arxiv.org/abs/2605.28781; Optimization Problems, record 84b, Sum-product exponent for the reals, tables of known upper and lower bounds, https://github.com/teorth/optimizationproblems/blob/2c1968cd520b60f1cf3cf50749f7285e800e4e15/constants/84b.md.

Stated but not proved: `MathlibExt.Combinatorics.RealSumProductExponentWanted.trivialLowerBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 484](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L484). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#trivial-lower-bound-holds).

## Elekes's lower bound for the real sum-product exponent

For a finite set $A \subset \mathbb{R}$
write $A + A$ and $AA$ for the sets of all sums $a + b$ and all products $ab$ with $a, b \in A$,
and let the real sum-product exponent $C_{84b}$ be the limit inferior, as $n \to \infty$, of the
least value of $\log \max(|A + A|, |AA|) / \log n$ over sets $A \subset \mathbb{R}$ with
$|A| = n$. Then $C_{84b} \ge 5/4$.

Elekes proved, using the Szemerédi–Trotter theorem, that $\max(|A + A|, |AA|) \gg |A|^{5/4}$ for
finite sets $A \subset \mathbb{R}$.

## Sources

- Paul Erdős and Endre Szemerédi, On sums and products of integers, Studies in Pure Mathematics (1983), 213-218, https://doi.org/10.1007/978-3-0348-5438-2_19; György Elekes, On the number of sums and products, Acta Arithmetica 81 (1997), no. 4, 365-367, https://doi.org/10.4064/aa-81-4-365-367; József Solymosi, On the number of sums and products, Bulletin of the London Mathematical Society 37 (2005), no. 4, 491-494, https://doi.org/10.1112/S0024609305004261; József Solymosi, Bounding multiplicative energy by the sumset, Advances in Mathematics 222 (2009), no. 2, 402-408, https://doi.org/10.1016/j.aim.2009.04.006; Misha Rudnev and Sophie Stevens, An update on the sum-product problem, Mathematical Proceedings of the Cambridge Philosophical Society 173 (2022), no. 2, 411-430, https://arxiv.org/abs/2005.11145; Thomas F. Bloom, A history of the sum-product problem, https://thomasbloom.org/notes/sumproduct.html; Adam Cushman, A note on the sum-product problem and the convex sumset problem, arXiv:2512.13849 (2025), https://arxiv.org/abs/2512.13849; Thomas F. Bloom, Will Sawin, Carl Schildkraut, and Dmitrii Zhelezov, The sum-product conjecture is false for real numbers, arXiv:2605.28781 (2026), https://arxiv.org/abs/2605.28781; Optimization Problems, record 84b, Sum-product exponent for the reals, tables of known upper and lower bounds, https://github.com/teorth/optimizationproblems/blob/2c1968cd520b60f1cf3cf50749f7285e800e4e15/constants/84b.md.

Stated but not proved: `MathlibExt.Combinatorics.RealSumProductExponentWanted.elekesLowerBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 517](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L517). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#elekes-lower-bound-holds).

## Solymosi's $14/11$ lower bound for the real sum-product exponent

Let $C$ be the real
sum-product exponent: the limit inferior, as $n \to \infty$, of the least value of
$\log \max(|A + A|, |AA|) / \log |A|$ over $n$-element sets $A \subset \mathbb{R}$, where
$A + A$ and $AA$ are the sets of sums $a + b$ and products $ab$ of elements $a, b \in A$. Then
$C \ge 14/11$.

Optimization Problems 84b lists the lower bound $14/11$ [So05] (Solymosi, Bull. London Math.
Soc. 37 (2005)); Bloom's history lists Solymosi 2005 with exponent $1 + 3/11$.

## Sources

- Paul Erdős and Endre Szemerédi, On sums and products of integers, Studies in Pure Mathematics (1983), 213-218, https://doi.org/10.1007/978-3-0348-5438-2_19; György Elekes, On the number of sums and products, Acta Arithmetica 81 (1997), no. 4, 365-367, https://doi.org/10.4064/aa-81-4-365-367; József Solymosi, On the number of sums and products, Bulletin of the London Mathematical Society 37 (2005), no. 4, 491-494, https://doi.org/10.1112/S0024609305004261; József Solymosi, Bounding multiplicative energy by the sumset, Advances in Mathematics 222 (2009), no. 2, 402-408, https://doi.org/10.1016/j.aim.2009.04.006; Misha Rudnev and Sophie Stevens, An update on the sum-product problem, Mathematical Proceedings of the Cambridge Philosophical Society 173 (2022), no. 2, 411-430, https://arxiv.org/abs/2005.11145; Thomas F. Bloom, A history of the sum-product problem, https://thomasbloom.org/notes/sumproduct.html; Adam Cushman, A note on the sum-product problem and the convex sumset problem, arXiv:2512.13849 (2025), https://arxiv.org/abs/2512.13849; Thomas F. Bloom, Will Sawin, Carl Schildkraut, and Dmitrii Zhelezov, The sum-product conjecture is false for real numbers, arXiv:2605.28781 (2026), https://arxiv.org/abs/2605.28781; Optimization Problems, record 84b, Sum-product exponent for the reals, tables of known upper and lower bounds, https://github.com/teorth/optimizationproblems/blob/2c1968cd520b60f1cf3cf50749f7285e800e4e15/constants/84b.md.

Stated but not proved: `MathlibExt.Combinatorics.RealSumProductExponentWanted.solymosiFourteenEleventhsLowerBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 550](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L550). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#solymosi-fourteen-elevenths-lower-bound-2).

## Solymosi's $4/3$ lower bound for the real sum-product exponent

Let $C$ be the real
sum-product exponent: the limit inferior, as $n \to \infty$, of the least value of
$\log \max(|A + A|, |AA|) / \log |A|$ over $n$-element sets $A \subset \mathbb{R}$, where
$A + A$ and $AA$ are the sets of sums $a + b$ and products $ab$ of elements $a, b \in A$. Then
$C \ge 4/3$.

Optimization Problems 84b lists the lower bound $4/3$ [So09] (Solymosi, Adv. Math. 222 (2009));
Bloom's history lists Solymosi 2009 with exponent $1 + 1/3$.

## Sources

- Paul Erdős and Endre Szemerédi, On sums and products of integers, Studies in Pure Mathematics (1983), 213-218, https://doi.org/10.1007/978-3-0348-5438-2_19; György Elekes, On the number of sums and products, Acta Arithmetica 81 (1997), no. 4, 365-367, https://doi.org/10.4064/aa-81-4-365-367; József Solymosi, On the number of sums and products, Bulletin of the London Mathematical Society 37 (2005), no. 4, 491-494, https://doi.org/10.1112/S0024609305004261; József Solymosi, Bounding multiplicative energy by the sumset, Advances in Mathematics 222 (2009), no. 2, 402-408, https://doi.org/10.1016/j.aim.2009.04.006; Misha Rudnev and Sophie Stevens, An update on the sum-product problem, Mathematical Proceedings of the Cambridge Philosophical Society 173 (2022), no. 2, 411-430, https://arxiv.org/abs/2005.11145; Thomas F. Bloom, A history of the sum-product problem, https://thomasbloom.org/notes/sumproduct.html; Adam Cushman, A note on the sum-product problem and the convex sumset problem, arXiv:2512.13849 (2025), https://arxiv.org/abs/2512.13849; Thomas F. Bloom, Will Sawin, Carl Schildkraut, and Dmitrii Zhelezov, The sum-product conjecture is false for real numbers, arXiv:2605.28781 (2026), https://arxiv.org/abs/2605.28781; Optimization Problems, record 84b, Sum-product exponent for the reals, tables of known upper and lower bounds, https://github.com/teorth/optimizationproblems/blob/2c1968cd520b60f1cf3cf50749f7285e800e4e15/constants/84b.md.

Stated but not proved: `MathlibExt.Combinatorics.RealSumProductExponentWanted.solymosiFourThirdsLowerBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 583](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L583). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#solymosi-four-thirds-lower-bound-holds).

## Rudnev–Stevens lower bound for the real sum-product exponent

Let $C$ be the real
sum-product exponent: the limit inferior, as $n \to \infty$, of the least value of
$\log \max(|A + A|, |AA|) / \log |A|$ over $n$-element sets $A \subset \mathbb{R}$, where
$A + A$ and $AA$ are the sets of sums $a + b$ and products $ab$ of elements $a, b \in A$. Then
$C \ge 1558/1167$.

Rudnev and Stevens (arXiv:2005.11145, abstract) prove
$\max(|A + A|, |AA|) \ge |A|^{4/3 + 2/1167 - o(1)}$ for finite $A \subset \mathbb{R}$, and
$4/3 + 2/1167 = 1558/1167$; Optimization Problems 84b lists this bound [RuSt22].

## Sources

- Paul Erdős and Endre Szemerédi, On sums and products of integers, Studies in Pure Mathematics (1983), 213-218, https://doi.org/10.1007/978-3-0348-5438-2_19; György Elekes, On the number of sums and products, Acta Arithmetica 81 (1997), no. 4, 365-367, https://doi.org/10.4064/aa-81-4-365-367; József Solymosi, On the number of sums and products, Bulletin of the London Mathematical Society 37 (2005), no. 4, 491-494, https://doi.org/10.1112/S0024609305004261; József Solymosi, Bounding multiplicative energy by the sumset, Advances in Mathematics 222 (2009), no. 2, 402-408, https://doi.org/10.1016/j.aim.2009.04.006; Misha Rudnev and Sophie Stevens, An update on the sum-product problem, Mathematical Proceedings of the Cambridge Philosophical Society 173 (2022), no. 2, 411-430, https://arxiv.org/abs/2005.11145; Thomas F. Bloom, A history of the sum-product problem, https://thomasbloom.org/notes/sumproduct.html; Adam Cushman, A note on the sum-product problem and the convex sumset problem, arXiv:2512.13849 (2025), https://arxiv.org/abs/2512.13849; Thomas F. Bloom, Will Sawin, Carl Schildkraut, and Dmitrii Zhelezov, The sum-product conjecture is false for real numbers, arXiv:2605.28781 (2026), https://arxiv.org/abs/2605.28781; Optimization Problems, record 84b, Sum-product exponent for the reals, tables of known upper and lower bounds, https://github.com/teorth/optimizationproblems/blob/2c1968cd520b60f1cf3cf50749f7285e800e4e15/constants/84b.md.

Stated but not proved: `MathlibExt.Combinatorics.RealSumProductExponentWanted.rudnevStevensLowerBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 616](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L616). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#rudnev-stevens-lower-bound-holds).

## Bloom's lower bound for the real sum-product exponent

The real sum-product exponent $C$ is
at least $1270/951$. Here, for a finite set $A \subset \mathbb{R}$, $A + A$ and $A \cdot A$ are
the sets of sums $a + b$ and products $ab$ with $a, b \in A$, and
$M(A) = \max(|A + A|, |A \cdot A|)$; for $n \ge 2$, $m(n)$ is the minimum of
$\log M(A) / \log |A|$ over all $A \subset \mathbb{R}$ with $|A| = n$; and
$C = \liminf_{n \to \infty} m(n)$.

Optimization Problems 84b lists this lower bound as Bloom 2025; Bloom's history of the
sum-product problem attributes it to Bloom, Control and its applications in additive
combinatorics. It also follows from Cushman's larger lower bound $4/3 + 10/4407$.

## Sources

- Paul Erdős and Endre Szemerédi, On sums and products of integers, Studies in Pure Mathematics (1983), 213-218, https://doi.org/10.1007/978-3-0348-5438-2_19; György Elekes, On the number of sums and products, Acta Arithmetica 81 (1997), no. 4, 365-367, https://doi.org/10.4064/aa-81-4-365-367; József Solymosi, On the number of sums and products, Bulletin of the London Mathematical Society 37 (2005), no. 4, 491-494, https://doi.org/10.1112/S0024609305004261; József Solymosi, Bounding multiplicative energy by the sumset, Advances in Mathematics 222 (2009), no. 2, 402-408, https://doi.org/10.1016/j.aim.2009.04.006; Misha Rudnev and Sophie Stevens, An update on the sum-product problem, Mathematical Proceedings of the Cambridge Philosophical Society 173 (2022), no. 2, 411-430, https://arxiv.org/abs/2005.11145; Thomas F. Bloom, A history of the sum-product problem, https://thomasbloom.org/notes/sumproduct.html; Adam Cushman, A note on the sum-product problem and the convex sumset problem, arXiv:2512.13849 (2025), https://arxiv.org/abs/2512.13849; Thomas F. Bloom, Will Sawin, Carl Schildkraut, and Dmitrii Zhelezov, The sum-product conjecture is false for real numbers, arXiv:2605.28781 (2026), https://arxiv.org/abs/2605.28781; Optimization Problems, record 84b, Sum-product exponent for the reals, tables of known upper and lower bounds, https://github.com/teorth/optimizationproblems/blob/2c1968cd520b60f1cf3cf50749f7285e800e4e15/constants/84b.md.

Stated but not proved: `MathlibExt.Combinatorics.RealSumProductExponentWanted.bloomLowerBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 650](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L650). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#bloom-lower-bound-holds).

## Cushman's lower bound for the real sum-product exponent

The real sum-product exponent $C$ is
at least $4/3 + 10/4407$. Here, for a finite set $A \subset \mathbb{R}$, $A + A$ and $A \cdot A$
are the sets of sums $a + b$ and products $ab$ with $a, b \in A$, and
$M(A) = \max(|A + A|, |A \cdot A|)$; for $n \ge 2$, $m(n)$ is the minimum of
$\log M(A) / \log |A|$ over all $A \subset \mathbb{R}$ with $|A| = n$; and
$C = \liminf_{n \to \infty} m(n)$.

Cushman (arXiv:2512.13849) proves $M(A) \gg_\varepsilon |A|^{4/3 + 10/4407 - \varepsilon}$ for
every finite $A \subset \mathbb{R}$; Optimization Problems 84b lists this as the current record.

## Sources

- Paul Erdős and Endre Szemerédi, On sums and products of integers, Studies in Pure Mathematics (1983), 213-218, https://doi.org/10.1007/978-3-0348-5438-2_19; György Elekes, On the number of sums and products, Acta Arithmetica 81 (1997), no. 4, 365-367, https://doi.org/10.4064/aa-81-4-365-367; József Solymosi, On the number of sums and products, Bulletin of the London Mathematical Society 37 (2005), no. 4, 491-494, https://doi.org/10.1112/S0024609305004261; József Solymosi, Bounding multiplicative energy by the sumset, Advances in Mathematics 222 (2009), no. 2, 402-408, https://doi.org/10.1016/j.aim.2009.04.006; Misha Rudnev and Sophie Stevens, An update on the sum-product problem, Mathematical Proceedings of the Cambridge Philosophical Society 173 (2022), no. 2, 411-430, https://arxiv.org/abs/2005.11145; Thomas F. Bloom, A history of the sum-product problem, https://thomasbloom.org/notes/sumproduct.html; Adam Cushman, A note on the sum-product problem and the convex sumset problem, arXiv:2512.13849 (2025), https://arxiv.org/abs/2512.13849; Thomas F. Bloom, Will Sawin, Carl Schildkraut, and Dmitrii Zhelezov, The sum-product conjecture is false for real numbers, arXiv:2605.28781 (2026), https://arxiv.org/abs/2605.28781; Optimization Problems, record 84b, Sum-product exponent for the reals, tables of known upper and lower bounds, https://github.com/teorth/optimizationproblems/blob/2c1968cd520b60f1cf3cf50749f7285e800e4e15/constants/84b.md.

Stated but not proved: `MathlibExt.Combinatorics.RealSumProductExponentWanted.cushmanCurrentLowerBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/RealSumProductExponentWanted.lean, line 683](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/RealSumProductExponentWanted.lean#L683). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html#cushman-current-lower-bound-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sum-product problem over the reals](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sum-product-problem-over-the-reals)
