---
declaration: section
origin: cited
lean: MetaMathlibExt.hyperLeonardo, MetaMathlibExt.hyperLeonardo_zero, MetaMathlibExt.hyperLeonardo_succ, MetaMathlibExt.hyperLeonardo_one_small, MetaMathlibExt.hyperFibonacci, MetaMathlibExt.hyperFibonacci_zero, MetaMathlibExt.hyperFibonacci_succ, MetaMathlibExt.hyperFibonacci_one_small
statement: formalized
---

# Hyper-Leonardo numbers

25 results, 9 proved and 16 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html).

## Hyper-Leonardo numbers

Let $Le_n$ be the Leonardo numbers, defined by
$Le_0 = Le_1 = 1$ and $Le_{n+2} = Le_{n+1} + Le_n + 1$. The hyper-Leonardo numbers are the
integers $Le^{(r)}_n$, for $r, n \ge 0$, defined by $Le^{(0)}_n = Le_n$ and
$Le^{(r+1)}_n = \sum_{k=0}^{n} Le^{(r)}_k$.

## Sources

- Elen Viviani Pereira Spreafico and Paula Maria Machado Cruz Catarino, *A Note on Hyper-Leonardo Numbers*, INTEGERS 26 (2026), Article A48, Definition 1, as displayed in the derivation `Le^{(1)}_n = ∑_{k=0}^{n} Le^{(0)}_k` after Proposition 5.

Formalized by `MetaMathlibExt.hyperLeonardo`, a definition declared in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#hyper-leonardo).

## Hyper-Leonardo numbers of order zero

For every natural number $n$, the hyper-Leonardo
number $Le^{(0)}_n$ equals the Leonardo number $L_{1,n}$, the generalized Leonardo number with
$k = 1$, given by $L_{1,0} = L_{1,1} = 1$ and $L_{1,n+2} = L_{1,n+1} + L_{1,n} + 1$.

## Sources

- Spreafico and Catarino, INTEGERS 26 (2026), Article A48, Definition 1.

Formalized by `MetaMathlibExt.hyperLeonardo_zero`, a theorem declared in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#hyper-leonardo-zero).

## Hyper-Leonardo numbers as partial sums

For all natural numbers $r$ and $n$, the
hyper-Leonardo numbers $Le^{(r)}_n$ satisfy $Le^{(r+1)}_n = \sum_{k=0}^{n} Le^{(r)}_k$.

## Sources

- Spreafico and Catarino, INTEGERS 26 (2026), Article A48, Definition 1.

Formalized by `MetaMathlibExt.hyperLeonardo_succ`, a theorem declared in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#hyper-leonardo-succ).

## First hyper-Leonardo numbers of order one

The hyper-Leonardo numbers $Le^{(1)}_n$ of
order $1$ satisfy $Le^{(1)}_0 = 1$, $Le^{(1)}_1 = 2$, $Le^{(1)}_2 = 5$ and $Le^{(1)}_3 = 10$.

## Sources

- Spreafico and Catarino, INTEGERS 26 (2026), Article A48, Proposition 1 (`Le^{(1)}_0 = 1`, `Le^{(1)}_1 = 2`).

Formalized by `MetaMathlibExt.hyperLeonardo_one_small`, a theorem declared in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#hyper-leonardo-one-small).

## Hyper-Fibonacci numbers

The hyper-Fibonacci numbers $F^{(r)}_n$, for natural numbers $r$
and $n$, are the natural numbers defined by $F^{(0)}_n = F_n$, the $n$-th Fibonacci number
(with $F_0 = 0$ and $F_1 = 1$), and $F^{(r+1)}_n = \sum_{k=0}^{n} F^{(r)}_k$.

## Sources

- Spreafico and Catarino, INTEGERS 26 (2026), Article A48, the hyper-Fibonacci numbers `F^{(r)}_{n+1} = ∑_{k=0}^{n+1} F^{(r-1)}_k` displayed after Proposition 5.

Formalized by `MetaMathlibExt.hyperFibonacci`, a definition declared in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#hyper-fibonacci).

## Hyper-Fibonacci numbers of order zero

For every natural number $n$, the hyper-Fibonacci
number $F^{(0)}_n$ equals the $n$-th Fibonacci number $F_n$ (with $F_0 = 0$ and $F_1 = 1$).

## Sources

- Spreafico and Catarino, INTEGERS 26 (2026), Article A48, after Proposition 5.

