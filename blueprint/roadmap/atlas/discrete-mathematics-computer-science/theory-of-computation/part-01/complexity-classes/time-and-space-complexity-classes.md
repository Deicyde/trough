---
declaration: section
origin: cited
lean: Cslib.Complexity.Classes.langOf, Cslib.Complexity.Classes.PSPACE, Cslib.Complexity.Classes.EXP, Cslib.Complexity.Classes.EXPSPACE, Cslib.Complexity.Classes.E, Cslib.Complexity.Classes.LogSpace, Cslib.Complexity.Classes.LogSpaceComputable, Cslib.Complexity.Classes.LogSpaceRed
statement: formalized
proof: formalized
---

# Time and space complexity classes

117 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html).

## Language of a decision problem

The language of a decision problem $L$ is the set of
bitstrings $x$ with $L(x) = \mathrm{true}$.

Formalized by `Cslib.Complexity.Classes.langOf`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#lang-of).

## Polynomial space for decision problems

The class PSPACE of decision problems consists of
the decision problems $L$ whose language $\{x : L(x) = \mathrm{true}\}$ lies in the multi-tape
class PSPACE, that is, is decided by a multi-tape Turing machine that halts on every input and
uses space $O(n^d)$ for some natural number $d$.

Formalized by `Cslib.Complexity.Classes.PSPACE`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#pspace).

## The class EXP

EXP, deterministic exponential time, is the class of decision problems
$L$ for which there is a natural number $d$ such that the language of $L$, the set of bitstrings
$x$ with $L(x)$ true, belongs to $\mathrm{DTIME}(2^{n^d})$: it is decided by a multi-tape Turing
machine over the binary alphabet with finitely many states in time at most $c_1 2^{n^d} + c_2$
on inputs of length $n$, for some natural numbers $c_1$ and $c_2$.

Formalized by `Cslib.Complexity.Classes.EXP`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#exp).

## The class EXPSPACE

EXPSPACE, deterministic exponential space, is the class of
decision problems $L$ for which there is a natural number $d$ such that the language of $L$, the
set of bitstrings $x$ with $L(x)$ true, belongs to $\mathrm{DSPACE}(2^{n^d})$: it is decided by a
multi-tape Turing machine over the binary alphabet with finitely many states that halts on every
input and visits at most $c_1 2^{n^d} + c_2$ work-tape cells on inputs of length $n$, for some
natural numbers $c_1$ and $c_2$.

Formalized by `Cslib.Complexity.Classes.EXPSPACE`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#expspace).

## The class E

E is the class of decision problems $L$ for which there is a natural
number $c$ such that the language of $L$, the set of bitstrings $x$ with $L(x)$ true, belongs to
$\mathrm{DTIME}(2^{cn})$: it is decided by a multi-tape Turing machine over the binary alphabet
with finitely many states in time at most $c_1 2^{cn} + c_2$ on inputs of length $n$, for some
natural numbers $c_1$ and $c_2$.

Formalized by `Cslib.Complexity.Classes.E`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#e).

## Deterministic logarithmic space

The class $\mathsf{L}$ consists of the decision problems
$L$ for which there is a constant $c \in \mathbb{N}$ such that the language of $L$ lies in
$\mathrm{DSPACE}(s)$ for $s(n) = c \lfloor \log_2(n + 1) \rfloor + c$, the class of languages
decided by a multi-tape Turing machine with binary alphabet and finitely many states, within
some time bound, visiting at most $c_1 s(n) + c_2$ work-tape cells on inputs of length $n$ for
some constants $c_1$ and $c_2$.

Formalized by `Cslib.Complexity.Classes.LogSpace`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#log-space).

## Log-space computable functions

A function $f$ from bitstrings to bitstrings is
log-space computable when there are a constant $c \in \mathbb{N}$ and a time bound
$t : \mathbb{N} \to \mathbb{N}$ such that some multi-tape Turing machine with binary alphabet and
finitely many states, on every bitstring input $x$, halts with output $f(x)$ within $t(|x|)$
steps and visits at most $c \lfloor \log_2(|x| + 1) \rfloor + c$ work-tape cells in total.

Formalized by `Cslib.Complexity.Classes.LogSpaceComputable`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#log-space-computable).

## Log-space many-one reductions

A decision problem $L_1$ is log-space many-one reducible
to a decision problem $L_2$ when there is a log-space computable function $f$ from bitstrings to
bitstrings such that, for every bitstring $x$, $L_1(x)$ is true if and only if $L_2(f(x))$ is
true.

Formalized by `Cslib.Complexity.Classes.LogSpaceRed`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#log-space-red).

## Nondeterministic decision

A nondeterministic multi-tape Turing machine $M$ over the
boolean alphabet decides a set $L$ of bitstrings if, for every bitstring $x$, $x \in L$ if and
only if some computation path of $M$ on $x$ ends in a halted configuration whose output is the
one-element list $[\mathrm{true}]$.

Formalized by `Cslib.Complexity.Classes.NTMDecides`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#ntmdecides).

## Nondeterministic decision in bounded time

Let $M$ be a nondeterministic multi-tape
Turing machine over the boolean alphabet, $t : \mathbb{N} \to \mathbb{N}$ and $L$ a set of
bitstrings. Then $M$ decides $L$ in time $t$ if, for every input $x$, every computation path of
$M$ on $x$ with at least $t(|x|)$ steps ends in a halted configuration, where $|x|$ is the length
of $x$, and for every bitstring $x$, $x \in L$ if and only if some computation path of $M$ on $x$
ends in a halted configuration whose output is the one-element list $[\mathrm{true}]$.

Formalized by `Cslib.Complexity.Classes.NTMDecidesInTime`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#ntmdecides-in-time).

## Nondeterministic decision in bounded space

Let $M$ be a nondeterministic multi-tape
Turing machine over the boolean alphabet, $s : \mathbb{N} \to \mathbb{N}$ and $L$ a set of
bitstrings. Then $M$ decides $L$ in space $s$ if, for every input $x$, every computation path of
$M$ on $x$ visits at most $s(|x|)$ work-tape cells in total, where $|x|$ is the length of $x$,
and for every bitstring $x$, $x \in L$ if and only if some computation path of $M$ on $x$ ends in
a halted configuration whose output is the one-element list $[\mathrm{true}]$.

Formalized by `Cslib.Complexity.Classes.NTMDecidesInSpace`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#ntmdecides-in-space).

## Nondeterministic time classes

For $t : \mathbb{N} \to \mathbb{N}$, $\mathrm{NTIME}(t)$ is
the set of languages $L$ of bitstrings for which there are natural numbers $c_1$, $c_2$, $k$ and a
nondeterministic multi-tape Turing machine $M$ over the boolean alphabet with finitely many states
and $k$ work tapes that decides $L$ in time $c_1 t(n) + c_2$: on every input $x$, every
computation path of $M$ with at least $c_1 t(|x|) + c_2$ steps ends in a halted configuration,
where $|x|$ is the length of $x$, and $x \in L$ if and only if some computation path of $M$ on
$x$ ends in a halted configuration whose output is the one-element list $[\mathrm{true}]$.

Formalized by `Cslib.Complexity.Classes.NTIME`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#ntime).

## Nondeterministic space classes

For $s : \mathbb{N} \to \mathbb{N}$, $\mathrm{NSPACE}(s)$
is the set of languages $L$ of bitstrings for which there are natural numbers $c_1$, $c_2$, $k$
and a nondeterministic multi-tape Turing machine $M$ over the boolean alphabet with finitely many
states and $k$ work tapes that decides $L$ in space $c_1 s(n) + c_2$: on every input $x$, every
computation path of $M$ visits at most $c_1 s(|x|) + c_2$ work-tape cells in total, where $|x|$
is the length of $x$, and $x \in L$ if and only if some computation path of $M$ on $x$ ends in a
halted configuration whose output is the one-element list $[\mathrm{true}]$.

Formalized by `Cslib.Complexity.Classes.NSPACE`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#nspace).

## The complexity class NL

NL is the set of decision problems $L$ for which there is a
natural number $c$ such that the language of $L$ (the set of bitstrings on which $L$ is true)
belongs to $\mathrm{NSPACE}(s)$ for $s(n) = c \lfloor \log_2 (n + 1) \rfloor + c$, where
$\mathrm{NSPACE}(s)$ is the class of languages decided by a nondeterministic multi-tape Turing
machine with finitely many states in space $c_1 s(n) + c_2$ for some natural numbers $c_1, c_2$.

Formalized by `Cslib.Complexity.Classes.NL`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#nl).

## The complexity class NPSPACE

NPSPACE is the set of decision problems $L$ for which there
is a natural number $d$ such that the language of $L$ (the set of bitstrings on which $L$ is true)
belongs to $\mathrm{NSPACE}(s)$ for $s(n) = n^d$, where $\mathrm{NSPACE}(s)$ is the class of
languages decided by a nondeterministic multi-tape Turing machine with finitely many states in
space $c_1 s(n) + c_2$ for some natural numbers $c_1, c_2$.

Formalized by `Cslib.Complexity.Classes.NPSPACE`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#npspace).

## The complexity class NEXP

NEXP is the set of decision problems $L$ for which there is a
polynomial $p$ with natural-number coefficients such that the language of $L$ (the set of
bitstrings on which $L$ is true) belongs to $\mathrm{NTIME}(t)$ for $t(n) = 2^{p(n)}$, where
$\mathrm{NTIME}(t)$ is the class of languages decided by a nondeterministic multi-tape Turing
machine with finitely many states in time $c_1 t(n) + c_2$ for some natural numbers $c_1, c_2$.

Formalized by `Cslib.Complexity.Classes.NEXP`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#nexp).

## BPP

