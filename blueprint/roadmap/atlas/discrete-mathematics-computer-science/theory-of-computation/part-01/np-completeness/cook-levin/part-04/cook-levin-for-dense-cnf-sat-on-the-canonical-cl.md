---
declaration: section
origin: cited
lean: Cslib.Complexity.CookLevin.Hardness.symSetX, Cslib.Complexity.CookLevin.Hardness.encX, Cslib.Complexity.CookLevin.Hardness.encX_acc, Cslib.Complexity.CookLevin.Hardness.vacc, Cslib.Complexity.CookLevin.Hardness.vE, Cslib.Complexity.CookLevin.Hardness.veqv, Cslib.Complexity.CookLevin.Hardness.vι, Cslib.Complexity.CookLevin.Hardness.vsep
statement: formalized
proof: formalized
---

# Cook-Levin for dense CNF-SAT on the canonical classes

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html).

## An encoding whose output alphabet contains a chosen accept symbol

## Effective alphabets with an adjoined accept symbol

For a finite multi-stack Turing
machine $M$, a symbol $a$ of its output-stack alphabet and a stack $k$, this is the finite set of
symbols that some statement of $M$ can push on stack $k$ (together with the whole input alphabet
when $k$ is the input stack), with $a$ added when $k$ is the output stack.

Formalized by `Cslib.Complexity.CookLevin.Hardness.symSetX`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Hardness.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Hardness.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html#sym-set-x).

## Tableau encoding with a chosen accept symbol

Given a finite multi-stack Turing machine
$M$ and a symbol $a$ of its output-stack alphabet, this is the encoding of $M$ that numbers the
stacks and the pairs (optional label, state) through their finite enumerations, and whose
effective alphabet on each stack $k$ is the set of symbols some statement of $M$ can push on $k$
(plus the whole input alphabet if $k$ is the input stack), with $a$ added if $k$ is the output
stack. A symbol in that set has code one more than its position in it; any other symbol has
code $0$.

Formalized by `Cslib.Complexity.CookLevin.Hardness.encX`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Hardness.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Hardness.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html#enc-x).

## The chosen accept symbol is encodable

Let $M$ be a finite multi-stack Turing machine and
let $a$ be a symbol of its output-stack alphabet. In the tableau encoding of $M$ with $a$ adjoined
to the output alphabet, some index of the effective output-stack alphabet decodes to $a$.

This discharges, for every machine, the accept-symbol hypothesis of the correctness theorem for
the assembled formula.

Formalized by `Cslib.Complexity.CookLevin.Hardness.encX_acc`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Hardness.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Hardness.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html#enc-x-acc).

## Accept symbol of the verifier

Let $V$ be a polynomial-time machine computing a function
of pairs of bit lists from their pair encoding, whose output alphabet is identified with the
Booleans. The accept symbol is the output symbol of $V$ that corresponds to $\mathrm{true}$.

Formalized by `Cslib.Complexity.CookLevin.Hardness.vacc`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Hardness.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Hardness.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html#vacc).

## Tableau encoding of the verifier

For a polynomial-time Turing machine $V$ that computes a
Boolean function on pairs of bit strings, reading a pair $(a, y)$ as the bits of $a$, a separator,
then the bits of $y$, and writing its answer as one bit, this is the tableau encoding of $V$ whose
effective output alphabet is enlarged by the accept symbol: the output symbol of $V$ for true.

Formalized by `Cslib.Complexity.CookLevin.Hardness.vE`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Hardness.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Hardness.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html#v-e).

## Bits as indices

The bijection from $\{0, 1\}$, the indices below the number $2$ of
Booleans, onto the Booleans that is inverse to the fixed enumeration of the Booleans.

Formalized by `Cslib.Complexity.CookLevin.Hardness.veqv`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Hardness.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Hardness.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html#veqv).

## Input-bit symbol of the verifier

Let $V$ be a polynomial-time machine computing a
function of pairs of bit lists from their pair encoding, whose input alphabet is identified with
the pair alphabet $\mathrm{Bool} \oplus \mathrm{Option}\ \mathrm{Bool}$, and let $\beta$ be the
fixed bijection from $\{0, 1\}$ onto the Booleans. For an index $i \in \{0, 1\}$, this is the
symbol of $V$'s input alphabet that corresponds to the left-tagged bit $\mathrm{inl}(\beta(i))$.

