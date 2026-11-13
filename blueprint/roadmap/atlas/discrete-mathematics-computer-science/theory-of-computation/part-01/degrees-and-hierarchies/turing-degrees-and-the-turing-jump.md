---
declaration: section
origin: cited
lean: Cslib.Decidability.OracleCode, Cslib.Decidability.encodeOracleCode, Cslib.Decidability.encodeOracleCode_injective, Cslib.Decidability.pair_ge_fst, Cslib.Decidability.pair_ge_snd, Cslib.Decidability.pair_four_gt, Cslib.Decidability.pair_gt_snd_of_pos, Cslib.Decidability.unpair_fst_le
statement: formalized
proof: formalized
---

# Turing degrees and the Turing jump

40 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html).

## Oracle codes

Oracle codes are the finite programs built from the basic codes
$\mathtt{zero}$, $\mathtt{succ}$, $\mathtt{left}$, $\mathtt{right}$ and $\mathtt{oracle}$ by the
binary constructors $\mathtt{pair}$, $\mathtt{comp}$ and $\mathtt{prec}$ and the unary constructor
$\mathtt{rfind}$. They are the codes for partial recursive functions (constant zero, successor,
the two unpairing projections, pairing, composition, primitive recursion and unbounded search)
extended by an instruction $\mathtt{oracle}$ that queries the oracle on its input.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, §2 (oracle computations).

Formalized by `Cslib.Decidability.OracleCode`, an inductive type declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#oracle-code).

## The Gödel numbering of oracle codes

Write $\langle a, b \rangle$ for the pairing of
natural numbers equal to $b^2 + a$ if $a < b$ and to $a^2 + a + b$ otherwise. The code number
$\ulcorner c \urcorner$ of an oracle code $c$ is defined by recursion on $c$: $\mathsf{zero}$,
$\mathsf{succ}$, $\mathsf{left}$, $\mathsf{right}$ and $\mathsf{oracle}$ have code numbers
$\langle 0, 0 \rangle$, $\langle 1, 0 \rangle$, $\langle 2, 0 \rangle$, $\langle 3, 0 \rangle$ and
$\langle 8, 0 \rangle$; $\mathsf{pair}(a, b)$, $\mathsf{comp}(a, b)$ and $\mathsf{prec}(a, b)$
have code numbers $\langle 4, \langle \ulcorner a \urcorner, \ulcorner b \urcorner \rangle \rangle$,
$\langle 5, \langle \ulcorner a \urcorner, \ulcorner b \urcorner \rangle \rangle$ and
$\langle 6, \langle \ulcorner a \urcorner, \ulcorner b \urcorner \rangle \rangle$; and
$\mathsf{rfind}(a)$ has code number $\langle 7, \ulcorner a \urcorner \rangle$.

This numbering is an injection into $\mathbb{N}$.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (Gödel numberings).

Formalized by `Cslib.Decidability.encodeOracleCode`, a definition declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#encode-oracle-code).

## The Gödel numbering of oracle codes is injective

**The Gödel numbering of oracle codes is injective.**

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (Gödel numberings).

Formalized by `Cslib.Decidability.encodeOracleCode_injective`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#encode-oracle-code-injective).

## Pairing is at least its first argument

Let $\langle a, b \rangle$ denote the pairing of
natural numbers, equal to $b^2 + a$ if $a < b$ and to $a^2 + a + b$ otherwise. For all natural
numbers $a$ and $b$, $a \le \langle a, b \rangle$.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.3 (pairing functions).

Formalized by `Cslib.Decidability.pair_ge_fst`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#pair-ge-fst).

## Pairing is at least its second argument

Let $\langle a, b \rangle$ denote the pairing of
natural numbers, equal to $b^2 + a$ if $a < b$ and to $a^2 + a + b$ otherwise. For all natural
numbers $a$ and $b$, $b \le \langle a, b \rangle$.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.3 (pairing functions).

Formalized by `Cslib.Decidability.pair_ge_snd`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#pair-ge-snd).

## Pairing with $4$ strictly increases the second argument

