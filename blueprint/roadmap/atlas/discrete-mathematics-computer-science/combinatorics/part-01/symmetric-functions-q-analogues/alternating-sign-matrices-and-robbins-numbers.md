---
declaration: section
origin: cited
lean: MetaMathlibExt.robbinsNumber, MetaMathlibExt.signedRobbinsNumber, MathlibExt.Combinatorics.AlternatingSignMatrixWanted.Combinatorics.AlternatingSignMatrix.rowPartialSum, MathlibExt.Combinatorics.AlternatingSignMatrixWanted.Combinatorics.AlternatingSignMatrix.colPartialSum, MathlibExt.Combinatorics.AlternatingSignMatrixWanted.Combinatorics.AlternatingSignMatrix.IsZeroOrOne, MathlibExt.Combinatorics.AlternatingSignMatrixWanted.Combinatorics.AlternatingSignMatrix.IsAlternatingSignMatrix, MathlibExt.Combinatorics.AlternatingSignMatrixWanted.Combinatorics.AlternatingSignMatrix.ASMatrix, MathlibExt.Combinatorics.AlternatingSignMatrixWanted.Combinatorics.AlternatingSignMatrix.robbinsProduct
statement: formalized
---

# Alternating sign matrices and Robbins numbers

9 results, 8 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/alternating-sign-matrices-and-robbins-numbers/index.html).

## Robbins numbers

For $n \in \mathbb{N}$, the Robbins number $A_n$ is the natural number
obtained by dividing $\prod_{k=0}^{n-1} (3k+1)!$ by $\prod_{k=0}^{n-1} (n+k)!$, where the division
is division of natural numbers rounded down.

## Sources

- Paul Barry, "From Fibonacci to Robbins: Series Reversion and Hankel Transforms," Journal of Integer Sequences 24 (2021).

Formalized by `MetaMathlibExt.robbinsNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/SignedRobbinsNumber.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/SignedRobbinsNumber.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/alternating-sign-matrices-and-robbins-numbers/index.html#robbins-number).

## Signed Robbins numbers

For $n \in \mathbb{N}$, the signed Robbins number is the integer
$(-1)^{\binom{n+1}{2}} A_{n+1}$, where $A_{n+1}$ is the Robbins number.

Formalized by `MetaMathlibExt.signedRobbinsNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/SignedRobbinsNumber.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/SignedRobbinsNumber.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/alternating-sign-matrices-and-robbins-numbers/index.html#signed-robbins-number).

## Row partial sums of a matrix

For an $n \times n$ integer matrix $A$ and indices
$i, k \in \{0, \dots, n-1\}$, the row partial sum of $A$ at $(i, k)$ is the sum of the entries of
row $i$ in columns $0$ through $k$, that is, $\sum_{j \le k} A_{ij}$.

Formalized by `MathlibExt.Combinatorics.AlternatingSignMatrixWanted.Combinatorics.AlternatingSignMatrix.rowPartialSum`, a definition declared in [WantedExt/Combinatorics/AlternatingSignMatrixWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AlternatingSignMatrixWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/alternating-sign-matrices-and-robbins-numbers/index.html#row-partial-sum).

## Column partial sums of a matrix

For an $n \times n$ integer matrix $A$ and indices
$j, k \in \{0, \dots, n-1\}$, the column partial sum of $A$ at $(j, k)$ is the sum of the entries
of column $j$ in rows $0$ through $k$, that is, $\sum_{i \le k} A_{ij}$.

Formalized by `MathlibExt.Combinatorics.AlternatingSignMatrixWanted.Combinatorics.AlternatingSignMatrix.colPartialSum`, a definition declared in [WantedExt/Combinatorics/AlternatingSignMatrixWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AlternatingSignMatrixWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/alternating-sign-matrices-and-robbins-numbers/index.html#col-partial-sum).

## Integers equal to zero or one

An integer $a$ is zero or one when $a = 0$ or $a = 1$. These
are the values allowed for the partial sums of an alternating sign matrix.

Formalized by `MathlibExt.Combinatorics.AlternatingSignMatrixWanted.Combinatorics.AlternatingSignMatrix.IsZeroOrOne`, a definition declared in [WantedExt/Combinatorics/AlternatingSignMatrixWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AlternatingSignMatrixWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/alternating-sign-matrices-and-robbins-numbers/index.html#is-zero-or-one).

## Alternating sign matrices

An $n \times n$ integer matrix $A$ is an alternating sign matrix
when every entry of $A$ is $-1$, $0$ or $1$; for all indices $i, k$ the row partial sum
$\sum_{j \le k} A_{ij}$ is $0$ or $1$; for all indices $j, k$ the column partial sum
$\sum_{i \le k} A_{ij}$ is $0$ or $1$; every row of $A$ sums to $1$; and every column of $A$
sums to $1$.

Formalized by `MathlibExt.Combinatorics.AlternatingSignMatrixWanted.Combinatorics.AlternatingSignMatrix.IsAlternatingSignMatrix`, a definition declared in [WantedExt/Combinatorics/AlternatingSignMatrixWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AlternatingSignMatrixWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/alternating-sign-matrices-and-robbins-numbers/index.html#is-alternating-sign-matrix).

## Alternating sign matrices of size $n$

For a natural number $n$, this is the collection of
all $n \times n$ integer matrices that are alternating sign matrices.

Formalized by `MathlibExt.Combinatorics.AlternatingSignMatrixWanted.Combinatorics.AlternatingSignMatrix.ASMatrix`, an abbreviation declared in [WantedExt/Combinatorics/AlternatingSignMatrixWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AlternatingSignMatrixWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/alternating-sign-matrices-and-robbins-numbers/index.html#asmatrix).

## The Robbins product

For a natural number $n$, the Robbins product is the rational number

$$\prod_{k=0}^{n-1} \frac{(3k+1)!}{(n+k)!},$$

an empty product, equal to $1$, when $n = 0$.

Formalized by `MathlibExt.Combinatorics.AlternatingSignMatrixWanted.Combinatorics.AlternatingSignMatrix.robbinsProduct`, a definition declared in [WantedExt/Combinatorics/AlternatingSignMatrixWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AlternatingSignMatrixWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/alternating-sign-matrices-and-robbins-numbers/index.html#robbins-product).

## Alternating sign matrix theorem

For every natural number $n$, the number of
$n \times n$ alternating sign matrices equals the Robbins product
$\prod_{k=0}^{n-1} \frac{(3k+1)!}{(n+k)!}$.

## Sources

- D. Zeilberger (1996); G. Kuperberg (1996). Knill, §168. Problem `alternating_sign_matrix_count` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.AlternatingSignMatrixWanted.Combinatorics.AlternatingSignMatrix.alternating_sign_matrix_count` is written with `theorem_wanted` in [WantedExt/Combinatorics/AlternatingSignMatrixWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/AlternatingSignMatrixWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/alternating-sign-matrices-and-robbins-numbers/index.html#alternating-sign-matrix-count).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Alternating sign matrices and Robbins numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/alternating-sign-matrices-and-robbins-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/symmetric-functions-q-analogues/alternating-sign-matrices-and-robbins-numbers)
