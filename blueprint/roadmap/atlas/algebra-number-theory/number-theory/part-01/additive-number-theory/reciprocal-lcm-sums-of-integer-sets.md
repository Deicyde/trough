---
declaration: section
origin: cited
lean: MetaMathlibExt.truncLog, MetaMathlibExt.truncLog2, MetaMathlibExt.truncLog3, MetaMathlibExt.one_le_truncLog, MetaMathlibExt.naturalsInSetUpTo, MetaMathlibExt.naturalsInSetUpTo_empty, MetaMathlibExt.recipSumUpTo, MetaMathlibExt.recipSumUpTo_empty
statement: formalized
---

# Reciprocal lcm sums of integer sets

22 results, 17 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html).

## Truncated logarithm

For a real number $x$, the truncated logarithm is
$\operatorname{Log} x = \max(\log x, 1)$. Here $\log$ is extended to all reals by $\log 0 = 0$
and $\log x = \log |x|$ for $x < 0$, so the definition is total; the paper uses it only for
$x > 0$.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Notation.

Formalized by `MetaMathlibExt.truncLog`, a definition declared in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#trunc-log).

## Second iterated truncated logarithm

For a real number $x$, the second iterated truncated
logarithm is $\operatorname{Log}_2 x = \operatorname{Log}(\operatorname{Log} x)$, where
$\operatorname{Log}$ is the truncated logarithm.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Notation.

Formalized by `MetaMathlibExt.truncLog2`, a definition declared in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#trunc-log2).

## Third iterated truncated logarithm

For real $x$, let
$\operatorname{Log} x = \max(\log x, 1)$ be the truncated logarithm, where $\log$ is the natural
logarithm extended by $\log x = \log |x|$ for $x < 0$ and $\log 0 = 0$, and let
$\operatorname{Log}_2 x = \operatorname{Log}(\operatorname{Log} x)$. The third iterated truncated
logarithm is the function on all of $\mathbb{R}$ given by
$\operatorname{Log}_3 x = \operatorname{Log}(\operatorname{Log}_2 x)$.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Notation.

Formalized by `MetaMathlibExt.truncLog3`, a definition declared in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#trunc-log3).

## The truncated logarithm is at least one

For every real number $x$, the truncated
logarithm $\operatorname{Log} x = \max(\log x, 1)$ satisfies $\operatorname{Log} x \ge 1$.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Notation.

Formalized by `MetaMathlibExt.one_le_truncLog`, a theorem declared in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#one-le-trunc-log).

## Elements of a set up to a bound

For a set $A$ of natural numbers and a real number $x$,
this is the finite set of positive integers $n \in A$ with $n \le x$; it is empty when $x < 1$.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Notation.

Formalized by `MetaMathlibExt.naturalsInSetUpTo`, a definition declared in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#naturals-in-set-up-to).

## The empty set has no elements up to any bound

For every real number $x$, the finite set
of elements $n$ of the empty set with $1 \le n \le x$ is empty.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Notation.

Formalized by `MetaMathlibExt.naturalsInSetUpTo_empty`, a theorem declared in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#naturals-in-set-up-to-empty).

## Harmonic sum of a set up to a bound

For a set $A$ of natural numbers and a real number
$x$, this is the finite sum $\sum_{n \in A,\, 1 \le n \le x} 1/n$ of the reciprocals of the
positive integers in $A$ that are at most $x$; it is $0$ when $x < 1$.

The sum starts at $n = 1$, matching the paper's convention that natural numbers are positive.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Notation.

Formalized by `MetaMathlibExt.recipSumUpTo`, a definition declared in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#recip-sum-up-to).

## The harmonic sum over the empty set vanishes

For every real number $x$,
$\sum_{n \in \emptyset,\, n \le x} 1/n = 0$.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Notation.

Formalized by `MetaMathlibExt.recipSumUpTo_empty`, a theorem declared in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#recip-sum-up-to-empty).

## Double sum of reciprocal least common multiples

For a set $A$ of natural numbers and a
real number $x$, the double sum of reciprocal least common multiples of $A$ up to $x$ is the
real number $\sum 1/\operatorname{lcm}(n, m)$, summed over all ordered pairs $(n, m)$ with
$n, m \in A$, $1 \le n \le x$ and $1 \le m \le x$.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Equation (12).

Formalized by `MetaMathlibExt.lcmReciprocalSum`, a definition declared in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#lcm-reciprocal-sum).

## Double reciprocal lcm sum of the empty set