Let $\langle a, b \rangle$ denote
the pairing of natural numbers, equal to $b^2 + a$ if $a < b$ and to $a^2 + a + b$ otherwise.
For every natural number $x$, $x < \langle 4, x \rangle$.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.3 (pairing functions).

Formalized by `Cslib.Decidability.pair_four_gt`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#pair-four-gt).

## Pairing with a positive first argument strictly increases the second

Let
$\langle a, b \rangle$ denote the pairing of natural numbers, equal to $b^2 + a$ if $a < b$ and to
$a^2 + a + b$ otherwise. For all natural numbers $t$ and $x$ with $t \ge 1$,
$x < \langle t, x \rangle$.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.3 (pairing functions).

Formalized by `Cslib.Decidability.pair_gt_snd_of_pos`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#pair-gt-snd-of-pos).

## The first unpairing component is at most the number

Let
$\mathrm{pair} : \mathbb{N} \times \mathbb{N} \to \mathbb{N}$ be the pairing bijection with
$\mathrm{pair}(a, b) = b^2 + a$ if $a < b$ and $\mathrm{pair}(a, b) = a^2 + a + b$ otherwise.
For every natural number $n$, the first component of $\mathrm{pair}^{-1}(n)$ is at most $n$.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.3 (pairing functions).

Formalized by `Cslib.Decidability.unpair_fst_le`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#unpair-fst-le).

## The second unpairing component is at most the number

Let
$\mathrm{pair} : \mathbb{N} \times \mathbb{N} \to \mathbb{N}$ be the pairing bijection with
$\mathrm{pair}(a, b) = b^2 + a$ if $a < b$ and $\mathrm{pair}(a, b) = a^2 + a + b$ otherwise.
For every natural number $n$, the second component of $\mathrm{pair}^{-1}(n)$ is at most $n$.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.3 (pairing functions).

Formalized by `Cslib.Decidability.unpair_snd_le`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#unpair-snd-le).

## Depth of an oracle code

Leaves have depth `0`; each constructor adds
one to the maximum depth of its children.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (Gödel numberings; size bounds).

Formalized by `Cslib.Decidability.oracleCodeDepth`, a definition declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#oracle-code-depth).

## Fuel-indexed decoder of oracle codes

Write $\langle a, b \rangle$ for the pairing
bijection $\mathbb{N} \times \mathbb{N} \to \mathbb{N}$ of the Gödel numbering. Given a fuel $f$,
a tag $t$ and a payload $p$, the decoder either returns an oracle code or fails; to decode a
number $n = \langle n_1, n_2 \rangle$ with fuel $f$ means to run it with fuel $f$, tag $n_1$ and
payload $n_2$. With fuel $0$ it fails. With fuel $f + 1$, writing $p = \langle p_1, p_2 \rangle$:
if $p = 0$ and $t$ is $0$, $1$, $2$, $3$ or $8$, it returns the instruction zero, successor, left
projection, right projection or oracle query respectively; if $t$ is $4$, $5$ or $6$, it decodes
$p_1$ and $p_2$ with fuel $f$ and, when these give codes $a$ and $b$, returns the pairing,
composition or primitive recursion code built from $a$ and $b$ respectively, failing otherwise;
if $t = 7$, it decodes $p$ with fuel $f$ and, when this gives a code $a$, returns the unbounded
search code built from $a$, failing otherwise; in all other cases it fails.

The recursion is structural in the fuel and uses no classical choice, so the decoder is a
computable function; with enough fuel it inverts the Gödel numbering of oracle codes.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (Gödel numberings; decoding).

Formalized by `Cslib.Decidability.decodeOracleCodeFuel`, a definition declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#decode-oracle-code-fuel).

## The fuel-indexed decoder inverts the encoder

Write $\langle a, b \rangle$ for the pairing
bijection $\mathbb{N} \times \mathbb{N} \to \mathbb{N}$ of the Gödel numbering. Let $c$ be an
oracle code with Gödel number $\langle t, p \rangle$. For every fuel $f$ strictly greater than the
depth of $c$, the fuel-indexed decoder with fuel $f$, tag $t$ and payload $p$ returns $c$.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (Gödel numberings; decoding).

