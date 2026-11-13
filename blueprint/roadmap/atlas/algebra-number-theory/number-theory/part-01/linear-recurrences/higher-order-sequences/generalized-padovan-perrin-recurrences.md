---
declaration: section
origin: cited
lean: MetaMathlibExt.padovanPerrin_charPoly_separable, MetaMathlibExt.padovanPerrinRecurrence, MetaMathlibExt.padovanPerrinRecurrence_isSolution_iff, MetaMathlibExt.padovanPerrinFundamental, MetaMathlibExt.padovanPerrinFundamental_of_lt, MetaMathlibExt.padovanPerrinFundamental_isSolution, MetaMathlibExt.padovanPerrinRho, MetaMathlibExt.padovanPerrinRho_of_lt
statement: formalized
---

# Generalized Padovan–Perrin recurrences

26 results, 10 proved and 16 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html).

## Simple roots of the Padovan–Perrin characteristic polynomial

Let $k_1, k_2, p, s$ be
natural numbers with $k_1 > 0$, $p \ge 2$, $p < s$ and $k_1^2 < k_2$. Then the characteristic
polynomial $P(z) = z^{s+p} - k_1 z^p - k_2$ of the $([k]; p; s)$-generalized Padovan–Perrin
recurrence is separable over $\mathbb{C}$, that is, it has only simple roots.

The hypotheses force $k_2 > 0$ and $s > 0$.

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, Lemma 4.

Stated but not proved: `MetaMathlibExt.padovanPerrin_charPoly_separable` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-char-poly-separable).

## Generalized Padovan–Perrin recurrence

Let $R$ be a commutative semiring, $k_1, k_2 \in R$
and $p, s \in \mathbb{N}$. The $([k]; p; s)$-generalized Padovan–Perrin recurrence is the linear
recurrence of order $s + p$ with coefficients $c_i = [i = 0] \, k_2 + [i = p] \, k_1$ for
$0 \le i < s + p$, where $[\cdot]$ is $1$ if the condition holds and $0$ otherwise: a sequence
$v \colon \mathbb{N} \to R$ solves it when $v_{n+s+p} = \sum_{i=0}^{s+p-1} c_i v_{n+i}$ for every
$n \ge 0$. For $s > 0$ this reads $v_{n+s+p} = k_1 v_{n+p} + k_2 v_n$, that is,
$v_n = k_1 v_{n-s} + k_2 v_{n-s-p}$ for $n \ge s + p$ (equation (1)).

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, equation (1).

Formalized by `MetaMathlibExt.padovanPerrinRecurrence`, a definition declared in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-recurrence).

## Characterization of solutions of the generalized Padovan–Perrin recurrence

Let $R$ be a
commutative semiring, $k_1, k_2 \in R$, and $p, s \in \mathbb{N}$ with $s > 0$. A sequence
$v \colon \mathbb{N} \to R$ is a solution of the $([k]; p; s)$-Padovan–Perrin recurrence if and
only if $v_{n+s+p} = k_1 v_{n+p} + k_2 v_n$ for every $n \ge 0$.

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, equation (1).

Formalized by `MetaMathlibExt.padovanPerrinRecurrence_isSolution_iff`, a theorem declared in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-recurrence-is-solution-if).

## Fibonacci fundamental system of the generalized Padovan–Perrin recurrence

Let $R$ be a
commutative semiring, $k_1, k_2 \in R$ and $p, s \in \mathbb{N}$. For a natural number $j$, the
$j$-th fundamental sequence $v^{(j)} \colon \mathbb{N} \to R$ is the solution of the
$([k]; p; s)$-Padovan–Perrin recurrence with initial values $v^{(j)}_n = 1$ if $n + 1 = j$ and
$v^{(j)}_n = 0$ otherwise, for $0 \le n < s + p$.

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, equation (2) and Definition 1.

Formalized by `MetaMathlibExt.padovanPerrinFundamental`, a definition declared in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-fundamental).

## Initial values of the generalized Padovan–Perrin fundamental system

Let $R$ be a
commutative semiring, $k_1, k_2 \in R$ and $p, s, j \in \mathbb{N}$. For every $n < s + p$, the
$j$-th sequence $v^{(j)}$ of the Fibonacci fundamental system satisfies $v^{(j)}_n = 1$ if
$n + 1 = j$ and $v^{(j)}_n = 0$ otherwise.

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, equation (2).

