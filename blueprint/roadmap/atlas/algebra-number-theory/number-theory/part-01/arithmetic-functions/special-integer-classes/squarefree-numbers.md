---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30LocalCoeff, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30Coeff, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30NonSquarefreeTerm, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30OddTerm, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30SignedCoeff, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30SquarefreeTerm, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30LocalCoeff_zero, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30LocalCoeff_one
statement: formalized
---

# Squarefree numbers

33 results, 32 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html).

## Local factor

Given $a : \mathbb{N} \to \mathbb{C}$ and natural numbers $p$ and $e$,
the local factor of $a$ at $p$ with exponent $e$ is $1$ if $e = 0$, $a(p)$ if $e = 1$, and $0$
if $e \ge 2$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30LocalCoeff`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-local-coeff).

## Coefficients for Entry 30

For a function $a : \mathbb{N} \to \mathbb{C}$ and
$n \in \mathbb{N}$, the Entry 30 coefficient $c_a(n) \in \mathbb{C}$ is $0$ when $n = 0$. When
$n \ne 0$ it is the product, over the prime factors $p$ of $n$, of the local factor of $a$ at $p$
with exponent the multiplicity of $p$ in $n$. The local factor at $p$ with exponent $e$ is $1$
for $e = 0$, $a(p)$ for $e = 1$, and $0$ for $e \ge 2$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30Coeff`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-coeff).

## Terms of the Dirichlet series over non-squarefree integers

For $s \in \mathbb{C}$ and a
natural number $j$, put $n = j + 1$; the $j$-th term is $0$ if $n$ is squarefree and $n^{-s}$
otherwise. As $j$ ranges over the natural numbers, these are the terms of $\sum n^{-s}$ over
non-squarefree $n \ge 1$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30NonSquarefreeTerm`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-non-squarefree-term).

## Terms over squarefree integers with an odd number of prime factors

For $s \in \mathbb{C}$
and a natural number $j$, put $n = j + 1$; the $j$-th term is $n^{-s}$ if $n$ is squarefree and
has an odd number of distinct prime factors, and $0$ otherwise. As $j$ ranges over the natural
numbers, these are the terms of $\sum n^{-s}$ over squarefree $n \ge 1$ with an odd number of
prime factors.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30OddTerm`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-odd-term).

## Signed multiplicative coefficient

For $s \in \mathbb{C}$ and a natural number $n$, let
$a(p) = -p^{-s}$ for natural numbers $p$. The signed coefficient of $n$ is $0$ if $n = 0$ and,
for $n \ne 0$, the product over the prime factors $p$ of $n$ of the local factor of $a$ at $p$
with exponent the multiplicity of $p$ in $n$, where the local factor of $a$ at $p$ with exponent
$e$ is $1$ for $e = 0$, $a(p)$ for $e = 1$, and $0$ for $e \ge 2$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30SignedCoeff`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-signed-coeff).

## Terms of the Dirichlet series over squarefree integers

For a complex number $s$ and a
natural number $j$, let $n = j + 1$; the $j$-th squarefree term is $n^{-s}$ if $n$ is squarefree
and $0$ otherwise, so the series of these terms over $j \ge 0$ is $\sum n^{-s}$ over the
squarefree $n \ge 1$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30SquarefreeTerm`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-squarefree-term).

## Local factor at exponent zero

For every $a : \mathbb{N} \to \mathbb{C}$ and every natural
number $p$, the local factor of $a$ at $p$ with exponent $0$ is $1$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30LocalCoeff_zero`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-local-coeff-zero).

## Local factor at exponent one

For every $a : \mathbb{N} \to \mathbb{C}$ and every natural
number $p$, the local factor of $a$ at $p$ with exponent $1$ is $a(p)$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30LocalCoeff_one`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-local-coeff-one).

## Entry 30 local factors vanish at exponents at least two

