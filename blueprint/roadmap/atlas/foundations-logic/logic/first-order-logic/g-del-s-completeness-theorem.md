---
declaration: section
origin: cited
lean: Cslib.Logic.FOL.Provable.mp, Cslib.Logic.FOL.Provable.of_bot, Cslib.Logic.FOL.Provable.imp_of_insert, Cslib.Logic.FOL.Consistent, Cslib.Logic.FOL.provable_iff_not_consistent_insert_not, Cslib.Logic.FOL.provable_not_iff_not_consistent_insert, Cslib.Logic.FOL.consistent_sUnion_of_isChain, Cslib.Logic.FOL.MaximalConsistent
statement: formalized
proof: formalized
---

# Gödel's completeness theorem

80 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html).

## Modus ponens for provability from sets

Let $L$ be a first-order language, let $\alpha$ be
an infinite type of variables, and let $S$ be a set of formulas of $L$ with free variables in
$\alpha$. For formulas $\varphi$ and $\psi$, if $S$ proves $\varphi \to \psi$ and $S$ proves
$\varphi$, then $S$ proves $\psi$.

Formalized by `Cslib.Logic.FOL.Provable.mp`, a theorem declared in [CSLibExt/Logics/FirstOrder/Consistency.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Consistency.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#mp).

## Ex falso for provability from sets

Let $L$ be a first-order language, let $\alpha$ be an
infinite type of variables, and let $S$ be a set of formulas of $L$ with free variables in
$\alpha$. If $S$ proves $\bot$, then $S$ proves every formula $\varphi$.

Formalized by `Cslib.Logic.FOL.Provable.of_bot`, a theorem declared in [CSLibExt/Logics/FirstOrder/Consistency.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Consistency.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#of-bot).

## Deduction theorem

Let $\alpha$ be an infinite set of variables, let $S$ be a set of
formulas with free variables in $\alpha$, and let $\varphi$, $\psi$ be such formulas. If
$S \cup \{\varphi\}$ proves $\psi$, then $S$ proves $\varphi \to \psi$.

Formalized by `Cslib.Logic.FOL.Provable.imp_of_insert`, a theorem declared in [CSLibExt/Logics/FirstOrder/Consistency.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Consistency.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#imp-of-insert).

## Consistent set of formulas

Let $L$ be a first-order language and $\alpha$ a type of
variables. A set $S$ of formulas of $L$ with free variables in $\alpha$ is consistent when $S$
does not prove $\bot$.

Formalized by `Cslib.Logic.FOL.Consistent`, a definition declared in [CSLibExt/Logics/FirstOrder/Consistency.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Consistency.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#consistent).

## Provability as inconsistency with the negation

Let $L$ be a first-order language, let
$\alpha$ be an infinite type of variables, let $S$ be a set of formulas of $L$ with free variables
in $\alpha$, and let $\varphi$ be a formula. Then $S$ proves $\varphi$ if and only if
$S \cup \{\neg\varphi\}$ is not consistent.

Formalized by `Cslib.Logic.FOL.provable_iff_not_consistent_insert_not`, a theorem declared in [CSLibExt/Logics/FirstOrder/Consistency.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Consistency.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#provable-iff-not-consistent-insert-not).

## Refutability as inconsistency

Let $L$ be a first-order language, let $\alpha$ be an
infinite type of variables, let $S$ be a set of formulas of $L$ with free variables in $\alpha$,
and let $\varphi$ be a formula. Then $S$ proves $\neg\varphi$ if and only if
$S \cup \{\varphi\}$ is not consistent.

Formalized by `Cslib.Logic.FOL.provable_not_iff_not_consistent_insert`, a theorem declared in [CSLibExt/Logics/FirstOrder/Consistency.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Consistency.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#provable-not-iff-not-consistent-insert).

## Unions of chains of consistent sets are consistent

If $C$ is a nonempty family of
sets of formulas that is totally ordered by inclusion and every member of $C$ is consistent,
then the union $\bigcup C$ is consistent.

A refutation uses only finitely many hypotheses, and these all lie in a single member of $C$.

Formalized by `Cslib.Logic.FOL.consistent_sUnion_of_isChain`, a theorem declared in [CSLibExt/Logics/FirstOrder/Consistency.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Consistency.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#consistent-s-union-of-is-chain).

## Maximal consistent set

A set $\Delta$ of formulas is maximal consistent when it is
consistent and every consistent set of formulas containing $\Delta$ is contained in
$\Delta$, that is, equals $\Delta$.

Formalized by `Cslib.Logic.FOL.MaximalConsistent`, an abbreviation declared in [CSLibExt/Logics/FirstOrder/Consistency.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Consistency.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#maximal-consistent).

## Maximal consistent sets absorb consistent extensions

Let $\Delta$ be a maximal consistent
set of first-order formulas of a language $L$ with free variables in $\alpha$, and let $\varphi$ be
a formula. If $\Delta \cup \{\varphi\}$ is consistent, then $\varphi \in \Delta$.

Formalized by `Cslib.Logic.FOL.MaximalConsistent.mem_of_consistent_insert`, a theorem declared in [CSLibExt/Logics/FirstOrder/Consistency.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Consistency.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#mem-of-consistent-insert).

## Lindenbaum's lemma for first-order logic

Every consistent set $S$ of first-order
formulas is contained in a maximal consistent set.

Formalized by `Cslib.Logic.FOL.exists_maximalConsistent`, a theorem declared in [CSLibExt/Logics/FirstOrder/Consistency.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Consistency.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#exists-maximal-consistent).

## Maximal consistent sets of first-order formulas are deductively closed

Let $L$ be a
first-order language, let $\alpha$ be an infinite type of variables, and let $\Delta$ be a maximal
consistent set of formulas of $L$ with free variables in $\alpha$. Every formula $\varphi$ that
$\Delta$ proves lies in $\Delta$.

Formalized by `Cslib.Logic.FOL.MaximalConsistent.mem_of_provable`, a theorem declared in [CSLibExt/Logics/FirstOrder/Consistency.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Consistency.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#mem-of-provable).

## Maximal consistent sets decide every formula

Let $L$ be a first-order language, let
$\alpha$ be an infinite type of variables, and let $\Delta$ be a maximal consistent set of formulas
of $L$ with free variables in $\alpha$. For every formula $\varphi$, $\neg\varphi \in \Delta$ if
and only if $\varphi \notin \Delta$; so exactly one of $\varphi$ and $\neg\varphi$ lies in
$\Delta$.

Formalized by `Cslib.Logic.FOL.MaximalConsistent.not_mem_iff`, a theorem declared in [CSLibExt/Logics/FirstOrder/Consistency.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Consistency.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#not-mem-iff).

## Universal instantiation in maximal consistent sets

Let $\alpha$ be an infinite set of
variables and let $\Delta$ be a maximal consistent set of formulas with free variables in
$\alpha$. Let $\varphi(x)$ be a formula with one bound variable $x$ left open, and for a term
$t$ write $\varphi(t)$ for the result of substituting $t$ for $x$. If $\Delta$ contains
$\forall x\, \varphi$, then $\Delta$ contains $\varphi(t)$ for every term $t$.

Formalized by `Cslib.Logic.FOL.MaximalConsistent.instantiate_mem_of_all_mem`, a theorem declared in [CSLibExt/Logics/FirstOrder/Consistency.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Consistency.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#instantiate-mem-of-all-mem).

## Substitution of equals in maximal consistent sets

Let $\alpha$ be an infinite set of
variables and let $\Delta$ be a maximal consistent set of formulas with free variables in
$\alpha$. Let $\varphi(x)$ be a formula with one bound variable $x$ left open, and for a term
$u$ write $\varphi(u)$ for the result of substituting $u$ for $x$. If $s$ and $t$ are terms
such that $\Delta$ contains the equation $s = t$ and the formula $\varphi(s)$, then $\Delta$
contains $\varphi(t)$.

Formalized by `Cslib.Logic.FOL.MaximalConsistent.instantiate_mem_of_equal`, a theorem declared in [CSLibExt/Logics/FirstOrder/Consistency.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Consistency.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#instantiate-mem-of-equal).

## Henkin axiom

Let $\varphi(x)$ be a formula with one bound variable $x$ left open and
let $c$ be a variable; write $\varphi(c)$ for the result of substituting $c$ for $x$. The
Henkin axiom for $\forall x\, \varphi$ with witness $c$ is the formula
$\neg \forall x\, \varphi \to \neg \varphi(c)$.

Formalized by `Cslib.Logic.FOL.henkinAxiom`, a definition declared in [CSLibExt/Logics/FirstOrder/Consistency.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Consistency.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#henkin-axiom).

## Adding a Henkin axiom preserves consistency

Let $\alpha$ be an infinite set of
variables and let $S$ be a consistent set of formulas with free variables in $\alpha$. Let
$\varphi(x)$ be a formula with one bound variable $x$ left open, and let $c \in \alpha$ be a
variable that occurs free neither in $\varphi$ nor in any formula of $S$. Then $S$ together
with the Henkin axiom for $\forall x\, \varphi$ with witness $c$ is consistent.

Formalized by `Cslib.Logic.FOL.Consistent.insert_henkinAxiom`, a theorem declared in [CSLibExt/Logics/FirstOrder/Consistency.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Consistency.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#insert-henkin-axiom).

## Universal formulas from Henkin witnesses

Let $\alpha$ be an infinite set of
variables and let $\Delta$ be a maximal consistent set of formulas with free variables in
$\alpha$. Let $\varphi(x)$ be a formula with one bound variable $x$ left open, let
$c \in \alpha$, and write $\varphi(c)$ for the result of substituting $c$ for $x$. If
$\Delta$ contains the Henkin axiom for $\forall x\, \varphi$ with witness $c$ and contains
$\varphi(c)$, then $\Delta$ contains $\forall x\, \varphi$.

Formalized by `Cslib.Logic.FOL.MaximalConsistent.all_mem_of_henkin`, a theorem declared in [CSLibExt/Logics/FirstOrder/Consistency.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Consistency.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#all-mem-of-henkin).

## Free variables of an instance

Let $t$ be a term and $\varphi$ a first-order formula with
$m + 1$ bound variables, and let $\varphi(t)$ be the instance obtained by substituting $t$ for the
outermost bound variable. Every free variable of $\varphi(t)$ is a free variable of $\varphi$ or a
variable of $t$.

Formalized by `Cslib.Logic.FOL.freeVarFinset_instantiate_subset`, a theorem declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#free-var-finset-instantiate-subset).

## Depth of a formula

The depth $d(\varphi)$ of a first-order formula $\varphi$ is the
nesting height of its implications and universal quantifiers: $\bot$, equations and relation
atoms have depth $0$, the implication $\varphi \to \psi$ has depth
$\max(d(\varphi), d(\psi)) + 1$, and $\forall \varphi$ has depth $d(\varphi) + 1$.

Formalized by `Cslib.Logic.FOL.depth`, a definition declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#depth).

## Renaming depends only on the free variables

Let $\alpha$ and $\beta$ be types of
variables, let $n \in \mathbb{N}$, and let $\varphi$ be a formula with free variables in $\alpha$
and $n$ further variables reserved for binding by enclosing quantifiers. If two maps
$f, g : \alpha \to \beta$ agree on every variable from $\alpha$ that occurs free in $\varphi$,
then renaming the variables of $\varphi$ from $\alpha$ along $f$ and along $g$ gives the same
formula.

Formalized by `Cslib.Logic.FOL.rename_congr_of_eqOn`, a theorem declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#rename-congr-of-eq-on).

## Renaming free variables along an arbitrary map preserves derivability

Let $\alpha$ and
$\beta$ be types of variables with $\beta$ infinite, and let $f : \alpha \to \beta$ be any map.
If $\varphi$ is derivable from the list of hypotheses $\Gamma$ in natural deduction, then the
formula obtained from $\varphi$ by renaming each free variable $x$ to $f(x)$ is derivable from
the list obtained by renaming the free variables of each formula of $\Gamma$ in the same way.

The map need not be injective: in the proof each eigenvariable is sent to a fresh variable.

Formalized by `Cslib.Logic.FOL.Derivable.relabel_of_infinite`, a theorem declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#relabel-of-infinite).

## Doubling the variables preserves consistency

If $S$ is a consistent set of formulas with
free variables in $\mathbb{N}$, then the set obtained from $S$ by renaming every free variable
$x$ to $2x$ in each of its formulas is consistent.

Halving the variables maps any derivation of $\bot$ from the renamed set back to one from $S$.

Formalized by `Cslib.Logic.FOL.Consistent.relabel_double`, a theorem declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#relabel-double).

## Replacing arguments one at a time

Let $r$ be a relation on a type $\beta$, let $n$ be a
natural number and let $P$ be a property of $n$-tuples $x = (x_i)_{i < n}$ in $\beta$. Suppose
that for every tuple $x$, every position $i$ and all $a, b \in \beta$ with $r(a, b)$, if $P$
holds of $x$ with its $i$-th entry replaced by $a$, then $P$ holds of $x$ with its $i$-th entry
replaced by $b$. Then for all tuples $x, y$ with $r(x_i, y_i)$ for every $i$, $P(x)$ implies
$P(y)$.

Formalized by `Cslib.Logic.FOL.update_chain`, a theorem declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#update-chain).

## Congruence for function symbols in a maximal consistent set

Let $\Delta$ be a maximal
consistent set of first-order formulas with free variables in $\mathbb{N}$, let $f$ be an $n$-ary
function symbol, let $x = (x_0, \dots, x_{n-1})$ be terms over $\mathbb{N}$ and let $i < n$. For a
term $u$, write $x[i := u]$ for $x$ with its $i$-th entry replaced by $u$. If the equation
$a = b$ lies in $\Delta$, then the equation $f(x[i := a]) = f(x[i := b])$ lies in $\Delta$.

Formalized by `Cslib.Logic.FOL.MaximalConsistent.func_update`, a theorem declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#func-update).

## Replacing an argument of a relation symbol by an equal term

Let $\Delta$ be a maximal
consistent set of formulas with free variables in $\mathbb{N}$, let $R$ be an $n$-ary relation
symbol, let $x_0, \dots, x_{n-1}$, $a$ and $b$ be terms with variables in $\mathbb{N}$, and let
$i < n$. If $\Delta$ contains $a = b$ and contains $R(x_0, \dots, x_{n-1})$ with $x_i$ replaced
by $a$, then $\Delta$ contains $R(x_0, \dots, x_{n-1})$ with $x_i$ replaced by $b$.

Formalized by `Cslib.Logic.FOL.MaximalConsistent.rel_update`, a theorem declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#rel-update).

## Term structure of a set of formulas

Let $\Delta$ be a set of first-order formulas in a
language $L$ with free variables in $\mathbb{N}$. The term structure of $\Delta$ is the
$L$-structure whose domain is the set of $L$-terms with variables in $\mathbb{N}$, in which an
$n$-ary function symbol $f$ sends terms $t_1, \dots, t_n$ to the term $f(t_1, \dots, t_n)$, and
an $n$-ary relation symbol $R$ holds of $t_1, \dots, t_n$ exactly when the atomic formula
$R(t_1, \dots, t_n)$ belongs to $\Delta$.

Formalized by `Cslib.Logic.FOL.termStructure`, a definition declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#term-structure).

## Provable equality of terms

Let $\Delta$ be a maximal consistent set of first-order
formulas in a language $L$ with free variables in $\mathbb{N}$. Provable equality in $\Delta$ is
the equivalence relation on $L$-terms with variables in $\mathbb{N}$ under which $s \sim t$ holds
exactly when the equation $s = t$ belongs to $\Delta$.

Formalized by `Cslib.Logic.FOL.termSetoid`, a definition declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#term-setoid).

## Term model of a maximal consistent set

For a maximal consistent set $\Delta$ of formulas
with free variables in $\mathbb{N}$, the term model of $\Delta$ is the set of terms with
variables in $\mathbb{N}$ modulo the equivalence relation that identifies $s$ and $t$ when the
formula $s = t$ belongs to $\Delta$.

Formalized by `Cslib.Logic.FOL.TermModel`, an abbreviation declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 411](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L411). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#term-model).

## Canonical assignment of the term model

For a maximal consistent set $\Delta$ of formulas
with free variables in $\mathbb{N}$, the canonical assignment sends each variable
$x \in \mathbb{N}$ to $[x]$, the class of the variable term $x$ in the term model of $\Delta$.

Formalized by `Cslib.Logic.FOL.termAssignment`, a definition declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 414](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L414). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#term-assignment).

## Lowering a term with no bound variables

A term whose variables are free variables from
$\mathbb{N}$ together with bound variables from the empty index set is lowered to the term over
$\mathbb{N}$ of the same shape, in which every free variable $x$ stays $x$.

Formalized by `Cslib.Logic.FOL.lowerTerm`, a definition declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#lower-term).

## Truth lemma for the first-order term model

Let $\Delta$ be a maximal consistent set of
formulas with free variables in $\mathbb{N}$ such that, for every formula $\varphi$ with one
bound variable, if $\Delta$ contains $\varphi(t)$ for every term $t$ (where $\varphi(t)$ is the
result of substituting $t$ for the bound variable), then $\Delta$ contains $\forall x\,\varphi$.
Then a formula $\psi$ with free variables in $\mathbb{N}$ holds in the term model of $\Delta$
under the canonical assignment $x \mapsto [x]$ if and only if $\psi \in \Delta$.

Formalized by `Cslib.Logic.FOL.realize_termModel_iff`, a theorem declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 454](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L454). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#realize-term-model-iff).

## Enumeration of formulas with one bound variable

For a language with countably many
symbols, the formulas $\varphi_0, \varphi_1, \dots$ are a fixed enumeration, chosen by choice, of
all first-order formulas with free variables in $\mathbb{N}$ and one bound variable: every such
formula is $\varphi_k$ for some $k \in \mathbb{N}$.

Formalized by `Cslib.Logic.FOL.enumBody`, a definition declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 509](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L509). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#enum-body).

## Variable bound of a formula

Let $\varphi$ be a first-order formula whose variables are
natural numbers together with $n$ variables reserved for quantifiers. Its variable bound
$b(\varphi)$ is one more than the largest natural number occurring as a free variable of
$\varphi$, or $1$ when there is none; it is a strict upper bound on these free variables.

Formalized by `Cslib.Logic.FOL.varBound`, a definition declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 517](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L517). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#var-bound).

## Witness bases

Let $L$ be a first-order language with countably many symbols, let
$\varphi_0, \varphi_1, \dots$ be the fixed surjective enumeration of the $L$-formulas with free
variables in $\mathbb{N}$ and one variable reserved for a quantifier, and let $b(\varphi)$ be one
more than the largest free variable of $\varphi$, or $1$ if it has none. The witness bases are
defined by $w_0 = b(\varphi_0)$ and $w_{k+1} = w_k + 1 + b(\varphi_{k+1})$. They are strictly
increasing, and $w_k$ exceeds every free variable of $\varphi_0, \dots, \varphi_k$.

Formalized by `Cslib.Logic.FOL.witnessBase`, a definition declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 525](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L525). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#witness-base).

## Henkin witnesses

Let $L$ be a first-order language with countably many symbols and let
$w_0 < w_1 < \dots$ be its witness bases, built from the fixed enumeration
$\varphi_0, \varphi_1, \dots$ of the $L$-formulas with one variable reserved for a quantifier.
The $k$-th Henkin witness is the variable $c_k = 2 w_k + 1$. It is odd, so it is not a free
variable of any formula whose free variables are all even, and it exceeds every free variable
of $\varphi_0, \dots, \varphi_k$.

Formalized by `Cslib.Logic.FOL.witness`, a definition declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 531](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#witness).

## The $k$-th Henkin axiom

For a language with countably many symbols and $k \in \mathbb{N}$,
the $k$-th Henkin axiom is the Henkin axiom $\neg \forall \varphi_k \to \neg \varphi_k(c_k)$, where
$\varphi_k$ is the $k$-th formula in the enumeration of formulas with one bound variable and
$c_k$ is the $k$-th Henkin witness.

Formalized by `Cslib.Logic.FOL.henkinAxiomAt`, a definition declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 559](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L559). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#henkin-axiom-at).

## Stages of the Henkin extension

Let $S$ be a set of first-order formulas with free variables
in $\mathbb{N}$, in a language with countably many symbols, and let $H_k$ be the $k$-th Henkin
axiom. The stages $S_k$ are defined by $S_0 = S$ and $S_{k+1} = S_k \cup \{H_k\}$, so $S_k$ is
$S$ together with $H_0, \dots, H_{k-1}$.

Formalized by `Cslib.Logic.FOL.henkinStage`, a definition declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 563](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L563). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#henkin-stage).

## Henkin extension

For a language with countably many symbols, the Henkin extension of a set
$S$ of first-order formulas with free variables in $\mathbb{N}$ is $S$ together with all Henkin
axioms, the $k$-th Henkin axiom for every $k \in \mathbb{N}$.

Formalized by `Cslib.Logic.FOL.henkinSet`, a definition declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 585](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L585). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#henkin-set).

## Henkin extension of a consistent set

Let $L$ be a language with countably many symbols
and let $S$ be a consistent set of first-order formulas with free variables in $\mathbb{N}$ such
that every free variable of every formula in $S$ is even. Then $S$ is contained in a maximal
consistent set $\Delta$ with the Henkin property: for every formula $\varphi$ with one bound
variable, if every instance $\varphi(t)$, for $t$ a term over $\mathbb{N}$, lies in $\Delta$, then
$\forall \varphi$ lies in $\Delta$.

Formalized by `Cslib.Logic.FOL.exists_maximalConsistent_henkin`, a theorem declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 617](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L617). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#exists-maximal-consistent-henkin).

## Model existence for first-order logic

Let $L$ be a language with countably many symbols.
Every consistent set $S$ of first-order formulas with free variables in $\mathbb{N}$ is
satisfiable: there are a nonempty $L$-structure $M$, in the universe of the function symbols of
$L$, and an assignment $v : \mathbb{N} \to M$ under which every formula of $S$ holds.

The free variables are first doubled, which keeps the set consistent and leaves the odd variables
free for Henkin witnesses.

Formalized by `Cslib.Logic.FOL.exists_model_of_consistent`, a theorem declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 631](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L631). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#exists-model-of-consistent).

## Strong completeness of first-order natural deduction

Let $L$ be a language with
countably many function and relation symbols, whose function symbols live in universe $u$. Let
$S$ be a set of formulas of $L$ and $\varphi$ a formula of $L$, all with free variables in
$\mathbb{N}$. If for every $L$-structure $M$ with carrier in universe $u$ and every assignment
$v : \mathbb{N} \to M$ under which all formulas of $S$ hold, $\varphi$ also holds under $v$,
then $\varphi$ is provable from $S$.

Formalized by `Cslib.Logic.FOL.provable_of_entails`, a theorem declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 646](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L646). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#provable-of-entails).

## Completeness of first-order natural deduction for theories

Let $L$ be a language with
countably many function and relation symbols, whose function symbols live in universe $u$ and
relation symbols in universe $v$. Let $T$ be a theory of $L$ and $\varphi$ a formula of $L$ with
free variables in $\mathbb{N}$. If $\varphi$ holds under every assignment of the variables in
every nonempty model of $T$ whose carrier lies in universe $\max(u, v)$, then $\varphi$ is
provable from the sentences of $T$, viewed as formulas over $\mathbb{N}$.

Formalized by `Cslib.Logic.FOL.provable_of_models`, a theorem declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 657](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L657). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#provable-of-models).

## Soundness and completeness of first-order natural deduction

Let $L$ be a language with
countably many function and relation symbols, whose function symbols live in universe $u$ and
relation symbols in universe $v$. For every theory $T$ of $L$ and every formula $\varphi$ of $L$
with free variables in $\mathbb{N}$, $\varphi$ is provable from the sentences of $T$, viewed as
formulas over $\mathbb{N}$, if and only if $\varphi$ holds under every assignment of the
variables in every nonempty model of $T$ whose carrier lies in universe $\max(u, v)$.

Formalized by `Cslib.Logic.FOL.provable_iff_models`, a theorem declared in [CSLibExt/Logics/FirstOrder/Completeness.lean, line 673](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Completeness.lean#L673). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#provable-iff-models).

## Finite set of symbols of a term

The finite set of symbols occurring in a term $t$ of a
first-order language $L$, a finite subset of the function and relation symbols of $L$, is
defined by recursion on $t$: it is empty when $t$ is a variable, and when
$t = f(t_0, \dots, t_{l-1})$ for an $l$-ary function symbol $f$ it consists of $f$ together with
the symbols occurring in each of $t_0, \dots, t_{l-1}$.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1 (the finite set of symbols occurring in a finite derivation).

Formalized by `Cslib.Logic.FOL.termSymbolFinset`, a definition declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#term-symbol-finset).

## The head function symbol of a term occurs in it

Let $L$ be a first-order language, $f$
an $l$-ary function symbol of $L$, and $t_1, \dots, t_l$ $L$-terms with variables in $\alpha$.
Then $f$ belongs to the finite set of symbols occurring in the term $f(t_1, \dots, t_l)$.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1.

Formalized by `Cslib.Logic.FOL.mem_termSymbolFinset_func`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#mem-term-symbol-finset-func).

## Symbols of an argument of a function application

Let $f$ be an $l$-ary function symbol
of a first-order language $L$ and let $t_0, \dots, t_{l-1}$ be terms of $L$ in variables from
$\alpha$. For every $i < l$, every symbol occurring in $t_i$ occurs in the term
$f(t_0, \dots, t_{l-1})$: the finite set of symbols of $t_i$ is contained in that of
$f(t_0, \dots, t_{l-1})$.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1.

Formalized by `Cslib.Logic.FOL.termSymbolFinset_func_subset`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#term-symbol-finset-func-subset).

## Finite set of symbols of a formula

The finite set of function and relation symbols
occurring in a bounded formula of a first-order language $L$, defined by recursion on the
formula: $\bot$ has no symbols; an equation $t_1 = t_2$ has the function symbols of $t_1$ and
$t_2$; an atomic formula $R(t_1, \dots, t_l)$ has $R$ together with the function symbols of
$t_1, \dots, t_l$; an implication $\varphi \to \psi$ has the symbols of $\varphi$ and of $\psi$;
and $\forall \varphi$ has the symbols of $\varphi$.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1.

Formalized by `Cslib.Logic.FOL.formulaSymbolFinset`, a definition declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#formula-symbol-finset).

## Symbols of the left side of an equation

Let $L$ be a first-order language and let $t_1$,
$t_2$ be terms of $L$ in free variables from $\alpha$ and $n$ bound variables. Every symbol
occurring in $t_1$ occurs in the atomic formula $t_1 = t_2$, viewed as a formula with $n$ bound
variables: the finite set of symbols of $t_1$ is contained in that of $t_1 = t_2$.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1.

Formalized by `Cslib.Logic.FOL.termSymbolFinset_equal_subset_left`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#term-symbol-finset-equal-subset-left).

## Symbols of the right side of an equation

Let $L$ be a first-order language and let
$t_1$, $t_2$ be terms of $L$ in free variables from $\alpha$ and $n$ bound variables. Every symbol
occurring in $t_2$ occurs in the atomic formula $t_1 = t_2$, viewed as a formula with $n$ bound
variables: the finite set of symbols of $t_2$ is contained in that of $t_1 = t_2$.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1.

Formalized by `Cslib.Logic.FOL.termSymbolFinset_equal_subset_right`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#term-symbol-finset-equal-subset-right).

## The relation symbol of an atomic formula occurs in it

Let $L$ be a first-order
language, $R$ an $l$-ary relation symbol of $L$, and $t_1, \dots, t_l$ $L$-terms with free
variables in $\alpha$ and $n$ bound variables. Then $R$ belongs to the finite set of symbols
occurring in the atomic bounded formula $R(t_1, \dots, t_l)$.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1.

Formalized by `Cslib.Logic.FOL.mem_formulaSymbolFinset_rel`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#mem-formula-symbol-finset-rel).

## Symbols of an argument of a relational atomic formula

Let $R$ be an $l$-ary relation
symbol of a first-order language $L$ and let $t_0, \dots, t_{l-1}$ be terms of $L$ in free
variables from $\alpha$ and $n$ bound variables. For every $i < l$, every symbol occurring in
$t_i$ occurs in the atomic formula $R(t_0, \dots, t_{l-1})$, viewed as a formula with $n$ bound
variables: the finite set of symbols of $t_i$ is contained in that of $R(t_0, \dots, t_{l-1})$.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1.

Formalized by `Cslib.Logic.FOL.termSymbolFinset_rel_subset`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#term-symbol-finset-rel-subset).

## Symbols of the antecedent occur in an implication

For bounded formulas $\varphi$ and
$\psi$ of a first-order language $L$ with free variables in $\alpha$ and $n$ bound variables,
every symbol occurring in $\varphi$ occurs in $\varphi \to \psi$.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1.

Formalized by `Cslib.Logic.FOL.formulaSymbolFinset_imp_subset_left`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#formula-symbol-finset-imp-subset-left).

## Symbols of the consequent occur in an implication

For bounded formulas $\varphi$ and
$\psi$ of a first-order language $L$ with free variables in $\alpha$ and $n$ bound variables,
every symbol occurring in $\psi$ occurs in $\varphi \to \psi$.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1.

Formalized by `Cslib.Logic.FOL.formulaSymbolFinset_imp_subset_right`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#formula-symbol-finset-imp-subset-right).

## Symbols of a finite set of formulas

For a finite set $F$ of first-order formulas of a
language $L$ with free variables indexed by $\mathbb{N}$, the symbols of $F$ are the finite set
of function and relation symbols of $L$ that occur in some formula of $F$, that is, the union over
$\psi \in F$ of the finite sets of symbols occurring in $\psi$.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1.

Formalized by `Cslib.Logic.FOL.symbolsOf`, a definition declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#symbols-of).

## A symbol of a member of a set of formulas is a symbol of the set

Let $L$ be a first-order
language, $F$ a finite set of $L$-formulas with free variables in $\mathbb{N}$, and $\psi \in F$.
Every symbol occurring in $\psi$ belongs to the finite set of symbols occurring in some formula
of $F$.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1.

Formalized by `Cslib.Logic.FOL.mem_symbolsOf`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#mem-symbols-of).

## Sublanguage of a finite set of formulas

For a finite set $F$ of formulas of a
first-order language $L$ with free variables in $\mathbb{N}$, the sublanguage of $L$ on the
symbols occurring in $F$ has as its $n$-ary function symbols the $n$-ary function symbols of
$L$ that occur in some formula of $F$, and as its $n$-ary relation symbols the $n$-ary
relation symbols of $L$ that occur in some formula of $F$.

## Sources

- H.-D. Ebbinghaus, J. Flum, and W. Thomas, *Mathematical Logic*, 2nd ed., Springer 1994, Chapter V (the sublanguage generated by a finite set of formulas).

Formalized by `Cslib.Logic.FOL.subLanguage`, a definition declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#sub-language).

## Inclusion of the sublanguage of a finite set of formulas

Let $L$ be a first-order
language. For a finite set $F$ of formulas of $L$ with free variables in $\mathbb{N}$, this is
the language homomorphism from the sublanguage of $L$ on the symbols occurring in $F$ into $L$
that sends each function symbol and each relation symbol to itself.

## Sources

- H.-D. Ebbinghaus, J. Flum, and W. Thomas, *Mathematical Logic*, 2nd ed., Springer 1994, Chapter V.

Formalized by `Cslib.Logic.FOL.subLanguageIncl`, a definition declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#sub-language-incl).

## The inclusion of the sublanguage of a finite set of formulas is injective

Let $L$ be a
first-order language. For every finite set $F$ of formulas of $L$ with free variables in
$\mathbb{N}$, the inclusion into $L$ of the sublanguage of $L$ on the symbols occurring in $F$
is injective on function symbols and on relation symbols.

## Sources

- H.-D. Ebbinghaus, J. Flum, and W. Thomas, *Mathematical Logic*, 2nd ed., Springer 1994, Chapter V.

Formalized by `Cslib.Logic.FOL.subLanguageIncl_injective`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#sub-language-incl-injective).

## Terms lift to the finite-symbol sublanguage

Let $F$ be a finite set of formulas of a
first-order language $L$ with free variables in $\mathbb{N}$, and let $L_F$ be the sublanguage of
$L$ on the symbols occurring in $F$, with inclusion $\iota : L_F \to L$. Every term $t$ of $L$
whose variables are drawn from $\mathbb{N}$ and from $n$ bound variables, each of whose symbols
occurs in some formula of $F$, is the image under $\iota$ of a term of $L_F$ with variables drawn
from the same set.

## Sources

- H.-D. Ebbinghaus, J. Flum, and W. Thomas, *Mathematical Logic*, 2nd ed., Springer 1994, Chapter V.

Formalized by `Cslib.Logic.FOL.exists_term_preimage`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#exists-term-preimage).

## Bounded formulas lift to the finite-symbol sublanguage

Let $F$ be a finite set of
formulas of a first-order language $L$ with free variables in $\mathbb{N}$, and let $L_F$ be the
sublanguage of $L$ on the symbols occurring in $F$, with inclusion $\iota : L_F \to L$. Every
bounded formula $\varphi$ of $L$ with free variables in $\mathbb{N}$ and $n$ bound variables, each
of whose symbols occurs in some formula of $F$, is the image under $\iota$ of a bounded formula
of $L_F$ with free variables in $\mathbb{N}$ and $n$ bound variables.

## Sources

- H.-D. Ebbinghaus, J. Flum, and W. Thomas, *Mathematical Logic*, 2nd ed., Springer 1994, Chapter V.

Formalized by `Cslib.Logic.FOL.exists_boundedFormula_preimage`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#exists-bounded-formula-preimage).

## Language homomorphisms commute with renaming variables

Let $h \colon L \to L'$ be a
homomorphism of first-order languages, and for an $L$-term $u$ write $h(u)$ for the $L'$-term
obtained by replacing every function symbol by its image under $h$. Let $t$ be an $L$-term with
variables in $\alpha$ and $g \colon \alpha \to \beta$ a map. Then $h$ applied to the term
obtained from $t$ by renaming each variable $a$ to $g(a)$ equals the term obtained from $h(t)$
by the same renaming.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1 (derivations depend only on the shape of a formula, not on the names of its symbols).

Formalized by `Cslib.Logic.FOL.onTerm_relabel`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#on-term-relabel).

## Language homomorphisms commute with substitution in terms

Let $h \colon L \to L'$ be a
homomorphism of first-order languages, and for an $L$-term $u$ write $h(u)$ for the $L'$-term
obtained by replacing every function symbol by its image under $h$. Let $s$ be an $L$-term with
variables in $\beta$ and $g$ a map assigning to each $b \in \beta$ an $L$-term $g(b)$ with
variables in $\gamma$. Then $h$ applied to the term obtained from $s$ by substituting $g(b)$ for
each variable $b$ equals the term obtained from $h(s)$ by substituting $h(g(b))$ for each
variable $b$.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1.

Formalized by `Cslib.Logic.FOL.onTerm_subst`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#on-term-subst).

## Term substitution depends only on the values of the substitution

Let $L$ be a
first-order language, let $s$ be a term of $L$ with variables in a type $\beta$, and let $g$ and
$g'$ assign to each variable in $\beta$ a term of $L$ with variables in a type $\gamma$. If
$g(a) = g'(a)$ for every $a \in \beta$, then substituting $g$ into $s$ gives the same term as
substituting $g'$ into $s$.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1.

Formalized by `Cslib.Logic.FOL.subst_congr`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#subst-congr).

## Language homomorphisms commute with instantiation in terms

Let $h \colon L \to L'$ be a
homomorphism of first-order languages, and for an $L$-term $u$ write $h(u)$ for the $L'$-term
obtained by replacing every function symbol by its image under $h$. Let $t$ be an $L$-term with
free variables in $\alpha$ and $s$ an $L$-term with free variables in $\alpha$ and $m + 1$
bound variables. Then $h$ applied to the instantiation of $t$ for the outermost bound variable
(the one with index $0$) of $s$ equals the instantiation of $h(t)$ for the outermost bound
variable of $h(s)$.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1.

Formalized by `Cslib.Logic.FOL.onTerm_instantiateTerm`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#on-term-instantiate-term).

## Language homomorphisms commute with instantiation in formulas

Let $h \colon L \to L'$ be
a homomorphism of first-order languages. For an $L$-term or bounded $L$-formula $x$, write $h(x)$
for the term or bounded formula of $L'$ obtained by replacing every symbol by its image under
$h$. Let $t$ be an $L$-term with free variables in $\alpha$ and $\varphi$ a bounded $L$-formula
with free variables in $\alpha$ and $m + 1$ bound variables. Then $h$ applied to the
instantiation of $t$ for the outermost bound variable (the one with index $0$) of $\varphi$
equals the instantiation of $h(t)$ for the outermost bound variable of $h(\varphi)$.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1.

Formalized by `Cslib.Logic.FOL.onBoundedFormula_instantiate`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#on-bounded-formula-instantiate).

## Language homomorphisms preserve the free variables of a term

Let $\phi : L \to L'$ be a
homomorphism of first-order languages and let $t$ be a term of $L$ in free variables from
$\alpha$ and $n$ bound variables. The finite set of free variables from $\alpha$ occurring in the
image $\phi(t)$ of $t$ under $\phi$ equals the finite set of those occurring in $t$.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1.

Formalized by `Cslib.Logic.FOL.varFinsetLeft_onTerm`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#var-finset-left-on-term).

## Language homomorphisms preserve free variables

Let $h : L \to L'$ be a homomorphism of
first-order languages, and let $\varphi$ be a bounded formula of $L$ with free variables in
$\alpha$ and $n$ bound variables. The formula of $L'$ obtained from $\varphi$ by replacing each
symbol by its image under $h$ has the same free variables as $\varphi$.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1.

Formalized by `Cslib.Logic.FOL.freeVarFinset_onBoundedFormula`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#free-var-finset-on-bounded-formula).

## Language homomorphisms preserve equations

Let $h \colon L \to L'$ be a homomorphism of
first-order languages. For an $L$-term or $L$-formula $x$, write $h(x)$ for the term or formula
of $L'$ obtained by replacing every symbol by its image under $h$. If $s$ and $t$ are $L$-terms
with free variables in $\alpha$, then $h$ applied to the formula $s = t$ is the formula
$h(s) = h(t)$.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1.

Formalized by `Cslib.Logic.FOL.onFormula_equal`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#on-formula-equal).

## Derivations survive language homomorphisms

Let $h : L \to L'$ be a homomorphism of
first-order languages, and write $h(\varphi)$ for the formula of $L'$ obtained from a formula
$\varphi$ of $L$ by replacing each symbol by its image under $h$. Let $\Gamma$ be a finite list of
formulas of $L$ with free variables in $\alpha$, and let $\varphi$ be a formula of $L$ with free
variables in $\alpha$. If $\Gamma \vdash \varphi$ in natural deduction, then
$h(\Gamma) \vdash h(\varphi)$, where $h(\Gamma)$ is the list of the images of the members of
$\Gamma$.

The calculus never inspects a symbol.

## Sources

- D. van Dalen, *Logic and Structure*, 5th ed., Springer 2013, §3.1.

Formalized by `Cslib.Logic.FOL.Derivable.mapLHom`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#map-lhom).

## Preimage of a finite set of formulas in its sublanguage

Let $L$ be a first-order
language. For a finite set $F$ of formulas of $L$ with free variables in $\mathbb{N}$, this is
the set of those formulas $\psi_0$ of the sublanguage of $L$ on the symbols occurring in $F$,
with free variables in $\mathbb{N}$, whose image under the inclusion of that sublanguage into
$L$ belongs to $F$.

## Sources

- H.-D. Ebbinghaus, J. Flum, and W. Thomas, *Mathematical Logic*, 2nd ed., Springer 1994, Chapter V.

Formalized by `Cslib.Logic.FOL.subLanguagePreimage`, a definition declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 427](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L427). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#sub-language-preimage).

## Consistency passes to the finite-symbol sublanguage

Let $F$ be a finite set of formulas
of a first-order language $L$ with free variables in $\mathbb{N}$, and let $L_F$ be the
sublanguage of $L$ on the symbols occurring in $F$, with inclusion $\iota : L_F \to L$. If $F$ is
consistent, then so is the preimage of $F$ in $L_F$: the set of formulas $\psi_0$ of $L_F$ with
free variables in $\mathbb{N}$ whose image $\iota(\psi_0)$ under the inclusion belongs to $F$.

A refutation of the preimage maps along the inclusion to a refutation of $F$.

## Sources

- H.-D. Ebbinghaus, J. Flum, and W. Thomas, *Mathematical Logic*, 2nd ed., Springer 1994, Chapter V.

Formalized by `Cslib.Logic.FOL.consistent_subLanguagePreimage`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 433](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L433). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#consistent-sub-language-preimage).

## Symbols of the sublanguage of a finite set of formulas as symbols of the language

Let
$L$ be a first-order language. For a finite set $F$ of formulas of $L$ with free variables in
$\mathbb{N}$, this map sends each function symbol (respectively relation symbol) of the
sublanguage of $L$ on the symbols occurring in $F$ to the same function symbol (respectively
relation symbol) of $L$, with the same arity.

## Sources

- H.-D. Ebbinghaus, J. Flum, and W. Thomas, *Mathematical Logic*, 2nd ed., Springer 1994, Chapter V.

Formalized by `Cslib.Logic.FOL.subLanguageSymbolsTo`, a definition declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 447](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L447). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#sub-language-symbols-to).

## Symbols of a generated sublanguage occur in the generating formulas

Let $L$ be a
first-order language and $F$ a finite set of $L$-formulas with free variables in $\mathbb{N}$. The
map from the symbols of the sublanguage of $L$ on the symbols occurring in $F$ to the symbols of
$L$ sends every symbol of that sublanguage to a symbol occurring in some formula of $F$.

## Sources

- H.-D. Ebbinghaus, J. Flum, and W. Thomas, *Mathematical Logic*, 2nd ed., Springer 1994, Chapter V.

Formalized by `Cslib.Logic.FOL.mem_subLanguageSymbolsTo`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 453](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L453). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#mem-sub-language-symbols-to).

## The symbol map of the sublanguage of a finite set of formulas is injective

Let $L$ be
a first-order language. For every finite set $F$ of formulas of $L$ with free variables in
$\mathbb{N}$, the map sending each symbol of the sublanguage of $L$ on the symbols occurring in
$F$ to the same symbol of $L$ is injective.

## Sources

- H.-D. Ebbinghaus, J. Flum, and W. Thomas, *Mathematical Logic*, 2nd ed., Springer 1994, Chapter V.

Formalized by `Cslib.Logic.FOL.subLanguageSymbolsTo_injective`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 466](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L466). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#sub-language-symbols-to-injective).

