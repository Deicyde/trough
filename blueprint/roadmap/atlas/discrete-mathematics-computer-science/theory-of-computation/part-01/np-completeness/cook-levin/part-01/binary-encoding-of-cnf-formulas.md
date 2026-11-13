---
declaration: section
origin: cited
lean: Cslib.CookLevin.readUnaryLength, Cslib.CookLevin.encodeNatPrefix, Cslib.CookLevin.decodeNatPrefix, Cslib.CookLevin.encodeLit, Cslib.CookLevin.decodeLit, Cslib.CookLevin.decodeLits, Cslib.CookLevin.encodeClause, Cslib.CookLevin.decodeClause
statement: formalized
proof: formalized
---

# Binary encoding of CNF formulas

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas/index.html).

## Reading a unary length prefix

On a list of Booleans that begins with $k$ copies of
$\mathrm{true}$ followed by $\mathrm{false}$, the reader returns $k$ together with the rest of
the list after that $\mathrm{false}$. On a list containing no $\mathrm{false}$, including the
empty list, it fails.

Formalized by `Cslib.CookLevin.readUnaryLength`, a definition declared in [CSLibExt/Computability/CookLevin.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/CookLevin.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas/index.html#read-unary-length).

## Prefix-free code of a natural number

The code of $n \in \mathbb{N}$ is the
self-delimiting block of the binary representation of $n$ (least significant bit first, with
$0$ represented by the empty list): each bit $c$ is written as the two bits $\mathrm{true}, c$,
and the block ends with a terminating $\mathrm{false}$.

Formalized by `Cslib.CookLevin.encodeNatPrefix`, a definition declared in [CSLibExt/Computability/CookLevin.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/CookLevin.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas/index.html#encode-nat-prefix).

## Decoding a prefix-coded natural number

Given a bit string $w$, writing $1$ for true and
$0$ for false, the decoder reads one self-delimiting block $1\,b_1\,1\,b_2 \cdots 1\,b_k\,0$ from
the front of $w$, with payload $b_1 \cdots b_k$ and remaining bits $r$. If the payload is the
binary expansion of some natural number $n$, least significant bit first and without trailing
zeros (empty for $n = 0$), the result is $(n, r)$. Decoding fails if $w$ does not begin with such
a block or the payload is not of this form.

Formalized by `Cslib.CookLevin.decodeNatPrefix`, a definition declared in [CSLibExt/Computability/CookLevin.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/CookLevin.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas/index.html#decode-nat-prefix).

## Binary code of a literal

A literal $(n, b)$, with variable index $n \in \mathbb{N}$ and
polarity $b \in \{\mathrm{false}, \mathrm{true}\}$, is encoded as the prefix-free code of $n$
followed by the single bit $b$.

Formalized by `Cslib.CookLevin.encodeLit`, a definition declared in [CSLibExt/Computability/CookLevin.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/CookLevin.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas/index.html#encode-lit).

## Decoding a literal

Given a bit string $w$, the decoder reads a prefix-coded natural
number $n$ from the front of $w$ and then one more bit $b$. The result is the literal $(n, b)$,
with variable index $n$ and polarity $b$, together with the bits left after $b$. Decoding fails if
no prefix-coded natural number can be read or no bit follows it.

Formalized by `Cslib.CookLevin.decodeLit`, a definition declared in [CSLibExt/Computability/CookLevin.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/CookLevin.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas/index.html#decode-lit).

## Decoding a fixed number of literals

For a natural number $n$ and a bit string $w$, the
decoder reads $n$ literals one after another from the front of $w$ with the literal decoder. The
result is the clause made of these literals, in order, together with the bits left after them;
for $n = 0$ it is the empty clause together with $w$. Decoding fails if one of the $n$ literals
cannot be read.

Formalized by `Cslib.CookLevin.decodeLits`, a definition declared in [CSLibExt/Computability/CookLevin.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/CookLevin.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas/index.html#decode-lits).

## Length-prefixed binary code of a clause

Writing $1$ for true and $0$ for false, the code
of a clause $C = (\ell_1, \dots, \ell_k)$ is $1^k 0$ ($k$ ones followed by a zero) followed by the
binary codes of $\ell_1, \dots, \ell_k$ in order, where a literal $(x, b)$ with variable index $x$
and polarity $b$ is coded by the prefix-free code of $x$ followed by the bit $b$.

Formalized by `Cslib.CookLevin.encodeClause`, a definition declared in [CSLibExt/Computability/CookLevin.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/CookLevin.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas/index.html#encode-clause).

## Decoding a length-prefixed clause

Given a bit string $w$, writing $1$ for true and $0$
for false, the decoder reads a unary length prefix $1^n 0$ ($n$ ones followed by a zero) from the
front of $w$, then reads exactly $n$ literals from the remaining bits with the literal decoder.
The result is the clause made of these literals, in order, together with the bits left after
them. Decoding fails if $w$ does not begin with such a prefix or one of the literals cannot be
read.

Formalized by `Cslib.CookLevin.decodeClause`, a definition declared in [CSLibExt/Computability/CookLevin.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/CookLevin.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas/index.html#decode-clause).

## Decoding a fixed number of clauses

For a natural number $n$ and a bit string $w$, the
decoder reads $n$ clauses one after another from the front of $w$ with the length-prefixed clause
decoder. The result is the CNF formula made of these clauses, in order, together with the bits
left after them; for $n = 0$ it is the empty formula together with $w$. Decoding fails if one of
the $n$ clauses cannot be read.

Formalized by `Cslib.CookLevin.decodeClauses`, a definition declared in [CSLibExt/Computability/CookLevin.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/CookLevin.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas/index.html#decode-clauses).

## Length-prefixed binary code of a CNF formula

Writing $1$ for true and $0$ for false, the
code of a CNF formula $\varphi = (C_1, \dots, C_m)$ is $1^m 0$ ($m$ ones followed by a zero)
followed by the length-prefixed binary codes of the clauses $C_1, \dots, C_m$ in order.

Formalized by `Cslib.CookLevin.encodeCNF`, a definition declared in [CSLibExt/Computability/CookLevin.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/CookLevin.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas/index.html#encode-cnf).

## Decoding a length-prefixed CNF formula

Given a bit string $w$, writing $1$ for true and
$0$ for false, the decoder reads a unary length prefix $1^n 0$ ($n$ ones followed by a zero) from
the front of $w$, then reads exactly $n$ clauses from the remaining bits with the length-prefixed
clause decoder. The result is the CNF formula made of these clauses, in order, together with the
bits left after them. Decoding fails if $w$ does not begin with such a prefix or one of the
clauses cannot be read.

Formalized by `Cslib.CookLevin.decodeCNFAux`, a definition declared in [CSLibExt/Computability/CookLevin.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/CookLevin.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas/index.html#decode-cnfaux).

## Decoding a complete length-prefixed CNF formula

Given a bit string $w$, the decoder reads
one CNF formula $\varphi$ from the front of $w$ with the length-prefixed CNF decoder, which also
returns the bits left after $\varphi$. The result is $\varphi$ if no bits are left; decoding fails
if no formula can be read or if bits remain after it.

Formalized by `Cslib.CookLevin.decodeCNF`, a definition declared in [CSLibExt/Computability/CookLevin.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/CookLevin.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas/index.html#decode-cnf).

## Parsing a self-delimiting block

For all lists of Booleans $u$, $p$ and $r$, parsing one
self-delimiting block from the front of $u$ succeeds with payload $p$ and remainder $r$ if and
only if $u$ is the self-delimiting block of $p$ followed by $r$.

Formalized by `Cslib.CookLevin.undelimit_eq_some_iff`, a theorem declared in [CSLibExt/Computability/CookLevin.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/CookLevin.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas/index.html#undelimit-eq-some-iff).

## The CNF decoder inverts the length-prefixed CNF code

For every bit string $w$ and every
CNF formula $\varphi$, the complete CNF decoder returns $\varphi$ on input $w$ if and only if $w$
is the length-prefixed binary code of $\varphi$.

Formalized by `Cslib.CookLevin.decodeCNF_eq_some_iff`, a theorem declared in [CSLibExt/Computability/CookLevin.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/CookLevin.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas/index.html#decode-cnf-eq-some-iff).

## Encodings of satisfiable CNF formulas

A list $x$ of Booleans encodes a satisfiable CNF
formula when $x$ is the binary code of some CNF formula $\varphi$ and $\varphi$ is
satisfiable.

Formalized by `Cslib.CookLevin.IsSATEncoded`, a definition declared in [CSLibExt/Computability/CookLevin.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/CookLevin.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas/index.html#is-satencoded).

## The SAT language

SAT is the set of lists of Booleans that encode a satisfiable CNF
formula.

Formalized by `Cslib.CookLevin.SATLang`, a definition declared in [CSLibExt/Computability/CookLevin.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/CookLevin.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas/index.html#satlang).

## SAT as a decision problem

The SAT decision problem returns true on a list $x$ of Booleans
when $x$ lies in the SAT language, that is, when $x$ encodes a satisfiable CNF formula, and
false otherwise.

Formalized by `Cslib.CookLevin.satDec`, a definition declared in [CSLibExt/Computability/CookLevin.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/CookLevin.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas/index.html#sat-dec).

## Polynomial-time many-one reduction

A decision problem $L_1$ reduces to a decision problem
$L_2$ in polynomial time when there is a polynomial-time computable function $f$ from lists of
Booleans to lists of Booleans such that $L_1(x) = L_2(f(x))$ for every list $x$ of Booleans.

Formalized by `Cslib.CookLevin.PolyManyOneRed`, a definition declared in [CSLibExt/Computability/CookLevin.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/CookLevin.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas/index.html#poly-many-one-red).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binary encoding of CNF formulas](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/binary-encoding-of-cnf-formulas)
