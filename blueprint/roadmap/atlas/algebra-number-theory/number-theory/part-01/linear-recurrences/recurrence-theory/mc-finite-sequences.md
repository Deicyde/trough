---
declaration: section
origin: cited
lean: MetaMathlibExt.IsMCFinite, MetaMathlibExt.isMCFinite_of_mvPolynomial_recursion, MetaMathlibExt.IsPRecursiveSequence.isMCFinite, MetaMathlibExt.polynomially_recursive_MC_finite
statement: formalized
proof: formalized
---

# MC-finite sequences

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/mc-finite-sequences/index.html).

## MC-finite sequences

An integer sequence $s$ is MC-finite if for every natural number
$m > 0$ it eventually satisfies, modulo $m$, a linear recurrence with constant integer
coefficients: there are natural numbers $p > 0$ and $q > 0$ and integers $c_0, \dots, c_{p-1}$
such that $s(n + p) \equiv \sum_{i=0}^{p-1} c_i\, s(n + i) \pmod{m}$ for all $n \ge q$.

## Sources

- Filmus, Fischer, Makowsky, and Rakita, "MC-Finiteness of Restricted Set Partition Functions," Journal of Integer Sequences 26 (2023), Article 23.7.4, lines 281–286.

Formalized by `MetaMathlibExt.IsMCFinite`, a definition declared in [MathlibExt/NumberTheory/Sequences/PolynomiallyRecursiveMCFinite.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Sequences/PolynomiallyRecursiveMCFinite.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/mc-finite-sequences/index.html#is-mcfinite).

## Polynomial recursions give MC-finite sequences

Let $u_0, \dots, u_k$ be integer sequences
and let $P_0, \dots, P_k$ be polynomials with integer coefficients in $k + 2$ variables such that
$u_i(n+1) = P_i(u_0(n), \dots, u_k(n), n)$ for every $i \le k$ and every $n \ge 0$. Then the
sequence $u_0$ is MC-finite.

Formalized by `MetaMathlibExt.isMCFinite_of_mvPolynomial_recursion`, a theorem declared in [MathlibExt/NumberTheory/Sequences/PolynomiallyRecursiveMCFinite.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Sequences/PolynomiallyRecursiveMCFinite.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/mc-finite-sequences/index.html#is-mcfinite-of-mv-polynomial-recursion).

## P-recursive sequences with leading coefficient 1 are MC-finite

Let $s$ be an integer
sequence that is P-recursive of order $k$ with coefficient polynomials $Q_0, \dots, Q_k$ with
integer coefficients, that is, $Q_0(n)\, s_n = \sum_{i=1}^{k} Q_i(n)\, s_{n-i}$ for every $n \ge k$.
If $Q_0 = 1$, then $s$ is MC-finite.

Formalized by `MetaMathlibExt.IsPRecursiveSequence.isMCFinite`, a theorem declared in [MathlibExt/NumberTheory/Sequences/PolynomiallyRecursiveMCFinite.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Sequences/PolynomiallyRecursiveMCFinite.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/mc-finite-sequences/index.html#is-mcfinite-2).

## Polynomially recursive integer sequences are MC-finite

Call an integer sequence $s$
MC-finite if for every natural number $m > 0$ there are natural numbers $p > 0$ and $q > 0$ and
integers $c_0, \dots, c_{p-1}$ such that $m$ divides $s(n + p) - \sum_{i=0}^{p-1} c_i\, s(n + i)$
for all $n \ge q$. Every integer sequence $s$ has the following two properties.

(1) If there are $k \ge 0$, integer sequences $u_0, \dots, u_k$ with $s = u_0$, and polynomials
$P_0, \dots, P_k$ with integer coefficients in $k + 2$ variables such that
$u_i(n+1) = P_i(u_0(n), \dots, u_k(n), n)$ for all $i \le k$ and all $n \ge 0$, then $s$ is
MC-finite.

(2) Holonomic case: if there are $k > 0$ and polynomials $P_1, \dots, P_k$ with integer
coefficients such that $P_1 \ne 0$, $P_k \ne 0$ and $s(n) = \sum_{i=1}^{k} P_i(n)\, s(n - i)$ for
all $n \ge k$, then $s$ is MC-finite.

## Sources

- Yuval Filmus, Eldar Fischer, and Johann A. Makowsky, with Vsevolod Rakita, "MC-Finiteness of Restricted Set Partition Functions," Journal of Integer Sequences 26 (2023), Article 23.7.4, Theorem, lines 422–427, with the MC-finite definition at lines 281–286 and the holonomic/PRS definitions at lines 387–412, <https://cs.uwaterloo.ca/journals/JIS/VOL26/Makowsky/makowsky16.tex>. It follows from `isMCFinite_of_mvPolynomial_recursion` and `IsPRecursiveSequence.isMCFinite`; in the holonomic premise the conditions `0 < k`, `P 1 ≠ 0` and `P k ≠ 0` are unused and keep the source's shape.

Formalized by `MetaMathlibExt.polynomially_recursive_MC_finite`, a theorem declared in [MathlibExt/NumberTheory/Sequences/PolynomiallyRecursiveMCFinite.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Sequences/PolynomiallyRecursiveMCFinite.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/mc-finite-sequences/index.html#polynomially-recursive-mc-finite).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: MC-finite sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/mc-finite-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/recurrence-theory/mc-finite-sequences)
