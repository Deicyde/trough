---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.GoldreichLevin.GLGate, MetaMathlibExt.Complexity.KeyTheorems.GoldreichLevin.glCircuitEval, MetaMathlibExt.Complexity.KeyTheorems.GoldreichLevin.glCircuitOutputs, MetaMathlibExt.Complexity.KeyTheorems.GoldreichLevin.invertSucc, MetaMathlibExt.Complexity.KeyTheorems.GoldreichLevin.xorDot, MetaMathlibExt.Complexity.KeyTheorems.GoldreichLevin.glPair, MetaMathlibExt.Complexity.KeyTheorems.GoldreichLevin.predictSucc, MetaMathlibExt.Complexity.KeyTheorems.GoldreichLevin.goldreich_levin
statement: formalized
---

# Goldreich–Levin theorem

8 results, 7 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/goldreich-levin-theorem/index.html).

## Serialized circuit gates

A serialized gate is a pair $(k, r)$ of a natural number $k$, the
kind of the gate, and a list $r$ of natural numbers, its references.

These pairs are read through the shared (kind, references) encoding of gates of flat Boolean
circuits.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.GoldreichLevin.GLGate`, an abbreviation declared in [WantedExt/Complexity/KeyTheorems/GoldreichLevinWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/GoldreichLevinWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/goldreich-levin-theorem/index.html#glgate).

## Gate values of a serialized circuit

For a list $C = (g_0, \dots, g_{m-1})$ of serialized
gates and a list $a = (a_0, \dots, a_{n-1})$ of Booleans, the gate values of $C$ on $a$ are the
list of gate values of the flat Boolean circuit on $n$ inputs whose $j$-th gate is decoded from the
(kind, references) pair $g_j$, evaluated on the assignment that gives input $i$ the value $a_i$.

A pair $(0, [i])$ with $i \ge n$ decodes to the constant false, so an input index out of range
reads as false.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.GoldreichLevin.glCircuitEval`, a definition declared in [WantedExt/Complexity/KeyTheorems/GoldreichLevinWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/GoldreichLevinWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/goldreich-levin-theorem/index.html#gl-circuit-eval).

## Outputs of a serialized circuit

For a list $C$ of serialized gates, a list $a$ of Booleans
and a natural number $k$, the outputs of $C$ on $a$ are the last $k$ entries of the gate values of
$C$ on $a$, or all of them when $C$ has fewer than $k$ gates.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.GoldreichLevin.glCircuitOutputs`, a definition declared in [WantedExt/Complexity/KeyTheorems/GoldreichLevinWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/GoldreichLevinWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/goldreich-levin-theorem/index.html#gl-circuit-outputs).

## Inversion success probability of a circuit

For a list $C$ of serialized gates and a map
$\pi$ from $n$-bit strings to $n$-bit strings, the inversion success probability of $C$ against
$\pi$ is the rational number $N / 2^n$, where $N$ is the number of $n$-bit strings $x$ such that
the outputs of $C$ on input $\pi(x)$, taken as its last $n$ gate values, are exactly $x$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.GoldreichLevin.invertSucc`, a definition declared in [WantedExt/Complexity/KeyTheorems/GoldreichLevinWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/GoldreichLevinWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/goldreich-levin-theorem/index.html#invert-succ).

## Inner product modulo 2

For $n$-bit strings $x$ and $r$, their inner product modulo 2 is
true if and only if the number of indices $i < n$ with $x_i$ and $r_i$ both true is odd, that is,
$\langle x, r \rangle = \sum_{i < n} x_i r_i \bmod 2$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.GoldreichLevin.xorDot`, a definition declared in [WantedExt/Complexity/KeyTheorems/GoldreichLevinWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/GoldreichLevinWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/goldreich-levin-theorem/index.html#xor-dot).

## Concatenation of two bitstrings

For $n$-bit strings $y$ and $r$, their concatenation is the
$2n$-bit string whose bit $i$ is $y_i$ for $i < n$ and $r_{i - n}$ for $n \le i < 2n$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.GoldreichLevin.glPair`, a definition declared in [WantedExt/Complexity/KeyTheorems/GoldreichLevinWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/GoldreichLevinWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/goldreich-levin-theorem/index.html#gl-pair).

## Prediction success probability for the inner-product bit

For a list $C$ of serialized
gates and a map $\pi$ from $n$-bit strings to $n$-bit strings, the prediction success probability
of $C$ against $\pi$ is the rational number $N / 2^{2n}$, where $N$ is the number of pairs
$(x, r)$ of $n$-bit strings such that $C$ has at least one gate and the value of its last gate on
the concatenation of $\pi(x)$ and $r$, a $2n$-bit input, equals the inner product of $x$ and $r$
modulo 2.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.GoldreichLevin.predictSucc`, a definition declared in [WantedExt/Complexity/KeyTheorems/GoldreichLevinWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/GoldreichLevinWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/goldreich-levin-theorem/index.html#predict-succ).

## Goldreich-Levin: hardcore predicate from one-way permutations

Let $\pi$ be a family of
bijections $\pi_n$ of the set of $n$-bit strings, one for each natural number $n$. Suppose that
$\pi$ is computable by polynomial-size circuits: there is a polynomial $q$ with natural number
coefficients such that for every $n$ some list of at most $q(n)$ serialized gates has, on every
$n$-bit string $x$, outputs (its last $n$ gate values) equal to $\pi_n(x)$. Suppose also that $\pi$
is one-way: for every polynomial $p$ with natural number coefficients and every family $(C_n)$ of
lists of serialized gates with at most $p(n)$ gates in $C_n$ for all $n$, the inversion success
probability of $C_n$ against $\pi_n$ is a negligible function of $n$. Then for every polynomial
$p$ with natural number coefficients and every family $(C'_n)$ of lists of serialized gates with
at most $p(n)$ gates in $C'_n$ for all $n$, the function $n \mapsto \max(0, s_n - 1/2)$ is
negligible, where $s_n$ is the prediction success probability of $C'_n$ against $\pi_n$ for the
inner product modulo 2.

## Sources

- O. Goldreich and L. A. Levin, "A hard-core predicate for all one-way functions", Proceedings of the Twenty-First Annual ACM Symposium on Theory of Computing (STOC 1989), 25-32.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.GoldreichLevin.goldreich_levin` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/GoldreichLevinWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/GoldreichLevinWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/goldreich-levin-theorem/index.html#goldreich-levin).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Goldreich–Levin theorem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/goldreich-levin-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/goldreich-levin-theorem)
