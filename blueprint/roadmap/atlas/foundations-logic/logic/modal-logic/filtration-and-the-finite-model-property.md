---
declaration: section
origin: cited
lean: Cslib.Modal.Formula.sub, Cslib.Modal.Formula.sub_subset_of_mem, Cslib.Modal.finModel, Cslib.Modal.evalFin, Cslib.Modal.subType, Cslib.Modal.filtrationWorlds, Cslib.Modal.filtrationRel, Cslib.Modal.exists_subType_eq
statement: formalized
proof: formalized
---

# Filtration and the finite model property

36 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html).

## Subformulas

The finite set $\mathrm{sub}(\varphi)$ of subformulas of a modal formula
$\varphi$, including $\varphi$ itself, is defined by recursion: $\mathrm{sub}(p) = \{p\}$ for an
atom $p$, $\mathrm{sub}(\bot) = \{\bot\}$, $\mathrm{sub}(\varphi \to \psi) = \{\varphi \to \psi\}
\cup \mathrm{sub}(\varphi) \cup \mathrm{sub}(\psi)$, and $\mathrm{sub}(\Box\varphi) =
\{\Box\varphi\} \cup \mathrm{sub}(\varphi)$.

Formalized by `Cslib.Modal.Formula.sub`, a definition declared in [CSLibExt/Logics/Modal/Filtration.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Filtration.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#sub).

## The subformula relation is transitive

If $\psi$ is a subformula of a modal formula
$\varphi$, then every subformula of $\psi$ is a subformula of $\varphi$.

Formalized by `Cslib.Modal.Formula.sub_subset_of_mem`, a theorem declared in [CSLibExt/Logics/Modal/Filtration.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Filtration.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#sub-subset-of-mem).

## Finite Kripke model on sets of formulas

Let $U$ be a nonempty finite set of finite sets of
formulas and $R$ a finite set of pairs of finite sets of formulas. The Kripke model on $U$ with
relation $R$ has the elements of $U$ as worlds, a world $s$ sees a world $t$ iff $(s, t) \in R$,
and an atom $p$ is true at $s$ iff $p \in s$.

Formalized by `Cslib.Modal.finModel`, a definition declared in [CSLibExt/Logics/Modal/Filtration.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Filtration.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#fin-model).

## Boolean evaluation in a finite model

Given a finite set $U$ of finite sets of formulas, a
finite set $R$ of pairs of such sets and a finite set $s$ of formulas, the Boolean value of a
formula at $s$ is defined by recursion on the formula: an atom $p$ is true iff $p \in s$; $\bot$ is
false; $\varphi \to \psi$ is true iff $\varphi$ is false or $\psi$ is true at $s$; and $\Box\varphi$
is true iff $\varphi$ is true at every $t \in U$ with $(s, t) \in R$.

For $s \in U$ this computes satisfaction at $s$ in the finite Kripke model on $U$ with relation
$R$ in which an atom is true at a world iff it belongs to it.

Formalized by `Cslib.Modal.evalFin`, a definition declared in [CSLibExt/Logics/Modal/Filtration.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Filtration.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#eval-fin).

## Type of a world

Given a Kripke model $M$ and a modal formula $\varphi$, the type (or
$\Sigma$-type, for $\Sigma$ the set of subformulas of $\varphi$) of a world $w$ of $M$ is the
finite set of subformulas of $\varphi$ that hold at $w$ in $M$.

Formalized by `Cslib.Modal.subType`, a definition declared in [CSLibExt/Logics/Modal/Filtration.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Filtration.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#sub-type).

## Worlds of the filtration

Let $M$ be a Kripke model and $\varphi$ a modal formula. The
worlds of the filtration of $M$ through the subformulas of $\varphi$ form the finite set of types
occurring in $M$: the subsets $s$ of the set $\mathrm{sub}(\varphi)$ of subformulas of $\varphi$
such that $s$ is the set of subformulas of $\varphi$ satisfied at some world of $M$.

Formalized by `Cslib.Modal.filtrationWorlds`, a definition declared in [CSLibExt/Logics/Modal/Filtration.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Filtration.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#filtration-worlds).

## Smallest filtration relation

Let $M$ be a Kripke model and $\varphi$ a modal formula, and
call the set of subformulas of $\varphi$ satisfied at a world $w$ of $M$ the type of $w$. The
smallest filtration relation is the finite set of pairs $(s, t)$ of types such that there are
worlds $w$ and $w'$ of $M$ of types $s$ and $t$ with $w'$ accessible from $w$.

Formalized by `Cslib.Modal.filtrationRel`, a definition declared in [CSLibExt/Logics/Modal/Filtration.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Filtration.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#filtration-rel).

## Filtration worlds are realized types

Let $M$ be a Kripke model and $\varphi$ a modal
formula, and call the set of subformulas of $\varphi$ satisfied at a world $w$ of $M$ the type of
$w$. Every world $s$ of the filtration of $M$ through the subformulas of $\varphi$, that is, every
element of the finite set of types occurring in $M$, is the type of some world of $M$.

Formalized by `Cslib.Modal.exists_subType_eq`, a theorem declared in [CSLibExt/Logics/Modal/Filtration.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Filtration.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#exists-sub-type-eq).

## Worlds of the same type agree on subformulas

Let $M$ be a Kripke model and $\varphi$ a
modal formula, and call the set of subformulas of $\varphi$ true at a world $w$ of $M$ the type
of $w$. If two worlds $w$ and $v$ of $M$ have the same type, then every subformula $\psi$ of
$\varphi$ holds at $w$ iff it holds at $v$.

Formalized by `Cslib.Modal.satisfies_iff_of_subType_eq`, a theorem declared in [CSLibExt/Logics/Modal/Filtration.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Filtration.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#satisfies-iff-of-sub-type-eq).

## Filtration relations

Let $M$ be a Kripke model, $\varphi$ a modal formula, $\Sigma$ the
set of subformulas of $\varphi$, and for a world $w$ let $[w]$, the type of $w$, be the set of
formulas of $\Sigma$ true at $w$ in $M$. A relation $R$ on finite sets of formulas is a
filtration of $M$ through $\Sigma$ when (min) for all worlds $w, v$ related in $M$, the pair
$([w], [v])$ is in $R$, and (max) for all worlds $w, v$ with $([w], [v]) \in R$ and every
formula $\psi$ with $\Box\psi \in \Sigma$, if $\Box\psi$ holds at $w$ in $M$ then $\psi$ holds at
$v$ in $M$.

These are conditions (ii) and (iii) of Blackburn–de Rijke–Venema, Definition 2.36, in $\Box$
form; conditions (i) and (iv) (worlds are the $\Sigma$-types, atoms of $\Sigma$ true where they
belong) are built into the construction of the finite model.

Formalized by `Cslib.Modal.IsFiltration`, a structure declared in [CSLibExt/Logics/Modal/Filtration.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Filtration.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#is-filtration).

## Filtration lemma

Let $M$ be a Kripke model, $\varphi$ a modal formula, and for a world
$w$ let $[w]$, the type of $w$, be the set of subformulas of $\varphi$ true at $w$ in $M$. Let $R$
be a filtration of $M$ through the subformulas of $\varphi$, and let $M^R$ be the Kripke model
whose worlds are the types of the worlds of $M$, with accessibility relation $R$ and an atom
true at a type iff the type contains it. Then for every subformula $\psi$ of $\varphi$ and every
world $w$ of $M$, $\psi$ holds at $[w]$ in $M^R$ iff $\psi$ holds at $w$ in $M$.

Formalized by `Cslib.Modal.satisfies_finModel_filtrationWorlds_iff`, a theorem declared in [CSLibExt/Logics/Modal/Filtration.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Filtration.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#satisfies-fin-model-filtration-worlds-if).

## The smallest filtration is a filtration

Let $M$ be a Kripke model and $\varphi$ a modal
formula, and call the set of subformulas of $\varphi$ true at a world $w$ the type of $w$. The
relation that relates two types when some worlds of those types are related in $M$ is a
filtration of $M$ through the set of subformulas of $\varphi$.

Formalized by `Cslib.Modal.isFiltration_filtrationRel`, a theorem declared in [CSLibExt/Logics/Modal/Filtration.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Filtration.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#is-filtration-filtration-rel).

## Smallest filtration of a Kripke model

Let $M$ be a Kripke model and $\varphi$ a modal
formula, and call the set of subformulas of $\varphi$ satisfied at a world $w$ of $M$ the type of
$w$. The filtration of $M$ through the subformulas of $\varphi$ is the Kripke model whose worlds
are the types occurring in $M$, in which a type $s$ sees a type $t$ iff some world of type $s$
sees some world of type $t$ in $M$, and in which an atom $p$ is true at $s$ iff $p \in s$.

Formalized by `Cslib.Modal.filtration`, a definition declared in [CSLibExt/Logics/Modal/Filtration.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Filtration.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#filtration).

## Filtration lemma for the smallest filtration

Let $M$ be a Kripke model, $\varphi$ a
modal formula, and for a world $w$ let $[w]$, the type of $w$, be the set of subformulas of
$\varphi$ true at $w$ in $M$. For every subformula $\psi$ of $\varphi$ and every world $w$ of $M$,
$\psi$ holds at $[w]$ in the smallest filtration of $M$ through the subformulas of $\varphi$ iff
$\psi$ holds at $w$ in $M$.

Formalized by `Cslib.Modal.satisfies_filtration_iff`, a theorem declared in [CSLibExt/Logics/Modal/Filtration.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Filtration.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#satisfies-filtration-iff).

## Completeness of K, countermodel form

A modal formula that is not a theorem of K fails at
some world of some Kripke model.

Formalized by `Cslib.Modal.exists_not_satisfies_of_not_derivable_K`, a theorem declared in [CSLibExt/Logics/Modal/Filtration.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Filtration.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#exists-not-satisfies-of-not-derivable-k).

## Finite model property of K

A formula that is not a K-theorem fails in a Kripke model with
at most `2 ^ |sub φ|` worlds.

Formalized by `Cslib.Modal.exists_finite_countermodel`, a theorem declared in [CSLibExt/Logics/Modal/Filtration.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Filtration.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#exists-finite-countermodel).

## Finite validity check for K

A modal formula $\varphi$ passes the finite check when,
for every nonempty set $U$ of subsets of the set $\mathrm{sub}(\varphi)$ of subformulas of
$\varphi$, every relation $R \subseteq U \times U$ and every $s \in U$, the formula $\varphi$
is true at $s$ in the Kripke model with set of worlds $U$, accessibility relation $R$, and an
atom $p$ true at a world $t$ iff $p \in t$; truth is computed by recursion on $\varphi$.

Formalized by `Cslib.Modal.FinValid`, a definition declared in [CSLibExt/Logics/Modal/Filtration.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Filtration.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#fin-valid).

## Finite-check criterion for K-theorems

A modal formula $\varphi$ is a theorem of K iff it
passes the following finite check: for every nonempty set $U$ of subsets of the set
$\mathrm{sub}(\varphi)$ of subformulas of $\varphi$, every relation $R \subseteq U \times U$ and
every $s \in U$, $\varphi$ evaluates to true at $s$ in the finite Kripke model on $U$ with
relation $R$ in which an atom $p$ is true at $s$ iff $p \in s$.

Formalized by `Cslib.Modal.derivable_K_iff_finValid`, a theorem declared in [CSLibExt/Logics/Modal/Filtration.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Filtration.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#derivable-k-iff-fin-valid).

## K-theorems via finite models on sets of subformulas

A modal formula $\varphi$ is a theorem
of K iff for every nonempty set $U$ of subsets of the set $\mathrm{sub}(\varphi)$ of subformulas of
$\varphi$ and every finite set $R$ of pairs of finite sets of formulas, $\varphi$ holds at every
world of the Kripke model whose worlds are the elements of $U$, in which $s$ sees $t$ iff
$(s, t) \in R$, and in which an atom $p$ is true at $s$ iff $p \in s$.

Formalized by `Cslib.Modal.derivable_K_iff_forall_finModel`, a theorem declared in [CSLibExt/Logics/Modal/Filtration.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Filtration.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#derivable-k-iff-forall-fin-model).

## A filtration refutes what the model refutes

Let $M$ be a Kripke model, $\varphi$ a
formula and $R$ a filtration of $M$ through the subformulas of $\varphi$. If $\varphi$ fails at
some world of $M$, then $\varphi$ is not valid in the finite model whose worlds are the types of
worlds of $M$ (the sets of subformulas of $\varphi$ satisfied at a world), with relation $R$ and
an atom true at a type iff it belongs to it.

Formalized by `Cslib.Modal.not_valid_finModel_of_isFiltration`, a theorem declared in [CSLibExt/Logics/Modal/FiniteModelProperty.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/FiniteModelProperty.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#not-valid-fin-model-of-is-filtration).

## Lemmon filtration relation

Let $M$ be a Kripke model and $\varphi$ a formula, and let
$U_\varphi$ be the set of types of worlds of $M$ (the sets of subformulas of $\varphi$ satisfied at
a world). The Lemmon relation is the relation $R$ on $U_\varphi$ such that $s \mathrel{R} t$ iff
for every formula $\psi$ with $\Box\psi$ a subformula of $\varphi$, $\Box\psi \in s$ implies
$\Box\psi \in t$ and $\psi \in t$.

This is the $\Box$ form of Blackburn–de Rijke–Venema's transitive filtration $R^t$ (Lemma 2.42).

Formalized by `Cslib.Modal.lemmonRel`, a definition declared in [CSLibExt/Logics/Modal/FiniteModelProperty.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/FiniteModelProperty.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#lemmon-rel).

## S5 filtration relation

Let $M$ be a Kripke model and $\varphi$ a formula, and let
$U_\varphi$ be the set of types of worlds of $M$ (the sets of subformulas of $\varphi$ satisfied at
a world). The S5 relation is the relation $R$ on $U_\varphi$ such that $s \mathrel{R} t$ iff for
every formula $\psi$ with $\Box\psi$ a subformula of $\varphi$, $\Box\psi \in s$ iff
$\Box\psi \in t$.

Formalized by `Cslib.Modal.s5Rel`, a definition declared in [CSLibExt/Logics/Modal/FiniteModelProperty.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/FiniteModelProperty.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#s5-rel).

## The Lemmon relation is a filtration of a transitive model

For every Kripke model $M$
with a transitive accessibility relation and every formula $\varphi$, the Lemmon relation of $M$
and $\varphi$ is a filtration of $M$ through the subformulas of $\varphi$.

Formalized by `Cslib.Modal.isFiltration_lemmonRel`, a theorem declared in [CSLibExt/Logics/Modal/FiniteModelProperty.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/FiniteModelProperty.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#is-filtration-lemmon-rel).

## The S5 relation is a filtration of an equivalence model

For every Kripke model $M$ whose
accessibility relation is an equivalence relation and every formula $\varphi$, the S5 relation of
$M$ and $\varphi$ is a filtration of $M$ through the subformulas of $\varphi$.

Formalized by `Cslib.Modal.isFiltration_s5Rel`, a theorem declared in [CSLibExt/Logics/Modal/FiniteModelProperty.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/FiniteModelProperty.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#is-filtration-s5-rel).

## Reflexivity on a finite set of worlds

Let $U$ be a finite set of finite sets of modal
formulas and $R$ a finite set of pairs of such sets. Then $R$ is reflexive on $U$ when
$(s, s) \in R$ for every $s \in U$.

Formalized by `Cslib.Modal.FinRefl`, a definition declared in [CSLibExt/Logics/Modal/FiniteModelProperty.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/FiniteModelProperty.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#fin-refl).

## Transitivity on a finite set of worlds

Let $U$ be a finite set of finite sets of modal
formulas and $R$ a finite set of pairs of such sets. Then $R$ is transitive on $U$ when
$(s, r) \in R$ for all $s, t, r \in U$ with $(s, t) \in R$ and $(t, r) \in R$.

Formalized by `Cslib.Modal.FinTrans`, a definition declared in [CSLibExt/Logics/Modal/FiniteModelProperty.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/FiniteModelProperty.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#fin-trans).

## Symmetry on a finite set of worlds

Let $U$ be a finite set of finite sets of modal
formulas and $R$ a finite set of pairs of such sets. Then $R$ is symmetric on $U$ when
$(t, s) \in R$ for all $s, t \in U$ with $(s, t) \in R$.

Formalized by `Cslib.Modal.FinSymm`, a definition declared in [CSLibExt/Logics/Modal/FiniteModelProperty.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/FiniteModelProperty.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#fin-symm).

## Filtrations of reflexive models are reflexive

Let $M$ be a Kripke model whose
accessibility relation is reflexive, let $\varphi$ be a modal formula, and let $R$ be a
filtration of $M$ through the subformulas of $\varphi$. Then $(s, s) \in R$ for every set $s$
that is the set of subformulas of $\varphi$ true at some world of $M$.

Formalized by `Cslib.Modal.finRefl_of_isFiltration`, a theorem declared in [CSLibExt/Logics/Modal/FiniteModelProperty.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/FiniteModelProperty.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#fin-refl-of-is-filtration).

## Finite model property of T

If a modal formula $\varphi$ is not a theorem of T, then
there is a Kripke model with finitely many worlds, at most $2^{|\mathrm{sub}(\varphi)|}$ of them,
where $\mathrm{sub}(\varphi)$ is the set of subformulas of $\varphi$, whose accessibility
relation is reflexive and in which $\varphi$ is false at some world.

Formalized by `Cslib.Modal.exists_finite_countermodel_T`, a theorem declared in [CSLibExt/Logics/Modal/FiniteModelProperty.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/FiniteModelProperty.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#exists-finite-countermodel-t).

## Finite model property of S4

If a modal formula $\varphi$ is not a theorem of S4, then
there is a Kripke model with finitely many worlds, at most $2^{|\mathrm{sub}(\varphi)|}$ of them,
where $\mathrm{sub}(\varphi)$ is the set of subformulas of $\varphi$, whose accessibility
relation is reflexive and transitive and in which $\varphi$ is false at some world.

Formalized by `Cslib.Modal.exists_finite_countermodel_S4`, a theorem declared in [CSLibExt/Logics/Modal/FiniteModelProperty.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/FiniteModelProperty.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#exists-finite-countermodel-s4).

## Finite model property of S5

If a modal formula $\varphi$ is not a theorem of S5, then
there is a Kripke model with finitely many worlds, at most $2^{|\mathrm{sub}(\varphi)|}$ of them,
where $\mathrm{sub}(\varphi)$ is the set of subformulas of $\varphi$, whose accessibility
relation is an equivalence relation and in which $\varphi$ is false at some world.

Formalized by `Cslib.Modal.exists_finite_countermodel_S5`, a theorem declared in [CSLibExt/Logics/Modal/FiniteModelProperty.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/FiniteModelProperty.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#exists-finite-countermodel-s5).

## Finite validity check for a frame condition

Given a condition $C$ on pairs $(U, R)$ of a
finite set $U$ of sets of formulas and a finite set $R$ of pairs of such sets, a formula $\varphi$
passes the finite check for $C$ when, for every nonempty set $U$ of subsets of the subformulas of
$\varphi$ and every relation $R \subseteq U \times U$ with $C(U, R)$, $\varphi$ holds at every
$s \in U$ in the Kripke model with worlds $U$, accessibility relation $R$, and an atom true at
$s$ iff it belongs to $s$.

Formalized by `Cslib.Modal.FinValidWith`, a definition declared in [CSLibExt/Logics/Modal/FiniteModelProperty.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/FiniteModelProperty.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#fin-valid-with).

## The finite check covers the filtration worlds

Let $C$ be a condition on pairs $(U, R)$ of
a finite set $U$ of sets of formulas and a finite relation $R$ on such sets, and let $\varphi$ be
a formula that passes the finite check for $C$. Let $M$ be a Kripke model, let $U_\varphi$ be the
set of types of worlds of $M$ (the sets of subformulas of $\varphi$ satisfied at a world), and
let $R \subseteq U_\varphi \times U_\varphi$ satisfy $C(U_\varphi, R)$. Then $\varphi$ is valid in
the finite model on $U_\varphi$ with relation $R$, in which an atom holds at $s$ iff it belongs to
$s$.

Formalized by `Cslib.Modal.finValidWith_apply`, a theorem declared in [CSLibExt/Logics/Modal/FiniteModelProperty.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/FiniteModelProperty.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#fin-valid-with-apply).

## T-provability via finite reflexive models

A modal formula $\varphi$ is a theorem of T
if and only if, for every nonempty set $U$ of subsets of $\mathrm{sub}(\varphi)$, the set of
subformulas of $\varphi$, and every relation $R \subseteq U \times U$ that is reflexive on $U$,
the formula $\varphi$ is true at every world $s \in U$ of the finite model with worlds $U$,
accessibility relation $R$, and each atom true at $s$ exactly when it belongs to $s$.

Formalized by `Cslib.Modal.derivable_T_iff_finValidWith`, a theorem declared in [CSLibExt/Logics/Modal/FiniteModelProperty.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/FiniteModelProperty.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#derivable-t-iff-fin-valid-with).

## S4-provability via finite reflexive transitive models

A modal formula $\varphi$ is a
theorem of S4 if and only if, for every nonempty set $U$ of subsets of $\mathrm{sub}(\varphi)$,
the set of subformulas of $\varphi$, and every relation $R \subseteq U \times U$ that is reflexive
and transitive on $U$, the formula $\varphi$ is true at every world $s \in U$ of the finite model
with worlds $U$, accessibility relation $R$, and each atom true at $s$ exactly when it belongs
to $s$.

Formalized by `Cslib.Modal.derivable_S4_iff_finValidWith`, a theorem declared in [CSLibExt/Logics/Modal/FiniteModelProperty.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/FiniteModelProperty.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#derivable-s4-iff-fin-valid-with).

## S5-provability via finite equivalence models

A modal formula $\varphi$ is a theorem of
S5 if and only if, for every nonempty set $U$ of subsets of $\mathrm{sub}(\varphi)$, the set of
subformulas of $\varphi$, and every relation $R \subseteq U \times U$ that is reflexive, symmetric
and transitive on $U$, the formula $\varphi$ is true at every world $s \in U$ of the finite model
with worlds $U$, accessibility relation $R$, and each atom true at $s$ exactly when it belongs
to $s$.

Formalized by `Cslib.Modal.derivable_S5_iff_finValidWith`, a theorem declared in [CSLibExt/Logics/Modal/FiniteModelProperty.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/FiniteModelProperty.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html#derivable-s5-iff-fin-valid-with).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Filtration and the finite model property](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/modal-logic/filtration-and-the-finite-model-property)
