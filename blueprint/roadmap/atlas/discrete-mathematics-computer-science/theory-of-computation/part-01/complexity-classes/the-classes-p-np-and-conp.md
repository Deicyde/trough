---
declaration: section
origin: cited
lean: MetaMathlibExt.BitstringEncoding, MetaMathlibExt.BitstringEncoding.bitEncode, MetaMathlibExt.BitstringEncoding.bitDecode, MetaMathlibExt.BitstringEncoding.bitDecode_bitEncode, MetaMathlibExt.BitstringEncoding.delimit, MetaMathlibExt.BitstringEncoding.undelimit, MetaMathlibExt.BitstringEncoding.undelimitBlocksAux, MetaMathlibExt.BitstringEncoding.undelimitBlocks
statement: formalized
proof: formalized
---

# The classes P, NP and coNP

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/the-classes-p-np-and-conp/index.html).

## Bitstring encodings

## Bitstring encodings

A canonical bitstring encoding of a type $\alpha$ consists of an
encoding map from $\alpha$ to finite lists of booleans and a partial decoding map from finite
lists of booleans to $\alpha$, such that decoding the encoding of any $a \in \alpha$ succeeds
and returns $a$.

## Sources

- a class version of Mathlib's `Computability.Encoding` specialized to the alphabet `Bool`, inlined from FormalConjectures (absent from Mathlib).