For every real number $x$, the double sum of
reciprocal least common multiples of the empty set up to $x$ is $0$.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Equation (12).

Formalized by `MetaMathlibExt.lcmReciprocalSum_empty`, a theorem declared in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#lcm-reciprocal-sum-empty).

## Logarithmic gcd moment

For a set $A$ of natural numbers and a real number $x$, the
logarithmic gcd moment of $A$ up to $x$ is the sum of $\gcd(n, m)/(nm)$ over all ordered pairs
$(n, m)$ with $n, m \in A$, $1 \le n \le x$ and $1 \le m \le x$.

When $A \cap [1, x]$ is nonempty, dividing by $\big(\sum_{n \in A,\ 1 \le n \le x} 1/n\big)^2$
gives the expected value of $\gcd(n, m)$ for $n$ and $m$ drawn independently from $A \cap [1, x]$,
each with probability proportional to $1/n$.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Equation (9).

Formalized by `MetaMathlibExt.gcdLogarithmicMoment`, a definition declared in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#gcd-logarithmic-moment).

## Gcd defect

For a set $A$ of natural numbers and a real number $x$, let
$S_A(x) = \sum_{n \in A,\ 1 \le n \le x} 1/n$ be the harmonic sum of $A$ up to $x$, and let
$G_A(x)$ be the sum of $\gcd(n, m)/(nm)$ over all ordered pairs $(n, m)$ with $n, m \in A$,
$1 \le n \le x$ and $1 \le m \le x$. The gcd defect of $A$ up to $x$ is
$\mathcal{E}_A(x) = G_A(x)/S_A(x)^2 - 1$, where division by $0$ gives $0$; in particular
$\mathcal{E}_A(x) = -1$ when $A$ has no element in $[1, x]$.

When $A$ has an element in $[1, x]$, $\mathcal{E}_A(x) + 1$ is the expected value of
$\gcd(n, m)$ for $n$ and $m$ drawn independently from $A \cap [1, x]$, each with probability
proportional to $1/n$, so $\mathcal{E}_A(x)$ is the quantity $\mathbb{E} \gcd(n, m) - 1$ of the
source.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Equation (9).

Formalized by `MetaMathlibExt.lcmDefect`, a definition declared in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#lcm-defect).

## The gcd defect of the empty set

For every real number $x$, the gcd defect of the empty
set up to $x$ equals $-1$.

The harmonic sum of the empty set is $0$, and division by $0$ gives $0$.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Equation (9).

Formalized by `MetaMathlibExt.lcmDefect_empty`, a theorem declared in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#lcm-defect-empty).

## Products of a fixed number of distinct primes

For a set $\mathcal{P}$ of natural numbers
and $k \in \mathbb{N}$, $\mathcal{P}^{[k]}$ is the set of squarefree natural numbers $n$ whose prime
divisors all lie in $\mathcal{P}$ and which have exactly $k$ distinct prime divisors; that is, the
products of exactly $k$ distinct primes from $\mathcal{P}$. In particular,
$\mathcal{P}^{[0]} = \{1\}$.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Lemma 1 notation.

Formalized by `MetaMathlibExt.primeProductLayer`, a definition declared in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#prime-product-layer).

## Products of at most a fixed number of distinct primes

For a set $\mathcal{P}$ of natural
numbers and $k \in \mathbb{N}$, $\mathcal{P}^{[\le k]}$ is the set of natural numbers that lie in
$\mathcal{P}^{[j]}$ for some $j \le k$, where $\mathcal{P}^{[j]}$ is the set of products of exactly
$j$ distinct primes from $\mathcal{P}$; that is,
$\mathcal{P}^{[\le k]} = \bigcup_{j \le k} \mathcal{P}^{[j]}$.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Lemma 1 notation.

Formalized by `MetaMathlibExt.primeProductsAtMost`, a definition declared in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#prime-products-at-most).

## At most zero primes means exactly zero primes

For every set $\mathcal{P}$ of natural
numbers, $\mathcal{P}^{[\le 0]} = \mathcal{P}^{[0]}$, where $\mathcal{P}^{[\le k]}$ and
$\mathcal{P}^{[k]}$ are the products of at most, respectively exactly, $k$ distinct primes from
$\mathcal{P}$.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Lemma 1 notation.

Formalized by `MetaMathlibExt.primeProductsAtMost_zero`, a theorem declared in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#prime-products-at-most-zero).

## Growth function of the dense-set construction