The class BPP of bounded-error probabilistic polynomial-time decision problems
consists of the decision problems $L$ for which there are a polynomial $p$ with natural number
coefficients and a polynomial-time computable function $R$ from pairs of bitstrings to booleans
such that, for every bitstring $x$, writing $m = p(|x|)$ and $c_x$ for the number of strings
$r \in \{0,1\}^m$ with $R(x, r)$ true: if $L(x)$ is true then $3 c_x \ge 2 \cdot 2^m$, and if
$L(x)$ is false then $3 c_x \le 2^m$. That is, for a uniformly random $r$, $R(x, r)$ is true with
probability at least $2/3$ on yes-instances and at most $1/3$ on no-instances.

Formalized by `Cslib.Complexity.Classes.BPP`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#bpp).

## Probabilistic polynomial time with unbounded error

The class PP consists of the decision
problems $L$ for which there are a polynomial $p$ with natural-number coefficients and a
polynomial-time computable function $R$ on pairs of bitstrings such that, for every bitstring $x$
and $r$ uniformly random among the bitstrings of length $p(|x|)$, the probability that $R(x, r)$
is true is greater than $1/2$ if $L(x)$ is true, and at most $1/2$ if $L(x)$ is false.

Formalized by `Cslib.Complexity.Classes.PP`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#pp).

## Polynomial time with polynomial advice

The class P/poly consists of the decision problems
$L$ for which there are a polynomial $p$ with natural-number coefficients, bitstrings
$a_0, a_1, a_2, \ldots$ with $|a_n| \le p(n)$ for every $n$, and a polynomial-time computable
function $R$ on pairs of bitstrings such that for every bitstring $x$, $L(x)$ is true if and only
if $R(x, a_{|x|})$ is true.

Formalized by `Cslib.Complexity.Classes.PPoly`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#ppoly).

## The counting class $\#P$

A function $f$ from bitstrings to natural numbers is in
$\#P$ when there are a polynomial $p$ with natural-number coefficients and a
polynomial-time computable Boolean function $R$ on pairs of bitstrings such that for every
bitstring $x$, $f(x)$ is the number of bitstrings $w$ of length exactly $p(|x|)$ for which
$R(x, w)$ is true.

Formalized by `Cslib.Complexity.Classes.SharpP`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#sharp-p).

## Evaluation of an oracle machine with adaptive queries

