---
declaration: section
origin: cited
lean: MetaMathlibExt.bellRiordan_hasNonnegativeMinors_of_aSequence, MetaMathlibExt.IsRiordanArrayAZ, MetaMathlibExt.IsRiordanArrayAZ.one_zero_and_one_one, MetaMathlibExt.riordanCoeffMatrix, MetaMathlibExt.riordanCoeffMatrix_zero_one, MetaMathlibExt.riordanArray_hasNonnegativeMinors_of_coeffMatrix, MetaMathlibExt.riordanArray_hasNonnegativeMinors_of_params, MetaMathlibExt.bellRiordanArray_hasNonnegativeMinors_of_pf
statement: formalized
---

# Total positivity of Riordan arrays

8 results, 4 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/total-positivity-of-riordan-arrays/index.html).

## Bell-type Riordan arrays with a Pólya frequency A-sequence are totally positive

Let $g$
be a formal power series over $\mathbb{R}$ with $g(0) \neq 0$, write $[x^n]F$ for the coefficient
of $x^n$ in a power series $F$, and let $D = (d_{n,k})_{n,k \ge 0}$ be the Bell-type Riordan array
$(g(x), x g(x))$, with entries $d_{n,k} = [x^n]\, g(x) (x g(x))^k$. Let $(a_j)_{j \ge 0}$ be a
real sequence, the $A$-sequence of $D$, such that for all $n, k \ge 0$

$$d_{n+1,k+1} = \sum_{j=0}^{n} a_j\, d_{n,k+j}.$$

If $(a_j)$ is a Pólya frequency sequence, that is, every minor of its lower Toeplitz matrix
(whose entry in row $n$ and column $k$ is $a_{n-k}$ for $k \le n$ and $0$ otherwise) is
nonnegative, then $D$ is totally positive: every minor of $D$ is nonnegative.

The sum stops at $j = n$ because $d_{n,m} = 0$ for $m > n$.

## Sources

- Lili Mu, Yuanyuan Xing and Sai-Nan Zheng, *A New Criterion for the Total Positivity of Riordan Arrays*, Journal of Integer Sequences 28 (2025), Article 25.7.5, Proposition 5.

Stated but not proved: `MetaMathlibExt.bellRiordan_hasNonnegativeMinors_of_aSequence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BellRiordanTotalPositivityWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/BellRiordanTotalPositivityWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/total-positivity-of-riordan-arrays/index.html#bell-riordan-has-nonnegative-minors-of-a).

## Riordan array with given A- and Z-sequences

For real sequences $(a_n)_{n \ge 0}$ and
$(z_n)_{n \ge 0}$, an infinite real matrix $R = (r_{n,k})_{n,k \ge 0}$ is the Riordan array with
$A$-sequence $(a_n)$ and $Z$-sequence $(z_n)$ when $r_{0,0} = 1$, $r_{0,k} = 0$ for $k \ge 1$, and
for all $n, k \ge 0$

$$r_{n+1,0} = \sum_{j=0}^{n} z_j\, r_{n,j}, \qquad r_{n+1,k+1} = \sum_{j=0}^{n} a_j\, r_{n,k+j}.$$

The sums stop at $j = n$ because the recurrence forces $r_{n,m} = 0$ for $m > n$.

## Sources

- Lili Mu, Yuanyuan Xing and Sai-Nan Zheng, *A New Criterion for the Total Positivity of Riordan Arrays*, Journal of Integer Sequences 28 (2025), Article 25.7.5, Section 1, equation (1).

Formalized by `MetaMathlibExt.IsRiordanArrayAZ`, a definition declared in [WantedExt/Combinatorics/Enumerative/BellRiordanTotalPositivityWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/BellRiordanTotalPositivityWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/total-positivity-of-riordan-arrays/index.html#is-riordan-array-az).

## Entries in row 1 of a Riordan array

If $R = (r_{n,k})_{n,k \ge 0}$ is the Riordan array
with $A$-sequence $(a_n)$ and $Z$-sequence $(z_n)$, for real sequences $(a_n)$ and $(z_n)$, then
$r_{1,0} = z_0$ and $r_{1,1} = a_0$.

## Sources

- Lili Mu, Yuanyuan Xing and Sai-Nan Zheng, *A New Criterion for the Total Positivity of Riordan Arrays*, Journal of Integer Sequences 28 (2025), Article 25.7.5, Section 1, equation (1).

Formalized by `MetaMathlibExt.IsRiordanArrayAZ.one_zero_and_one_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/BellRiordanTotalPositivityWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/BellRiordanTotalPositivityWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/total-positivity-of-riordan-arrays/index.html#one-zero-and-one-one).