Formalized by `MetaMathlibExt.padovanPerrinFundamental_of_lt`, a theorem declared in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-fundamental-of-lt).

## The generalized Padovan–Perrin fundamental sequences solve the recurrence

Let $R$ be a
commutative semiring, $k_1, k_2 \in R$ and $p, s \in \mathbb{N}$. For every natural number $j$,
the $j$-th sequence $v^{(j)}$ of the Fibonacci fundamental system is a solution of the
$([k]; p; s)$-Padovan–Perrin recurrence.

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, equation (2).

Formalized by `MetaMathlibExt.padovanPerrinFundamental_isSolution`, a theorem declared in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-fundamental-is-solution).

## Padovan–Perrin coefficients

Let $R$ be a commutative semiring, let $k_1, k_2 \in R$ and
let $p, s, n$ be natural numbers. The coefficient $\rho(n, s + p)$ attached to $k_1, k_2, p, s$ is
$0$ when $n < s + p$; when $n \ge s + p$ it is the sum of $\binom{a + b}{a} k_1^a k_2^b$ over all
pairs of natural numbers $a, b \le n$ with $s a + (s + p) b = n - (s + p)$. For $s > 0$ the bounds
$a, b \le n$ hold automatically.

For $s > 0$ this is the coefficient $\rho(n, r)$, $r = s + p$, of the paper's general formula (12)
for the recurrence $v_n = k_1 v_{n-s} + k_2 v_{n-s-p}$. The paper's Proposition 4 prints the
constraint as $s a + (s + p) b = n - (s + p - 1)$, which contradicts its own normalization
$\rho(s + p, s + p) = 1$ for $s \ge 2$; the constraint used here is the one of formula (12).

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, equation (12) and Proposition 4.

Formalized by `MetaMathlibExt.padovanPerrinRho`, a definition declared in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-rho).

## The Padovan–Perrin coefficients vanish below the order

Let $R$ be a commutative
semiring, let $k_1, k_2 \in R$ and let $p, s, n$ be natural numbers with $n < s + p$. Then the
Padovan–Perrin coefficient $\rho(n, s + p)$ attached to $k_1, k_2, p, s$ equals $0$.

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, Proposition 4.

Formalized by `MetaMathlibExt.padovanPerrinRho_of_lt`, a theorem declared in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-rho-of-lt).

## Normalization of the Padovan–Perrin coefficients

Let $R$ be a commutative semiring, let
$k_1, k_2 \in R$ and let $p, s$ be natural numbers with $s > 0$. Then the Padovan–Perrin
coefficient $\rho(s + p, s + p)$ attached to $k_1, k_2, p, s$ equals $1$.

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, Proposition 4.

Formalized by `MetaMathlibExt.padovanPerrinRho_self`, a theorem declared in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-rho-self).

## Recurrence for the generalized Padovan–Perrin coefficients ρ

Let $R$ be a commutative
semiring, $k_1, k_2 \in R$, and $p, s \in \mathbb{N}$ with $s > 0$, and write $\rho(m, s+p)$ for
the Padovan–Perrin coefficient. For every $n \ge 0$,

$$\rho(n + s + p + 1, s + p) = k_1 \, \rho(n + p + 1, s + p) + k_2 \, \rho(n + 1, s + p),$$

that is, $\rho(m, s+p) = k_1 \rho(m - s, s+p) + k_2 \rho(m - s - p, s+p)$ for every $m > s + p$.

Together with $\rho(m, s+p) = 0$ for $m < s + p$ and $\rho(s+p, s+p) = 1$, this determines $\rho$.

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, equation (12) and Proposition 4.

Formalized by `MetaMathlibExt.padovanPerrinRho_add_succ`, a theorem declared in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-rho-add-succ).

## The Padovan–Perrin coefficient $\rho(12, 3)$ equals $5$

Over the integers, with
$k_1 = k_2 = 1$, $p = 1$ and $s = 2$ (the Padovan–Perrin recurrence $v_n = v_{n-2} + v_{n-3}$),
the coefficient $\rho(12, 3)$ equals $5$.

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, equation (14) and Table 1.

Formalized by `MetaMathlibExt.padovanPerrinRho_one_one_one_two_twelve`, a theorem declared in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-rho-one-one-one-two-twelv).

## Expansion in the Fibonacci fundamental system