Formalized by `Cslib.Decidability.decodeOracleCodeFuel_complete`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#decode-oracle-code-fuel-complete).

## Decoder soundness

Write $\langle a, b \rangle$ for the pairing bijection
$\mathbb{N} \times \mathbb{N} \to \mathbb{N}$ of the Gödel numbering. For every fuel $f$, tag
$t$, payload $p$ and oracle code $c$, if the fuel-indexed decoder with fuel $f$, tag $t$ and
payload $p$ returns $c$, then the Gödel number of $c$ is $\langle t, p \rangle$.

Together with the fact that the fuel-indexed decoder inverts the encoder at any fuel above the
code depth, this says that the decoder is exactly the inverse of the Gödel numbering on its image.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (Gödel numberings; decoding).

Formalized by `Cslib.Decidability.decodeOracleCodeFuel_sound`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#decode-oracle-code-fuel-sound).

## Depth is bounded by the code number

For every oracle code $c$, the depth of $c$ is at most
the code number of $c$ under the Gödel numbering of oracle codes.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (Gödel numberings; size bounds).

Formalized by `Cslib.Decidability.oracleCodeDepth_le_encode`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 428](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L428). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#oracle-code-depth-le-encode).

## Decoding oracle codes

The computable decoder for the Gödel numbering of oracle codes
sends a natural number $n$ to the result of the fuel-indexed decoder with fuel $n + 1$, tag $n_1$
and payload $n_2$, where $(n_1, n_2)$ is the unpairing of $n$; the result is either an oracle code
or undefined. The fuel $n + 1$ is more than enough, since the depth of an oracle code is at most
its code number.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (Gödel numberings; decoding).

Formalized by `Cslib.Decidability.decodeOracleCode`, a definition declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 479](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L479). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#decode-oracle-code).

## The computable decoder inverts the encoder

For every oracle code $c$, the computable
decoder applied to the Gödel number of $c$ returns $c$.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (Gödel numberings; decoding).

Formalized by `Cslib.Decidability.decodeOracleCode_encode`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 485](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L485). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#decode-oracle-code-encode).

## The fuel-indexed decoder agrees with the total decoder

**The fuel-indexed decoder agrees with the total decoder** whenever the
code number is below the fuel: decoding `(tag, payload)` at any fuel above
the code number gives the same result as decoding the code number itself.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (Gödel numberings; decoding).

Formalized by `Cslib.Decidability.decodeOracleCodeFuel_eq_decode`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 497](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L497). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#decode-oracle-code-fuel-eq-decode).

## The decoder, by cases on the tag

Write $\langle t, p \rangle$ for the pairing of natural
numbers used by the Gödel numbering of oracle codes, $(p_1, p_2)$ for the unpairing of $p$ (so that
$\langle p_1, p_2 \rangle = p$), and $\mathrm{dec}(n)$ for the result of the computable decoder on
$n$, which is either an oracle code or undefined. Then for all natural numbers $t$ and $p$, the
value $\mathrm{dec}\langle t, p \rangle$ is: $\mathsf{zero}$, $\mathsf{succ}$, $\mathsf{left}$,
$\mathsf{right}$ or $\mathsf{oracle}$ when $p = 0$ and $t$ is $0$, $1$, $2$, $3$ or $8$
respectively; $\mathsf{pair}(a, b)$, $\mathsf{comp}(a, b)$ or $\mathsf{prec}(a, b)$ when $t$ is
$4$, $5$ or $6$ respectively and $\mathrm{dec}(p_1) = a$ and $\mathrm{dec}(p_2) = b$ are both
defined; $\mathsf{rfind}(a)$ when $t = 7$ and $\mathrm{dec}(p) = a$ is defined; and undefined in
every other case.

For $t \in \{4, 5, 6, 7\}$ the numbers decoded on the right, $p_1$, $p_2$ and $p$, are at most $p$
and hence strictly below $\langle t, p \rangle$, so this is a recursion on the code number.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (Gödel numberings; decoding).

