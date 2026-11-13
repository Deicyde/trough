---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.karatsuba, Cslib.Algorithms.Lean.TimeM.karatsubaCost, Cslib.Algorithms.Lean.TimeM.karatsuba_middle, Cslib.Algorithms.Lean.TimeM.karatsuba_ret, Cslib.Algorithms.Lean.TimeM.karatsuba_operands_lt, Cslib.Algorithms.Lean.TimeM.karatsuba_time, Cslib.Algorithms.Lean.TimeM.karatsubaCost_two_pow, Cslib.Algorithms.Lean.TimeM.karatsubaCost_le
statement: formalized
proof: formalized
---

# Karatsuba algorithm

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/karatsuba-algorithm/index.html).

## Karatsuba multiplication

Karatsuba's algorithm on natural numbers $x$ and $y$, viewed as
$n$-digit numbers in base $B$, as a computation that returns a natural number together with a
cost. If $n \le 1$, it returns $xy$ at cost $1$. If $n \ge 2$, let $m = \lceil n/2 \rceil$, let
$a$ and $b$ be the natural-number quotient and remainder of $x$ by $B^m$, and let $c$ and $d$ be
those of $y$ by $B^m$. It runs itself with digit count $m$ on the pairs $(a, c)$, $(b, d)$ and
$(|a - b|, |c - d|)$, with results $e$, $f$ and $g$, and returns $B^{2m} e + B^m h + f$, where
$h = e + f - g$ (subtraction truncated at $0$) if $b \le a$ holds exactly when $d \le c$, and
$h = e + f + g$ otherwise. The cost of the call is $n$ plus the costs of the three recursive
calls.

Formalized by `Cslib.Algorithms.Lean.TimeM.karatsuba`, a definition declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/karatsuba-algorithm/index.html#karatsuba).

## Karatsuba cost recurrence

The function $T$ on natural numbers defined by $T(n) = 1$ for
$n \le 1$ and $T(n) = 3\,T(\lceil n/2 \rceil) + n$ for $n \ge 2$.

It is the cost of Karatsuba multiplication on $n$ digits: one unit for a product of single
digits, and for $n \ge 2$ three recursive calls on $\lceil n/2 \rceil$ digits plus $n$ units of
linear digit work.

Formalized by `Cslib.Algorithms.Lean.TimeM.karatsubaCost`, a definition declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/karatsuba-algorithm/index.html#karatsuba-cost).

## Karatsuba's middle coefficient

For all natural numbers $a, b, c, d$, write
$P = |a - b| \cdot |c - d|$. If $b \le a$ holds exactly when $d \le c$, then
$ac + bd - P = ad + bc$, where the subtraction is truncated at $0$; otherwise
$ac + bd + P = ad + bc$.

So the cross term $ad + bc$ is recovered from the three products $ac$, $bd$ and $P$.

Formalized by `Cslib.Algorithms.Lean.TimeM.karatsuba_middle`, a theorem declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/karatsuba-algorithm/index.html#karatsuba-middle).

## Correctness of Karatsuba multiplication

For all natural numbers $B$, $n$, $x$ and $y$,
Karatsuba multiplication of $x$ and $y$ as $n$-digit numbers in base $B$ returns $xy$.

The inputs need not be below $B^n$: the digit count only steers the recursion.

Formalized by `Cslib.Algorithms.Lean.TimeM.karatsuba_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/karatsuba-algorithm/index.html#karatsuba-ret).

## Size bound for Karatsuba's recursive operands

Let $B \ge 1$ and $n$ be natural numbers,
let $m = \lceil n/2 \rceil$, and let $x < B^n$ be a natural number. Then the high part
$\lfloor x / B^m \rfloor$, the low part $x \bmod B^m$, and their distance
$|\lfloor x / B^m \rfloor - x \bmod B^m|$ are all less than $B^m$.

Applied to both inputs, all six recursive operands stay within the digit model, and the base case
multiplies single digits.

Formalized by `Cslib.Algorithms.Lean.TimeM.karatsuba_operands_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/karatsuba-algorithm/index.html#karatsuba-operands-lt).