Let $R$ be a commutative ring, let
$k_1, k_2 \in R$ and $p, s \in \mathbb{N}$, and for $1 \le j \le s + p$ let $v^{(j)}$ be the
solution of the $([k]; p; s)$-Padovan–Perrin recurrence with $v^{(j)}(m) = 1$ if $m + 1 = j$ and
$v^{(j)}(m) = 0$ otherwise, for $0 \le m < s + p$. Then every solution $v \colon \mathbb{N} \to R$
of the recurrence satisfies, for every $n \ge 0$,

$$v(n) = \sum_{j=0}^{s+p-1} v(j)\, v^{(j+1)}(n).$$

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, Proposition 1.

Stated but not proved: `MetaMathlibExt.padovanPerrin_eq_sum_fundamental` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-eq-sum-fundamental).

## Solutions agreeing on a window agree afterwards

Let $R$ be a commutative ring, let
$k_1, k_2 \in R$, let $p, s$ be natural numbers and let $v, w \colon \mathbb{N} \to R$ be solutions
of the Padovan–Perrin recurrence with parameters $k_1, k_2, p, s$. Let $n_0, m_0, N$ be natural
numbers such that $v(j + n_0) = w(j + m_0)$ for every $j$ with $N \le j < N + s + p$. Then
$v(n + n_0) = w(n + m_0)$ for every $n \ge N$.

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, Lemma 1.

Stated but not proved: `MetaMathlibExt.padovanPerrin_shift_eq_of_window` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-shift-eq-of-window).

## The Fibonacci fundamental system spans the solutions

Let $R$ be a commutative ring, let
$k_1, k_2 \in R$ and let $p, s$ be natural numbers. For $1 \le j \le s + p$ let $v^{(j)}$ be the
solution of the Padovan–Perrin recurrence with parameters $k_1, k_2, p, s$ whose initial values
are $v^{(j)}(n) = 1$ if $n + 1 = j$ and $v^{(j)}(n) = 0$ otherwise, for $n < s + p$. Then the
submodule of $R^{\mathbb{N}}$ formed by all solutions of this recurrence is the submodule spanned
by $v^{(1)}, \dots, v^{(s+p)}$.

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, Corollary 1.

Stated but not proved: `MetaMathlibExt.padovanPerrin_solSpace_eq_span_fundamental` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-sol-space-eq-span-fundame).

## Shift property of the generalized Padovan–Perrin fundamental system

Let $R$ be a
commutative ring, $k_1, k_2 \in R$, and let $p, s, j$ be natural numbers with $p \ge 1$ and
$p + 1 \le j \le s + p - 1$. Write $v^{(\ell)}$ for the $\ell$-th sequence of the Fibonacci
fundamental system of the $([k]; p; s)$-Padovan–Perrin recurrence. Then
$v^{(j)}_n = v^{(s+p)}_{n+s+p-j}$ for every $n \ge 0$, and
$v^{(j)}_n = k_1 v^{(s+p)}_{n-j+p} + k_2 v^{(s+p)}_{n-j}$ for every $n \ge j$.

The paper's second clause, $v^{(j)}_n = k_2 v^{(s+p)}_{n+j}$ for $1 \le j \le p$, is omitted: it
fails for $k_1 = k_2 = 1$, $p = 1$, $s = 2$, $j = 1$, $n = 0$, where $v^{(1)}_0 = 1$ but
$v^{(3)}_1 = 0$.

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, Proposition 2.

Stated but not proved: `MetaMathlibExt.padovanPerrinFundamental_eq_shift` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-fundamental-eq-shift).

## Powers of the Padovan–Perrin companion matrix

Let $R$ be a commutative ring, let
$k_1, k_2 \in R$, let $p, s$ be positive integers, and write $r = s + p$. Let $A$ be the
$r \times r$ matrix over $R$, with rows and columns indexed by $0, \dots, r - 1$, whose row $0$ has
$k_1$ in column $s - 1$, $k_2$ in column $r - 1$ and $0$ elsewhere, and whose entry in row
$a \ge 1$ and column $b$ is $1$ if $a = b + 1$ and $0$ otherwise. For $1 \le \ell \le r$ let
$v^{(\ell)}$ be the solution of the $([k]; p; s)$-Padovan–Perrin recurrence with
$v^{(\ell)}(m) = 1$ if $m + 1 = \ell$ and $v^{(\ell)}(m) = 0$ otherwise, for $0 \le m < r$. Then
for every $n \ge 0$ and all $0 \le i, j \le r - 1$,