Formalized by `MetaMathlibExt.hyperFibonacci_zero`, a theorem declared in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#hyper-fibonacci-zero).

## Hyper-Fibonacci numbers as partial sums

For all natural numbers $r$ and $n$, the
hyper-Fibonacci numbers $F^{(r)}_n$ satisfy $F^{(r+1)}_n = \sum_{k=0}^{n} F^{(r)}_k$.

## Sources

- Spreafico and Catarino, INTEGERS 26 (2026), Article A48, after Proposition 5.

Formalized by `MetaMathlibExt.hyperFibonacci_succ`, a theorem declared in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#hyper-fibonacci-succ).

## Small values of the hyper-Fibonacci numbers of order one

The hyper-Fibonacci numbers
$F^{(1)}_n$ of order $1$ satisfy $F^{(1)}_0 = 0$, $F^{(1)}_1 = 1$, $F^{(1)}_2 = 2$ and
$F^{(1)}_3 = 4$.

## Sources

- Spreafico and Catarino, INTEGERS 26 (2026), Article A48, after Proposition 5 (`F^{(r)}_0 = 0`).

Formalized by `MetaMathlibExt.hyperFibonacci_one_small`, a theorem declared in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#hyper-fibonacci-one-small).

## Recurrences for the hyper-Leonardo numbers of orders zero, one and two

The
hyper-Leonardo numbers $Le^{(r)}_n$ satisfy $Le^{(0)}_0 = Le^{(0)}_1 = 1$, $Le^{(1)}_0 = 1$,
$Le^{(1)}_1 = 2$, $Le^{(2)}_0 = 1$ and $Le^{(2)}_1 = 3$, and for every natural number $n \ge 2$,

$$Le^{(0)}_n = Le^{(0)}_{n-1} + Le^{(0)}_{n-2} + 1,$$



$$Le^{(1)}_n = Le^{(1)}_{n-1} + Le^{(1)}_{n-2} + \binom{n-1}{1} + 1,$$



$$Le^{(2)}_n = Le^{(2)}_{n-1} + Le^{(2)}_{n-2} + \binom{n}{2} + \binom{n-1}{1} + 2.$$

## Sources

- Elen Viviani Pereira Spreafico and Paula Maria Machado Cruz Catarino, *A Note on Hyper-Leonardo Numbers*, INTEGERS 26 (2026), Article A48, Proposition 1.

Stated but not proved: `MetaMathlibExt.hyperLeonardo_recurrence_small_order` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#hyper-leonardo-recurrence-small-order).

## Recurrence for the hyper-Leonardo numbers

For every natural number $r$, the
hyper-Leonardo numbers $Le^{(r)}_n$ of order $r$ satisfy $Le^{(r)}_0 = 1$, $Le^{(r)}_1 = r + 1$
and, for every natural number $n \ge 2$,
$Le^{(r)}_n = r + Le^{(r)}_{n-1} + Le^{(r)}_{n-2} + \binom{n+r-2}{r} +
\sum_{j=1}^{r-1} j \binom{n+r-2-j}{r-j}$.

## Sources

- Elen Viviani Pereira Spreafico and Paula Maria Machado Cruz Catarino, *A Note on Hyper-Leonardo Numbers*, INTEGERS 26 (2026), Article A48, Proposition 2.

Stated but not proved: `MetaMathlibExt.hyperLeonardo_recurrence` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#hyper-leonardo-recurrence).

## Recurrence across consecutive orders of hyper-Leonardo numbers

For all natural numbers
$r \ge 1$ and $n \ge 1$, the hyper-Leonardo numbers $Le^{(r)}_n$ satisfy
$Le^{(r)}_n = Le^{(r)}_{n-1} + Le^{(r-1)}_n$.

## Sources

- Elen Viviani Pereira Spreafico and Paula Maria Machado Cruz Catarino, *A Note on Hyper-Leonardo Numbers*, INTEGERS 26 (2026), Article A48, Proposition 3, Equation (4).

