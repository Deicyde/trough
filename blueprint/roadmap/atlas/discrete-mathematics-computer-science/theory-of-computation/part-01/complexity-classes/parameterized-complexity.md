---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.Parameterized.ParamProblem, MetaMathlibExt.Complexity.KeyTheorems.Parameterized.FPTTime, MetaMathlibExt.Complexity.KeyTheorems.Parameterized.FPT, MetaMathlibExt.Complexity.KeyTheorems.Parameterized.FPTReduces, MetaMathlibExt.Complexity.KeyTheorems.Parameterized.WCGate, MetaMathlibExt.Complexity.KeyTheorems.Parameterized.wcCircuitEval, MetaMathlibExt.Complexity.KeyTheorems.Parameterized.wcGatePreds, MetaMathlibExt.Complexity.KeyTheorems.Parameterized.wcGateWeft
statement: formalized
---

# Parameterized complexity

16 results, 15 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/parameterized-complexity/index.html).

## Parameterized problems

A parameterized problem is a function that assigns a boolean
answer to every pair of a bitstring (a finite list of booleans) $x$ and a natural-number
parameter $k$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Parameterized.ParamProblem`, an abbreviation declared in [WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/parameterized-complexity/index.html#param-problem).

## FPT time

Let $\beta$ be a type with a canonical bitstring encoding. A function $R$
from pairs $(x, k)$ of a bitstring $x$ and a natural number $k$ to $\beta$ is computable in FPT
time when there are a computable function $f : \mathbb{N} \to \mathbb{N}$ and a
polynomial-time computable function $A$ from pairs of bitstrings to $\beta$ such that
$R(x, k) = A(x, 1^{f(k)})$ for every bitstring $x$ and every $k \in \mathbb{N}$, where
$1^{f(k)}$ is the list of $f(k)$ booleans all equal to true.

Padding the input with $f(k)$ entries in this way is equivalent to a running time of
$F(k) \cdot p(n)$ for a computable $F$ and a polynomial $p$, where $n$ is the length of $x$;
the padding function must be computable, since otherwise every predicate on the parameter would
be fixed-parameter tractable.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Parameterized.FPTTime`, a definition declared in [WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/parameterized-complexity/index.html#fpttime).

## Fixed-parameter tractable problems

A parameterized problem $P$ is fixed-parameter
tractable when there is a function $D$, from pairs $(x, k)$ of a bitstring $x$ and a natural
number $k$ to booleans, that is computable in FPT time and satisfies $P(x, k) = D(x, k)$ for
every bitstring $x$ and every $k \in \mathbb{N}$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Parameterized.FPT`, a definition declared in [WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/parameterized-complexity/index.html#fpt).

## FPT-reductions

A parameterized problem $P$ FPT-reduces to a parameterized problem $Q$
when there are a map $R$, sending each pair $(x, k)$ of a bitstring $x$ and a natural number
$k$ to such a pair $R(x, k) = (x', k')$, that is computable in FPT time, and a computable
function $g : \mathbb{N} \to \mathbb{N}$, such that for every bitstring $x$ and every
$k \in \mathbb{N}$, $k' \le g(k)$ and $P(x, k)$ is true if and only if $Q(x', k')$ is true.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Parameterized.FPTReduces`, a definition declared in [WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/parameterized-complexity/index.html#fptreduces).

## Encoded gates for weighted circuit satisfiability

An encoded gate is a pair $(k, r)$ of a
natural number $k$, its kind, and a list $r$ of natural numbers, its references.

Gates are read as in the shared (kind, references) encoding of flat Boolean circuits on $n$
inputs: $(0, [i])$ is the input variable $x_i$ when $i < n$, $(1, [b])$ is the constant that is
true exactly when $b = 1$, $(2, [a])$ is the negation of gate $a$, and $(3, r)$ and $(4, r)$ are
the AND and the OR of the gates listed in $r$; every other pair, including $(0, [i])$ with
$i \ge n$ and $(2, r)$ with $r$ not of length one, evaluates to false.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Parameterized.WCGate`, an abbreviation declared in [WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/parameterized-complexity/index.html#wcgate).

## Gate values of an encoded circuit

Let $C = (g_0, \dots, g_{m-1})$ be a list of gates
encoded as (kind, references) pairs and let $a = (a_0, \dots, a_{n-1})$ be a list of booleans.
The gate values of $C$ under $a$ are the values $(v_0, \dots, v_{m-1})$ of the flat Boolean
circuit on $n$ inputs obtained by decoding each $g_j$ to a gate on $n$ inputs, evaluated at the
assignment that gives input $i$ the value $a_i$.

Decoding turns an input gate with index $i \ge n$ into the constant false, so such inputs read
as false.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Parameterized.wcCircuitEval`, a definition declared in [WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/parameterized-complexity/index.html#wc-circuit-eval).

## Predecessors of an encoded gate

The predecessor list of an encoded gate $(k, r)$ is $r$
when $k$ is $2$, $3$ or $4$ (a NOT, AND or OR gate), and the empty list for every other kind.

Variable (kind $0$) and constant (kind $1$) payloads are a variable index and a constant value,
not predecessor gates; folding over them would attribute unrelated gates' weft or depth (for
example, an input gate $(0, [0])$ inheriting gate $0$'s depth).

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Parameterized.wcGatePreds`, a definition declared in [WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/parameterized-complexity/index.html#wc-gate-preds).

## Weft of an encoded gate

Given a list $w$ of wefts of earlier gates, where $w_a$ reads as
$0$ when $a$ is not a position of $w$, the weft of an encoded gate $(k, r)$ is $1$ if it is a
large AND or OR gate ($k \in \{3, 4\}$ and $r$ has more than $2$ entries) and $0$ otherwise,
plus the maximum of $w_a$ over the entries $a$ of its predecessor list (the maximum over an
empty list is $0$). In particular, input and constant gates have weft $0$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Parameterized.wcGateWeft`, a definition declared in [WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/parameterized-complexity/index.html#wc-gate-weft).

## Depth of one encoded gate

Let $d = (d_0, d_1, \dots)$ be a list of natural numbers
(the depths of earlier gates), where $d_a$ is read as $0$ when $a$ is out of range, and let
$(c, r)$ be a gate encoded as a (kind, references) pair. Its depth is $0$ if $c = 0$ or $c = 1$
(an input or constant gate), and otherwise one plus the maximum of $d_a$ over the entries $a$ of
$r$, the maximum over no entries being $0$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Parameterized.wcGateDepth`, a definition declared in [WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/parameterized-complexity/index.html#wc-gate-depth).

## Wefts of the gates of an encoded circuit

For a list
$C = (g_0, \dots, g_{m-1})$ of gates encoded as (kind, references) pairs, the list of wefts is
$(w_0, \dots, w_{m-1})$, where $w_j$ is computed from $w_0, \dots, w_{j-1}$ as follows. Write
$g_j = (c, r)$. The weft $w_j$ is $1$ if $c = 3$ or $c = 4$ (an AND or OR gate) and $r$ has
more than $2$ entries, and $0$ otherwise, plus, when $c = 2$, $c = 3$ or $c = 4$, the maximum of
$w_a$ over the entries $a$ of $r$, where $w_a$ is read as $0$ for $a \ge j$ and the maximum
over no entries is $0$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Parameterized.wcCircuitWefts`, a definition declared in [WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/parameterized-complexity/index.html#wc-circuit-wefts).

## Depths of the gates of an encoded circuit

For a list
$C = (g_0, \dots, g_{m-1})$ of gates encoded as (kind, references) pairs, the list of depths is
$(d_0, \dots, d_{m-1})$, where $d_j$ is computed from $d_0, \dots, d_{j-1}$ as follows. Write
$g_j = (c, r)$. If $c = 0$ or $c = 1$ (an input or constant gate), then $d_j = 0$; otherwise
$d_j$ is one plus the maximum of $d_a$ over the entries $a$ of $r$, where $d_a$ is read as $0$
for $a \ge j$ and the maximum over no entries is $0$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Parameterized.wcCircuitDepths`, a definition declared in [WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/parameterized-complexity/index.html#wc-circuit-depths).

## Well-formed encoded circuits

A list $C = (g_0, \dots, g_{m-1})$ of encoded gates is
well-formed when every NOT, AND or OR gate references only strictly earlier gates: for every
$j < m$ such that $g_j = (k, r)$ has kind $k \in \{2, 3, 4\}$, every entry $a$ of $r$ satisfies
$a < j$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Parameterized.WCWellFormed`, a definition declared in [WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/parameterized-complexity/index.html#wcwell-formed).

## Weighted circuit satisfiability with bounded weft and depth

For natural numbers $t$ and
$d$, weighted circuit satisfiability is the parameterized problem that, on a bitstring $x$ and a
parameter $k$, answers true exactly when $x$ decodes to a pair $(n, C)$ of a natural number $n$
and a list $C$ of encoded gates such that: every NOT, AND or OR gate of $C$ references only
strictly earlier gates; every gate of $C$ has weft at most $t$ and depth at most $d$; and there
is an assignment of $n$ Boolean values to the inputs, exactly $k$ of them true, under which $C$
has a last gate and that gate evaluates to true.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Parameterized.WeightedCircuitSat`, a definition declared in [WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/parameterized-complexity/index.html#weighted-circuit-sat).

## Parameterized Clique

The parameterized $k$-Clique problem answers a bitstring $x$ and
a parameter $k \in \mathbb{N}$ as follows. If $x$ decodes, under the canonical bitstring
encoding, to a pair $(n, E)$ of a natural number $n$ and a list $E$ of pairs of natural numbers,
the answer is true exactly when there is a list of $k$ distinct natural numbers, each less than
$n$, such that for any two distinct entries $u$ and $v$ of the list, $(u, v) \in E$ or
$(v, u) \in E$. If $x$ decodes to no such pair, the answer is false.

That is, on a well-formed input the answer says whether the graph on the vertices
$0, \dots, n - 1$ whose edges are the pairs in $E$, with direction ignored, has a clique of
size $k$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Parameterized.CliqueParam`, a definition declared in [WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/parameterized-complexity/index.html#clique-param).

## The level $\mathrm{W}(t)$ of the W-hierarchy

For a natural number $t$, $\mathrm{W}[t]$ is
the set of parameterized problems $P$ for which there is a natural number $d$ such that $P$
FPT-reduces to weighted circuit satisfiability for circuits of weft at most $t$ and depth at
most $d$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Parameterized.WLevel`, a definition declared in [WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/parameterized-complexity/index.html#wlevel).

## Parameterized complexity: FPT and W(1)-completeness of Clique

Write $W[t]$ for the
$t$-th level of the W-hierarchy. The parameterized $k$-Clique problem lies in $W[1]$, and every
parameterized problem in $W[1]$ has an FPT-reduction to it. Every fixed-parameter tractable
parameterized problem lies in $W[1]$. For every $t \in \mathbb{N}$, $W[t] \subseteq W[t + 1]$.

## Sources

- R. G. Downey and M. R. Fellows, Parameterized Complexity, Springer, 1999 (W[1]-completeness of Clique); J. Flum and M. Grohe, Parameterized Complexity Theory, Springer, 2006.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.Parameterized.parameterized_clique_w1_complete` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/ParameterizedWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/parameterized-complexity/index.html#parameterized-clique-w1-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Parameterized complexity](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/parameterized-complexity/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/complexity-classes/parameterized-complexity)