Let $\operatorname{Log}_2$ be the second
iterated truncated logarithm. For real numbers $C_0$ and $x$, let $k$ be the natural number
$\max(\lceil C_0 \sqrt{\operatorname{Log}_2 x}\,\rceil - 1, 0)$, and set
$h = \operatorname{Log}_2 x - k^2/C_0^2 + 1$, $x' = \exp(\exp((k + 1)^2/C_0^2))$,
$h' = \operatorname{Log}_2 x' - k^2/C_0^2 + 1$ and $\psi = 1 + h^2/h'$. The growth function at
$(C_0, x)$ is $F_{C_0}(x) = \psi\, k^{2k} / (C_0^{2k}\, k!)$. Here division by $0$ gives $0$ and
$0^0 = 1$.

In the source, $h'$ is the value at $x_{k+1} = x'$ of the expression defining $h$, with $k$ kept
fixed, and $F_{C_0}(x)$ is written $\psi(x)\, k^{2k} C_0^{-2k}/k!$; the function is used only for
$C_0 > 0$ and sufficiently large $x$.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Equations (13)--(15).

Formalized by `MetaMathlibExt.lcmDenseGrowthF`, a definition declared in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#lcm-dense-growth-f).

## Harmonic sums over products of distinct primes

There are constants $c > 0$ and $C > 0$
such that the following holds. Let $\mathcal{P}$ be a set of primes, let $k$ be a natural number,
let $x \ge 1$ be real, and put $S = \sum_{p \in \mathcal{P},\, p \le x} 1/p$,
$T_k = \sum_{n \in \mathcal{P}^{[k]},\, n \le x} 1/n$ and
$T_{\le k} = \sum_{n \in \mathcal{P}^{[\le k]},\, n \le x} 1/n$, where $\mathcal{P}^{[k]}$ and
$\mathcal{P}^{[\le k]}$ are the sets of products of exactly $k$, respectively at most $k$,
distinct primes from $\mathcal{P}$. If $k \le cS$, then
$S^k/(C\,k!) \le T_k \le C\,S^k/k!$ and $S^k/(C\,k!) \le T_{\le k} \le C\,S^k/k!$.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Lemma 1.

Stated but not proved: `MetaMathlibExt.recipSum_primeProductLayer_asymp` is written with `theorem_wanted` in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#recip-sum-prime-product-layer-asymp).

## Dense sets with unusually large least common multiples

Let $\operatorname{Log}_2$ and
$\operatorname{Log}_3$ be the second and third iterated truncated logarithms. For a set $A$ of
natural numbers and real $x$, write $S_A(x) = \sum_{n \in A,\ 1 \le n \le x} 1/n$, and write
$L_A(x)$ for the sum of $1/\operatorname{lcm}(n, m)$ over all ordered pairs $(n, m)$ with
$n, m \in A$, $1 \le n \le x$ and $1 \le m \le x$. Then for every real $C_0 > 0$ there is a set
$A$ of natural numbers with the following two properties. First, there is a function
$\varepsilon : \mathbb{R} \to \mathbb{R}$ with $\varepsilon(x) \to 0$ as $x \to \infty$ such that
for all sufficiently large real $x$,
$S_A(x) = \exp((C_0/2 + \varepsilon(x))(\operatorname{Log}_2 x)^{1/2} \operatorname{Log}_3 x)$.
Second, there is a constant $K > 0$ such that $L_A(x) \le K\, S_A(x)^2$ for all sufficiently
large real $x$.

The source presents this as a negative answer to Erdős problem #442. Its accompanying claim that
the exponent is optimal is made precise by Theorem 2(ii) and is stated separately.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Theorem 1.

Stated but not proved: `MetaMathlibExt.exists_dense_set_large_lcm` is written with `theorem_wanted` in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#exists-dense-set-large-lcm).

## Dense sets with controlled gcd defect

Let $e$ be Euler's number. There is an absolute
constant $C > 0$ with the following property. Let $C_0 > 0$ be real, and let $F_{C_0}$ be the
growth function of the dense-set construction. Then there is a set $A$ of natural numbers such
that, writing $S_A(x) = \sum_{n \in A,\ 1 \le n \le x} 1/n$ for its harmonic sum up to $x$ and
$\mathcal{E}_A(x)$ for its gcd defect up to $x$, the following two statements hold. First, there
is a constant $K > 0$ with $F_{C_0}(x)/K \le S_A(x) \le K\, F_{C_0}(x)$ for all sufficiently large
real $x$. Second, there is a function $\varepsilon : \mathbb{R} \to \mathbb{R}$ with
$\varepsilon(x) \to 0$ as $x \to \infty$ such that
$\mathcal{E}_A(x) \le C\,(\exp(e^2 C_0^2) - 1 + \varepsilon(x))$ for all sufficiently large
real $x$.

