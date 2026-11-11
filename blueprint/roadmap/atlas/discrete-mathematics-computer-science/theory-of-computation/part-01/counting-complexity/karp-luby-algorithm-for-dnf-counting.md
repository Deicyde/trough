---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.KarpLuby.dnfSat, MetaMathlibExt.Complexity.KeyTheorems.KarpLuby.dnfCountOf, MetaMathlibExt.Complexity.KeyTheorems.KarpLuby.karp_luby_dnf_counting
statement: formalized
---

# Karp–Luby algorithm for DNF counting

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/karp-luby-algorithm-for-dnf-counting/index.html).

## Satisfaction of a DNF formula

A DNF formula is a list of terms, each a list of literals
$(v, b)$ of a natural number $v$ (the variable) and a boolean $b$ (the polarity). An assignment $a$
of booleans to the natural numbers satisfies the formula when some term of it has $a(v) = b$ for
every literal $(v, b)$ of that term.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.KarpLuby.dnfSat`, a definition declared in [WantedExt/Complexity/KeyTheorems/KarpLubyWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/KarpLubyWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/karp-luby-algorithm-for-dnf-counting/index.html#dnf-sat).

## Number of satisfying assignments of an encoded DNF formula

For a bitstring $x$: if $x$
decodes, under the canonical bitstring encoding, to a pair $(u, \varphi)$ of a bitstring $u$ of
length $m$ and a DNF formula $\varphi$ all of whose literals have variables less than $m$, the
value at $x$ is the number of assignments of booleans to the variables $0, \dots, m - 1$ that
satisfy $\varphi$; otherwise the value is $0$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.KarpLuby.dnfCountOf`, a definition declared in [WantedExt/Complexity/KeyTheorems/KarpLubyWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/KarpLubyWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/karp-luby-algorithm-for-dnf-counting/index.html#dnf-count-of).

## Karp-Luby: FPRAS for DNF counting

For a bitstring $x$, let $N(x)$ be the number of
satisfying assignments of the DNF formula encoded by $x$: if $x$ decodes, under the canonical
bitstring encoding, to a pair $(u, \varphi)$ of a bitstring $u$ of length $m$ and a DNF formula
$\varphi$ whose variables are all less than $m$, then $N(x)$ is the number of assignments of
booleans to the variables $0, \dots, m - 1$ that satisfy $\varphi$, and otherwise $N(x) = 0$.
There are a polynomial $p$ with natural-number coefficients and a polynomial-time computable
function $E$ from triples of bitstrings to natural numbers such that for all bitstrings $x$ and
$w$ with $n = |w| \ge 1$ (the precision, given in unary), at least two thirds of the bitstrings
$r$ of length $p(|x| + n)$ satisfy $|E(x, r, w) - N(x)| \le N(x) / n$.

## Sources

- R. M. Karp and M. Luby, "Monte-Carlo algorithms for enumeration and reliability problems", Proceedings of the Twenty-Fourth Annual Symposium on Foundations of Computer Science (FOCS 1983), 56-64.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.KarpLuby.karp_luby_dnf_counting` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/KarpLubyWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/KarpLubyWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/karp-luby-algorithm-for-dnf-counting/index.html#karp-luby-dnf-counting).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Karp–Luby algorithm for DNF counting](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/karp-luby-algorithm-for-dnf-counting/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/counting-complexity/karp-luby-algorithm-for-dnf-counting)
