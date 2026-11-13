---
declaration: section
origin: cited
lean: MetaMathlibExt.IsLGeneralizedFibonacci, MetaMathlibExt.lGeneralizedFibonacciCharacteristic, MetaMathlibExt.lGeneralizedFibonacciCoefficient, MetaMathlibExt.lGeneralizedFibonacciOtherRoots, MetaMathlibExt.lGeneralizedFibonacciZetaPole, MetaMathlibExt.lGeneralizedFibonacciCharacteristic_two, MetaMathlibExt.lGeneralizedFibonacciZetaPole_zero, MetaMathlibExt.lGeneralizedFibonacciZetaPoleSet
statement: formalized
---

# Zeta functions of generalized Fibonacci numbers

15 results, 10 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/zeta-functions-of-generalized-fibonacci-numbers/index.html).

## ℓ-generalized Fibonacci sequence

Let $\ell$ be a natural number. A function
$F : \mathbb{Z} \to \mathbb{Z}$ is an $\ell$-generalized Fibonacci sequence when $F(n) = 0$ for
every integer $n$ with $2 - \ell \le n \le 0$, $F(1) = 1$, and
$F(n) = \sum_{i=0}^{\ell-1} F(n-1-i)$ for every integer $n > 1$.

The values of $F$ below $2 - \ell$ are unconstrained, since the sequence is defined only from
that index onward.

## Sources

- Nabin Kumar Meher and Dilip Kumar Sahoo, *Analytic Continuation of the ℓ-Generalized Fibonacci Zeta Function*, INTEGERS 24 (2024), Article A85, Definition preceding Proposition 1.