Stated but not proved: `MetaMathlibExt.hyperLeonardo_succ_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#hyper-leonardo-succ-succ).

## Consecutive hyper-Leonardo numbers of order one

For every natural number $n$, the
hyper-Leonardo numbers $Le^{(1)}_n$ of order $1$ satisfy
$Le^{(1)}_{n+1} = Le^{(1)}_n + L_{1,n+1}$, where $L_{1,n}$ is the generalized Leonardo number
with $k = 1$, that is, the Leonardo number $Le_n$.

This is the case $r = 1$ of the recurrence $Le^{(r)}_n = Le^{(r)}_{n-1} + Le^{(r-1)}_n$. The
extracted text of the source reads $Le^{(1)}_n = Le_{n-1} + Le_n$, which fails at $n = 2$, where
$Le^{(1)}_2 = 5$ but $Le_1 + Le_2 = 4$.

## Sources

- Elen Viviani Pereira Spreafico and Paula Maria Machado Cruz Catarino, *A Note on Hyper-Leonardo Numbers*, INTEGERS 26 (2026), Article A48, Corollary 1, Equation (5).

Stated but not proved: `MetaMathlibExt.hyperLeonardo_one_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#hyper-leonardo-one-succ).

## Generating function of shifted binomial coefficients

For every natural number $r$, the
formal power series $\sum_{n \ge 0} \binom{n+r}{r} t^n$ with integer coefficients satisfies
$\left(\sum_{n \ge 0} \binom{n+r}{r} t^n\right)(1-t)^{r+1} = 1$ in $\mathbb{Z}[[t]]$, that is,
$\sum_{n \ge 0} \binom{n+r}{r} t^n = 1/(1-t)^{r+1}$.

The paper states this for positive $r$; it holds for every $r \ge 0$ and is stated so.

## Sources

- Elen Viviani Pereira Spreafico and Paula Maria Machado Cruz Catarino, *A Note on Hyper-Leonardo Numbers*, INTEGERS 26 (2026), Article A48, Lemma 2.

Formalized by `MetaMathlibExt.choose_add_powerSeries_mul_one_sub_pow`, a theorem declared in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#choose-add-power-series-mul-one-sub-pow).

## The convolution of log-concave sequences is log-concave

Let $(x_n)_{n \ge 0}$ and
$(y_n)_{n \ge 0}$ be sequences of positive real numbers that are log-concave, that is,
$x_{j-1} x_{j+1} \le x_j^2$ and $y_{j-1} y_{j+1} \le y_j^2$ for every $j \ge 1$. Let
$z_n = \sum_{k=0}^{n} x_k y_{n-k}$ be their convolution. Then $z_{j-1} z_{j+1} \le z_j^2$ for
every $j \ge 1$.

Positivity is the paper's standing assumption on log-concave sequences.

## Sources

- Elen Viviani Pereira Spreafico and Paula Maria Machado Cruz Catarino, *A Note on Hyper-Leonardo Numbers*, INTEGERS 26 (2026), Article A48, Lemma 3, quoting [1].

Stated but not proved: `MetaMathlibExt.logConcave_convolution` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#log-concave-convolution).

## Generating function of the Leonardo numbers

Let $Le_n$ be the Leonardo numbers
($Le_0 = Le_1 = 1$ and $Le_{n+2} = Le_{n+1} + Le_n + 1$), and let
$L(t) = \sum_{n \ge 0} Le_n t^n$ in the ring $\mathbb{Z}[[t]]$ of formal power series. Then
$L(t)(1 - 2t + t^3) = 1 - t + t^2$ and $L(t)(1 - t - t^2)(1 - t) = 2(1 - t) - (1 - t - t^2)$.

Equivalently, $L(t) = \frac{2}{1-t-t^2} - \frac{1}{1-t} = \frac{1-t+t^2}{1-2t+t^3}$; the
identities above are this equality with the denominators cleared.

## Sources

- Elen Viviani Pereira Spreafico and Paula Maria Machado Cruz Catarino, *A Note on Hyper-Leonardo Numbers*, INTEGERS 26 (2026), Article A48, Corollary 2.

Stated but not proved: `MetaMathlibExt.leonardo_generatingFunction` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#leonardo-generating-function).

## Generating functions of the hyper-Leonardo numbers of orders one and two

In the ring
$\mathbb{Z}[[t]]$ of formal power series, the hyper-Leonardo numbers $Le^{(r)}_n$ satisfy
$\left(\sum_{n \ge 0} Le^{(1)}_n t^n\right)(1 - 2t + t^3)(1 - t) = 1 - t + t^2$ and
$\left(\sum_{n \ge 0} Le^{(2)}_n t^n\right)(1 - 2t + t^3)(1 - t)^2 = 1 - t + t^2$.

