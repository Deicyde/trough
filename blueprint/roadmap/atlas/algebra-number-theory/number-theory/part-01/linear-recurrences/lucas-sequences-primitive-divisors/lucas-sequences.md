---
declaration: section
origin: cited
lean: MetaMathlibExt.LucasSequenceParams, MetaMathlibExt.LucasSequenceParams.IsCoprime, MetaMathlibExt.lucasU, MetaMathlibExt.lucasV, MetaMathlibExt.fibonacciLucasParams, MetaMathlibExt.lucasNumber, MetaMathlibExt.lucasU_fibonacciLucasParams, MetaMathlibExt.lucasU_add_two
statement: formalized
---

# Lucas sequences

20 results, 19 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html).

## Parameters of a Lucas sequence

Lucas sequence parameters are a pair of integers
$(P, Q)$ with $Q \ne 0$.

The condition $Q \ne 0$ follows the convention of the sources.

Formalized by `MetaMathlibExt.LucasSequenceParams`, a structure declared in [MathlibExt/NumberTheory/LucasSequence.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LucasSequence.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html#lucas-sequence-params).

## Coprime Lucas sequence parameters

Lucas sequence parameters $(P, Q)$ are coprime when
there exist integers $x$ and $y$ with $xP + yQ = 1$.

This additional condition is imposed in some applications of Lucas sequences.

Formalized by `MetaMathlibExt.LucasSequenceParams.IsCoprime`, a definition declared in [MathlibExt/NumberTheory/LucasSequence.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LucasSequence.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html#is-coprime).

## Lucas sequence $U(P, Q)$

For Lucas sequence parameters $(P, Q)$, the Lucas sequence
$U(P, Q)$ is the integer sequence $(U_n)_{n \ge 0}$ with $U_0 = 0$, $U_1 = 1$ and
$U_{n+2} = P U_{n+1} - Q U_n$ for every natural number $n$.

Formalized by `MetaMathlibExt.lucasU`, a definition declared in [MathlibExt/NumberTheory/LucasSequence.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LucasSequence.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html#lucas-u).

## Companion Lucas sequence $V(P, Q)$

For Lucas sequence parameters $(P, Q)$, the
companion Lucas sequence $V(P, Q)$ is the integer sequence $(V_n)_{n \ge 0}$ with $V_0 = 2$,
$V_1 = P$ and $V_{n+2} = P V_{n+1} - Q V_n$ for every natural number $n$.

Formalized by `MetaMathlibExt.lucasV`, a definition declared in [MathlibExt/NumberTheory/LucasSequence.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LucasSequence.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html#lucas-v).

## Fibonacci parameters for Lucas sequences

The Fibonacci parameters are the Lucas sequence
parameters $P = 1$ and $Q = -1$; they satisfy the required condition $Q \ne 0$.

These parameters give the Fibonacci and classical Lucas-number sequences.

Formalized by `MetaMathlibExt.fibonacciLucasParams`, a definition declared in [MathlibExt/NumberTheory/LucasSequence.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LucasSequence.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html#fibonacci-lucas-params).

## Lucas numbers

The Lucas numbers are the natural numbers $L_n$ defined by $L_0 = 2$,
$L_1 = 1$ and $L_{n+2} = L_{n+1} + L_n$ for every natural number $n$. They begin
$2, 1, 3, 4, 7, \dots$.

Formalized by `MetaMathlibExt.lucasNumber`, a definition declared in [MathlibExt/NumberTheory/LucasSequence.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LucasSequence.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html#lucas-number).

## The Lucas sequence $U(1, -1)$ is the Fibonacci sequence

For every natural number $n$,
the $n$-th term of the Lucas sequence $U(1, -1)$ equals the Fibonacci number $F_n$, where
$F_0 = 0$, $F_1 = 1$ and $F_{n+2} = F_{n+1} + F_n$.

Formalized by `MetaMathlibExt.lucasU_fibonacciLucasParams`, a theorem declared in [MathlibExt/NumberTheory/LucasSequence.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LucasSequence.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html#lucas-u-fibonacci-lucas-params).

## Recurrence for the Lucas sequence $U(P, Q)$

For Lucas sequence parameters $(P, Q)$ and
every natural number $n$, the Lucas sequence $U = U(P, Q)$ satisfies
$U_{n+2} = P U_{n+1} - Q U_n$.

Formalized by `MetaMathlibExt.lucasU_add_two`, a theorem declared in [MathlibExt/NumberTheory/LucasSequence.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LucasSequence.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html#lucas-u-add-two).

## Cassini's identity for Lucas sequences

For Lucas sequence parameters $(P, Q)$ and every
natural number $n$, the Lucas sequence $U = U(P, Q)$ satisfies
$U_{n+1}^2 - U_n U_{n+2} = Q^n$.

Formalized by `MetaMathlibExt.lucasU_cassini`, a theorem declared in [MathlibExt/NumberTheory/LucasSequence.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LucasSequence.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html#lucas-u-cassini).

## The Lucas sequence $V(1, -1)$ gives the Lucas numbers

For every natural number $n$, the
$n$-th term of the companion Lucas sequence $V(1, -1)$ equals the $n$-th Lucas number $L_n$.

Formalized by `MetaMathlibExt.lucasV_fibonacciLucasParams`, a theorem declared in [MathlibExt/NumberTheory/LucasSequence.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LucasSequence.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html#lucas-v-fibonacci-lucas-params).

## Special primes of a Lucas pair

For integers $P$ and $Q$, a natural number $p$ is a special
prime for the Lucas parameters $(P, Q)$ if $p$ is prime and $p$ divides $\gcd(P, Q)$.

Formalized by `MetaMathlibExt.IsLucasSpecialPrime`, a definition declared in [MathlibExt/NumberTheory/LucasSpecialPrime.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LucasSpecialPrime.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html#is-lucas-special-prime).

## Special primes are the common prime divisors of the parameters

For integers $P$ and $Q$
and a natural number $p$, $p$ is a special prime for the Lucas parameters $(P, Q)$ if and only if
$p$ is prime and $p$ divides both $P$ and $Q$ in $\mathbb{Z}$.

Formalized by `MetaMathlibExt.isLucasSpecialPrime_iff`, a theorem declared in [MathlibExt/NumberTheory/LucasSpecialPrime.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LucasSpecialPrime.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html#is-lucas-special-prime-iff).

## Binet formulas for Lucas sequences over any field

Let $P$ and $Q$ be integers with
$Q \ne 0$, let $U_n = U_n(P, Q)$ and $V_n = V_n(P, Q)$ be the associated Lucas sequences, and let
$\alpha$ and $\beta$ be elements of a field $K$ with $\alpha + \beta = P$ and $\alpha \beta = Q$
in $K$. If $\alpha \ne \beta$, then for every natural number $n$,
$U_n = (\alpha^n - \beta^n) / (\alpha - \beta)$ and $V_n = \alpha^n + \beta^n$ in $K$. If
$\beta = \alpha$, then for every natural number $n$, $U_n = n \alpha^{n-1}$ and $V_n = 2 \alpha^n$
in $K$, where $\alpha^{n-1}$ is read as $1$ when $n = 0$. Here the integers $U_n$, $V_n$, $P$, $Q$
and $n$ are mapped into $K$.

No assumption on the characteristic of $K$ is made; for example $K$ may be $\mathbb{Z}/p\mathbb{Z}$
for a prime $p$, where the coefficient $n$ of the double-root formula is read modulo $p$.

Formalized by `MetaMathlibExt.lucas_binet_formulas_of_field`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/LucasBinetFormula.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/LucasBinetFormula.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html#lucas-binet-formulas-of-field).

## Binet formulas for Lucas sequences

Let $P$ and $Q$ be integers with $Q \ne 0$, let
$U_n = U_n(P, Q)$ and $V_n = V_n(P, Q)$ be the associated Lucas sequences, and let $\alpha$ and
$\beta$ be elements of a field $K$ of characteristic zero with $\alpha + \beta = P$ and
$\alpha \beta = Q$ in $K$. If $\alpha \ne \beta$, then for every natural number $n$,
$U_n = (\alpha^n - \beta^n) / (\alpha - \beta)$ and $V_n = \alpha^n + \beta^n$ in $K$. If
$\beta = \alpha$, then for every natural number $n$, $U_n = n \alpha^{n-1}$ and $V_n = 2 \alpha^n$
in $K$, where $\alpha^{n-1}$ is read as $1$ when $n = 0$. Here the integers $U_n$, $V_n$, $P$, $Q$
and $n$ are mapped into $K$.

In the double-root case the hypotheses give $P = 2 \alpha$ and $Q = \alpha^2$.

## Sources

- Christian Ballot, "A Further Generalization of a Congruence of Wolstenholme", Journal of Integer Sequences 15 (2012), Article 12.8.6, sequence definitions and formulas at lines 274–289, https://cs.uwaterloo.ca/journals/JIS/VOL15/Ballot/ballot4.tex

Formalized by `MetaMathlibExt.lucas_binet_formulas`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/LucasBinetFormula.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/LucasBinetFormula.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html#lucas-binet-formulas).

## Lucas sequence of the first kind

For integers $P$ and $Q$, a sequence of integers
$(u_n)_{n \ge 0}$ is the Lucas sequence of the first kind with parameters $P$ and $Q$ when
$u_0 = 0$, $u_1 = 1$, and $u_{n+2} = P u_{n+1} - Q u_n$ for every natural number $n$.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL13/Smyth/smyth2.tex>, lines 114-122.

Formalized by `MetaMathlibExt.IsLucasSequenceFirstKind`, a definition declared in [MathlibExt/NumberTheory/Recurrences/LucasSequenceFirstKind.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/LucasSequenceFirstKind.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html#is-lucas-sequence-first-kind).

## Lucas sequence of the first kind: value at zero

If $(u_n)_{n \ge 0}$ is the Lucas sequence
of the first kind with integer parameters $P$ and $Q$, then $u_0 = 0$.

Formalized by `MetaMathlibExt.IsLucasSequenceFirstKind.initialZero`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/LucasSequenceFirstKind.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/LucasSequenceFirstKind.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html#initial-zero).

## Lucas sequence of the first kind: value at one

If $(u_n)_{n \ge 0}$ is the Lucas sequence
of the first kind with integer parameters $P$ and $Q$, then $u_1 = 1$.

Formalized by `MetaMathlibExt.IsLucasSequenceFirstKind.initialOne`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/LucasSequenceFirstKind.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/LucasSequenceFirstKind.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html#initial-one).

## Lucas sequence of the first kind: the recurrence

If $(u_n)_{n \ge 0}$ is the Lucas
sequence of the first kind with integer parameters $P$ and $Q$, then
$u_{n+2} = P u_{n+1} - Q u_n$ for every natural number $n$.

Formalized by `MetaMathlibExt.IsLucasSequenceFirstKind.recurrenceStep`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/LucasSequenceFirstKind.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/LucasSequenceFirstKind.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html#recurrence-step).

## Nondegenerate Lucas pair

A pair of integers $(P, Q)$ is nondegenerate when $Q \ne 0$ and,
for all complex numbers $\alpha$ and $\beta$ with $\alpha + \beta = P$ and $\alpha \beta = Q$, the
quotient $\alpha / \beta$ is not a root of unity. Such $\alpha$ and $\beta$ are the two roots of
$x^2 - P x + Q$, in either order.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL13/Smyth/smyth2.tex>: lines 621-622 say a Lucas sequence is degenerate iff `Q = 0` or `α / β` is a root of unity, where `α` and `β` are the two roots of `x² - P x + Q`. Lines 114-122 establish `α + β = P` and `α * β = Q`.

Formalized by `MetaMathlibExt.IsNondegenerateLucasPair`, a definition declared in [MathlibExt/NumberTheory/Recurrences/NondegenerateLucasPair.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/NondegenerateLucasPair.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html#is-nondegenerate-lucas-pair).

## Addition formula $2U_{m+n} = U_m V_n + V_m U_n$ for Lucas sequences

For all integers
$P$ and $Q$ with $Q \neq 0$ and all natural numbers $m$ and $n$, the Lucas sequences
$U_n = U_n(P, Q)$ and $V_n = V_n(P, Q)$ satisfy $2U_{m+n} = U_m V_n + V_m U_n$.

This is the integer specialization of the paper's Proposition 1: its generalized Fibonacci
numbers $F_n$ and Lucas numbers $L_n$, with recurrence $x_{n+2} = a x_{n+1} + b x_n$, are
$U_n(a, -b)$ and $V_n(a, -b)$, and the paper allows real $a$ and $b$.

## Sources

- Vladimir V. Kruchinin and Maria Y. Perminova, "Identities and Hadamard Product of the Generalized Fibonacci, Lucas, Catalan, and Harmonic Numbers", Proposition 1.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.KruchininPerminovaHadamardWanted.two_mul_lucasU_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/KruchininPerminovaHadamardWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/KruchininPerminovaHadamardWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html#two-mul-lucas-u-add).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lucas sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/lucas-sequences)