Formalized by `MetaMathlibExt.IsLGeneralizedFibonacci`, a definition declared in [WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/zeta-functions-of-generalized-fibonacci-numbers/index.html#is-lgeneralized-fibonacci).

## Characteristic polynomial of the ℓ-generalized Fibonacci recurrence

For a natural number
$\ell$, the characteristic polynomial of the $\ell$-generalized Fibonacci recurrence is the
polynomial $\varphi_\ell(X) = X^\ell - \sum_{i=0}^{\ell-1} X^i$ in $\mathbb{C}[X]$; for
$\ell \ge 2$ this is $X^\ell - X^{\ell-1} - \cdots - X - 1$.

## Sources

- Nabin Kumar Meher and Dilip Kumar Sahoo, *Analytic Continuation of the ℓ-Generalized Fibonacci Zeta Function*, INTEGERS 24 (2024), Article A85, Characteristic polynomial definition.

Formalized by `MetaMathlibExt.lGeneralizedFibonacciCharacteristic`, a definition declared in [WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/zeta-functions-of-generalized-fibonacci-numbers/index.html#l-generalized-fibonacci-characteristic).

## Dresden–Du coefficient

For a natural number $\ell$ and a complex number $\beta$, the
Dresden–Du coefficient is the complex number
$c(\beta) = \frac{\beta - 1}{2 + (\ell + 1)(\beta - 2)}$, taken to be $0$ when the denominator
vanishes.

## Sources

- Nabin Kumar Meher and Dilip Kumar Sahoo, *Analytic Continuation of the ℓ-Generalized Fibonacci Zeta Function*, INTEGERS 24 (2024), Article A85, Coefficient definition preceding Lemma 1.

Formalized by `MetaMathlibExt.lGeneralizedFibonacciCoefficient`, a definition declared in [WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/zeta-functions-of-generalized-fibonacci-numbers/index.html#l-generalized-fibonacci-coefficient).

## Other roots of the ℓ-generalized Fibonacci characteristic polynomial

For a natural number
$\ell$ and a real number $\alpha$, this is the finite set of distinct complex roots of the
characteristic polynomial $\varphi_\ell(X) = X^\ell - \sum_{i=0}^{\ell-1} X^i$ other than $\alpha$.
In applications $\alpha$ is the dominant real root of $\varphi_\ell$.

Each root is listed once, without multiplicity; the roots of $\varphi_\ell$ are in fact simple.

## Sources

- Nabin Kumar Meher and Dilip Kumar Sahoo, *Analytic Continuation of the ℓ-Generalized Fibonacci Zeta Function*, INTEGERS 24 (2024), Article A85, Root notation preceding Proposition 1.

Formalized by `MetaMathlibExt.lGeneralizedFibonacciOtherRoots`, a definition declared in [WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/zeta-functions-of-generalized-fibonacci-numbers/index.html#l-generalized-fibonacci-other-roots).

## Possible pole of the ℓ-generalized Fibonacci zeta function at a given index

Let $\ell$
be a natural number, let $\alpha$ be a real number, and let $R$ be the set of complex roots of
$X^\ell - \sum_{i\lt \ell} X^i$ other than $\alpha$. For a function $\kappa$ from $\mathbb{C}$ to the
natural numbers and an integer $n$, the possible pole indexed by $(\kappa, n)$ is

$$
s_{\kappa,n} = -\sum_{\beta \in R} \kappa(\beta) +
\frac{2 n \pi i + \sum_{\beta \in R} \kappa(\beta) \log \beta}{\log \alpha},
$$

where $\log$ is the principal branch of the complex logarithm.

Only the values of $\kappa$ on $R$ enter; their sum is the number called $k$ in the paper.

## Sources

- Nabin Kumar Meher and Dilip Kumar Sahoo, *Analytic Continuation of the ℓ-Generalized Fibonacci Zeta Function*, INTEGERS 24 (2024), Article A85, Theorem 1.

Formalized by `MetaMathlibExt.lGeneralizedFibonacciZetaPole`, a definition declared in [WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/zeta-functions-of-generalized-fibonacci-numbers/index.html#l-generalized-fibonacci-zeta-pole).

## The ℓ-generalized Fibonacci characteristic polynomial for ℓ = 2

For $\ell = 2$ the
characteristic polynomial $\varphi_2$ of the $\ell$-generalized Fibonacci recurrence is the
Fibonacci polynomial $X^2 - X - 1$ in $\mathbb{C}[X]$.

## Sources

- Nabin Kumar Meher and Dilip Kumar Sahoo, *Analytic Continuation of the ℓ-Generalized Fibonacci Zeta Function*, INTEGERS 24 (2024), Article A85, Equation (3).

Formalized by `MetaMathlibExt.lGeneralizedFibonacciCharacteristic_two`, a theorem declared in [WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/zeta-functions-of-generalized-fibonacci-numbers/index.html#l-generalized-fibonacci-characteristic-t).

## The possible pole at the zero index is zero

For every natural number $\ell$ and every
real number $\alpha$, the possible pole $s_{\kappa,n}$ of the $\ell$-generalized Fibonacci zeta
function indexed by the identically zero function $\kappa$ and $n = 0$ equals $0$.

## Sources

- Nabin Kumar Meher and Dilip Kumar Sahoo, *Analytic Continuation of the ℓ-Generalized Fibonacci Zeta Function*, INTEGERS 24 (2024), Article A85, Theorem 1.

Formalized by `MetaMathlibExt.lGeneralizedFibonacciZetaPole_zero`, a theorem declared in [WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/zeta-functions-of-generalized-fibonacci-numbers/index.html#l-generalized-fibonacci-zeta-pole-zero).

## Set of possible poles of the ℓ-generalized Fibonacci zeta function

For a natural number
$\ell$ and a real number $\alpha$, let $R$ be the set of distinct complex roots of the
characteristic polynomial $X^\ell - \sum_{i=0}^{\ell-1} X^i$ other than $\alpha$. The set $S$ of
possible poles is the set of all complex numbers $-K + (2n\pi i + L)/\log\alpha$, where $n$ is
an integer, $(\kappa_\beta)_{\beta \in R}$ is a family of natural numbers,
$K = \sum_{\beta \in R} \kappa_\beta$ and $L = \sum_{\beta \in R} \kappa_\beta \log \beta$. Here
$\log$ is the principal complex logarithm.

## Sources

- Nabin Kumar Meher and Dilip Kumar Sahoo, *Analytic Continuation of the ℓ-Generalized Fibonacci Zeta Function*, INTEGERS 24 (2024), Article A85, Theorem 1.

Formalized by `MetaMathlibExt.lGeneralizedFibonacciZetaPoleSet`, a definition declared in [WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/zeta-functions-of-generalized-fibonacci-numbers/index.html#l-generalized-fibonacci-zeta-pole-set).

## Residue expression of the ℓ-generalized Fibonacci zeta function

Let $\ell$ be a natural
number, let $\alpha$ be a real number, let $R$ be the set of complex roots of
$X^\ell - \sum_{i\lt \ell} X^i$ other than $\alpha$, let
$c(\beta) = (\beta - 1)/(2 + (\ell + 1)(\beta - 2))$ be the Dresden–Du coefficient, and put
$d = c(\alpha)/\alpha$. For a function $\kappa$ from $\mathbb{C}$ to the natural numbers and an
integer $n$, let $k = \sum_{\beta \in R} \kappa(\beta)$ and let $s_0$ be the possible pole
indexed by $(\kappa, n)$. The residue expression indexed by $(\kappa, n)$ is

$$
\rho_{\kappa,n} = d^{-s_0} \binom{-s_0}{k} d^{-k} \cdot
\frac{k!}{\prod_{\beta \in R} \kappa(\beta)!} \cdot
\prod_{\beta \in R} \left(\frac{c(\beta)}{\beta}\right)^{\kappa(\beta)} \cdot
\frac{1}{\log \alpha},
$$

where $\binom{-s_0}{k} = (-s_0)(-s_0 - 1)\cdots(-s_0 - k + 1)/k!$ is the generalized binomial
coefficient, $d^{-s_0}$ and $d^{-k}$ are principal complex powers, and $\log$ is the principal
branch of the complex logarithm.

## Sources

- Nabin Kumar Meher and Dilip Kumar Sahoo, *Analytic Continuation of the ℓ-Generalized Fibonacci Zeta Function*, INTEGERS 24 (2024), Article A85, Theorem 1.

Formalized by `MetaMathlibExt.lGeneralizedFibonacciZetaResidue`, a definition declared in [WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/zeta-functions-of-generalized-fibonacci-numbers/index.html#l-generalized-fibonacci-zeta-residue).

## Corollary pole of the ℓ-generalized Fibonacci zeta function

For natural numbers $\ell$
and $k$, a real number $\alpha$ and an integer $n$, let $q$ be the quotient of $k$ by $\ell - 1$
in natural-number division, with $q = 0$ when $\ell \le 1$ (so $q = k/(\ell - 1)$ when
$\ell \ge 2$ and $\ell - 1$ divides $k$). The corollary pole is the complex number
$-(k + q) + i\pi(2n + q)/\log \alpha$ if $\ell$ is even and $-(k + q) + 2\pi i n/\log \alpha$ if
$\ell$ is odd, where $\log$ is the principal complex logarithm.

## Sources

- Nabin Kumar Meher and Dilip Kumar Sahoo, *Analytic Continuation of the ℓ-Generalized Fibonacci Zeta Function*, INTEGERS 24 (2024), Article A85, Corollary 1.

Formalized by `MetaMathlibExt.lGeneralizedFibonacciZetaCorollaryPole`, a definition declared in [WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/zeta-functions-of-generalized-fibonacci-numbers/index.html#l-generalized-fibonacci-zeta-corollary-p).

## Absolute convergence of the ℓ-generalized Fibonacci zeta series

Let $\ell \ge 2$ and let
$F$ be an $\ell$-generalized Fibonacci sequence. For every complex number $s$ with
$\operatorname{Re} s > 0$, the series $\sum_{n \ge 1} |F_n^{-s}|$ converges, where $F_n^{-s}$ is
the principal complex power of $F_n$ viewed as a complex number.

## Sources

- Nabin Kumar Meher and Dilip Kumar Sahoo, *Analytic Continuation of the ℓ-Generalized Fibonacci Zeta Function*, INTEGERS 24 (2024), Article A85, Proposition 1.

Stated but not proved: `MetaMathlibExt.lGeneralizedFibonacciZeta_summable` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/zeta-functions-of-generalized-fibonacci-numbers/index.html#l-generalized-fibonacci-zeta-summable).

## Meromorphic continuation of the ℓ-generalized Fibonacci zeta function

Let $\ell \ge 2$,
let $F$ be an $\ell$-generalized Fibonacci sequence, let $\alpha > 1$ be a real number with
$\alpha^\ell = \sum_{i=0}^{\ell-1} \alpha^i$, and let $S$ be the set of possible poles determined
by $\ell$ and $\alpha$. Then there is a function $f : \mathbb{C} \to \mathbb{C}$ such that
$f(s) = \sum_{n \ge 1} F(n)^{-s}$ for every complex $s$ with $\operatorname{Re} s > 0$, $f$ is
complex differentiable at every point outside $S$, and for every $s_0 \in S$ the limit of
$(s - s_0) f(s)$ as $s \to s_0$ with $s \ne s_0$ exists in $\mathbb{C}$.

The last clause says that $f$ has at most simple poles, all lying in $S$; the residues are
stated separately.

## Sources

- Nabin Kumar Meher and Dilip Kumar Sahoo, *Analytic Continuation of the ℓ-Generalized Fibonacci Zeta Function*, INTEGERS 24 (2024), Article A85, Theorem 1.

Stated but not proved: `MetaMathlibExt.lGeneralizedFibonacciZeta_meromorphicContinuation` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/zeta-functions-of-generalized-fibonacci-numbers/index.html#l-generalized-fibonacci-zeta-meromorphic).

## Residues of the ℓ-generalized Fibonacci zeta function

Let $\ell \ge 2$, let $F$ be an
$\ell$-generalized Fibonacci sequence, and let $\alpha > 1$ be a real number with
$\alpha^\ell = \sum_{i\lt \ell} \alpha^i$. Let $R$ be the set of complex roots of
$X^\ell - \sum_{i\lt \ell} X^i$ other than $\alpha$, let $s_{\kappa,n}$ be the possible pole and
$\rho_{\kappa,n}$ the residue expression indexed by a function $\kappa$ from $\mathbb{C}$ to the
natural numbers and an integer $n$, and let $S$ be the set of all possible poles $s_{\kappa,n}$.
Fix $\kappa$ and $n$ such that whenever $s_{\kappa',n'} = s_{\kappa,n}$, we have $n' = n$ and
$\kappa'(\beta) = \kappa(\beta)$ for every $\beta \in R$. Let $f : \mathbb{C} \to \mathbb{C}$
satisfy $f(s) = \sum_{m \ge 1} F_m^{-s}$ (principal complex powers) for every $s$ with
$\operatorname{Re} s > 0$, and let $f$ be complex differentiable at every point outside $S$.
Then $(s - s_{\kappa,n}) f(s)$ tends to $\rho_{\kappa,n}$ as $s$ tends to $s_{\kappa,n}$ with
$s \ne s_{\kappa,n}$.

The hypothesis that $(\kappa, n)$ is the only index of its pole is not in the paper: when
different indices give the same pole, their residue contributions add up, a case the printed
formula does not address.

## Sources

- Nabin Kumar Meher and Dilip Kumar Sahoo, *Analytic Continuation of the ℓ-Generalized Fibonacci Zeta Function*, INTEGERS 24 (2024), Article A85, Theorem 1 (residue formula).

Stated but not proved: `MetaMathlibExt.lGeneralizedFibonacciZeta_residue` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/zeta-functions-of-generalized-fibonacci-numbers/index.html#l-generalized-fibonacci-zeta-residue-2).

## Explicit possible poles of the ℓ-generalized Fibonacci zeta function

Let $\ell \ge 2$, let
$\alpha > 1$ be a real number with $\alpha^\ell = \sum_{i=0}^{\ell-1} \alpha^i$, and let $k$ be a
natural number divisible by $\ell - 1$; write $q = k/(\ell - 1)$. Then for every integer $n$, the
point $-(k + q) + i\pi(2n + q)/\log \alpha$ if $\ell$ is even, and $-(k + q) + 2\pi i n/\log \alpha$
if $\ell$ is odd, belongs to the set $S$ of possible poles of the $\ell$-generalized Fibonacci
zeta function determined by $\ell$ and $\alpha$.

A witnessing exponent tuple takes the constant value $q$ at every root of the characteristic
polynomial other than $\alpha$.

## Sources

- Nabin Kumar Meher and Dilip Kumar Sahoo, *Analytic Continuation of the ℓ-Generalized Fibonacci Zeta Function*, INTEGERS 24 (2024), Article A85, Corollary 1.

Stated but not proved: `MetaMathlibExt.lGeneralizedFibonacciZeta_corollaryPole_mem` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/zeta-functions-of-generalized-fibonacci-numbers/index.html#l-generalized-fibonacci-zeta-corollary-p-2).

## Rational values of the ℓ-generalized Fibonacci zeta function at negative integers

Let
$\ell \ge 2$, let $F$ be an $\ell$-generalized Fibonacci sequence, let $\alpha > 1$ be a real
number with $\alpha^\ell = \sum_{i=0}^{\ell-1} \alpha^i$, and let $S$ be the set of possible
poles determined by $\ell$ and $\alpha$. Let $m$ be a positive integer and let
$f : \mathbb{C} \to \mathbb{C}$ be a function that satisfies $f(s) = \sum_{n \ge 1} F(n)^{-s}$
whenever $\operatorname{Re} s > 0$ and is complex differentiable at every point outside $S$. If
$f$ is complex differentiable at $-m$, then $f(-m)$ is a rational number.

## Sources

- Nabin Kumar Meher and Dilip Kumar Sahoo, *Analytic Continuation of the ℓ-Generalized Fibonacci Zeta Function*, INTEGERS 24 (2024), Article A85, Theorem 2.

Stated but not proved: `MetaMathlibExt.lGeneralizedFibonacciZeta_negInt_rational` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFibonacciZetaWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/zeta-functions-of-generalized-fibonacci-numbers/index.html#l-generalized-fibonacci-zeta-neg-int-rat).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Zeta functions of generalized Fibonacci numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/zeta-functions-of-generalized-fibonacci-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/zeta-functions-of-generalized-fibonacci-numbers)
