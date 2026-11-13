---
declaration: section
origin: cited
lean: MetaMathlibExt.meshPatternGeneratingFunction_eq_factorial_mul_prod_general, MetaMathlibExt.meshPatternGeneratingFunction_eq_factorial_mul_prod, MetaMathlibExt.MatchPred, MetaMathlibExt.ZeroPred, MetaMathlibExt.meshN, MetaMathlibExt.PolyN, MetaMathlibExt.meshPatternCount_stirlingRecursion, MetaMathlibExt.meshPatternCount_eq_factorial_mul_rStirlingNumber_general
statement: formalized
proof: formalized
---

# Mesh patterns in permutations

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/mesh-patterns-in-permutations/index.html).

## Product formula from the mesh-pattern recurrence

Let $R$ be a commutative semiring, let
$x \in R$, let $0 < k \le n$ be natural numbers, and let $P(m, r) \in R$ for natural numbers
$m, r$. Natural numbers are mapped into $R$. Suppose that $P(k-1, k) = (k-1)!$ and that
$P(m, k) = (x + (m - 1))\,P(m-1, k)$ for every natural number $m \ge k$. Then

$$P(n, k) = (k-1)! \prod_{i=0}^{n-k} \bigl(x + (k - 1 + i)\bigr).$$

With $R$ the polynomials over $\mathbb{N}$ and $x$ the variable, this is the product formula for
the mesh-pattern counting polynomial.

## Sources

- Matt Davis, "Quadrant Marked Mesh Patterns and the r-Stirling Numbers," Journal of Integer Sequences 18 (2015), Article 15.10.1, Corollary, line 194, with the recurrence and base value from Theorem, line 175, <https://cs.uwaterloo.ca/journals/JIS/VOL18/Davis/davis3.tex>.

Formalized by `MetaMathlibExt.meshPatternGeneratingFunction_eq_factorial_mul_prod_general`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MeshPatternGeneratingFunction.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MeshPatternGeneratingFunction.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/mesh-patterns-in-permutations/index.html#mesh-pattern-generating-function-eq-fact).

## Product formula from the mesh-pattern recurrence, real case

Let $0 < k \le n$ be natural
numbers, let $x$ be a real number, and let $P(m, r, y)$ be real numbers indexed by natural
numbers $m, r$ and a real number $y$. Suppose that $P(k-1, k, x) = (k-1)!$ and that
$P(m, k, x) = (x + m - 1)\,P(m-1, k, x)$ for every natural number $m \ge k$. Then

$$P(n, k, x) = (k-1)! \prod_{i=0}^{n-k} (x + k - 1 + i).$$

## Sources

- Matt Davis, "Quadrant Marked Mesh Patterns and the r-Stirling Numbers," Journal of Integer Sequences 18 (2015), Article 15.10.1, Corollary, line 194, with the recurrence and base value from Theorem, line 175, <https://cs.uwaterloo.ca/journals/JIS/VOL18/Davis/davis3.tex>.

Formalized by `MetaMathlibExt.meshPatternGeneratingFunction_eq_factorial_mul_prod`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MeshPatternGeneratingFunction.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MeshPatternGeneratingFunction.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/mesh-patterns-in-permutations/index.html#mesh-pattern-generating-function-eq-fact-2).

## Mesh-pattern match

Let $\sigma$ be a permutation of $m$ elements, with positions numbered
$1, \dots, m$, let $p$ be the position of the largest value of $\sigma$, and let $r$ be a natural
number. A position $i$ is a mesh-pattern match of $\sigma$ with parameter $r$ when
$\sigma(t) < \sigma(i)$ for every position $t < i$ and at least $r - 1$ positions $t$ with
$i < t < p$ have $\sigma(t) > \sigma(i)$.

Formalized by `MetaMathlibExt.MatchPred`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MeshPatternStirlingRecursion.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MeshPatternStirlingRecursion.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/mesh-patterns-in-permutations/index.html#match-pred).

## Mesh-pattern zero condition

Let $\sigma$ be a permutation of $m$ elements, with positions
numbered $1, \dots, m$, and let $r$ be a natural number. The zero condition holds for $\sigma$
with parameter $r$ when some position $p \ge r$ holds the largest value of $\sigma$.

Formalized by `MetaMathlibExt.ZeroPred`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MeshPatternStirlingRecursion.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MeshPatternStirlingRecursion.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/mesh-patterns-in-permutations/index.html#zero-pred).

## Canonical mesh-pattern statistic

Let $\sigma$ be a permutation of $m$ elements, with
positions numbered $1, \dots, m$, and let $r$ be a natural number. The statistic $N_r(\sigma)$ is
the number of mesh-pattern matches of $\sigma$ with parameter $r$, plus $1$ if the mesh-pattern
zero condition holds, that is, if the largest value of $\sigma$ sits at a position $p \ge r$.

Formalized by `MetaMathlibExt.meshN`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MeshPatternStirlingRecursion.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MeshPatternStirlingRecursion.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/mesh-patterns-in-permutations/index.html#mesh-n).

## Mesh-pattern counting polynomial

