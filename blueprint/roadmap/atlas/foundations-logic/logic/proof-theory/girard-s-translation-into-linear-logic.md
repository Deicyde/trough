---
declaration: section
origin: cited
lean: Cslib.Logic.CLL.Sequent.allQuest_cons_quest, Cslib.Logic.CLL.Girard.translate, Cslib.Logic.CLL.Girard.translate_imp, Cslib.Logic.CLL.Girard.hyp, Cslib.Logic.CLL.Girard.hyps, Cslib.Logic.CLL.Girard.weaken_hyps, Cslib.Logic.CLL.Girard.contract_hyps, Cslib.Logic.CLL.Girard.bang_hyps
statement: formalized
proof: formalized
---

# Girard's translation into linear logic

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/girard-s-translation-into-linear-logic/index.html).

## Adding a why-not proposition keeps a sequent all why-not

For every CLL proposition $a$
and every CLL sequent $\Delta$, every proposition of the sequent $?a, \Delta$ has the form $?b$
for some $b$ if and only if every proposition of $\Delta$ does.

Formalized by `Cslib.Logic.CLL.Sequent.allQuest_cons_quest`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/girard-s-translation-into-linear-logic/index.html#all-quest-cons-quest).

## Girard's translation

Given a map $f$ from propositional atoms to CLL propositions, the
translation $A \mapsto A^\circ$ of propositional formulas into CLL is defined by recursion:
$a^\circ = f(a)$ for an atom $a$, $(A \wedge B)^\circ = A^\circ \mathbin{\&} B^\circ$,
$(A \vee B)^\circ = {!A^\circ} \oplus {!B^\circ}$, and $(A \to B)^\circ$ is the multiplicative
disjunction (par) of $?\big((A^\circ)^\perp\big)$ and $B^\circ$, that is, the linear implication
${!A^\circ} \multimap B^\circ$.

Formalized by `Cslib.Logic.CLL.Girard.translate`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/girard-s-translation-into-linear-logic/index.html#translate).

## Girard's translation of an implication

For every map $f$ from propositional atoms to CLL
propositions and all propositional formulas $A$ and $B$, $(A \to B)^\circ = {!A^\circ} \multimap
B^\circ$, where $C^\circ$ denotes Girard's translation of a formula $C$ with atoms translated by
$f$ and $\multimap$ is linear implication in CLL.

Formalized by `Cslib.Logic.CLL.Girard.translate_imp`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/girard-s-translation-into-linear-logic/index.html#translate-imp).

## Girard's translation of a reusable hypothesis

Given a map $f$ from atoms to CLL
propositions and a propositional formula $A$, this is the CLL proposition $?((A^\circ)^\perp)$,
where $A^\circ$ is Girard's translation of $A$ with atoms translated by $f$ and $(\cdot)^\perp$
is linear negation.

Formalized by `Cslib.Logic.CLL.Girard.hyp`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/girard-s-translation-into-linear-logic/index.html#hyp).

## Translated hypotheses of a context

Given a map $f$ from propositional atoms to CLL
propositions and a multiset $\Gamma$ of propositional formulas, $?\Gamma^{\circ\perp}$ is the CLL
sequent consisting of the propositions $?\big((A^\circ)^\perp\big)$ for $A \in \Gamma$, counted
with multiplicity, where $A^\circ$ is Girard's translation of $A$ with atoms translated by $f$.

Formalized by `Cslib.Logic.CLL.Girard.hyps`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/girard-s-translation-into-linear-logic/index.html#hyps).

## Weakening by translated hypotheses

Let $f$ map propositional atoms to CLL propositions.
If a CLL sequent $\vdash \Delta$ is provable, then for every multiset $\Gamma$ of propositional
formulas the sequent $\vdash ?\Gamma^{\circ\perp}, \Delta$ is provable, where $?\Gamma^{\circ\perp}$
is the multiset of the propositions $?\big((A^\circ)^\perp\big)$ for $A \in \Gamma$ and $A^\circ$
is Girard's translation of $A$ with atoms translated by $f$.

Formalized by `Cslib.Logic.CLL.Girard.weaken_hyps`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/girard-s-translation-into-linear-logic/index.html#weaken-hyps).

