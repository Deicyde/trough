---
declaration: section
origin: cited
lean: Cslib.Circuits.ArithGate, Cslib.Circuits.arithSignature, Cslib.Circuits.arithInterpretation, Cslib.Circuits.binLine, Cslib.Circuits.RippleCarry.carryWire, Cslib.Circuits.RippleCarry.line, Cslib.Circuits.rcaProgram, Cslib.Circuits.rippleCarryAdder
statement: formalized
proof: formalized
---

# Ripple-carry adder

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/ripple-carry-adder/index.html).

## Circuits

## Arithmetic gate symbols

The gate symbols of arithmetic circuits are exactly three:
XOR, AND and OR.

Formalized by `Cslib.Circuits.ArithGate`, an inductive type declared in [CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/ripple-carry-adder/index.html#arith-gate).

## Arithmetic basis

The circuit signature whose operation symbols are the three arithmetic
gate symbols XOR, AND and OR, each of arity $2$.

Formalized by `Cslib.Circuits.arithSignature`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/ripple-carry-adder/index.html#arith-signature).

## Boolean interpretation of the arithmetic gates

The interpretation of the arithmetic
basis in the Booleans: on a first argument $a$ and a second argument $b$, the XOR gate computes
$a \oplus b$, the AND gate computes $a \wedge b$, and the OR gate computes $a \vee b$.

Formalized by `Cslib.Circuits.arithInterpretation`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/ripple-carry-adder/index.html#arith-interpretation).

## Binary gate line

For an arithmetic gate symbol $\mathrm{op}$ and wires $u$ and $v$ of a
circuit with $m$ inputs (each wire is an input or one of the $g$ preceding gates), the gate that
applies $\mathrm{op}$ to $u$ as its first argument and $v$ as its second.

Formalized by `Cslib.Circuits.binLine`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/ripple-carry-adder/index.html#bin-line).

## Carry wire

For natural numbers $n$, $g$ and $i$ with $5i \le g$, the wire carrying the
carry into bit $i$ of the $n$-bit adder, in a circuit with $2n + 1$ inputs and $g$ gates: for
$i = 0$ it is the carry-in input (input $2n$), and for $i \ne 0$ it is gate $5i - 1$, the
carry-out gate of bit $i - 1$.

Formalized by `Cslib.Circuits.RippleCarry.carryWire`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/ripple-carry-adder/index.html#carry-wire).

## Gates of the ripple-carry adder

For natural numbers $n$ and $g$ with $g < 5n$, gate $g$ of
the $n$-bit ripple-carry adder is the following binary gate of the arithmetic basis, whose
arguments are among the $2n + 1$ inputs and the $g$ gates before it. Write $g = 5i + r$ with
$0 \le r < 5$, let $a$ be input $i$ and $b$ input $n + i$, and let $c$ be the carry into bit $i$:
input $2n$ if $i = 0$ and gate $5i - 1$ otherwise. Gate $g$ is the XOR gate with first argument
$a$ and second argument $b$ if $r = 0$, the XOR gate with first argument gate $g - 1$ and second
argument $c$ if $r = 1$, the AND gate with first argument $a$ and second argument $b$ if $r = 2$,
the AND gate with first argument gate $g - 3$ and second argument $c$ if $r = 3$, and the OR gate
with first argument gate $g - 2$ and second argument gate $g - 1$ if $r = 4$.

Formalized by `Cslib.Circuits.RippleCarry.line`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/ripple-carry-adder/index.html#line).

## Gate program of the ripple-carry adder

For $g \le 5n$, the straight-line program over the
arithmetic basis with $2n + 1$ inputs whose gates are, in order, gates $0, 1, \dots, g - 1$ of
the $n$-bit ripple-carry adder; for $g = 0$ it is the empty program.

Formalized by `Cslib.Circuits.rcaProgram`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/ripple-carry-adder/index.html#rca-program).

## Ripple-carry adder

The $n$-bit ripple-carry adder is the circuit with $2n + 1$ inputs,
$5n$ binary gates, each an XOR, AND or OR gate, and $n + 1$ outputs, built as follows. Write $a_i$
for input $i$, $b_i$ for input $n + i$ and $c_0$ for input $2n$, where $i < n$. For each $i < n$,
gates $g_{5i}, \dots, g_{5i+4}$ form a full adder for position $i$: $g_{5i} = a_i \oplus b_i$,
$g_{5i+1} = g_{5i} \oplus c_i$, $g_{5i+2} = a_i \wedge b_i$, $g_{5i+3} = g_{5i} \wedge c_i$ and
$g_{5i+4} = g_{5i+2} \vee g_{5i+3}$, where the carry $c_i$ is input $2n$ when $i = 0$ and gate
$g_{5i-1}$ otherwise. For $i < n$, output $i$ is gate $g_{5i+1}$, and output $n$ is the carry out
$c_n$: input $2n$ when $n = 0$, otherwise gate $g_{5n-1}$.

Formalized by `Cslib.Circuits.rippleCarryAdder`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/ripple-carry-adder/index.html#ripple-carry-adder).

## Input of the ripple-carry adder

For $n$-bit vectors $x$ and $y$ and a bit $c$, the
assignment to the $2n + 1$ inputs of the $n$-bit adder: for $j < n$, input $j$ is bit $j$ of
$x$; for $n \le j < 2n$, input $j$ is bit $j - n$ of $y$; and input $2n$ is $c$. Bit $0$ is the
least significant bit.

Formalized by `Cslib.Circuits.rcaInput`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/ripple-carry-adder/index.html#rca-input).

## Gate-value specification of the ripple-carry adder

Let $x, y$ be $n$-bit vectors, $c$ a
bit and $j$ a natural number, and write $j = 5i + r$ with $0 \le r < 5$. Let $x_i$ and $y_i$ be
bit $i$ of $x$ and $y$ (bit $0$ is the least significant, and bits at positions $i \ge n$ are $0$),
and let $c_i$ be the carry into position $i$ when $x$, $y$ and $c$ are added: reading $x$ and $y$
as natural numbers, $c_i = 1$ exactly when $(x \bmod 2^i) + (y \bmod 2^i) + c \ge 2^i$. The
specification assigns to $j$ the bit $x_i \oplus y_i$ if $r = 0$, $(x_i \oplus y_i) \oplus c_i$
if $r = 1$, $x_i \wedge y_i$ if $r = 2$, $(x_i \oplus y_i) \wedge c_i$ if $r = 3$, and $c_{i+1}$
if $r = 4$.

Formalized by `Cslib.Circuits.rcaSpec`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/ripple-carry-adder/index.html#rca-spec).

## Value of the carry wire

Let $x$ and $y$ be $n$-bit vectors, $c$ a bit, and $i$ and $g$
natural numbers with $5i \le g$. Suppose the first $g$ gates are given values $v_0, \dots, v_{g-1}$
with each $v_j$ equal to the specified value of gate $j$ of the adder on $x$, $y$, $c$. Then, on
the adder input for $x$, $y$, $c$ and with these gate values, the carry wire into bit $i$ carries
the carry into bit $i$ of $x + y + c$: it is true exactly when
$(x \bmod 2^i) + (y \bmod 2^i) + c \ge 2^i$, reading $x$, $y$ and $c$ as natural numbers.

Formalized by `Cslib.Circuits.carryWire_value`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/ripple-carry-adder/index.html#carry-wire-value).

## Gate values of the ripple-carry adder

Let $x$ and $y$ be $n$-bit vectors and $c$ a bit.
For every $g \le 5n$ and every $j < g$, evaluating the first $g$ gates of the $n$-bit adder with
the Boolean interpretation of the arithmetic gates on the adder input for $x$, $y$, $c$ gives
gate $j$ its specified value on $x$, $y$, $c$.

Formalized by `Cslib.Circuits.rcaProgram_eval`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/ripple-carry-adder/index.html#rca-program-eval).

## Sum bits of the ripple-carry adder

Let $x, y$ be $n$-bit vectors, $c$ a bit and $i < n$,
and evaluate the $n$-bit ripple-carry adder, with its gates read as Boolean XOR, AND and OR, on the
input whose entry $j$ is bit $j$ of $x$ and entry $n + j$ is bit $j$ of $y$ for $j < n$ (bit $0$
being the least significant), and whose entry $2n$ is $c$. Its output number $i$ (outputs being
numbered from $0$) is bit $i$ of the $n$-bit sum $(x + y + c) \bmod 2^n$, reading $x$ and $y$ as
natural numbers below $2^n$.

Formalized by `Cslib.Circuits.rippleCarryAdder_sum`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/ripple-carry-adder/index.html#ripple-carry-adder-sum).

## Carry out of the ripple-carry adder

Let $x, y$ be $n$-bit vectors and $c$ a bit, and
evaluate the $n$-bit ripple-carry adder, with its gates read as Boolean XOR, AND and OR, on the
input whose entry $j$ is bit $j$ of $x$ and entry $n + j$ is bit $j$ of $y$ for $j < n$ (bit $0$
being the least significant), and whose entry $2n$ is $c$. Its output number $n$ (the last,
outputs being numbered from $0$) is the carry out of $x + y + c$: reading $x$ and $y$ as natural
numbers below $2^n$, it is $1$ exactly when $x + y + c \ge 2^n$.

Formalized by `Cslib.Circuits.rippleCarryAdder_carry`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/ripple-carry-adder/index.html#ripple-carry-adder-carry).

## Size of the ripple-carry adder

The $n$-bit ripple-carry adder has exactly $5n$ gates.

Formalized by `Cslib.Circuits.rippleCarryAdder_size`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/RippleCarry.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/ripple-carry-adder/index.html#ripple-carry-adder-size).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ripple-carry adder](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/ripple-carry-adder/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/circuit-complexity/ripple-carry-adder)