For every function
$a : \mathbb{N} \to \mathbb{C}$, every $p \in \mathbb{N}$ and every $e \ge 2$, the Entry 30 local
factor of $a$ at $p$ with exponent $e$ is $0$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30LocalCoeff_of_two_le`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-local-coeff-of-two-le).

## Entry 30 coefficients at squarefree integers

For every function
$a : \mathbb{N} \to \mathbb{C}$ and every squarefree $n \in \mathbb{N}$ with $n \ne 0$, the Entry 30
coefficient $c_a(n)$ is the product of $a(p)$ over the prime factors $p$ of $n$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30Coeff_of_squarefree`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-coeff-of-squarefree).

## Entry 30 coefficients vanish at nonzero non-squarefree natural numbers

For every
function $a : \mathbb{N} \to \mathbb{C}$ and every natural number $n \ne 0$ that is not
squarefree, the Entry 30 coefficient $c_a(n)$ is $0$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30Coeff_of_not_squarefree`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-coeff-of-not-squarefree).

## Closed form of the Entry 30 coefficients

For every function $a : \mathbb{N} \to \mathbb{C}$
and every $n \in \mathbb{N}$ with $n \ne 0$, the Entry 30 coefficient $c_a(n)$ equals the product of
$a(p)$ over the prime factors $p$ of $n$ when $n$ is squarefree, and $c_a(n) = 0$ otherwise.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30Coeff_of_ne_zero`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-coeff-of-ne-zero).

## Summability of the Entry 30 coefficients

Let $a : \mathbb{N} \to \mathbb{C}$ and let
$c > 1$ be real with $|a(p)| \le p^{-c}$ for every prime $p$. Then the Entry 30 coefficients
$f_a(n)$ of $a$ (equal to $0$ at $n = 0$; for $n \ge 1$, the product of $a(p)$ over the primes
$p \mid n$ if $n$ is squarefree, and $0$ otherwise) form a summable family over $n \ge 2$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.summable_chapter5Entry30Coeff_add_two`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#summable-chapter5-entry30-coeff-add-two).

## The Entry 30 coefficient at zero

For every function $a : \mathbb{N} \to \mathbb{C}$, the
Entry 30 coefficient $c_a(0)$ is $0$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30Coeff_zero`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-coeff-zero).

## The Entry 30 coefficient at one

For every function $a : \mathbb{N} \to \mathbb{C}$, the
Entry 30 coefficient $c_a(1)$ is $1$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30Coeff_one`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-coeff-one).

## Entry 30 coefficients at primes

For every function $a : \mathbb{N} \to \mathbb{C}$ and
every prime $p$, the Entry 30 coefficient $c_a(p)$ equals $a(p)$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30Coeff_prime`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-coeff-prime).

## Entry 30 coefficients vanish at higher prime powers

For every function
$a : \mathbb{N} \to \mathbb{C}$, every prime $p$ and every $e \ge 2$, the Entry 30 coefficient
satisfies $c_a(p^e) = 0$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30Coeff_prime_pow_of_two_le`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-coeff-prime-pow-of-two).

## Entry 30 coefficients are multiplicative

For every function $a : \mathbb{N} \to \mathbb{C}$
and all coprime $m, n \in \mathbb{N}$, the Entry 30 coefficients $c_a$ satisfy
$c_a(mn) = c_a(m)\,c_a(n)$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30Coeff_mul_of_coprime`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-coeff-mul-of-coprime).

## Euler product for the Entry 30 coefficients

