---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.DinurGapAmplification.CSPInstance, MetaMathlibExt.Complexity.KeyTheorems.DinurGapAmplification.CSPWellFormed, MetaMathlibExt.Complexity.KeyTheorems.DinurGapAmplification.cspConstraintSat, MetaMathlibExt.Complexity.KeyTheorems.DinurGapAmplification.cspVal, MetaMathlibExt.Complexity.KeyTheorems.DinurGapAmplification.cspDegree, MetaMathlibExt.Complexity.KeyTheorems.DinurGapAmplification.gapAmplification, MetaMathlibExt.Complexity.KeyTheorems.DinurGapAmplification.alphabetReduction, MetaMathlibExt.Complexity.KeyTheorems.DinurGapAmplification.dinur_gap_amplification
statement: formalized
---

# Dinur's gap amplification

8 results, 7 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/dinur-s-gap-amplification/index.html).

## 2CSP instances

A 2CSP instance is a triple $(n, \Sigma, C)$ of a natural number $n$ (the
number of variables), a natural number $\Sigma$ (the alphabet size) and a finite list $C$ of
constraints, where each constraint is a triple $(u, v, P)$ of natural numbers $u$ and $v$ (the
variables it mentions) and a finite list $P$ of pairs of natural numbers (the allowed label
pairs).

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.DinurGapAmplification.CSPInstance`, an abbreviation declared in [WantedExt/Complexity/KeyTheorems/DinurGapAmplificationWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/DinurGapAmplificationWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/dinur-s-gap-amplification/index.html#cspinstance).

## Well-formed 2CSP instances

A 2CSP instance $(n, \Sigma, C)$ is well-formed when every
constraint $(u, v, P)$ in $C$ satisfies $u < n$ and $v < n$, and every allowed pair $(a, b)$ in
$P$ satisfies $a < \Sigma$ and $b < \Sigma$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.DinurGapAmplification.CSPWellFormed`, a definition declared in [WantedExt/Complexity/KeyTheorems/DinurGapAmplificationWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/DinurGapAmplificationWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/dinur-s-gap-amplification/index.html#cspwell-formed).

## Satisfied constraint of a 2CSP instance

Let $I = (n, \Sigma, C)$ be a 2CSP instance and
$\sigma$ an assignment of a label less than $\Sigma$ to each variable less than $n$. A constraint
$(u, v, P)$ is satisfied by $\sigma$ when $u < n$, $v < n$ and the pair $(\sigma(u), \sigma(v))$
belongs to $P$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.DinurGapAmplification.cspConstraintSat`, a definition declared in [WantedExt/Complexity/KeyTheorems/DinurGapAmplificationWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/DinurGapAmplificationWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/dinur-s-gap-amplification/index.html#csp-constraint-sat).

## Value of a 2CSP instance under an assignment

Let $I = (n, \Sigma, C)$ be a 2CSP
instance and $\sigma$ an assignment of a label less than $\Sigma$ to each variable less than $n$.
The value of $I$ under $\sigma$ is the rational number $1$ if $C$ is empty, and otherwise the
number of entries of the list $C$ that are constraints satisfied by $\sigma$, divided by the
length of $C$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.DinurGapAmplification.cspVal`, a definition declared in [WantedExt/Complexity/KeyTheorems/DinurGapAmplificationWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/DinurGapAmplificationWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/dinur-s-gap-amplification/index.html#csp-val).

## Degree of a variable in a 2CSP instance

For a 2CSP instance $(n, \Sigma, C)$ and a
natural number $v$, the degree of $v$ is the number of entries $(u, w, P)$ of the list $C$ with
$u = v$ or $w = v$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.DinurGapAmplification.cspDegree`, a definition declared in [WantedExt/Complexity/KeyTheorems/DinurGapAmplificationWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/DinurGapAmplificationWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/dinur-s-gap-amplification/index.html#csp-degree).

## Gap amplification with given constants

Let $c, \alpha$ be rationals and $d, D, e$ natural
numbers. A map $T$ from 2CSP instances to 2CSP instances is a gap amplification with constants
$c, \alpha, d, D, e$ when $c > 1$, $0 < \alpha < 1$, $d \ge 1$, $D \ge 1$, and for every 2CSP
instance $I$ with $n$ variables, alphabet size $\Sigma$ and $m$ constraints: $T(I)$ has exactly $n$
variables, alphabet size at most $\Sigma^e$ and at most $d m$ constraints; if $I$ is well-formed
then so is $T(I)$; for every natural number $v$, if $v$ has degree $k$ in $I$, then $v$ has degree
at most $D(k + 1)$ in $T(I)$; if some assignment gives $I$ value $1$ then some assignment
gives $T(I)$ value $1$; and for every rational $\delta$ with $0 < \delta \le 1$, if every assignment
gives $I$ value at most $1 - \delta$, then every assignment gives $T(I)$ value at most
$1 - \min(\alpha, c\delta)$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.DinurGapAmplification.gapAmplification`, a definition declared in [WantedExt/Complexity/KeyTheorems/DinurGapAmplificationWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/DinurGapAmplificationWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/dinur-s-gap-amplification/index.html#gap-amplification).

## Alphabet reduction with given constants

Let $S_0, e, d', V$ be natural numbers and
$c', \alpha'$ rationals. A map $T$ from 2CSP instances to 2CSP instances is an alphabet reduction
with constants $S_0, e, c', \alpha', d', V$ when $S_0 \ge 2$, $e \ge 2$, $0 < c' \le 1$,
$0 < \alpha' < 1$, $d' \ge 1$, $V \ge 1$, and for every 2CSP instance $I$ with $n$ variables,
alphabet size at most $S_0^e$ and $m$ constraints: $T(I)$ has at most $V(n + 1)$ variables,
alphabet size at most $S_0$ and at most $d' m$ constraints; if $I$ is well-formed then so is
$T(I)$; if some assignment gives $I$ value $1$ then some assignment gives $T(I)$ value $1$; and
for every rational $\delta$ with $0 < \delta \le 1$, if every assignment gives $I$ value at most
$1 - \delta$, then every assignment gives $T(I)$ value at most $1 - \min(\alpha', c'\delta)$.

The bounds $S_0 \ge 2$ and $e \ge 2$ give $S_0^e > S_0$, so the reduction must genuinely shrink
the alphabet.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.DinurGapAmplification.alphabetReduction`, a definition declared in [WantedExt/Complexity/KeyTheorems/DinurGapAmplificationWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/DinurGapAmplificationWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/dinur-s-gap-amplification/index.html#alphabet-reduction).

## Dinur's gap amplification and alphabet reduction

There exist natural numbers
$S_0, e, d, D, d', V$ and rationals $c, \alpha, c', \alpha'$ with $S_0 \ge 2$, $e \ge 2$, $c > 1$,
$0 < \alpha < 1$, $d \ge 1$, $D \ge 1$, $0 < c' \le 1$, $0 < \alpha' < 1$, $d' \ge 1$ and $V \ge 1$,
and maps $A$ and $R$ from 2CSP instances to 2CSP instances, with the following properties.
Both maps are polynomial-time computable: for each $T \in \{A, R\}$ there is a polynomial-time
computable function $f$ from lists of booleans to lists of booleans such that, for every 2CSP
instance $I$, decoding $f$ applied to the bitstring encoding of $I$ succeeds and returns $T(I)$.
The map $A$ is a gap amplification with constants $c, \alpha, d, D, e$, and $R$ is an alphabet
reduction with constants $S_0, e, c', \alpha', d', V$. Finally, for every 2CSP instance $I$ with
alphabet size at most $S_0$, the instance $J = R(A(I))$ has alphabet size at most $S_0$; if $I$
is well-formed then so is $J$; if some assignment gives $I$ value $1$ then some assignment gives
$J$ value $1$; and for every rational $\delta$ with $0 < \delta \le 1$, if every assignment gives
$I$ value at most $1 - \delta$, then every assignment gives $J$ value at most
$1 - \min(\alpha', c' \min(\alpha, c\delta))$.

The constants $c$ and $c'$ are not tied together: the statement does not assert $c' c > 1$, so
the composed map $R \circ A$ need not enlarge the gap.

## Sources

- I. Dinur, "The PCP theorem by gap amplification", Journal of the ACM 54 (2007), 12:1-12:44 (Proceedings of the Thirty-Eighth Annual ACM Symposium on Theory of Computing, STOC 2006, 241-250).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.DinurGapAmplification.dinur_gap_amplification` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/DinurGapAmplificationWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/DinurGapAmplificationWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/dinur-s-gap-amplification/index.html#dinur-gap-amplification).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dinur's gap amplification](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pcp-and-inapproximability/dinur-s-gap-amplification/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/pcp-and-inapproximability/dinur-s-gap-amplification)