Equivalently, the two generating functions are $\frac{1 - t + t^2}{(1 - 2t + t^3)(1 - t)}$ and
$\frac{1 - t + t^2}{(1 - 2t + t^3)(1 - t)^2}$.

## Sources

- Elen Viviani Pereira Spreafico and Paula Maria Machado Cruz Catarino, *A Note on Hyper-Leonardo Numbers*, INTEGERS 26 (2026), Article A48, Corollary 3.

Stated but not proved: `MetaMathlibExt.hyperLeonardo_one_two_generatingFunction` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#hyper-leonardo-one-two-generating-functi).

## Generating function of the hyper-Leonardo numbers

For every natural number $r$, the
formal power series $\sum_{n \ge 0} \mathrm{Le}^{(r)}_n t^n$ of the hyper-Leonardo numbers of
order $r$ satisfies
$\left(\sum_{n \ge 0} \mathrm{Le}^{(r)}_n t^n\right)(1-2t+t^3)(1-t)^r = 1-t+t^2$ in
$\mathbb{Z}[[t]]$, that is,
$\sum_{n \ge 0} \mathrm{Le}^{(r)}_n t^n = \frac{1-t+t^2}{(1-2t+t^3)(1-t)^r}$.

## Sources

- Elen Viviani Pereira Spreafico and Paula Maria Machado Cruz Catarino, *A Note on Hyper-Leonardo Numbers*, INTEGERS 26 (2026), Article A48, Theorem 1, Equation (10).

Stated but not proved: `MetaMathlibExt.hyperLeonardo_generatingFunction` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#hyper-leonardo-generating-function).

## Hyper-Leonardo numbers in terms of hyper-Fibonacci numbers

For all natural numbers $r$
and $n$, the hyper-Leonardo number $\mathrm{Le}^{(r)}_n$ and the hyper-Fibonacci number
$F^{(r)}_{n+1}$ satisfy $\mathrm{Le}^{(r)}_n = 2F^{(r)}_{n+1} - \binom{n+r}{r}$ as integers.

## Sources

- Elen Viviani Pereira Spreafico and Paula Maria Machado Cruz Catarino, *A Note on Hyper-Leonardo Numbers*, INTEGERS 26 (2026), Article A48, Proposition 6, Equation (9).

Stated but not proved: `MetaMathlibExt.hyperLeonardo_eq_hyperFibonacci` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#hyper-leonardo-eq-hyper-fibonacci).

## Log-convexity and log-concavity of the Leonardo numbers

Let $Le_n$ be the Leonardo
numbers ($Le_0 = Le_1 = 1$ and $Le_{n+2} = Le_{n+1} + Le_n + 1$). Then
$Le_n^2 \le Le_{n-1} Le_{n+1}$ for $n = 1$ and $n = 3$, $Le_5^2 = Le_4 Le_6$, and
$Le_{n-1} Le_{n+1} \le Le_n^2$ for $n = 2$, $n = 4$ and every $n \ge 6$.

The paper's "the sequence is log-convex for $n = 1$" is read as the defining inequality at
index $n$.

## Sources

- Elen Viviani Pereira Spreafico and Paula Maria Machado Cruz Catarino, *A Note on Hyper-Leonardo Numbers*, INTEGERS 26 (2026), Article A48, Proposition 10.

Stated but not proved: `MetaMathlibExt.leonardo_logConvex_logConcave_pointwise` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#leonardo-log-convex-log-concave-pointwis).

## Leonardo numbers are log-balanced at index three

Let $Le_n$ be the Leonardo numbers
($Le_0 = Le_1 = 1$ and $Le_{n+2} = Le_{n+1} + Le_n + 1$). Then $Le_3^2 \le Le_2 Le_4$ and
$\frac{Le_2}{2!} \cdot \frac{Le_4}{4!} \le \left(\frac{Le_3}{3!}\right)^2$, the second
inequality in the real numbers. That is, $(Le_n)$ satisfies the log-convexity inequality at
$n = 3$ and $(Le_n / n!)$ satisfies the log-concavity inequality at $n = 3$.

## Sources

- Elen Viviani Pereira Spreafico and Paula Maria Machado Cruz Catarino, *A Note on Hyper-Leonardo Numbers*, INTEGERS 26 (2026), Article A48, Proposition 11, with the definition of log-balanced displayed before Proposition 10.