For natural numbers $m$ and $r$, the polynomial
$P_{m,r}(X) \in \mathbb{N}[X]$ is the sum of $X^{N_r(\sigma)}$ over all permutations $\sigma$ of
$m$ elements, where $N_r(\sigma)$ is the canonical mesh-pattern statistic with parameter $r$.

Formalized by `MetaMathlibExt.PolyN`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MeshPatternStirlingRecursion.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MeshPatternStirlingRecursion.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/mesh-patterns-in-permutations/index.html#poly-n).

## Stirling-type recursion for the mesh-pattern counting polynomial

Let $1 < k \le n$ and
$j > 0$. For a permutation $\sigma$ of $m$ elements, with positions numbered $1, \dots, m$, let
$p$ be the position of its largest value and let $N_r(\sigma)$ be the number of positions $i$
such that $\sigma(t) < \sigma(i)$ for all $t < i$ and at least $r - 1$ positions $t$ with
$i < t < p$ have $\sigma(t) > \sigma(i)$, plus $1$ if $p \ge r$. Let $P_{m,r}(X) \in \mathbb{N}[X]$
be the sum of $X^{N_r(\sigma)}$ over all permutations $\sigma$ of $m$ elements, and let
$c_{m,r}(s)$ be its coefficient of $X^s$. Then
$c_{n,k}(j) = (n-1)\,c_{n-1,k}(j) + c_{n-1,k}(j-1)$,
$P_{n,k}(X) = (X + n - 1)\,P_{n-1,k}(X)$, $c_{n,k}(0) = (n-1)\,c_{n-1,k}(0)$, and
$P_{k-1,k}(X) = (k-1)!$.

## Sources

- Matt Davis, "Quadrant Marked Mesh Patterns and the r-Stirling Numbers," Journal of Integer Sequences 18 (2015), Article 15.10.1, Theorem, line 175, <https://cs.uwaterloo.ca/journals/JIS/VOL18/Davis/davis3.tex>.

Formalized by `MetaMathlibExt.meshPatternCount_stirlingRecursion`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MeshPatternStirlingRecursion.lean, line 967](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MeshPatternStirlingRecursion.lean#L967). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/mesh-patterns-in-permutations/index.html#mesh-pattern-count-stirling-recursion).

## Distribution of the canonical mesh-pattern statistic

Let $2 \le k \le n$ and let $j$ be a
natural number. For a permutation $\sigma$ of $\{1, \dots, n\}$ with positions numbered
$1, \dots, n$, let $p$ be the position of its largest value, and let $N_k(\sigma)$ be the
canonical mesh-pattern statistic: the number of positions $i$ such that $\sigma(t) < \sigma(i)$
for all $t < i$ and at least $k - 1$ positions $t$ with $i < t < p$ have $\sigma(t) > \sigma(i)$,
plus $1$ if $p \ge k$. Then the number of permutations $\sigma$ of $\{1, \dots, n\}$ with
$N_k(\sigma) = j$ equals $(k-1)!\, c_{k-1}(n, j + k - 1)$, where the unsigned $r$-Stirling
number of the first kind $c_r(n, m)$ is the coefficient of $X^m$ in
$X^r (X + r)(X + r + 1) \cdots (X + n - 1)$.

Formalized by `MetaMathlibExt.meshPatternCount_eq_factorial_mul_rStirlingNumber_general`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MeshPatternRStirling.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MeshPatternRStirling.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/mesh-patterns-in-permutations/index.html#mesh-pattern-count-eq-factorial-mul-r-st).

## Counting permutations by mesh-pattern matches

Let $2 \le k \le n$ and let $j$ be a
natural number. For a permutation $\sigma$ of $\{1, \dots, n\}$, let $p$ be the position of its
largest entry, and call a position $i$ a match if $\sigma(t) < \sigma(i)$ for every position
$t < i$ and at least $k - 1$ positions $q$ with $i < q < p$ have $\sigma(q) > \sigma(i)$. Let
$N(\sigma)$ be the number of matches, plus $1$ if $p \ge k$. Then the number of permutations
$\sigma$ of $\{1, \dots, n\}$ with $N(\sigma) = j$ equals $(k-1)!\, c_{k-1}(n, j + k - 1)$, where
the unsigned $r$-Stirling number of the first kind $c_r(n, m)$ is the coefficient of $X^m$ in
$X^r (X + r)(X + r + 1) \cdots (X + n - 1)$.

## Sources

- Matt Davis, "Quadrant Marked Mesh Patterns and the r-Stirling Numbers", Journal of Integer Sequences 18 (2015), Article 15.10.1, Theorem `thm:rstir`, line 201, <https://cs.uwaterloo.ca/journals/JIS/VOL18/Davis/davis3.tex>.

Formalized by `MetaMathlibExt.meshPatternCount_eq_factorial_mul_rStirlingNumber`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MeshPatternRStirling.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MeshPatternRStirling.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/mesh-patterns-in-permutations/index.html#mesh-pattern-count-eq-factorial-mul-r-st-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mesh patterns in permutations](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/mesh-patterns-in-permutations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/permutations/permutation-patterns/mesh-patterns-in-permutations)
