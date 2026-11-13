---
declaration: section
origin: cited
lean: Cslib.Modal.Derivable, Cslib.Modal.Deduces, Cslib.Modal.Axioms.K, Cslib.Modal.Axioms.T, Cslib.Modal.Axioms.S4, Cslib.Modal.Axioms.S5, Cslib.Modal.Derivable.imp_self, Cslib.Modal.Derivable.mono
statement: formalized
proof: formalized
---

# Normal modal logics

35 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html).

## Modal

## Theorems of a normal modal logic

Let $\Lambda$ be a set of modal formulas. The theorems of
the normal modal logic $\mathbf{K} \oplus \Lambda$ form the least set of modal formulas that
contains, for all modal formulas $\varphi$, $\psi$, $\chi$, the propositional axioms
$\varphi \to (\psi \to \varphi)$,
$(\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))$ and
$\neg\neg\varphi \to \varphi$ (where $\neg\varphi$ is $\varphi \to \bot$) and the distribution
axiom $\Box(\varphi \to \psi) \to (\Box\varphi \to \Box\psi)$, that contains every member of
$\Lambda$, and that is closed under modus ponens (from $\varphi \to \psi$ and $\varphi$ infer
$\psi$) and necessitation (from $\varphi$ infer $\Box\varphi$).

Formalized by `Cslib.Modal.Derivable`, an inductive type declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#derivable).

## Local consequence in a normal modal logic

Let $\Lambda$ and $\Gamma$ be sets of modal
formulas. The local consequences of the hypotheses $\Gamma$ in the normal modal logic
$\mathbf{K} \oplus \Lambda$ form the least set of modal formulas that contains every member of
$\Gamma$ and every theorem of $\mathbf{K} \oplus \Lambda$ and is closed under modus ponens: whenever
it contains $\varphi \to \psi$ and $\varphi$, it contains $\psi$.

Necessitation applies to theorems only, not to hypotheses.

Formalized by `Cslib.Modal.Deduces`, an inductive type declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#deduces).

## Extra axioms of the modal logic K

The set of extra axioms of the normal modal logic K is
the empty set of modal formulas over a given type of atoms; that is, K adds no axioms to the
propositional axioms and the distribution axiom.

Formalized by `Cslib.Modal.Axioms.K`, a definition declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#k).

## Extra axioms of T

The extra axioms of the modal logic T are the formulas
$\Box\varphi \to \varphi$ (axiom T), for all modal formulas $\varphi$.

Formalized by `Cslib.Modal.Axioms.T`, a definition declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#t).

## Extra axioms of S4

The extra axioms of the modal logic S4 are the formulas
$\Box\varphi \to \varphi$ (axiom T) and $\Box\varphi \to \Box\Box\varphi$ (axiom 4), for all
modal formulas $\varphi$.

Formalized by `Cslib.Modal.Axioms.S4`, a definition declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#s4).

## Extra axioms of S5

For a modal formula $\varphi$, write $\Diamond\varphi$ for
$\neg\Box\neg\varphi$. The extra axioms of the modal logic S5 are the formulas
$\Box\varphi \to \varphi$ (axiom T) and $\Diamond\varphi \to \Box\Diamond\varphi$ (axiom 5), for
all modal formulas $\varphi$.

Formalized by `Cslib.Modal.Axioms.S5`, a definition declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#s5).

## Self-implication is a theorem

Let $\Lambda$ be a set of modal formulas. For every modal
formula $\varphi$, the formula $\varphi \to \varphi$ is a theorem of the normal modal logic
$\mathbf{K} \oplus \Lambda$.

Formalized by `Cslib.Modal.Derivable.imp_self`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#imp-self).

## Monotonicity of theorems in the extra axioms

Let $\Lambda \subseteq \Lambda'$ be sets of
modal formulas. Every theorem of the normal modal logic $\mathrm{K} \oplus \Lambda$ is a theorem of
$\mathrm{K} \oplus \Lambda'$.