Let $a : \mathbb{N} \to \mathbb{C}$ and let
$c > 1$ be real with $|a(p)| \le p^{-c}$ for every prime $p$. Write $f_a(n)$ for the Entry 30
coefficient of $a$ at $n$ (it is $0$ at $n = 0$; for $n \ge 1$ it is the product of $a(p)$ over
the primes $p \mid n$ if $n$ is squarefree, and $0$ otherwise). Then the product of $1 + a(p)$
over all primes $p$ converges unconditionally to $1 + \sum_{n \ge 2} f_a(n)$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.hasProd_one_add_chapter5Entry30Coeff`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#has-prod-one-add-chapter5-entry30-coeff).

## Squarefree term, explicit form

For $s \in \mathbb{C}$ and a natural number $j$, the $j$-th
term of the Dirichlet series over squarefree integers equals $(j + 1)^{-s}$ if $j + 1$ is
squarefree and $0$ otherwise.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30SquarefreeTerm_def`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 634](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L634). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-squarefree-term-def).

## Summability of the squarefree terms

For every complex number $s$ with
$\operatorname{Re} s > 1$, the series of $n^{-s}$ over the squarefree $n \ge 1$ is summable.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.summable_chapter5Entry30SquarefreeTerm`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 653](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L653). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#summable-chapter5-entry30-squarefree-ter).

## Sum of $n^{-s}$ over squarefree $n$

For every complex number $s$ with
$\operatorname{Re} s > 1$, the sum of $n^{-s}$ over the squarefree $n \ge 1$ equals
$\zeta(s)/\zeta(2s)$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.tsum_chapter5Entry30SquarefreeTerm`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 663](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L663). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#tsum-chapter5-entry30-squarefree-term).

## Odd-count squarefree term, explicit form

For $s \in \mathbb{C}$ and a natural number $j$,
the $j$-th term of the Dirichlet series over squarefree integers with an odd number of prime
factors equals $(j + 1)^{-s}$ if $j + 1$ is squarefree and has an odd number of distinct prime
factors, and $0$ otherwise.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30OddTerm_def`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 753](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L753). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-odd-term-def).

## Summability of the odd squarefree terms

For every complex number $s$ with
$\operatorname{Re} s > 1$, the series of $n^{-s}$ over the squarefree $n \ge 1$ with an odd number
of distinct prime factors is summable.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.summable_chapter5Entry30OddTerm`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 796](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L796). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#summable-chapter5-entry30-odd-term).

## Sum of $n^{-s}$ over squarefree $n$ with an odd number of prime factors

For every complex
number $s$ with $\operatorname{Re} s > 1$, the sum of $n^{-s}$ over the squarefree $n \ge 1$ with
an odd number of distinct prime factors equals $(\zeta(s)^2 - \zeta(2s))/(2\zeta(s)\zeta(2s))$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.tsum_chapter5Entry30OddTerm`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 832](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L832). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#tsum-chapter5-entry30-odd-term).

## Non-squarefree term, explicit form

For $s \in \mathbb{C}$ and a natural number $j$, the
$j$-th term of the Dirichlet series over non-squarefree integers equals $0$ if $j + 1$ is
squarefree and $(j + 1)^{-s}$ otherwise.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30NonSquarefreeTerm_def`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 887](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L887). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-non-squarefree-term-def).

## Summability of the non-squarefree terms

For every complex number $s$ with
$\operatorname{Re} s > 1$, the series of $n^{-s}$ over the non-squarefree $n \ge 1$ is summable.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.summable_chapter5Entry30NonSquarefreeTerm`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 904](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L904). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#summable-chapter5-entry30-non-squarefree).

## Sum of $n^{-s}$ over non-squarefree $n$

For every complex number $s$ with
$\operatorname{Re} s > 1$, the sum of $n^{-s}$ over the non-squarefree $n \ge 1$ equals
$\zeta(s)(\zeta(2s) - 1)/\zeta(2s)$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.tsum_chapter5Entry30NonSquarefreeTerm`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 928](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L928). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#tsum-chapter5-entry30-non-squarefree-ter).

## Explicit form of the signed coefficient