Formalized by `Cslib.Complexity.CookLevin.Hardness.vι`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Hardness.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Hardness.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html#v).

## Separator symbol of the verifier

Let $V$ be a polynomial-time machine computing a
function of pairs of bit lists from their pair encoding, whose input alphabet is identified with
the pair alphabet $\mathrm{Bool} \oplus \mathrm{Option}\ \mathrm{Bool}$. This is the symbol of
$V$'s input alphabet that corresponds to the separator $\#$, the element
$\mathrm{inr}(\mathrm{none})$.

Formalized by `Cslib.Complexity.CookLevin.Hardness.vsep`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Hardness.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Hardness.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html#vsep).

## Certificate symbol of the verifier

Let $V$ be a polynomial-time machine computing a
function of pairs of bit lists from their pair encoding, whose input alphabet is identified with
the pair alphabet $\mathrm{Bool} \oplus \mathrm{Option}\ \mathrm{Bool}$. For a bit $g$, this is the
symbol of $V$'s input alphabet that corresponds to the right-tagged bit
$\mathrm{inr}(\mathrm{some}\ g)$.

Formalized by `Cslib.Complexity.CookLevin.Hardness.vY`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Hardness.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Hardness.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html#v-y).

## Certificate symbols of the verifier

Let $V$ be a polynomial-time machine computing a
function of pairs of bit lists from their pair encoding, whose input alphabet is identified with
the pair alphabet $\mathrm{Bool} \oplus \mathrm{Option}\ \mathrm{Bool}$. This is the list of the
symbols of $V$'s input alphabet corresponding to the right-tagged bits
$\mathrm{inr}(\mathrm{some}\ g)$ for $g = \mathrm{true}$ and $g = \mathrm{false}$, each once, in
the order of a fixed enumeration of the Booleans.

Formalized by `Cslib.Complexity.CookLevin.Hardness.vYs`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Hardness.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Hardness.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html#v-ys).

## Offset of the verifier's time bound

Let $V$ be a polynomial-time machine computing a
function of pairs of bit lists from their pair encoding, with time polynomial $t_V$. This is a
natural number $c \ge 1$, fixed by choice, such that for some exponent $e$ we have
$t_V(j) \le (j + c)^e$ for every natural number $j$.

Formalized by `Cslib.Complexity.CookLevin.Hardness.vc`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Hardness.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Hardness.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html#vc).

## Exponent of the verifier's time bound

Let $V$ be a polynomial-time machine computing a
function of pairs of bit lists from their pair encoding, with time polynomial $t_V$, and let
$c \ge 1$ be the offset of its time bound, fixed by choice so that some exponent works. This is
an exponent $e$, fixed by choice, with $t_V(j) \le (j + c)^e$ for every natural number $j$.

Formalized by `Cslib.Complexity.CookLevin.Hardness.ve`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Hardness.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Hardness.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html#ve).

## Input of the verifier on a pair

Let $V$ be a polynomial-time machine computing a function
of pairs of bit lists from their pair encoding, whose input alphabet is identified with the pair
alphabet $\mathrm{Bool} \oplus \mathrm{Option}\ \mathrm{Bool}$, and let $\beta$ be the fixed
bijection from $\{0, 1\}$ onto the Booleans. For bit lists $a$ and $y$, translating the pair
encoding $a \# y$ symbol by symbol into $V$'s input alphabet gives the input-bit symbols of the
indices $\beta^{-1}(b)$ for the bits $b$ of $a$ in order, then the separator symbol, then the
certificate symbols of the bits of $y$ in order.

Formalized by `Cslib.Complexity.CookLevin.Hardness.v_input`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Hardness.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Hardness.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html#v-input).

## The verifier's run settles on its output

Let $V$ be a machine that computes a function
$f_v$ of pairs of bit lists from their pair encoding, within $t_V(n)$ steps on an encoding of
length $n$ for a polynomial $t_V$ with natural-number coefficients, with input alphabet
identified with the pair alphabet $\mathrm{Bool} \oplus \mathrm{Option}\ \mathrm{Bool}$ and output
alphabet identified with the Booleans. Let $a$, $y$ be bit lists of lengths $|a|$, $|y|$, and $T$ a
natural number with $t_V(|a| + 1 + |y|) \le T$. Start $V$ in its initial configuration with its
input stack holding the symbols for the left-tagged bits $\mathrm{inl}(b)$ of $a$, then the
separator $\mathrm{inr}(\mathrm{none})$, then the symbols for the right-tagged bits
$\mathrm{inr}(\mathrm{some}\ b)$ of $y$, and run it for $T$ steps, a halted configuration staying
unchanged. The result is the halted configuration, in the initial internal state, whose output
stack holds exactly the one output symbol for $f_v(a, y)$ and whose other stacks are empty.

