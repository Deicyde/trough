---
declaration: section
origin: cited
lean: Cslib.Modal.Formula, Cslib.Modal.Formula.neg, Cslib.Modal.Formula.dia, Cslib.Modal.Formula.top, Cslib.Modal.Formula.and, Cslib.Modal.Formula.or, Cslib.Modal.Formula.axiomK, Cslib.Modal.Formula.axiomT
statement: formalized
proof: formalized
---

# Kripke semantics

29 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html).

## Modal

## Modal formulas

For a type $\alpha$ of atoms, the formulas of basic modal logic over
$\alpha$ are generated as follows: every atom $p \in \alpha$ is a formula; falsity $\bot$ is a
formula; if $\varphi$ and $\psi$ are formulas then so is the implication $\varphi \to \psi$; and
if $\varphi$ is a formula then so is the necessity formula $\Box\varphi$.

Formalized by `Cslib.Modal.Formula`, an inductive type declared in [CSLibExt/Logics/Modal/Kripke.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#formula).

## Negation of modal formulas

The negation of a modal formula $\varphi$ is the formula
$\neg\varphi := \varphi \to \bot$.

Formalized by `Cslib.Modal.Formula.neg`, a definition declared in [CSLibExt/Logics/Modal/Kripke.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#neg).

## The possibility operator

For a modal formula $\varphi$, the formula $\Diamond\varphi$
("possibly $\varphi$") is $\neg\Box\neg\varphi$, where $\neg\chi$ stands for $\chi \to \bot$.

Formalized by `Cslib.Modal.Formula.dia`, a definition declared in [CSLibExt/Logics/Modal/Kripke.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#dia).

## The truth constant

The formula $\top$ is the negation $\neg\bot$ of falsity, that is,
the implication $\bot \to \bot$.

Formalized by `Cslib.Modal.Formula.top`, a definition declared in [CSLibExt/Logics/Modal/Kripke.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#top).

## Conjunction

For modal formulas $\varphi$ and $\psi$, the conjunction $\varphi \wedge \psi$
is the formula $\neg(\varphi \to \neg\psi)$, where $\neg\chi$ stands for $\chi \to \bot$.

Formalized by `Cslib.Modal.Formula.and`, a definition declared in [CSLibExt/Logics/Modal/Kripke.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#and).

## Disjunction of modal formulas

The disjunction of modal formulas $\varphi$ and $\psi$ is
the formula $\varphi \lor \psi := \neg\varphi \to \psi$, where $\neg\varphi$ is
$\varphi \to \bot$.

Formalized by `Cslib.Modal.Formula.or`, a definition declared in [CSLibExt/Logics/Modal/Kripke.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#or).

## Axiom K

For modal formulas $\varphi$ and $\psi$, the distribution axiom K is the formula
$\Box(\varphi \to \psi) \to (\Box\varphi \to \Box\psi)$.

Formalized by `Cslib.Modal.Formula.axiomK`, a definition declared in [CSLibExt/Logics/Modal/Kripke.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#axiom-k).

## Axiom T

For a modal formula $\varphi$, the reflexivity axiom T is the formula
$\Box\varphi \to \varphi$.

Formalized by `Cslib.Modal.Formula.axiomT`, a definition declared in [CSLibExt/Logics/Modal/Kripke.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#axiom-t).

## Axiom 4

For a modal formula $\varphi$, the transitivity axiom 4 is the formula
$\Box\varphi \to \Box\Box\varphi$.

Formalized by `Cslib.Modal.Formula.axiomFour`, a definition declared in [CSLibExt/Logics/Modal/Kripke.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#axiom-four).

## Axiom D

For a modal formula $\varphi$, the seriality axiom D is the formula
$\Box\varphi \to \Diamond\varphi$, where $\Diamond\psi$ is $\neg\Box\neg\psi$ and $\neg\chi$ stands
for $\chi \to \bot$.

Formalized by `Cslib.Modal.Formula.axiomD`, a definition declared in [CSLibExt/Logics/Modal/Kripke.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#axiom-d).

## Axiom B

For a modal formula $\varphi$, the symmetry axiom B is the formula
$\varphi \to \Box\Diamond\varphi$, where $\Diamond\psi$ is $\neg\Box\neg\psi$ and $\neg\chi$ stands
for $\chi \to \bot$.

Formalized by `Cslib.Modal.Formula.axiomB`, a definition declared in [CSLibExt/Logics/Modal/Kripke.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#axiom-b).

## Axiom 5

For a modal formula $\varphi$, the euclidean axiom 5 is the formula
$\Diamond\varphi \to \Box\Diamond\varphi$, where $\Diamond\psi$ is $\neg\Box\neg\psi$ and $\neg\chi$
stands for $\chi \to \bot$.

Formalized by `Cslib.Modal.Formula.axiomFive`, a definition declared in [CSLibExt/Logics/Modal/Kripke.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#axiom-five).

## Kripke model

A Kripke model consists of a nonempty collection of worlds, an accessibility relation,
and an atom valuation.

Formalized by `Cslib.Modal.KripkeModel`, a structure declared in [CSLibExt/Logics/Modal/Kripke.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#kripke-model).

## Satisfaction in a Kripke model

Let $M$ be a Kripke model with accessibility relation
$R$. Satisfaction of a modal formula at a world $w$ of $M$ is defined by recursion on the
formula: $w$ satisfies an atom $p$ if and only if the valuation of $M$ makes $p$ true at $w$;
$w$ never satisfies $\bot$; $w$ satisfies $\varphi \to \psi$ if and only if $w$ satisfies
$\psi$ whenever it satisfies $\varphi$; and $w$ satisfies $\Box\varphi$ if and only if every
world $v$ with $w \mathrel{R} v$ satisfies $\varphi$.

Formalized by `Cslib.Modal.KripkeModel.Satisfies`, a definition declared in [CSLibExt/Logics/Modal/Kripke.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#satisfies).

## Global validity in a Kripke model

A formula $\varphi$ is globally valid in a Kripke
model $M$ when $\varphi$ is satisfied at every world of $M$.

Formalized by `Cslib.Modal.KripkeModel.Valid`, a definition declared in [CSLibExt/Logics/Modal/Kripke.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#valid).

## Falsity is valid in no Kripke model

For every Kripke model $M$, the formula $\bot$ is
not valid in $M$: since $M$ has at least one world and no world satisfies $\bot$, some world
of $M$ fails to satisfy $\bot$.

Formalized by `Cslib.Modal.KripkeModel.not_valid_bot`, a theorem declared in [CSLibExt/Logics/Modal/Kripke.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#not-valid-bot).

## Semantics of possibility

Let $M$ be a Kripke model with accessibility relation $R$, and
let $\Diamond\varphi$ denote the formula $\neg\Box\neg\varphi$, where $\neg\chi$ is
$\chi \to \bot$. For every world $w$ and modal formula $\varphi$, $w$ satisfies $\Diamond\varphi$
in $M$ if and only if there is a world $v$ with $w \mathrel{R} v$ such that $v$ satisfies
$\varphi$ in $M$.

Formalized by `Cslib.Modal.KripkeModel.satisfies_dia`, a theorem declared in [CSLibExt/Logics/Modal/Kripke.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#satisfies-dia).

## Validity of axiom K on Kripke models

The K axiom is valid on every Kripke model.

Formalized by `Cslib.Modal.KripkeModel.valid_axiomK`, a theorem declared in [CSLibExt/Logics/Modal/Kripke.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#valid-axiom-k).

## Axiom T is valid on reflexive Kripke models

Let $M$ be a Kripke model whose
accessibility relation $R$ is reflexive: $R\,w\,w$ for every world $w$. Then for every formula
$\varphi$ the T axiom $\Box\varphi \to \varphi$ is globally valid in $M$.

Formalized by `Cslib.Modal.KripkeModel.valid_axiomT`, a theorem declared in [CSLibExt/Logics/Modal/Kripke.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#valid-axiom-t).

## Axiom 4 is valid on transitive Kripke models

Let $M$ be a Kripke model whose
accessibility relation $R$ is transitive: $R\,u\,v$ and $R\,v\,w$ imply $R\,u\,w$ for all worlds
$u, v, w$. Then for every formula $\varphi$ the 4 axiom $\Box\varphi \to \Box\Box\varphi$ is
globally valid in $M$.

Formalized by `Cslib.Modal.KripkeModel.valid_axiomFour`, a theorem declared in [CSLibExt/Logics/Modal/Kripke.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#valid-axiom-four).

## Axiom D is valid on serial Kripke models

Let $M$ be a Kripke model whose accessibility
relation $R$ is serial: every world $w$ has some world $v$ with $R\,w\,v$. Then for every formula
$\varphi$ the D axiom $\Box\varphi \to \Diamond\varphi$, where $\Diamond\varphi$ abbreviates
$\neg\Box\neg\varphi$, is globally valid in $M$.

Formalized by `Cslib.Modal.KripkeModel.valid_axiomD`, a theorem declared in [CSLibExt/Logics/Modal/Kripke.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#valid-axiom-d).

## Axiom B is valid on symmetric Kripke models

Let $M$ be a Kripke model whose
accessibility relation $R$ is symmetric: $R\,u\,v$ implies $R\,v\,u$ for all worlds $u, v$.
Then for every formula $\varphi$ the B axiom $\varphi \to \Box\Diamond\varphi$, where
$\Diamond\varphi$ abbreviates $\neg\Box\neg\varphi$, is globally valid in $M$.

Formalized by `Cslib.Modal.KripkeModel.valid_axiomB`, a theorem declared in [CSLibExt/Logics/Modal/Kripke.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#valid-axiom-b).

## Axiom 5 is valid on euclidean Kripke models

Let $M$ be a Kripke model whose
accessibility relation $R$ is euclidean: $R\,u\,v$ and $R\,u\,w$ imply $R\,v\,w$ for all worlds
$u, v, w$. Then for every formula $\varphi$ the 5 axiom $\Diamond\varphi \to \Box\Diamond\varphi$,
where $\Diamond\varphi$ abbreviates $\neg\Box\neg\varphi$, is globally valid in $M$.

Formalized by `Cslib.Modal.KripkeModel.valid_axiomFive`, a theorem declared in [CSLibExt/Logics/Modal/Kripke.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#valid-axiom-five).

## Bounded morphism

Let $M$ and $N$ be Kripke models over the same atoms, with sets of worlds
$W$ and $V$ and accessibility relations $R_M$ and $R_N$. A bounded morphism from $M$ to $N$ is
a map $f : W \to V$ such that every atom holds at a world $w$ in $M$ if and only if it holds
at $f(w)$ in $N$; whenever $w \mathrel{R_M} w'$, also $f(w) \mathrel{R_N} f(w')$ (forth); and
whenever $f(w) \mathrel{R_N} v'$, there is a world $w'$ with $w \mathrel{R_M} w'$ and
$f(w') = v'$ (back).

Bounded morphisms are also called p-morphisms.

Formalized by `Cslib.Modal.BoundedMorphism`, a structure declared in [CSLibExt/Logics/Modal/Kripke.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#bounded-morphism).

## Extensionality for bounded morphisms

Two bounded morphisms $f$ and $g$ between the same
Kripke models are equal if $f(w) = g(w)$ for every world $w$.

Formalized by `Cslib.Modal.BoundedMorphism.ext`, a theorem declared in [CSLibExt/Logics/Modal/Kripke.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#ext).

## Identity bounded morphism

For every Kripke model $M$, the identity map on the worlds of
$M$ is a bounded morphism from $M$ to itself.

Formalized by `Cslib.Modal.BoundedMorphism.id`, a definition declared in [CSLibExt/Logics/Modal/Kripke.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#id).

## Composition of bounded morphisms

Let $M_1$, $M_2$, $M_3$ be Kripke models over the same
atoms. If $f$ is a bounded morphism from $M_1$ to $M_2$ and $g$ is a bounded morphism from $M_2$
to $M_3$, then the composite map $g \circ f$ on worlds is a bounded morphism from $M_1$ to
$M_3$.

Formalized by `Cslib.Modal.BoundedMorphism.comp`, a definition declared in [CSLibExt/Logics/Modal/Kripke.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#comp).

## Invariance of modal satisfaction under bounded morphisms

Let $f$ be a bounded morphism
from a Kripke model $M$ to a Kripke model $N$ over the same atoms. Then for every modal formula
$\varphi$ and every world $w$ of $M$, $w$ satisfies $\varphi$ in $M$ if and only if $f(w)$
satisfies $\varphi$ in $N$.

Formalized by `Cslib.Modal.BoundedMorphism.satisfies_iff`, a theorem declared in [CSLibExt/Logics/Modal/Kripke.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#satisfies-iff).

## Surjective bounded morphisms preserve and reflect validity

Let $M$ and $N$ be Kripke
models over the same atoms and let $f$ be a bounded morphism from $M$ to $N$ whose map on worlds
is surjective. Then for every formula $\varphi$, $\varphi$ is globally valid in $M$ if and only
if $\varphi$ is globally valid in $N$.

Formalized by `Cslib.Modal.BoundedMorphism.valid_iff_of_surjective`, a theorem declared in [CSLibExt/Logics/Modal/Kripke.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Kripke.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html#valid-iff-of-surjective).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kripke semantics](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/kripke-semantics/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/modal-logic/kripke-semantics)