## Contraction of a translated hypothesis context

Let $f$ map atoms to CLL propositions,
let $\Gamma$ be a multiset of propositional formulas, and write $?\Gamma^{\circ\perp}$ for the
CLL sequent of the propositions $?((B^\circ)^\perp)$, one for each $B \in \Gamma$ counted with
multiplicity, where $B^\circ$ is Girard's translation of $B$ with atoms translated by $f$. For
every CLL sequent $\Delta$, if $\vdash ?\Gamma^{\circ\perp}, ?\Gamma^{\circ\perp}, \Delta$ is
provable in CLL, then so is $\vdash ?\Gamma^{\circ\perp}, \Delta$.

Formalized by `Cslib.Logic.CLL.Girard.contract_hyps`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/girard-s-translation-into-linear-logic/index.html#contract-hyps).

## Promotion in a translated hypothesis context

Let $f$ map atoms to CLL propositions, let
$\Gamma$ be a multiset of propositional formulas, and write $?\Gamma^{\circ\perp}$ for the CLL
sequent of the propositions $?((B^\circ)^\perp)$, one for each $B \in \Gamma$ counted with
multiplicity, where $B^\circ$ is Girard's translation of $B$ with atoms translated by $f$. For
every CLL proposition $a$, if the sequent $\vdash a, ?\Gamma^{\circ\perp}$ is provable in CLL,
then so is $\vdash !a, ?\Gamma^{\circ\perp}$.

Formalized by `Cslib.Logic.CLL.Girard.bang_hyps`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/girard-s-translation-into-linear-logic/index.html#bang-hyps).

## Cut of a translated hypothesis context against a closed proof

Let $f$ map atoms to CLL
propositions, let $\Gamma$ be a multiset of propositional formulas, and write
$?\Gamma^{\circ\perp}$ for the CLL sequent of the propositions $?((B^\circ)^\perp)$, one for
each $B \in \Gamma$ counted with multiplicity, where $B^\circ$ is Girard's translation of $B$
with atoms translated by $f$. For all CLL propositions $a$ and $c$, if
$\vdash a, ?\Gamma^{\circ\perp}$ is provable in CLL and there is a CLL proof of
$\vdash a^\perp, c$, then $\vdash c, ?\Gamma^{\circ\perp}$ is provable in CLL.

Formalized by `Cslib.Logic.CLL.Girard.cut_closed`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/girard-s-translation-into-linear-logic/index.html#cut-closed).

## Cut within a translated hypothesis context

Let $f$ map atoms to CLL propositions, let
$\Gamma$ be a multiset of propositional formulas, and write $?\Gamma^{\circ\perp}$ for the CLL
sequent of the propositions $?((B^\circ)^\perp)$, one for each $B \in \Gamma$ counted with
multiplicity, where $B^\circ$ is Girard's translation of $B$ with atoms translated by $f$. For
all CLL propositions $a$ and $c$, if both $\vdash a, ?\Gamma^{\circ\perp}$ and
$\vdash a^\perp, c, ?\Gamma^{\circ\perp}$ are provable in CLL, then so is
$\vdash c, ?\Gamma^{\circ\perp}$.

Formalized by `Cslib.Logic.CLL.Girard.cut_hyps`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/girard-s-translation-into-linear-logic/index.html#cut-hyps).

## Translated hypotheses are provable from their context

Let $f$ map atoms to CLL
propositions, let $\Gamma$ be a multiset of propositional formulas, and write
$?\Gamma^{\circ\perp}$ for the CLL sequent of the propositions $?((B^\circ)^\perp)$, one for
each $B \in \Gamma$ counted with multiplicity, where $B^\circ$ is Girard's translation of $B$
with atoms translated by $f$. For every propositional formula $A \in \Gamma$, the sequent
$\vdash A^\circ, ?\Gamma^{\circ\perp}$ is provable in CLL.

Formalized by `Cslib.Logic.CLL.Girard.hyp_mem`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/girard-s-translation-into-linear-logic/index.html#hyp-mem).

## Separating a new hypothesis in the translation

