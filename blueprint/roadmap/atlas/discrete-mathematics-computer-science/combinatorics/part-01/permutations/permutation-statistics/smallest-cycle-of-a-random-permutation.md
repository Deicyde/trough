---
declaration: section
origin: cited
lean: MetaMathlibExt.smallest_cycle_mean_asymp, MetaMathlibExt.smallest_cycle_moment_asymp, MetaMathlibExt.smallest_cycle_variance_asymp, MetaMathlibExt.buchstab_taylor_coeff_recursion, MetaMathlibExt.generalized_buchstab_taylor_coeff_recursion
statement: formalized
---

# Smallest cycle of a random permutation

5 results, 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/smallest-cycle-of-a-random-permutation/index.html).

## Mean length of the smallest cycle of a random permutation

For $n \ge 1$ let $X_n$ be the
length of the smallest cycle of a uniformly random permutation of $\{1, \dots, n\}$. Then
$\mathbb{E}(X_n) / (e^{-\gamma} \log n) \to 1$ as $n \to \infty$, where $\gamma$ is the
Euler–Mascheroni constant.

The paper states this as $\mathbb{E}(X_n) = e^{-\gamma} \log n \, (1 + O(h(n)/\log n))$ for some
$h(n) = o(\log n)$, which is equivalent.

## Sources

- Claude Gravel and Daniel Panario, *Evaluating the Generalized Buchstab Function and Revisiting the Variance of the Distribution of the Smallest Components of Combinatorial Objects*, INTEGERS 24 (2024), Article A7, Theorem 1.

Stated but not proved: `MetaMathlibExt.smallest_cycle_mean_asymp` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SmallestCycleBuchstabWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SmallestCycleBuchstabWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/smallest-cycle-of-a-random-permutation/index.html#smallest-cycle-mean-asymp).

## Higher moments of the smallest cycle length

Let $\omega$ be a real function with
$\omega(x) = 1/x$ for $1 \le x \le 2$ and $x\,\omega(x) = 1 + \int_1^{x-1} \omega(t)\,dt$ for
$x \ge 2$, and for $n \ge 1$ let $X_n$ be the length of the smallest cycle of a uniformly random
permutation of $\{1, \dots, n\}$. For every integer $\ell \ge 2$ there are real constants
$\varepsilon > 0$ and $C$ such that for every $n \ge 1$

$$\left| \mathbb{E}(X_n^\ell) - \ell\, n^{\ell-1} \int_1^\infty \frac{\omega(x)}{x^\ell}\,dx \right|
\le C\, n^{\ell-1} n^{-\varepsilon}.$$

## Sources

- Claude Gravel and Daniel Panario, *Evaluating the Generalized Buchstab Function and Revisiting the Variance of the Distribution of the Smallest Components of Combinatorial Objects*, INTEGERS 24 (2024), Article A7, Theorem 1.

Stated but not proved: `MetaMathlibExt.smallest_cycle_moment_asymp` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SmallestCycleBuchstabWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SmallestCycleBuchstabWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/smallest-cycle-of-a-random-permutation/index.html#smallest-cycle-moment-asymp).

## Variance of the smallest cycle length

Let $\omega$ be a real function with
$\omega(x) = 1/x$ for $1 \le x \le 2$ and $x\,\omega(x) = 1 + \int_1^{x-1} \omega(t)\,dt$ for
$x \ge 2$, and for $n \ge 1$ let $X_n$ be the length of the smallest cycle of a uniformly random
permutation of $\{1, \dots, n\}$. There are real constants $\varepsilon > 0$ and $C$ such that for
every $n \ge 1$

$$\left| \operatorname{Var}(X_n) - 2n \int_1^\infty \frac{\omega(x)}{x^2}\,dx \right|
\le C\, n \cdot n^{-\varepsilon}.$$

## Sources

- Claude Gravel and Daniel Panario, *Evaluating the Generalized Buchstab Function and Revisiting the Variance of the Distribution of the Smallest Components of Combinatorial Objects*, INTEGERS 24 (2024), Article A7, Theorem 2.

Stated but not proved: `MetaMathlibExt.smallest_cycle_variance_asymp` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SmallestCycleBuchstabWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SmallestCycleBuchstabWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/smallest-cycle-of-a-random-permutation/index.html#smallest-cycle-variance-asymp).

## Recursion for the Taylor coefficients of the Buchstab function

