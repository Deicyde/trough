---
declaration: section
origin: cited
lean: MathlibExt.Algebra.RealZerosParityChangeBoundWanted.cTilde, MathlibExt.Algebra.RealZerosParityChangeBoundWanted.posIndices, MathlibExt.Algebra.RealZerosParityChangeBoundWanted.vVal, MathlibExt.Algebra.RealZerosParityChangeBoundWanted.conjecture, MathlibExt.Algebra.RealZerosParityChangeBoundWanted.conjecture_refuted
statement: formalized
---

# Parity-change bound on real zeros

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/parity-change-bound-on-real-zeros/index.html).

## Newton-type coefficient differences

For a real polynomial $f = \sum_k a_k x^k$ and a
natural number $k$, $\tilde c_k(f) = (k+1)\,a_k^2 - k\,a_{k-1}a_{k+1}$, where $a_j = 0$ for $j$
above the degree of $f$; for $k = 0$ the second term vanishes, so $\tilde c_0(f) = a_0^2$.

Formalized by `MathlibExt.Algebra.RealZerosParityChangeBoundWanted.cTilde`, a definition declared in [WantedExt/Algebra/RealZerosParityChangeBoundWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/RealZerosParityChangeBoundWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/parity-change-bound-on-real-zeros/index.html#c-tilde).

## Indices with positive Newton-type difference

For a real polynomial
$f = a_0 + a_1 x + \dots + a_n x^n$ of degree $n$ (with $n = 0$ for $f = 0$), set $a_{n+1} = 0$,
$\tilde c_0(f) = a_0^2$ and $\tilde c_k(f) = (k+1)\,a_k^2 - k\,a_{k-1}a_{k+1}$ for $1 \le k \le n$.
This is the list of the indices $k \in \{0, \dots, n\}$ with $\tilde c_k(f) > 0$, in increasing
order.

Formalized by `MathlibExt.Algebra.RealZerosParityChangeBoundWanted.posIndices`, a definition declared in [WantedExt/Algebra/RealZerosParityChangeBoundWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/RealZerosParityChangeBoundWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/parity-change-bound-on-real-zeros/index.html#pos-indices).

## Parity changes of the positive-difference indices

For a real polynomial
$f = a_0 + a_1 x + \dots + a_n x^n$ of degree $n$ (with $n = 0$ for $f = 0$), set $a_{n+1} = 0$,
$\tilde c_0(f) = a_0^2$ and $\tilde c_k(f) = (k+1)\,a_k^2 - k\,a_{k-1}a_{k+1}$ for $1 \le k \le n$.
Let $k_1 < k_2 < \dots < k_m$ be the indices $k \le n$ with $\tilde c_k(f) > 0$. Then $v(f)$ is the
number of $i < m$ such that $k_i$ and $k_{i+1}$ have different parities.

Formalized by `MathlibExt.Algebra.RealZerosParityChangeBoundWanted.vVal`, a definition declared in [WantedExt/Algebra/RealZerosParityChangeBoundWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/RealZerosParityChangeBoundWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/parity-change-bound-on-real-zeros/index.html#v-val).

## Parity-change bound on real zeros (conjecture)

For a real polynomial
$f = a_0 + a_1 x + \dots + a_n x^n$ of degree $n$, set $a_{n+1} = 0$, $\tilde c_0(f) = a_0^2$ and
$\tilde c_k(f) = (k+1)\,a_k^2 - k\,a_{k-1}a_{k+1}$ for $1 \le k \le n$, and let $v(f)$ be the
number of parity changes between consecutive terms of the increasing list of indices $k \le n$
with $\tilde c_k(f) > 0$. The conjecture asserts that every such $f$ with $a_k > 0$ for all
$0 \le k \le n$ has at most $v(f)$ distinct real zeros.

## Sources

- AMR-021-0014.

Formalized by `MathlibExt.Algebra.RealZerosParityChangeBoundWanted.conjecture`, a definition declared in [WantedExt/Algebra/RealZerosParityChangeBoundWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/RealZerosParityChangeBoundWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/parity-change-bound-on-real-zeros/index.html#conjecture).

## The parity-change bound on real zeros is false

For a real polynomial
$f = a_0 + a_1 x + \dots + a_n x^n$ of degree $n$, set $a_{n+1} = 0$, $\tilde c_0(f) = a_0^2$ and
$\tilde c_k(f) = (k+1)\,a_k^2 - k\,a_{k-1}a_{k+1}$ for $1 \le k \le n$, and let $v(f)$ be the
number of parity changes between consecutive terms of the increasing list of indices $k \le n$
with $\tilde c_k(f) > 0$. There is such an $f$ with $a_k > 0$ for all $0 \le k \le n$ whose number
of distinct real zeros exceeds $v(f)$.

Katkova, Shapiro and Vishnyakova (Sec. 5) disprove Conjecture 9 via iterated primitives $Q_n$ of
an explicit $Q_{15}$. Splitting the repeated root also refutes the distinct-zero reading used
here: $\prod_{j<23}(x+1+j/10^4)\,(38x^2-199x+363)$ has positive coefficients, 23 distinct real
zeros and $v = 21$.

## Sources

- Olga Katkova, Boris Shapiro and Anna Vishnyakova, In search of Newton-type inequalities, arXiv:2403.12200 (2024), https://arxiv.org/abs/2403.12200.

Stated but not proved: `MathlibExt.Algebra.RealZerosParityChangeBoundWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Algebra/RealZerosParityChangeBoundWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/RealZerosParityChangeBoundWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/parity-change-bound-on-real-zeros/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Parity-change bound on real zeros](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/parity-change-bound-on-real-zeros/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/zeros-of-polynomials/parity-change-bound-on-real-zeros)
