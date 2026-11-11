---
declaration: section
origin: cited
lean: MathlibExt.TheoryOfComputation.IntegerMultiplicationWanted.IntegerMultiplication.encodeProd, MathlibExt.TheoryOfComputation.IntegerMultiplicationWanted.IntegerMultiplication.encodeNatBinary, MathlibExt.TheoryOfComputation.IntegerMultiplicationWanted.IntegerMultiplication.theorem_1_1
statement: formalized
---

# Integer multiplication in time O(n log n)

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/integer-multiplication-in-time-o-n-log-n/index.html).

## Encoding of pairs

Given encodings $e_A : A \to \Gamma_A^*$ and $e_B : B \to \Gamma_B^*$
of types $A$ and $B$ as lists over alphabets $\Gamma_A$ and $\Gamma_B$, and a new symbol $\bot$
in neither alphabet, a pair $(a, b)$ is encoded as a list over the alphabet
$(\Gamma_A \cup \{\bot\}) \times (\Gamma_B \cup \{\bot\})$ by zipping: its length is the larger of
the lengths of $e_A(a)$ and $e_B(b)$, and its $i$-th entry is the pair of the $i$-th entries of
$e_A(a)$ and $e_B(b)$, where an entry missing from the shorter list is replaced by $\bot$.

Formalized by `MathlibExt.TheoryOfComputation.IntegerMultiplicationWanted.IntegerMultiplication.encodeProd`, a definition declared in [WantedExt/TheoryOfComputation/IntegerMultiplicationWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/IntegerMultiplicationWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/integer-multiplication-in-time-o-n-log-n/index.html#encode-prod).

## Binary encoding of natural numbers

The binary encoding of a natural number $n$ is the
list of its base-$2$ digits, least significant first, with the digit $1$ written as the Boolean
value true and the digit $0$ as false. The list has no trailing zero digit, so $0$ is encoded by
the empty list.

Unlike the unary encoding, this encoding of $n > 0$ has length $\lfloor \log_2 n \rfloor + 1$,
which is the size model of the bit-complexity bound $O(n \log n)$ for integer multiplication;
with the unary encoding that bound could not hold.

## Sources

- Lean variant; this replaces the upstream unary encoding `Computability.encodeNat`.

Formalized by `MathlibExt.TheoryOfComputation.IntegerMultiplicationWanted.IntegerMultiplication.encodeNatBinary`, a definition declared in [WantedExt/TheoryOfComputation/IntegerMultiplicationWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/IntegerMultiplicationWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/integer-multiplication-in-time-o-n-log-n/index.html#encode-nat-binary).

## Harvey–van der Hoeven: integer multiplication in time $O(n \log n)$

There is a
multi-stack Turing machine with finite alphabets and a function $t : \mathbb{N} \to \mathbb{N}$
such that, for all natural numbers $x$ and $y$, the machine started on the encoding of the pair
$(x, y)$ (the binary encodings of $x$ and $y$, zipped) halts within $t(\ell)$ steps with the
binary encoding of $xy$, where $\ell$ is the length of the input, and $t(n) = O(n \log n)$ as
$n \to \infty$.

## Sources

- D. Harvey and J. van der Hoeven, `Integer multiplication in time O(n log n)`, Annals of Math, 193 (2) 2021. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_integer_multiplication` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.TheoryOfComputation.IntegerMultiplicationWanted.IntegerMultiplication.theorem_1_1` is written with `theorem_wanted` in [WantedExt/TheoryOfComputation/IntegerMultiplicationWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/IntegerMultiplicationWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/integer-multiplication-in-time-o-n-log-n/index.html#theorem-1-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integer multiplication in time O(n log n)](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/integer-multiplication-in-time-o-n-log-n/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/algebraic-complexity/integer-multiplication-in-time-o-n-log-n)