For $s \in \mathbb{C}$ and a natural number
$n \ne 0$, the signed coefficient of $n$ equals $-n^{-s}$ if $n$ is squarefree with an odd number
of distinct prime factors, $n^{-s}$ if $n$ is squarefree with an even number of distinct prime
factors, and $0$ if $n$ is not squarefree.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.chapter5Entry30SignedCoeff_of_ne_zero`, a lemma declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 951](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L951). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#chapter5-entry30-signed-coeff-of-ne-zero).

## Ramanujan's squarefree Dirichlet series (Entry 30)

(i) Let $a : \mathbb{N} \to \mathbb{C}$
and let $c > 1$ be real with $|a(p)| \le p^{-c}$ for every prime $p$, and write $f_a(n)$ for the
Entry 30 coefficient of $a$ at $n$. Then the family $(f_a(n))_{n \ge 2}$ is summable; for every
$n \ge 1$, $f_a(n)$ is the product of $a(p)$ over the primes $p \mid n$ if $n$ is squarefree and
$0$ otherwise; and the product of $1 + a(p)$ over all primes $p$ converges unconditionally to
$1 + \sum_{n \ge 2} f_a(n)$. (ii) Let $s$ be a complex number with $\operatorname{Re} s > 1$.
Then for every $n \ge 1$ the Entry 30 coefficient at $n$ of $p \mapsto -p^{-s}$ is $-n^{-s}$ if
$n$ is squarefree with an odd number of distinct prime factors, $n^{-s}$ if $n$ is squarefree
with an even number of distinct prime factors, and $0$ if $n$ is not squarefree; $\zeta(s) \ne 0$
and $\zeta(2s) \ne 0$; the series of $n^{-s}$ over the squarefree $n \ge 1$ is summable with sum
$\zeta(s)/\zeta(2s)$; the series of $n^{-s}$ over the squarefree $n \ge 1$ with an odd number of
distinct prime factors is summable with sum $(\zeta(s)^2 - \zeta(2s))/(2\zeta(s)\zeta(2s))$; and
the series of $n^{-s}$ over the non-squarefree $n \ge 1$ is summable with sum
$\zeta(s)(\zeta(2s) - 1)/\zeta(2s)$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 5, Entry 30, pp. 131–132.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry30Secondordereulerian.ramanujan_part1_ch5_entry30_secondordereulerian`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean, line 1013](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry30Secondordereulerian.lean#L1013). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#ramanujan-part1-ch5-entry30-secondordere).

## Even or odd non-squarefree numbers up to a bound

For a natural number $N$, the set of
integers $n$ with $1 \le n \le N$ that are even or not squarefree, that is, the even numbers in
$\{1, \dots, N\}$ together with the odd non-squarefree numbers in $\{1, \dots, N\}$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem844Wanted.evenOrOddNonSquarefree`, a definition declared in [WantedExt/NumberTheory/ErdosProblem844Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem844Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#even-or-odd-non-squarefree).

## Erdős Problem 844

For a natural number $N$, let $E_N$ be the set of integers $n$ with
$1 \le n \le N$ that are even or not squarefree. The statement that for every natural number $N$,
the largest size of a set $A \subseteq \{1, \dots, N\}$ such that $ab$ is not squarefree for all
$a, b \in A$ (including $a = b$) is the size of $E_N$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem844Wanted.conjecture`, a definition declared in [WantedExt/NumberTheory/ErdosProblem844Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem844Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#conjecture).

## Erdős Problem 844 is true

For every natural number $N$, the largest size of a set
$A \subseteq \{1, \dots, N\}$ such that $ab$ is not squarefree for all $a, b \in A$ (including
$a = b$) is the number of integers $n$ with $1 \le n \le N$ that are even or not squarefree.

## Sources

- B. Alexeev, D. Mixon, and W. Sawin, The independence and clique cover numbers of the squarefree graph, arXiv:2507.01928 (2025), https://arxiv.org/abs/2507.01928; Erdős Problems, Problem 844 (including Desmond Weisenberg's proof), https://www.erdosproblems.com/latex/844.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem844Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem844Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem844Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Squarefree numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/squarefree-numbers)
