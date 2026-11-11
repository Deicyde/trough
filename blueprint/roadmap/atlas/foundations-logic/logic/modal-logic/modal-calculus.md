---
declaration: section
origin: cited
lean: Cslib.Modal.MuCalculus.MuFormula, Cslib.Modal.MuCalculus.MuFormula.neg, Cslib.Modal.MuCalculus.MuFormula.neg_neg, Cslib.Modal.MuCalculus.extendEnv, Cslib.Modal.MuCalculus.sat, Cslib.Modal.MuCalculus.sat_mono_env, Cslib.Modal.MuCalculus.sat_mono_extend, Cslib.Modal.MuCalculus.mu_pre_fixed
statement: formalized
proof: formalized
---

# Modal μ-calculus

43 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html).

## Formulas of the modal μ-calculus

The formulas over a type of atoms are built from
atoms $a$, negated atoms $\neg a$, variables $X_n$ for $n \in \mathbb{N}$ (de Bruijn indices for
the fixed-point binders), $\bot$ and $\top$ by conjunction $\varphi \wedge \psi$, disjunction
$\varphi \vee \psi$, the modalities $\Box\varphi$ and $\Diamond\varphi$, and the fixed-point
binders $\mu\varphi$ and $\nu\varphi$.

There is no negation of arbitrary formulas. Negated atoms are present so that the meta-level
negation, which swaps each connective with its dual, is an involution.

Formalized by `Cslib.Modal.MuCalculus.MuFormula`, an inductive type declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#mu-formula).

## Negation of μ-calculus formulas

The meta-level negation $\neg\varphi$ of a μ-calculus
formula $\varphi$ swaps each connective with its dual. It is defined by recursion: an atom $p$
becomes the negated atom $\overline{p}$ and $\overline{p}$ becomes $p$, each variable $x_n$
stays $x_n$, $\neg\bot = \top$, $\neg\top = \bot$,
$\neg(\varphi \wedge \psi) = \neg\varphi \vee \neg\psi$,
$\neg(\varphi \vee \psi) = \neg\varphi \wedge \neg\psi$, $\neg\Box\varphi = \Diamond\neg\varphi$,
$\neg\Diamond\varphi = \Box\neg\varphi$, $\neg\mu\varphi = \nu\neg\varphi$ and
$\neg\nu\varphi = \mu\neg\varphi$.

Formalized by `Cslib.Modal.MuCalculus.MuFormula.neg`, a definition declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#neg).

## Meta-level negation is an involution

Write $\neg\varphi$ for the meta-level negation of
a μ-calculus formula $\varphi$, which swaps each connective with its dual. For every μ-calculus
formula $\varphi$, negating twice gives back $\varphi$: $\neg\neg\varphi = \varphi$.

Formalized by `Cslib.Modal.MuCalculus.MuFormula.neg_neg`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#neg-neg).

## Extending an environment under a binder

An environment $\rho$ assigns to each variable
index $n \in \mathbb{N}$ a predicate $\rho(n)$ on worlds. Its extension by a predicate $S$ on
worlds is the environment that assigns $S$ to index $0$ and $\rho(n)$ to index $n + 1$.

With de Bruijn indices, variable $1$ inside a binder thus refers to the enclosing binder.

Formalized by `Cslib.Modal.MuCalculus.extendEnv`, a definition declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#extend-env).

## Satisfaction in the modal μ-calculus