The factor $e^2$ follows the journal version of the source; the arXiv preprint prints
$\exp(C_0^2)$, but its proof, through the factor $e^\ell$ of (35), gives $e^2 C_0^2$.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Theorem 2(i).

Stated but not proved: `MetaMathlibExt.exists_dense_set_controlled_defect` is written with `theorem_wanted` in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#exists-dense-set-controlled-defect).

## Baby version of the dense-set construction

Let $e$ be Euler's number, let
$\operatorname{Log}_2$ and $\operatorname{Log}_3$ be the second and third iterated truncated
logarithms, and for a set $B$ of natural numbers and real $x$ write
$S_B(x) = \sum_{n \in B,\ 1 \le n \le x} 1/n$ and $\mathcal{E}_B(x)$ for the gcd defect of $B$ up
to $x$. There is an absolute constant $C > 0$ such that for every real $C_0 > 0$ there are sets
$A_0, A_1, A_2, \dots$ of natural numbers with the following property: for every $\varepsilon > 0$
there are a real $\delta > 0$ and a natural number $k_0$ such that for every natural number
$k \ge k_0$ and every real $x$ with $|C_0 (\operatorname{Log}_2 x)^{1/2} - k| \le \delta k$, there
is a real $\eta$ with $|\eta| \le \varepsilon$ and
$S_{A_k}(x) = \exp((C_0/2 + \eta)(\operatorname{Log}_2 x)^{1/2} \operatorname{Log}_3 x)$, and
moreover $\mathcal{E}_{A_k}(x) \le C(\exp(e^2 C_0^2) - 1 + \varepsilon)$.

In the source this is Proposition 1, a simplified version of the construction for Theorem 2(i)
(its lead-in sentence refers to Theorem 2(ii)): the sets $A_k$ satisfy (31) and the bound (21)
in the range (32), with all $o(1)$ terms taken as $k \to \infty$. Above, these $o(1)$ terms are
written with $\varepsilon$, $\delta$ and $k_0$.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Proposition 1, (31) and (32), with (21).

Stated but not proved: `MetaMathlibExt.exists_dense_sets_baby` is written with `theorem_wanted` in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#exists-dense-sets-baby).

## Harmonic sums of sets with small gcd defect

For a set $A$ of natural numbers and a real
number $x$, let $S_A(x)$ be the sum of $1/n$ over $n \in A$ with $1 \le n \le x$, and let the
defect of $A$ at $x$ be the sum of $\gcd(n, m)/(nm)$ over $n, m \in A$ with $1 \le n, m \le x$,
divided by $S_A(x)^2$, minus $1$ (the defect is $-1$ when $S_A(x) = 0$). Let
$\operatorname{Log} x = \max(\log x, 1)$ be the truncated logarithm, let
$\operatorname{Log}_2 x = \operatorname{Log}(\operatorname{Log} x)$ and let
$\operatorname{Log}_3 x = \operatorname{Log}(\operatorname{Log}_2 x)$. For every real
$C_0 > 0$ there are a function $e : \mathbb{R} \to \mathbb{R}$ with $e(x) \to 0$ as
$x \to \infty$ and a real $x_0$ such that for every real $x \ge x_0$ and every set $A$ of natural
numbers whose defect at $x$ is at most $C_0^2$,

$$S_A(x) \le \exp\bigl((C_0 + e(x)) (\operatorname{Log}_2 x)^{1/2} \operatorname{Log}_3 x\bigr).$$

The function $e$ and the threshold $x_0$ are chosen before $x$ and $A$, so the $o(1)$ error is
uniform in $A$.

## Sources

- Terence Tao, *Dense Sets of Natural Numbers with Unusually Large Least Common Multiples*, INTEGERS 24 (2024), Article A100, Theorem 2(ii).

Stated but not proved: `MetaMathlibExt.uniform_harmonic_bound_of_defect` is written with `theorem_wanted` in [WantedExt/NumberTheory/LcmDenseSetsWanted.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LcmDenseSetsWanted.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html#uniform-harmonic-bound-of-defect).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reciprocal lcm sums of integer sets](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/additive-number-theory/reciprocal-lcm-sums-of-integer-sets)
