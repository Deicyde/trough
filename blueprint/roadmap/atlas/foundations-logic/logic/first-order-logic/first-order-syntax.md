---
declaration: section
origin: cited
lean: FirstOrder.Language.Term.leafCount, FirstOrder.Language.Term.leafCount_relabel, Cslib.Logic.FOL.termSymbols, Cslib.Logic.FOL.formulaSymbols, Cslib.Logic.FOL.instantiateTerm, Cslib.Logic.FOL.instantiate, Cslib.Logic.FOL.instantiateTerm_var_zero, Cslib.Logic.FOL.instantiateTerm_var_succ
statement: formalized
proof: formalized
---

# First-order syntax

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html).

## Leaf count of a first-order term

The number of leaves of a first-order term.

Variables and nullary function applications are leaves. A nonnullary function application has
the sum of the leaf counts of its arguments.

Formalized by `FirstOrder.Language.Term.leafCount`, a definition declared in [MathlibExt/ModelTheory/Term/LeafCount.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/ModelTheory/Term/LeafCount.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html#leaf-count).

## Relabeling variables preserves the leaf count

Relabeling variables does not change the number of leaves.

Formalized by `FirstOrder.Language.Term.leafCount_relabel`, a theorem declared in [MathlibExt/ModelTheory/Term/LeafCount.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/ModelTheory/Term/LeafCount.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html#leaf-count-relabel).

## Symbols of a term

The set of symbols of a first-order language $L$ that occur in a
term $t$ (with free variables and possibly bound variables), defined by recursion on $t$: a
variable contributes no symbols, and $f(t_1, \dots, t_k)$ contributes the function symbol $f$
together with the symbols of the terms $t_i$. The result lies in the set of all symbols of $L$,
but only function symbols can occur in a term.

Formalized by `Cslib.Logic.FOL.termSymbols`, a definition declared in [CSLibExt/Logics/FirstOrder/Symbols.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Symbols.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html#term-symbols).

## Symbols of a formula

The set of function and relation symbols of a first-order
language $L$ that occur in a formula $\varphi$ (with free variables and possibly bound
variables), defined by recursion on $\varphi$: falsum $\bot$ contributes no symbols, an
equation $t_1 = t_2$ contributes the symbols of the terms $t_1$ and $t_2$, an atomic formula
$R(t_1, \dots, t_k)$ contributes $R$ together with the symbols of the terms $t_i$, an
implication $\varphi \to \psi$ contributes the symbols of $\varphi$ and of $\psi$, and
$\forall x\, \varphi$ contributes the symbols of $\varphi$. Variables and the equality sign
contribute nothing.

Formalized by `Cslib.Logic.FOL.formulaSymbols`, a definition declared in [CSLibExt/Logics/FirstOrder/Symbols.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Symbols.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html#formula-symbols).

## Instantiating the outermost bound variable of a term

Let $L$ be a first-order language,
$t$ an $L$-term with free variables in $\alpha$, and $s$ an $L$-term with free variables in
$\alpha$ and $m + 1$ bound variables $0, \dots, m$. The instantiation of $t$ in $s$ is the term
with free variables in $\alpha$ and $m$ bound variables obtained from $s$ by substituting $t$ for
the bound variable $0$, replacing each other bound variable $i + 1$ by $i$, and leaving the free
variables unchanged.

Formalized by `Cslib.Logic.FOL.instantiateTerm`, a definition declared in [CSLibExt/Logics/FirstOrder/Syntax.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Syntax.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html#instantiate-term).

## Instantiating the outermost bound variable of a formula

Let $L$ be a first-order
language, $t$ an $L$-term with free variables in $\alpha$, and $\varphi$ a bounded $L$-formula with
free variables in $\alpha$ and $m + 1$ bound variables $0, \dots, m$. The instantiation of $t$ in
$\varphi$ is the bounded formula with free variables in $\alpha$ and $m$ bound variables obtained
from $\varphi$ by instantiating $t$ in every term of its atomic subformulas: in each term, $t$ is
substituted for the bound variable $0$ and each other bound variable $i + 1$ is replaced by $i$.
Falsum, implication and universal quantification are kept, the quantifier being passed through
unchanged since bound variables are de Bruijn levels.

Formalized by `Cslib.Logic.FOL.instantiate`, a definition declared in [CSLibExt/Logics/FirstOrder/Syntax.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Syntax.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html#instantiate).

## Instantiation at the outermost bound variable

Let $L$ be a first-order language, $t$ an
$L$-term with free variables in $\alpha$, and $m$ a natural number. Instantiating $t$ in the term
consisting of the bound variable $0$ (a term with free variables in $\alpha$ and $m + 1$ bound
variables) gives $t$, regarded as a term with free variables in $\alpha$ and $m$ bound variables.

Formalized by `Cslib.Logic.FOL.instantiateTerm_var_zero`, a theorem declared in [CSLibExt/Logics/FirstOrder/Syntax.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Syntax.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html#instantiate-term-var-zero).

## Instantiation shifts the remaining bound variables down

Let $L$ be a first-order language,
$t$ an $L$-term with free variables in $\alpha$, and $i < m$. Instantiating $t$ in the term
consisting of the bound variable $i + 1$ (a term with free variables in $\alpha$ and $m + 1$ bound
variables) gives the term consisting of the bound variable $i$ (with $m$ bound variables).

Formalized by `Cslib.Logic.FOL.instantiateTerm_var_succ`, a theorem declared in [CSLibExt/Logics/FirstOrder/Syntax.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Syntax.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html#instantiate-term-var-succ).

## Instantiation commutes with the universal quantifier

Let $L$ be a first-order language,
$t$ an $L$-term with free variables in $\alpha$, and $\varphi$ a bounded $L$-formula with free
variables in $\alpha$ and $m + 2$ bound variables. Instantiating $t$ in the universal formula
$\forall \varphi$ (which has $m + 1$ bound variables) gives the universal quantification of the
instantiation of $t$ in $\varphi$.

Under a quantifier the outermost bound variable is still index $0$ (bound variables are de Bruijn
levels), so instantiation passes through the quantifier unchanged.

Formalized by `Cslib.Logic.FOL.instantiate_all`, a theorem declared in [CSLibExt/Logics/FirstOrder/Syntax.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Syntax.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html#instantiate-all).

## Truth of an instance

Let $L$ be a first-order language, $M$ an $L$-structure,
$v : \alpha \to M$ an assignment of the free variables, $t$ an $L$-term with free variables in
$\alpha$, and $\varphi$ a bounded $L$-formula with free variables in $\alpha$ and one bound
variable. Then the instantiation of $t$ in $\varphi$, a formula with free variables in $\alpha$,
holds in $M$ under $v$ if and only if $\varphi$ holds in $M$ under $v$ with its bound variable set
to the value of $t$ under $v$.

Formalized by `Cslib.Logic.FOL.realize_instantiate_formula`, a theorem declared in [CSLibExt/Logics/FirstOrder/Syntax.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Syntax.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html#realize-instantiate-formula).

## Truth of a universal formula

Let $L$ be a first-order language, $M$ an $L$-structure,
$v : \alpha \to M$ an assignment of the free variables, and $\varphi$ a bounded $L$-formula with
free variables in $\alpha$ and one bound variable. Then the formula $\forall \varphi$ holds in $M$
under $v$ if and only if, for every $a \in M$, $\varphi$ holds in $M$ under $v$ with its bound
variable set to $a$.

Formalized by `Cslib.Logic.FOL.realize_all_formula`, a theorem declared in [CSLibExt/Logics/FirstOrder/Syntax.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Syntax.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html#realize-all-formula).

## Truth depends only on the free variables

Let $L$ be a first-order language, $M$ an
$L$-structure, and $\varphi$ a bounded $L$-formula with free variables in $\alpha$ and $n$ bound
variables. If two assignments $v, v' : \alpha \to M$ agree on every free variable of $\varphi$,
then for every choice of values in $M$ for the $n$ bound variables, $\varphi$ holds in $M$ under
$v$ and these values if and only if it holds under $v'$ and these values.

Formalized by `Cslib.Logic.FOL.realize_congr`, a theorem declared in [CSLibExt/Logics/FirstOrder/Syntax.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Syntax.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html#realize-congr).

## Renaming free variables of a term

Given a map $f : \alpha \to \beta$ and
$n \in \mathbb{N}$, a term of a first-order language over the variables
$\alpha \sqcup \mathrm{Fin}\,n$ (free variables from $\alpha$, bound variables from
$\mathrm{Fin}\,n$) becomes a term over $\beta \sqcup \mathrm{Fin}\,n$ by replacing each free
variable $a$ with $f(a)$ and leaving the bound variables unchanged.

Formalized by `Cslib.Logic.FOL.renameTerm`, a definition declared in [CSLibExt/Logics/FirstOrder/Syntax.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Syntax.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html#rename-term).

## Renaming free variables of a formula

Given a map $f : \alpha \to \beta$, a bounded formula
$\varphi$ of a first-order language $L$ with free variables in $\alpha$ and $n$ bound variables
becomes a bounded formula of $L$ with free variables in $\beta$ and the same $n$ bound variables,
by replacing each free variable $a$ with $f(a)$ in every term of $\varphi$ and leaving the bound
variables, the relation symbols and the logical connectives and quantifiers unchanged.

Formalized by `Cslib.Logic.FOL.rename`, a definition declared in [CSLibExt/Logics/FirstOrder/Syntax.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Syntax.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html#rename).

## Truth of a renamed formula

Let $M$ be a structure for a first-order language $L$, let
$f : \alpha \to \beta$, and let $\varphi$ be a bounded formula of $L$ with free variables in
$\alpha$ and $n$ bound variables. For every assignment $v : \beta \to M$ of the free variables
and every assignment $x : \mathrm{Fin}\,n \to M$ of the bound variables, the renaming of
$\varphi$ along $f$ holds in $M$ at $v$ and $x$ if and only if $\varphi$ holds in $M$ at
$v \circ f$ and $x$.

Formalized by `Cslib.Logic.FOL.realize_rename`, a theorem declared in [CSLibExt/Logics/FirstOrder/Syntax.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Syntax.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html#realize-rename).

## Relabeling along $f$ agrees with renaming

Let $f : \alpha \to \beta$ and let $\varphi$
be a bounded formula of a first-order language with free variables in $\alpha$ and $k$ bound
variables. Mathlib's relabeling of $\varphi$ along the map $\alpha \to \beta \sqcup \mathrm{Fin}\,0$
sending $a$ to the free variable $f(a)$ replaces each free variable $a$ by $f(a)$ and produces a
formula with $0 + k$ bound variables. This formula equals the renaming of $\varphi$ along $f$,
regarded as a formula with $0 + k$ bound variables through the inclusion $k \le 0 + k$.

Formalized by `Cslib.Logic.FOL.relabel_inl_comp_eq_castLE_rename`, a theorem declared in [CSLibExt/Logics/FirstOrder/Syntax.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Syntax.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html#relabel-inl-comp-eq-cast-le-rename).

## Relabelling a formula is renaming

Let $L$ be a first-order language and
$f : \alpha \to \beta$ a map. For every $L$-formula $\varphi$ with free variables in $\alpha$ (a
bounded formula with no bound variables), Mathlib's relabelling of $\varphi$ along $f$ equals the
renaming of the free variables of $\varphi$ along $f$.

Formalized by `Cslib.Logic.FOL.formula_relabel_eq_rename`, a theorem declared in [CSLibExt/Logics/FirstOrder/Syntax.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Syntax.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html#formula-relabel-eq-rename).

## Renaming that fixes the free variables

If a map $f : \alpha \to \alpha$ fixes every free
variable of a bounded formula $\varphi$, then renaming the free variables of $\varphi$ along $f$
leaves $\varphi$ unchanged.

Formalized by `Cslib.Logic.FOL.rename_congr`, a theorem declared in [CSLibExt/Logics/FirstOrder/Syntax.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Syntax.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html#rename-congr).

## Free variables of a renamed formula

Let $L$ be a first-order language and
$f : \alpha \to \beta$ a map. For every bounded $L$-formula $\varphi$ with free variables in
$\alpha$ and $n$ bound variables, the set of free variables of the renaming of $\varphi$ along $f$
is the image under $f$ of the set of free variables of $\varphi$.

Formalized by `Cslib.Logic.FOL.freeVarFinset_rename`, a theorem declared in [CSLibExt/Logics/FirstOrder/Syntax.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/FirstOrder/Syntax.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html#free-var-finset-rename).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: First-order syntax](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-syntax/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/first-order-logic/first-order-syntax)