Let $M$ be a Kripke model with accessibility
relation $R$ and valuation $V$, and let $\rho$ be an environment assigning a set of worlds to
each variable index $n \in \mathbb{N}$. For a set of worlds $S$, write $\rho[0 \mapsto S]$ for the
environment sending index $0$ to $S$ and index $n + 1$ to $\rho(n)$. The set $[\![\varphi]\!]_\rho$
of worlds satisfying a formula $\varphi$ in $M$ under $\rho$ is defined by recursion on
$\varphi$: an atom $a$ holds at $w$ when $V$ makes $a$ true at $w$, and the negated atom of $a$
when $V$ does not; the variable with index $n$ denotes $\rho(n)$; $\bot$ holds nowhere and $\top$
everywhere; conjunction and disjunction denote intersection and union; $\Box\varphi$ holds at $w$
when $\varphi$ holds at every $v$ with $w \mathrel{R} v$, and $\Diamond\varphi$ when $\varphi$
holds at some such $v$; $\mu\varphi$ holds at $w$ when $w \in S$ for every set of worlds $S$ with
$[\![\varphi]\!]_{\rho[0 \mapsto S]} \subseteq S$; and $\nu\varphi$ holds at $w$ when $w \in S$
for some set of worlds $S$ with $S \subseteq [\![\varphi]\!]_{\rho[0 \mapsto S]}$.

So $\mu\varphi$ is the least pre-fixed point of $S \mapsto [\![\varphi]\!]_{\rho[0 \mapsto S]}$,
stated directly as an infimum over pre-fixed points, and $\nu\varphi$ is the greatest
post-fixed point, stated as a supremum over post-fixed points.

Formalized by `Cslib.Modal.MuCalculus.sat`, a definition declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#sat).

## Satisfaction is monotone in the environment

Let $M$ be a Kripke model and let $\rho$
and $\rho'$ be environments (each assigns a set of worlds of $M$ to every variable $n$) with
$\rho(n) \subseteq \rho'(n)$ for every $n$. Then every μ-calculus formula $\varphi$ holds under
$\rho'$ at every world of $M$ where it holds under $\rho$: enlarging every variable's denotation
can only enlarge a formula's denotation.

Formalized by `Cslib.Modal.MuCalculus.sat_mono_env`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#sat-mono-env).

## Monotonicity in the bound variable

Let $M$ be a Kripke model, $\rho$ an environment
assigning a set of worlds to each variable index $n \in \mathbb{N}$, and $\varphi$ a μ-calculus
formula. For a set of worlds $S$, write $\rho[0 \mapsto S]$ for the environment sending index $0$
to $S$ and index $n + 1$ to $\rho(n)$. If $S_1 \subseteq S_2$ are sets of worlds, then every world
that satisfies $\varphi$ in $M$ under $\rho[0 \mapsto S_1]$ also satisfies $\varphi$ in $M$ under
$\rho[0 \mapsto S_2]$.

Formalized by `Cslib.Modal.MuCalculus.sat_mono_extend`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#sat-mono-extend).

## The least fixed point is a pre-fixed point

Let $M$ be a Kripke model, $\rho$ an
environment and $\varphi$ a μ-calculus formula. Write $\llbracket\psi\rrbracket_\sigma$ for the
set of worlds of $M$ at which $\psi$ holds under the environment $\sigma$, and $\rho[S]$ for the
extension of $\rho$ under a binder by a set of worlds $S$ (variable $0$ denotes $S$ and variable
$n + 1$ denotes $\rho(n)$). For $T = \llbracket\mu\varphi\rrbracket_\rho$, where $\mu\varphi$
binds variable $0$ of $\varphi$, we have $\llbracket\varphi\rrbracket_{\rho[T]} \subseteq T$.

Formalized by `Cslib.Modal.MuCalculus.mu_pre_fixed`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#mu-pre-fixed).

## The least fixed point is contained in its unfolding

For every Kripke model $M$,
environment $\rho$ and μ-calculus formula $\varphi$, every world satisfying $\mu\varphi$ in $\rho$
also satisfies $\varphi$ in the extension of $\rho$ by the set of worlds satisfying $\mu\varphi$
in $\rho$.

Formalized by `Cslib.Modal.MuCalculus.mu_le_fixed`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#mu-le-fixed).

## The μ unfolding

Let $M$ be a Kripke model, $\rho$ an environment assigning a set of
worlds to each variable index $n \in \mathbb{N}$, and $\varphi$ a μ-calculus formula. Let $A$ be
the set of worlds satisfying $\mu\varphi$ in $M$ under $\rho$. Then $A$ is exactly the set of
worlds satisfying $\varphi$ in $M$ under the environment that sends index $0$ to $A$ and index
$n + 1$ to $\rho(n)$.