$$(A^n)_{ij} = v^{(r - j)}(n + r - 1 - i).$$

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, Theorem 1, equations (5) and (9).

Stated but not proved: `MetaMathlibExt.padovanPerrin_companion_pow_apply` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-companion-pow-apply).

## Product identity for the generalized Padovan–Perrin fundamental system

Let $R$ be a
commutative ring, $k_1, k_2 \in R$, and $p, s \ge 1$. Write $r = s + p$ and $v^{(\ell)}$ for the
$\ell$-th sequence of the Fibonacci fundamental system of the $([k]; p; s)$-Padovan–Perrin
recurrence. Then for all $m, n \ge 0$ and all $1 \le i, j \le r$,

$$v^{(r-j+1)}_{n+m+r-i} = \sum_{k=1}^{r} v^{(r-k+1)}_{m+r-i} \, v^{(r-j+1)}_{n+r-k}.$$

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, Proposition 3, equation (10).

Stated but not proved: `MetaMathlibExt.padovanPerrinFundamental_mul_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-fundamental-mul-sum).

## Combinatorial expression of the Padovan–Perrin sequences

Let $R$ be a commutative ring,
let $k_1, k_2 \in R$, let $p, s$ be positive integers, and let $v \colon \mathbb{N} \to R$ satisfy
$v(n + s + p) = k_1 v(n + p) + k_2 v(n)$ for every $n$. For $0 \le m \le s + p - 1$ put
$A_m = k_2 v(m) + k_1 v(m + p)$ if $m < s$ and $A_m = k_2 v(m)$ if $m \ge s$. Let $\rho(N, s + p)$
be the Padovan–Perrin coefficient: $0$ for $N < s + p$, and for $N \ge s + p$ the sum of
$\binom{a+b}{a} k_1^a k_2^b$ over all $a, b \ge 0$ with $s a + (s + p) b = N - (s + p)$. Then for
every $n \ge s + p$,

$$v(n) = \sum_{m=0}^{s+p-1} \rho(n - m, s + p)\, A_m.$$

The paper prints the constraint in $\rho$ as $s a + (s + p) b = N - (s + p - 1)$, and with it the
identity fails (for $k_1 = k_2 = 1$, $p = 1$, $s = 2$ the printed $\rho(4, 3)$ is $1$ instead of
$0$); the constraint used here is the one of the paper's general formula (12).

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, Theorem 3.

Stated but not proved: `MetaMathlibExt.padovanPerrin_eq_sum_rho` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-eq-sum-rho).

## The last generalized Padovan–Perrin fundamental sequence is a shifted ρ

Let $R$ be a
commutative ring, $k_1, k_2 \in R$, and $p, s \ge 1$. Write $v^{(s+p)}$ for the $(s+p)$-th
sequence of the Fibonacci fundamental system of the $([k]; p; s)$-Padovan–Perrin recurrence and
$\rho(m, s+p)$ for the Padovan–Perrin coefficient. Then $v^{(s+p)}_n = \rho(n + 1, s + p)$ for
every $n \ge s + p$.

Here $\rho(m, s+p)$ sums over $a, b \ge 0$ with $sa + (s+p)b = m - (s+p)$, the constraint of
formula (12). With the printed constraint $m - (s + p - 1)$ the identity fails, e.g. for
$k_1 = k_2 = 1$, $p = 1$, $s = 2$, $n = 3$, where $v^{(3)}_3 = 0$ but the printed
$\rho(4, 3)$ is $1$.

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, Proposition 4.

Stated but not proved: `MetaMathlibExt.padovanPerrinFundamental_last_eq_rho` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 414](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L414). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-fundamental-last-eq-rho).

## Fundamental Padovan–Perrin solutions as shifted coefficients $\rho$

Let $R$ be a
commutative ring, let $k_1, k_2 \in R$, let $p \ge 1$ and $s$ be natural numbers, and let $j$
satisfy $p + 1 \le j \le s + p - 1$. For $1 \le \ell \le s + p$ let $v^{(\ell)}$ be the solution of
the $([k]; p; s)$-Padovan–Perrin recurrence with $v^{(\ell)}(m) = 1$ if $m + 1 = \ell$ and
$v^{(\ell)}(m) = 0$ otherwise, for $0 \le m < s + p$. Let $\rho(N, s + p)$ be the Padovan–Perrin
coefficient: $0$ for $N < s + p$, and for $N \ge s + p$ the sum of $\binom{a+b}{a} k_1^a k_2^b$
over all $a, b \ge 0$ with $s a + (s + p) b = N - (s + p)$. Then for every $n \ge 0$,

$$v^{(j)}(n) = v^{(s+p)}(n + s + p - j) = \rho(n + s + p - j + 1, s + p).$$

The paper's second clause $v^{(j)}(n) = k_2\,\rho(n + j + 1, s + p)$ for $1 \le j \le p$ is
omitted: it fails for $k_1 = 1$, $k_2 = 2$, $p = 1$, $s = 2$, $j = 1$, $n = 0$, where
$v^{(1)}(0) = 1$ but $2\rho(2, 3) = 0$.

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, Proposition 5.

Stated but not proved: `MetaMathlibExt.padovanPerrinFundamental_eq_rho` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 427](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L427). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-fundamental-eq-rho).

## Simple roots of the Padovan–Perrin polynomial for $p = 1$

Let $k_1, k_2, s$ be positive
integers with $\left(-\frac{k_2 (s + 1)}{k_1 s}\right)^s \neq \frac{k_1}{s + 1}$. Then the
polynomial $P(z) = z^{s+1} - k_1 z - k_2$ is separable over $\mathbb{C}$, that is, it has only
simple roots.

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, Lemma 2.

Stated but not proved: `MetaMathlibExt.padovanPerrin_charPoly_separable_of_p_eq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-char-poly-separable-of-p).

