---
declaration: section
origin: cited
lean: MetaMathlibExt.bell_convolution_linear_recurrence_of_charZero, MetaMathlibExt.bell_convolution_linear_recurrence, MetaMathlibExt.bell_convolution_linear_recurrence_partialBellPolynomial, MetaMathlibExt.invertTransform, MetaMathlibExt.invertTransform_spec
statement: formalized
proof: formalized
---

# INVERT transform

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/invert-transform/index.html).

## Linear recurrence for INVERT convolution powers in characteristic zero

Let $K$ be a
field of characteristic zero and let $(c_m)_{m \ge 0}$ and $(y_n)_{n \ge 0}$ be sequences in $K$
such that for every $n \ge 0$

$$y_n = \sum_{k=0}^{n} k! \sum_{j} \prod_{i=1}^{n+1} \frac{c_i^{j_i}}{j_i!},$$

where the inner sum runs over all tuples $(j_1, \dots, j_{n+1})$ of integers with
$0 \le j_i \le n$, $j_1 + j_2 + \dots + j_{n+1} = k$ and $j_1 + 2 j_2 + \dots + (n+1) j_{n+1} = n$.
Let $r \ge 1$ be an integer, and for $N \ge 0$ let $y^{(r)}_N$ be the sum of
$y_{a_1} y_{a_2} \cdots y_{a_r}$ over all tuples $(a_1, \dots, a_r)$ of nonnegative integers with
$a_1 + \dots + a_r = N$. Then for every $n \ge 1$

$$n \, y^{(r)}_n = \sum_{m=1}^{n} \bigl(n + m(r-1)\bigr) \, c_m \, y^{(r)}_{n-m}.$$

The hypothesis says that $y_n = \sum_{k=0}^{n} \frac{k!}{n!} B_{n,k}(1!\,c_1, 2!\,c_2, \dots)$
with the partial Bell polynomials $B_{n,k}$, that is, $y$ is the INVERT transform of $c$: as
formal power series in $z$, $\sum_{n \ge 0} y_n z^n = 1/(1 - \sum_{m \ge 1} c_m z^m)$. The value
$c_0$ plays no role, and the theorem for real sequences is the case $K = \mathbb{R}$.

Formalized by `MetaMathlibExt.bell_convolution_linear_recurrence_of_charZero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BellPolynomialConvolutionRecurrence.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/BellPolynomialConvolutionRecurrence.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/invert-transform/index.html#bell-convolution-linear-recurrence-of-ch).

## Linear recurrence for convolution powers of an INVERT sequence

Let $(c_m)_{m \ge 0}$ and
$(y_n)_{n \ge 0}$ be real sequences such that for every $n \ge 0$

$$y_n = \sum_{k=0}^{n} k! \sum_{j} \prod_{i=1}^{n+1} \frac{c_i^{j_i}}{j_i!},$$

where the inner sum runs over all tuples $(j_1, \dots, j_{n+1})$ of integers with
$0 \le j_i \le n$, $j_1 + j_2 + \dots + j_{n+1} = k$ and $j_1 + 2 j_2 + \dots + (n+1) j_{n+1} = n$.
Let $r \ge 1$ be an integer, and for $N \ge 0$ let $y^{(r)}_N$ be the sum of
$y_{a_1} y_{a_2} \cdots y_{a_r}$ over all tuples $(a_1, \dots, a_r)$ of nonnegative integers with
$a_1 + \dots + a_r = N$. Then for every $n \ge 1$

$$n \, y^{(r)}_n = \sum_{m=1}^{n} \bigl(n + m(r-1)\bigr) \, c_m \, y^{(r)}_{n-m}.$$

The hypothesis says that $y_n = \sum_{k=0}^{n} \frac{k!}{n!} B_{n,k}(1!\,c_1, 2!\,c_2, \dots)$
with the partial Bell polynomials $B_{n,k}$, that is, $y$ is the INVERT transform of $c$: as
formal power series in $z$, $\sum_{n \ge 0} y_n z^n = 1/(1 - \sum_{m \ge 1} c_m z^m)$. The value
$c_0$ plays no role.

## Sources

- Daniel Birmajer, Juan B. Gil, and Michael D. Weiner, "Linear Recurrence Sequences and Their Convolutions via Bell Polynomials," Journal of Integer Sequences 18 (2015), Article 15.1.2, Theorem, equation, lines 425–435, https://cs.uwaterloo.ca/journals/JIS/VOL18/Gil/gil3.tex

Formalized by `MetaMathlibExt.bell_convolution_linear_recurrence`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BellPolynomialConvolutionRecurrence.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/BellPolynomialConvolutionRecurrence.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/invert-transform/index.html#bell-convolution-linear-recurrence).

## Linear recurrence for INVERT convolution powers via partial Bell polynomials

Let $K$ be a
field of characteristic zero, let $(c_m)_{m \ge 0}$ and $(y_n)_{n \ge 0}$ be sequences in $K$, and
write $B_{n,k}$ for the partial Bell polynomial. Suppose that for every $n \ge 0$

$$y_n = \sum_{k=0}^{n} \frac{k!}{n!} \, B_{n,k}(x_1, x_2, \dots), \qquad x_m = m! \, c_m.$$

Let $r \ge 1$ be an integer, and for $N \ge 0$ let $y^{(r)}_N$ be the sum of
$y_{a_1} y_{a_2} \cdots y_{a_r}$ over all tuples $(a_1, \dots, a_r)$ of nonnegative integers with
$a_1 + \dots + a_r = N$. Then for every $n \ge 1$

$$n \, y^{(r)}_n = \sum_{m=1}^{n} \bigl(n + m(r-1)\bigr) \, c_m \, y^{(r)}_{n-m}.$$

Formalized by `MetaMathlibExt.bell_convolution_linear_recurrence_partialBellPolynomial`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BellPolynomialConvolutionRecurrence.lean, line 448](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/BellPolynomialConvolutionRecurrence.lean#L448). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/invert-transform/index.html#bell-convolution-linear-recurrence-parti).

## The INVERT transform of an integer sequence

The INVERT transform of an integer sequence
$a = (a_n)_{n \ge 0}$ is the integer sequence $b = (b_n)_{n \ge 0}$ in which $b_n$ is the
coefficient of $x^{n+1}$ in the inverse of $1 - \sum_{m \ge 0} a_m x^{m+1}$ in $\mathbb{Z}[[x]]$
(the inverse exists because the constant coefficient is $1$). In the one-based indexing of the
source, $a_n$ and $b_n$ are the terms of index $n + 1$.

Formalized by `MetaMathlibExt.invertTransform`, a definition declared in [MathlibExt/Combinatorics/Enumerative/InvertTransform.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/InvertTransform.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/invert-transform/index.html#invert-transform).

## Generating function of the INVERT transform

Let $a = (a_n)_{n \ge 0}$ be an integer
sequence and $b = (b_n)_{n \ge 0}$ its INVERT transform, and put
$A(x) = \sum_{n \ge 0} a_n x^{n+1}$ and $B(x) = \sum_{n \ge 0} b_n x^{n+1}$. Then
$(1 - A(x))(1 + B(x)) = 1$ in $\mathbb{Z}[[x]]$, that is, $1 + B(x)$ is the inverse of $1 - A(x)$.

Formalized by `MetaMathlibExt.invertTransform_spec`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/InvertTransform.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/InvertTransform.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/invert-transform/index.html#invert-transform-spec).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: INVERT transform](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/invert-transform/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/invert-transform)