Formalized by `Cslib.Modal.MuCalculus.sat_mu_unfold`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#sat-mu-unfold).

## The greatest fixed point is a post-fixed point

Let $M$ be a Kripke model, $\rho$ an
environment and $\varphi$ a μ-calculus formula. Write $\llbracket\psi\rrbracket_\sigma$ for the
set of worlds of $M$ at which $\psi$ holds under the environment $\sigma$, and $\rho[S]$ for the
extension of $\rho$ under a binder by a set of worlds $S$ (variable $0$ denotes $S$ and variable
$n + 1$ denotes $\rho(n)$). For $T = \llbracket\nu\varphi\rrbracket_\rho$, where $\nu\varphi$
binds variable $0$ of $\varphi$, we have $T \subseteq \llbracket\varphi\rrbracket_{\rho[T]}$.

Formalized by `Cslib.Modal.MuCalculus.nu_post_fixed`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#nu-post-fixed).

## The greatest fixed point is a pre-fixed point

Let $M$ be a Kripke model, $\rho$ an
environment and $\varphi$ a μ-calculus formula. Write $\llbracket\psi\rrbracket_\sigma$ for the
set of worlds of $M$ at which $\psi$ holds under the environment $\sigma$, and $\rho[S]$ for the
extension of $\rho$ under a binder by a set of worlds $S$ (variable $0$ denotes $S$ and variable
$n + 1$ denotes $\rho(n)$). For $T = \llbracket\nu\varphi\rrbracket_\rho$, where $\nu\varphi$
binds variable $0$ of $\varphi$, we have $\llbracket\varphi\rrbracket_{\rho[T]} \subseteq T$.

Formalized by `Cslib.Modal.MuCalculus.nu_le_post_fixed`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#nu-le-post-fixed).

## The ν unfolding

Let $M$ be a Kripke model, $\rho$ an environment assigning a set of
worlds to each variable index $n \in \mathbb{N}$, and $\varphi$ a μ-calculus formula. Let $A$ be
the set of worlds satisfying $\nu\varphi$ in $M$ under $\rho$. Then $A$ is exactly the set of
worlds satisfying $\varphi$ in $M$ under the environment that sends index $0$ to $A$ and index
$n + 1$ to $\rho(n)$.

Formalized by `Cslib.Modal.MuCalculus.sat_nu_unfold`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#sat-nu-unfold).

## Park induction

Let $M$ be a Kripke model, $\rho$ an environment, $\varphi$ a μ-calculus
formula and $P$ a predicate on worlds. If every world satisfying $\varphi$ in the extension of
$\rho$ by $P$ satisfies $P$, then every world satisfying $\mu\varphi$ in $\rho$ satisfies $P$.

Formalized by `Cslib.Modal.MuCalculus.mu_induction`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#mu-induction).

## Coinduction for the greatest fixed point

Let $M$ be a Kripke model, $\rho$ an
environment, $\varphi$ a μ-calculus formula and $P$ a set of worlds of $M$. Write
$\llbracket\psi\rrbracket_\sigma$ for the set of worlds at which $\psi$ holds under the
environment $\sigma$, and $\rho[P]$ for the extension of $\rho$ under a binder by $P$ (variable
$0$ denotes $P$ and variable $n + 1$ denotes $\rho(n)$). If
$P \subseteq \llbracket\varphi\rrbracket_{\rho[P]}$, then
$P \subseteq \llbracket\nu\varphi\rrbracket_\rho$, where $\nu\varphi$ binds variable $0$ of
$\varphi$: every post-fixed point is below the greatest fixed point.

Formalized by `Cslib.Modal.MuCalculus.nu_coinduction`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#nu-coinduction).

## The fixed-point operator of a formula

Given a Kripke model $M$, an environment $\rho$
(a set of worlds $\rho(n)$ for each variable $n$) and a μ-calculus formula $\varphi$, this is
the monotone map on sets of worlds of $M$ sending $S$ to the set of worlds at which $\varphi$
holds under $\rho[S]$, the extension of $\rho$ under a binder by $S$ (variable $0$ denotes $S$
and variable $n + 1$ denotes $\rho(n)$).

