---
declaration: section
origin: cited
lean: MetaMathlibExt.product_add_add_eq_univ_of_card_mul_gt, MetaMathlibExt.diagonal_congruence_solvable_of_card_eq_exponent, MetaMathlibExt.smooth_diagonal_solution_count_asymp, MetaMathlibExt.card_smooth_diagonal_values_ge, MetaMathlibExt.exists_small_solution_diagonal_congruence
statement: formalized
---

# Small solutions of diagonal congruences

5 results, 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/small-solutions-of-diagonal-congruences/index.html).

## Sum-product sets cover the integers modulo a prime

Let $p$ be a prime and let
$A_1, A_2, A_3, D$ be subsets of $\mathbb{Z}/p\mathbb{Z}$ with $|A_1| |A_2| |A_3| |D| > p^3$.
Then every residue class modulo $p$ can be written as $a_1 d + a_2 + a_3$ with $a_1 \in A_1$,
$d \in D$, $a_2 \in A_2$ and $a_3 \in A_3$; that is, $A_1 D + A_2 + A_3 = \mathbb{Z}/p\mathbb{Z}$.

## Sources

- Todd Cochrane, Misty Ostergaard, Craig Spencer, and Kathryn Wilson, *A Note on Small Solutions to Diagonal Congruences*, INTEGERS 26 (2026), Article A14, Lemma 3, quoting Lemma 8.3 of their reference [5] (a consequence of Sárközy's Corollary A).

Stated but not proved: `MetaMathlibExt.product_add_add_eq_univ_of_card_mul_gt` is written with `theorem_wanted` in [WantedExt/NumberTheory/DiagonalCongruenceSmallSolutionsWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DiagonalCongruenceSmallSolutionsWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/small-solutions-of-diagonal-congruences/index.html#product-add-add-eq-univ-of-card-mul-gt).

## Diagonal congruences in $k$ variables are solvable

Let $p$ be a prime and $k \ge 1$. For
all integers $a_1, \dots, a_k$ not divisible by $p$ and every integer $c$, there are integers
$x_1, \dots, x_k$ with $a_1 x_1^k + \dots + a_k x_k^k \equiv c \pmod p$.

Equivalently, $\Gamma(k, p) \le k$, where $\Gamma(k, p)$ is the least $n$ such that every such
congruence in $n$ variables is solvable; extra variables can be set to $0$.

## Sources

- Todd Cochrane, Misty Ostergaard, Craig Spencer, and Kathryn Wilson, *A Note on Small Solutions to Diagonal Congruences*, INTEGERS 26 (2026), Article A14, Lemma 2.

Stated but not proved: `MetaMathlibExt.diagonal_congruence_solvable_of_card_eq_exponent` is written with `theorem_wanted` in [WantedExt/NumberTheory/DiagonalCongruenceSmallSolutionsWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DiagonalCongruenceSmallSolutionsWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/small-solutions-of-diagonal-congruences/index.html#diagonal-congruence-solvable-of-card-eq).

## Smooth solutions of diagonal equations (Chow–Lindqvist–Prendiville)

For a natural number
$N$ and real $\eta > 0$, let $A(N, N^\eta)$ be the set of integers $1 \le x \le N$ all of whose
prime factors are at most $N^\eta$. There is a real-valued function $g$ on the natural numbers
with $g(k) = O(\log \log k / \log k)$ as $k \to \infty$ such that for every $k \ge 2$ there is
$\eta_0 > 0$ with the following property. Let $c_1, \dots, c_s$ be nonzero integers such that
$\sum_{i \in I} c_i = 0$ for some nonempty $I \subseteq \{1, \dots, s\}$, and suppose $s \ge 5$
if $k = 2$, $s \ge 8$ if $k = 3$, and $s \ge k (\log k + \log \log k + 2 + g(k))$ if $k \ge 4$.
Then for every $0 < \eta \le \eta_0$ there are a natural number $N_0$ and constants
$C_1, C_2 > 0$ such that for all $N \ge N_0$ the number of $x \in A(N, N^\eta)^s$ with
$c_1 x_1^k + \dots + c_s x_s^k = 0$ is at least $C_1 N^{s-k}$ and at most $C_2 N^{s-k}$.

## Sources

- Todd Cochrane, Misty Ostergaard, Craig Spencer, and Kathryn Wilson, *A Note on Small Solutions to Diagonal Congruences*, INTEGERS 26 (2026), Article A14, Theorem 2, quoting Chow, Lindqvist and Prendiville, *Rado's criterion over squares and higher powers*, J. Eur. Math. Soc. 23 (2021), Theorem B.1.

Stated but not proved: `MetaMathlibExt.smooth_diagonal_solution_count_asymp` is written with `theorem_wanted` in [WantedExt/NumberTheory/DiagonalCongruenceSmallSolutionsWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DiagonalCongruenceSmallSolutionsWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/small-solutions-of-diagonal-congruences/index.html#smooth-diagonal-solution-count-asymp).

## Many values of a smooth diagonal form modulo a prime

For a natural number $B$ and real
$\eta > 0$, let $A(B, B^\eta)$ be the set of integers $1 \le x \le B$ all of whose prime factors
are at most $B^\eta$. There is a real-valued function $g$ on the natural numbers with
$g(k) = O(\log \log k / \log k)$ as $k \to \infty$ such that for every $k \ge 2$ there is
$\eta_0 > 0$ with the following property. Let $0 < \eta \le \eta_0$ and let $n \ge 1$ satisfy
$2n \ge 5$ if $k = 2$, $2n \ge 8$ if $k = 3$, and $2n \ge k (\log k + \log \log k + 2 + g(k))$
if $k \ge 4$. Then there is $C > 0$ such that for every prime $p$, every natural number $B \ge 1$
with $n B^k \le p$ and all integers $a_1, \dots, a_n$ not divisible by $p$, the set of residues
modulo $p$ of $a_1 x_1^k + \dots + a_n x_n^k$ with $x \in A(B, B^\eta)^n$ has at least $C B^k$
elements.

## Sources

- Todd Cochrane, Misty Ostergaard, Craig Spencer, and Kathryn Wilson, *A Note on Small Solutions to Diagonal Congruences*, INTEGERS 26 (2026), Article A14, Lemma 1.

Stated but not proved: `MetaMathlibExt.card_smooth_diagonal_values_ge` is written with `theorem_wanted` in [WantedExt/NumberTheory/DiagonalCongruenceSmallSolutionsWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DiagonalCongruenceSmallSolutionsWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/small-solutions-of-diagonal-congruences/index.html#card-smooth-diagonal-values-ge).

## Small solutions of diagonal congruences

There is a real-valued function $g$ on the natural
numbers with $g(k) = O(\log \log k / \log k)$ as $k \to \infty$ such that for every $k \ge 2$
there is a constant $C > 0$ with the following property. Let $n$ satisfy $n \ge 9$ if $k = 2$,
$n \ge 12$ if $k = 3$, and $n \ge \frac{3}{2} k (\log k + \log \log k + 2 + g(k))$ if $k \ge 4$.
Then for every prime $p$, every integer $c$ and all integers $a_1, \dots, a_n$ not divisible by
$p$, the congruence $a_1 x_1^k + \dots + a_n x_n^k \equiv c \pmod p$ has a solution in natural
numbers $x_1, \dots, x_n$ with $1 \le x_i \le C p^{1/k}$ for every $i$.

## Sources

- Todd Cochrane, Misty Ostergaard, Craig Spencer, and Kathryn Wilson, *A Note on Small Solutions to Diagonal Congruences*, INTEGERS 26 (2026), Article A14, Theorem 1.

Stated but not proved: `MetaMathlibExt.exists_small_solution_diagonal_congruence` is written with `theorem_wanted` in [WantedExt/NumberTheory/DiagonalCongruenceSmallSolutionsWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DiagonalCongruenceSmallSolutionsWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/small-solutions-of-diagonal-congruences/index.html#exists-small-solution-diagonal-congruenc).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Small solutions of diagonal congruences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/small-solutions-of-diagonal-congruences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/small-solutions-of-diagonal-congruences)