Let $\alpha$ be a type of
oracle answers and $\beta$ a type of outputs, and call a list of pairs of a bitstring and an
element of $\alpha$ a history. Fix a length cap $c \in \mathbb{N}$, a next-query function $N$
sending an input bitstring and a history to a bitstring, a decision function $F$ sending an
input bitstring and a history to an element of $\beta$, an oracle $O$ from bitstrings to
$\alpha$ and an input bitstring $x$. For a number $f \in \mathbb{N}$ of remaining queries and a
history $h$, the evaluation $E_f(h)$ is defined by recursion on $f$: $E_0(h) = F(x, h)$, and for
$E_{f+1}(h)$ let $q = N(x, h)$; if $q$ has length at most $c$, then $E_{f+1}(h) = E_f(h')$,
where $h'$ is $h$ with the pair $(q, O(q))$ appended at the end, and otherwise
$E_{f+1}(h) = F(x, h)$.

Dummy queries simulate early halting, so a fixed number of queries is without loss of
generality. At use sites the cap is polynomial in the length of $x$, so polynomial running time
of $N$ and $F$ on each call gives polynomial total running time in the length of $x$.

Formalized by `Cslib.Complexity.Classes.evalOracle`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#eval-oracle).

## Polynomial time with an oracle

For a Boolean oracle $O$ on bitstrings, the class
$\mathsf{P}^O$ consists of the decision problems $L$ for which there are polynomials $p$ and $q$
and polynomial-time functions $\mathrm{next}$ and $\mathrm{final}$ such that, for every
bitstring $x$, $L(x)$ is true exactly when the following oracle machine outputs true on $x$.
Starting from the empty history $h$, it runs $p(|x|)$ rounds; in each round it computes the
query $y = \mathrm{next}(x, h)$ from $x$ and the history $h$ of queries and answers so far,
and if $|y| \le q(|x|)$ it appends $(y, O(y))$ to $h$, while otherwise it skips all remaining
rounds. Finally it outputs $\mathrm{final}(x, h)$.

Formalized by `Cslib.Complexity.Classes.PWithOracle`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#pwith-oracle).

## NP relative to an oracle

Let $O$ be a function from bitstrings to booleans. The class
$\mathrm{NP}^O$ is the set of decision problems $L$ for which there are polynomials $p$ and $q$
with natural-number coefficients and polynomial-time computable functions $\mathrm{nextQ}$ and
$\mathrm{final}$, each taking a bitstring and a list of query/answer pairs, such that for every
bitstring $x$, $L(x)$ is true if and only if there is a bitstring $w$ of length at most $p(|x|)$,
where $|x|$ is the length of $x$, for which the oracle computation that chooses queries with
$\mathrm{nextQ}$ and decides with $\mathrm{final}$, run with oracle $O$, query-length cap $q(|x|)$
and $p(|x|)$ adaptive queries on the bitstring encoding of the pair $(x, w)$ from the empty
history, returns true.

Formalized by `Cslib.Complexity.Classes.NPWithOracle`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#npwith-oracle).

## Polynomial time with a #P oracle

The class $\mathsf{P}^{\#\mathsf{P}}$ consists of the
decision problems $L$ for which there are a function $f$ in $\#\mathsf{P}$, polynomials $p$ and
$q$, and polynomial-time functions $\mathrm{next}$ and $\mathrm{final}$ such that, for every
bitstring $x$, $L(x)$ is true exactly when the following oracle machine outputs true on $x$.
Starting from the empty history $h$, it runs $p(|x|)$ rounds; in each round it computes the
query $y = \mathrm{next}(x, h)$ from $x$ and the history $h$ of queries and their natural-number
answers so far, and if $|y| \le q(|x|)$ it appends $(y, f(y))$ to $h$, while otherwise it skips
all remaining rounds. Finally it outputs $\mathrm{final}(x, h)$.

Formalized by `Cslib.Complexity.Classes.PWithSharpP`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#pwith-sharp-p).

## $\#P$-complete functions

A function $f$ from bitstrings to natural numbers is
$\#P$-complete when $f$ is in $\#P$ and every function $g$ in $\#P$ is computed from $f$ by a
polynomial-time oracle machine. That is, there are polynomials $p$ and $q$ with natural-number
coefficients and polynomial-time computable functions choosing the next query and the final
natural-number answer from the input and the history of queries and oracle answers, such that
for every bitstring $x$ the following outputs $g(x)$: make up to $p(|x|)$ queries to $f$ in
turn, stop early as soon as the next query is longer than $q(|x|)$, and then return the final
answer computed from $x$ and the history.

Formalized by `Cslib.Complexity.Classes.SharpPComplete`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#sharp-pcomplete).

## Alternating bounded quantifiers

Let $b : \mathbb{N} \to \mathbb{N}$ be a length bound,
$k$ a natural number, $R$ a Boolean function of a bitstring and a list of bitstrings, and $x$ a
bitstring. The statement with $k$ blocks, beginning with $\exists$ when the given flag is true and
with $\forall$ when it is false, is

$$Q_1 w_1 \, Q_2 w_2 \cdots Q_k w_k \; R(x, [w_1, \dots, w_k]) = \mathrm{true},$$

where the quantifiers $Q_1, \dots, Q_k$ alternate between $\exists$ and $\forall$ and every $w_i$
ranges over the bitstrings of length at most $b(|x|)$. For $k = 0$ it is
$R(x, []) = \mathrm{true}$.

Formalized by `Cslib.Complexity.Classes.AltQuant`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#alt-quant).

## The class $\Sigma_k^p$

For a natural number $k$, a decision problem $L$ is in
$\Sigma_k^p$ when there are a polynomial $p$ with natural-number coefficients and a
polynomial-time computable Boolean function $R$ of a bitstring and a list of bitstrings such
that for every bitstring $x$, $L(x)$ is true if and only if
$Q_1 w_1\, Q_2 w_2 \cdots Q_k w_k$ with $R(x, [w_1, \dots, w_k])$ true, where $Q_i$ is $\exists$
for odd $i$ and $\forall$ for even $i$, and each $w_i$ ranges over bitstrings of length at
most $p(|x|)$. For $k = 0$ the condition is that $R(x, [\,])$ is true.

Formalized by `Cslib.Complexity.Classes.SigmaK`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#sigma-k).

## The universal levels of the polynomial hierarchy

For a natural number $k$, the class
$\Pi_k^p$ consists of the decision problems $L$ for which there are a polynomial $p$ with
natural-number coefficients and a polynomial-time computable function $R$, taking a bitstring and
a list of bitstrings to a boolean, such that for every bitstring $x$, $L(x)$ is true if and only
if

$$
\forall w_1\, \exists w_2\, \forall w_3 \cdots Q_k w_k\; R(x, [w_1, \ldots, w_k]) = \mathrm{true},
$$

where the $k$ quantifiers alternate starting with $\forall$ (so $Q_k$ is $\forall$ for odd $k$
and $\exists$ for even $k$) and each $w_i$ ranges over the bitstrings of length at most
$p(|x|)$. For $k = 0$ the condition is $R(x, []) = \mathrm{true}$.

Formalized by `Cslib.Complexity.Classes.PiK`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#pi-k).

## The polynomial hierarchy

The class PH is the union, over all natural numbers $k$, of the
classes $\Sigma_k^p$ of the polynomial hierarchy.

Formalized by `Cslib.Complexity.Classes.PH`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#ph).

## The class $\mathsf{AM}$ (Arthur–Merlin)

A decision problem $L$ on bitstrings is in
$\mathsf{AM}$ when there are polynomials $p$ and $q$ with natural-number coefficients and a
polynomial-time computable Boolean function $R(x, r, w)$ of three bitstrings such that, for every
bitstring $x$, writing $A_x$ for the set of strings $r \in \{0,1\}^{p(|x|)}$ for which some
bitstring $w$ of length at most $q(|x|)$ makes $R(x, r, w)$ true: if $L(x)$ is true then
$3|A_x| \ge 2 \cdot 2^{p(|x|)}$, and if $L(x)$ is false then $3|A_x| \le 2^{p(|x|)}$.

Here $r$ is Arthur's random string and $w$ is Merlin's reply, so for uniformly random $r$ the
acceptance probability is at least $2/3$ on yes-instances and at most $1/3$ on no-instances.

Formalized by `Cslib.Complexity.Classes.AM`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#am).

## The class coAM

**The class coAM.** coAM is the class of decision problems $L$ whose complement, the
decision problem that accepts exactly the bitstrings that $L$ rejects, belongs to AM.

Formalized by `Cslib.Complexity.Classes.coAM`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#co-am).

## Interactive-proof game

The game takes a length cap $c$, a verifier message function
$V_{\mathrm{msg}}$, a verifier decision function $V_{\mathrm{dec}}$, a prover $P$ mapping
transcripts (lists of bitstrings) to bitstrings, an input $x$, a coin string $\rho$, a number
$k$ of rounds and a transcript $t$, and returns a Boolean outcome. If $k = 0$, the outcome is
$V_{\mathrm{dec}}(x, \rho, t)$. Otherwise the verifier sends $m = V_{\mathrm{msg}}(x, \rho, t)$,
and the prover replies $a = P(t')$, where $t'$ is $t$ extended by $m$. If both $m$ and $a$ have
length at most $c$, the outcome is that of the game with $k - 1$ rounds and transcript $t$
extended by $m$ and then $a$; otherwise the outcome is false.

The transcript records only verifier messages and prover replies, so the prover never sees the
verifier's coins. At use sites the cap is polynomial in $|x|$, so polynomial time for each
verifier step gives polynomial total time in the original input.

Formalized by `Cslib.Complexity.Classes.IPGame`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#ipgame).

## The class IP

A decision problem $L$ is in $\mathsf{IP}$ when there are polynomials $s$,
$r$ and $q$ with natural-number coefficients and polynomial-time functions $V_{\mathrm{msg}}$
(the verifier's message function) and $V_{\mathrm{dec}}$ (its decision function) with the
following property. For a bitstring $x$, a prover $P$ (an arbitrary function from transcripts
to bitstrings) and a coin string $c$, let $G(P, c)$ be the outcome of the interactive-proof game
with message length cap $q(|x|)$, verifier $V_{\mathrm{msg}}$ and $V_{\mathrm{dec}}$, prover
$P$, input $x$, coins $c$, $r(|x|)$ rounds and the empty initial transcript. Then for every
bitstring $x$: if $L(x)$ is true, some prover $P$ makes $G(P, c)$ true for at least $2/3$ of
the coin strings $c \in \{0,1\}^{s(|x|)}$; and if $L(x)$ is false, every prover $P$ makes
$G(P, c)$ true for at most $1/3$ of them.

Formalized by `Cslib.Complexity.Classes.IP`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#ip).

## Probabilistically checkable proofs

For functions $r, q : \mathbb{N} \to \mathbb{N}$, the
class $\mathrm{PCP}(r, q)$ consists of the decision problems $L$ for which there are
polynomial-time computable functions $Q$ and $D$ such that $Q(x, \rho)$ is a list of at most
$q(|x|)$ natural numbers for all bitstrings $x$ and $\rho$, and such that for every bitstring $x$
the following holds. For a proof $\pi : \mathbb{N} \to \{\mathrm{true}, \mathrm{false}\}$, let
$\pi(Q(x, \rho))$ be the list of values of $\pi$ at the entries of $Q(x, \rho)$, and let
$P_\pi(x)$ be the probability, over a uniformly random bitstring $\rho$ of length $r(|x|)$, that
$D(x, \rho, \pi(Q(x, \rho)))$ is true. If $L(x)$ is true, then $P_\pi(x) \ge 2/3$ for some proof
$\pi$; if $L(x)$ is false, then $P_\pi(x) \le 1/3$ for every proof $\pi$.

The verifier is non-adaptive: the queried positions depend only on $x$ and $\rho$.

Formalized by `Cslib.Complexity.Classes.PCP`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#pcp).

## Gates of a flat Boolean circuit

A gate of a flat Boolean circuit on $n$ inputs is one of:
an input variable $x_i$ for some $i < n$; a Boolean constant; a negation gate with one predecessor
index $a \in \mathbb{N}$; a conjunction gate or a disjunction gate with a list of predecessor
indices; or a mod gate with a modulus $m \in \mathbb{N}$ and a list of predecessor indices.

Predecessors are referred to by their positions in the circuit; that gate $j$ refers only to
gates before $j$ is a separate well-formedness condition on circuits.

Formalized by `Cslib.Complexity.Classes.ACGate`, an inductive type declared in [CSLibExt/Computability/Complexity/Classes.lean, line 414](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L414). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#acgate).

## Predecessors of a gate

For a gate $g$ of a flat Boolean circuit on $n$ inputs, this is
the list of gate indices that $g$ reads: the empty list for an input variable or a constant, the
one-element list $[a]$ for the negation of gate $a$, and the argument list $l$ for an and, or or
mod gate with argument list $l$ (the modulus of a mod gate is not included).

Formalized by `Cslib.Complexity.Classes.gateInputs`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#gate-inputs).

## Well-formed flat circuits

A flat Boolean circuit on $n$ inputs, given as a list of
gates $(g_0, \dots, g_{m-1})$, is well-formed when every gate references only strictly earlier
gates: for every $j < m$, every gate index $a$ among the inputs of $g_j$ satisfies $a < j$.

Formalized by `Cslib.Complexity.Classes.WellFormedCircuit`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 432](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L432). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#well-formed-circuit).

## Value of a gate

Let $v$ be a list of Boolean values of earlier gates, where an index
outside $v$ reads as false, and let $\sigma$ assign a Boolean value to each of the $n$ inputs.
Given $v$ and $\sigma$, the value of the input variable $x_i$ is $\sigma(i)$; the value of the
constant $b$ is $b$; the value of the negation of gate $a$ is the negation of $v_a$; the value
of an and gate (or gate) with argument list $l$ is the conjunction (disjunction) of the values
$v_a$ for $a$ in $l$; and the value of a mod gate with modulus $m$ and argument list $l$ is false
if $m = 0$, and otherwise true exactly when the number of entries $a$ of $l$ with $v_a$ true,
counted with repetition, is divisible by $m$.

Formalized by `Cslib.Complexity.Classes.gateValue`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 436](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L436). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#gate-value).

## Evaluation of a flat Boolean circuit

For a circuit on $n$ inputs given as a list of
gates $g_0, \dots, g_{m-1}$ and an assignment $\alpha$ of booleans to the inputs, the list of
gate values is $(v_0, \dots, v_{m-1})$, where $v_j$ is computed from $v_0, \dots, v_{j-1}$, a
reference to a gate $a \ge j$ reading as false: an input gate $i$ has value $\alpha(i)$, a
constant gate has its constant, a negation gate on $a$ has value $\lnot v_a$, an and gate (or
gate) has the conjunction (disjunction) of the values it references, and a mod gate with
modulus $k$ is true if and only if $k \ne 0$ and the number of its references with value true,
counted with multiplicity, is divisible by $k$.

Formalized by `Cslib.Complexity.Classes.circuitEval`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 447](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L447). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#circuit-eval).

## Encoding a gate as a (kind, references) pair

A gate of a flat Boolean circuit on $n$
inputs is encoded as a pair of a natural number (its kind) and a list of natural numbers (its
references), the shared encoding used by decoding-based problems such as Circuit Value and
succinct circuits: the input variable $x_i$ is encoded as $(0, [i])$; the constant true as
$(1, [1])$ and the constant false as $(1, [0])$; the negation of gate $a$ as $(2, [a])$; the
conjunction of the gates listed in $r$ as $(3, r)$; and the disjunction of the gates listed in $r$
as $(4, r)$. Mod gates have no encoding of their own: every mod gate is encoded as $(5, [])$.

The serial evaluator reads kind $5$ as false.

Formalized by `Cslib.Complexity.Classes.acGateToPair`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 456](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L456). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#ac-gate-to-pair).

## Decoding a gate from its (kind, references) pair

A pair $(k, r)$ of a natural number $k$
and a list $r$ of natural numbers decodes to a gate of a flat Boolean circuit on $n$ inputs as
follows: $(0, [i])$ decodes to the input variable $x_i$ when $i < n$ and to the constant false
when $i \ge n$; $(1, [b])$ decodes to the constant that is true if and only if $b = 1$; $(2, [a])$
decodes to the negation of gate $a$; $(3, r)$ decodes to the conjunction of the gates listed in
$r$; and $(4, r)$ decodes to the disjunction of the gates listed in $r$. Every other pair,
including every pair of kind $5$ (the encoding of a mod gate), decodes to the constant false.

These defaults match the serial evaluator, which reads an unknown kind, and an input variable
with no corresponding input, as false.

Formalized by `Cslib.Complexity.Classes.acGateOfPair`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 469](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#ac-gate-of-pair).

## Evaluating a serialized gate

Let $v$ be a list of Boolean values of earlier gates,
let $a$ assign a Boolean to each of the $n$ inputs $0, \dots, n - 1$, and let $(k, \ell)$ be a
serialized gate. Write $v_c$ for entry $c$ of $v$, read as false when $c$ is out of range.
The value of the gate is: $a(i)$ if $(k, \ell) = (0, [i])$ with $i < n$, and false if
$(k, \ell) = (0, [i])$ with $i \ge n$; true exactly when $b = 1$ if $(k, \ell) = (1, [b])$;
the negation of $v_c$ if $(k, \ell) = (2, [c])$; the conjunction of the $v_c$ for $c$ in $\ell$
if $k = 3$; their disjunction if $k = 4$; and false in every other case.

Formalized by `Cslib.Complexity.Classes.serialGateEval`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 479](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L479). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#serial-gate-eval).

## Serial gate evaluation agrees with typed gate evaluation