Formalized by `Cslib.Modal.MuCalculus.muOp`, a definition declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#mu-op).

## The μ formula denotes the least fixed point

Let $M$ be a Kripke model, $\rho$ an
environment assigning a set of worlds to each variable index $n \in \mathbb{N}$, and $\varphi$ a
μ-calculus formula. For a set of worlds $S$, write $\rho[0 \mapsto S]$ for the environment sending
index $0$ to $S$ and index $n + 1$ to $\rho(n)$. Then the set of worlds satisfying $\mu\varphi$ in
$M$ under $\rho$ is the least fixed point of the monotone operator on sets of worlds that sends
$S$ to the set of worlds satisfying $\varphi$ in $M$ under $\rho[0 \mapsto S]$.

Formalized by `Cslib.Modal.MuCalculus.sat_mu_eq_lfp`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#sat-mu-eq-lfp).

## The ν formula denotes the greatest fixed point

Let $M$ be a Kripke model, $\rho$ an
environment assigning a set of worlds to each variable index $n \in \mathbb{N}$, and $\varphi$ a
μ-calculus formula. For a set of worlds $S$, write $\rho[0 \mapsto S]$ for the environment sending
index $0$ to $S$ and index $n + 1$ to $\rho(n)$. Then the set of worlds satisfying $\nu\varphi$ in
$M$ under $\rho$ is the greatest fixed point of the monotone operator on sets of worlds that sends
$S$ to the set of worlds satisfying $\varphi$ in $M$ under $\rho[0 \mapsto S]$.

Formalized by `Cslib.Modal.MuCalculus.sat_nu_eq_gfp`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#sat-nu-eq-gfp).

## Complementing an extended environment

For every environment $\rho$ (assigning to each
variable index $n$ a predicate $\rho(n)$ on worlds) and every predicate $S$ on worlds,
complementing every predicate of the extension of $\rho$ by $S$ gives the extension of the
complemented environment $n \mapsto \neg\rho(n)$ by the predicate $w \mapsto \neg S(w)$.

Formalized by `Cslib.Modal.MuCalculus.extendEnv_compl`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#extend-env-compl).

## Double complement of a predicate

For every predicate $S$ on worlds, the predicate
$w \mapsto \neg\neg S(w)$ equals $S$.

Formalized by `Cslib.Modal.MuCalculus.compl_compl`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#compl-compl).

## Duality

Let $M$ be a Kripke model, $\rho$ an environment assigning a set of worlds to
each variable index $n \in \mathbb{N}$, and $\varphi$ a μ-calculus formula. Let $\neg\varphi$ be
the dual formula of $\varphi$, obtained by swapping atoms with negated atoms, $\bot$ with $\top$,
$\wedge$ with $\vee$, $\Box$ with $\Diamond$ and $\mu$ with $\nu$, and keeping variables. Write
$\overline{\rho}$ for the environment sending each index $n$ to the complement of $\rho(n)$. Then
for every world $w$, $w$ satisfies $\neg\varphi$ in $M$ under $\overline{\rho}$ if and only if $w$
does not satisfy $\varphi$ in $M$ under $\rho$.

Formalized by `Cslib.Modal.MuCalculus.sat_neg`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#sat-neg).

## The μ-calculus formula $\mathsf{EF}\,p$

For an atom $p$, $\mathsf{EF}\,p$ is the least
fixed point formula $\mu X.\,(p \vee \Diamond X)$. It expresses that some state reachable from
the current one satisfies $p$.

Formalized by `Cslib.Modal.MuCalculus.EF`, a definition declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#ef).

## The μ-calculus formula $\mathsf{AG}\,p$

For an atom $p$, $\mathsf{AG}\,p$ is the
greatest fixed point formula $\nu X.\,(p \wedge \Box X)$. It expresses that every state reachable
from the current one satisfies $p$.

Formalized by `Cslib.Modal.MuCalculus.AG`, a definition declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#ag).

