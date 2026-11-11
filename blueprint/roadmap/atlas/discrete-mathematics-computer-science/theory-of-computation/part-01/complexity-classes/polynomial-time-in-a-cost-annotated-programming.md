---
declaration: section
origin: cited
lean: Cslib.TimeMComplexity.DecidesInDeclaredPolyTime, Cslib.TimeMComplexity.ComputesInDeclaredPolyTime, Cslib.TimeMComplexity.VerifierInDeclaredPolyTime, Cslib.TimeMComplexity.Verifies, Cslib.TimeMComplexity.DeclaredPolyManyOneRedVia, Cslib.TimeMComplexity.exists_decidesInDeclaredPolyTime, Cslib.TimeMComplexity.verifierInDeclaredPolyTime_of_decidesInDeclaredPolyTime, Cslib.TimeMComplexity.verifies_of_decides
statement: formalized
proof: formalized
---

# Polynomial time in a cost-annotated programming model

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-in-a-cost-annotated-programming/index.html).

## Declared polynomial time for timed deciders

Let $f$ be a timed function that maps each
list $x$ of Booleans to a Boolean $f(x)$ together with a declared time $t_f(x) \in \mathbb{N}$.
Then $f$ decides in declared polynomial time when there is a polynomial $p$ with natural-number
coefficients such that $t_f(x) \le p(|x|)$ for every list $x$ of Booleans, where $|x|$ is the
length of $x$.

This constrains only the trusted time annotation: it implies neither that $f$ is computable in
any machine model nor that $f$ is related to any particular decision problem.