Let $f$ map propositional atoms to CLL
propositions, let $\Gamma$ be a finite set of propositional formulas, $A$ a propositional formula
and $c$ a CLL proposition. Write $B^\circ$ for Girard's translation of a formula $B$ with atoms
translated by $f$, and $?\Delta^{\circ\perp}$ for the multiset of the propositions
$?\big((B^\circ)^\perp\big)$ for $B \in \Delta$. If the CLL sequent
$\vdash c, ?(\Gamma \cup \{A\})^{\circ\perp}$ is provable, then so is
$\vdash ?\big((A^\circ)^\perp\big), c, ?\Gamma^{\circ\perp}$.

When $A \in \Gamma$ the conclusion follows by weakening.

Formalized by `Cslib.Logic.CLL.Girard.of_insert`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/girard-s-translation-into-linear-logic/index.html#of-insert).

## Girard's translation preserves provability

Let $f$ map atoms to CLL propositions and
write $B^\circ$ for Girard's translation of a propositional formula $B$ with atoms translated by
$f$. Let $T$ be a propositional theory such that the one-formula sequent $\vdash B^\circ$ is
provable in CLL for every $B \in T$. If $\Gamma$ is a finite set of propositional formulas and
$\Gamma \vdash A$ has a natural-deduction derivation (in minimal propositional logic) using the
axioms of $T$, then the CLL sequent $\vdash A^\circ, ?\Gamma^{\circ\perp}$ is provable, where
$?\Gamma^{\circ\perp}$ consists of the propositions $?((B^\circ)^\perp)$, one for each
$B \in \Gamma$.

Formalized by `Cslib.Logic.CLL.Girard.derivable_of_derivation`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/girard-s-translation-into-linear-logic/index.html#derivable-of-derivation).

## Theorems of minimal logic translate to CLL theorems

For every map $f$ from propositional
atoms to CLL propositions, if a propositional formula $A$ is derivable in natural deduction from
the empty context with no axioms (minimal logic), then the one-sided CLL sequent $\vdash A^\circ$
is provable, where $A^\circ$ is Girard's translation of $A$ with atoms translated by $f$.

Formalized by `Cslib.Logic.CLL.Girard.mpl`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/girard-s-translation-into-linear-logic/index.html#mpl).

## The atom map sending $\bot$ to $0$

For a type of atoms with a distinguished atom $\bot$
and decidable equality, this is the map from atoms to CLL propositions that sends $\bot$ to the
additive unit $0$ and every other atom $a$ to the CLL atom $a$.

Formalized by `Cslib.Logic.CLL.Girard.botToZero`, a definition declared in [CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/girard-s-translation-into-linear-logic/index.html#bot-to-zero).

## Ex falso translates to a CLL theorem

Let $f$ map atoms to CLL propositions and send the
atom $\bot$ to the additive unit $0$. Then for every propositional formula $B$, the one-formula
CLL sequent $\vdash (\bot \to B)^\circ$ is provable, where $(\cdot)^\circ$ is Girard's
translation with atoms translated by $f$.

The translation $(\bot \to B)^\circ$ is the par of $?\top$ and $B^\circ$, which is provable by
the $\top$ rule.

Formalized by `Cslib.Logic.CLL.Girard.efq`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/girard-s-translation-into-linear-logic/index.html#efq).

## Theorems of intuitionistic logic translate to CLL theorems

Let $f$ map propositional atoms
to CLL propositions and send the atom $\bot$ to the additive unit $0$. If a propositional formula
$A$ is derivable in natural deduction from the empty context in intuitionistic propositional
logic (no axioms other than ex falso $\bot \to B$ for every formula $B$), then the one-sided CLL
sequent $\vdash A^\circ$ is provable, where $A^\circ$ is Girard's translation of $A$ with atoms
translated by $f$.

Formalized by `Cslib.Logic.CLL.Girard.ipl`, a theorem declared in [CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LinearLogic/CLL/GirardTranslation.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/girard-s-translation-into-linear-logic/index.html#ipl).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Girard's translation into linear logic](https://deicyde.github.io/atlas-lean/roadmap/Logic/proof-theory/girard-s-translation-into-linear-logic/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/proof-theory/girard-s-translation-into-linear-logic)