## $\mathsf{EF}$ is reachability

For every Kripke model $M$, every environment $\rho$ (an
assignment of a predicate on worlds to each variable index), every atom $p$ and every world $w$,
the μ-calculus formula $\mathsf{EF}\,p$ holds at $w$ in $\rho$ if and only if $p$ is true at some
world reachable from $w$ in zero or more steps of the accessibility relation of $M$.

Formalized by `Cslib.Modal.MuCalculus.EF_iff_reachable`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 463](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#ef-iff-reachable).

## $\mathsf{AG}$ is universal reachability

For every Kripke model $M$, every environment
$\rho$ (an assignment of a predicate on worlds to each variable index), every atom $p$ and every
world $w$, the μ-calculus formula $\mathsf{AG}\,p$ holds at $w$ in $\rho$ if and only if $p$ is
true at every world reachable from $w$ in zero or more steps of the accessibility relation of
$M$.

Formalized by `Cslib.Modal.MuCalculus.AG_iff_forall_reachable`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 491](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L491). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#ag-iff-forall-reachable).

## The formula $\mu X.\, \mu Y.\, X$ is false everywhere

For every Kripke model $M$ and
every environment $\rho$, the formula $\mu X.\, \mu Y.\, X$ holds at no world of $M$ under $\rho$.
In de Bruijn form this formula is $\mu\, \mu\, x_1$: inside the inner binder, variable $1$ refers
to the outer binder, not to the inner one.

Formalized by `Cslib.Modal.MuCalculus.mu_mu_var_one_eq_bot`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 523](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L523). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#mu-mu-var-one-eq-bot).

## The formula $\nu X.\, \nu Y.\, X$ is true everywhere

For every Kripke model $M$ and
every environment $\rho$, the formula $\nu X.\, \nu Y.\, X$ holds at every world of $M$ under
$\rho$. In de Bruijn form this formula is $\nu\, \nu\, x_1$: inside the inner binder, variable
$1$ refers to the outer binder. This is the dual of the fact that $\mu X.\, \mu Y.\, X$ is false
everywhere.