Formalized by `Cslib.Decidability.decodeOracleCode_pair`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 539](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L539). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#decode-oracle-code-pair).

## Whether a code number decodes

For a natural number $n$, this is the Boolean value that is
true exactly when the computable decoder of oracle codes returns an oracle code on $n$.

By decoder soundness and the inversion of the encoder, this holds exactly when $n$ is the Gödel
number of an oracle code.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (Gödel numberings; decoding).

Formalized by `Cslib.Decidability.decodeIsSome`, a definition declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 687](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L687). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#decode-is-some).

## The definedness predicate, by cases on the tag

Write $\langle a, b \rangle$ for the
pairing bijection $\mathbb{N} \times \mathbb{N} \to \mathbb{N}$ of the Gödel numbering, and say
that a natural number decodes when the computable decoder returns an oracle code on it. Let $t$
and $p$ be natural numbers and write $p = \langle p_1, p_2 \rangle$. Then $\langle t, p \rangle$
decodes if and only if one of the following holds: $t$ is $0$, $1$, $2$, $3$ or $8$ and $p = 0$;
$t$ is $4$, $5$ or $6$ and both $p_1$ and $p_2$ decode; or $t = 7$ and $p$ decodes.

In the recursive cases $t \ge 1$, so $p_1$, $p_2$ and $p$ are strictly smaller than
$\langle t, p \rangle$.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (Gödel numberings; decoding).

Formalized by `Cslib.Decidability.decodeIsSome_pair`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 694](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L694). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#decode-is-some-pair).

## One step of the course-of-values recursion for definedness

Write $\langle a, b \rangle$
for the pairing bijection $\mathbb{N} \times \mathbb{N} \to \mathbb{N}$ of the Gödel numbering.
The step takes an argument of the unit type, which it ignores, and a list $L$ of natural numbers;
for $i \in \mathbb{N}$ write $L_i$ for the entry of $L$ at position $i$ (counting from $0$), with
$L_i = 0$ when $i$ is at least the length of $L$. Let $m$ be the length of $L$, and write
$m = \langle t, p \rangle$ and $p = \langle p_1, p_2 \rangle$. The step always returns a value,
namely $1$ if one of the following holds and $0$ otherwise: $t$ is $0$, $1$, $2$, $3$ or $8$ and
$p = 0$; $t$ is $4$, $5$ or $6$ and $L_{p_1} = L_{p_2} = 1$; or $t = 7$ and $L_p = 1$.

Applied to the list whose entry at position $k < m$ is $1$ if $k$ decodes to an oracle code and
$0$ otherwise, it returns the corresponding value for $m$, because in the recursive cases $p_1$,
$p_2$ and $p$ are smaller than $m$.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (Gödel numberings; decoding).

Formalized by `Cslib.Decidability.decodeIsSomeStep`, a definition declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 777](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L777). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#decode-is-some-step).

## The course-of-values step for definedness is primitive recursive

One step of the
course-of-values recursion for definedness is primitive recursive as a function of its two
arguments, an element of the unit type and a list of natural numbers.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (Gödel numberings; decoding).

Formalized by `Cslib.Decidability.primrec₂_decodeIsSomeStep`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 799](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L799). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#primrec-decode-is-some-step).

## The definedness step function is correct

For a natural number $n$, let $b_n$ be $1$ if
the computable decoder returns an oracle code on $n$, and $0$ otherwise. For every natural number
$m$, the one-step function of the course-of-values recursion for definedness, applied to the list
$(b_0, b_1, \dots, b_{m-1})$, returns $b_m$.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (Gödel numberings; decoding).

Formalized by `Cslib.Decidability.decodeIsSomeStep_correct`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 883](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L883). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#decode-is-some-step-correct).

## The definedness predicate is primitive recursive

The function $\mathbb{N} \to \mathbb{N}$
sending $n$ to $1$ if $n$ decodes to an oracle code under the computable decoder and to $0$
otherwise is primitive recursive.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (Gödel numberings; decoding).

Formalized by `Cslib.Decidability.natPrimrec_decodeIsSome`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 1017](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L1017). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#nat-primrec-decode-is-some).

## Effective enumeration of oracle codes