## Symbols of the sublanguage as symbols occurring in a finite set of formulas

Let $L$ be
a first-order language. For a finite set $F$ of formulas of $L$ with free variables in
$\mathbb{N}$, this map sends each symbol of the sublanguage of $L$ on the symbols occurring in
$F$ to the same symbol of $L$, regarded as an element of the finite set of symbols occurring in
$F$.

## Sources

- H.-D. Ebbinghaus, J. Flum, and W. Thomas, *Mathematical Logic*, 2nd ed., Springer 1994, Chapter V.

Formalized by `Cslib.Logic.FOL.symEmbed`, a definition declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 492](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L492). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#sym-embed).

## Finite satisfiability

Let $L$ be a first-order language, with no countability hypothesis
on its symbols. Every finite consistent set $F$ of formulas of $L$ with free variables in
$\mathbb{N}$ is satisfiable: there are a nonempty $L$-structure $M$, in the universe of the
function symbols of $L$, and an assignment $v : \mathbb{N} \to M$ under which every formula of $F$
holds.

The proof passes to the sublanguage on the finitely many symbols occurring in $F$, applies the
countable Henkin theorem there, and expands the resulting structure along the inclusion.

## Sources

- H.-D. Ebbinghaus, J. Flum, and W. Thomas, *Mathematical Logic*, 2nd ed., Springer 1994, Chapter V.

