---
declaration: section
origin: cited
lean: PierceExpansion.traj, PierceExpansion.traj_zero, PierceExpansion.traj_succ_of_eq_zero, PierceExpansion.traj_succ_of_ne_zero, PierceExpansion.traj_one, PierceExpansion.exists_traj_eq_zero, PierceExpansion.exists_traj_eq_zero_pos, PierceExpansion.length
statement: formalized
proof: formalized
---

# Pierce expansions

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/pierce-expansions/index.html).

## Pierce remainder trajectory

For natural numbers $n$ and $a$, the Pierce remainder
trajectory of $a$ with respect to $n$ is the sequence $t_0, t_1, t_2, \dots$ of natural numbers
with $t_0 = a$ and, for every $j \ge 0$, $t_{j+1} = 0$ if $t_j = 0$, while if $t_j \ne 0$ then
$t_{j+1} = n \bmod t_j$ is the remainder of $n$ modulo $t_j$. Once the trajectory reaches $0$ it
stays there.

Formalized by `PierceExpansion.traj`, a definition declared in [MathlibExt/NumberTheory/PierceExpansion.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PierceExpansion.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/pierce-expansions/index.html#traj).

## Initial term of the Pierce trajectory

For all natural numbers $n$ and $a$, the Pierce
remainder trajectory of $a$ with respect to $n$ has value $a$ at step $0$.

Formalized by `PierceExpansion.traj_zero`, a theorem declared in [MathlibExt/NumberTheory/PierceExpansion.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PierceExpansion.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/pierce-expansions/index.html#traj-zero).

## Step of the Pierce trajectory at a zero term

Let $n$, $a$ and $j$ be natural numbers and
let $t_0, t_1, \dots$ be the Pierce remainder trajectory of $a$ with respect to $n$. If $t_j = 0$,
then $t_{j+1} = 0$.

Formalized by `PierceExpansion.traj_succ_of_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/PierceExpansion.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PierceExpansion.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/pierce-expansions/index.html#traj-succ-of-eq-zero).

## Step of the Pierce trajectory at a nonzero term

Let $n$, $a$ and $j$ be natural numbers
and let $t_0, t_1, \dots$ be the Pierce remainder trajectory of $a$ with respect to $n$. If
$t_j \ne 0$, then $t_{j+1} = n \bmod t_j$, the remainder of $n$ modulo $t_j$.

Formalized by `PierceExpansion.traj_succ_of_ne_zero`, a theorem declared in [MathlibExt/NumberTheory/PierceExpansion.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PierceExpansion.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/pierce-expansions/index.html#traj-succ-of-ne-zero).

## First step of the Pierce trajectory

Let $n$ and $t$ be natural numbers with $t \ne 0$.
Then the Pierce remainder trajectory of $t$ with respect to $n$ is, at step $1$, equal to
$n \bmod t$, the remainder of $n$ modulo $t$.

Formalized by `PierceExpansion.traj_one`, a theorem declared in [MathlibExt/NumberTheory/PierceExpansion.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PierceExpansion.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/pierce-expansions/index.html#traj-one).

## A bound on when a Pierce trajectory vanishes

For natural numbers $n$ and $a$, let
$(t_j)_{j \ge 0}$ be the Pierce remainder trajectory: $t_0 = a$, and $t_{j+1} = n \bmod t_j$ if
$t_j \ne 0$, $t_{j+1} = 0$ if $t_j = 0$. Then $t_i = 0$ for some $i \le a + 1$.

Formalized by `PierceExpansion.exists_traj_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/PierceExpansion.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PierceExpansion.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/pierce-expansions/index.html#exists-traj-eq-zero).

## Pierce trajectories vanish at a positive step

For all natural numbers $n$ and $a$, the
Pierce remainder trajectory $(t_j)_{j \ge 0}$ of $n$ and $a$ (with $t_0 = a$) satisfies $t_j = 0$
for some $j \ge 1$.

Formalized by `PierceExpansion.exists_traj_eq_zero_pos`, a theorem declared in [MathlibExt/NumberTheory/PierceExpansion.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PierceExpansion.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/pierce-expansions/index.html#exists-traj-eq-zero-pos).

## Pierce length

For natural numbers $n$ and $a$, let $(t_j)_{j \ge 0}$ be the Pierce
remainder trajectory, with $t_0 = a$, $t_{j+1} = n \bmod t_j$ if $t_j \ne 0$ and $t_{j+1} = 0$ if
$t_j = 0$. The Pierce length $\ell(n, a)$ is the least $j \ge 1$ with $t_j = 0$; such a $j$
always exists.

For $1 \le a \le n$ this is the length of the Pierce expansion of $a / n$.

Formalized by `PierceExpansion.length`, a definition declared in [MathlibExt/NumberTheory/PierceExpansion.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PierceExpansion.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/pierce-expansions/index.html#length).

## The Pierce length is positive

For all natural numbers $n$ and $a$, the Pierce length
$\ell(n, a)$ satisfies $\ell(n, a) \ge 1$.

Formalized by `PierceExpansion.length_pos`, a theorem declared in [MathlibExt/NumberTheory/PierceExpansion.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PierceExpansion.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/pierce-expansions/index.html#length-pos).

## The Pierce trajectory vanishes at the Pierce length

For all natural numbers $n$ and $a$,
the Pierce remainder trajectory $(t_j)_{j \ge 0}$ of $n$ and $a$ satisfies $t_{\ell(n, a)} = 0$,
where $\ell(n, a)$ is the Pierce length.

Formalized by `PierceExpansion.traj_length_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/PierceExpansion.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PierceExpansion.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/pierce-expansions/index.html#traj-length-eq-zero).

## The Pierce length is at most any positive vanishing step

For natural numbers $n$, $a$ and
$j$ with $j \ge 1$, if the Pierce remainder trajectory $(t_i)_{i \ge 0}$ of $n$ and $a$ satisfies
$t_j = 0$, then the Pierce length $\ell(n, a)$ satisfies $\ell(n, a) \le j$.

Formalized by `PierceExpansion.length_le_of_traj_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/PierceExpansion.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PierceExpansion.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/pierce-expansions/index.html#length-le-of-traj-eq-zero).

## The Pierce trajectory is nonzero before the Pierce length

For natural numbers $n$, $a$ and
$j$ with $1 \le j < \ell(n, a)$, where $\ell(n, a)$ is the Pierce length, the Pierce remainder
trajectory $(t_i)_{i \ge 0}$ of $n$ and $a$ satisfies $t_j \ne 0$.

Formalized by `PierceExpansion.traj_ne_zero_of_lt_length`, a theorem declared in [MathlibExt/NumberTheory/PierceExpansion.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PierceExpansion.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/pierce-expansions/index.html#traj-ne-zero-of-lt-length).

## Maximal Pierce length

For a natural number $n$, the maximal Pierce length $P(n)$ is the
maximum of the Pierce lengths $\ell(n, a)$ over $1 \le a \le n$, with $P(0) = 0$.

Formalized by `PierceExpansion.maxLength`, a definition declared in [MathlibExt/NumberTheory/PierceExpansion.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PierceExpansion.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/pierce-expansions/index.html#max-length).

## Each Pierce length is at most the maximal Pierce length

For natural numbers $n$ and $a$
with $1 \le a \le n$, the Pierce length $\ell(n, a)$ satisfies $\ell(n, a) \le P(n)$, where
$P(n) = \max_{1 \le b \le n} \ell(n, b)$ is the maximal Pierce length.

Formalized by `PierceExpansion.length_le_maxLength`, a theorem declared in [MathlibExt/NumberTheory/PierceExpansion.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PierceExpansion.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/pierce-expansions/index.html#length-le-max-length).

## A uniform bound on Pierce lengths bounds the maximal Pierce length

Let $n$ and $L$ be
natural numbers. If the Pierce length $\ell(n, a)$ satisfies $\ell(n, a) \le L$ for every $a$ with
$1 \le a \le n$, then the maximal Pierce length $P(n) = \max_{1 \le a \le n} \ell(n, a)$ (which is
$0$ when $n = 0$) satisfies $P(n) \le L$.

Formalized by `PierceExpansion.maxLength_le_of_forall`, a theorem declared in [MathlibExt/NumberTheory/PierceExpansion.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PierceExpansion.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/pierce-expansions/index.html#max-length-le-of-forall).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pierce expansions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/pierce-expansions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/continued-fractions-expansions/part-01/pierce-expansions)
