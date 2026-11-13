---
declaration: section
origin: cited
lean: EngelExpansion.negRem, EngelExpansion.negRem_eq_iff, EngelExpansion.traj, EngelExpansion.traj_zero, EngelExpansion.traj_succ_of_eq_zero, EngelExpansion.traj_succ_of_ne_zero, EngelExpansion.traj_one, EngelExpansion.exists_traj_eq_zero
statement: formalized
proof: formalized
---

# Engel expansions

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/engel-expansions/index.html).

## Negated remainder

For natural numbers $n$ and $k$ with $k \ge 1$, the negated remainder
of $n$ modulo $k$ is the unique $u$ with $0 \le u < k$ and $u \equiv -n \pmod{k}$: it equals $0$
when $k$ divides $n$ and $k - (n \bmod k)$ otherwise. For $k = 0$ it is defined to be $0$.

Formalized by `EngelExpansion.negRem`, a definition declared in [MathlibExt/NumberTheory/EngelExpansion.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EngelExpansion.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/engel-expansions/index.html#neg-rem).

## Characterization of the negated remainder

For natural numbers $n$, $k$ and $u$ with
$k \ne 0$, the negated remainder of $n$ modulo $k$ equals $u$ if and only if $u < k$ and $k$
divides $n + u$.

This is the natural-number form of $u \equiv -n \pmod{k}$.

Formalized by `EngelExpansion.negRem_eq_iff`, a theorem declared in [MathlibExt/NumberTheory/EngelExpansion.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EngelExpansion.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/engel-expansions/index.html#neg-rem-eq-iff).

## Engel remainder trajectory

For natural numbers $n$ and $a$, the Engel remainder
trajectory of $a$ with respect to $n$ is the sequence $t_0, t_1, t_2, \dots$ of natural
numbers with $t_0 = a$ and, for every $j \ge 0$, $t_{j+1} = 0$ if $t_j = 0$, while if
$t_j \ne 0$ then $t_{j+1}$ is the negated remainder of $n$ modulo $t_j$: the unique natural
number $u < t_j$ with $u \equiv -n \pmod{t_j}$. Once the trajectory reaches $0$ it stays there.

Formalized by `EngelExpansion.traj`, a definition declared in [MathlibExt/NumberTheory/EngelExpansion.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EngelExpansion.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/engel-expansions/index.html#traj).

## Initial term of the Engel trajectory

For all natural numbers $n$ and $a$, the Engel
remainder trajectory of $a$ with respect to $n$ has value $a$ at step $0$.

Formalized by `EngelExpansion.traj_zero`, a theorem declared in [MathlibExt/NumberTheory/EngelExpansion.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EngelExpansion.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/engel-expansions/index.html#traj-zero).

## Zero is absorbing for the Engel trajectory

Let $n$, $a$ and $j$ be natural numbers
and let $t_0, t_1, \dots$ be the Engel remainder trajectory of $a$ with respect to $n$. If
$t_j = 0$, then $t_{j+1} = 0$.

Formalized by `EngelExpansion.traj_succ_of_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/EngelExpansion.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EngelExpansion.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/engel-expansions/index.html#traj-succ-of-eq-zero).

## Step of the Engel trajectory at a nonzero term

Let $n$, $a$ and $j$ be natural
numbers and let $t_0, t_1, \dots$ be the Engel remainder trajectory of $a$ with respect to
$n$. If $t_j \ne 0$, then $t_{j+1}$ is the negated remainder of $n$ modulo $t_j$: the unique
natural number $u < t_j$ with $u \equiv -n \pmod{t_j}$.

Formalized by `EngelExpansion.traj_succ_of_ne_zero`, a theorem declared in [MathlibExt/NumberTheory/EngelExpansion.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EngelExpansion.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/engel-expansions/index.html#traj-succ-of-ne-zero).

## First step of the Engel trajectory

Let $n$ and $t$ be natural numbers with
$t \ne 0$. Then the Engel remainder trajectory of $t$ with respect to $n$ is, at step $1$,
the negated remainder of $n$ modulo $t$: the unique natural number $u < t$ with
$u \equiv -n \pmod{t}$.

Formalized by `EngelExpansion.traj_one`, a theorem declared in [MathlibExt/NumberTheory/EngelExpansion.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EngelExpansion.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/engel-expansions/index.html#traj-one).

## An Engel trajectory started at $a$ vanishes within $a + 1$ steps

Let $n$ and $a$ be
natural numbers and let $t_0 = a, t_1, t_2, \dots$ be the Engel trajectory of $a$ with respect to
$n$. Then $t_i = 0$ for some $i \le a + 1$.

Formalized by `EngelExpansion.exists_traj_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/EngelExpansion.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EngelExpansion.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/engel-expansions/index.html#exists-traj-eq-zero).

## Engel trajectories vanish at a positive step

Let $n$ and $a$ be natural numbers and let
$t_0 = a, t_1, t_2, \dots$ be the Engel trajectory of $a$ with respect to $n$. Then $t_j = 0$ for
some $j \ge 1$.

Formalized by `EngelExpansion.exists_traj_eq_zero_pos`, a theorem declared in [MathlibExt/NumberTheory/EngelExpansion.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EngelExpansion.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/engel-expansions/index.html#exists-traj-eq-zero-pos).

## Engel length

For natural numbers $n$ and $a$, let $t_0 = a, t_1, t_2, \dots$ be the Engel
trajectory of $a$ with respect to $n$. The Engel length $L(n, a)$ is the least $j \ge 1$ with
$t_j = 0$.

For $1 \le a \le n$ this is the number of terms of the Engel expansion of $a / n$.

Formalized by `EngelExpansion.length`, a definition declared in [MathlibExt/NumberTheory/EngelExpansion.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EngelExpansion.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/engel-expansions/index.html#length).

## The Engel length is positive

For all natural numbers $n$ and $a$, the Engel length
$L(n, a)$ of $a$ with respect to $n$ satisfies $L(n, a) \ge 1$.

Formalized by `EngelExpansion.length_pos`, a theorem declared in [MathlibExt/NumberTheory/EngelExpansion.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EngelExpansion.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/engel-expansions/index.html#length-pos).

## Engel trajectory vanishes at the Engel length

For all natural numbers $n$ and $a$,
let $L$ be the Engel length of $a$ with respect to $n$. Then the Engel remainder trajectory
of $a$ with respect to $n$ is $0$ at step $L$.

Formalized by `EngelExpansion.traj_length_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/EngelExpansion.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EngelExpansion.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/engel-expansions/index.html#traj-length-eq-zero).

## The Engel length is at most any positive vanishing step

Let $n$, $a$ and $j$ be natural
numbers with $j \ge 1$, and let $t_0 = a, t_1, t_2, \dots$ be the Engel trajectory of $a$ with
respect to $n$. If $t_j = 0$, then the Engel length $L(n, a)$ satisfies $L(n, a) \le j$.

Formalized by `EngelExpansion.length_le_of_traj_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/EngelExpansion.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EngelExpansion.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/engel-expansions/index.html#length-le-of-traj-eq-zero).

## Engel trajectory is nonzero at positive steps before the Engel length

Let $n$, $a$
and $j$ be natural numbers and let $L$ be the Engel length of $a$ with respect to $n$. If
$1 \le j < L$, then the Engel remainder trajectory of $a$ with respect to $n$ is nonzero at
step $j$.

Formalized by `EngelExpansion.traj_ne_zero_of_lt_length`, a theorem declared in [MathlibExt/NumberTheory/EngelExpansion.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EngelExpansion.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/engel-expansions/index.html#traj-ne-zero-of-lt-length).

## Maximal Engel length

For a natural number $n$, the maximal Engel length is
$M(n) = \max_{1 \le a \le n} L(n, a)$, where $L(n, a)$ is the Engel length of $a$ with respect
to $n$; for $n = 0$ the maximum is over the empty set and $M(0) = 0$.

Formalized by `EngelExpansion.maxLength`, a definition declared in [MathlibExt/NumberTheory/EngelExpansion.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EngelExpansion.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/engel-expansions/index.html#max-length).

## Each Engel length is at most the maximal Engel length

Let $n$ and $a$ be natural numbers
with $1 \le a \le n$. Then the Engel length $L(n, a)$ of $a$ with respect to $n$ is at most the
maximal Engel length $M(n) = \max_{1 \le b \le n} L(n, b)$.

Formalized by `EngelExpansion.length_le_maxLength`, a theorem declared in [MathlibExt/NumberTheory/EngelExpansion.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EngelExpansion.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/engel-expansions/index.html#length-le-max-length).

## A uniform bound on Engel lengths bounds the maximal Engel length

Let $n$ and $B$ be
natural numbers. If the Engel length $L(n, a)$ of $a$ with respect to $n$ satisfies
$L(n, a) \le B$ for every $a$ with $1 \le a \le n$, then the maximal Engel length
$M(n) = \max_{1 \le a \le n} L(n, a)$ (with $M(0) = 0$) satisfies $M(n) \le B$.

Formalized by `EngelExpansion.maxLength_le_of_forall`, a theorem declared in [MathlibExt/NumberTheory/EngelExpansion.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/EngelExpansion.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/engel-expansions/index.html#max-length-le-of-forall).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Engel expansions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/engel-expansions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/continued-fractions-expansions/part-01/engel-expansions)