Formalized by `MetaMathlibExt.BitstringEncoding`, a class declared in [MathlibExt/Computability/Complexity.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/Complexity.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/the-classes-p-np-and-conp/index.html#bitstring-encoding).

## Encoding function of a bitstring encoding

For a type $\alpha$ with a canonical bitstring
encoding, the bitstring encoding of $a \in \alpha$ is the finite list of booleans that this
encoding assigns to $a$.

Formalized by `MetaMathlibExt.BitstringEncoding.bitEncode`, a definition declared in [MathlibExt/Computability/Complexity.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/Complexity.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/the-classes-p-np-and-conp/index.html#bit-encode).

## Decoding function of a bitstring encoding

For a type $\alpha$ with a canonical bitstring
encoding, bitstring decoding is the decoding function of that encoding: it sends each finite list
of booleans either to an element of $\alpha$ or to failure.

Formalized by `MetaMathlibExt.BitstringEncoding.bitDecode`, a definition declared in [MathlibExt/Computability/Complexity.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/Complexity.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/the-classes-p-np-and-conp/index.html#bit-decode).

## Decoding inverts bitstring encoding

Let $\alpha$ be a type with a canonical bitstring
encoding. For every $a \in \alpha$, decoding the bitstring encoding of $a$ succeeds and returns
$a$.

Formalized by `MetaMathlibExt.BitstringEncoding.bitDecode_bitEncode`, a theorem declared in [MathlibExt/Computability/Complexity.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/Complexity.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/the-classes-p-np-and-conp/index.html#bit-decode-bit-encode).

## Self-delimiting form of a bitstring

The self-delimiting form of a bitstring
$(b_1, \dots, b_n)$ is $(\mathrm{true}, b_1, \dots, \mathrm{true}, b_n, \mathrm{false})$: each
bit is preceded by $\mathrm{true}$ and the block is terminated by $\mathrm{false}$. In
particular the empty bitstring becomes $(\mathrm{false})$.

Formalized by `MetaMathlibExt.BitstringEncoding.delimit`, a definition declared in [MathlibExt/Computability/Complexity.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/Complexity.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/the-classes-p-np-and-conp/index.html#delimit).

## Parsing one self-delimiting block

Write booleans as bits, with true as $1$ and false as
$0$. Reading a list of bits from the front, a $0$ ends the block, and a $1$ followed by a bit $b$
contributes $b$ to the payload. The result is the payload together with the rest of the list
after the terminating $0$. Parsing fails if the list runs out before a terminating $0$ is read.

Formalized by `MetaMathlibExt.BitstringEncoding.undelimit`, a definition declared in [MathlibExt/Computability/Complexity.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/Complexity.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/the-classes-p-np-and-conp/index.html#undelimit).

## Bounded parsing of self-delimiting blocks

Given a bound $n$ and a list of booleans $s$,
the parse returns the empty list of payloads if $s$ is empty. If $s$ is nonempty and $n = 0$ it
fails. If $s$ is nonempty and $n = m + 1$, it parses one self-delimiting block from the front of
$s$, then parses the remaining list with bound $m$, and returns the first payload followed by the
payloads of the rest. It fails if either step fails. So the parse succeeds exactly when $s$ is
the concatenation of at most $n$ self-delimiting blocks, and it returns their payloads in order.

Formalized by `MetaMathlibExt.BitstringEncoding.undelimitBlocksAux`, a definition declared in [MathlibExt/Computability/Complexity.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/Complexity.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/the-classes-p-np-and-conp/index.html#undelimit-blocks-aux).

## Parsing a list of booleans into self-delimiting blocks

Given a list of booleans $s$, this
repeatedly parses one self-delimiting block from the front of $s$ until $s$ is used up, allowing
at most as many blocks as the length of $s$, and returns the list of payloads in order. It fails
if some block fails to parse. The bound never binds, since every block uses at least one bit.
So the parse succeeds exactly when $s$ is a concatenation of self-delimiting blocks.

Formalized by `MetaMathlibExt.BitstringEncoding.undelimitBlocks`, a definition declared in [MathlibExt/Computability/Complexity.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/Complexity.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/the-classes-p-np-and-conp/index.html#undelimit-blocks).

## Decision problems

A decision problem is a function from finite lists of booleans
(bitstrings) to booleans.

## Sources

- inlined from FormalConjectures (absent from Mathlib).

Formalized by `MetaMathlibExt.ComplexityTheory.DecisionProblem`, an abbreviation declared in [MathlibExt/Computability/Complexity.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/Complexity.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/the-classes-p-np-and-conp/index.html#decision-problem).

## Complexity classes

A complexity class is a set of decision problems.

## Sources

- inlined from FormalConjectures (absent from Mathlib).

Formalized by `MetaMathlibExt.ComplexityTheory.DecisionComplexityClass`, an abbreviation declared in [MathlibExt/Computability/Complexity.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/Complexity.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/the-classes-p-np-and-conp/index.html#decision-complexity-class).

## Polynomial-time computability under given encodings

Let $e_\alpha$ encode $\alpha$ as
words over an alphabet $\Gamma_\alpha$ and $e_\beta$ encode $\beta$ as words over $\Gamma_\beta$. A
function $f : \alpha \to \beta$ is polynomial-time computable with respect to $e_\alpha$ and
$e_\beta$ when there are a multi-stack Turing machine with finitely many stacks, function labels
and internal states and a finite input stack alphabet, identifications of its input and output
stack alphabets with $\Gamma_\alpha$ and $\Gamma_\beta$, and a polynomial $p$ with natural-number
coefficients, such that for every $a \in \alpha$ the machine, started at its main function in its
initial state with $e_\alpha(a)$ on its input stack and every other stack empty, halts within
$p(n)$ steps, where $n$ is the length of $e_\alpha(a)$, with $e_\beta(f(a))$ on its output stack,
every other stack empty and its internal state equal to its initial state.

## Sources

- inlined from FormalConjectures (absent from Mathlib).

Formalized by `MetaMathlibExt.ComplexityTheory.IsPolyTimeWithEncoding`, a definition declared in [MathlibExt/Computability/Complexity.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/Complexity.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/the-classes-p-np-and-conp/index.html#is-poly-time-with-encoding).

## Polynomial-time computable functions

Let $\alpha$ and $\beta$ be types with canonical
bitstring encodings. A function $f : \alpha \to \beta$ is polynomial-time computable when it is
polynomial-time computable with respect to the canonical bitstring encodings of $\alpha$ and
$\beta$.

## Sources

- inlined from FormalConjectures (absent from Mathlib).

Formalized by `MetaMathlibExt.ComplexityTheory.IsPolyTime`, a definition declared in [MathlibExt/Computability/Complexity.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/Complexity.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/the-classes-p-np-and-conp/index.html#is-poly-time).

## The complexity class P

P is the set of decision problems (functions from lists of
booleans to booleans) that are computable in polynomial time by a deterministic multi-stack
Turing machine, with respect to the canonical bitstring encodings of inputs and outputs.

Formalized by `MetaMathlibExt.ComplexityTheory.P`, a definition declared in [MathlibExt/Computability/Complexity.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/Complexity.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/the-classes-p-np-and-conp/index.html#p).

## The complexity class NP

NP is the set of decision problems $L$ (functions from lists of
booleans to booleans) for which there exist a polynomial $p$ with natural-number coefficients and
a polynomial-time computable function $R$ from pairs of lists of booleans to booleans such that,
for every list of booleans $x$, $L(x)$ is true if and only if there is a list of booleans $w$
whose length is at most $p$ evaluated at the length of $x$ and for which $R(x, w)$ is true.

Polynomial time is measured with respect to the canonical bitstring encodings.

Formalized by `MetaMathlibExt.ComplexityTheory.NP`, a definition declared in [MathlibExt/Computability/Complexity.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/Complexity.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/the-classes-p-np-and-conp/index.html#np).

## The class coNP

**The class coNP.** coNP is the set of decision problems $L$ whose complement, the decision
problem that accepts exactly the bitstrings that $L$ rejects, belongs to NP.

## Sources

- inlined from FormalConjectures (absent from Mathlib).

Formalized by `MetaMathlibExt.ComplexityTheory.coNP`, a definition declared in [MathlibExt/Computability/Complexity.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Computability/Complexity.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/the-classes-p-np-and-conp/index.html#co-np).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The classes P, NP and coNP](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/the-classes-p-np-and-conp/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/complexity-classes/the-classes-p-np-and-conp)
