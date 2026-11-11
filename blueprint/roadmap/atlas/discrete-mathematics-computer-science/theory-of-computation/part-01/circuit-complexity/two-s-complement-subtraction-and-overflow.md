---
declaration: section
origin: cited
lean: Cslib.Circuits.adc_not_true, Cslib.Circuits.rippleCarryAdder_sub, Cslib.Circuits.rippleCarryAdder_noBorrow, Cslib.Circuits.carryLookaheadAdder_sub, Cslib.Circuits.saddOverflow_eq_carry_xor, Cslib.Circuits.overflowAdder, Cslib.Circuits.overflowAdder_eval_of_lt, Cslib.Circuits.overflowAdder_overflow
statement: formalized
proof: formalized
---

# Two's complement subtraction and overflow

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/two-s-complement-subtraction-and-overflow/index.html).

## Subtraction

## Subtraction by addition

Let $x$ and $y$ be $n$-bit words and let $\bar y$ be the bitwise
complement of $y$. Adding $x$ and $\bar y$ with carry in $1$ gives the $n$-bit result $x - y$
(the difference modulo $2^n$), and the carry out is $1$ exactly when there is no unsigned borrow,
that is, when $y \le x$ as unsigned integers.

Formalized by `Cslib.Circuits.adc_not_true`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/TwosComplement.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/TwosComplement.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/two-s-complement-subtraction-and-overflow/index.html#adc-not-true).

## The ripple-carry adder subtracts

Let $x$ and $y$ be $n$-bit words and let $\bar y$ be the
bitwise complement of $y$. Evaluate the $n$-bit ripple-carry adder, with XOR, AND and OR gates, on
the bits of $x$, the bits of $\bar y$ and carry in $1$. Then for every $i < n$, output $i$ is bit
$i$ (counting from the least significant bit $0$) of $x - y$ modulo $2^n$.

Formalized by `Cslib.Circuits.rippleCarryAdder_sub`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/TwosComplement.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/TwosComplement.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/two-s-complement-subtraction-and-overflow/index.html#ripple-carry-adder-sub).

## Carry out of ripple-carry subtraction

Let $x$ and $y$ be $n$-bit words and let $\bar y$ be
the bitwise complement of $y$. Evaluate the $n$-bit ripple-carry adder, with XOR, AND and OR
gates, on the bits of $x$, the bits of $\bar y$ and carry in $1$. Its carry out (output $n$) is $1$
exactly when there is no unsigned borrow in $x - y$, that is, when $y \le x$ as unsigned
integers.

Formalized by `Cslib.Circuits.rippleCarryAdder_noBorrow`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/TwosComplement.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/TwosComplement.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/two-s-complement-subtraction-and-overflow/index.html#ripple-carry-adder-no-borrow).

## The carry-lookahead adder subtracts

Let $x$ and $y$ be $n$-bit words, let $\bar y$ be the
bitwise complement of $y$, and let $K$ satisfy $n \le 2^K$. Evaluate the $n$-bit carry-lookahead
adder with $K$ levels, with XOR, AND and OR gates, on the bits of $x$, the bits of $\bar y$ and
carry in $1$. Then for every $i < n$, output $i$ is bit $i$ (counting from the least significant
bit $0$) of $x - y$ modulo $2^n$.

Formalized by `Cslib.Circuits.carryLookaheadAdder_sub`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/TwosComplement.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/TwosComplement.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/two-s-complement-subtraction-and-overflow/index.html#carry-lookahead-adder-sub).

## Signed overflow is the XOR of the last two carries

Let $n \ge 1$ and let $x$ and $y$ be
$n$-bit words. The two's complement addition $x + y$ overflows (the sum of the two's complement
values of $x$ and $y$ is at least $2^{n-1}$ or less than $-2^{n-1}$) exactly when the carry into
the sign bit $n - 1$ differs from the carry out of it, both carries taken when adding $x$ and $y$
with carry in $0$.

Formalized by `Cslib.Circuits.saddOverflow_eq_carry_xor`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/TwosComplement.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/TwosComplement.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/two-s-complement-subtraction-and-overflow/index.html#sadd-overflow-eq-carry-xor).

## The overflow adder

The $n$-bit overflow adder is the $n$-bit ripple-carry adder with one
extra XOR gate. It has the same $2n + 1$ inputs (the bits of the two summands, then the carry in)
and $5n + 1$ gates: the $5n$ gates of the ripple-carry adder, followed by an XOR of the carry into
bit $n - 1$ and the carry into bit $n$ (the carry out). Here the carry into bit $0$ is the carry
in, and for $n = 0$ the index $n - 1$ is read as $0$. Its $n + 2$ outputs are the ripple-carry
adder's $n$ sum bits and carry out, followed by the new gate, the signed-overflow flag.

Formalized by `Cslib.Circuits.overflowAdder`, a definition declared in [CSLibExt/Computability/Circuit/Arithmetic/TwosComplement.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/TwosComplement.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/two-s-complement-subtraction-and-overflow/index.html#overflow-adder).

## The overflow adder extends the ripple-carry adder

Let $x$ and $y$ be $n$-bit words and let
$c$ be a carry-in bit. Evaluate the $n$-bit overflow adder and the $n$-bit ripple-carry adder, with
XOR, AND and OR gates, on the bits of $x$, the bits of $y$ and $c$. Then for every $o < n + 1$,
output $o$ of the overflow adder equals output $o$ of the ripple-carry adder: the first $n + 1$
outputs (the $n$ sum bits and the carry out) agree.

Formalized by `Cslib.Circuits.overflowAdder_eval_of_lt`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/TwosComplement.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/TwosComplement.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/two-s-complement-subtraction-and-overflow/index.html#overflow-adder-eval-of-lt).

## The overflow flag

Let $n \ge 1$ and let $x$ and $y$ be $n$-bit words. Evaluate the $n$-bit
overflow adder, with XOR, AND and OR gates, on the bits of $x$, the bits of $y$ and carry in $0$.
Its last output (output $n + 1$) is $1$ exactly when the two's complement addition $x + y$
overflows, that is, when the sum of the two's complement values of $x$ and $y$ is at least
$2^{n-1}$ or less than $-2^{n-1}$.

Formalized by `Cslib.Circuits.overflowAdder_overflow`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/TwosComplement.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/TwosComplement.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/two-s-complement-subtraction-and-overflow/index.html#overflow-adder-overflow).

## Sum bits of the overflow adder

Let $x$ and $y$ be $n$-bit words. Evaluate the $n$-bit
overflow adder, with XOR, AND and OR gates, on the bits of $x$, the bits of $y$ and carry in $0$.
Then for every $i < n$, output $i$ is bit $i$ (counting from the least significant bit $0$) of
$x + y$ modulo $2^n$.

Formalized by `Cslib.Circuits.overflowAdder_sum`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/TwosComplement.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/TwosComplement.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/two-s-complement-subtraction-and-overflow/index.html#overflow-adder-sum).

## Size of the overflow adder

The $n$-bit overflow adder has $5n + 1$ gates.

This is one gate more than the $5n$ gates of the $n$-bit ripple-carry adder.

Formalized by `Cslib.Circuits.overflowAdder_size`, a theorem declared in [CSLibExt/Computability/Circuit/Arithmetic/TwosComplement.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Circuit/Arithmetic/TwosComplement.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/two-s-complement-subtraction-and-overflow/index.html#overflow-adder-size).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Two's complement subtraction and overflow](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/circuit-complexity/two-s-complement-subtraction-and-overflow/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/circuit-complexity/two-s-complement-subtraction-and-overflow)
