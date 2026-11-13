---
declaration: section
origin: cited
lean: Nat.collatzStep, Nat.collatzIterate, Nat.collatzStoppingTime, MetaMathlibExt.qShift, MetaMathlibExt.qShift_X_mul, MetaMathlibExt.qCollatz, MetaMathlibExt.qCollatz_X_mul, MetaMathlibExt.qCollatz_zero
statement: formalized
---

# Collatz problem

26 results, 16 proved and 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html).

## The Collatz map

The Collatz map $T : \mathbb{N} \to \mathbb{N}$ sends a natural number
$n$ to $n / 2$ if $n$ is even and to $3n + 1$ if $n$ is odd.

Formalized by `Nat.collatzStep`, a definition declared in [MathlibExt/NumberTheory/Collatz.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Collatz.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#collatz-step).

## Iterates of the Collatz map

Let $T : \mathbb{N} \to \mathbb{N}$ be the Collatz map, which
sends $n$ to $n / 2$ if $n$ is even and to $3n + 1$ if $n$ is odd. For natural numbers $k$ and
$n$, the $k$-th Collatz iterate of $n$ is $T^k(n)$, the result of applying $T$ to $n$ exactly $k$
times: $T^0(n) = n$ and $T^{k+1}(n) = T(T^k(n))$.

Formalized by `Nat.collatzIterate`, a definition declared in [MathlibExt/NumberTheory/Collatz.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Collatz.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#collatz-iterate).

## Collatz stopping time

Let $T : \mathbb{N} \to \mathbb{N}$ be the Collatz map, which sends
$n$ to $n / 2$ if $n$ is even and to $3n + 1$ if $n$ is odd, and let $T^k$ denote its $k$-fold
iterate, with $T^0(n) = n$. For a natural number $n$, the Collatz stopping time of $n$ is
undefined if $n = 0$ or if $T^k(n) \ne 1$ for every $k \in \mathbb{N}$; otherwise it is the least
$k \in \mathbb{N}$ with $T^k(n) = 1$.

In the Collatz literature this quantity is often called the total stopping time.

Formalized by `Nat.collatzStoppingTime`, a definition declared in [MathlibExt/NumberTheory/Collatz.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Collatz.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#collatz-stopping-time).

## Division by $q$ in $\mathbb{F}_2((q))$

For a power series
$x = \sum_n x_n q^n \in \mathbb{F}_2[[q]]$, its shift is the power series $\sum_n x_{n+1} q^n$,
obtained by discarding the constant term of $x$ and dividing by $q$. In particular, the shift of
$qy$ is $y$ for every $y \in \mathbb{F}_2[[q]]$.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Section 1 (the quotients `x/q` and `(Ax+B)/q` in the definition of `T_{A,B}`).

Formalized by `MetaMathlibExt.qShift`, a definition declared in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#q-shift).

## Dividing a multiple of $q$ by $q$

For every power series $y \in \mathbb{F}_2[[q]]$,
applying the shift $\sum_n x_n q^n \mapsto \sum_n x_{n+1} q^n$ to $qy$ gives back $y$.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Section 1 (division by `q`).

Formalized by `MetaMathlibExt.qShift_X_mul`, a theorem declared in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#q-shift-x-mul).

## The q-analog of the 3x+1 map

For a power series $y = \sum_n y_n q^n \in \mathbb{F}_2[[q]]$,
write $y/q$ for the power series $\sum_n y_{n+1} q^n$: the constant term of $y$ is discarded and the
rest is divided by $q$. For power series $A, B \in \mathbb{F}_2[[q]]$, the map
$T_{A,B} : \mathbb{F}_2[[q]] \to \mathbb{F}_2[[q]]$ is defined by $T_{A,B}(x) = x/q$ if the
constant term of $x$ is $0$, and $T_{A,B}(x) = (Ax + B)/q$ otherwise.

When $A$ and $B$ have constant term $1$, the numerator $Ax + B$ has constant term $0$ whenever
$x$ has constant term $1$, so in that case the division by $q$ is exact.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Section 1 (definition of `T_{A,B}`).

Formalized by `MetaMathlibExt.qCollatz`, a definition declared in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#q-collatz).

## The q-analog 3x+1 map on multiples of $q$

For all power series
$A, B, y \in \mathbb{F}_2[[q]]$, the $q$-analog $3x+1$ map satisfies $T_{A,B}(qy) = y$.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Section 1 (definition of `T_{A,B}`).

Formalized by `MetaMathlibExt.qCollatz_X_mul`, a theorem declared in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#q-collatz-x-mul).

## Zero is a fixed point of the q-analog 3x+1 map

For all power series
$A, B \in \mathbb{F}_2[[q]]$, the $q$-analog $3x+1$ map satisfies $T_{A,B}(0) = 0$.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Section 1 (definition of `T_{A,B}`).

Formalized by `MetaMathlibExt.qCollatz_zero`, a theorem declared in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#q-collatz-zero).

## Divisibility by $2$ from the residue modulo $2$

If the residue modulo $2$ of a $2$-adic
integer $y \in \mathbb{Z}_2$ is zero, then $2$ divides $y$ in $\mathbb{Z}_2$.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Section 1 (parity in `ℤ₂`, so that `T` is a self-map).

Formalized by `MetaMathlibExt.two_dvd_of_toZMod_eq_zero`, a theorem declared in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#two-dvd-of-to-zmod-eq-zero).

## $3x + 1$ is even for odd $2$-adic $x$

For every $2$-adic integer $x \in \mathbb{Z}_2$ whose
residue modulo $2$ is nonzero, the residue of $3x + 1$ modulo $2$ is zero.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Section 1 (definition of `T`).

Formalized by `MetaMathlibExt.toZMod_three_mul_add_one_of_odd`, a theorem declared in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#to-zmod-three-mul-add-one-of-odd).

## The $2$-adic $3x+1$ map

The map $T : \mathbb{Z}_2 \to \mathbb{Z}_2$ is defined by
$T(x) = x/2$ if $x$ is even and $T(x) = (3x+1)/2$ if $x$ is odd, where even and odd refer to the
residue of $x$ modulo $2$.

In both cases the numerator is divisible by $2$ in $\mathbb{Z}_2$, so the division is exact.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Section 1 (definition of `T` extended to `ℤ₂`).

Formalized by `MetaMathlibExt.twoAdicCollatz`, a definition declared in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#two-adic-collatz).

## Even branch of the $2$-adic $3x+1$ map

Let $T : \mathbb{Z}_2 \to \mathbb{Z}_2$ be
the $3x+1$ map on the $2$-adic integers. For every $x \in \mathbb{Z}_2$ whose residue modulo $2$
is zero, $2\,T(x) = x$.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Section 1 (definition of `T`).

Formalized by `MetaMathlibExt.two_mul_twoAdicCollatz_of_even`, a theorem declared in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#two-mul-two-adic-collatz-of-even).

## Odd branch of the $2$-adic $3x+1$ map

Let $T : \mathbb{Z}_2 \to \mathbb{Z}_2$ be
the $3x+1$ map on the $2$-adic integers. For every $x \in \mathbb{Z}_2$ whose residue modulo $2$
is nonzero, $2\,T(x) = 3x + 1$.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Section 1 (definition of `T`).

Formalized by `MetaMathlibExt.two_mul_twoAdicCollatz_of_odd`, a theorem declared in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#two-mul-two-adic-collatz-of-odd).

## The $2$-adic $3x+1$ map swaps $1$ and $2$

The $2$-adic $3x+1$ map
$T : \mathbb{Z}_2 \to \mathbb{Z}_2$ satisfies $T(1) = 2$ and $T(2) = 1$.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Section 1 (definition of `T`).

Formalized by `MetaMathlibExt.twoAdicCollatz_one_two`, a theorem declared in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#two-adic-collatz-one-two).

## The parity vector of the q-analog 3x+1 map

For power series
$A, B, x \in \mathbb{F}_2[[q]]$, the parity vector of $x$ is the $2$-adic integer
$\mathrm{PV}_{A,B}(x) = \sum_{k \ge 0} x_k 2^k \in \mathbb{Z}_2$, where $x_k \in \{0, 1\}$ is the
constant coefficient of the $k$-th iterate $T_{A,B}^k(x)$ of the $q$-analog $3x+1$ map $T_{A,B}$.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Definition 10.

Formalized by `MetaMathlibExt.qCollatzParityVector`, a definition declared in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#q-collatz-parity-vector).

## The parity vector of $0$

For all $A, B \in \mathbb{F}_2[[q]]$, the parity vector of $0$
under the $q$-analog $T_{A,B}$ of the $3x+1$ map is $0$, that is, $\mathrm{PV}_{A,B}(0) = 0$.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Definition 10.

Formalized by `MetaMathlibExt.qCollatzParityVector_zero`, a theorem declared in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#q-collatz-parity-vector-zero).

## The $q$-Collatz map is conjugate to the $2$-adic $3x+1$ map

Let $A$ and $B$ be odd
power series in $\mathbb{F}_2[[q]]$ (constant term $1$), let $T_{A,B}$ be the $q$-analog of the
$3x+1$ map on $\mathbb{F}_2[[q]]$, and let $T$ be the $3x+1$ map on the $2$-adic integers
$\mathbb{Z}_2$. Then there is a bijection $h : \mathbb{Z}_2 \to \mathbb{F}_2[[q]]$ with
$h^{-1}(T_{A,B}(h(x))) = T(x)$ for every $x \in \mathbb{Z}_2$.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Theorem 2 (`jis-2025-25.6.8-thm-2`).

Stated but not proved: `MetaMathlibExt.qCollatz_conjugate_twoAdicCollatz` is written with `theorem_wanted` in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#q-collatz-conjugate-two-adic-collatz).

## The map $T_{1+q,1}$ is conjugate to the $2$-adic $3x+1$ map

Let $T_q = T_{1+q,1}$
be the $q$-analog of the $3x+1$ map with $A = 1 + q$ and $B = 1$, so that $T_q(x) = x/q$ if $q$
divides $x$ and $T_q(x) = ((1+q)x + 1)/q$ otherwise, and let $T$ be the $3x+1$ map on the
$2$-adic integers $\mathbb{Z}_2$. Then there is a bijection $h : \mathbb{Z}_2 \to \mathbb{F}_2[[q]]$
with $h^{-1}(T_q(h(x))) = T(x)$ for every $x \in \mathbb{Z}_2$.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Corollary 3 (`jis-2025-25.6.8-cor-3`).

Stated but not proved: `MetaMathlibExt.qCollatz_one_add_X_conjugate_twoAdicCollatz` is written with `theorem_wanted` in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#q-collatz-one-add-x-conjugate-two-adic-c).

## Polynomial orbits of $T_{1,1+q^2}$

Let $T = T_{1,1+q^2}$ be the $q$-analog of the $3x+1$
map with $A = 1$ and $B = 1 + q^2$. For every polynomial $p$ over $\mathbb{F}_2$, some iterate
$T^k(p)$ with $k \ge 0$ lies in $\{0, 1 + q, 1, q\}$, the set formed by the fixed points $0$ and
$1 + q$ of $T$ and its $2$-cycle $\{1, q\}$. Moreover, for every $x \in \mathbb{F}_2[[q]]$, $T(x)$
is a polynomial if and only if $x$ is a polynomial.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Theorem 5 (`jis-2025-25.6.8-thm-5`).

Stated but not proved: `MetaMathlibExt.qCollatz_one_one_add_X_sq_polynomial` is written with `theorem_wanted` in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#q-collatz-one-one-add-x-sq-polynomial).

## A perturbation at $q^{n+1}$ moves to $q^n$ under $T_{A,B}$

Let $A, B, U, V$ be power
series in $\mathbb{F}_2[[q]]$ with $A$, $B$ and $V$ odd (constant term $1$), let $T_{A,B}$ be the
$q$-analog of the $3x+1$ map, and let $n \ge 0$ be an integer. Then there is an odd power series
$W \in \mathbb{F}_2[[q]]$ with $T_{A,B}(U + q^{n+1} V) = T_{A,B}(U) + q^n W$.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Lemma 7 (`jis-2025-25.6.8-lem-7`).

Stated but not proved: `MetaMathlibExt.qCollatz_add_X_pow_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#q-collatz-add-x-pow-mul).

## Iterates of $T_{A,B}$ move a perturbation at $q^{n+1}$ to $q^{n+1-k}$

Let $A, B, U, V$
be power series in $\mathbb{F}_2[[q]]$ with $A$, $B$ and $V$ odd (constant term $1$), let
$T_{A,B}$ be the $q$-analog of the $3x+1$ map, and let $n$ and $k$ be natural numbers with
$k \le n + 1$. Write $T_{A,B}^k$ for the $k$-th iterate of $T_{A,B}$. Then there is an odd power
series $W \in \mathbb{F}_2[[q]]$ with $T_{A,B}^k(U + q^{n+1} V) = T_{A,B}^k(U) + q^{n+1-k} W$.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Corollary 8 (`jis-2025-25.6.8-cor-8`).

Stated but not proved: `MetaMathlibExt.qCollatz_iterate_add_X_pow_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#q-collatz-iterate-add-x-pow-mul).

## A perturbation at $q^n$ flips the parity of the $n$-th iterate

Let
$A, B, U, V \in \mathbb{F}_2[[q]]$ with $A$, $B$ and $V$ odd (constant term $1$), let $T_{A,B}$ be
the $q$-analog of the $3x+1$ map, and let $n \ge 0$ be an integer. Then the $n$-th iterates
$T_{A,B}^n(U + q^n V)$ and $T_{A,B}^n(U)$ have different constant terms.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Corollary 9 (`jis-2025-25.6.8-cor-9`).

Stated but not proved: `MetaMathlibExt.qCollatz_iterate_parity_flip` is written with `theorem_wanted` in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#q-collatz-iterate-parity-flip).

## Parity vectors detect congruence modulo $q^{n+1}$

Let $A, B \in \mathbb{F}_2[[q]]$ be odd
(constant term $1$), let $\mathrm{PV}_{A,B}$ be the parity vector map of the $q$-analog $T_{A,B}$
of the $3x+1$ map, and let $n \ge 0$ be an integer. For all $a, b \in \mathbb{F}_2[[q]]$, we have
$\mathrm{PV}_{A,B}(a) \equiv \mathrm{PV}_{A,B}(b) \pmod{2^{n+1}}$ in $\mathbb{Z}_2$ if and only if
$q^{n+1}$ divides $a - b$.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Theorem 11 (`jis-2025-25.6.8-thm-11`).

Stated but not proved: `MetaMathlibExt.qCollatzParityVector_modEq_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#q-collatz-parity-vector-mod-eq-iff).

## Parity vectors induce bijections modulo $q^n$

Let $A, B \in \mathbb{F}_2[[q]]$ be odd
(constant term $1$), let $\mathrm{PV}_{A,B}$ be the parity vector map of the $q$-analog $T_{A,B}$
of the $3x+1$ map, and let $n \ge 1$ be an integer. Then there is a bijection
$e : \mathbb{F}_2[[q]]/(q^n) \to \mathbb{Z}/2^n\mathbb{Z}$ such that, for every
$a \in \mathbb{F}_2[[q]]$, $e$ sends the class of $a$ to the residue of $\mathrm{PV}_{A,B}(a)$
modulo $2^n$.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Corollary 12 (`jis-2025-25.6.8-cor-12`).

Stated but not proved: `MetaMathlibExt.qCollatzParityVector_quotient_bijection` is written with `theorem_wanted` in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#q-collatz-parity-vector-quotient-bijecti).

## Fixed points and the $2$-cycle of the $q$-Collatz map

Let $A, B \in \mathbb{F}_2[[q]]$ be
odd (constant term $1$) and let $T_{A,B}$ be the $q$-analog of the $3x+1$ map. For every
$x \in \mathbb{F}_2[[q]]$, $T_{A,B}(x) = x$ holds exactly when $x = 0$ or $x = B/(A+q)$. Moreover,
for every $x \in \mathbb{F}_2[[q]]$, $T_{A,B}(T_{A,B}(x)) = x$ and $T_{A,B}(x) \ne x$ hold together
exactly when $x = B/(A+q^2)$ or $x = qB/(A+q^2)$.

## Sources

- Kenneth G. Monks, *On q-Analogs of the 3x+1 Dynamical System*, Journal of Integer Sequences 28 (2025), Article 25.6.8, Lemma 13 (`jis-2025-25.6.8-lem-13`).

Stated but not proved: `MetaMathlibExt.qCollatz_fixedPoints_and_twoCycle` is written with `theorem_wanted` in [WantedExt/NumberTheory/QAnalogCollatzWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QAnalogCollatzWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#q-collatz-fixed-points-and-two-cycle).

## No Collatz $m$-cycles with $m \le 91$ (Hercher)

Let $T$ be the shortcut Collatz map on
the natural numbers, $T(c) = c/2$ for even $c$ and $T(c) = (3c+1)/2$ for odd $c$, and let $m$ be
a natural number with $m \le 91$. There are no natural numbers $n$ and $p > 0$ such that
$T^i(n) > 2$ for all $i < p$, $T^p(n) = n$, $T^k(n) \ne n$ for all $k$ with $0 < k < p$, and
exactly $m$ indices $i < p$ satisfy both $T^i(n) < T^{(i+1) \bmod p}(n)$ and
$T^i(n) < T^{(i+p-1) \bmod p}(n)$.

In words: no cycle of $T$ all of whose entries exceed $2$ (which excludes the trivial cycle
$1, 2, 1, 2, \dots$), taken with its minimal period $p$, has exactly $m$ entries lying cyclically
strictly below both neighbours.

## Sources

- Christian Hercher, "There are no Collatz m-Cycles with m ≤ 91," Journal of Integer Sequences 26 (2023), Article 23.3.5, Main Theorem, lines 541–543, https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.tex with the operator at lines 104–111 and the m-cycle definition at lines 149–151.

Stated but not proved: `MetaMathlibExt.no_collatz_m_cycle_le_ninety_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Sequences/NoCollatzMCycleWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Sequences/NoCollatzMCycleWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html#no-collatz-m-cycle-le-ninety-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Collatz problem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/integer-sequences/iterated-self-referential/collatz-problem)