Formalized by `Cslib.Logic.FOL.exists_model_of_consistent_finset`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 510](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L510). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#exists-model-of-consistent-finset).

## Model existence for arbitrary languages

Let $L$ be a first-order language, with no
countability hypothesis on its symbols. Every consistent set $S$ of formulas of $L$ with free
variables in $\mathbb{N}$ is satisfiable: there are a nonempty $L$-structure $M$, in the larger of
the universes of the function symbols and the relation symbols of $L$, and an assignment
$v : \mathbb{N} \to M$ under which every formula of $S$ holds.

## Sources

- L. Henkin, *The completeness of the first-order functional calculus*, J. Symbolic Logic 14, 1949, 159-166; H.-D. Ebbinghaus, J. Flum, and W. Thomas, *Mathematical Logic*, 2nd ed., Springer 1994, Chapter V.

Formalized by `Cslib.Logic.FOL.exists_model_of_consistent_general`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 542](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L542). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#exists-model-of-consistent-general).

## Strong completeness for arbitrary languages

Let $L$ be a first-order language whose
function symbols live in universe $u$ and relation symbols in universe $v$, with no restriction
on the number of symbols. Let $S$ be a set of formulas of $L$ and $\varphi$ a formula of $L$,
all with free variables in $\mathbb{N}$. If for every $L$-structure $M$ with carrier in
universe $\max(u, v)$ and every assignment $e : \mathbb{N} \to M$ under which all formulas of
$S$ hold, $\varphi$ also holds under $e$, then $\varphi$ is provable from $S$.