Let $\omega$ be a real
function with $\omega(x) = 1/x$ for $1 \le x \le 2$ and
$x\,\omega(x) = 1 + \int_1^{x-1} \omega(t)\,dt$ for $x \ge 2$, and let $c_{n,i}$ ($n, i \ge 0$)
be real numbers such that for every integer $n \ge 1$ and every real $z$ with $-1 \le z < 1$ the
series $\sum_{i \ge 0} c_{n,i} z^i$ converges absolutely to $\omega(n + (1+z)/2)$. Then
$c_{1,i} = \frac{2}{3} \left(-\frac{1}{3}\right)^i$ for every $i \ge 0$, and for every $n \ge 1$

$$c_{n+1,0} = \frac{1}{2n+3} \sum_{i \ge 0} c_{n,i} \left(2(n+1) + \frac{(-1)^i}{i+1}\right)$$

and, for every $i \ge 1$,

$$c_{n+1,i} = \frac{1}{2n+3} \left(\frac{c_{n,i-1}}{i} - c_{n+1,i-1}\right).$$

The printed statement of Theorem 3 has $c_{n,i}/n$ in place of $c_{n,i-1}/i$; the recursion above
is the identity $(2n+3) c_{n+1,i} + c_{n+1,i-1} = c_{n,i-1}/i$ derived in the paper's proof.

## Sources

- Claude Gravel and Daniel Panario, *Evaluating the Generalized Buchstab Function and Revisiting the Variance of the Distribution of the Smallest Components of Combinatorial Objects*, INTEGERS 24 (2024), Article A7, Theorem 3.

Stated but not proved: `MetaMathlibExt.buchstab_taylor_coeff_recursion` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SmallestCycleBuchstabWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SmallestCycleBuchstabWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/smallest-cycle-of-a-random-permutation/index.html#buchstab-taylor-coeff-recursion).

## Recursion for the Taylor coefficients of the generalized Buchstab function

Let $K > 0$,
let $\Omega$ be a real function with $\Omega(x) = 1$ for $1 \le x < 2$ and
$\Omega(x) = 1 + K \int_2^x \frac{\Omega(u-1)}{u-1}\,du$ for $x \ge 2$, and let $c_{n,i}$
($n, i \ge 0$) be real numbers such that for every integer $n \ge 1$ and every real $z$ with
$-1 \le z < 1$ the series $\sum_{i \ge 0} c_{n,i} z^i$ converges absolutely to
$\Omega(n + (1+z)/2)$. Then $c_{1,0} = 1$, $c_{1,i} = 0$ for every $i \ge 1$,

$$c_{2,0} = 1 + K \sum_{i \ge 0} \frac{(-1)^i}{(i+1)\,2^{i+1}},$$



$$c_{2,i} = K \sum_{j \ge 0} \frac{(-1)^{j+i-1} \binom{j+i}{i}}{(j+i)\,2^{j+i}} \quad (i \ge 1),$$

and for every $n \ge 3$, writing
$\alpha_{n,m} = \sum_{j=0}^{m} \frac{(-1)^{m-j}}{(2n-1)^{m-j}}\, c_{n-1,j}$ for $m \ge 0$,

$$c_{n,0} = \sum_{i \ge 0} c_{n-1,i} -
\frac{K}{2n-1} \sum_{i \ge 0} \frac{(-1)^{i+1} \alpha_{n,i}}{i+1}$$

and $c_{n,i} = \dfrac{K\, \alpha_{n,i-1}}{(2n-1)\, i}$ for every $i \ge 1$.

Here $c_{2,0} = 1 + K \log(3/2)$. The printed statement of Theorem 4 has
$c_{2,0} = 1 + K \sum_{i \ge 1} 1/(i\, 2^i)$, which omits the sign $(-1)^{i-1}$.

## Sources

- Claude Gravel and Daniel Panario, *Evaluating the Generalized Buchstab Function and Revisiting the Variance of the Distribution of the Smallest Components of Combinatorial Objects*, INTEGERS 24 (2024), Article A7, Theorem 4.

Stated but not proved: `MetaMathlibExt.generalized_buchstab_taylor_coeff_recursion` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SmallestCycleBuchstabWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SmallestCycleBuchstabWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/smallest-cycle-of-a-random-permutation/index.html#generalized-buchstab-taylor-coeff-recurs).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Smallest cycle of a random permutation](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/smallest-cycle-of-a-random-permutation/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/permutations/permutation-statistics/smallest-cycle-of-a-random-permutation)
