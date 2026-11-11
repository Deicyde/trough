---
declaration: section
origin: cited
lean: MetaMathlibExt.partitionPolynomial, MetaMathlibExt.coeff_partitionPolynomial, MetaMathlibExt.eval_partitionPolynomial_at_one, MetaMathlibExt.partitionPolynomial_iteratedDeriv_eq_sum_stirlingSecond_general, MetaMathlibExt.partitionPolynomial_iteratedDeriv_eq_sum_stirlingSecond
statement: formalized
proof: formalized
---

# Partition polynomials

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/partition-polynomials/index.html).

## Partition polynomial

For a partition $\lambda$ of a natural number $n$ with parts
$\lambda_1, \dots, \lambda_\ell$, listed with multiplicity, the (unnormalized) partition
polynomial of $\lambda$ is $f_\lambda(x) = x^{\lambda_1} + \dots + x^{\lambda_\ell}$, a polynomial
with natural number coefficients.

Formalized by `MetaMathlibExt.partitionPolynomial`, a definition declared in [MathlibExt/Combinatorics/Enumerative/Partition/PartitionPolynomial.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/PartitionPolynomial.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/partition-polynomials/index.html#partition-polynomial).

## Coefficients of the partition polynomial

For every partition $\lambda$ of a natural
number $n$ and every $j \in \mathbb{N}$, the coefficient of $x^j$ in the partition polynomial
$f_\lambda$ equals the number of parts of $\lambda$ equal to $j$.

Formalized by `MetaMathlibExt.coeff_partitionPolynomial`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/PartitionPolynomial.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/PartitionPolynomial.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/partition-polynomials/index.html#coeff-partition-polynomial).

## The partition polynomial at one

For every partition $\lambda$ of a natural number $n$,
the value $f_\lambda(1)$ of the partition polynomial $f_\lambda$ at $1$ equals the number of
parts of $\lambda$, counted with multiplicity.

Formalized by `MetaMathlibExt.eval_partitionPolynomial_at_one`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/PartitionPolynomial.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/PartitionPolynomial.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/partition-polynomials/index.html#eval-partition-polynomial-at-one).

## Stirling recursion for derivatives, for arbitrary multiplicities

Let $k$ and $d$ be
natural numbers, let $m \colon \mathbb{N} \to \mathbb{N}$, write $m_i = m(i)$, and let
$f(y) = \sum_{i=1}^{k} m_i y^i$ for real $y$. Then for every real $x \ne 0$,

$$f^{(d)}(x) = \sum_{i=1}^{k} i^d m_i x^{i-d} -
\sum_{j=0}^{d-1} S(d, j)\, x^{j-d} f^{(j)}(x),$$

where $S(d, j)$ are the Stirling numbers of the second kind and $f^{(j)}$ is the $j$th
derivative of $f$. No relation between $d$ and $k$ is assumed.

Formalized by `MetaMathlibExt.partitionPolynomial_iteratedDeriv_eq_sum_stirlingSecond_general`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/PartitionPolynomialDerivatives.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/PartitionPolynomialDerivatives.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/partition-polynomials/index.html#partition-polynomial-iterated-deriv-eq-s).

## Derivatives of the partition polynomial via Stirling numbers

Let $k \ge 1$, let
$m \colon \mathbb{N} \to \mathbb{N}$, and write $m_i = m(i)$. Assume $m_k \ne 0$ and $m_i = 0$
for every $i$ outside $\{1, \dots, k\}$, so that $m$ lists the part multiplicities of a
partition $\lambda = \langle 1^{m_1}, \dots, k^{m_k} \rangle$ with largest part $k$. Let
$f(y) = \sum_{i=1}^{k} m_i y^i$ for real $y$. Then for every natural number $d \le k$ and every
real $x \ne 0$,

$$f^{(d)}(x) = \sum_{i=1}^{k} i^d m_i x^{i-d} -
\sum_{j=0}^{d-1} S(d, j)\, x^{j-d} f^{(j)}(x),$$

where $S(d, j)$ are the Stirling numbers of the second kind and $f^{(j)}$ is the $j$th
derivative of $f$; for $d = 0$ the second sum is empty.

## Sources

- Madeline Locus Dawsey, Tyler Russell, and Dannie Urban, "Derivatives and Integrals of Polynomials Associated with Integer Partitions," Journal of Integer Sequences 25 (2022), Article 22.5.1, Theorem 1, lines 108–114, <https://cs.uwaterloo.ca/journals/JIS/VOL25/Dawsey/dawsey3.tex>.

Formalized by `MetaMathlibExt.partitionPolynomial_iteratedDeriv_eq_sum_stirlingSecond`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/PartitionPolynomialDerivatives.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/PartitionPolynomialDerivatives.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/partition-polynomials/index.html#partition-polynomial-iterated-deriv-eq-s-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partition polynomials](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/partition-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-partitions/counting-partitions/partition-polynomials)
