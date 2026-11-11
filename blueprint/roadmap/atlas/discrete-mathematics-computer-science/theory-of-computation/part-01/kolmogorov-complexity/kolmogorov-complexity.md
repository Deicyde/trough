---
declaration: section
origin: cited
lean: Cslib.Kolmogorov.run, Cslib.Kolmogorov.describe, Cslib.Kolmogorov.U, Cslib.Kolmogorov.K, Cslib.Kolmogorov.K_le, Cslib.Kolmogorov.exists_length_eq_K, Cslib.Kolmogorov.K_le_length_add, Cslib.Kolmogorov.partrec_U
statement: formalized
proof: formalized
---

# Kolmogorov complexity: its own results

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/index.html).

Algorithmic information content of individual strings: universal description methods, incompressible strings, non-computability and upper semicomputability of Kolmogorov complexity.

## Running a program on a binary string

For a code $c$ of a partial recursive function on
the natural numbers and a binary string $w$, running $c$ on $w$ evaluates $c$ at the number
encoding $w$; if this halts with output $m$, the result is the binary string encoded by $m$. The
result is undefined when the evaluation does not halt or $m$ encodes no binary string.

Formalized by `Cslib.Kolmogorov.run`, a definition declared in [CSLibExt/Computability/Kolmogorov/Basic.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Kolmogorov/Basic.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/index.html#run).

## Description of a code running on an input

Let $c$ be a code for a partial recursive
function and let $n$ be its number in the standard encoding of codes as natural numbers. For a
binary string $w$, the description of $c$ running on $w$ is the binary string $1^n 0 w$, that is,
$n$ ones, then a zero, then $w$.

Formalized by `Cslib.Kolmogorov.describe`, a definition declared in [CSLibExt/Computability/Kolmogorov/Basic.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Kolmogorov/Basic.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/index.html#describe).

## The universal description method

A description `1ⁿ 0 w` runs code number `n` on `w`;
a string of `1`s describes nothing.

Formalized by `Cslib.Kolmogorov.U`, a definition declared in [CSLibExt/Computability/Kolmogorov/Basic.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Kolmogorov/Basic.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/index.html#u).

## Kolmogorov complexity

The Kolmogorov complexity $K(x)$ of a binary string $x$ is the
least length of a binary string $p$ such that $U(p)$ is defined and equals $x$, where $U$ is the
universal description method.

Formalized by `Cslib.Kolmogorov.K`, a definition declared in [CSLibExt/Computability/Kolmogorov/Basic.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Kolmogorov/Basic.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/index.html#k).

## A description bounds the complexity

Let $x$ and $p$ be binary strings such that $U(p)$ is
defined and equals $x$, where $U$ is the universal description method. Then the Kolmogorov
complexity of $x$ is at most the length of $p$: $K(x) \le |p|$.

Formalized by `Cslib.Kolmogorov.K_le`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Basic.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Kolmogorov/Basic.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/index.html#k-le).

## Shortest descriptions exist

For every binary string $x$ there is a binary string $p$
whose length is the Kolmogorov complexity $K(x)$ and such that $U(p)$ is defined and equals $x$,
where $U$ is the universal description method.

Formalized by `Cslib.Kolmogorov.exists_length_eq_K`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Basic.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Kolmogorov/Basic.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/index.html#exists-length-eq-k).

## Complexity is at most the length plus a constant

There is a natural number $c$ such that
every binary string $x$ satisfies $K(x) \le |x| + c$, where $K(x)$ is the Kolmogorov complexity
of $x$ and $|x|$ is its length.

Formalized by `Cslib.Kolmogorov.K_le_length_add`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Basic.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Kolmogorov/Basic.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/index.html#k-le-length-add).

## The universal description method is partial recursive

The universal description
method, as a partial function from binary strings to binary strings, is partial recursive.

Formalized by `Cslib.Kolmogorov.partrec_U`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Basic.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Kolmogorov/Basic.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/index.html#partrec-u).

## Every partial recursive description method has a code

Let $D$ be a partial recursive
function from binary strings to binary strings. Then there is a code $c$ for a partial recursive
function such that running $c$ equals $D$ as a partial function: for every binary string $w$,
running $c$ on $w$ is defined exactly when $D(w)$ is, and then has the same value.

Formalized by `Cslib.Kolmogorov.exists_run_eq`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Basic.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Kolmogorov/Basic.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/index.html#exists-run-eq).

## Optimality (the invariance theorem)

Let $D$ be a partial recursive function from binary
strings to binary strings, viewed as a description method. Then there is a natural number $c$
such that for all binary strings $x$ and $p$ for which $D(p)$ is defined and equals $x$, the
Kolmogorov complexity of $x$ satisfies $K(x) \le |p| + c$, where $|p|$ is the length of $p$.

Formalized by `Cslib.Kolmogorov.exists_K_le_of_partrec`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Basic.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Kolmogorov/Basic.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/index.html#exists-k-le-of-partrec).

## Doubling costs a constant

There is a natural number $c$ such that for every binary string
$x$, the Kolmogorov complexity of the concatenation $xx$ of $x$ with itself satisfies
$K(xx) \le K(x) + c$.

Formalized by `Cslib.Kolmogorov.K_append_self_le`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Basic.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Kolmogorov/Basic.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/index.html#k-append-self-le).

## Pair description

For binary strings $p$ and $q$, the pair description of $p$ and $q$ is
the binary string $1^{|p|} 0 p q$, that is, $|p|$ ones, where $|p|$ is the length of $p$, then a
zero, then $p$, then $q$.

The prefix $1^{|p|} 0$ records the length of $p$, so the string splits back into $p$ and $q$.

Formalized by `Cslib.Kolmogorov.pairDescribe`, a definition declared in [CSLibExt/Computability/Kolmogorov/Basic.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Kolmogorov/Basic.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/index.html#pair-describe).

## Reading pair descriptions

Write a binary string $s$ as $1^n s'$, where $n$ is the number
of leading $1$s, and let $r$ be $s'$ without its first letter ($r$ is empty when $s'$ is). Let
$r_1$ be the first $\min(n, |r|)$ letters of $r$ and $r_2$ the remaining ones. The pair reader
maps $s$ to the concatenation $U(r_1)\,U(r_2)$, where $U$ is the universal description method,
and is undefined when $U(r_1)$ or $U(r_2)$ is undefined. On a pair description $1^n 0 r$ with
$|r| \ge n$, this is the concatenation of what the first $n$ letters of $r$ and the rest
describe.

Formalized by `Cslib.Kolmogorov.pairU`, a definition declared in [CSLibExt/Computability/Kolmogorov/Basic.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Kolmogorov/Basic.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/index.html#pair-u).

## Concatenation costs at most twice the first part

There is a natural number $c$ such that
for all binary strings $x$ and $y$, the Kolmogorov complexity of their concatenation $xy$
satisfies $K(xy) \le 2K(x) + K(y) + c$.

Formalized by `Cslib.Kolmogorov.K_append_le`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Basic.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Kolmogorov/Basic.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/index.html#k-append-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kolmogorov complexity](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/kolmogorov-complexity)