Formalized by `Cslib.TimeMComplexity.DecidesInDeclaredPolyTime`, a definition declared in [CSLibExt/Computability/TimeMComplexity.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/TimeMComplexity.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-in-a-cost-annotated-programming/index.html#decides-in-declared-poly-time).

## Declared polynomial time for timed functions on bitstrings

Let $f$ be a timed function
that maps each list $x$ of Booleans to an output list $f(x)$ of Booleans together with a declared
time $t_f(x) \in \mathbb{N}$. Then $f$ computes in declared polynomial time when there is a
polynomial $p$ with natural-number coefficients such that, for every list $x$ of Booleans, both
$t_f(x)$ and the length of $f(x)$ are at most $p(|x|)$, where $|x|$ is the length of $x$.

Declared times are trusted annotations, not checked against any machine model, so this does not
make $f$ polynomial-time computable: for an arbitrary decision problem $L$, the function returning
the one-element list $[L(x)]$ with declared time $0$ satisfies it. The output-length bound is what
lets declared bounds compose.

Formalized by `Cslib.TimeMComplexity.ComputesInDeclaredPolyTime`, a definition declared in [CSLibExt/Computability/TimeMComplexity.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/TimeMComplexity.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-in-a-cost-annotated-programming/index.html#computes-in-declared-poly-time).

## Verifiers with polynomial declared time

A timed verifier $V$, which assigns to each pair
of bit strings $(x, w)$ (an input and a witness) a timed computation returning a Boolean, runs in
declared polynomial time when there is a polynomial $q$ with natural coefficients such that the
declared time of $V(x, w)$ is at most $q(|x| + |w|)$ for all $x$ and $w$.

As for deciders, this constrains only the declared time, which is a trusted annotation, and
establishes no computability in any machine model.

Formalized by `Cslib.TimeMComplexity.VerifierInDeclaredPolyTime`, a definition declared in [CSLibExt/Computability/TimeMComplexity.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/TimeMComplexity.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-in-a-cost-annotated-programming/index.html#verifier-in-declared-poly-time).

## Verifying a decision problem with a witness bound

A timed verifier $V$, which assigns to
each pair of bit strings $(x, w)$ (an input and a witness) a timed computation returning a
Boolean, verifies a decision problem $L$ with witness bound $p$, a polynomial with natural
coefficients, when for every bit string $x$, $L(x)$ holds if and only if there is a witness $w$
with $|w| \le p(|x|)$ such that $V(x, w)$ returns true.

This is the verifier half of the definition of NP, phrased for a named timed verifier.

Formalized by `Cslib.TimeMComplexity.Verifies`, a definition declared in [CSLibExt/Computability/TimeMComplexity.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/TimeMComplexity.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-in-a-cost-annotated-programming/index.html#verifies).

## Declared-time many-one reduction by a timed function

Let $L_1$ and $L_2$ be decision
problems and let $f$ be a timed function that maps each list $x$ of Booleans to a list $f(x)$ of
Booleans together with a declared time. Then $f$ is a declared-time many-one reduction from $L_1$
to $L_2$ when $f$ computes in declared polynomial time and $L_1(x) = L_2(f(x))$ for every list $x$
of Booleans.

Because declared times are trusted annotations, this is not a polynomial-time many-one reduction
in the Turing-machine sense: nothing is established about the computability of $f$.

Formalized by `Cslib.TimeMComplexity.DeclaredPolyManyOneRedVia`, a definition declared in [CSLibExt/Computability/TimeMComplexity.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/TimeMComplexity.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-in-a-cost-annotated-programming/index.html#declared-poly-many-one-red-via).

## Every decision problem has a timed decider in declared polynomial time

For every decision
problem $L$ there is a timed function $f$ from lists of Booleans to Booleans that decides in
declared polynomial time and whose output $f(x)$ equals $L(x)$ for every list $x$ of Booleans.

The witness returns $L(x)$ with declared time $0$, treating the evaluation of $L$ as free. This is
why no complexity classes are defined by quantifying over timed functions.

Formalized by `Cslib.TimeMComplexity.exists_decidesInDeclaredPolyTime`, a theorem declared in [CSLibExt/Computability/TimeMComplexity.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/TimeMComplexity.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-in-a-cost-annotated-programming/index.html#exists-decides-in-declared-poly-time).

## A decider with polynomial declared time gives a verifier with polynomial declared time

If a timed decider $f$ on bit strings has declared time bounded by a polynomial in the input
length, then the verifier that sends an input $x$ and a witness $w$ to $f(x)$, ignoring $w$, has
declared time bounded by a polynomial in $|x| + |w|$.

Formalized by `Cslib.TimeMComplexity.verifierInDeclaredPolyTime_of_decidesInDeclaredPolyTime`, a theorem declared in [CSLibExt/Computability/TimeMComplexity.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/TimeMComplexity.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-in-a-cost-annotated-programming/index.html#verifier-in-declared-poly-time-of-decide).

## A decider is a verifier with witness bound zero

Let $L$ be a decision problem and let $f$
be a timed decider whose return value on every bit string $x$ equals $L(x)$. Then the verifier
that sends an input $x$ and a witness $w$ to $f(x)$, ignoring $w$, verifies $L$ with the zero
polynomial as witness bound, so only the empty witness is allowed.

Together with the fact that this verifier has polynomial declared time whenever $f$ does, this is
the declared-time form of $\mathrm{P} \subseteq \mathrm{NP}$ for named algorithms.

Formalized by `Cslib.TimeMComplexity.verifies_of_decides`, a theorem declared in [CSLibExt/Computability/TimeMComplexity.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/TimeMComplexity.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-in-a-cost-annotated-programming/index.html#verifies-of-decides).

## Declared-time many-one reduction is reflexive

For every decision problem $L$, the timed
identity function, which returns its input with declared time $0$, is a declared-time many-one
reduction from $L$ to $L$.

Formalized by `Cslib.TimeMComplexity.declaredPolyManyOneRedVia_refl`, a theorem declared in [CSLibExt/Computability/TimeMComplexity.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/TimeMComplexity.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-in-a-cost-annotated-programming/index.html#declared-poly-many-one-red-via-refl).

## Declared-time many-one reductions compose

Let $L_1$, $L_2$ and $L_3$ be decision problems.
If $f_1$ is a declared-time many-one reduction from $L_1$ to $L_2$ and $f_2$ is a declared-time
many-one reduction from $L_2$ to $L_3$, then the timed function that on input $x$ returns
$f_2(f_1(x))$, with declared time the declared time of $f_1$ on $x$ plus that of $f_2$ on
$f_1(x)$, is a declared-time many-one reduction from $L_1$ to $L_3$.

If $p_1$ and $p_2$ bound the declared times and output lengths of $f_1$ and $f_2$, then
$p_1 + p_2 \circ p_1$ bounds those of the composite.

Formalized by `Cslib.TimeMComplexity.declaredPolyManyOneRedVia_trans`, a theorem declared in [CSLibExt/Computability/TimeMComplexity.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/TimeMComplexity.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-in-a-cost-annotated-programming/index.html#declared-poly-many-one-red-via-trans).

## Declared polynomial time is preserved under precomposition with a reduction

Let $L_1$ and
$L_2$ be decision problems, let $f$ be a declared-time many-one reduction from $L_1$ to $L_2$, and
let $g$ be a timed function from lists of Booleans to Booleans that decides in declared polynomial
time. Then the timed function that on input $x$ returns $g(f(x))$, with declared time the declared
time of $f$ on $x$ plus that of $g$ on $f(x)$, decides in declared polynomial time.

If $p_f$ bounds the declared time and output length of $f$ and $p_g$ bounds the declared time of
$g$, then $p_f + p_g \circ p_f$ bounds the declared time of the composite.

Formalized by `Cslib.TimeMComplexity.decidesInDeclaredPolyTime_comp_reduction`, a theorem declared in [CSLibExt/Computability/TimeMComplexity.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/TimeMComplexity.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-in-a-cost-annotated-programming/index.html#decides-in-declared-poly-time-comp-reduc).

## A declared-time reduction followed by a decider for the target decides the source

Let
$L_1$ and $L_2$ be decision problems, let $f$ be a declared-time many-one reduction from $L_1$ to
$L_2$, and let $g$ be a timed function from lists of Booleans to Booleans whose output on every
list $y$ is $L_2(y)$. Then for every list $x$ of Booleans, the timed function that runs $f$ on $x$
and then $g$ on its output returns $L_1(x)$.

Together with the preservation of declared polynomial time under such compositions, this is the
declared-time form of closure under reductions; no membership in the class P is claimed.

Formalized by `Cslib.TimeMComplexity.decides_comp_reduction`, a theorem declared in [CSLibExt/Computability/TimeMComplexity.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/TimeMComplexity.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-in-a-cost-annotated-programming/index.html#decides-comp-reduction).

## Pulling a verifier back along a declared reduction

Let $L_1$ and $L_2$ be decision
problems, let $f$ be a declared polynomial-time many-one reduction from $L_1$ to $L_2$, and let
$V$ be a verifier with polynomial declared time that verifies $L_2$ with witness bound $p$. Let
$V'$ be the verifier that on input $x$ and witness $w$ first runs $f$ on $x$, obtaining $y$, then
runs $V$ on $(y, w)$ and accepts when $V$ accepts and $|w| \le p(|y|)$; its declared time is the
declared time of $f(x)$ plus that of $V(y, w)$. Then $V'$ has polynomial declared time, and there
is a polynomial $p'$ with natural coefficients such that $V'$ verifies $L_1$ with witness bound
$p'$.

The proof takes $p' = p \circ r$ and the time bound $r(n) + q(r(n) + n)$ with $n = |x| + |w|$,
where $r$ bounds the declared time and output length of $f$ and $q$ bounds the declared time of
$V$.

Formalized by `Cslib.TimeMComplexity.verifies_comp_reduction`, a theorem declared in [CSLibExt/Computability/TimeMComplexity.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/TimeMComplexity.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-in-a-cost-annotated-programming/index.html#verifies-comp-reduction).

## A timed decider with polynomial-time output function gives membership in P

Let $L$ be
a decision problem and let $f$ assign to each bit string $x$ a timed computation, that is, a
Boolean return value together with a declared time in $\mathbb{N}$, whose return value equals
$L(x)$ for every $x$. If the function sending $x$ to the return value of $f(x)$ is
polynomial-time computable, then $L$ belongs to the class P.

The polynomial-time hypothesis must be proved for the specific decider: it does not follow from a
polynomial bound on the declared times, which are trusted annotations, since every decision
problem has a decider of declared time zero.

Formalized by `Cslib.TimeMComplexity.mem_P_of_decides`, a theorem declared in [CSLibExt/Computability/TimeMComplexity.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/TimeMComplexity.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-in-a-cost-annotated-programming/index.html#mem-p-of-decides).

## A timed verifier with polynomial-time output function puts its language in NP

Let $L$ be
a decision problem, $p$ a polynomial with natural-number coefficients, and $V$ a timed function
from pairs of lists of Booleans to Booleans that verifies $L$ with witness bound $p$. If the
function sending $(x, w)$ to the output of $V$ on $(x, w)$ is polynomial-time computable by a
Turing machine for the canonical bitstring encodings, then $L$ is in NP.

The polynomial-time hypothesis must be proved separately for $V$; it does not follow from any
bound on the declared time of $V$.

Formalized by `Cslib.TimeMComplexity.mem_NP_of_verifies`, a theorem declared in [CSLibExt/Computability/TimeMComplexity.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/TimeMComplexity.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-in-a-cost-annotated-programming/index.html#mem-np-of-verifies).

## From declared-time to polynomial-time many-one reductions

Let $L_1$ and $L_2$ be decision
problems and let $f$ be a declared-time many-one reduction from $L_1$ to $L_2$. If the function
sending $x$ to the output of $f$ on $x$ is polynomial-time computable by a Turing machine for the
canonical bitstring encodings, then $L_1$ reduces to $L_2$ by a polynomial-time many-one
reduction.

The polynomial-time hypothesis must be proved separately for $f$; it does not follow from the
declared-time bound.

Formalized by `Cslib.TimeMComplexity.cookLevinPolyManyOneRed_of_declared`, a theorem declared in [CSLibExt/Computability/TimeMComplexity.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/TimeMComplexity.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-in-a-cost-annotated-programming/index.html#cook-levin-poly-many-one-red-of-declared).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Polynomial time in a cost-annotated programming model](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-in-a-cost-annotated-programming/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-in-a-cost-annotated-programming)
