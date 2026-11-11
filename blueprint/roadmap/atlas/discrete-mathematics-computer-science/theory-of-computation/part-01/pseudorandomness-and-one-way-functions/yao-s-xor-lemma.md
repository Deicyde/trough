---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.YaoXOR.XORGate, MetaMathlibExt.Complexity.KeyTheorems.YaoXOR.xorCircuitEval, MetaMathlibExt.Complexity.KeyTheorems.YaoXOR.xorFlat, MetaMathlibExt.Complexity.KeyTheorems.YaoXOR.xorFold, MetaMathlibExt.Complexity.KeyTheorems.YaoXOR.xorOf, MetaMathlibExt.Complexity.KeyTheorems.YaoXOR.agreement, MetaMathlibExt.Complexity.KeyTheorems.YaoXOR.yao_xor_lemma
statement: formalized
---

# Yao's XOR lemma

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/yao-s-xor-lemma/index.html).

## Encoded gates

An encoded gate is a pair $(k, r)$ of a natural number $k$ (the gate kind)
and a list $r$ of natural numbers (its references), the shared (kind, references) encoding of
gates of flat Boolean circuits.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.YaoXOR.XORGate`, an abbreviation declared in [WantedExt/Complexity/KeyTheorems/YaoXORWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/YaoXORWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/yao-s-xor-lemma/index.html#xorgate).

## Gate values of an encoded circuit

For a list $C$ of encoded gates and a list $x$ of
Booleans of length $\ell$, the gate values of $C$ on $x$ are obtained by decoding each pair of $C$
to a gate of a flat Boolean circuit on $\ell$ inputs and evaluating the decoded circuit with the
assignment that gives input $i$ the value $x_i$; the result lists the values of all gates in
order. A pair referring to an input index $i \ge \ell$ decodes to the constant false.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.YaoXOR.xorCircuitEval`, a definition declared in [WantedExt/Complexity/KeyTheorems/YaoXORWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/YaoXORWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/yao-s-xor-lemma/index.html#xor-circuit-eval).

## Flattening blocks of bits

For $n > 0$ and $k$ blocks $x_0, \dots, x_{k-1}$ of $n$ bits
each, the flattened string has $nk$ bits, and its bit $i$ is bit $i \bmod n$ of the block
$x_{\lfloor i/n \rfloor}$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.YaoXOR.xorFlat`, a definition declared in [WantedExt/Complexity/KeyTheorems/YaoXORWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/YaoXORWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/yao-s-xor-lemma/index.html#xor-flat).

## XOR of finitely many bits

For $k$ bits $b_0, \dots, b_{k-1}$, their XOR is true if and
only if an odd number of the $b_i$ are true.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.YaoXOR.xorFold`, a definition declared in [WantedExt/Complexity/KeyTheorems/YaoXORWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/YaoXORWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/yao-s-xor-lemma/index.html#xor-fold).

## XOR of independent copies of a function

For natural numbers $n$ and $k$ and a Boolean
function $f$ on $n$ bits, the function $f^{\oplus k}$ takes $k$ blocks $x_0, \dots, x_{k-1}$
of $n$ bits each to $f(x_0) \oplus \cdots \oplus f(x_{k-1})$, which is true if and only if an
odd number of the values $f(x_i)$ are true.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.YaoXOR.xorOf`, a definition declared in [WantedExt/Complexity/KeyTheorems/YaoXORWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/YaoXORWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/yao-s-xor-lemma/index.html#xor-of).

## Agreement of a circuit with a Boolean function

Let $\alpha$ be a finite type, let $C$
be a circuit given as a list of encoded gates, let $g$ assign a Boolean to each $a \in \alpha$,
and let $\mathrm{enc}$ encode each $a \in \alpha$ as a list of Booleans. The agreement of $C$
with $g$ is the rational number $N / |\alpha|$ (which is $0$ when $\alpha$ is empty), where $N$
is the number of $a \in \alpha$ such that $C$ has at least one gate and the value of its last
gate, when $C$ is evaluated on the input list $\mathrm{enc}(a)$, equals $g(a)$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.YaoXOR.agreement`, a definition declared in [WantedExt/Complexity/KeyTheorems/YaoXORWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/YaoXORWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/yao-s-xor-lemma/index.html#agreement).

## Yao's XOR lemma: hardness amplification by XOR

There is a natural number $c$ such that
the following holds for all natural numbers $n \ge 1$ and $k$, every rational $\delta$ with
$0 < \delta \le 1/2$, every Boolean function $f$ on $n$ bits and every natural number $s$.
Suppose every circuit given as a list of at most $s$ encoded gates has agreement at most
$1 - \delta$ with $f$, where an input $x \in \{0,1\}^n$ is given to the circuit as its $n$ bits.
Then every circuit $C$ given as a list of encoded gates, whose number of gates $|C|$ satisfies
$|C| \cdot (k + 1)^c \le s$, has agreement at most $1/2 + (1 - 2\delta)^k / 2 + 1/(k + 1)$ with
the XOR $f^{\oplus k}$ of $k$ independent copies of $f$, where a $k$-tuple of $n$-bit blocks is
given to the circuit as its $nk$-bit flattening.

## Sources

- A. C. Yao, "Theory and applications of trapdoor functions", Proceedings of the Twenty-Third Annual Symposium on Foundations of Computer Science (FOCS 1982), 80-91.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.YaoXOR.yao_xor_lemma` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/YaoXORWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/YaoXORWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/yao-s-xor-lemma/index.html#yao-xor-lemma).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Yao's XOR lemma](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/yao-s-xor-lemma/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/yao-s-xor-lemma)