For every list $v$ of Boolean
values of earlier gates, every assignment of Boolean values to the $n$ inputs and every pair
$g = (k, r)$ of a natural number $k$ (the gate kind) and a list $r$ of natural numbers (its
references), evaluating $g$ with the serial $(\mathrm{kind}, \mathrm{refs})$ gate evaluator
gives the same value as evaluating the gate decoded from $g$ with the gate-value function.

Formalized by `Cslib.Complexity.Classes.gateValue_ofPair`, a theorem declared in [CSLibExt/Computability/Complexity/Classes.lean, line 491](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L491). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#gate-value-of-pair).

## Depth of a gate

Let $d$ be the list of depths of the earlier gates of a flat Boolean
circuit on $n$ inputs, and for a gate index $a$ let $d_a$ be the entry of $d$ at (zero-based)
position $a$, or $0$ when $a$ is not a position of $d$. The depth of an input-variable gate or a
constant gate is $0$; the depth of a negation, AND, OR or modular gate is one more than the
maximum of $d_a$ over the gates $a$ it references, where the maximum over no gates is $0$.

Formalized by `Cslib.Complexity.Classes.gateDepthOf`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 521](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L521). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#gate-depth-of).

## Gate depths of a flat Boolean circuit

For a circuit given as a list of gates
$g_0, \dots, g_{m-1}$, the list of gate depths is $(d_0, \dots, d_{m-1})$, where $d_j = 0$ if
$g_j$ is an input or constant gate, and otherwise $d_j$ is one more than the maximum of the
depths $d_a$ of the gates $a$ that $g_j$ references (the maximum over no references is $0$),
a reference $a \ge j$ counting as depth $0$.

Formalized by `Cslib.Complexity.Classes.circuitDepths`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 530](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L530). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#circuit-depths).

## Depth of a flat Boolean circuit

The depth of a circuit, given as a list of gates, is
the maximum of the depths of its gates, and $0$ for the empty circuit. Input and constant gates
have depth $0$; a negation, and, or or mod gate has depth one more than the maximum depth of the
gates it references (the maximum over no references is $0$), where a reference to a gate that
does not come earlier in the list counts as depth $0$.

Formalized by `Cslib.Complexity.Classes.circuitDepth`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 534](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L534). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#circuit-depth).

## Circuits without mod gates

A flat Boolean circuit $C$ on $n$ inputs is mod-free when
none of its gates is a mod gate.

Formalized by `Cslib.Complexity.Classes.IsModFree`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 538](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L538). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#is-mod-free).

## Circuits whose modular gates have a fixed modulus

For a natural number $m$, a flat
Boolean circuit on $n$ inputs satisfies the modulus-$m$ condition when every $\mathrm{mod}$
gate in it has modulus exactly $m$; gates of the other kinds are unrestricted.

Formalized by `Cslib.Complexity.Classes.ModOnly`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 544](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L544). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#mod-only).

## Monotone circuits

A flat circuit $C$ on $n$ input variables, given as a list of gates, is
monotone when every gate of $C$ is an input variable, an AND gate or an OR gate. Constant, NOT
and mod gates are not allowed.

Formalized by `Cslib.Complexity.Classes.IsMonotoneCircuit`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 550](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L550). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#is-monotone-circuit).

## The class $\mathsf{AC}^0$

A decision problem $L$ on bitstrings is in $\mathsf{AC}^0$ when
there are a depth bound $d$, a polynomial $p$ with natural-number coefficients and, for every
$n$, a flat Boolean circuit $C_n$ on $n$ inputs such that for every $n$: every gate of $C_n$
refers only to earlier gates; $C_n$ has no mod gates; $C_n$ has at most $p(n)$ gates and depth at
most $d$; and for every bitstring $x$ of length $n$, $L(x)$ is true if and only if $C_n$ has a
last gate and the value of that gate on input $x$ is true.

The and and or gates have unbounded fan-in, and the family $(C_n)$ need not be uniform.

Formalized by `Cslib.Complexity.Classes.AC0`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 558](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L558). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#ac0).

## The class $\mathsf{AC}^0(m)$

For a natural number $m$, a decision problem $L$ on
bitstrings is in $\mathsf{AC}^0[m]$ when there are a depth bound $d$, a polynomial $p$ with
natural-number coefficients and, for every $n$, a flat Boolean circuit $C_n$ on $n$ inputs such
that for every $n$: every gate of $C_n$ refers only to earlier gates; every mod gate of $C_n$ has
modulus $m$; $C_n$ has at most $p(n)$ gates and depth at most $d$; and for every bitstring $x$ of
length $n$, $L(x)$ is true if and only if $C_n$ has a last gate and the value of that gate on
input $x$ is true.

The and and or gates have unbounded fan-in, the family $(C_n)$ need not be uniform, and a circuit
with no mod gates also qualifies.

Formalized by `Cslib.Complexity.Classes.AC0Mod`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 567](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L567). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#ac0-mod).

## The class $\mathsf{ACC}^0$

$\mathsf{ACC}^0$ is the union of the classes
$\mathsf{AC}^0[m]$ over all natural numbers $m$: a decision problem is in $\mathsf{ACC}^0$ when it
is in $\mathsf{AC}^0[m]$ for some $m$. A circuit family witnessing membership uses one fixed
modulus $m$ throughout.

Formalized by `Cslib.Complexity.Classes.ACC0`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 577](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L577). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#acc0).

## The parity language

The parity decision problem accepts a bitstring exactly when an odd
number of its entries are true.

Formalized by `Cslib.Complexity.Classes.parityDec`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 580](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L580). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#parity-dec).

## The majority language

The majority language is the decision problem that accepts a
bitstring $x$ exactly when $x$ has more true bits than false bits, that is, when $2k > |x|$,
where $k$ is the number of true bits of $x$ and $|x|$ is its length.

Formalized by `Cslib.Complexity.Classes.majorityDec`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 584](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L584). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#majority-dec).

## The class RP

A decision problem $L$ is in $\mathsf{RP}$ when there are a polynomial
$p$ with natural-number coefficients and a polynomial-time computable Boolean function $R$
on pairs of bitstrings such that for every bitstring $x$: if $L(x)$ is true, then $R(x, r)$
is true for at least half of the $2^{p(|x|)}$ bitstrings $r$ of length $p(|x|)$; and if
$L(x)$ is false, then $R(x, r)$ is false for every bitstring $r$ of length $p(|x|)$.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Definition 7.2; M. Sipser, Introduction to the Theory of Computation, 3rd ed., 2013, Definition 10.8.

Formalized by `Cslib.Complexity.Classes.RP`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 594](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L594). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#rp).

## The class coRP

**The class coRP.** coRP is the class of decision problems $L$ whose complement, the
decision problem that accepts exactly the bitstrings that $L$ rejects, belongs to RP.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Definition 7.2; M. Sipser, Introduction to the Theory of Computation, 3rd ed., 2013, Definition 10.8.

Formalized by `Cslib.Complexity.Classes.coRP`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 607](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L607). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#co-rp).

## Membership in coRP

A decision problem $L$ belongs to $\mathsf{coRP}$ if and only if its
complement, the decision problem that accepts exactly the bitstrings $L$ rejects, belongs to
$\mathsf{RP}$.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Definition 7.2.

Formalized by `Cslib.Complexity.Classes.mem_coRP`, a theorem declared in [CSLibExt/Computability/Complexity/Classes.lean, line 612](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L612). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#mem-co-rp).

## ZPP

The class $\mathsf{ZPP}$ (zero-error probabilistic polynomial time) is defined as
the set of decision problems that lie in both $\mathsf{RP}$ and $\mathsf{coRP}$, that is,
$\mathsf{ZPP} = \mathsf{RP} \cap \mathsf{coRP}$.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Definition 7.2 (where `ZPP` is defined as this intersection); M. Sipser, Introduction to the Theory of Computation, 3rd ed., 2013, Definition 10.8.

Formalized by `Cslib.Complexity.Classes.ZPP`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 618](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L618). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#zpp).

## ZPP is the intersection of RP and coRP

The class $\mathsf{ZPP}$ equals
$\mathsf{RP} \cap \mathsf{coRP}$; here this holds by definition.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Definition 7.2.

Formalized by `Cslib.Complexity.Classes.zpp_eq`, a theorem declared in [CSLibExt/Computability/Complexity/Classes.lean, line 623](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L623). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#zpp-eq).

## ZPP is contained in RP

Every decision problem in $\mathsf{ZPP}$ lies in
$\mathsf{RP}$, that is, $\mathsf{ZPP} \subseteq \mathsf{RP}$.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Definition 7.2.

Formalized by `Cslib.Complexity.Classes.zpp_subset_rp`, a theorem declared in [CSLibExt/Computability/Complexity/Classes.lean, line 628](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L628). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#zpp-subset-rp).

## ZPP is contained in coRP

Every decision problem in $\mathsf{ZPP}$ lies in
$\mathsf{coRP}$, that is, $\mathsf{ZPP} \subseteq \mathsf{coRP}$.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Definition 7.2.

Formalized by `Cslib.Complexity.Classes.zpp_subset_corp`, a theorem declared in [CSLibExt/Computability/Complexity/Classes.lean, line 633](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L633). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#zpp-subset-corp).

## The class MA (Merlin–Arthur)

A decision problem $L$ is in $\mathsf{MA}$ when there are
polynomials $p$ and $q$ with natural-number coefficients and a polynomial-time computable
predicate $R$ on triples $(x, w, r)$ of bitstrings such that, for every bitstring $x$, with
$N_x(w)$ the number of strings $r$ of length $p(|x|)$ for which $R(x, w, r)$ is true: if $L(x)$
is true, then some $w$ with $|w| \le q(|x|)$ satisfies $3 N_x(w) \ge 2 \cdot 2^{p(|x|)}$; and if
$L(x)$ is false, then every $w$ with $|w| \le q(|x|)$ satisfies $3 N_x(w) \le 2^{p(|x|)}$.