## Cost of Karatsuba multiplication

For all natural numbers $B$, $n$, $x$ and $y$, the cost
of Karatsuba multiplication of $x$ and $y$ as $n$-digit numbers in base $B$ equals $T(n)$, where
$T$ is the Karatsuba cost recurrence, $T(n) = 1$ for $n \le 1$ and
$T(n) = 3\,T(\lceil n/2 \rceil) + n$ for $n \ge 2$.

In particular the cost depends only on the digit count $n$, not on $B$, $x$ or $y$.

Formalized by `Cslib.Algorithms.Lean.TimeM.karatsuba_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/karatsuba-algorithm/index.html#karatsuba-time).

## Karatsuba cost at powers of two

Let $T$ be the Karatsuba cost recurrence, $T(n) = 1$ for
$n \le 1$ and $T(n) = 3\,T(\lceil n/2 \rceil) + n$ for $n \ge 2$. For every natural number $k$,
$T(2^k) + 2^{k+1} = 3^{k+1}$.

So at $n = 2^k$ digits the cost is exactly $3^{k+1} - 2^{k+1} = 3\, n^{\log_2 3} - 2n$.

Formalized by `Cslib.Algorithms.Lean.TimeM.karatsubaCost_two_pow`, a theorem declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/karatsuba-algorithm/index.html#karatsuba-cost-two-pow).

## Power-of-three bound on the Karatsuba cost recurrence

Let $T$ be the Karatsuba cost
recurrence, $T(n) = 1$ for $n \le 1$ and $T(n) = 3\,T(\lceil n/2 \rceil) + n$ for $n \ge 2$, and
let $\ell(n)$ be the least natural number $k$ with $n \le 2^k$ (so
$\ell(n) = \lceil \log_2 n \rceil$ for $n \ge 1$). For every natural number $n$,
$T(n) \le 3^{\ell(n) + 1}$.

The proof pads $n$ up to the next power of two.

Formalized by `Cslib.Algorithms.Lean.TimeM.karatsubaCost_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/karatsuba-algorithm/index.html#karatsuba-cost-le).

## Power-of-three bound on the cost of Karatsuba multiplication

Let $\ell(n)$ be the least
natural number $k$ with $n \le 2^k$ (so $\ell(n) = \lceil \log_2 n \rceil$ for $n \ge 1$). For all
natural numbers $B$, $n$, $x$ and $y$, the cost of Karatsuba multiplication of $x$ and $y$ as
$n$-digit numbers in base $B$ is at most $3^{\ell(n) + 1}$.

Formalized by `Cslib.Algorithms.Lean.TimeM.karatsuba_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/karatsuba-algorithm/index.html#karatsuba-time-le).

## The $n^{\log_2 3}$ bound for the Karatsuba cost recurrence

Let $T$ be the Karatsuba cost
recurrence, $T(n) = 1$ for $n \le 1$ and $T(n) = 3\,T(\lceil n/2 \rceil) + n$ for $n \ge 2$. For
every natural number $n \ge 1$, $T(n) \le 9\, n^{\log_2 3}$.

Formalized by `Cslib.Algorithms.Lean.TimeM.karatsubaCost_le_rpow`, a theorem declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/karatsuba-algorithm/index.html#karatsuba-cost-le-rpow).

## The $n^{\log_2 3}$ bound for Karatsuba multiplication

For all natural numbers $B$, $x$,
$y$ and $n \ge 1$, the cost of Karatsuba multiplication of $x$ and $y$ as $n$-digit numbers in
base $B$ is at most $9\, n^{\log_2 3}$.

Formalized by `Cslib.Algorithms.Lean.TimeM.karatsuba_time_le_rpow`, a theorem declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DivideAndConquer/Karatsuba.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/karatsuba-algorithm/index.html#karatsuba-time-le-rpow).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Karatsuba algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/karatsuba-algorithm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/algebraic-and-numerical-algorithms/karatsuba-algorithm)