The $n$-th oracle code is the code that the
computable decoder of the Gödel numbering of oracle codes assigns to $n$, or the basic code
$\mathtt{zero}$ (the constant $0$ program) when $n$ is not the number of any code. Because the
decoder inverts the Gödel numbering, this is an effective enumeration tied to that numbering,
not an arbitrary countable encoding.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (standard enumerations).

Formalized by `Cslib.Decidability.oracleCodeOfNat`, a definition declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 1052](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L1052). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#oracle-code-of-nat).

## The effective enumeration is a left inverse of the Gödel numbering

For every oracle code
$c$, the effective enumeration of oracle codes sends the code number of $c$ to $c$.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (standard enumerations).

Formalized by `Cslib.Decidability.oracleCodeOfNat_encode`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 1058](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L1058). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#oracle-code-of-nat-encode).

## The enumeration of oracle codes is surjective

**The enumeration of oracle codes is surjective.**

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (standard enumerations).

Formalized by `Cslib.Decidability.oracleCodeOfNat_surjective`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 1065](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L1065). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#oracle-code-of-nat-surjective).

## The Gödel encoding of oracle codes is primitive recursive

Regard oracle codes as coded
by their Gödel numbers, with the computable decoder as decoding. Then the map sending each oracle
code to its Gödel number is primitive recursive.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (Gödel numberings).

Formalized by `Cslib.Decidability.primrec_encodeOracleCode`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 1098](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L1098). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#primrec-encode-oracle-code).

## The Gödel decoder of oracle codes is primitive recursive

Regard oracle codes as coded
by their Gödel numbers. Then the computable decoder, which sends a natural number $n$ to the
oracle code with Gödel number $n$ when there is one and to no value otherwise, is primitive
recursive as a map from natural numbers to optional oracle codes.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (Gödel numberings; decoding).

Formalized by `Cslib.Decidability.primrec_decodeOracleCode`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 1104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L1104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#primrec-decode-oracle-code).

## The effective enumeration of oracle codes is primitive recursive

Regard oracle codes as
coded by their Gödel numbers. Then the effective enumeration of oracle codes, which sends a
natural number $n$ to the oracle code with Gödel number $n$ when there is one and to the zero
code otherwise, is primitive recursive.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (standard enumerations).

Formalized by `Cslib.Decidability.primrec_oracleCodeOfNat`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 1110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L1110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#primrec-oracle-code-of-nat).

## The effective enumeration of oracle codes is computable

**The effective enumeration of oracle codes is computable.**

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.6 (standard enumerations).

Formalized by `Cslib.Decidability.computable_oracleCodeOfNat`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 1116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L1116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#computable-oracle-code-of-nat).

## Fuel-indexed evaluation of oracle codes

Write $\langle a, b \rangle$ for the pairing of
natural numbers. For an oracle $o$ assigning to each natural number a natural number or no
value, a fuel $k$, an oracle code $c$ and an input $n$, the evaluator $E_k(c, n)$ returns a
natural number or fails. $E_0(c, n)$ always fails. $E_{k+1}(c, n)$ fails if $n > k$;
otherwise, with $n = \langle a, m \rangle$:

- $\mathtt{zero}$ returns $0$, $\mathtt{succ}$ returns $n + 1$, $\mathtt{left}$ returns $a$ and
  $\mathtt{right}$ returns $m$;
- $\mathtt{pair}(f, g)$ returns $\langle E_{k+1}(f, n), E_{k+1}(g, n) \rangle$;
- $\mathtt{comp}(f, g)$ returns $E_{k+1}(f, x)$ where $x = E_{k+1}(g, n)$;
- $\mathtt{prec}(f, g)$ returns $E_{k+1}(f, a)$ if $m = 0$, and if $m = y + 1$ it returns
  $E_{k+1}(g, \langle a, \langle y, i \rangle \rangle)$ where $i = E_k(\mathtt{prec}(f, g),
  \langle a, y \rangle)$;
