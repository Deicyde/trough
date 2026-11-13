---
declaration: section
origin: cited
lean: Cslib.Logic.FOL.Derivable, Cslib.Logic.FOL.Derivable.sound, Cslib.Logic.FOL.Derivable.rename, Cslib.Logic.FOL.Derivable.relabel, Cslib.Logic.FOL.Derivable.mono, Cslib.Logic.FOL.Derivable.cut, Cslib.Logic.FOL.Derivable.exI, Cslib.Logic.FOL.Derivable.symm
statement: formalized
proof: formalized
---

# First-order natural deduction

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-natural-deduction/index.html).

## Natural deduction

Fix a first-order language $L$ and a type $\alpha$ of variables;
formulas and terms below are those of $L$ with free variables in $\alpha$. For a formula
$\varphi$ with one additional bound variable and a term $t$, write $\varphi[t]$ for $\varphi$
with $t$ substituted for that bound variable and $\forall \varphi$ for its universal
quantification. Write $\neg \psi$ for $\psi \to \bot$, and $\psi, \Gamma$ for the list $\Gamma$
with $\psi$ added in front. Derivability $\Gamma \vdash \varphi$ of a formula $\varphi$ (the
conclusion) from a finite list $\Gamma$ of formulas (the open hypotheses) is the least relation
closed under the following rules.

* Assumption: $\Gamma \vdash \varphi$ whenever $\varphi$ is a member of $\Gamma$.
* Implication introduction: from $\varphi, \Gamma \vdash \psi$ infer
  $\Gamma \vdash \varphi \to \psi$.
* Implication elimination: from $\Gamma \vdash \varphi \to \psi$ and $\Gamma \vdash \varphi$
  infer $\Gamma \vdash \psi$.
* Reductio ad absurdum: from $\neg \varphi, \Gamma \vdash \bot$ infer $\Gamma \vdash \varphi$.
* Universal introduction: if a variable $x$ occurs free in no member of $\Gamma$ and does not
  occur free in $\varphi$, then from $\Gamma \vdash \varphi[x]$ infer
  $\Gamma \vdash \forall \varphi$.
* Universal elimination: from $\Gamma \vdash \forall \varphi$ infer $\Gamma \vdash \varphi[t]$,
  for every term $t$.
* Reflexivity: $\Gamma \vdash t = t$ for every term $t$.
* Substitution: from $\Gamma \vdash s = t$ and $\Gamma \vdash \varphi[s]$ infer
  $\Gamma \vdash \varphi[t]$.