Formalized by `Cslib.Modal.Derivable.mono`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#mono).

## Monotonicity of local consequence in the hypotheses

Let $\Lambda$, $\Gamma$ and $\Delta$
be sets of modal formulas with $\Gamma \subseteq \Delta$. If a formula $\varphi$ is a local
consequence of the hypotheses $\Gamma$ in the normal modal logic $\mathrm{K} \oplus \Lambda$, then
$\varphi$ is a local consequence of the hypotheses $\Delta$ in $\mathrm{K} \oplus \Lambda$.

Formalized by `Cslib.Modal.Deduces.mono`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#mono-2).

## Transitivity of local consequence

Let $\Lambda$ be a set of modal formulas and let
$\Gamma$ and $\Delta$ be sets of formulas such that every formula of $\Delta$ is a local
consequence of $\Gamma$ in the normal modal logic $\mathbf{K} \oplus \Lambda$. If a formula
$\varphi$ is a local consequence of $\Delta$ in $\mathbf{K} \oplus \Lambda$, then $\varphi$ is a
local consequence of $\Gamma$ in $\mathbf{K} \oplus \Lambda$.

Formalized by `Cslib.Modal.Deduces.trans`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#trans).

## The deduction theorem for local modal consequence, forward direction

Let $\Lambda$ and
$\Gamma$ be sets of modal formulas and let $\varphi$, $\psi$ be modal formulas. If $\varphi$ is a
local consequence of $\Gamma \cup \{\psi\}$ in the normal modal logic $\mathbf{K} \oplus \Lambda$,
then $\psi \to \varphi$ is a local consequence of $\Gamma$ in $\mathbf{K} \oplus \Lambda$.

Formalized by `Cslib.Modal.Deduces.imp_of_insert`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#imp-of-insert).

## The deduction theorem for local modal consequence

Let $\Lambda$ and $\Gamma$ be sets of
modal formulas and let $\varphi$, $\psi$ be modal formulas. In the normal modal logic
$\mathbf{K} \oplus \Lambda$, $\varphi$ is a local consequence of $\Gamma \cup \{\psi\}$ if and only
if $\psi \to \varphi$ is a local consequence of $\Gamma$.

Formalized by `Cslib.Modal.deduces_insert_iff`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#deduces-insert-iff).

## Consequences of no hypotheses are the theorems

Let $\Lambda$ be a set of modal formulas.
A modal formula $\varphi$ is a local consequence of the empty set of hypotheses in the normal modal
logic $\mathbf{K} \oplus \Lambda$ if and only if $\varphi$ is a theorem of
$\mathbf{K} \oplus \Lambda$.

Formalized by `Cslib.Modal.deduces_empty_iff`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#deduces-empty-iff).

## Compactness of local modal consequence

Let $\Lambda$ and $\Gamma$ be sets of modal
formulas. If a modal formula $\varphi$ is a local consequence of the hypotheses $\Gamma$ in the
normal modal logic $\mathbf{K} \oplus \Lambda$, then there is a finite set
$\Delta \subseteq \Gamma$ such that $\varphi$ is a local consequence of $\Delta$ in
$\mathbf{K} \oplus \Lambda$.

Formalized by `Cslib.Modal.Deduces.exists_finset`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#exists-finset).

## Ex falso quodlibet

Let $\Lambda$ be a set of modal formulas and $\Gamma$ a set of
hypotheses. If $\bot$ is a local consequence of $\Gamma$ in the normal modal logic
$\mathbf{K} \oplus \Lambda$, then every formula $\varphi$ is a local consequence of $\Gamma$ in
$\mathbf{K} \oplus \Lambda$.

Formalized by `Cslib.Modal.Deduces.of_bot`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#of-bot).

## Contradiction yields falsity