## Root formula for the generalized Padovan–Perrin coefficients ρ

Let $k_1, k_2$ be complex
numbers with $k_2 \neq 0$, let $p, s \ge 1$, and let $P(z) = z^{s+p} - k_1 z^p - k_2$. If $P$ is
separable, that is, has $s + p$ distinct roots $\lambda_1, \dots, \lambda_{s+p}$ in $\mathbb{C}$,
then for every $n \ge s + p$ the Padovan–Perrin coefficient satisfies

$$\rho(n, s + p) = \sum_{i=1}^{s+p} \frac{\lambda_i^{n-1}}{P'(\lambda_i)}.$$

The paper states this for the general $\rho$ of formula (12) attached to an arbitrary
characteristic polynomial $z^r - a_0 z^{r-1} - \cdots - a_{r-1}$; this is its specialization to
the $([k]; p; s)$-Padovan–Perrin coefficients, the case the paper applies.

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, Lemma 5.

Stated but not proved: `MetaMathlibExt.padovanPerrinRho_eq_sum_roots` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-rho-eq-sum-roots).

## Analytic expression of the Padovan–Perrin sequences

Let $k_1, k_2, p, s$ be natural
numbers with $k_1 > 0$, $p \ge 2$, $p < s$ and $k_1^2 < k_2$, let
$P(z) = z^{s+p} - k_1 z^p - k_2$, and let $v \colon \mathbb{N} \to \mathbb{C}$ satisfy
$v(n + s + p) = k_1 v(n + p) + k_2 v(n)$ for every $n$. For $0 \le m \le s + p - 1$ put
$A_m = k_2 v(m) + k_1 v(m + p)$ if $m < s$ and $A_m = k_2 v(m)$ if $m \ge s$. Then for every
$n \ge s + p$,

$$v(n) = \sum_{m=0}^{s+p-1} A_m \sum_{\lambda} \frac{\lambda^{n-1-m}}{P'(\lambda)},$$

where $\lambda$ runs over the complex roots of $P$ counted with multiplicity.

The paper assumes that the roots of $P$ are distinct; this follows from the other hypotheses
(Lemma 4 of the paper).

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, Proposition 6.

Stated but not proved: `MetaMathlibExt.padovanPerrin_eq_sum_roots` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#padovan-perrin-eq-sum-roots).

## Combinatorial formula for the $k$-Padovan–Perrin numbers

Let $R$ be a commutative ring,
let $k \in R$, and let $v \colon \mathbb{N} \to R$ satisfy $v(n + 3) = v(n + 1) + k\,v(n)$ for
every $n$, that is, $v$ solves the Padovan–Perrin recurrence with $k_1 = 1$, $k_2 = k$, $p = 1$,
$s = 2$. Let $\rho(m) = \rho(m, 3)$ be the Padovan–Perrin coefficient for these parameters:
$\rho(m) = 0$ for $m < 3$, and for $m \ge 3$ it is the sum of $\binom{a+b}{a} k^b$ over all
$a, b \ge 0$ with $2a + 3b = m - 3$. Then for every $n \ge 3$,

$$v(n) = \rho(n)\,(k\,v(0) + v(1)) + (k\,v(1) + v(2))\,\rho(n - 1) + k\,v(2)\,\rho(n - 2).$$

The paper prints the middle coefficient as $k\,v(1)$; the coefficient $k\,v(1) + v(2)$ is the one
its Theorem 3 gives, and the printed form fails for $k = 2$, $(v(0), v(1), v(2)) = (0, 0, 1)$,
$n = 4$, where $v(4) = 1$ but the printed right side is $0$. The paper takes $k \ge 2$ an integer.

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, Proposition 8.

Stated but not proved: `MetaMathlibExt.kPadovanPerrin_eq_sum_rho` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 494](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L494). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#k-padovan-perrin-eq-sum-rho).