## Sources

- L. Henkin, *The completeness of the first-order functional calculus*, J. Symbolic Logic 14, 1949, 159-166.

Formalized by `Cslib.Logic.FOL.provable_of_entails_general`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 594](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L594). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#provable-of-entails-general).

## Completeness for arbitrary languages

Let $L$ be a first-order language whose function
symbols live in universe $u$ and relation symbols in universe $v$, with no restriction on the
number of symbols. Let $T$ be a theory of $L$ and $\varphi$ a formula of $L$ with free
variables in $\mathbb{N}$. If $\varphi$ holds under every assignment of the variables in every
nonempty model of $T$ whose carrier lies in universe $\max(u, v)$, then $\varphi$ is provable
from the sentences of $T$, viewed as formulas over $\mathbb{N}$.

## Sources

- L. Henkin, *The completeness of the first-order functional calculus*, J. Symbolic Logic 14, 1949, 159-166.

Formalized by `Cslib.Logic.FOL.provable_of_models_general`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 607](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L607). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#provable-of-models-general).

## Soundness and completeness for arbitrary languages

Let $L$ be a first-order language,
with no countability hypothesis, $T$ a theory of $L$ (a set of sentences), and $\varphi$ an
$L$-formula with free variables in $\mathbb{N}$. Then $\varphi$ is provable from the sentences of
$T$, each regarded as a formula with free variables in $\mathbb{N}$, if and only if $\varphi$
holds in every nonempty model of $T$ under every assignment of elements of the model to the
variables in $\mathbb{N}$.

The models range over types in the universe $\max(u, v)$, where $u$ and $v$ are the universe
levels of the function and relation symbols of $L$.

## Sources

- L. Henkin, *The completeness of the first-order functional calculus*, J. Symbolic Logic 14, 1949, 159-166.

Formalized by `Cslib.Logic.FOL.provable_iff_models_general`, a theorem declared in [CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean, line 623](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/CompletenessUncountable.lean#L623). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html#provable-iff-models-general).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gödel's completeness theorem](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/first-order-logic/g-del-s-completeness-theorem)
