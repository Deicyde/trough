---
declaration: section
origin: cited
lean: Cslib.Logic.PL.BDD, Cslib.Logic.PL.BDD.eval, Cslib.Logic.PL.BDD.size, Cslib.Logic.PL.BDD.OrderedFrom, Cslib.Logic.PL.BDD.Reduced, Cslib.Logic.PL.BDD.IsROBDD, Cslib.Logic.PL.BDD.eval_update_of_lt, Cslib.Logic.PL.BDD.eval_update_node
statement: formalized
proof: formalized
---

# Reduced ordered binary decision diagrams: canonicity and apply

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html).

## Binary decision diagram

A binary decision diagram, in tree form, is either a leaf
carrying a Boolean value, or a node consisting of a variable $v \in \mathbb{N}$ and two
diagrams: the low child, for $v$ false, and the high child, for $v$ true.

Formalized by `Cslib.Logic.PL.BDD`, an inductive type declared in [CSLibExt/Logics/Propositional/BDD/Basic.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Basic.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html#bdd).

## Evaluation of a binary decision diagram

Under an assignment $\sigma$ of a Boolean value
to each variable $v \in \mathbb{N}$, the value of a leaf is its Boolean value, and the value of a
node testing $v$ is the value of its high child if $\sigma(v)$ is true and the value of its low
child if $\sigma(v)$ is false.

Formalized by `Cslib.Logic.PL.BDD.eval`, a definition declared in [CSLibExt/Logics/Propositional/BDD/Basic.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Basic.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html#eval).

## Size of a diagram

The size of a diagram is its number of leaves and nodes, counted in
tree form: a leaf has size $1$, and a node with children $\ell$ and $h$ has size one more than the
sum of the sizes of $\ell$ and $h$.

Formalized by `Cslib.Logic.PL.BDD.size`, a definition declared in [CSLibExt/Logics/Propositional/BDD/Basic.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Basic.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html#size).

## Diagrams ordered from a variable

For a natural number $n$, a diagram is ordered from
$n$ when every variable it tests is at least $n$ and the tested variables strictly increase
along every path. Recursively: every leaf is ordered from $n$, and the node testing $v$ with
children $\ell$ and $h$ is ordered from $n$ when $n \le v$ and both $\ell$ and $h$ are ordered
from $v + 1$.

Formalized by `Cslib.Logic.PL.BDD.OrderedFrom`, a definition declared in [CSLibExt/Logics/Propositional/BDD/Basic.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Basic.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html#ordered-from).

## Reduced diagrams

A diagram is reduced when no node in it has two equal children: every
leaf is reduced, and the node testing $v$ with children $\ell$ and $h$ is reduced when
$\ell \ne h$ and both $\ell$ and $h$ are reduced.

Formalized by `Cslib.Logic.PL.BDD.Reduced`, a definition declared in [CSLibExt/Logics/Propositional/BDD/Basic.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Basic.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html#reduced).

## Reduced ordered binary decision diagram

A binary decision diagram is a reduced ordered
binary decision diagram (ROBDD), for the natural order on variables, when it is ordered from
$0$ (the tested variables strictly increase along every path) and reduced (no node has two
equal children).

Formalized by `Cslib.Logic.PL.BDD.IsROBDD`, a definition declared in [CSLibExt/Logics/Propositional/BDD/Basic.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Basic.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html#is-robdd).

## Independence from variables below the order

Let $t$ be a binary decision diagram
ordered from $n \in \mathbb{N}$ and let $v < n$ be a variable. For every assignment $\sigma$ of
Boolean values to the variables and every Boolean $b$, the value of $t$ under
$\sigma[v \mapsto b]$ (the assignment $\sigma$ with $v$ set to $b$) equals the value of $t$ under
$\sigma$.

Formalized by `Cslib.Logic.PL.BDD.eval_update_of_lt`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Basic.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Basic.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html#eval-update-of-lt).

## Fixing the top variable of an ordered node

Let $t$ be a node testing the variable $v$
with low child $\ell$ and high child $h$, and suppose $t$ is ordered from some $n \in \mathbb{N}$.
For every assignment $\sigma$ of Boolean values to the variables and every Boolean $b$, the value
of $t$ under $\sigma[v \mapsto b]$ (the assignment $\sigma$ with $v$ set to $b$) is the value of
$h$ under $\sigma$ if $b$ is true, and the value of $\ell$ under $\sigma$ if $b$ is false.

Formalized by `Cslib.Logic.PL.BDD.eval_update_node`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Basic.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Basic.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html#eval-update-node).

## Binary decision diagrams have positive size

For every binary decision diagram $t$,
the size of $t$ (its number of leaves and nodes, counted in tree form) is strictly positive.

Formalized by `Cslib.Logic.PL.BDD.size_pos`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Basic.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Basic.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html#size-pos).

## Canonicity

**Canonicity** (Bryant): two reduced ordered diagrams with the same function are
equal.

Formalized by `Cslib.Logic.PL.BDD.eq_of_eval_eq`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Basic.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Basic.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html#eq-of-eval-eq).

## Reduced ordered diagrams are equal iff they have the same values

If $t_1$ and $t_2$ are
reduced ordered binary decision diagrams, then $t_1 = t_2$ if and only if $t_1$ and $t_2$ have
the same value under every assignment of Boolean values to the variables.

Formalized by `Cslib.Logic.PL.BDD.eq_iff_eval_eq`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Basic.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Basic.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html#eq-iff-eval-eq).

## Unsatisfiable reduced ordered diagrams

A reduced ordered binary decision diagram $t$ is
the leaf with value false if and only if $t$ has value false under every assignment of Boolean
values to the variables.

Formalized by `Cslib.Logic.PL.BDD.eq_leaf_false_iff`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Basic.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Basic.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html#eq-leaf-false-iff).

## Node constructor removing a redundant test

For a variable $v \in \mathbb{N}$ and diagrams
$\ell$ and $h$, the diagram $\mathrm{mk}(v, \ell, h)$ is $\ell$ if $\ell = h$, and otherwise the
node that tests $v$ with $\ell$ as its false-child and $h$ as its true-child.

Formalized by `Cslib.Logic.PL.BDD.mk`, a definition declared in [CSLibExt/Logics/Propositional/BDD/Basic.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Basic.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html#mk).

## Bryant's apply operation

For a binary Boolean operation $\mathrm{op}$ and binary decision
diagrams $t_1, t_2$, the diagram $A_{\mathrm{op}}(t_1, t_2)$ is defined by recursion. If $t_1$
and $t_2$ are leaves with values $a$ and $b$, it is the leaf with value $\mathrm{op}(a, b)$.
Otherwise let $v$ be the smallest variable tested at the root of $t_1$ or of $t_2$ (a leaf tests
none), and for $i = 1, 2$ let $\ell_i$ and $h_i$ be the low and high children of $t_i$ if its
root tests $v$, and $\ell_i = h_i = t_i$ otherwise. The result is
$\mathrm{mk}(v, A_{\mathrm{op}}(\ell_1, \ell_2), A_{\mathrm{op}}(h_1, h_2))$, where
$\mathrm{mk}(v, \ell, h)$ is $\ell$ if $\ell = h$, and otherwise the node testing $v$ with low
child $\ell$ and high child $h$.

Formalized by `Cslib.Logic.PL.BDD.apply`, a definition declared in [CSLibExt/Logics/Propositional/BDD/Basic.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Basic.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html#apply).

## Apply computes the operation pointwise

For every binary Boolean operation
$\mathrm{op}$, all binary decision diagrams $t_1$ and $t_2$, and every assignment $\sigma$ of
Boolean values to the variables, the value under $\sigma$ of the diagram
$\mathrm{apply}(\mathrm{op}, t_1, t_2)$ obtained from $t_1$ and $t_2$ by Bryant's apply operation
under $\mathrm{op}$ is $\mathrm{op}(a_1, a_2)$, where $a_i$ is the value of $t_i$ under $\sigma$.

Formalized by `Cslib.Logic.PL.BDD.eval_apply`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Basic.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Basic.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html#eval-apply).

## Apply preserves orderedness

Let $\mathrm{op}$ be a binary Boolean operation and $n$ a
natural number. If the diagrams $t_1$ and $t_2$ are both ordered from $n$, then the result of
apply with $\mathrm{op}$ on $t_1$ and $t_2$ is ordered from $n$.

Formalized by `Cslib.Logic.PL.BDD.orderedFrom_apply`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Basic.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Basic.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html#ordered-from-apply).

## Apply returns reduced diagrams

For every binary Boolean operation $\mathrm{op}$ and all
diagrams $t_1$ and $t_2$, the result of apply with $\mathrm{op}$ on $t_1$ and $t_2$ is reduced.

Formalized by `Cslib.Logic.PL.BDD.reduced_apply`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Basic.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Basic.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html#reduced-apply).

## Diagram of a proposition

Each proposition $A$ whose atoms are natural numbers is sent
to a binary decision diagram by recursion on $A$: an atom $x$ goes to the node testing $x$ with
the leaf false as its false-child and the leaf true as its true-child, and a conjunction
$A \wedge B$, disjunction $A \vee B$ or implication $A \to B$ goes to the result of apply on the
diagrams of $A$ and $B$ under the Boolean operation and, or, or $(a, b) \mapsto \lnot a \lor b$
respectively.

Formalized by `Cslib.Logic.PL.BDD.ofProposition`, a definition declared in [CSLibExt/Logics/Propositional/BDD/Basic.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Basic.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html#of-proposition).

## Equal BDDs iff equal truth tables

For propositions $A$ and $B$ over natural-number
atoms, the binary decision diagrams of $A$ and $B$ are equal if and only if $A$ and $B$ have the
same truth value under every valuation $\sigma : \mathbb{N} \to \mathrm{Bool}$.

Comparing the diagrams therefore decides truth-table equivalence.

Formalized by `Cslib.Logic.PL.BDD.ofProposition_eq_iff`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Basic.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Basic.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html#of-proposition-eq-iff).

## Satisfiable iff the BDD is not the false leaf

For a proposition $A$ over
natural-number atoms, the binary decision diagram of $A$ is not the leaf false if and only if
some valuation $\sigma : \mathbb{N} \to \mathrm{Bool}$ makes $A$ true.

Both sides always hold: the valuation that makes every atom true satisfies every proposition
built from atoms by conjunction, disjunction and implication.

Formalized by `Cslib.Logic.PL.BDD.ofProposition_ne_leaf_false_iff`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Basic.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Basic.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html#of-proposition-ne-leaf-false-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reduced ordered binary decision diagrams: canonicity and apply](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/propositional-logic/binary-decision-diagrams/reduced-ordered-binary-decision-diagrams-canonic)
