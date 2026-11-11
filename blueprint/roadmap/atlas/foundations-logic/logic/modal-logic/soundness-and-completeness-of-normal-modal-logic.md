---
declaration: section
origin: cited
lean: Cslib.Modal.Formula.ofProposition, Cslib.Modal.KripkeModel.ofModel, Cslib.Modal.satisfies_ofProposition, Cslib.Modal.KripkeModel.toModel, Cslib.Modal.KripkeModel.ofModel_toModel, Cslib.Modal.KripkeModel.toModel_ofModel, Cslib.Modal.Formula.toProposition, Cslib.Modal.satisfies_toProposition
statement: formalized
proof: formalized
---

# Soundness and completeness of normal modal logics

53 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html).

## Translation of CSLib's modal propositions

CSLib's unimodal propositions are translated into
modal formulas in the $\bot$, $\to$, $\Box$ basis by recursion, writing $\varphi'$ for the
translation of $\varphi$: an atom $p$ goes to $p$, falsehood to $\bot$, $\neg\varphi$ to
$\varphi' \to \bot$, $\varphi \lor \psi$ to $(\varphi' \to \bot) \to \psi'$, and the diamond
(the unimodal triangle) applied to $\varphi$ goes to $\Diamond\varphi'$, that is, to
$\Box(\varphi' \to \bot) \to \bot$.

Formalized by `Cslib.Modal.Formula.ofProposition`, a definition declared in [CSLibExt/Logics/Modal/CslibTranslation.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/CslibTranslation.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#of-proposition).

## Kripke model of a CSLib model

For a CSLib unimodal model $m$ on a nonempty type of worlds,
the associated Kripke model has the same worlds, the binary accessibility relation of $m$ as its
accessibility relation, and the valuation of $m$ as its valuation.

Formalized by `Cslib.Modal.KripkeModel.ofModel`, a definition declared in [CSLibExt/Logics/Modal/CslibTranslation.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/CslibTranslation.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#of-model).

## The translation preserves satisfaction

Let $m$ be a CSLib unimodal model on a nonempty type
of worlds, $w$ a world and $\varphi$ a CSLib unimodal proposition. Then the translation of $\varphi$
into the $\bot$, $\to$, $\Box$ basis holds at $w$ in the Kripke model of $m$ if and only if
$\varphi$ holds at $w$ in $m$.

Formalized by `Cslib.Modal.satisfies_ofProposition`, a theorem declared in [CSLibExt/Logics/Modal/CslibTranslation.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/CslibTranslation.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#satisfies-of-proposition).

## The CSLib unimodal model of a Kripke model

A Kripke model $k$ on worlds $W$ gives the
CSLib unimodal model on $W$ whose frame is the unimodal frame built from the accessibility
relation of $k$ and whose valuation is the valuation of $k$.

Formalized by `Cslib.Modal.KripkeModel.toModel`, a definition declared in [CSLibExt/Logics/Modal/CslibTranslation.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/CslibTranslation.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#to-model).

## Kripke to CSLib and back is the identity

Let $k$ be a Kripke model on a nonempty type of
worlds. Converting $k$ to a CSLib unimodal model and converting that model back to a Kripke model
gives $k$.

Formalized by `Cslib.Modal.KripkeModel.ofModel_toModel`, a theorem declared in [CSLibExt/Logics/Modal/CslibTranslation.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/CslibTranslation.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#of-model-to-model).

## Round trip from CSLib models through Kripke models

For a nonempty type of worlds $W$,
converting a CSLib unimodal model $m$ on $W$ into a Kripke model and then back into a CSLib
unimodal model returns $m$: a unimodal frame is determined by its binary accessibility relation.

Formalized by `Cslib.Modal.KripkeModel.toModel_ofModel`, a theorem declared in [CSLibExt/Logics/Modal/CslibTranslation.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/CslibTranslation.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#to-model-of-model).

## Translation of modal formulas into CSLib propositions

Each modal formula built from
atoms, $\bot$, $\to$ and $\Box$ is translated into a CSLib unimodal proposition by recursion:
an atom $p$ goes to the atom $p$, $\bot$ goes to false, $\varphi \to \psi$ goes to
$\neg\varphi' \lor \psi'$, and $\Box\varphi$ goes to $\neg\Diamond\neg\varphi'$, where
$\varphi'$ and $\psi'$ are the translations of $\varphi$ and $\psi$ and $\Diamond$ is the
possibility operator of CSLib's unimodal language.

Formalized by `Cslib.Modal.Formula.toProposition`, a definition declared in [CSLibExt/Logics/Modal/CslibTranslation.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/CslibTranslation.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#to-proposition).

## The reverse translation preserves satisfaction

Let $k$ be a Kripke model, $w$ a world
and $\varphi$ a modal formula in the $\bot$, $\to$, $\Box$ basis. Then $\varphi$ holds at $w$ in $k$
if and only if its translation into a CSLib unimodal proposition holds at $w$ in the CSLib model
associated with $k$.

Together with the preservation of satisfaction by the forward translation and the two model round
trips, this shows that the two presentations have the same unimodal semantics.

Formalized by `Cslib.Modal.satisfies_toProposition`, a theorem declared in [CSLibExt/Logics/Modal/CslibTranslation.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/CslibTranslation.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#satisfies-to-proposition).

## Validity agrees with its CSLib translation

A modal formula $\varphi$ is
valid in a Kripke model $k$ (true at every world of $k$) if and only if its translation into a
CSLib unimodal proposition is satisfied at every world of the CSLib unimodal model associated
with $k$.

Formalized by `Cslib.Modal.KripkeModel.valid_toProposition`, a theorem declared in [CSLibExt/Logics/Modal/CslibTranslation.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/CslibTranslation.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#valid-to-proposition).

## Validity of the translation gives membership in CSLib's logic

Let $S$ be a class of CSLib
unimodal models on a type of worlds and $\varphi$ a CSLib unimodal proposition. Suppose that, if
the type of worlds is nonempty, the translation of $\varphi$ into the $\bot$, $\to$, $\Box$ basis is
valid in the Kripke model of every model in $S$. Then $\varphi$ belongs to CSLib's semantic logic
of $S$: it holds at every world of every model in $S$.

Formalized by `Cslib.Modal.mem_logic_of_valid`, a theorem declared in [CSLibExt/Logics/Modal/CslibTranslation.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/CslibTranslation.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#mem-logic-of-valid).

## Soundness for CSLib's K

Let $\varphi$ be a CSLib unimodal proposition. If the translation
of $\varphi$ into the $\bot$, $\to$, $\Box$ basis is a theorem of the Hilbert system K, then, for
every type of worlds, $\varphi$ belongs to CSLib's modal logic K: it holds at every world of every
CSLib unimodal model on that type.

Formalized by `Cslib.Modal.Derivable.mem_K`, a theorem declared in [CSLibExt/Logics/Modal/CslibTranslation.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/CslibTranslation.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#mem-k).

## Soundness for CSLib's T

Let $\varphi$ be a CSLib unimodal proposition. If the translation
of $\varphi$ into the $\bot$, $\to$, $\Box$ basis is a theorem of the Hilbert system T, then, for
every type of worlds, $\varphi$ belongs to CSLib's modal logic T: it holds at every world of every
CSLib unimodal model on that type whose accessibility relation is reflexive.

Formalized by `Cslib.Modal.Derivable.mem_T`, a theorem declared in [CSLibExt/Logics/Modal/CslibTranslation.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/CslibTranslation.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#mem-t).

## Soundness for CSLib's S4

Let $\varphi$ be a CSLib unimodal proposition. If the translation
of $\varphi$ into the $\bot$, $\to$, $\Box$ basis is a theorem of the Hilbert system S4, then, for
every type of worlds, $\varphi$ belongs to CSLib's modal logic S4: it holds at every world of every
CSLib unimodal model on that type whose accessibility relation is reflexive and transitive.

Formalized by `Cslib.Modal.Derivable.mem_S4`, a theorem declared in [CSLibExt/Logics/Modal/CslibTranslation.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/CslibTranslation.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#mem-s4).

## Soundness for CSLib's S5

Let $\varphi$ be a CSLib unimodal proposition. If the translation
of $\varphi$ into the $\bot$, $\to$, $\Box$ basis is a theorem of the Hilbert system S5, then, for
every type of worlds, $\varphi$ belongs to CSLib's modal logic S5: it holds at every world of every
CSLib unimodal model on that type whose accessibility relation $R$ is reflexive, transitive and
Euclidean ($R(w, u)$ and $R(w, v)$ imply $R(u, v)$).

Formalized by `Cslib.Modal.Derivable.mem_S5`, a theorem declared in [CSLibExt/Logics/Modal/CslibTranslation.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/CslibTranslation.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#mem-s5).

## Consistency relative to a normal modal logic

For sets of formulas $\Lambda$ and
$\Gamma$, the set $\Gamma$ is consistent relative to $K \oplus \Lambda$ when $\bot$ is not
deducible from $\Gamma$ in $K \oplus \Lambda$.

Formalized by `Cslib.Modal.Consistent`, a definition declared in [CSLibExt/Logics/Modal/Canonical.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#consistent).

## Consistency is of finite character

For every set $\Lambda$ of extra axioms, a set of
formulas is consistent relative to $K \oplus \Lambda$ iff all its finite subsets are.

Formalized by `Cslib.Modal.consistent_isOfFiniteCharacter`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#consistent-is-of-finite-character).

## Lindenbaum's lemma for normal modal logics

Let $\Lambda$ be a set of modal formulas and
$\mathrm{K} \oplus \Lambda$ the normal modal logic K extended by the axioms $\Lambda$. Every set
$\Gamma$ of modal formulas that is consistent relative to $\mathrm{K} \oplus \Lambda$ is contained
in a set $M$ of modal formulas that is maximal among the sets consistent relative to
$\mathrm{K} \oplus \Lambda$.

The proof applies the Teichmüller–Tukey lemma: consistency is a property of finite character.

Formalized by `Cslib.Modal.exists_maximal_consistent`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#exists-maximal-consistent).

## Maximal consistent sets of modal formulas are deductively closed

Let $\Lambda$ be a set
of modal formulas and $M$ a set of modal formulas that is maximal among the sets consistent
relative to the normal modal logic K extended by the axioms $\Lambda$. Every formula that is a
local consequence of $M$ in that logic belongs to $M$.

Formalized by `Cslib.Modal.MaximalConsistent.mem_of_deduces`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#mem-of-deduces).

## Iterated modus ponens in maximal consistent sets

Let $\Lambda$ be a set of modal
formulas, $M$ a set of modal formulas that is maximal among the sets consistent relative to the
normal modal logic K extended by the axioms $\Lambda$, and $\varphi$ and $\gamma_1, \dots, \gamma_n$
modal formulas. If $\gamma_1 \to (\gamma_2 \to \cdots \to (\gamma_n \to \varphi) \cdots) \in M$
and $\gamma_1, \dots, \gamma_n \in M$, then $\varphi \in M$.

Formalized by `Cslib.Modal.MaximalConsistent.mem_of_foldr_imp_mem`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#mem-of-foldr-imp-mem).

## Discharging a list of hypotheses

Let $\Lambda$ and $\Gamma$ be sets of modal formulas,
$\varphi$ a modal formula and $\gamma_1, \dots, \gamma_n$ a list of modal formulas. If $\varphi$
is a local consequence of $\Gamma \cup \{\gamma_1, \dots, \gamma_n\}$ in the normal modal logic K
extended by the axioms $\Lambda$, then
$\gamma_1 \to (\gamma_2 \to \cdots \to (\gamma_n \to \varphi) \cdots)$ is a local consequence of
$\Gamma$ in the same logic.

Formalized by `Cslib.Modal.Deduces.foldr_imp`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#foldr-imp).

## Boxing an implication chain

Let $\Lambda$ be a set of extra axioms, let
$\gamma_1, \dots, \gamma_n$ be formulas (with $n \ge 0$) and let $\varphi$ be a formula. Then
$\Box(\gamma_1 \to \cdots \to \gamma_n \to \varphi) \to
(\Box\gamma_1 \to \cdots \to \Box\gamma_n \to \Box\varphi)$
is a theorem of $K \oplus \Lambda$.

Formalized by `Cslib.Modal.Derivable.box_foldr_imp`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#box-foldr-imp).

## Worlds of the canonical model

For a set $\Lambda$ of extra axioms, the worlds of the
canonical model of $K \oplus \Lambda$ are the maximal consistent sets of $K \oplus \Lambda$: the
sets of formulas that are consistent relative to $K \oplus \Lambda$ and have no consistent proper
superset.

Formalized by `Cslib.Modal.CanonicalWorld`, a definition declared in [CSLibExt/Logics/Modal/Canonical.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#canonical-world).

## The canonical accessibility relation

For a set $\Lambda$ of modal formulas and maximal
$(K \oplus \Lambda)$-consistent sets $M$ and $N$ (worlds of the canonical model), $M$ is related to
$N$ iff every formula $\varphi$ with $\Box\varphi \in M$ belongs to $N$.

Formalized by `Cslib.Modal.CanonicalWorld.rel`, a definition declared in [CSLibExt/Logics/Modal/Canonical.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#rel).

## The canonical model

Let $\Lambda$ be a set of extra axioms such that $\bot$ is not a
theorem of $K \oplus \Lambda$. The canonical model of $K \oplus \Lambda$ is the Kripke model
whose worlds are the maximal consistent sets of $K \oplus \Lambda$ (there is at least one, by
Lindenbaum's lemma), in which $M$ sees $N$ iff $\varphi \in N$ for every formula $\varphi$
with $\Box\varphi \in M$, and in which an atom $p$ is true at $M$ iff $p \in M$.

Formalized by `Cslib.Modal.canonicalModel`, a definition declared in [CSLibExt/Logics/Modal/Canonical.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#canonical-model).

## Existence lemma

Let $\Lambda$ be a set of modal formulas, $\mathrm{K} \oplus \Lambda$ the
normal modal logic K extended by the axioms $\Lambda$, $M$ a canonical world, that is, a set of
modal formulas maximal among the sets consistent relative to $\mathrm{K} \oplus \Lambda$, and
$\varphi$ a modal formula. If $\Box\varphi \notin M$, then there is a canonical world $N$ with
$\varphi \notin N$ that is accessible from $M$ in the canonical relation: every $\psi$ with
$\Box\psi \in M$ lies in $N$.

Formalized by `Cslib.Modal.CanonicalWorld.exists_rel_not_mem`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#exists-rel-not-mem).

## Truth lemma

A formula holds at a world of the canonical model iff it belongs to it.

Formalized by `Cslib.Modal.satisfies_canonical_iff`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#satisfies-canonical-iff).

## Deducibility from maximal consistent extensions

Let $\Lambda$ and $\Gamma$ be sets of modal
formulas and $\varphi$ a formula. If $\varphi$ belongs to every maximal
$(K \oplus \Lambda)$-consistent set that contains $\Gamma$, then $\Gamma$ deduces $\varphi$ in
$K \oplus \Lambda$.

Formalized by `Cslib.Modal.Deduces.of_canonical`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#of-canonical).

## Completeness relative to the canonical model

Let $\Lambda$ be a set of modal formulas
such that $\bot$ is not a theorem of $K \oplus \Lambda$, let $\Gamma$ be a set of formulas and
$\varphi$ a formula. If $\varphi$ holds at every world of the canonical model of $K \oplus \Lambda$
at which every formula of $\Gamma$ holds, then $\Gamma$ deduces $\varphi$ in $K \oplus \Lambda$.

Formalized by `Cslib.Modal.Deduces.of_canonicalModel`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#of-canonical-model).

## Double-negation introduction under a box

For every set $\Lambda$ of extra axioms and every
modal formula $\psi$, the formula $\Box\psi \to \Box\neg\neg\psi$ is a theorem of the normal modal
logic $K \oplus \Lambda$, where $\neg\chi$ abbreviates $\chi \to \bot$.

Formalized by `Cslib.Modal.CanonicalWorld.derivable_box_imp_box_neg_neg`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#derivable-box-imp-box-neg-neg).

## Local semantic consequence over a class of Kripke models

Let $C$ be a class of Kripke
models, given as a predicate on models. A set $\Gamma$ of modal formulas locally entails a formula
$\varphi$ over $C$ when, for every Kripke model $M$ in $C$ whose type of worlds lies in the
universe of the atoms and every world $w$ of $M$, if every formula of $\Gamma$ is satisfied at $w$
in $M$, then $\varphi$ is satisfied at $w$ in $M$.

Formalized by `Cslib.Modal.LocallyEntails`, a definition declared in [CSLibExt/Logics/Modal/Canonical.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#locally-entails).

## Strong completeness of K

Let $\Gamma$ be a set of formulas and $\varphi$ a formula.
Suppose that for every Kripke model whose worlds form a type in the universe of the atoms, and
every world $w$ of it at which all formulas of $\Gamma$ hold, $\varphi$ holds at $w$. Then
$\varphi$ is deducible from $\Gamma$ in K.

Formalized by `Cslib.Modal.completeness_K`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#completeness-k).

## Strong completeness of T

Let $\Gamma$ be a set of formulas and $\varphi$ a formula.
Suppose that for every Kripke model with reflexive accessibility relation whose worlds form a
type in the universe of the atoms, and every world $w$ of it at which all formulas of $\Gamma$
hold, $\varphi$ holds at $w$. Then $\varphi$ is deducible from $\Gamma$ in T.

Formalized by `Cslib.Modal.completeness_T`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#completeness-t).

## Strong completeness of S4

Let $\Gamma$ be a set of formulas and $\varphi$ a formula.
Suppose that for every Kripke model with reflexive and transitive accessibility relation whose
worlds form a type in the universe of the atoms, and every world $w$ of it at which all formulas
of $\Gamma$ hold, $\varphi$ holds at $w$. Then $\varphi$ is deducible from $\Gamma$ in S4.

Formalized by `Cslib.Modal.completeness_S4`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#completeness-s4).

## Strong completeness of S5

Let $\Gamma$ be a set of formulas and $\varphi$ a formula.
Suppose that for every Kripke model whose accessibility relation is an equivalence relation and
whose worlds form a type in the universe of the atoms, and every world $w$ of it at which all
formulas of $\Gamma$ hold, $\varphi$ holds at $w$. Then $\varphi$ is deducible from $\Gamma$ in
S5.

Formalized by `Cslib.Modal.completeness_S5`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#completeness-s5).

## Soundness and completeness of K

A modal formula $\varphi$ is a theorem of K if and only if
$\varphi$ is valid, that is, true at every world, in every Kripke model whose worlds live in the
universe of the atoms.

Formalized by `Cslib.Modal.derivable_K_iff`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#derivable-k-iff).

## Soundness and completeness of T

A modal formula $\varphi$ is a theorem of T if and only
if $\varphi$ is valid in every Kripke model whose accessibility relation is reflexive and whose
type of worlds lies in the same universe as the type of atoms.

Formalized by `Cslib.Modal.derivable_T_iff`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#derivable-t-iff).

## Soundness and completeness of S4

A modal formula $\varphi$ is a theorem of S4 if and only
if $\varphi$ is valid in every Kripke model whose accessibility relation is reflexive and
transitive and whose type of worlds lies in the same universe as the type of atoms.

Formalized by `Cslib.Modal.derivable_S4_iff`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#derivable-s4-iff).

## Soundness and completeness of S5

A modal formula $\varphi$ is a theorem of S5 if and only
if $\varphi$ is valid in every Kripke model whose accessibility relation is an equivalence
relation and whose type of worlds lies in the same universe as the type of atoms.

Formalized by `Cslib.Modal.derivable_S5_iff`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#derivable-s5-iff).

## Model existence from the canonical model

Let $\Lambda$ be a set of modal formulas and $C$
a class of Kripke models whose worlds lie in the universe of the atoms, such that $C$ contains the
canonical model of $K \oplus \Lambda$ whenever $\bot$ is not a theorem of $K \oplus \Lambda$. Then
every $(K \oplus \Lambda)$-consistent set $\Gamma$ of formulas is satisfiable in $C$: some model in
$C$ has a world at which every formula of $\Gamma$ holds.

This is strong completeness in satisfiability form. The converse needs every model in $C$ to
validate $\Lambda$; for K, T, S4 and S5 it is soundness.

Formalized by `Cslib.Modal.satisfiable_of_consistent`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#satisfiable-of-consistent).

## Model existence for K

For every K-consistent set $\Gamma$ of modal formulas there are a
Kripke model, whose worlds lie in the universe of the atoms, and a world of it at which every
formula of $\Gamma$ holds.

Formalized by `Cslib.Modal.satisfiable_K`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#satisfiable-k).

## Model existence for T

For every T-consistent set $\Gamma$ of modal formulas there are a
reflexive Kripke model, whose worlds lie in the universe of the atoms, and a world of it at which
every formula of $\Gamma$ holds.

Formalized by `Cslib.Modal.satisfiable_T`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#satisfiable-t).

## Model existence for S4

For every S4-consistent set $\Gamma$ of modal formulas there are a
reflexive transitive Kripke model, whose worlds lie in the universe of the atoms, and a world of it
at which every formula of $\Gamma$ holds.

Formalized by `Cslib.Modal.satisfiable_S4`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#satisfiable-s4).

## Model existence for S5

For every S5-consistent set $\Gamma$ of modal formulas there are a
Kripke model whose accessibility relation is an equivalence and whose worlds lie in the universe
of the atoms, and a world of it at which every formula of $\Gamma$ holds.

Formalized by `Cslib.Modal.satisfiable_S5`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#satisfiable-s5).

## Strong soundness and completeness of K

For every set $\Gamma$ of modal formulas and every
modal formula $\varphi$, $\varphi$ is a local consequence of $\Gamma$ in K if and only if $\Gamma$
locally entails $\varphi$ over all Kripke models: $\varphi$ holds at every world of every Kripke
model, with worlds in the universe of the atoms, at which every formula of $\Gamma$ holds.

Formalized by `Cslib.Modal.deduces_K_iff`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 389](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L389). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#deduces-k-iff).

## Strong soundness and completeness of T

For every set $\Gamma$ of modal formulas and every
modal formula $\varphi$, $\varphi$ is a local consequence of $\Gamma$ in T if and only if $\Gamma$
locally entails $\varphi$ over reflexive Kripke models: $\varphi$ holds at every world of every
Kripke model with reflexive accessibility relation, with worlds in the universe of the atoms, at
which every formula of $\Gamma$ holds.

Formalized by `Cslib.Modal.deduces_T_iff`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#deduces-t-iff).

## Strong soundness and completeness of S4

For every set $\Gamma$ of modal formulas and every
modal formula $\varphi$, $\varphi$ is a local consequence of $\Gamma$ in S4 if and only if $\Gamma$
locally entails $\varphi$ over reflexive transitive Kripke models: $\varphi$ holds at every world of
every Kripke model with reflexive and transitive accessibility relation, with worlds in the
universe of the atoms, at which every formula of $\Gamma$ holds.

Formalized by `Cslib.Modal.deduces_S4_iff`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#deduces-s4-iff).

## Strong soundness and completeness of S5

For every set $\Gamma$ of modal formulas and every
modal formula $\varphi$, $\varphi$ is a local consequence of $\Gamma$ in S5 if and only if $\Gamma$
locally entails $\varphi$ over Kripke models whose accessibility relation is an equivalence
relation: $\varphi$ holds at every world of every such Kripke model, with worlds in the universe of
the atoms, at which every formula of $\Gamma$ holds.

Formalized by `Cslib.Modal.deduces_S5_iff`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#deduces-s5-iff).

## The canonical model as a CSLib model

For a set $\Lambda$ of extra axioms, this is the
unimodal model of CSLib's modal semantics whose worlds are the maximal consistent sets of
$K \oplus \Lambda$, in which $M$ sees $N$ iff $\varphi \in N$ for every formula $\varphi$ with
$\Box\varphi \in M$, and in which an atom $p$ is true at $M$ iff $p \in M$.

No consistency hypothesis on $K \oplus \Lambda$ is needed here, since a CSLib model may have no
worlds.

Formalized by `Cslib.Modal.canonicalCslibModel`, a definition declared in [CSLibExt/Logics/Modal/Canonical.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#canonical-cslib-model).

## Validity in a class containing the canonical model gives derivability

Let $\Lambda$ be a
set of extra axioms, and let $S$ be a set of CSLib unimodal models whose worlds are the maximal
consistent sets of $K \oplus \Lambda$. If $S$ contains the canonical model of $K \oplus \Lambda$,
viewed as a CSLib model, and a CSLib proposition $\varphi$ holds at every world of every model in
$S$, then the translation of $\varphi$ into the $\bot$, $\to$, $\Box$ basis is a theorem of
$K \oplus \Lambda$.

Formalized by `Cslib.Modal.derivable_ofProposition_of_mem_logic`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#derivable-of-proposition-of-mem-logic).

## Completeness for CSLib's K

Let $\varphi$ be a proposition of CSLib's unimodal language over
a type of atoms $A$. Then the translation of $\varphi$ into the $\bot$, $\to$, $\Box$ basis is a
theorem of K if and only if, for every type of worlds $W$ in the universe of $A$, $\varphi$ belongs
to CSLib's semantic logic K over $W$ and $A$, that is, $\varphi$ holds at every world of every CSLib
model with worlds $W$.

Formalized by `Cslib.Modal.derivable_ofProposition_K_iff`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 449](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L449). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#derivable-of-proposition-k-iff).

## Completeness for CSLib's T

For a CSLib unimodal proposition $\varphi$, the translation
of $\varphi$ into the $\bot$, $\to$, $\Box$ basis is a theorem of the Hilbert system T if and only
if, for every type of worlds in the universe of the atoms, $\varphi$ belongs to CSLib's modal logic
T over that type, that is, $\varphi$ holds at every world of every CSLib model on that type whose
accessibility relation is reflexive.

Formalized by `Cslib.Modal.derivable_ofProposition_T_iff`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 456](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L456). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#derivable-of-proposition-t-iff).

## Completeness for CSLib's S4

Let $\varphi$ be a proposition of CSLib's unimodal language
over a type of atoms $A$. Then the translation of $\varphi$ into the $\bot$, $\to$, $\Box$ basis is
a theorem of S4 if and only if, for every type of worlds $W$ in the universe of $A$, $\varphi$
belongs to CSLib's semantic logic S4 over $W$ and $A$, that is, $\varphi$ holds at every world of
every CSLib model with worlds $W$ whose accessibility relation is reflexive and transitive.

Formalized by `Cslib.Modal.derivable_ofProposition_S4_iff`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 463](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#derivable-of-proposition-s4-iff).

## Completeness for CSLib's S5

Let $\varphi$ be a proposition of CSLib's unimodal language
over a type of atoms $A$. Then the translation of $\varphi$ into the $\bot$, $\to$, $\Box$ basis is
a theorem of S5 if and only if, for every type of worlds $W$ in the universe of $A$, $\varphi$
belongs to CSLib's semantic logic S5 over $W$ and $A$, that is, $\varphi$ holds at every world of
every CSLib model with worlds $W$ whose accessibility relation $R$ is reflexive, transitive and
right Euclidean ($w R u$ and $w R v$ imply $u R v$).

Formalized by `Cslib.Modal.derivable_ofProposition_S5_iff`, a theorem declared in [CSLibExt/Logics/Modal/Canonical.lean, line 471](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Canonical.lean#L471). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html#derivable-of-proposition-s5-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Soundness and completeness of normal modal logics](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/modal-logic/soundness-and-completeness-of-normal-modal-logic)