Let $\Lambda$ and $\Gamma$ be sets of modal formulas and let
$\varphi$ be a modal formula. If both $\varphi$ and its negation $\neg\varphi$ are local
consequences of the hypotheses $\Gamma$ in the normal modal logic $\mathbf{K} \oplus \Lambda$, then
so is $\bot$.

Formalized by `Cslib.Modal.Deduces.bot_of_neg`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#bot-of-neg).

## Proof by contradiction

Let $\Lambda$ be a set of modal formulas, $\Gamma$ a set of
hypotheses and $\varphi$ a formula. If $\bot$ is a local consequence of
$\Gamma \cup \{\neg\varphi\}$ in the normal modal logic $\mathbf{K} \oplus \Lambda$, then
$\varphi$ is a local consequence of $\Gamma$ in $\mathbf{K} \oplus \Lambda$.

Formalized by `Cslib.Modal.Deduces.of_insert_neg`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#of-insert-neg).

## Negation introduction

Let $\Lambda$ and $\Gamma$ be sets of modal formulas and $\varphi$ a
formula. If $\bot$ is a local consequence of the hypotheses $\Gamma \cup \{\varphi\}$ in the normal
modal logic $\mathrm{K} \oplus \Lambda$, then $\neg\varphi$ is a local consequence of $\Gamma$ in
$\mathrm{K} \oplus \Lambda$, where $\neg\varphi$ abbreviates $\varphi \to \bot$.

Formalized by `Cslib.Modal.Deduces.neg_of_insert`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#neg-of-insert).

## Hypothetical syllogism

Let $\Lambda$ and $\Gamma$ be sets of modal formulas and let
$\varphi$, $\psi$, $\chi$ be modal formulas. If $\varphi \to \psi$ and $\psi \to \chi$ are local
consequences of the hypotheses $\Gamma$ in the normal modal logic $\mathbf{K} \oplus \Lambda$, then
so is $\varphi \to \chi$.

Formalized by `Cslib.Modal.Deduces.imp_trans`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#imp-trans).

## Double-negation introduction

Let $\Lambda$ and $\Gamma$ be sets of modal formulas. If a
formula $\varphi$ is a local consequence of the hypotheses $\Gamma$ in the normal modal logic
$\mathrm{K} \oplus \Lambda$, then so is $\neg\neg\varphi$, where $\neg\psi$ abbreviates
$\psi \to \bot$.

Formalized by `Cslib.Modal.Deduces.neg_neg`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#neg-neg).

## Local consequences of theorems are theorems

Let $\Lambda$ be a set of modal formulas
and let $\Gamma$ be a set of formulas each of which is a theorem of the normal modal logic
$\mathbf{K} \oplus \Lambda$. If a formula $\varphi$ is a local consequence of $\Gamma$ in
$\mathbf{K} \oplus \Lambda$, then $\varphi$ is a theorem of $\mathbf{K} \oplus \Lambda$.

Formalized by `Cslib.Modal.Derivable.of_deduces`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#of-deduces).

## The monotonicity rule for necessity

Let $\Lambda$ be a set of modal formulas and let
$\varphi$, $\psi$ be modal formulas. If $\varphi \to \psi$ is a theorem of the normal modal logic
$\mathbf{K} \oplus \Lambda$, then so is $\Box\varphi \to \Box\psi$.

Formalized by `Cslib.Modal.Derivable.box_imp_box`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#box-imp-box).

## Soundness of modal Hilbert systems for Kripke models

Let $\Lambda$ be a set of modal
formulas and $M$ a Kripke model in which every formula of $\Lambda$ is valid. Then every formula
derivable in $K \oplus \Lambda$ (from the propositional axioms, the distribution axiom and the
members of $\Lambda$ by modus ponens and necessitation) is valid in $M$, that is, it holds at
every world of $M$.

Formalized by `Cslib.Modal.Derivable.valid`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#valid).

## Local soundness

