---
declaration: section
origin: cited
lean: Cslib.Logic.PL.BDD.restrict, Cslib.Logic.PL.BDD.reduced_restrict, Cslib.Logic.PL.BDD.isROBDD_restrict, Cslib.Logic.PL.BDD.existsVar, Cslib.Logic.PL.BDD.forallVar, Cslib.Logic.PL.BDD.isROBDD_existsVar, Cslib.Logic.PL.BDD.satPath, Cslib.Logic.PL.BDD.ofPath
statement: formalized
proof: formalized
---

# Restriction, quantification, and satisfying paths for BDDs

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/restriction-quantification-and-satisfying-paths/index.html).

## Restriction

## Restriction of a binary decision diagram

For a variable $x$ and a Boolean $b$, the
restriction (cofactor) $t[x := b]$ of a binary decision diagram $t$ is defined recursively: a
leaf is kept; a node testing $x$ is replaced by the restriction of its $\mathrm{hi}$ child if $b$
is true and of its $\mathrm{lo}$ child if $b$ is false; and a node testing any other variable
$v$ is rebuilt from the restrictions of its two children with the reducing node constructor,
which returns the common child when the two are equal and a node testing $v$ otherwise.

Formalized by `Cslib.Logic.PL.BDD.restrict`, a definition declared in [CSLibExt/Logics/Propositional/BDD/Quantify.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Quantify.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/restriction-quantification-and-satisfying-paths/index.html#restrict).

## Restriction yields a reduced diagram

For every binary decision diagram $t$, every
variable $x$ and every Boolean $b$, the cofactor $t[x := b]$ is reduced: no node has two equal
children.

Nodes that restriction keeps are rebuilt with the node constructor that removes redundant
tests, so the input need not be reduced.

Formalized by `Cslib.Logic.PL.BDD.reduced_restrict`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Quantify.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Quantify.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/restriction-quantification-and-satisfying-paths/index.html#reduced-restrict).

## Restriction yields an ROBDD

If $t$ is an ordered binary decision diagram (tested
variables strictly increase along every path), then for every variable $x$ and every Boolean
$b$ the cofactor $t[x := b]$ is a reduced ordered binary decision diagram.

Formalized by `Cslib.Logic.PL.BDD.isROBDD_restrict`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Quantify.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Quantify.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/restriction-quantification-and-satisfying-paths/index.html#is-robdd-restrict).

## Existential quantification of a diagram

For a variable $x$ and a binary decision diagram
$t$, the existential quantification of $t$ over $x$ is the diagram obtained by combining the
cofactors $t[x := \mathrm{false}]$ and $t[x := \mathrm{true}]$ with Bryant's apply under
disjunction.

Formalized by `Cslib.Logic.PL.BDD.existsVar`, a definition declared in [CSLibExt/Logics/Propositional/BDD/Quantify.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Quantify.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/restriction-quantification-and-satisfying-paths/index.html#exists-var).

## Universal quantification of a diagram

For a variable $x$ and a binary decision diagram
$t$, the universal quantification of $t$ over $x$ is the diagram obtained by combining the
cofactors $t[x := \mathrm{false}]$ and $t[x := \mathrm{true}]$ with Bryant's apply under
conjunction.

Formalized by `Cslib.Logic.PL.BDD.forallVar`, a definition declared in [CSLibExt/Logics/Propositional/BDD/Quantify.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Quantify.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/restriction-quantification-and-satisfying-paths/index.html#forall-var).

## Existential quantification yields an ROBDD

If $t$ is an ordered binary decision diagram
(tested variables strictly increase along every path), then for every variable $x$ the
existential quantification of $t$ over $x$ is a reduced ordered binary decision diagram.

Formalized by `Cslib.Logic.PL.BDD.isROBDD_existsVar`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Quantify.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Quantify.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/restriction-quantification-and-satisfying-paths/index.html#is-robdd-exists-var).

## Satisfying path of a binary decision diagram

The satisfying path of a diagram is found
by a depth-first search for a leaf $\mathrm{true}$ that tries the $\mathrm{hi}$ (true) child of
each node before its $\mathrm{lo}$ (false) child. It is returned as the list of pairs $(v, c)$ of
the variables $v$ tested along the path with the branches $c$ taken (empty at a leaf
$\mathrm{true}$), and the search returns nothing when the diagram has no leaf $\mathrm{true}$.

Formalized by `Cslib.Logic.PL.BDD.satPath`, a definition declared in [CSLibExt/Logics/Propositional/BDD/Quantify.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Quantify.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/restriction-quantification-and-satisfying-paths/index.html#sat-path).

## Assignment read off a path

For a path $p$, given as a list of pairs $(v, b)$ of a
variable $v \in \mathbb{N}$ and a Boolean $b$, the assignment read off $p$ sends a variable $x$
to the Boolean of the first pair in $p$ whose variable is $x$, and to $\mathrm{false}$ if $x$
occurs in no pair of $p$.

Formalized by `Cslib.Logic.PL.BDD.ofPath`, a definition declared in [CSLibExt/Logics/Propositional/BDD/Quantify.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Quantify.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/restriction-quantification-and-satisfying-paths/index.html#of-path).

## The path assignment satisfies an ordered diagram

Let $t$ be a binary decision diagram
ordered from some $n$ (every tested variable is at least $n$, and tested variables strictly
increase along every path). If the satisfying-path search on $t$ returns a path $p$, then $t$
evaluates to true under the assignment read off $p$.

Formalized by `Cslib.Logic.PL.BDD.eval_ofPath_satPath`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Quantify.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Quantify.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/restriction-quantification-and-satisfying-paths/index.html#eval-of-path-sat-path).

## Reduced diagrams other than false have a satisfying path

If a binary decision diagram
$t$ is reduced and is not the leaf $\mathrm{false}$, then the search for a satisfying path in $t$
succeeds: it returns a path from the root of $t$ to a leaf $\mathrm{true}$.

Formalized by `Cslib.Logic.PL.BDD.satPath_isSome_of_ne`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Quantify.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Quantify.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/restriction-quantification-and-satisfying-paths/index.html#sat-path-is-some-of-ne).

## Satisfiability with one variable fixed to false

Let $A$ be a proposition over atoms
indexed by natural numbers, let $t$ be its ROBDD, and let $f$ be a natural number. Then $A$
evaluates to true under some valuation $\sigma$ with $\sigma(f) = \mathrm{false}$ if and only
if the cofactor $t[f := \mathrm{false}]$ is not the leaf $\mathrm{false}$.

The variable $f$ can, for instance, play the role of falsum. Without such a constraint, every
proposition over atoms indexed by natural numbers is satisfied by the all-true valuation.

Formalized by `Cslib.Logic.PL.BDD.exists_evalBool_eq_false_at_iff`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Quantify.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Quantify.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/restriction-quantification-and-satisfying-paths/index.html#exists-eval-bool-eq-false-at-iff).

## Satisfy-one with a variable fixed to false

Let $A$ be a proposition over
natural-number atoms and let $f$ be a natural number. If some assignment $\sigma$ with
$\sigma(f) = \mathrm{false}$ satisfies $A$, then the search for a satisfying path in the
restriction at $f := \mathrm{false}$ of the ROBDD of $A$ returns a path $p$, and the assignment
read off $p$ (the recorded value on each variable of $p$, false elsewhere), changed to send $f$
to $\mathrm{false}$, satisfies $A$.

Formalized by `Cslib.Logic.PL.BDD.satPath_restrict_ofProposition`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Quantify.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Quantify.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/restriction-quantification-and-satisfying-paths/index.html#sat-path-restrict-of-proposition).

## The all-true valuation satisfies every proposition

Every proposition $A$ over atoms
indexed by natural numbers, built from atoms with $\land$, $\lor$ and $\to$ only, evaluates to
true under the valuation that makes every atom true.

Formalized by `Cslib.Logic.PL.BDD.evalBool_allTrue`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Quantify.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Quantify.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/restriction-quantification-and-satisfying-paths/index.html#eval-bool-all-true).

## Satisfy-one for propositions

For every proposition $A$ over atoms indexed by natural
numbers, the satisfying-path search on the ROBDD of $A$ returns a path $p$, and $A$ evaluates to
true under the assignment read off $p$.

Every such proposition is satisfiable, by the all-true valuation; the path usually gives a
different model.

Formalized by `Cslib.Logic.PL.BDD.ofProposition_satPath`, a theorem declared in [CSLibExt/Logics/Propositional/BDD/Quantify.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Propositional/BDD/Quantify.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/restriction-quantification-and-satisfying-paths/index.html#of-proposition-sat-path).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Restriction, quantification, and satisfying paths for BDDs](https://deicyde.github.io/atlas-lean/roadmap/Logic/propositional-logic/binary-decision-diagrams/restriction-quantification-and-satisfying-paths/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/propositional-logic/binary-decision-diagrams/restriction-quantification-and-satisfying-paths)