So Merlin sends a witness $w$ first and Arthur then flips $p(|x|)$ coins $r$: Arthur accepts
with probability at least $2/3$ for some $w$ on yes-instances, and with probability at most
$1/3$ for every $w$ on no-instances. In the class AM the random string comes before the
witness.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Definition 8.1; L. Babai, "Trading group theory for randomness", Proceedings of the Seventeenth Annual ACM Symposium on Theory of Computing (STOC 1985), 421-429.

Formalized by `Cslib.Complexity.Classes.MA`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 649](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#ma).

## The class coMA

**The class coMA.** coMA is the class of decision problems $L$ whose complement, the
decision problem that accepts exactly the bitstrings that $L$ rejects, belongs to MA.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Definition 8.1.

Formalized by `Cslib.Complexity.Classes.coMA`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 665](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L665). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#co-ma).

## Membership in coMA

A decision problem $L$ belongs to $\mathsf{coMA}$ if and only if its
complement, the decision problem that accepts exactly the bitstrings $L$ rejects, belongs to
$\mathsf{MA}$.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Definition 8.1.

Formalized by `Cslib.Complexity.Classes.mem_coMA`, a theorem declared in [CSLibExt/Computability/Complexity/Classes.lean, line 670](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L670). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#mem-co-ma).

## Serial circuits

A serial circuit is a list of pairs $(k, \ell)$, where $k$ is a
natural number (the gate kind) and $\ell$ is a list of natural numbers (the gate's references).

A flat circuit is serialized gate by gate into this form: kind $0$ is an input variable,
kind $1$ a constant, kind $2$ a negation, kind $3$ a conjunction and kind $4$ a
disjunction, while a modular-counting gate, which has no serial form here, becomes $(5, [\,])$.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Chapter 6 (circuit encodings).

Formalized by `Cslib.Complexity.Classes.SerialCircuit`, an abbreviation declared in [CSLibExt/Computability/Complexity/Classes.lean, line 678](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L678). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#serial-circuit).

## Log-space uniform circuit families

A family $(C_n)_{n \in \mathbb{N}}$ of flat Boolean
circuits, $C_n$ having $n$ inputs, is log-space uniform when there is a log-space computable
function $D$ on bitstrings such that, for every $n$, decoding $D(1^n)$ (where $1^n$ is the string
of $n$ ones) as a list of (gate kind, references) pairs succeeds and returns the serial encoding
of $C_n$, that is, the list of the serial encodings of its gates in order. Since $1^n$ has
length $n$, the description is computed in space $O(\log n)$.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Definition 6.21 (log-space uniformity); M. Sipser, Introduction to the Theory of Computation, 3rd ed., 2013, Definition 9.20.

Formalized by `Cslib.Complexity.Classes.UniformCircuitFamily`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 687](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L687). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#uniform-circuit-family).

## Circuits of fan-in at most two

A flat Boolean circuit $C$ on $n$ inputs has fan-in at
most two when every and gate, or gate and mod gate of $C$ has an argument list of length at
most $2$.

Bounded fan-in is what $\mathsf{NC}$ requires: without it, the $\mathsf{NC}^k$ circuit classes
would be the unbounded-fan-in classes $\mathsf{AC}^k$.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Definition 6.21; M. Sipser, Introduction to the Theory of Computation, 3rd ed., 2013, Definition 9.20.

Formalized by `Cslib.Complexity.Classes.IsFanInLeTwo`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 698](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L698). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#is-fan-in-le-two).

## The class NC^k

For a natural number $k$, a decision problem $L$ is in $\mathsf{NC}^k$
when there are a constant $c$, a polynomial $p$ with natural number coefficients and a
log-space uniform family of flat Boolean circuits $(C_n)_{n \in \mathbb{N}}$, where $C_n$ has
$n$ inputs, such that for every $n$ the circuit $C_n$ is well formed, has no $\mathrm{mod}$
gates, has at most two inputs at every and gate and every or gate, has at most $p(n)$ gates,
has depth at most $c \cdot (\lfloor \log_2 (n + 1) \rfloor + 1)^k$, and, for every bitstring
$x$ of length $n$, $L$ accepts $x$ exactly when $C_n$ has a last gate and that gate evaluates
to true on input $x$.

So $\mathsf{NC}^k$ consists of the problems decided by log-space uniform circuit families of
polynomial size, fan-in at most $2$ and depth $O(\log^k n)$, and $\mathsf{NC}^0$ is constant
depth. Bounded fan-in is essential: with unbounded fan-in this would be $\mathsf{AC}^k$.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Definition 6.21; M. Sipser, Introduction to the Theory of Computation, 3rd ed., 2013, Definition 9.20.

Formalized by `Cslib.Complexity.Classes.NCK`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 712](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L712). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#nck).

## The class NC

$\mathsf{NC}$ is the complexity class of decision problems that belong to
$\mathsf{NC}^k$ for some natural number $k$, that is, $\mathsf{NC} = \bigcup_{k} \mathsf{NC}^k$.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Definition 6.21; M. Sipser, Introduction to the Theory of Computation, 3rd ed., 2013, Definition 9.20.

Formalized by `Cslib.Complexity.Classes.NC`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 726](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L726). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#nc).

## NC is the union of its levels

The class $\mathsf{NC}$ equals the union
$\bigcup_{k \in \mathbb{N}} \mathsf{NC}^k$ of the classes $\mathsf{NC}^k$ over all natural
numbers $k$; this holds by definition.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Definition 6.21.

Formalized by `Cslib.Complexity.Classes.nc_eq`, a theorem declared in [CSLibExt/Computability/Complexity/Classes.lean, line 731](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L731). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#nc-eq).

## Membership in NC

A decision problem $L$ belongs to $\mathsf{NC}$ if and only if $L$
belongs to $\mathsf{NC}^k$ for some natural number $k$.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Definition 6.21.

Formalized by `Cslib.Complexity.Classes.mem_nc`, a theorem declared in [CSLibExt/Computability/Complexity/Classes.lean, line 736](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L736). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#mem-nc).

## The NC hierarchy is increasing

For every natural number $k$, every decision problem in
$\mathsf{NC}^k$ is in $\mathsf{NC}^{k+1}$, that is, $\mathsf{NC}^k \subseteq \mathsf{NC}^{k+1}$.

The depth bound of $\mathsf{NC}^k$, a constant times $(\lfloor \log_2 (n + 1) \rfloor + 1)^k$, is
monotone in $k$ because its base is at least $1$.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Definition 6.21.

Formalized by `Cslib.Complexity.Classes.nck_mono`, a theorem declared in [CSLibExt/Computability/Complexity/Classes.lean, line 742](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L742). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#nck-mono).

## Encoded rational number

A rational number is encoded as a triple $(s, a, b)$ of a
boolean $s$ and natural numbers $a$ and $b$, read as the sign, the numerator and the
denominator.

## Sources

- A. Y. Kitaev, A. H. Shen, and M. N. Vyalyi, Classical and Quantum Computation, American Mathematical Society, 2002, Section 14.4 (rational gate entries).

Formalized by `Cslib.Complexity.Classes.RatEnc`, an abbreviation declared in [CSLibExt/Computability/Complexity/Classes.lean, line 758](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L758). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#rat-enc).

## Rational number of an encoding

A triple $(s, p, q)$, with $s$ a boolean and $p, q$
natural numbers, encodes the rational number $-p/q$ when $s$ is true and $p/q$ when $s$ is
false; when $q = 0$ the value is $0$, since division by zero gives $0$.

## Sources

- A. Y. Kitaev, A. H. Shen, and M. N. Vyalyi, Classical and Quantum Computation, American Mathematical Society, 2002, Section 14.4.

Formalized by `Cslib.Complexity.Classes.toRat`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 763](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L763). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#to-rat).

## Complex number of a pair of rational encodings

A pair $(e_1, e_2)$ of rational
encodings encodes the complex number $q_1 + q_2 i$, where $q_1$ and $q_2$ are the rational
numbers encoded by $e_1$ and $e_2$.

## Sources

- A. Y. Kitaev, A. H. Shen, and M. N. Vyalyi, Classical and Quantum Computation, American Mathematical Society, 2002, Section 14.4.

Formalized by `Cslib.Complexity.Classes.toComplex`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 769](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L769). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#to-complex).

## Binary digit of a natural number

For natural numbers $k$ and $i$, this is the digit of
$i$ at position $k$ in binary, counting from the least significant digit at position $0$, that
is, $\lfloor i / 2^k \rfloor \bmod 2$, taken as an element of $\{0, 1\}$.

## Sources

- A. Y. Kitaev, A. H. Shen, and M. N. Vyalyi, Classical and Quantum Computation, American Mathematical Society, 2002, Section 14.4.

Formalized by `Cslib.Complexity.Classes.qBit`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 775](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L775). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#q-bit).

## Index of a pair of bits

A pair $(a, b)$ of bits $a, b \in \{0, 1\}$ has index $2a + b$,
its position in the enumeration $(0, 0), (0, 1), (1, 0), (1, 1)$ of the four pairs.

## Sources

- A. Y. Kitaev, A. H. Shen, and M. N. Vyalyi, Classical and Quantum Computation, American Mathematical Society, 2002, Section 14.4.

Formalized by `Cslib.Complexity.Classes.qIdx2`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 781](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L781). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#q-idx2).

## Matrix encoded by a list of entries

Number the pairs $(a, b)$ with $a, b \in \{0, 1\}$
by $2a + b$, and index the rows and columns of a $4 \times 4$ complex matrix by these pairs.
Given a list $e$ of pairs of encoded rational numbers, the matrix of $e$ has in row $p$ and
column $q$ the complex number whose real part is the first and whose imaginary part is the
second rational of the entry of $e$ at position $4p + q$ (counting from $0$, with $p$ and $q$
replaced by their numbers), and $0$ when $e$ has no entry at that position. A list of $16$
pairs thus lists the entries in row-major order.

## Sources

- A. Y. Kitaev, A. H. Shen, and M. N. Vyalyi, Classical and Quantum Computation, American Mathematical Society, 2002, Section 14.4.

Formalized by `Cslib.Complexity.Classes.matrixOfEntries`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 787](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L787). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#matrix-of-entries).

