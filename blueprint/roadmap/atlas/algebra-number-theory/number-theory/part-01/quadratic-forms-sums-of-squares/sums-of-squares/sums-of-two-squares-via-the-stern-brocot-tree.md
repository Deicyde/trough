---
declaration: section
origin: cited
lean: MetaMathlibExt.continuedFraction_path_eq_convergents, MetaMathlibExt.exists_palindrome_continuedFraction_div, MetaMathlibExt.sq_add_sq_of_sternBrocot_path
statement: formalized
---

# Sums of two squares via the Stern–Brocot tree

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-two-squares-via-the-stern-brocot-tree/index.html).

## Continued fraction convergents as matrix paths

Let
$R = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and
$L = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$, as matrices over $\mathbb{N}$. Let
$q_0, q_1, q_2, \dots$ be natural numbers, and define natural numbers $A_k$, $B_k$ for $k \ge -1$
by $A_{-1} = 1$, $A_0 = q_0$, $B_{-1} = 0$, $B_0 = 1$ and, for $k \ge 1$,
$A_k = q_k A_{k-1} + A_{k-2}$ and $B_k = q_k B_{k-1} + B_{k-2}$. For $n \ge 0$ let
$W_n = M_0^{q_0} M_1^{q_1} \cdots M_n^{q_n}$, where $M_i = R$ for even $i$ and $M_i = L$ for odd
$i$. Then $W_n = \begin{pmatrix} A_{n-1} & A_n \\ B_{n-1} & B_n \end{pmatrix}$ when $n$ is even,
and $W_n = \begin{pmatrix} A_n & A_{n-1} \\ B_n & B_{n-1} \end{pmatrix}$ when $n$ is odd.

When every $q_i$ is positive, $A_k / B_k$ is the $k$-th convergent of $[q_0; q_1, q_2, \dots]$,
and the parity of $n$ says whether the path $W_n$ ends with an $R$-move or an $L$-move, which is
the paper's case split; the identity holds for all $q_i \ge 0$.

## Sources

- Hongshen Chua, *Binary Trees and Sum of Two Squares*, INTEGERS 26 (2026), Article A76, Theorem 1.

Stated but not proved: `MetaMathlibExt.continuedFraction_path_eq_convergents` is written with `theorem_wanted` in [WantedExt/NumberTheory/SternBrocotSumTwoSquaresWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SternBrocotSumTwoSquaresWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-two-squares-via-the-stern-brocot-tree/index.html#continued-fraction-path-eq-convergents).

## Perron's lemma

Let $p$ be a prime with $p \equiv 1 \pmod 4$, and let $x_0$ be an integer
with $0 < x_0 < p/2$ and $x_0^2 \equiv -1 \pmod p$. Then there are positive integers
$q_0, q_1, \dots, q_m$ with $m + 1$ even and $q_i = q_{m-i}$ for every $i$ such that
$p / x_0 = [q_0; q_1, \dots, q_m] = q_0 + 1/(q_1 + 1/(\cdots + 1/q_m))$.

Since $x_0 < p/2$ forces $q_0 \ge 2$, such an expansion is the canonical continued fraction of
$p / x_0$ (the other expansion ends in $1$): the continued fraction of $p / x_0$ has an even
number of terms and is palindromic.

## Sources

- Hongshen Chua, *Binary Trees and Sum of Two Squares*, INTEGERS 26 (2026), Article A76, Lemma 1 (Perron).

Stated but not proved: `MetaMathlibExt.exists_palindrome_continuedFraction_div` is written with `theorem_wanted` in [WantedExt/NumberTheory/SternBrocotSumTwoSquaresWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SternBrocotSumTwoSquaresWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-two-squares-via-the-stern-brocot-tree/index.html#exists-palindrome-continued-fraction-div).

## Sums of two squares from the Stern–Brocot tree

Let $p$ be a prime with
$p \equiv 1 \pmod 4$, and let $x_0$ be an integer with $0 < x_0 < p/2$ and
$x_0^2 \equiv -1 \pmod p$. Let $n \ge 0$ and let $q_0, q_1, \dots, q_n$ be positive integers with
$p / x_0 = [q_0; q_1, \dots, q_n, q_n, \dots, q_1, q_0]$, where
$[a_0; a_1, \dots, a_m] = a_0 + 1/(a_1 + 1/(\cdots + 1/a_m))$. With
$R = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and
$L = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$, let
$M = R^{q_0 - 1} M_1^{q_1} M_2^{q_2} \cdots M_n^{q_n}$, where $M_i = R$ for even $i$ and
$M_i = L$ for odd $i$. If $(x, y)^{\mathsf T} = M^{\mathsf T} (1, 1)^{\mathsf T}$, then
$p = x^2 + y^2$.

The fraction $x / y$ is the label of the path $M^{\mathsf T}$ in the Stern–Brocot tree.

## Sources

- Hongshen Chua, *Binary Trees and Sum of Two Squares*, INTEGERS 26 (2026), Article A76, Theorem 3.

Stated but not proved: `MetaMathlibExt.sq_add_sq_of_sternBrocot_path` is written with `theorem_wanted` in [WantedExt/NumberTheory/SternBrocotSumTwoSquaresWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SternBrocotSumTwoSquaresWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-two-squares-via-the-stern-brocot-tree/index.html#sq-add-sq-of-stern-brocot-path).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sums of two squares via the Stern–Brocot tree](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-two-squares-via-the-stern-brocot-tree/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-two-squares-via-the-stern-brocot-tree)