## Fundamental $k$-Padovan–Perrin solutions as coefficients $\rho$

Let $R$ be a commutative
ring and $k \in R$, and take the Padovan–Perrin recurrence with $k_1 = 1$, $k_2 = k$, $p = 1$,
$s = 2$, that is, $v(n + 3) = v(n + 1) + k\,v(n)$. Let $v^{(2)}$ and $v^{(3)}$ be its solutions
with initial values $(v^{(2)}(0), v^{(2)}(1), v^{(2)}(2)) = (0, 1, 0)$ and
$(v^{(3)}(0), v^{(3)}(1), v^{(3)}(2)) = (0, 0, 1)$. Let $\rho(m) = \rho(m, 3)$ be the
Padovan–Perrin coefficient for these parameters: $\rho(m) = 0$ for $m < 3$, and for $m \ge 3$ it
is the sum of $\binom{a+b}{a} k^b$ over all $a, b \ge 0$ with $2a + 3b = m - 3$. Then for every
$n \ge 0$, $v^{(3)}(n) = \rho(n + 1)$ and $v^{(2)}(n) = \rho(n + 2)$.

The paper's third formula $v^{(1)}(n) = k\,\rho(n + 2)$, for the solution $v^{(1)}$ with initial
values $(1, 0, 0)$, is omitted: it fails for $k = 2$, $n = 0$ ($v^{(1)}(0) = 1$, $2\rho(2) = 0$).
The paper takes $k \ge 2$ an integer.

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, Proposition 9.

Stated but not proved: `MetaMathlibExt.kPadovanPerrinFundamental_eq_rho` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 508](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#k-padovan-perrin-fundamental-eq-rho).

## Root formula for the $k$-Padovan–Perrin numbers

Let $k \ge 2$ be an integer, let
$P(z) = z^3 - z - k$, and let $v \colon \mathbb{N} \to \mathbb{C}$ satisfy
$v(n + 3) = v(n + 1) + k\,v(n)$ for every $n$, that is, $v$ solves the Padovan–Perrin recurrence
with $k_1 = 1$, $k_2 = k$, $p = 1$, $s = 2$. Put $A_0 = k\,v(0) + v(1)$, $A_1 = k\,v(1) + v(2)$
and $A_2 = k\,v(2)$. Then for every $n \ge 3$,

$$v(n) = \sum_\lambda \frac{A_0\lambda^{n-1} + A_1\lambda^{n-2} + A_2\lambda^{n-3}}{P'(\lambda)},$$

where $\lambda$ runs over the complex roots of $P$ counted with multiplicity.

Since $27 k^2 - 4 \neq 0$, the roots of $P$ are distinct. The paper prints the middle coefficient
as $k\,v(1)$; $k\,v(1) + v(2)$ is the coefficient $A_1$ of its Theorem 3, and the printed form
fails already for $k = 2$, $(v(0), v(1), v(2)) = (0, 0, 1)$, $n = 4$, where it gives $0$ while
$v(4) = 1$.

## Sources

- Elen Viviani Pereira Spreafico, Mustapha Rachidi, and Paula Maria Machado Cruz Catarino, *On a Model of (k;p;s)-Generalized Padovan-Perrin and Fibonacci Fundamental System*, INTEGERS 24 (2024), Article A49, Proposition 10.

Stated but not proved: `MetaMathlibExt.kPadovanPerrin_eq_sum_roots` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedPadovanPerrinModelWanted.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html#k-padovan-perrin-eq-sum-roots).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized Padovan–Perrin recurrences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/generalized-padovan-perrin-recurrences)