Stated but not proved: `MetaMathlibExt.leonardo_logBalanced_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#leonardo-log-balanced-three).

## Log-convexity and log-concavity of the hyper-Leonardo numbers at index one

The
hyper-Leonardo numbers $\mathrm{Le}^{(r)}_n$ satisfy
$\left(\mathrm{Le}^{(1)}_1\right)^2 \le \mathrm{Le}^{(1)}_0 \mathrm{Le}^{(1)}_2$, and for every
natural number $r \ge 2$ they satisfy
$\mathrm{Le}^{(r)}_0 \mathrm{Le}^{(r)}_2 \le \left(\mathrm{Le}^{(r)}_1\right)^2$.

## Sources

- Elen Viviani Pereira Spreafico and Paula Maria Machado Cruz Catarino, *A Note on Hyper-Leonardo Numbers*, INTEGERS 26 (2026), Article A48, Proposition 12.

Stated but not proved: `MetaMathlibExt.hyperLeonardo_logConvex_logConcave_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#hyper-leonardo-log-convex-log-concave-on).

## Eventual log-concavity of the hyper-Leonardo numbers of order one

For every natural
number $n \ge 2$, the hyper-Leonardo numbers $Le^{(1)}_n$ of order $1$ satisfy
$Le^{(1)}_{n-1} Le^{(1)}_{n+1} \le (Le^{(1)}_n)^2$.

## Sources

- Elen Viviani Pereira Spreafico and Paula Maria Machado Cruz Catarino, *A Note on Hyper-Leonardo Numbers*, INTEGERS 26 (2026), Article A48, Proposition 13.

Stated but not proved: `MetaMathlibExt.hyperLeonardo_one_logConcave` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#hyper-leonardo-one-log-concave).

## Cassini-type identity for hyper-Leonardo numbers

For all natural numbers $r \ge 1$ and
$n \ge 1$, the hyper-Leonardo numbers $Le^{(r)}_n$ satisfy
$Le^{(r)}_{n-1} Le^{(r)}_{n+1} - (Le^{(r)}_n)^2 =
Le^{(r)}_n Le^{(r-1)}_{n+1} - Le^{(r-1)}_n Le^{(r)}_{n+1}$.

## Sources

- Elen Viviani Pereira Spreafico and Paula Maria Machado Cruz Catarino, *A Note on Hyper-Leonardo Numbers*, INTEGERS 26 (2026), Article A48, Proposition 4.

Stated but not proved: `MetaMathlibExt.hyperLeonardo_mul_sub_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#hyper-leonardo-mul-sub-sq).

## Eventual log-concavity of the hyper-Leonardo numbers of positive order

For all natural
numbers $r \ge 1$ and $n \ge 2$, the hyper-Leonardo numbers $Le^{(r)}_n$ of order $r$ satisfy
$Le^{(r)}_{n-1} Le^{(r)}_{n+1} \le (Le^{(r)}_n)^2$.

The source states this for $r \ge 0$, but it fails for the Leonardo numbers $Le_n = Le^{(0)}_n$
at $n = 3$, where $Le_2 Le_4 = 27 > 25 = Le_3^2$; the source's proof starts its induction at
$r = 1$ (Proposition 13).

## Sources

- Elen Viviani Pereira Spreafico and Paula Maria Machado Cruz Catarino, *A Note on Hyper-Leonardo Numbers*, INTEGERS 26 (2026), Article A48, Proposition 14.

Stated but not proved: `MetaMathlibExt.hyperLeonardo_logConcave` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#hyper-leonardo-log-concave).

## Convexity of the hyper-Leonardo numbers

For all natural numbers $r$ and $n \ge 1$, the
hyper-Leonardo numbers $\mathrm{Le}^{(r)}_n$ satisfy
$2 \mathrm{Le}^{(r)}_n \le \mathrm{Le}^{(r)}_{n-1} + \mathrm{Le}^{(r)}_{n+1}$.

## Sources

- Elen Viviani Pereira Spreafico and Paula Maria Machado Cruz Catarino, *A Note on Hyper-Leonardo Numbers*, INTEGERS 26 (2026), Article A48, Theorem 3, with the definition of convexity displayed before it.

Stated but not proved: `MetaMathlibExt.hyperLeonardo_convex` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperLeonardoWanted.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HyperLeonardoWanted.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html#hyper-leonardo-convex).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hyper-Leonardo numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/second-order-sequences/hyper-leonardo-numbers)