Formalized by `Cslib.Logic.FOL.Derivable`, an inductive type declared in [CSLibExt/Logics/FirstOrder/NaturalDeduction.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/FirstOrder/NaturalDeduction.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-natural-deduction/index.html#derivable).

## Soundness of first-order natural deduction

Let $\Gamma$ be a finite list of formulas of
a first-order language $L$ with free variables in $\alpha$, and let $\varphi$ be such a formula.
If $\Gamma \vdash \varphi$ in natural deduction, then for every $L$-structure $M$ and every
assignment $v \colon \alpha \to M$ under which all members of $\Gamma$ hold, $\varphi$ holds
under $v$.

Formalized by `Cslib.Logic.FOL.Derivable.sound`, a theorem declared in [CSLibExt/Logics/FirstOrder/NaturalDeduction.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/FirstOrder/NaturalDeduction.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-natural-deduction/index.html#sound).

## Injective renaming preserves derivability

Let $f \colon \alpha \to \beta$ be an
injective map between types of variables. For a formula $\psi$ of a first-order language $L$
with free variables in $\alpha$, write $f(\psi)$ for the renaming of the free variables of
$\psi$ by $f$, and for a finite list $\Gamma$ of such formulas write $f(\Gamma)$ for the list
obtained by renaming each member of $\Gamma$. If $\Gamma$ is such a list, $\varphi$ is such a
formula and $\Gamma \vdash \varphi$ in natural deduction, then $f(\Gamma) \vdash f(\varphi)$.

On formulas this renaming coincides with Mathlib's relabeling of free variables.

Formalized by `Cslib.Logic.FOL.Derivable.rename`, a theorem declared in [CSLibExt/Logics/FirstOrder/NaturalDeduction.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/FirstOrder/NaturalDeduction.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-natural-deduction/index.html#rename).

## Injective relabeling preserves derivability

Let $f \colon \alpha \to \beta$ be an
injective map between types of variables. For a formula $\psi$ of a first-order language $L$
with free variables in $\alpha$, write $f(\psi)$ for Mathlib's relabeling of $\psi$ by $f$,
which replaces each free variable $x$ by $f(x)$, and for a finite list $\Gamma$ of such formulas
write $f(\Gamma)$ for the list obtained by applying this to each member of $\Gamma$. If $\Gamma$
is such a list, $\varphi$ is such a formula and $\Gamma \vdash \varphi$ in natural deduction,
then $f(\Gamma) \vdash f(\varphi)$.

Formalized by `Cslib.Logic.FOL.Derivable.relabel`, a theorem declared in [CSLibExt/Logics/FirstOrder/NaturalDeduction.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/FirstOrder/NaturalDeduction.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-natural-deduction/index.html#relabel).

## Weakening

Let $\alpha$ be an infinite type of variables, let $\Gamma$ and $\Delta$ be
finite lists of formulas of a first-order language $L$ with free variables in $\alpha$ such that
every member of $\Gamma$ is a member of $\Delta$, and let $\varphi$ be such a formula. If
$\Gamma \vdash \varphi$ in natural deduction, then $\Delta \vdash \varphi$.

Formalized by `Cslib.Logic.FOL.Derivable.mono`, a theorem declared in [CSLibExt/Logics/FirstOrder/NaturalDeduction.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/FirstOrder/NaturalDeduction.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-natural-deduction/index.html#mono).

## Cut

Let $\Gamma$ be a finite list of formulas of a first-order language $L$ with free
variables in $\alpha$, let $\varphi$ and $\psi$ be such formulas, and write $\varphi, \Gamma$ for
the list $\Gamma$ with $\varphi$ added in front. If $\Gamma \vdash \varphi$ and
$\varphi, \Gamma \vdash \psi$ in natural deduction, then $\Gamma \vdash \psi$.

Formalized by `Cslib.Logic.FOL.Derivable.cut`, a theorem declared in [CSLibExt/Logics/FirstOrder/NaturalDeduction.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/FirstOrder/NaturalDeduction.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-natural-deduction/index.html#cut).

## Existential introduction

Let $\Gamma$ be a finite list of formulas of a first-order
language $L$ with free variables in $\alpha$, let $\varphi$ be such a formula with one
additional bound variable, let $t$ be a term, and write $\varphi[t]$ for $\varphi$ with $t$
substituted for that bound variable. If $\Gamma \vdash \varphi[t]$ in natural deduction, then
$\Gamma \vdash \exists \varphi$, where $\exists \varphi$ abbreviates $\neg \forall \neg \varphi$
as in Mathlib.

Formalized by `Cslib.Logic.FOL.Derivable.exI`, a theorem declared in [CSLibExt/Logics/FirstOrder/NaturalDeduction.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/FirstOrder/NaturalDeduction.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-natural-deduction/index.html#ex-i).

## Symmetry of equality in natural deduction

Let $\Gamma$ be a list of first-order formulas
and let $s$ and $t$ be terms. If the equation $s = t$ is derivable from the hypotheses $\Gamma$,
then the equation $t = s$ is derivable from $\Gamma$.

Formalized by `Cslib.Logic.FOL.Derivable.symm`, a theorem declared in [CSLibExt/Logics/FirstOrder/NaturalDeduction.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/FirstOrder/NaturalDeduction.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-natural-deduction/index.html#symm).

## Transitivity of equality in natural deduction

Let $\Gamma$ be a list of first-order
formulas and let $r$, $s$ and $t$ be terms. If the equations $r = s$ and $s = t$ are both
derivable from the hypotheses $\Gamma$, then the equation $r = t$ is derivable from $\Gamma$.

Formalized by `Cslib.Logic.FOL.Derivable.trans`, a theorem declared in [CSLibExt/Logics/FirstOrder/NaturalDeduction.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/FirstOrder/NaturalDeduction.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-natural-deduction/index.html#trans).

## Provability from a set of formulas

A set $T$ of formulas of a first-order language $L$
with free variables in $\alpha$ proves such a formula $\varphi$ when there is a finite list
$\Gamma$ of members of $T$ with $\Gamma \vdash \varphi$ in natural deduction.

Formalized by `Cslib.Logic.FOL.Provable`, a definition declared in [CSLibExt/Logics/FirstOrder/NaturalDeduction.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/FirstOrder/NaturalDeduction.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-natural-deduction/index.html#provable).

## Soundness for theories

Let $T$ be a theory, that is, a set of sentences of a
first-order language $L$, and regard each sentence of $T$ as a formula with free variables in
$\alpha$. If a formula $\varphi$ with free variables in $\alpha$ is provable from these
formulas, then $\varphi$ holds in every model of $T$ under every assignment of elements of the
model to the variables in $\alpha$.

Formalized by `Cslib.Logic.FOL.Provable.models`, a theorem declared in [CSLibExt/Logics/FirstOrder/NaturalDeduction.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/FirstOrder/NaturalDeduction.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-natural-deduction/index.html#models).

## Consistency of the calculus

The empty context does not derive `⊥`.

Formalized by `Cslib.Logic.FOL.not_derivable_nil_bot`, a theorem declared in [CSLibExt/Logics/FirstOrder/NaturalDeduction.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/FirstOrder/NaturalDeduction.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-natural-deduction/index.html#not-derivable-nil-bot).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: First-order natural deduction](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-natural-deduction/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/first-order-logic/first-order-natural-deduction)