## Coefficient matrix of a Riordan array

For real sequences $(z_n)_{n \ge 0}$ and
$(a_n)_{n \ge 0}$ with generating functions $Z(x)$ and $A(x)$, the coefficient matrix
$J(Z(x), A(x))$ is the infinite real matrix, with rows and columns indexed by $n, k \ge 0$, whose
entry in row $n$ and column $k$ is $z_n$ if $k = 0$, is $a_{n+1-k}$ if $1 \le k \le n + 1$, and is
$0$ if $k > n + 1$. Thus row $n$ reads $z_n, a_n, a_{n-1}, \ldots, a_0, 0, 0, \ldots$

## Sources

- Lili Mu, Yuanyuan Xing and Sai-Nan Zheng, *A New Criterion for the Total Positivity of Riordan Arrays*, Journal of Integer Sequences 28 (2025), Article 25.7.5, Section 1.

Formalized by `MetaMathlibExt.riordanCoeffMatrix`, a definition declared in [WantedExt/Combinatorics/Enumerative/BellRiordanTotalPositivityWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/BellRiordanTotalPositivityWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/total-positivity-of-riordan-arrays/index.html#riordan-coeff-matrix).

## First two columns of the coefficient matrix of a Riordan array

For real sequences
$(z_n)$ and $(a_n)$ with generating functions $Z(x)$ and $A(x)$, and for every $n \ge 0$, the
coefficient matrix $J(Z(x), A(x))$ has entry $z_n$ in row $n$, column $0$, and entry $a_n$ in
row $n$, column $1$.

## Sources

- Lili Mu, Yuanyuan Xing and Sai-Nan Zheng, *A New Criterion for the Total Positivity of Riordan Arrays*, Journal of Integer Sequences 28 (2025), Article 25.7.5, Section 1.

Formalized by `MetaMathlibExt.riordanCoeffMatrix_zero_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/BellRiordanTotalPositivityWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/BellRiordanTotalPositivityWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/total-positivity-of-riordan-arrays/index.html#riordan-coeff-matrix-zero-one).

## Total positivity of a Riordan array from its coefficient matrix

Let $(a_n)$ and $(z_n)$
be real sequences with generating functions $A(x)$ and $Z(x)$, and let $R$ be the Riordan array
with $A$-sequence $(a_n)$ and $Z$-sequence $(z_n)$. If the coefficient matrix $J(Z(x), A(x))$ is
totally positive, that is, every minor of it is nonnegative, then every minor of $R$ is
nonnegative.

## Sources

- Lili Mu, Yuanyuan Xing and Sai-Nan Zheng, *A New Criterion for the Total Positivity of Riordan Arrays*, Journal of Integer Sequences 28 (2025), Article 25.7.5, Proposition 1 (`jis-2025-25.7.5-prop-1`).

Stated but not proved: `MetaMathlibExt.riordanArray_hasNonnegativeMinors_of_coeffMatrix` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BellRiordanTotalPositivityWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/BellRiordanTotalPositivityWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/total-positivity-of-riordan-arrays/index.html#riordan-array-has-nonnegative-minors-of).

## A total positivity criterion for Riordan arrays

Let $P, Q, A, Z$ be formal power series
over $\mathbb{R}$ with $P(0) \ne 0$, write $[x^n]F$ for the coefficient of $x^n$ in a power
series $F$, and let $a, b, r, s, t \ge 0$ be real numbers. Suppose that

$$A(x)\,(P(x) - rx) = P(x)^2 + sxP(x) + tx^2$$

and

$$Z(x)\,(P(x)^2 - rxP(x)) =
(P(x)^2 + sxP(x) + tx^2)\,Q(x) + (aP(x) + bx)(P(x) - xQ(x)),$$

and let $R$ be the Riordan array whose $A$-sequence is $([x^n]A)_{n \ge 0}$ and whose
$Z$-sequence is $([x^n]Z)_{n \ge 0}$. Let $J(Q(x), P(x))$ be the coefficient matrix whose row
$n \ge 0$ reads $[x^n]Q, [x^n]P, [x^{n-1}]P, \dots, [x^0]P, 0, 0, \dots$. Call a matrix totally
positive when every minor of it is nonnegative. If $J(Q(x), P(x))$ is totally positive,
$s^2 \ge 4t$ and $as + a\sqrt{s^2 - 4t} \ge 2b$, then $R$ is totally positive.

Since $P(0) \ne 0$, the series $P(x) - rx$ and $P(x)^2 - rxP(x)$ are invertible, so the two
hypotheses say $A = (P^2 + sxP + tx^2)/(P - rx)$ and
$Z = ((P^2 + sxP + tx^2)Q + (aP + bx)(P - xQ))/(P^2 - rxP)$.

## Sources

- Lili Mu, Yuanyuan Xing and Sai-Nan Zheng, *A New Criterion for the Total Positivity of Riordan Arrays*, Journal of Integer Sequences 28 (2025), Article 25.7.5, Theorem 2 (`jis-2025-25.7.5-thm-2`).

Stated but not proved: `MetaMathlibExt.riordanArray_hasNonnegativeMinors_of_params` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BellRiordanTotalPositivityWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/BellRiordanTotalPositivityWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/total-positivity-of-riordan-arrays/index.html#riordan-array-has-nonnegative-minors-of-2).

## Total positivity of Bell-type Riordan arrays from a Pólya frequency series

Let $P$ and
$A$ be formal power series over $\mathbb{R}$ with $P(0) \ne 0$, write $[x^n]F$ for the
coefficient of $x^n$ in a power series $F$, and let $r, s, t \ge 0$ be real numbers with
$s^2 \ge 4t$. Suppose that $P$ is a Pólya frequency series, that is, every minor of the lower
Toeplitz matrix of its coefficients (whose entry in row $n$ and column $k$ is $[x^{n-k}]P$ for
$k \le n$ and $0$ otherwise) is nonnegative, and that

$$A(x)\,(P(x) - rx) = P(x)^2 + sxP(x) + tx^2.$$

Let $R$ be the Riordan array with $A$-sequence $(a_n)_{n \ge 0}$ and $Z$-sequence
$(z_n)_{n \ge 0}$, where $a_n = [x^n]A$ and $z_n = a_{n+1}$ (a Bell-type Riordan array). Then
$R$ is totally positive: every minor of $R$ is nonnegative.

Since $P(0) \ne 0$, the series $P(x) - rx$ is invertible, so the hypothesis on $A$ says
$A = (P^2 + sxP + tx^2)/(P - rx)$.

## Sources

- Lili Mu, Yuanyuan Xing and Sai-Nan Zheng, *A New Criterion for the Total Positivity of Riordan Arrays*, Journal of Integer Sequences 28 (2025), Article 25.7.5, Corollary 6 (`jis-2025-25.7.5-cor-6`).

Stated but not proved: `MetaMathlibExt.bellRiordanArray_hasNonnegativeMinors_of_pf` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BellRiordanTotalPositivityWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/BellRiordanTotalPositivityWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/total-positivity-of-riordan-arrays/index.html#bell-riordan-array-has-nonnegative-minor).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Total positivity of Riordan arrays](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/total-positivity-of-riordan-arrays/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/total-positivity-of-riordan-arrays)