## Setting two bits of an index

For natural numbers $N$, $s$, $i$, $j$ and a pair
$b = (b_1, b_2)$ of bits, this is the index in $\{0, \dots, 2^N - 1\}$ given by
$(s - s_i 2^i - s_j 2^j + b_1 2^i + b_2 2^j) \bmod 2^N$, where $s_k$ is bit $k$ of $s$ and
each subtraction of natural numbers is truncated at $0$. When $i \ne j$ this is $s$ with
bit $i$ set to $b_1$ and bit $j$ set to $b_2$, reduced modulo $2^N$.

## Sources

- A. Y. Kitaev, A. H. Shen, and M. N. Vyalyi, Classical and Quantum Computation, American Mathematical Society, 2002, Section 14.4.

Formalized by `Cslib.Complexity.Classes.setBits`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 795](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L795). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#set-bits).

## Encoded 2-local quantum gate

A 2-local quantum gate is encoded as a triple $(i, j, e)$
of natural numbers $i$ and $j$, the qubits it acts on, and a list $e$ of pairs of encoded
rational numbers, the real and imaginary parts of the entries of its $4 \times 4$ matrix in
row-major order.

The encoding itself does not require $e$ to have $16$ entries or the matrix to be unitary;
unitarity and the qubit bounds are part of well-formedness.

## Sources

- A. Y. Kitaev, A. H. Shen, and M. N. Vyalyi, Classical and Quantum Computation, American Mathematical Society, 2002, Section 14.4.

Formalized by `Cslib.Complexity.Classes.QGate`, an abbreviation declared in [CSLibExt/Computability/Complexity/Classes.lean, line 803](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L803). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#qgate).

## Well-formed quantum gate

A 2-local gate acting on qubits $i$ and $j$ with entry list $e$
is well-formed on $N$ qubits when $i < j < N$ and the $4 \times 4$ complex matrix $U$ encoded by
$e$ is unitary, that is, $U^* U = I$.

## Sources

- A. Y. Kitaev, A. H. Shen, and M. N. Vyalyi, Classical and Quantum Computation, American Mathematical Society, 2002, Section 14.4.

Formalized by `Cslib.Complexity.Classes.QGateWellFormed`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 809](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L809). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#qgate-well-formed).

## Applying a 2-local gate to a state

Let $N$ be a number of qubits, and let a gate consist
of two qubit positions $i$ and $j$ together with a list of entries encoding a $4 \times 4$ complex
matrix $U$ whose rows and columns are indexed by pairs of bits. For a state vector $\psi$ on $N$
qubits, that is, a function from $\{0, \dots, 2^N - 1\}$ to $\mathbb{C}$, applying the gate gives
the state whose value at a basis index $s$ is
$\sum_{b \in \{0,1\}^2} U_{(s_i, s_j), b} \, \psi(s[b])$. Here
$s_k = \lfloor s / 2^k \rfloor \bmod 2$ is bit $k$ of $s$, and for $b = (b_1, b_2)$ the index
$s[b]$ is $(s - s_i 2^i - s_j 2^j + b_1 2^i + b_2 2^j) \bmod 2^N$, with truncated subtraction of
natural numbers; when $i \ne j$ and $i, j < N$, this is $s$ with bits $i$ and $j$ replaced by
$b_1$ and $b_2$.

## Sources

- M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information, Cambridge University Press, 2000, Chapter 4 (unitary evolution).

Formalized by `Cslib.Complexity.Classes.applyGate`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 816](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L816). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#apply-gate).

## Applying a quantum circuit to a state

For a state vector $\psi \in \mathbb{C}^{2^N}$ on
$N$ qubits and a list of 2-local gates $g_1, \dots, g_k$, the result of applying the circuit to
$\psi$ is obtained by applying the gate $g_1$ to $\psi$, then $g_2$ to the result, and so on up to
$g_k$. For the empty list it is $\psi$ itself.

## Sources

- M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information, Cambridge University Press, 2000, Chapter 4 (quantum circuits).

Formalized by `Cslib.Complexity.Classes.applyCircuit`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 824](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L824). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#apply-circuit).

## Number with a given binary expansion

A list $b_0, b_1, \ldots, b_{n-1}$ of booleans,
read as bits with true as $1$ and false as $0$, denotes the natural number
$\sum_{i < n} b_i 2^i$; the first entry is the least significant bit.

## Sources

- M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information, Cambridge University Press, 2000, Chapter 1 (computational basis).

Formalized by `Cslib.Complexity.Classes.qNumOf`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 831](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L831). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#q-num-of).

## Computational basis state of a bitstring

For a bitstring $x = (x_0, \dots, x_{n-1})$,
reading true as $1$ and false as $0$, the computational basis state of $x$ is the vector
$\psi : \{0, \dots, 2^n - 1\} \to \mathbb{C}$ with $\psi(s) = 1$ if $s = \sum_{k < n} x_k 2^k$
(the number whose binary expansion is $x$, least significant bit first) and $\psi(s) = 0$
otherwise.

## Sources

- M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information, Cambridge University Press, 2000, Chapter 1 (computational basis).

Formalized by `Cslib.Complexity.Classes.basisState`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 838](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L838). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#basis-state).

## Tensor product of state vectors

For vectors $\varphi \in \mathbb{C}^{2^a}$ and
$\psi \in \mathbb{C}^{2^b}$, indexed by $\{0, \dots, 2^a - 1\}$ and $\{0, \dots, 2^b - 1\}$, their
tensor product is the vector in $\mathbb{C}^{2^{a+b}}$ whose entry at $s$ is
$\varphi_{s \bmod 2^a}\, \psi_{\lfloor s / 2^a \rfloor}$. Thus $\varphi$ occupies the low-order $a$
bits of the index and $\psi$ the high-order $b$ bits.

## Sources

- M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information, Cambridge University Press, 2000, Chapter 2 (tensor products).

Formalized by `Cslib.Complexity.Classes.tensorProd`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 844](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L844). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#tensor-prod).

## All-zero state

The all-zero state on $a$ qubits is the vector in $\mathbb{C}^{2^a}$,
indexed by $s \in \{0, \dots, 2^a - 1\}$, whose entry at $s = 0$ is $1$ and whose other
entries are $0$; that is, the computational basis state $|0 \cdots 0\rangle$.

## Sources

- M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information, Cambridge University Press, 2000, Chapter 1 (computational basis).

Formalized by `Cslib.Complexity.Classes.zeroState`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 857](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L857). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#zero-state).

## Squared norm of a state vector

For a vector $\psi \in \mathbb{C}^{2^m}$, indexed by
$\{0, \dots, 2^m - 1\}$, its squared norm is the real number
$\sum_{s} \overline{\psi_s}\, \psi_s = \sum_{s} |\psi_s|^2$.

## Sources

- M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information, Cambridge University Press, 2000, Chapter 2 (Born rule).

Formalized by `Cslib.Complexity.Classes.sqNorm`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 863](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L863). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#sq-norm).

## Acceptance probability of a quantum state

For a state vector $\psi$ on $N$ qubits, given
by its amplitudes $\psi(s) \in \mathbb{C}$ at the basis states $s \in \{0, \dots, 2^N - 1\}$, the
acceptance probability is the sum of $|\psi(s)|^2$ over the basis states $s$ whose qubit $0$ (the
output qubit, the least significant bit of $s$) equals $1$. By the Born rule, for a unit vector
$\psi$ this is the probability that measuring the output qubit gives $1$.

## Sources

- M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information, Cambridge University Press, 2000, Chapter 2 (Born rule, measurement).

Formalized by `Cslib.Complexity.Classes.acceptProb`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 870](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L870). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#accept-prob).

## Initial state of a BQP computation

For a bitstring $x = (x_0, \dots, x_{n-1})$, with
true read as $1$ and false as $0$, and a number $a$ of ancilla qubits, the initial state is the
tensor product of the computational basis state of $x$ and the all-zero state on $a$ qubits: the
vector on $\{0, \dots, 2^{n+a} - 1\}$ whose value at $s$ is the value of the basis state of $x$ at
$s \bmod 2^n$ times the value of the all-zero state at $\lfloor s / 2^n \rfloor$. So $x$ occupies
the $n$ low-order bits of the index, and the state equals $1$ at the index $\sum_{k < n} x_k 2^k$
and $0$ elsewhere.

## Sources

- M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information, Cambridge University Press, 2000, Chapter 4 (quantum circuits); S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Definition 10.1.

Formalized by `Cslib.Complexity.Classes.bqpInitState`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 879](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L879). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#bqp-init-state).

## BQP

The class BQP of bounded-error quantum polynomial-time decision problems consists
of the decision problems $L$ for which there are polynomials $a$ and $q$ with natural number
coefficients and a polynomial-time computable map sending each bitstring $x$ to a list of
2-local quantum gates such that, for every bitstring $x$, with $n = |x|$ and $N = n + a(n)$:
the list has at most $q(n)$ gates; each gate acts on qubits $i < j < N$ and its $4 \times 4$
matrix, whose entries have rational real and imaginary parts, is unitary; and after the gates
are applied in order to the state with $x$ in the computational basis on the $n$ low-order
qubits and $a(n)$ ancilla qubits in state $0$, the probability that qubit $0$ measures $1$ is
at least $2/3$ if $L(x)$ is true and at most $1/3$ if $L(x)$ is false.

## Sources

- S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Definition 10.1; M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information, Cambridge University Press, 2000, Chapter 4; E. Bernstein and U. Vazirani, "Quantum complexity theory", SIAM Journal on Computing 26 (1997), 1411-1473.

Formalized by `Cslib.Complexity.Classes.BQP`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 893](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L893). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#bqp).

## Optimization problems

An optimization problem consists of a function $v$ assigning a
rational value $v(x, s)$ to every instance $x$ and every candidate solution $s$, both bitstrings;
a feasibility predicate saying whether $s$ is a feasible solution for $x$; and a polynomial $p$
with natural-number coefficients such that every feasible solution $s$ for $x$ has length at
most $p(|x|)$. It is required that $v(x, s) \ge 0$ for all $x$ and $s$, that $v(x, s) = 0$
whenever $s$ is not feasible for $x$, and that every instance has a feasible solution.

