---
declaration: section
origin: cited
lean: Cslib.Algorithms.CCS.sumOf, Cslib.Algorithms.CCS.step_sumOf_iff, Cslib.Algorithms.CCS.Realizes, Cslib.Algorithms.CCS.Realizes.constant, Cslib.Algorithms.CCS.parSteps, Cslib.Algorithms.CCS.Realizes.parallel, Cslib.Algorithms.CCS.allowedB, Cslib.Algorithms.CCS.restrictSteps
statement: formalized
proof: formalized
---

# Finite-state CCS agents

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/finite-state-ccs-agents/index.html).

## Sum of prefixes

For a list $l$ of pairs $(a, q)$ of a label and a process, the process
that chooses among the prefixes $a.q$ listed in $l$: the empty list gives the inactive process
$\mathbf{0}$, and the list with head $(a, q)$ and tail $r$ gives the choice $a.q + P$ between the
prefix $a.q$ and the process $P$ built in the same way from $r$.

Formalized by `Cslib.Algorithms.CCS.sumOf`, a definition declared in [CSLibExt/Algorithms/CCS/FiniteState.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/FiniteState.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/finite-state-ccs-agents/index.html#sum-of).

## Transitions of a sum of prefixes

For every recursive specification, every list $l$ of
pairs of a label and a process, every label $a$ and every process $q$, the sum of the prefixes
listed in $l$ has a transition labelled $a$ to $q$ exactly when $(a, q)$ belongs to $l$.

Formalized by `Cslib.Algorithms.CCS.step_sumOf_iff`, a theorem declared in [CSLibExt/Algorithms/CCS/FiniteState.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/FiniteState.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/finite-state-ccs-agents/index.html#step-sum-of-iff).

## Realization of a code-level transition system

Fix a recursive specification. A family
of processes $P_x$ indexed by codes $x$ realizes a function $s$ that lists, for each code $x$,
labelled transitions $(a, y)$ with $a$ a label and $y$ a code, when for every code $x$, every
label $a$ and every process $q$, the process $P_x$ has a transition with label $a$ to $q$
exactly when $s(x)$ contains an entry $(a, y)$ with $P_y = q$.

Formalized by `Cslib.Algorithms.CCS.Realizes`, a definition declared in [CSLibExt/Algorithms/CCS/FiniteState.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/FiniteState.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/finite-state-ccs-agents/index.html#realizes).

## Constants listing their transitions realize them

Fix a recursive specification, a map
$\iota$ from codes to process constants and a function $s$ listing labelled transitions for
each code. Suppose that for every code $x$, writing $(a_1, y_1), \dots, (a_n, y_n)$ for the
entries of $s(x)$ in order, the body of the constant $\iota(x)$ is
$a_1.\iota(y_1) + (a_2.\iota(y_2) + \dots + (a_n.\iota(y_n) + 0))$, which is $0$ when $n = 0$.
Then the processes $\iota(x)$, indexed by codes $x$, realize $s$.

Formalized by `Cslib.Algorithms.CCS.Realizes.constant`, a theorem declared in [CSLibExt/Algorithms/CCS/FiniteState.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/FiniteState.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/finite-state-ccs-agents/index.html#constant).

## Code-level parallel composition

Given functions $s$ and $t$ listing the labelled
transitions of codes $x$ and $y$, the transitions of the pair $(x, y)$ are listed in three
blocks: $(a, (x', y))$ for each entry $(a, x')$ of $s(x)$; then $(a, (x, y'))$ for each entry
$(a, y')$ of $t(y)$; then $(\tau, (x', y'))$ for each entry $(a, x')$ of $s(x)$ and each entry
$(b, y')$ of $t(y)$ whose labels are complementary, that is, one is the input and the other the
output on the same name.

Formalized by `Cslib.Algorithms.CCS.parSteps`, a definition declared in [CSLibExt/Algorithms/CCS/FiniteState.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/FiniteState.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/finite-state-ccs-agents/index.html#par-steps).

## Parallel composition preserves realization

Fix a recursive specification. If the
processes $P_x$ realize $s$ and the processes $Q_y$ realize $t$, then the parallel compositions
$P_x \mid Q_y$, indexed by pairs $(x, y)$, realize the code-level parallel composition of $s$
and $t$.

Formalized by `Cslib.Algorithms.CCS.Realizes.parallel`, a theorem declared in [CSLibExt/Algorithms/CCS/FiniteState.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/FiniteState.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/finite-state-ccs-agents/index.html#parallel).

## Boolean restriction test

For a list $L$ of blocked names, the test returns true on a
label exactly when the label is the silent action $\tau$, or an input or an output on a name
that does not occur in $L$. It is the Boolean form of the condition that restriction by $L$
allows the label.

Formalized by `Cslib.Algorithms.CCS.allowedB`, a definition declared in [CSLibExt/Algorithms/CCS/FiniteState.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/FiniteState.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/finite-state-ccs-agents/index.html#allowed-b).

## Code-level restriction

For a list $L$ of blocked names and a function $s$ listing the
labelled transitions of each code, the restricted transitions of a code $x$ are the entries
$(a, y)$ of $s(x)$, in order, whose label $a$ is the silent action $\tau$ or an input or an
output on a name that does not occur in $L$.

Formalized by `Cslib.Algorithms.CCS.restrictSteps`, a definition declared in [CSLibExt/Algorithms/CCS/FiniteState.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/FiniteState.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/finite-state-ccs-agents/index.html#restrict-steps).

## Restriction preserves realization

Fix a recursive specification and a list $L$ of
blocked names. If the processes $P_x$ realize $s$, then the restricted processes
$P_x \setminus L$ realize the code-level restriction of $s$ by $L$.

Formalized by `Cslib.Algorithms.CCS.Realizes.restriction`, a theorem declared in [CSLibExt/Algorithms/CCS/FiniteState.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/FiniteState.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/finite-state-ccs-agents/index.html#restriction).

## Forward certificate check

Let $s$ list the labelled transitions $(a, x')$ of each
implementation code $x$, let $t$ list those of each specification code $y$, and let $R$ be a
finite list of code pairs. The forward check succeeds when for every pair $(x, y)$ in $R$ and
every entry $(a, x')$ of $s(x)$, either $a = \tau$ and $(x', y)$ is in $R$, or some entry
$(a, y')$ of $t(y)$ with the same label has $(x', y')$ in $R$.

Formalized by `Cslib.Algorithms.CCS.forwardCheck`, a definition declared in [CSLibExt/Algorithms/CCS/FiniteState.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/FiniteState.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/finite-state-ccs-agents/index.html#forward-check).

## Backward certificate check

Let $s$ list the labelled transitions $(a, x')$ of each
implementation code $x$, let $t$ list those of each specification code $y$, and let $R$ be a
finite list of code pairs. The backward check succeeds when for every pair $(x, y)$ in $R$ and
every entry $(a, y')$ of $t(y)$, at least one of the following holds: $a = \tau$ and
$(x, y')$ is in $R$; some entry $(a, x')$ of $s(x)$ with the same label has $(x', y')$ in $R$;
or some entry $(\tau, x'')$ of $s(x)$ has $(x'', y)$ in $R$, and the first occurrence of
$(x'', y)$ in $R$ comes strictly before the first occurrence of $(x, y)$.

Formalized by `Cslib.Algorithms.CCS.backwardCheck`, a definition declared in [CSLibExt/Algorithms/CCS/FiniteState.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/FiniteState.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/finite-state-ccs-agents/index.html#backward-check).

## Weak-bisimulation certificate check

For transition lists $s$ of implementation codes
and $t$ of specification codes and a finite list $R$ of code pairs, the certificate check
succeeds when both the forward check and the backward check succeed on $s$, $t$ and $R$.

Formalized by `Cslib.Algorithms.CCS.certCheck`, a definition declared in [CSLibExt/Algorithms/CCS/FiniteState.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/FiniteState.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/finite-state-ccs-agents/index.html#cert-check).

## Certificate checks give weak bisimilarity

Let $f$ realize the code-level transition
function $s$ and $g$ realize $t$ for a recursive specification, and let $R$ be a list of code
pairs on which the certificate check of $s$, $t$ and $R$ succeeds. Then for every pair $(x, y)$
in $R$, the processes $f(x)$ and $g(y)$ are weakly bisimilar in the labelled transition system
of the specification.

Formalized by `Cslib.Algorithms.CCS.weaklyBisimilar_of_certCheck`, a theorem declared in [CSLibExt/Algorithms/CCS/FiniteState.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/FiniteState.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/finite-state-ccs-agents/index.html#weakly-bisimilar-of-cert-check).

## Direct check of the root condition

Given code-level transition functions $s$ on codes
$\alpha$ and $t$ on codes $\beta$, each listing labelled steps to codes, a relation $R$ given as
a list of code pairs, and codes $x$ and $y$, the root check succeeds exactly when every listed
step $(a, x')$ of $s(x)$ is matched by some listed step $(a, y')$ of $t(y)$ with the same label
and $(x', y') \in R$, and every listed step $(a, y')$ of $t(y)$ is matched by some listed step
$(a, x')$ of $s(x)$ with the same label and $(x', y') \in R$.

This is a sufficient check of the root condition of observation congruence at $(x, y)$. Rooted
weak bisimilarity also allows silent steps around the matching step, so the check is incomplete.

Formalized by `Cslib.Algorithms.CCS.rootCheck`, a definition declared in [CSLibExt/Algorithms/CCS/FiniteState.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/FiniteState.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/finite-state-ccs-agents/index.html#root-check).

## Certificate checks give rooted observation congruence

Let $f$ realize the code-level
transition function $s$ and $g$ realize $t$ for a recursive specification, and let $R$ be a list
of code pairs on which the certificate check of $s$, $t$ and $R$ succeeds. If the root check of
$s$, $t$ and $R$ succeeds at codes $x$ and $y$, then the processes $f(x)$ and $g(y)$ are rooted
weakly bisimilar (observation congruent) in the labelled transition system of the specification
(Milner, Chapter 7).

Formalized by `Cslib.Algorithms.CCS.rootedWeaklyBisimilar_of_certCheck`, a theorem declared in [CSLibExt/Algorithms/CCS/FiniteState.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/CCS/FiniteState.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/finite-state-ccs-agents/index.html#rooted-weakly-bisimilar-of-cert-check).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite-state CCS agents](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/finite-state-ccs-agents/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/process-calculi/finite-state-ccs-agents)
