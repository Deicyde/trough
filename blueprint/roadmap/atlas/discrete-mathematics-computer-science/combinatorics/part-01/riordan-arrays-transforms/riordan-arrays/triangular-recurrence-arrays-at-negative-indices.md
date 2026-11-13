---
declaration: section
origin: cited
lean: MetaMathlibExt.TriangularRecurrence, MetaMathlibExt.TriangularRecurrence.array, MetaMathlibExt.TriangularRecurrence.array_binomial_four_two, MetaMathlibExt.TriangularRecurrence.weight, MetaMathlibExt.TriangularRecurrence.weight', MetaMathlibExt.TriangularRecurrence.negPosAux, MetaMathlibExt.TriangularRecurrence.negPos, MetaMathlibExt.TriangularRecurrence.negPos_neg_one_zero
statement: formalized
---

# Triangular recurrence arrays at negative indices

19 results, 15 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html).

## Triangular recurrences

## Triangular recurrence

A triangular recurrence is a tuple
$(\alpha, \beta, \gamma; \alpha', \beta', \gamma')$ of six integers, the parameters of the linear
recurrence

$$
a_{n,k} = (\alpha n + \beta k + \gamma)\, a_{n-1,k} +
  (\alpha' n + \beta' k + \gamma')\, a_{n-1,k-1}.
$$

## Sources

- Lars Palapies, *On Extensions of Triangular Arrays to Negative Row Indices and Their Generating Functions*, INTEGERS 26 (2026), Article A83, Equation (1).

Formalized by `MetaMathlibExt.TriangularRecurrence`, a structure declared in [WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html#triangular-recurrence).

## Triangular array of a linear recurrence

Given integer parameters
$(\alpha, \beta, \gamma; \alpha', \beta', \gamma')$, the array $a_{n,k} \in \mathbb{Q}$,
$n, k \ge 0$, is defined by $a_{0,k} = \delta_{k,0}$ and, for $n \ge 1$, by the recurrence (1)
$a_{n,k} = (\alpha n + \beta k + \gamma)\, a_{n-1,k} +
(\alpha' n + \beta' k + \gamma')\, a_{n-1,k-1}$, where $a_{n-1,-1} = 0$.

## Sources

- Lars Palapies, *On Extensions of Triangular Arrays to Negative Row Indices and Their Generating Functions*, INTEGERS 26 (2026), Article A83, Equation (1).

Formalized by `MetaMathlibExt.TriangularRecurrence.array`, a definition declared in [WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html#array).

## The binomial array at $(4, 2)$

For the parameters
$(\alpha, \beta, \gamma; \alpha', \beta', \gamma') = (0, 0, 1; 0, 0, 1)$ of the binomial
coefficients (Table 1), the triangular array $a$ satisfies $a_{4,2} = 6$.

## Sources

- Lars Palapies, *On Extensions of Triangular Arrays to Negative Row Indices and Their Generating Functions*, INTEGERS 26 (2026), Article A83, Table 1.

Formalized by `MetaMathlibExt.TriangularRecurrence.array_binomial_four_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html#array-binomial-four-two).

## First weight of a triangular recurrence

For a triangular recurrence with parameters
$(\alpha, \beta, \gamma; \alpha', \beta', \gamma')$ and integers $n, k$, the first weight is the
rational number $\alpha(n + 1) + \beta k + \gamma$.

It is the divisor in the recurrence defining the negative-positive number $a^{NP}_{n,k}$.

## Sources

- Lars Palapies, *On Extensions of Triangular Arrays to Negative Row Indices and Their Generating Functions*, INTEGERS 26 (2026), Article A83, Definition 1.

Formalized by `MetaMathlibExt.TriangularRecurrence.weight`, a definition declared in [WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html#weight).

## Second weight of a triangular recurrence

For a triangular recurrence with parameters
$(\alpha, \beta, \gamma; \alpha', \beta', \gamma')$ and integers $n, k$, the second weight is the
rational number $\alpha'(n + 1) + \beta' k + \gamma'$.

It is the divisor in the recurrence defining the negative-negative number $a^{NN}_{n,k-1}$.

## Sources

- Lars Palapies, *On Extensions of Triangular Arrays to Negative Row Indices and Their Generating Functions*, INTEGERS 26 (2026), Article A83, Definition 2.

Formalized by `MetaMathlibExt.TriangularRecurrence.weight'`, a definition declared in [WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html#weight-2).

## Negative-positive numbers at negative rows (auxiliary)

For integer parameters
$(\alpha, \beta, \gamma; \alpha', \beta', \gamma')$ and $p, k \ge 0$, put $n = -(p + 1)$. The
rational numbers $c_{p,k}$ are defined by recursion on $p$ and then on $k$ through
$c_{p,k} = (r - (\alpha'(n+1) + \beta' k + \gamma')\, s) / (\alpha(n+1) + \beta k + \gamma)$,
where $r = c_{p-1,k}$ if $p \ge 1$, $r = 1$ if $p = k = 0$, and $r = 0$ if $p = 0 < k$; and
$s = c_{p,k-1}$ if $k \ge 1$, $s = 0$ if $k = 0$. Division by $0$ gives $0$.

## Sources

- Lars Palapies, *On Extensions of Triangular Arrays to Negative Row Indices and Their Generating Functions*, INTEGERS 26 (2026), Article A83, Definition 1.

Formalized by `MetaMathlibExt.TriangularRecurrence.negPosAux`, a definition declared in [WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html#neg-pos-aux).

## Negative-positive numbers

Let $a_{n,k}$ ($n, k \ge 0$) be the triangular array of a
triangular recurrence with parameters $(\alpha, \beta, \gamma; \alpha', \beta', \gamma')$. Its
negative-positive numbers $a^{NP}_{n,k} \in \mathbb{Q}$, for $n, k \in \mathbb{Z}$, are defined by
$a^{NP}_{n,k} = a_{n,k}$ for $n, k \ge 0$, $a^{NP}_{n,k} = 0$ for $k < 0$, and, for $n < 0 \le k$,
recursively by

$$
a^{NP}_{n,k} = \frac{a^{NP}_{n+1,k} - (\alpha'(n+1) + \beta' k + \gamma')\, a^{NP}_{n,k-1}}
  {\alpha(n+1) + \beta k + \gamma},
$$

where division by $0$ gives $0$.

## Sources

- Lars Palapies, *On Extensions of Triangular Arrays to Negative Row Indices and Their Generating Functions*, INTEGERS 26 (2026), Article A83, Definition 1.

Formalized by `MetaMathlibExt.TriangularRecurrence.negPos`, a definition declared in [WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html#neg-pos).

## The negative-positive number at $(-1, 0)$

For every triangular recurrence with
parameters $(\alpha, \beta, \gamma; \alpha', \beta', \gamma')$, its negative-positive number at
row $-1$ and column $0$ is $a^{NP}_{-1,0} = 1/\gamma$, computed in $\mathbb{Q}$ with $1/0 = 0$.

## Sources

- Lars Palapies, *On Extensions of Triangular Arrays to Negative Row Indices and Their Generating Functions*, INTEGERS 26 (2026), Article A83, Definition 1.

Formalized by `MetaMathlibExt.TriangularRecurrence.negPos_neg_one_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html#neg-pos-neg-one-zero).

## Recurrence for the negative-positive numbers

For every triangular recurrence with
parameters $(\alpha, \beta, \gamma; \alpha', \beta', \gamma')$ and all integers $n \le -2$ and
$k \ge 1$, the negative-positive numbers satisfy

$$
a^{NP}_{n,k} = \frac{a^{NP}_{n+1,k} - (\alpha'(n+1) + \beta' k + \gamma')\, a^{NP}_{n,k-1}}
  {\alpha(n+1) + \beta k + \gamma},
$$

where the division is in $\mathbb{Q}$ and division by $0$ gives $0$.

## Sources

- Lars Palapies, *On Extensions of Triangular Arrays to Negative Row Indices and Their Generating Functions*, INTEGERS 26 (2026), Article A83, Definition 1.

Formalized by `MetaMathlibExt.TriangularRecurrence.negPos_rec`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html#neg-pos-rec).

## Negative-negative numbers on and below the diagonal (auxiliary)

For integer parameters
$(\alpha, \beta, \gamma; \alpha', \beta', \gamma')$ and $p, q \ge 0$, put $n = -(p + 1)$ and
$k = n - q$. The rational numbers $b_{p,q}$ are defined by recursion on $p$ and then on $q$ through
$b_{p,q} = (c - (\alpha(n+1) + \beta(k+1) + \gamma)\, e) / (\alpha'(n+1) + \beta'(k+1) + \gamma')$,
where $c = b_{p-1,q}$ if $p \ge 1$, $c = 1$ if $p = q = 0$, and $c = 0$ if $p = 0 < q$; and
$e = b_{p,q-1}$ if $q \ge 1$, $e = 0$ if $q = 0$. Division by $0$ gives $0$.

## Sources

- Lars Palapies, *On Extensions of Triangular Arrays to Negative Row Indices and Their Generating Functions*, INTEGERS 26 (2026), Article A83, Definition 2.

Formalized by `MetaMathlibExt.TriangularRecurrence.negNegAux`, a definition declared in [WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html#neg-neg-aux).

## Negative-negative numbers

For parameters
$(\alpha, \beta, \gamma; \alpha', \beta', \gamma')$ with triangular array $a_{n,k}$ ($n, k \ge 0$),
the negative-negative numbers $a^{NN}_{n,k} \in \mathbb{Q}$, $n, k \in \mathbb{Z}$, are defined
as follows (Definition 2): $a^{NN}_{0,k} = \delta_{k,0}$ for all $k$; $a^{NN}_{n,k} = a_{n,k}$ for
$n > 0$ and $k \ge 0$; $a^{NN}_{n,k} = 0$ for $n > 0 > k$ and for $n < 0$, $k > n$; and, for
$k \le n < 0$,
$a^{NN}_{n,k} = (a^{NN}_{n+1,k+1} - (\alpha(n+1) + \beta(k+1) + \gamma)\, a^{NN}_{n,k+1}) /
(\alpha'(n+1) + \beta'(k+1) + \gamma')$, where division by $0$ gives $0$.

## Sources

- Lars Palapies, *On Extensions of Triangular Arrays to Negative Row Indices and Their Generating Functions*, INTEGERS 26 (2026), Article A83, Definition 2.

Formalized by `MetaMathlibExt.TriangularRecurrence.negNeg`, a definition declared in [WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html#neg-neg).

## Negative-negative numbers at $(-1, -1)$ and $(-1, 0)$

For all parameters
$(\alpha, \beta, \gamma; \alpha', \beta', \gamma')$, the negative-negative numbers $a^{NN}$ satisfy
$a^{NN}_{-1,-1} = 1/\gamma'$ (read as $0$ when $\gamma' = 0$) and $a^{NN}_{-1,0} = 0$.

## Sources

- Lars Palapies, *On Extensions of Triangular Arrays to Negative Row Indices and Their Generating Functions*, INTEGERS 26 (2026), Article A83, Definition 2.

Formalized by `MetaMathlibExt.TriangularRecurrence.negNeg_neg_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html#neg-neg-neg-one).

## Recurrence for the negative-negative numbers

For all parameters
$(\alpha, \beta, \gamma; \alpha', \beta', \gamma')$ and all integers $k < n \le -2$, the
negative-negative numbers $a^{NN}$ satisfy
$a^{NN}_{n,k} = (a^{NN}_{n+1,k+1} - (\alpha(n+1) + \beta(k+1) + \gamma)\, a^{NN}_{n,k+1}) /
(\alpha'(n+1) + \beta'(k+1) + \gamma')$, where division by $0$ gives $0$.

## Sources

- Lars Palapies, *On Extensions of Triangular Arrays to Negative Row Indices and Their Generating Functions*, INTEGERS 26 (2026), Article A83, Definition 2.

Formalized by `MetaMathlibExt.TriangularRecurrence.negNeg_rec`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html#neg-neg-rec).

## Reflected triangular recurrence

The reflection of a triangular recurrence with
parameters $(\alpha, \beta, \gamma; \alpha', \beta', \gamma')$ is the triangular recurrence with
parameters $(\alpha' + \beta', -\beta', \gamma'; \alpha + \beta, -\beta, \gamma)$.

If $a_{n,k}$ is the triangular array of the original recurrence, these are the parameters of the
reflected array $\tilde a_{n,k} = a_{n,n-k}$.

## Sources

- Lars Palapies, *On Extensions of Triangular Arrays to Negative Row Indices and Their Generating Functions*, INTEGERS 26 (2026), Article A83, Proposition 3.

Formalized by `MetaMathlibExt.TriangularRecurrence.reflect`, a definition declared in [WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html#reflect).

## Reflection of triangular recurrences is an involution

Reflecting a triangular
recurrence with parameters $(\alpha, \beta, \gamma; \alpha', \beta', \gamma')$ twice gives back the
recurrence with parameters $(\alpha, \beta, \gamma; \alpha', \beta', \gamma')$.

## Sources

- Lars Palapies, *On Extensions of Triangular Arrays to Negative Row Indices and Their Generating Functions*, INTEGERS 26 (2026), Article A83, proof of Proposition 3.

Formalized by `MetaMathlibExt.TriangularRecurrence.reflect_reflect`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html#reflect-reflect).

## Linear Diophantine equations

Let $a, b, c, u, v \in \mathbb{Z}$ with $a \ne 0$ or
$b \ne 0$, let $d = \gcd(a, b)$, and suppose $a u + b v = d$ (Bézout). If $d \mid c$, then the
integers $x, y$ with $a x + b y + c = 0$ are exactly those of the form
$x = -(c/d) u + m (b/d)$, $y = -(c/d) v - m (a/d)$ with $m \in \mathbb{Z}$. If $d \nmid c$, then
$a x + b y + c = 0$ has no solution in integers $x, y$.

## Sources

- Lars Palapies, *On Extensions of Triangular Arrays to Negative Row Indices and Their Generating Functions*, INTEGERS 26 (2026), Article A83, Proposition 1.

Stated but not proved: `MetaMathlibExt.linear_diophantine_solutions` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html#linear-diophantine-solutions).

## Knuth-type duality

For integers $\alpha, \beta, \gamma$, let $a$ and $b$ be the arrays with
parameters $(\alpha, \beta, \gamma; 0, 0, 1)$ and $(\beta, \alpha, -\gamma; 0, 0, 1)$. Then their
negative-negative numbers satisfy $a^{NN}_{-n,-k} = b^{NN}_{k-1,n-1}$ for all $n, k \in \mathbb{Z}$.

This generalizes the identity $[-n, -k] = \{k, n\}$ between the Stirling numbers $[n, k]$ of the
first kind and $\{n, k\}$ of the second kind.

## Sources

- Lars Palapies, *On Extensions of Triangular Arrays to Negative Row Indices and Their Generating Functions*, INTEGERS 26 (2026), Article A83, Proposition 2.

Stated but not proved: `MetaMathlibExt.TriangularRecurrence.negNeg_duality` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html#neg-neg-duality).

## NP/NN duality

Let $a$ be the array of a triangular recurrence with parameters
$(\alpha, \beta, \gamma; \alpha', \beta', \gamma')$, with weights
$w(n, k) = \alpha(n + 1) + \beta k + \gamma$ and $w'(n, k) = \alpha'(n + 1) + \beta' k + \gamma'$,
and let $\tilde a$ be the array of the reflected recurrence, with parameters
$(\alpha' + \beta', -\beta', \gamma'; \alpha + \beta, -\beta, \gamma)$ and weights $\tilde w$,
$\tilde w'$. Then for all integers $n, k$ the negative-positive and negative-negative numbers
satisfy $\tilde a^{NP}_{n,k} = a^{NN}_{n,n-k}$ and $\tilde a^{NN}_{n,n-k} = a^{NP}_{n,k}$.
Moreover, $\tilde w(n, k) \ne 0$ for all integers $n < 0 \le k$ if and only if
$w'(n, k + 1) \ne 0$ for all integers $k \le n < 0$; and $\tilde w'(n, k + 1) \ne 0$ for all
integers $k \le n < 0$ if and only if $w(n, k) \ne 0$ for all integers $n < 0 \le k$.

Thus the divisor condition of Definition 1 for $\tilde a$ is equivalent to that of Definition 2
for $a$, and conversely, so the left-hand sides exist exactly when the right-hand sides do.
With junk value $0$ for a zero divisor, the two identities need no existence hypothesis.

## Sources

- Lars Palapies, *On Extensions of Triangular Arrays to Negative Row Indices and Their Generating Functions*, INTEGERS 26 (2026), Article A83, Proposition 3.

Stated but not proved: `MetaMathlibExt.TriangularRecurrence.reflect_negPos_eq_negNeg` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html#reflect-neg-pos-eq-neg-neg).

## Generating function of the negative-positive numbers for $\beta = \beta' = 0$

Let
$\alpha, \gamma, \alpha', \gamma'$ be integers and let $a^{NP}$ be the negative-positive numbers
for the parameters $(\alpha, 0, \gamma; \alpha', 0, \gamma')$. For every $n \ge 0$, in the ring
$\mathbb{Q}[[u]]$ of formal power series,

$$
\sum_{k \ge 0} a^{NP}_{-n,k} u^k =
\Bigl(\prod_{j=0}^{n-1} \bigl((\gamma - j\alpha) + (\gamma' - j\alpha') u\bigr)\Bigr)^{-1},
$$

where the inverse of a power series with constant term $0$ is taken to be $0$.

Coefficientwise in $x^n/n!$ this is Theorem 1, which says that the exponential generating
function $\bar F(u, x) = \sum_{n,k \ge 0} a^{NP}_{-n,k} u^k x^n/n!$ equals the hypergeometric
series ${}_0F_1(-; b; -x/(\alpha + \alpha' u))$
with $b = -(\gamma + \gamma' u)/(\alpha + \alpha' u)$, and $e^{x/(\gamma + \gamma' u)}$ when
$\alpha = \alpha' = 0$: the rising factorial $b^{\overline{n}} = b(b+1)\cdots(b+n-1)$ satisfies
$b^{\overline{n}} (-(\alpha + \alpha' u))^n =
\prod_{j\lt n} (\gamma + \gamma' u - j(\alpha + \alpha' u))$. The paper's existence hypothesis
($\gamma - j\alpha \ne 0$ for all $j$) is not needed: a zero divisor makes both sides $0$ from
that row on.

## Sources

- Lars Palapies, *On Extensions of Triangular Arrays to Negative Row Indices and Their Generating Functions*, INTEGERS 26 (2026), Article A83, Theorem 1.

Stated but not proved: `MetaMathlibExt.TriangularRecurrence.negPos_egf_beta_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PalapiesTriangularArraysWanted.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html#neg-pos-egf-beta-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Triangular recurrence arrays at negative indices](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/triangular-recurrence-arrays-at-negative-indices)