The problem is read as a maximization problem. The structure carries no computational content:
polynomial-time feasibility and a polynomial-time encoding of the objective form a separate
predicate (NPO), which the approximation classes APX, PTAS and FPTAS require.

## Sources

- C. H. Papadimitriou and M. Yannakakis, "Optimization, approximation, and complexity classes", Journal of Computer and System Sciences 43 (1991), 425-440; S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Chapter 11.

Formalized by `Cslib.Complexity.Classes.OptProblem`, a structure declared in [CSLibExt/Computability/Complexity/Classes.lean, line 919](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L919). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#opt-problem).

## Approximation ratio at a precision

Let $P$ be a maximization problem with objective
value $\mathrm{val}(x, s)$ for instance $x$ and solution $s$, let $A$ be an algorithm taking a
pair of bitstrings, let $k$ be a natural number and let $\rho$ be a rational number. Then $A$
achieves ratio $\rho$ on $P$ at precision $k$ when, for every instance $x$ and every feasible
solution $s$ of $x$, the output $y = A(x, 1^k)$ of $A$ on $x$ and the unary string $1^k$ of $k$
ones is a feasible solution of $x$ with $\rho \cdot \mathrm{val}(x, s) \le \mathrm{val}(x, y)$.

Since every instance has a feasible solution, the output is then always feasible and worth at
least $\rho$ times the value of every feasible solution. The approximation classes share this
call convention: a fully polynomial-time approximation scheme is one algorithm achieving ratio
$1 - 1/k$ at every precision $k \ge 1$, a polynomial-time approximation scheme has such an
algorithm for each $k \ge 1$ separately, and APX asks for some ratio $\rho$ with $0 < \rho \le 1$
at precision $2$.

## Sources

- C. H. Papadimitriou and M. Yannakakis, "Optimization, approximation, and complexity classes", Journal of Computer and System Sciences 43 (1991), 425-440; S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Chapter 11.

Formalized by `Cslib.Complexity.Classes.ApproxAt`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 947](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L947). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#approx-at).

## NPO optimization problems

Let $P$ be an optimization problem whose instances $x$ and
solutions $s$ are bitstrings, with rational value $\mathrm{val}(x, s)$ and feasibility predicate
$\mathrm{feas}(x, s)$. Then $P$ is an NPO problem when the map $(x, s) \mapsto \mathrm{feas}(x, s)$
is polynomial-time computable, and there is a polynomial-time computable map $\mathrm{enc}$
sending each pair $(x, s)$ to a triple $(b, a, d)$ of a boolean and two natural numbers such
that, for all $x$ and $s$: $d \neq 0$; if $s$ is feasible for $x$, then
$\mathrm{val}(x, s) = \sigma a / d$, where $\sigma = -1$ if $b$ is true and $\sigma = 1$
otherwise; and if $s$ is not feasible for $x$, then $\mathrm{val}(x, s) = 0$.

The approximation classes APX, PTAS and FPTAS all require this condition. Without it, a problem
could hide an undecidable feasibility relation while assigning value $0$ everywhere, and the
constant empty-solution algorithm would vacuously satisfy the approximation guarantees.

## Sources

- C. H. Papadimitriou and M. Yannakakis, "Optimization, approximation, and complexity classes", Journal of Computer and System Sciences 43 (1991), 425-440; S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Chapter 11.

Formalized by `Cslib.Complexity.Classes.IsNPO`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 967](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L967). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#is-npo).

## Constant-factor approximable problems

A maximization problem $P$ is in $\mathsf{APX}$
when $P$ is an NPO problem and there are a rational number $\rho$ with $0 < \rho \le 1$ and a
polynomial-time algorithm $A$ such that, for every instance $x$ and every feasible solution $s$
for $x$, the output $A(x, 1^2)$ of $A$ on $x$ with the unary precision tape of length $2$ is a
feasible solution for $x$ whose value is at least $\rho$ times the value of $s$.

The ratio $\rho$ is the fraction of the optimum achieved, the reciprocal of the convention
$\rho \ge 1$ in which the value is at least the optimum divided by $\rho$. The NPO
requirement is part of the class: without it, a problem that is not NPO and has value $0$
everywhere would qualify vacuously.

## Sources

- C. H. Papadimitriou and M. Yannakakis, "Optimization, approximation, and complexity classes", Journal of Computer and System Sciences 43 (1991), 425-440; S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Chapter 11.

Formalized by `Cslib.Complexity.Classes.IsAPX`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 985](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L985). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#is-apx).

## The class APX

APX is the set of maximization problems $P$ that are NP optimization
problems (feasibility is decidable in polynomial time, and a polynomial-time computable map
sends every instance-solution pair to a signed fraction with nonzero denominator that equals the
objective value whenever the solution is feasible) and for which there are a rational number
$\rho$ with $0 < \rho \le 1$ and a polynomial-time algorithm $A$ achieving ratio $\rho$ on $P$ at
precision $2$: for every instance $x$ and every feasible solution $s$ of $x$, the output $y$ of
$A$ on $x$ and the unary precision string $11$ is a feasible solution of $x$ whose value is at
least $\rho$ times the value of $s$.

## Sources

- C. H. Papadimitriou and M. Yannakakis, "Optimization, approximation, and complexity classes", Journal of Computer and System Sciences 43 (1991), 425-440.

Formalized by `Cslib.Complexity.Classes.APX`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 994](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L994). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#apx).

## Polynomial-time approximation schemes

An optimization problem $P$, with value
$\mathrm{val}(x, s)$ of a solution $s$ for an instance $x$, admits a polynomial-time
approximation scheme when $P$ is an NPO problem and for every integer $k \ge 1$ there is a
polynomial-time computable algorithm $A$ on pairs of bitstrings with the following property:
for every instance $x$ and every feasible solution $s$ for $x$, the output $A(x, 1^k)$ on $x$
and the string $1^k$ of $k$ true bits is a feasible solution for $x$ with
$(1 - 1/k)\,\mathrm{val}(x, s) \le \mathrm{val}(x, A(x, 1^k))$. That is, $A$ achieves
approximation ratio $1 - 1/k$, an error of $\varepsilon = 1/k$; the algorithm may depend on $k$.

## Sources

- C. H. Papadimitriou and M. Yannakakis, "Optimization, approximation, and complexity classes", Journal of Computer and System Sciences 43 (1991), 425-440; S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Chapter 11.

Formalized by `Cslib.Complexity.Classes.IsPTAS`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 1002](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L1002). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#is-ptas).

## The class PTAS

PTAS is the set of optimization problems $P$ that are NPO problems
(feasibility is decidable in polynomial time and the objective value is given by a
polynomial-time computable rational encoding) and that have a polynomial-time approximation
scheme: for every natural number $k \ge 1$ there is a polynomial-time algorithm $A$ such that,
for every instance $x$ and every feasible solution $s$ of $x$, the output of $A$ on $x$ and the
string of $k$ ones is a feasible solution of $x$ whose value is at least $(1 - 1/k)$ times the
value of $s$.

## Sources

- C. H. Papadimitriou and M. Yannakakis, "Optimization, approximation, and complexity classes", Journal of Computer and System Sciences 43 (1991), 425-440.

Formalized by `Cslib.Complexity.Classes.PTAS`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 1011](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L1011). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#ptas).

## Fully polynomial-time approximation schemes

A maximization problem $P$ has an FPTAS
when $P$ is an NPO problem and there is one polynomial-time algorithm $A$ such that, for every
integer $k \ge 1$, every instance $x$ and every feasible solution $s$ for $x$, the output
$A(x, 1^k)$ of $A$ on $x$ with the unary precision tape of length $k$ is a feasible solution for
$x$ whose value is at least $1 - 1/k$ times the value of $s$.

Since the precision tape is unary, polynomial time in the total input length is polynomial
time in $|x|$ and $1/\varepsilon$, where $\varepsilon = 1/k$.

## Sources

- C. H. Papadimitriou and M. Yannakakis, "Optimization, approximation, and complexity classes", Journal of Computer and System Sciences 43 (1991), 425-440; S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Chapter 11.

Formalized by `Cslib.Complexity.Classes.IsFPTAS`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 1020](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L1020). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#is-fptas).

## The class FPTAS

FPTAS is the class of optimization problems that have a fully
polynomial-time approximation scheme.

## Sources

- C. H. Papadimitriou and M. Yannakakis, "Optimization, approximation, and complexity classes", Journal of Computer and System Sciences 43 (1991), 425-440.

Formalized by `Cslib.Complexity.Classes.FPTAS`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 1029](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L1029). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#fptas).

## FPTAS is contained in PTAS

Every optimization problem in the class FPTAS of
problems with a fully polynomial-time approximation scheme belongs to the class PTAS of
problems with a polynomial-time approximation scheme.

The single fully polynomial-time algorithm serves as the algorithm for every precision $k$.

## Sources

- C. H. Papadimitriou and M. Yannakakis, "Optimization, approximation, and complexity classes", Journal of Computer and System Sciences 43 (1991), 425-440.

Formalized by `Cslib.Complexity.Classes.fptas_subset_ptas`, a theorem declared in [CSLibExt/Computability/Complexity/Classes.lean, line 1035](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L1035). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#fptas-subset-ptas).

## PTAS is contained in APX

Every optimization problem in the class PTAS belongs to the
class APX.

The algorithm that the approximation scheme provides for error $1/2$ achieves the constant
ratio $1/2$.

## Sources

- C. H. Papadimitriou and M. Yannakakis, "Optimization, approximation, and complexity classes", Journal of Computer and System Sciences 43 (1991), 425-440.

Formalized by `Cslib.Complexity.Classes.ptas_subset_apx`, a theorem declared in [CSLibExt/Computability/Complexity/Classes.lean, line 1044](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L1044). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#ptas-subset-apx).

