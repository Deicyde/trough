---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.FWGate, MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.fwCircuitEval, MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.fwCircuitOutputs, MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.fwInvertSucc, MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.OWFExists, MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.Samplable, MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.AvgEasy, MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.AvgHard
statement: formalized
---

# Impagliazzo's five worlds

18 results, 17 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds/index.html).

## Serialized gates of five-worlds circuits

A serialized gate of a flat Boolean circuit is a
pair $(k, r)$ of a natural number $k$ (the gate kind) and a list $r$ of natural numbers (its
references, depending on the kind: an input index, a constant bit, or indices of other gates), in
the shared encoding of gates as (kind, references) pairs.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.FWGate`, an abbreviation declared in [WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds/index.html#fwgate).

## Evaluation of an encoded flat circuit

Let $C$ be a flat Boolean circuit given as a list
of gates, each encoded as a (kind, references) pair, and let $a = (a_0, \dots, a_{k-1})$ be a
list of booleans. The gate values of $C$ on $a$ are the gate values, in order, of the circuit on
$k$ inputs obtained by decoding each gate of $C$, evaluated on the assignment that sends input
$i$ to $a_i$.

Decoding turns an input variable $x_i$ with $i \ge k$ into the constant false.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.fwCircuitEval`, a definition declared in [WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds/index.html#fw-circuit-eval).

## Outputs of an encoded flat circuit

For an encoded flat Boolean circuit $C$, a list of
booleans $a$ and a natural number $k$, the outputs of $C$ on $a$ are the last $k$ entries of the
list of gate values of $C$ on $a$, or the whole list if $C$ has fewer than $k$ gates.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.fwCircuitOutputs`, a definition declared in [WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds/index.html#fw-circuit-outputs).

## Inversion success probability of a circuit

Let $f$ map $n$-bit strings to bitstrings
and let $C$ be an encoded flat Boolean circuit. For an $n$-bit string $x$, the candidate preimage
$x'$ consists of the last $n$ gate values of $C$ on input $f(x)$ (all of them if $C$ has fewer
than $n$ gates), padded with false to length $n$. The inversion success probability of $C$
against $f$ is the fraction of the $2^n$ strings $x$ for which $f(x') = f(x)$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.fwInvertSucc`, a definition declared in [WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds/index.html#fw-invert-succ).

## One-way functions exist

There are a family of functions $f_n$, each mapping $n$-bit strings
to bitstrings, and a polynomial $q$ with natural-number coefficients such that the following hold:
$|f_n(x)| \le q(n)$ for every $n$ and every $n$-bit string $x$; some polynomial-time computable
function on bitstrings maps the canonical bitstring encoding of every pair $(n, x)$ to $f_n(x)$;
and for every family of flat Boolean circuits $C_n$, given as lists of serialized gates, with at
most $p(n)$ gates for some polynomial $p$ with natural-number coefficients, the fraction of
$n$-bit strings $x$ with $f_n(x') = f_n(x)$ is a negligible function of $n$. Here $x'$ is the
$n$-bit string whose $i$-th bit is the $i$-th of the last $n$ gate values of $C_n$ on input
$f_n(x)$, or false when there is no such value.

The functions need not be injective, and they are computed by a single uniform polynomial-time
algorithm: per-length polynomial-size circuits would admit noncomputable $\mathsf{P/poly}$
families.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.OWFExists`, a definition declared in [WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds/index.html#owfexists).

## Samplable distributions

Let $p$ be a polynomial with natural-number coefficients and let
$S$ be a family of maps $S_n$ from $p(n)$-bit coin strings to bitstrings. The pair $(p, S)$ is
samplable when every $S_n(r)$ has length exactly $n$ and some polynomial-time computable function
on bitstrings maps the canonical bitstring encoding of every pair $(n, r)$ to $S_n(r)$.

The distribution sampled at length $n$ is that of $S_n(r)$ for a uniformly random coin string
$r$. The sampler is a single uniform polynomial-time algorithm: per-length circuits would admit
noncomputable $\mathsf{P/poly}$ samplers. The coin count is a polynomial rather than $n$: a
distribution giving probability $2^{-(n+1)}$ to one output is samplable with $n + 1$ coins but
not from $n$ uniform coins.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.Samplable`, a definition declared in [WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds/index.html#samplable).

## Easy on average

Let $p$ be a polynomial with natural-number coefficients, $L$ a
decision problem, and $S$ a family of samplers, where $S_n$ sends each string $r$ of $p(n)$
random bits to a bitstring $S_n(r)$. The pair $(L, S)$ is easy on average when there is a
polynomial-time computable function $A$ from bitstrings to booleans such that for every natural
number $c$ there is $N$ such that for all $n \ge N$

$$1 - \frac{1}{n^c + 1} \le \frac{\#\{r \in \{0,1\}^{p(n)} : A(S_n(r)) = L(S_n(r))\}}{2^{p(n)}},$$

that is, $A$ agrees with $L$ on $S_n(r)$ for at least a fraction $1 - 1/(n^c + 1)$ of the
coin strings $r$.

The algorithm $A$ does not depend on $c$, so its error is negligible. Requiring the bound
$1 - 1/(q(n) + 1)$ for a single polynomial $q$ instead would be vacuous: the zero polynomial
gives the lower bound $0$, which every algorithm meets.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.AvgEasy`, a definition declared in [WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds/index.html#avg-easy).

## Hard on average

Let $p$ be a polynomial with natural-number coefficients, $L$ a
decision problem, and $S$ a family of samplers, where $S_n$ sends each string $r$ of $p(n)$
random bits to a bitstring $S_n(r)$. The pair $(L, S)$ is hard on average when it is not easy
on average: there is no polynomial-time computable function $A$ from bitstrings to booleans
such that for every natural number $c$ and all sufficiently large $n$, $A$ agrees with $L$ on
$S_n(r)$ for at least a fraction $1 - 1/(n^c + 1)$ of the $2^{p(n)}$ coin strings $r$.

Since hardness is the logical complement of easiness, if $\mathrm{P} \ne \mathrm{NP}$ and
Heuristica fails, then some NP problem is hard on average for some samplable ensemble.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.AvgHard`, a definition declared in [WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds/index.html#avg-hard).

## Key pair produced by a key generator

For a map $G$ from bitstrings to bitstrings (the key
generator) and a bitstring $r$ of coins, the key pair of $G$ on $r$ is the pair of bitstrings
obtained by decoding $G(r)$ with the canonical bitstring encoding of pairs of bitstrings, or the
pair of empty bitstrings if this decoding fails.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.fwKeyPair`, a definition declared in [WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds/index.html#fw-key-pair).

## Eavesdropping advantage against a public-key scheme

Let $G$ (key generation) and $E$
(encryption) be maps from bitstrings to bitstrings, let $C$ be an encoded flat Boolean circuit,
let $\ell$ be a polynomial with natural-number coefficients and let $n$ be a natural number. For
key coins $r$ and encryption coins $s$, each a string of $\ell(n)$ bits, and a bit $b$, let $pk$
be the first component of the key pair of $G$ on $r$, and let the ciphertext $e$ be $E$ applied
to the bitstring encoding of the triple $(pk, (b), s)$, where $(b)$ is the one-bit list. The
circuit $C$ succeeds on $(r, s, b)$ when it has a last gate value on the bitstring encoding of
the pair $(pk, e)$ and that value equals $b$. If $N$ is the number of triples $(r, s, b)$ on
which $C$ succeeds, the advantage of $C$ at length $n$ is $|N / 2^{2\ell(n) + 1} - 1/2|$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.fwPKAdv`, a definition declared in [WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds/index.html#fw-pkadv).

## Public-key encryption exists

There are a polynomial $\ell$ with natural-number
coefficients and polynomial-time computable functions $G$ (key generation), $E$ (encryption) and
$D$ (decryption) on bitstrings with the following two properties. Here tuples are passed to
these functions and to circuits through their canonical bitstring encodings, and for a bitstring
$r$ the keys $(\mathit{pk}, \mathit{sk})$ are the decoding of $G(r)$ as a pair of bitstrings,
both empty when decoding fails. Correctness: for every $n$, all bitstrings $r$ and $s$ of length
$\ell(n)$ and every bit $b$, $D(\mathit{sk}, E(\mathit{pk}, [b], s)) = [b]$. Security: for every
family of flat Boolean circuits $C_n$, given as lists of serialized gates, with at most $p(n)$
gates for some polynomial $p$ with natural-number coefficients, and for every natural number
$c$, the advantage of $C_n$ is at most $1 / n^c$ for all sufficiently large $n$. The advantage
of $C_n$ is $|P_n - 1/2|$, where $P_n$ is the fraction of triples $(r, s, b)$ of bitstrings $r$
and $s$ of length $\ell(n)$ and a bit $b$ for which the last gate value of $C_n$ on input
$(\mathit{pk}, E(\mathit{pk}, [b], s))$ is $b$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.PKExists`, a definition declared in [WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds/index.html#pkexists).

## Algorithmica

Algorithmica is the statement that the complexity classes $\mathrm{P}$ and
$\mathrm{NP}$ are equal.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.Algorithmica`, a definition declared in [WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds/index.html#algorithmica).

## Heuristica

Heuristica: `P ≠ NP`, but every NP problem is easy on average for every samplable
distribution.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.Heuristica`, a definition declared in [WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds/index.html#heuristica).

## Pessiland

Pessiland is the statement that $\mathsf{P} \ne \mathsf{NP}$, that one-way
functions do not exist, and that some decision problem $L$ in NP is hard on average for some
samplable distribution: there are a polynomial $p$ with natural-number coefficients and a family
$S$ of maps $S_n$ from $p(n)$-bit coin strings to bitstrings such that $(p, S)$ is samplable and
$L$ is hard on average with respect to $S$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.Pessiland`, a definition declared in [WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds/index.html#pessiland).

## Minicrypt

Minicrypt: one-way functions exist, but public-key cryptography does not.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.Minicrypt`, a definition declared in [WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds/index.html#minicrypt).

## Cryptomania

Cryptomania is the statement that public-key cryptography exists: there
are a polynomial $\ell$ with natural-number coefficients and polynomial-time computable maps
$G$ (key generation), $E$ (encryption) and $D$ (decryption) from bitstrings to bitstrings with
the following two properties. First, decryption is correct: for every natural number $n$, all
key coins $r$ and encryption coins $s$ that are bitstrings of length $\ell(n)$, and every bit
$b$, if $(pk, sk)$ is the key pair of $G$ on $r$ and the ciphertext $e$ is $E$ applied to the
bitstring encoding of the triple $(pk, (b), s)$, where $(b)$ is the one-bit list, then $D$
applied to the bitstring encoding of the pair $(sk, e)$ is $(b)$. Second, the scheme is secure:
for every family $(C_n)$ of encoded flat Boolean circuits and every polynomial $q$ with
natural-number coefficients such that each $C_n$ has at most $q(n)$ gates, and for every natural
number $c$, there is $N$ such that for all $n \ge N$ the eavesdropping advantage of $C_n$
against $(G, E)$ with polynomial $\ell$ at length $n$ is at most $1/n^c$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.Cryptomania`, a definition declared in [WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds/index.html#cryptomania).

## Exactly one of Impagliazzo's five worlds holds

Exactly one of the statements
Algorithmica, Heuristica, Pessiland, Minicrypt and Cryptomania is true: one of them holds and
the other four fail.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.ExactlyOneWorld`, a definition declared in [WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds/index.html#exactly-one-world).

## Impagliazzo's five worlds

The following four statements hold. First, if public-key
encryption exists, then one-way functions exist. Second, if one-way functions exist, then some
decision problem $L$ in NP is hard on average for some samplable distribution: there are a
polynomial $p$ with natural-number coefficients and a family $S$ of maps $S_n$ from $p(n)$-bit
coin strings to bitstrings such that $(p, S)$ is samplable and $L$ is hard on average with
respect to $S$. Third, if some decision problem in NP is hard on average for some samplable
distribution in this sense, then $\mathsf{P} \ne \mathsf{NP}$. Fourth, exactly one of the five
worlds Algorithmica, Heuristica, Pessiland, Minicrypt and Cryptomania holds.

## Sources

- R. Impagliazzo, "A personal view of average-case complexity", Proceedings of the Tenth Annual Structure in Complexities Theory Conference (1995), 134-147.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.FiveWorlds.impagliazzo_five_worlds` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/FiveWorldsWanted.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds/index.html#impagliazzo-five-worlds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Impagliazzo's five worlds](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/impagliazzo-s-five-worlds)