- $\mathtt{rfind}(f)$ computes $x = E_{k+1}(f, \langle a, m \rangle)$ and returns $m$ if $x = 0$,
  and $E_k(\mathtt{rfind}(f), \langle a, m + 1 \rangle)$ otherwise;
- $\mathtt{oracle}$ returns $o(n)$, failing if $o$ has no value at $n$.

In every case the result fails if any evaluation it uses fails.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, §2 (oracle computations).

Formalized by `Cslib.Decidability.oracleEvaln`, a definition declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 1122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L1122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#oracle-evaln).

## Fuel bounds the inputs

For every oracle $o$, fuel $k$, oracle code $c$ and input $n$,
if the fuel-indexed evaluator with fuel $k$ returns a value on $c$ and $n$ relative to $o$, then
$n < k$.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, §2 (oracle computations).

Formalized by `Cslib.Decidability.oracleEvaln_bound`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 1164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L1164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#oracle-evaln-bound).

## Evaluation of oracle codes

Let $o$ be an oracle that assigns to each natural number
either a natural number or no value, $c$ an oracle code and $n$ a natural number. The value of
$c$ on $n$ relative to $o$ is the value returned by the fuel-indexed evaluator of $c$ on $n$
relative to $o$ at the least fuel $k$ for which that evaluator returns a value; it is undefined
when there is no such $k$.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, §2 (oracle computations).

Formalized by `Cslib.Decidability.oracleEval`, a definition declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 1178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L1178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#oracle-eval).

## The Turing jump

For a predicate $P$ on $\mathbb{N}$, the Turing jump $P'$ is the
predicate that holds at $n$ exactly when the $n$-th oracle code in the effective enumeration of
oracle codes, evaluated with the oracle that answers $1$ at $m$ if $P(m)$ holds and $0$ otherwise,
halts on input $n$. Thus $P'$ is the diagonal halting set of the universal oracle machine with
oracle $P$.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Definition 2.1 (the jump).

Formalized by `Cslib.Decidability.Jump`, a definition declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 1187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L1187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#jump).

## Turing reducibility of predicates

A predicate $P$ on the natural numbers is Turing
reducible to a predicate $Q$ on the natural numbers when the characteristic function of $P$ is
Turing reducible to the characteristic function of $Q$, that is, partial recursive relative to an
oracle for the characteristic function of $Q$.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Definition 2.2.

Formalized by `Cslib.Decidability.TuringReduciblePred`, a definition declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 1194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L1194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#turing-reducible-pred).

## Turing equivalence of predicates

Two predicates $P$ and $Q$ on the natural numbers are
Turing equivalent when the characteristic function of $P$ is Turing reducible to the
characteristic function of $Q$ and the characteristic function of $Q$ is Turing reducible to the
characteristic function of $P$.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Definition 2.2.

Formalized by `Cslib.Decidability.TuringEquivalentPred`, a definition declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 1200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L1200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#turing-equivalent-pred).

## Turing degree of a predicate

The Turing degree of a predicate $P$ on the natural numbers
is the Turing degree of its characteristic function, that is, the class of the characteristic
function of $P$ under Turing equivalence of partial functions
$\mathbb{N} \rightharpoonup \mathbb{N}$.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Definition 2.3.

Formalized by `Cslib.Decidability.turingDegreeOf`, a definition declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 1205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L1205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#turing-degree-of).

## Turing reducibility is reflexive

Every predicate $P$ on the natural numbers is Turing
reducible to itself.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Theorem 2.4.

Formalized by `Cslib.Decidability.turingReduciblePred_refl`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 1210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L1210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#turing-reducible-pred-refl).

## Turing reducibility is transitive

For predicates $P$, $Q$ and $R$ on the natural
numbers, if $P$ is Turing reducible to $Q$ and $Q$ is Turing reducible to $R$, then $P$ is Turing
reducible to $R$.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Theorem 2.4.

Formalized by `Cslib.Decidability.turingReduciblePred_trans`, a theorem declared in [CSLibExt/Computability/Decidability/Degrees.lean, line 1216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/Degrees.lean#L1216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html#turing-reducible-pred-trans).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Turing degrees and the Turing jump](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-degrees-and-the-turing-jump)
