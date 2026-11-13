---
declaration: section
origin: cited
lean: Cslib.IMP.HAssertion, Cslib.IMP.HAssertion.Entails, Cslib.IMP.HAssertion.emp, Cslib.IMP.HAssertion.pure, Cslib.IMP.HAssertion.pointsTo, Cslib.IMP.HAssertion.star, Cslib.IMP.HAssertion.hexists, Cslib.IMP.HAssertion.hand
statement: formalized
proof: formalized
---

# Separation logic

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html).

## Heap assertion

A heap assertion is a predicate on a store and a heap: it assigns a
proposition to every store $s$ and every heap $h$. Heap assertions serve as the preconditions
and postconditions of separation logic.

Formalized by `Cslib.IMP.HAssertion`, an abbreviation declared in [CSLibExt/Languages/IMP/SeparationLogic.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/SeparationLogic.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html#hassertion).

## Entailment of heap assertions

A heap assertion $P$ entails a heap assertion $Q$ when, for
every store $s$ and every heap $h$, if $P$ holds of $s$ and $h$, then $Q$ holds of $s$ and $h$.

Formalized by `Cslib.IMP.HAssertion.Entails`, a definition declared in [CSLibExt/Languages/IMP/SeparationLogic.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/SeparationLogic.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html#entails).

## Empty-heap assertion

The heap assertion $\mathrm{emp}$ holds of a store $s$ and a heap
$h$ exactly when $h$ is the empty heap, whatever the store $s$ is.

Formalized by `Cslib.IMP.HAssertion.emp`, a definition declared in [CSLibExt/Languages/IMP/SeparationLogic.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/SeparationLogic.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html#emp).

## Pure assertion

For a proposition $p$, the pure assertion of $p$ holds of a store $s$ and
a heap $h$ exactly when $h$ is the empty heap and $p$ is true.

Formalized by `Cslib.IMP.HAssertion.pure`, a definition declared in [CSLibExt/Languages/IMP/SeparationLogic.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/SeparationLogic.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html#pure).

## Points-to assertion

For natural numbers $a$ and $v$, the assertion $a \mapsto v$ holds of
a store $s$ and a heap $h$ exactly when $h$ is the singleton heap that maps the address $a$ to the
value $v$ and allocates no other address.

Formalized by `Cslib.IMP.HAssertion.pointsTo`, a definition declared in [CSLibExt/Languages/IMP/SeparationLogic.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/SeparationLogic.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html#points-to).

## Separating conjunction

For heap assertions $P$ and $Q$, the assertion $P \star Q$ holds
of a store $s$ and a heap $h$ when there are disjoint heaps $h_1$ and $h_2$ with
$h = h_1 \cup h_2$ such that $P(s, h_1)$ and $Q(s, h_2)$.

Formalized by `Cslib.IMP.HAssertion.star`, a definition declared in [CSLibExt/Languages/IMP/SeparationLogic.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/SeparationLogic.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html#star).

## Existential heap assertion

For a function $p$ assigning a heap assertion $p(n)$ to each
natural number $n$ (an address or a value), the assertion $\exists n,\ p(n)$ holds of a store $s$
and a heap $h$ exactly when $p(n)$ holds of $s$ and $h$ for some natural number $n$.

Formalized by `Cslib.IMP.HAssertion.hexists`, a definition declared in [CSLibExt/Languages/IMP/SeparationLogic.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/SeparationLogic.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html#hexists).

## Conjunction of heap assertions

For heap assertions $P$ and $Q$, the assertion
$P \wedge Q$ holds of a store $s$ and a heap $h$ exactly when $P$ holds of $s$ and $h$ and $Q$
holds of $s$ and the same heap $h$.

Formalized by `Cslib.IMP.HAssertion.hand`, a definition declared in [CSLibExt/Languages/IMP/SeparationLogic.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/SeparationLogic.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html#hand).

## Separation-logic triple validity

For heap assertions $P$, $Q$ and a heap command $c$,
the triple $\lbrace P \rbrace\ c\ \lbrace Q \rbrace$ is valid (in the fault-avoiding sense)
when, for every store $s$ and heap $h$ with $P(s, h)$, the configuration $(c, s, h)$ is safe
(no configuration reachable from it is stuck at a command other than $\mathtt{skip}$), and
whenever $(c, s, h)$ reaches $(\mathtt{skip}, s', h')$ in finitely many heap steps,
$Q(s', h')$ holds.

Formalized by `Cslib.IMP.SepValid`, a definition declared in [CSLibExt/Languages/IMP/SeparationLogic.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/SeparationLogic.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html#sep-valid).

## Separation-logic while rule

Let $I$ be a heap assertion, $b$ a Boolean expression and
$c$ a heap command. Write $I \wedge b$ for the assertion that holds of a store $s$ and a heap
$h$ when $I(s, h)$ holds and $b$ evaluates to true in $s$, and $I \wedge \neg b$ for the one
that holds when $I(s, h)$ holds and $b$ evaluates to false in $s$. If the triple
$\lbrace I \wedge b \rbrace\ c\ \lbrace I \rbrace$ is valid, then so is the triple
$\lbrace I \rbrace\ \mathtt{while}\ b\ \mathtt{do}\ c\ \lbrace I \wedge \neg b \rbrace$.

Formalized by `Cslib.IMP.SepValid.whileLoop`, a theorem declared in [CSLibExt/Languages/IMP/SeparationLogic.lean, line 430](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/SeparationLogic.lean#L430). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html#while-loop).

## Frame rule

Let $P$, $Q$ and $R$ be heap assertions and $c$ a heap command. Suppose the
separation-logic triple with precondition $P$, command $c$ and postcondition $Q$ is valid, and
suppose that whenever $R$ holds of a store $s$ and a heap $h$, it also holds of $s'$ and $h$ for
every store $s'$ that agrees with $s$ on every variable outside the set of variables that $c$ may
assign to. Then the triple with precondition $P \star R$, command $c$ and postcondition
$Q \star R$ is valid, where $\star$ denotes separating conjunction.

Formalized by `Cslib.IMP.SepValid.frame`, a theorem declared in [CSLibExt/Languages/IMP/SeparationLogic.lean, line 576](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/SeparationLogic.lean#L576). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html#frame).

## Hoare validity embeds into separation validity

Let $P$ and $Q$ be store assertions and
$c$ a command of plain IMP. If the partial-correctness Hoare triple with precondition $P$, command
$c$ and postcondition $Q$ is valid, then the separation-logic triple for the embedding of $c$ into
heap IMP is valid with the precondition that holds of a store $s$ and any heap exactly when $P(s)$
holds and the postcondition that holds of a store $s$ and any heap exactly when $Q(s)$ holds.

Embedded commands are always safe, never change the heap, and terminate exactly when the plain
command does.

Formalized by `Cslib.IMP.SepValid.of_valid`, a theorem declared in [CSLibExt/Languages/IMP/SeparationLogic.lean, line 607](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/SeparationLogic.lean#L607). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html#of-valid).

## Framed embedding of Hoare validity

Let $P$ and $Q$ be store assertions, $R$ a heap
assertion and $c$ a command of plain IMP, and write $\hat c$ for the embedding of $c$ into heap
IMP. Suppose the partial-correctness Hoare triple with precondition $P$, command $c$ and
postcondition $Q$ is valid, and suppose that whenever $R$ holds of a store $s$ and a heap $h$, it
also holds of $s'$ and $h$ for every store $s'$ that agrees with $s$ on every variable outside the
set of variables that $\hat c$ may assign to. Write $\tilde P$ and $\tilde Q$ for the heap
assertions that hold of a store $s$ and any heap exactly when $P(s)$, respectively $Q(s)$, holds.
Then the separation-logic triple with precondition $\tilde P \star R$, command $\hat c$ and
postcondition $\tilde Q \star R$ is valid, where $\star$ denotes separating conjunction.

Formalized by `Cslib.IMP.SepValid.of_valid_frame`, a theorem declared in [CSLibExt/Languages/IMP/SeparationLogic.lean, line 619](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/SeparationLogic.lean#L619). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html#of-valid-frame).

## Store-irrelevant heap assertions

A heap assertion $P$ is store-irrelevant when for all
stores $s, s'$ and every heap $h$, $P(s, h)$ implies $P(s', h)$; that is, whether $P$ holds
does not depend on the store.

The empty-heap and points-to assertions are store-irrelevant, and so is the separating
conjunction of two store-irrelevant assertions.

Formalized by `Cslib.IMP.StoreIrrel`, a definition declared in [CSLibExt/Languages/IMP/SeparationAPI.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/SeparationAPI.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html#store-irrel).

## Store-irrelevant frames satisfy the frame-rule side condition

Let $R$ be a
store-irrelevant heap assertion and $c$ a heap command. For all stores $s, s'$ and every heap
$h$, if $R(s, h)$ holds and $s'(x) = s(x)$ for every variable $x$ outside the set of variables
that $c$ may assign to, then $R(s', h)$ holds.

This is the side condition on the frame in the frame rule.

Formalized by `Cslib.IMP.frame_of_storeIrrel`, a theorem declared in [CSLibExt/Languages/IMP/SeparationAPI.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/SeparationAPI.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html#frame-of-store-irrel).

## Pulling a store fact out of a separating conjunction

Let $p$ be a predicate on
stores and $P$, $R$ heap assertions. Write $A \star B$ for the separating conjunction of heap
assertions $A$ and $B$ (the heap splits into two disjoint parts satisfying $A$ and $B$,
respectively, at the same store), and $p \land P$ for the heap assertion that holds at store
$s$ and heap $h$ when $p(s)$ and $P(s, h)$ both hold. Then
$(p \land P) \star R = p \land (P \star R)$.

This lets framed local triples be stated with the store facts kept outside the separating
conjunction.

Formalized by `Cslib.IMP.star_and_left`, a theorem declared in [CSLibExt/Languages/IMP/SeparationAPI.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/SeparationAPI.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html#star-and-left).

## Rearranging a separating conjunction

For heap assertions $P$, $Q$ and $R$, write
$A \star B$ for the separating conjunction of heap assertions $A$ and $B$ (the heap splits into
two disjoint parts satisfying $A$ and $B$, respectively, at the same store). Then
$P \star (Q \star R)$ entails $(P \star R) \star Q$: every store and heap satisfying the first
assertion satisfy the second.

Formalized by `Cslib.IMP.star_swap_right`, a theorem declared in [CSLibExt/Languages/IMP/SeparationAPI.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/SeparationAPI.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html#star-swap-right).

## Local rule for a heap read

Let $x$ and $y$ be variables, let $a$ and $v$ be natural
numbers, and let $p$ and $q$ be predicates on stores. Write $s[x := n]$ for the store that agrees
with $s$ except that it maps $x$ to $n$, and $a \mapsto v$ for the heap assertion that holds when
the heap is the single cell at address $a$ holding $v$. If every store $s$ satisfying $p$ has
$s(y) = a$ and $q(s[x := v])$, then the separation-logic triple for the heap read $x := [y]$
(which loads into $x$ the value stored at the address held in $y$) is valid with precondition
"$p(s)$ and $a \mapsto v$ holds at $(s, h)$" and postcondition "$q(s)$ and $a \mapsto v$ holds at
$(s, h)$", where $s$ is the store and $h$ the heap.

Formalized by `Cslib.IMP.read_local`, a theorem declared in [CSLibExt/Languages/IMP/SeparationAPI.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/SeparationAPI.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html#read-local).

## Assignment rule with a store-irrelevant heap assertion

Let $x$ and $y$ be variables,
let $p$ and $q$ be predicates on stores, and let $H$ be a store-irrelevant heap assertion.
Write $s[x := n]$ for the store that agrees with $s$ except that it maps $x$ to $n$. If every
store $s$ satisfying $p$ has $q(s[x := s(y)])$, then the separation-logic triple for the
assignment $x := y$ is valid with precondition "$p(s)$ and $H(s, h)$" and postcondition
"$q(s)$ and $H(s, h)$", where $s$ is the store and $h$ the heap.

An assignment leaves the heap untouched, so no framing is needed.

Formalized by `Cslib.IMP.assign_step`, a theorem declared in [CSLibExt/Languages/IMP/SeparationAPI.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/SeparationAPI.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html#assign-step).

## Existential rule for separation-logic triples

Let $c$ be a heap command, let $\iota$ be
an arbitrary index (any type or proposition), and let $P_i$ and $Q_i$ be heap assertions for
each $i$ in $\iota$. If for every $i$ the triple with precondition $P_i$, command $c$ and
postcondition $Q_i$ is valid, then the triple with precondition "there is $i$ with $P_i$",
command $c$ and postcondition "there is $i$ with $Q_i$" is valid.

Formalized by `Cslib.IMP.SepValid.exists`, a theorem declared in [CSLibExt/Languages/IMP/SeparationAPI.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/IMP/SeparationAPI.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html#exists).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Separation logic](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/program-logics-and-verification/separation-logic/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/program-logics-and-verification/separation-logic)