Formalized by `Cslib.Complexity.CookLevin.Hardness.v_run`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Hardness.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Hardness.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html#v-run).

## The Cook–Levin reduction

Let $V$ be a polynomial-time Turing machine that computes a
Boolean function on pairs of bit strings, reading a pair $(a, y)$ as the bits of $a$, a separator,
then the bits of $y$, and writing its answer as one bit; let $t$ be its time bound and fix
constants $c \ge 1$ and $e$ with $t(j) \le (j + c)^e$ for all $j$. For a polynomial $p$ with
natural-number coefficients, the reduction sends a bit string $a$ of length $n$ to the dense bit
encoding of the tableau formula $\Phi$ of $V$, built with the encoding of $V$ whose output
alphabet contains the output symbol $\mathrm{acc}$ for true, for the input prefix $x$ made of the
bits of $a$ followed by the separator, the certificate symbols of $V$ (one per bit) as the
allowed symbols after $x$, the accept symbol $\mathrm{acc}$, width $m = n + 1 + p(n)$ and
$T = (m + c)^e$ steps.

Formalized by `Cslib.Complexity.CookLevin.Hardness.red`, a definition declared in [CSLibExt/Computability/Complexity/CookLevin/Hardness.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Hardness.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html#red).

## Correctness of the reduction

Let $V$ be a polynomial-time Turing machine that computes a
Boolean function $f$ on pairs of bit strings, reading a pair $(a, y)$ as the bits of $a$, a
separator, then the bits of $y$, and writing its answer as one bit. Let $p$ be a polynomial with
natural-number coefficients, $R$ a relation on bit strings with $R(a, y)$ iff $f(a, y)$ is true,
and $L'$ a predicate on bit strings such that $L'(a)$ holds iff some bit string $y$ of length at
most $p(|a|)$ satisfies $R(a, y)$. Then for every bit string $a$, $L'(a)$ holds iff the image of
$a$ under the reduction built from $V$ and $p$ is in CNF-SAT.

Formalized by `Cslib.Complexity.CookLevin.Hardness.v_correct`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Hardness.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Hardness.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html#v-correct).

## The Cook–Levin reduction is polynomial-time

Let $V$ be a polynomial-time Turing machine
that computes a Boolean function on pairs of bit strings, reading a pair $(a, y)$ as the bits of
$a$, a separator, then the bits of $y$, and writing its answer as one bit. For every polynomial
$p$ with natural-number coefficients, the reduction built from $V$ and $p$ is polynomial-time
computable with respect to the canonical bit-string encodings.

Formalized by `Cslib.Complexity.CookLevin.Hardness.isPolyTime_red`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Hardness.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Hardness.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html#is-poly-time-red).

## Every NP problem reduces to dense CNF-SAT

Every decision problem $L$ in NP has a
polynomial-time many-one reduction to dense CNF-SAT: a polynomial-time computable map $f$ on bit
strings such that, for every bit string $x$, $L$ accepts $x$ exactly when dense CNF-SAT accepts
$f(x)$.

Formalized by `Cslib.Complexity.CookLevin.Hardness.denseSatDec_npHard`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Hardness.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Hardness.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html#dense-sat-dec-np-hard).

## Cook-Levin for dense CNF-SAT

Dense CNF-SAT is NP-complete: it lies in NP, and every
decision problem in NP has a polynomial-time many-one reduction to dense CNF-SAT.

Formalized by `Cslib.Complexity.CookLevin.Hardness.denseSatDec_npComplete`, a theorem declared in [CSLibExt/Computability/Complexity/CookLevin/Hardness.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/CookLevin/Hardness.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html#dense-sat-dec-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cook-Levin for dense CNF-SAT on the canonical classes](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/cook-levin-for-dense-cnf-sat-on-the-canonical-cl)