Let $M$ be a Kripke model and $\Lambda$ a set of modal formulas each
of which is valid in $M$. If a formula $\varphi$ is a local consequence of a set $\Gamma$ of
formulas in the normal modal logic $\mathbf{K} \oplus \Lambda$, then $\varphi$ holds at every
world of $M$ at which every formula of $\Gamma$ holds.

Formalized by `Cslib.Modal.Deduces.satisfies`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#satisfies).

## Soundness of K for Kripke models

Every theorem of the modal logic K is valid in every
Kripke model: if a formula $\varphi$ is derivable in K, then $\varphi$ holds at every world of
every Kripke model $M$.

Formalized by `Cslib.Modal.Derivable.valid_K`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#valid-k).

## Soundness of T for reflexive Kripke models

If the accessibility relation of a Kripke
model $M$ is reflexive, then every formula derivable in the modal logic T is valid in $M$, that
is, it holds at every world of $M$.

Formalized by `Cslib.Modal.Derivable.valid_T`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#valid-t).

## Soundness of S4 for reflexive transitive Kripke models

If the accessibility relation of
a Kripke model $M$ is reflexive and transitive, then every formula derivable in the modal logic
S4 is valid in $M$, that is, it holds at every world of $M$.

Formalized by `Cslib.Modal.Derivable.valid_S4`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#valid-s4).

## Soundness of S5 for Kripke models with an equivalence relation

If the accessibility
relation of a Kripke model $M$ is an equivalence relation, then every formula derivable in the
modal logic S5 is valid in $M$, that is, it holds at every world of $M$.

Formalized by `Cslib.Modal.Derivable.valid_S5`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#valid-s5).

## The one-world Kripke model

For any type of atoms, the one-world Kripke model has a
single world, which sees itself, and every atom is false at that world.

Formalized by `Cslib.Modal.KripkeModel.unit`, a definition declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#unit).

## The one-world model has an equivalence relation

The accessibility relation of the
one-world Kripke model, whose single world sees itself and at which every atom is false, is an
equivalence relation.

Formalized by `Cslib.Modal.KripkeModel.unit_equivalence`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#unit-equivalence).

## Consistency of normal modal logics

Let $\Lambda$ be a set of modal formulas each of which
is valid in the one-world Kripke model whose world sees itself and in which every atom is false.
Then $\bot$ is not a theorem of the normal modal logic $\mathrm{K} \oplus \Lambda$.

Formalized by `Cslib.Modal.not_derivable_bot`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#not-derivable-bot).

## Consistency of S5

For every type of atoms, $\bot$ is not a theorem of the normal modal
logic S5, whose extra axioms are the formulas $\Box\varphi \to \varphi$ and
$\Diamond\varphi \to \Box\Diamond\varphi$, where $\Diamond\varphi$ abbreviates
$\neg\Box\neg\varphi$ and $\neg\psi$ abbreviates $\psi \to \bot$.

Formalized by `Cslib.Modal.not_derivable_bot_S5`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#not-derivable-bot-s5).

## Consistency of S4

For every type of atoms, $\bot$ is not a theorem of the normal modal
logic S4, whose extra axioms are the formulas $\Box\varphi \to \varphi$ and
$\Box\varphi \to \Box\Box\varphi$.

Formalized by `Cslib.Modal.not_derivable_bot_S4`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#not-derivable-bot-s4).

## Consistency of T

For every type of atoms, $\bot$ is not a theorem of the normal modal
logic T, whose extra axioms are the formulas $\Box\varphi \to \varphi$.

Formalized by `Cslib.Modal.not_derivable_bot_T`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#not-derivable-bot-t).

## Consistency of K

For every type of atoms, $\bot$ is not a theorem of the normal modal
logic K, the logic with no extra axioms.

Formalized by `Cslib.Modal.not_derivable_bot_K`, a theorem declared in [CSLibExt/Logics/Modal/Hilbert.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/Modal/Hilbert.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html#not-derivable-bot-k).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Normal modal logics](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/normal-modal-logics/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/modal-logic/normal-modal-logics)
