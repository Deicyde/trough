---
declaration: section
origin: cited
lean: MathlibExt.LinearAlgebra.PowerSumMatrixWanted.trace_pow_two, MathlibExt.LinearAlgebra.PowerSumMatrixWanted.integral_pow_one_sub_pow, MathlibExt.LinearAlgebra.TraceNewtonWanted.LinearAlgebra.TraceNewton.charpolyDescendingCoeff, MathlibExt.LinearAlgebra.TraceNewtonWanted.LinearAlgebra.TraceNewton.trace_cayley_hamilton_newton
statement: formalized
---

# Newton's identities for traces of matrix powers

4 results, 1 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/newton-s-identities-for-traces-of-matrix-powers/index.html).

## Traces of powers of a $2 \times 2$ matrix

Let $M$ be a real $2 \times 2$ matrix and
let $m \ge 1$ be an integer. Then

$$\operatorname{tr}(M^{2m}) = 2m \sum_{r=0}^{m} (-1)^r \frac{(2m - r - 1)!}{r! \, (2m - 2r)!}
(\det M)^r (\operatorname{tr} M)^{2m - 2r}$$

and

$$\operatorname{tr}(M^{2m+1}) = (2m + 1) \sum_{r=0}^{m} (-1)^r
\frac{(2m - r)!}{r! \, (2m + 1 - 2r)!} (\det M)^r (\operatorname{tr} M)^{2m + 1 - 2r}.$$

## Sources

- Peiran Ding, Yanjun Zhu and Lei Wang, "A New Formula for the Sum of Integer Powers Based on Elementary Matrix Theory", Theorem 1, equations (5) and (6).

Stated but not proved: `MathlibExt.LinearAlgebra.PowerSumMatrixWanted.trace_pow_two` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/PowerSumMatrixWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/LinearAlgebra/PowerSumMatrixWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/newton-s-identities-for-traces-of-matrix-powers/index.html#trace-pow-two).

## Integral of $x^r (1 - x)^r$ over $(0, 1)$

For every natural number $r$ (including
$r = 0$),

$$\int_0^1 x^r (1 - x)^r \, dx = \frac{1}{(2r + 1) \binom{2r}{r}}.$$

## Sources

- Peiran Ding, Yanjun Zhu and Lei Wang, "A New Formula for the Sum of Integer Powers Based on Elementary Matrix Theory", Lemma 3.

Stated but not proved: `MathlibExt.LinearAlgebra.PowerSumMatrixWanted.integral_pow_one_sub_pow` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/PowerSumMatrixWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/LinearAlgebra/PowerSumMatrixWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/newton-s-identities-for-traces-of-matrix-powers/index.html#integral-pow-one-sub-pow).

## Characteristic-polynomial coefficients in descending order

Let $A$ be a square matrix
over a commutative ring $R$ whose rows and columns are indexed by a finite set of size $N$, and
write its characteristic polynomial as $\chi_A(X) = \det(X I - A) = X^N + c_1 X^{N-1} + \dots +
c_N$. For a natural number $k$, the descending coefficient $c_k$ of $A$ is the coefficient of
$X^{N-k}$ in $\chi_A$ when $k \le N$, and $0$ when $k > N$.

Setting $c_k = 0$ for $k > N$ lets the trace recurrence be stated uniformly for all positive $k$.

Formalized by `MathlibExt.LinearAlgebra.TraceNewtonWanted.LinearAlgebra.TraceNewton.charpolyDescendingCoeff`, a definition declared in [WantedExt/LinearAlgebra/TraceNewtonWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/LinearAlgebra/TraceNewtonWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/newton-s-identities-for-traces-of-matrix-powers/index.html#charpoly-descending-coeff).

## Newton's trace identities for the characteristic polynomial

Let $A$ be a square matrix
over a commutative ring $R$ whose rows and columns are indexed by a finite set of size $N$. For
each natural number $k$, let $c_k$ be the coefficient of $X^{N-k}$ in the characteristic
polynomial $\chi_A(X) = \det(X I - A)$ when $k \le N$, and $c_k = 0$ when $k > N$, so that
$\chi_A(X) = X^N + c_1 X^{N-1} + \dots + c_N$. Then for every natural number $k \ge 1$,

$$k \, c_k + \sum_{j=1}^{k} \operatorname{tr}(A^j) \, c_{k-j} = 0,$$

where $k$ is read as an element of $R$.

## Sources

- Knill, *Some fundamental theorems in mathematics*, §220. Problem `trace_cayley_hamilton_newton` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.LinearAlgebra.TraceNewtonWanted.LinearAlgebra.TraceNewton.trace_cayley_hamilton_newton` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/TraceNewtonWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/LinearAlgebra/TraceNewtonWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/newton-s-identities-for-traces-of-matrix-powers/index.html#trace-cayley-hamilton-newton).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Newton's identities for traces of matrix powers](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/newton-s-identities-for-traces-of-matrix-powers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/newton-s-identities-for-traces-of-matrix-powers)