Formalized by `Cslib.Modal.MuCalculus.nu_nu_var_one_eq_top`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculus.lean, line 533](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculus.lean#L533). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#nu-nu-var-one-eq-top).

## μ-calculus formula closed at a given binding depth

A formula is closed at depth `d` when every free de Bruijn variable is `< d`:
only `μ` / `ν` increase the depth; `□` / `◇` do not bind variables and preserve it.

Formalized by `Cslib.Modal.MuCalculus.MuFormula.ClosedAt`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusEncoding.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculusEncoding.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#closed-at).

## Closed modal μ-calculus formula

A formula is closed when it is closed at depth `0`: every variable is bound.

Formalized by `Cslib.Modal.MuCalculus.MuFormula.Closed`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusEncoding.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculusEncoding.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#closed).

## Depth of a modal μ-calculus formula

The depth of a formula: the length of its longest root-to-leaf path, counting
each connective once.

Formalized by `Cslib.Modal.MuCalculus.MuFormula.depth`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusEncoding.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculusEncoding.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#depth).

## Denotation of a closed μ-calculus formula is environment-independent

A closed formula does not depend on the environment: environments agreeing below
the depth give the same denotation.

Formalized by `Cslib.Modal.MuCalculus.sat_closed_env`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusEncoding.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculusEncoding.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#sat-closed-env).

## Cantor-pairing number code of a μ-calculus formula

An injective encoding of μ-calculus formulas over `ℕ` atoms as natural numbers,
via the Cantor pairing function `Nat.pair`. This is a Nat code only, not a complexity
input encoding: repeated pairing squares the code at every unary connective, so the
binary length of the code of `box^d (atom 0)` doubles at each `box` and is exponential
in `d`. Complexity statements use `muTokens` / `muDecodeList` instead.

Formalized by `Cslib.Modal.MuCalculus.muCode`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusEncoding.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculusEncoding.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#mu-code).

## Fuelled decoding of a μ-calculus number code

Fuelled decoding of a `muCode` number back to a formula. The fuel bounds the
recursion depth; `muDecode` supplies fuel `c + 1`, which exceeds every formula's
depth (see `depth_le_code`).

Formalized by `Cslib.Modal.MuCalculus.muDecodeFuel`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusEncoding.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculusEncoding.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#mu-decode-fuel).

## Decoding a μ-calculus number code to a formula

Decode a `muCode` number back to the formula it encodes.

Formalized by `Cslib.Modal.MuCalculus.muDecode`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusEncoding.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculusEncoding.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#mu-decode).

## Depth of a μ-calculus formula is at most its number code

A formula's depth is at most its code: pairing dominates each component
(`Nat.add_le_pair`).

Formalized by `Cslib.Modal.MuCalculus.depth_le_code`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusEncoding.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculusEncoding.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#depth-le-code).

## Fuelled decoding inverts the μ-calculus number code

Decoding inverts encoding, with enough fuel: a formula's own code carries
more fuel than its depth needs.

Formalized by `Cslib.Modal.MuCalculus.muDecodeFuel_muCode`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusEncoding.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculusEncoding.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#mu-decode-fuel-mu-code).

## Decoding inverts the μ-calculus number code

Decoding inverts encoding.

Formalized by `Cslib.Modal.MuCalculus.muDecode_muCode`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusEncoding.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculusEncoding.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#mu-decode-mu-code).

## Polynomial-size token-list encoding of μ-calculus formulas

A polynomial-size token-list encoding of μ-calculus formulas over `ℕ`
atoms, used for the complexity statements in `WantedExt`. Each connective
contributes one tag token (`Nat.pair` of a small tag with `0`), and each atom
or variable contributes one token `Nat.pair tag value`, whose binary size is
`O(log value)`. The canonical bitstring encoding of a `List ℕ` delimits each
token, so the bitstring for a formula has length linear in the number of
connectives plus the total binary size of its atoms: `box^d (atom 0)` is
encoded by exactly `d + 1` tokens, unlike its Cantor-paired `muCode`,
whose binary length is exponential in `d`.

Formalized by `Cslib.Modal.MuCalculus.muTokens`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusEncoding.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculusEncoding.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#mu-tokens).

## Fuelled parser for modal μ-calculus token lists

Fuelled parsing of a `muTokens` token list back to a formula, returning
the formula and the unconsumed suffix. The fuel bounds the recursion depth;
`muDecodeList` supplies fuel `l.length + 1`.

Formalized by `Cslib.Modal.MuCalculus.muParseFuel`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusEncoding.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculusEncoding.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#mu-parse-fuel).

## Decoding a modal μ-calculus token list to a formula

Decode a `muTokens` token list back to the formula it encodes, rejecting
trailing tokens.

Formalized by `Cslib.Modal.MuCalculus.muDecodeList`, a definition declared in [CSLibExt/Logics/Modal/MuCalculusEncoding.lean, line 424](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculusEncoding.lean#L424). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#mu-decode-list).

## Fuelled parsing inverts modal μ-calculus token encoding

Parsing inverts token encoding, with enough fuel.

Formalized by `Cslib.Modal.MuCalculus.muParseFuel_muTokens`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusEncoding.lean, line 430](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculusEncoding.lean#L430). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#mu-parse-fuel-mu-tokens).

## Token-list decoding inverts modal μ-calculus token encoding

Decoding inverts token encoding.

Formalized by `Cslib.Modal.MuCalculus.muDecodeList_muTokens`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusEncoding.lean, line 526](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculusEncoding.lean#L526). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#mu-decode-list-mu-tokens).

## Injectivity of the μ-calculus number code

The encoding is injective.

Formalized by `Cslib.Modal.MuCalculus.muCode_injective`, a theorem declared in [CSLibExt/Logics/Modal/MuCalculusEncoding.lean, line 533](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/MuCalculusEncoding.lean#L533). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html#mu-code-injective).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Modal μ-calculus](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/modal-calculus/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/modal-logic/modal-calculus)