## Negligible functions

A function $e : \mathbb{N} \to \mathbb{Q}$ is negligible if for
every natural number $c$ there is a natural number $N$ such that $e(n) \le 1 / n^c$ for all
natural numbers $n \ge N$.

## Sources

- O. Goldreich, Foundations of Cryptography, Vol. 1, Cambridge University Press, 2001, Section 2.2.

Formalized by `Cslib.Complexity.Classes.Negligible`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 1058](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L1058). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#negligible).

## Inversion success probability

Let $f$ be a family of functions, $f_n$ mapping $n$-bit
strings to bitstrings, and let $A$ be an inverter mapping a triple $(n, y, r)$ of a length $n$,
an output $y$ and a coin string $r$ to a bitstring. For natural numbers $n$ and $m$, the
inversion success probability of $A$ against $f$ at length $n$ with $m$ coins is the fraction of
the $2^{n+m}$ pairs $(x, r)$ of an $n$-bit string $x$ and an $m$-bit string $r$ such that
$f_n(x') = f_n(x)$, where $x'$ is the $n$-bit string whose $i$-th bit is the $i$-th bit of
$A(n, f_n(x), r)$, or false when that output has no $i$-th bit.

The inverter receives the length $n$ explicitly: when output lengths vary, it could not
otherwise recover $n$ from $f_n(x)$ alone.

## Sources

- O. Goldreich, Foundations of Cryptography, Vol. 1, Cambridge University Press, 2001, Section 2.2.

Formalized by `Cslib.Complexity.Classes.invertSucc`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 1071](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L1071). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#invert-succ).

## One-way function families

Let $f$ assign to each $n \in \mathbb{N}$ and each $n$-bit
string $x$ a bitstring $f_n(x)$. The family $f$ is one-way when three conditions hold. First, its
output lengths are polynomially bounded: some polynomial $p$ satisfies $|f_n(x)| \le p(n)$ for
all $n$ and $x$. Second, it is uniformly computable: some polynomial-time computable function
maps the bitstring encoding of the pair $(n, x)$ to $f_n(x)$ for all $n$ and $x$. Third, it is
hard to invert: for every polynomial $q$ with natural-number coefficients and every
polynomial-time computable inverter $A$ on triples $(n, y, r)$ of a natural number and two
bitstrings, the inversion success probability of $A$ against $f$ at length $n$ with $q(n)$
coins is negligible in $n$, that is, for every $c \in \mathbb{N}$ it is at most $1 / n^c$ for
all large enough $n$. Here the inversion success probability is the fraction of pairs $(x, r)$
of an $n$-bit string $x$ and a $q(n)$-bit string $r$ for which the $n$-bit string $x'$ formed
by the first $n$ bits of $A(n, f_n(x), r)$, with missing bits false, satisfies
$f_n(x') = f_n(x)$.

Deterministic inverters are the special case that ignores the coins. The uniform evaluator is
essential: per-length polynomial-size circuits would admit arbitrary noncomputable families.

## Sources

- O. Goldreich, Foundations of Cryptography, Vol. 1, Cambridge University Press, 2001, Section 2.2; R. Impagliazzo, "A personal view of average-case complexity", Proceedings of the Tenth Annual Structure in Complexities Theory Conference (1995), 134-147.

Formalized by `Cslib.Complexity.Classes.IsOneWayFunction`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 1090](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L1090). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#is-one-way-function).

## Inversion success probability against a permutation family

Let $\pi$ be a family of
maps $\pi_n$ from $n$-bit strings to $n$-bit strings, let $A$ be a function sending a natural
number and two bitstrings to a bitstring, and let $n$ and $m$ be natural numbers. For a bitstring
$w$, write $\mathrm{trunc}_n(w)$ for the $n$-bit string whose bit at each position $i < n$ is the
entry of $w$ at position $i$, or false if $w$ has at most $i$ entries. The success probability of
$A$ against $\pi$ at length $n$ with $m$ coins is the rational number $N / 2^{n+m}$, where $N$ is
the number of pairs $(x, c)$ of an $n$-bit string $x$ and an $m$-bit string $c$ with
$\pi_n(\mathrm{trunc}_n(A(n, \pi_n(x), c))) = \pi_n(x)$, where $\pi_n(x)$ is passed to $A$ as a
bitstring.

Here $A$ is a probabilistic inverter that receives the security parameter $n$, the image
$\pi_n(x)$ and the coins $c$.

## Sources

- O. Goldreich, Foundations of Cryptography, Vol. 1, Cambridge University Press, 2001, Section 2.2.

Formalized by `Cslib.Complexity.Classes.permInvertSucc`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 1105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L1105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#perm-invert-succ).

## One-way permutation families

Let $\pi$ assign to each $n \in \mathbb{N}$ a map $\pi_n$
from $n$-bit strings to $n$-bit strings. The family $\pi$ is a one-way permutation when three
conditions hold. First, each $\pi_n$ is injective, hence a permutation of the $n$-bit strings.
Second, it is uniformly computable: some polynomial-time computable function maps the
bitstring encoding of the pair $(n, x)$ to $\pi_n(x)$ for all $n$ and all $n$-bit strings $x$.
Third, it is hard to invert: for every polynomial $q$ with natural-number coefficients and every
polynomial-time computable inverter $A$ on triples $(n, y, r)$ of a natural number and two
bitstrings, the inversion success probability of $A$ against $\pi$ at length $n$ with $q(n)$
coins is negligible in $n$, that is, for every $c \in \mathbb{N}$ it is at most $1 / n^c$ for
all large enough $n$. Here the inversion success probability is the fraction of pairs $(x, r)$
of an $n$-bit string $x$ and a $q(n)$-bit string $r$ for which the $n$-bit string $x'$ formed
by the first $n$ bits of $A(n, \pi_n(x), r)$, with missing bits false, satisfies
$\pi_n(x') = \pi_n(x)$.

## Sources

- O. Goldreich, Foundations of Cryptography, Vol. 1, Cambridge University Press, 2001, Section 2.2.

Formalized by `Cslib.Complexity.Classes.IsOneWayPermutation`, a definition declared in [CSLibExt/Computability/Complexity/Classes.lean, line 1118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L1118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#is-one-way-permutation).

## One-way permutations are one-way functions

Let $\pi$ be a one-way permutation family, so
that each $\pi_n$ maps $n$-bit strings to $n$-bit strings. Then the family that sends an $n$-bit
string $x$ to the bitstring $\pi_n(x)$ is a one-way function family.

Length preservation gives the polynomial output bound, the evaluator of $\pi$ serves unchanged,
and the inversion success probabilities coincide because an $n$-bit string is determined by the
list of its bits.

## Sources

- O. Goldreich, Foundations of Cryptography, Vol. 1, Cambridge University Press, 2001, Section 2.2.

Formalized by `Cslib.Complexity.Classes.one_way_permutation_implies_one_way_function`, a theorem declared in [CSLibExt/Computability/Complexity/Classes.lean, line 1134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Classes.lean#L1134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#one-way-permutation-implies-one-way-func).

## Polynomial-time machines have polynomially bounded output

A polynomial-time machine has polynomially bounded encoded output.

Formalized by `Cslib.Complexity.Preimage.output_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/Preimage.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Preimage.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#output-length-le).

## Polynomial-time maps run on unframed bit lists

Canonical polynomial-time maps can also be run on unframed bit lists.

Formalized by `Cslib.Complexity.Preimage.raw_computable`, a theorem declared in [CSLibExt/Computability/Complexity/Preimage.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Preimage.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#raw-computable).

## Mapping the first component of a pair is polynomial-time

Mapping the first component of an encoded pair is polynomial-time;
the second component is preserved, not recomputed or guessed.

Formalized by `MetaMathlibExt.ComplexityTheory.IsPolyTime.map_fst`, a theorem declared in [CSLibExt/Computability/Complexity/Preimage.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Preimage.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#map-fst).

## Output of a polynomial-time map is polynomial in raw input length

Encoded output length is polynomial in the unframed input length.

Formalized by `MetaMathlibExt.ComplexityTheory.IsPolyTime.length_bound`, a theorem declared in [CSLibExt/Computability/Complexity/Preimage.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Preimage.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#length-bound).

## Preimage of SAT under a polynomial-time map is in NP

Pulling SAT back along a polynomial map preserves NP membership.
SAT verifier soundness holds even for certificates above its length bound.

Formalized by `MetaMathlibExt.ComplexityTheory.satDec_comp_mem_NP`, a theorem declared in [CSLibExt/Computability/Complexity/Preimage.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Preimage.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#sat-dec-comp-mem-np).

## NP is closed under polynomial-time preimages

Canonical NP is closed under polynomial-time preimages.
Cook–Levin supplies a verifier sound for arbitrarily long certificates,
so enlarging the transformed witness bound introduces no false positives.

Formalized by `MetaMathlibExt.ComplexityTheory.comp_mem_NP`, a theorem declared in [CSLibExt/Computability/Complexity/Preimage.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Preimage.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#comp-mem-np).

## NP membership pulls back along polynomial many-one reductions

NP membership transfers backwards along a polynomial many-one reduction.

Formalized by `MetaMathlibExt.ComplexityTheory.mem_NP_of_polyManyOneRed`, a theorem declared in [CSLibExt/Computability/Complexity/Preimage.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Preimage.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#mem-np-of-poly-many-one-red).

## coNP is closed under polynomial-time preimages

Canonical coNP is closed under polynomial-time preimages.

Formalized by `MetaMathlibExt.ComplexityTheory.comp_mem_coNP`, a theorem declared in [CSLibExt/Computability/Complexity/Preimage.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Preimage.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#comp-mem-co-np).

## Polynomial many-one reductions also reduce complements

The same reduction function reduces the complements.

Formalized by `Cslib.CookLevin.PolyManyOneRed.compl`, a theorem declared in [CSLibExt/Computability/Complexity/Preimage.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/Preimage.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html#compl).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Time and space complexity classes](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/complexity-classes/time-and-space-complexity-classes)
