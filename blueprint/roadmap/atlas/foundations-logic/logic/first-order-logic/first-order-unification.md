---
declaration: section
origin: cited
lean: Cslib.Unification.Term, Cslib.Unification.Subst, Cslib.Unification.Term.subst, Cslib.Unification.Term.size, Cslib.Unification.Term.vars, Cslib.Unification.Term.subst_congr, Cslib.Unification.Term.exists_of_mem_vars_subst, Cslib.Unification.Term.vars_subset_vars_subst
statement: formalized
proof: formalized
---

# First-order unification

33 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html).

## Terms for unification

For a type $C$ of constants, a term over $C$ is either a variable
$x$, indexed by a natural number $x \in \mathbb{N}$, or a constant $c \in C$, or a binary node
built from two terms $l$ and $r$.

Formalized by `Cslib.Unification.Term`, an inductive type declared in [CSLibExt/Foundations/Unification/Basic.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#term).

## Substitution

A substitution is a map assigning a term to every variable, that is, a
function from the set $\mathbb{N}$ of variables to terms.

Formalized by `Cslib.Unification.Subst`, an abbreviation declared in [CSLibExt/Foundations/Unification/Basic.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#subst).

## Applying a substitution to a term

For a substitution $\sigma$ and a term $t$, the term
$t\sigma$ is obtained from $t$ by replacing every variable $x$ by $\sigma(x)$: a variable $x$
becomes $\sigma(x)$, a constant is unchanged, and a node with subterms $l$ and $r$ becomes the
node with subterms $l\sigma$ and $r\sigma$.

Formalized by `Cslib.Unification.Term.subst`, a definition declared in [CSLibExt/Foundations/Unification/Basic.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#subst-2).

## Size of a term

The size of a term is the number of symbols in it: a variable and a
constant have size $1$, and a node with subterms $l$ and $r$ has size equal to the size of $l$
plus the size of $r$ plus $1$.

Formalized by `Cslib.Unification.Term.size`, a definition declared in [CSLibExt/Foundations/Unification/Basic.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#size).

## Variables of a term

The variables of a term form a finite set of natural numbers,
defined recursively: the variable $x$ has the variable set $\{x\}$, a constant has no variables,
and the variables of a node with subterms $l$ and $r$ are those of $l$ together with those of
$r$.

Formalized by `Cslib.Unification.Term.vars`, a definition declared in [CSLibExt/Foundations/Unification/Basic.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#vars).

## Substitution depends only on the variables of the term

If two substitutions $\sigma$
and $\tau$ agree on every variable occurring in a term $u$, then applying $\sigma$ to $u$ gives
the same term as applying $\tau$ to $u$.

Formalized by `Cslib.Unification.Term.subst_congr`, a theorem declared in [CSLibExt/Foundations/Unification/Basic.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#subst-congr).

## Variables of a substituted term

Let $s$ be a substitution and $t$ a term. Every
variable of the term obtained by applying $s$ to $t$ is a variable of $s(y)$ for some variable
$y$ of $t$.

Formalized by `Cslib.Unification.Term.exists_of_mem_vars_subst`, a theorem declared in [CSLibExt/Foundations/Unification/Basic.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#exists-of-mem-vars-subst).

## Variables of a substituted variable occur in the substituted term

For every
substitution $s$, term $t$ and variable $y$ occurring in $t$, every variable of the term $s(y)$
occurs in the term obtained from $t$ by applying $s$.

Formalized by `Cslib.Unification.Term.vars_subset_vars_subst`, a theorem declared in [CSLibExt/Foundations/Unification/Basic.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#vars-subset-vars-subst).

## Occurs check: size bound

Let $x$ be a variable and $t$ a term in which $x$ occurs, with
$t$ not the variable $x$ itself. Then for every substitution $\sigma$, the term $\sigma(x)$ has
strictly smaller size than $t\sigma$, the result of applying $\sigma$ to $t$.

Consequently the equation $x = t$ has no unifier when $x$ occurs in $t$ and $t \ne x$ (the occurs
check).

Formalized by `Cslib.Unification.Term.size_subst_lt_of_mem`, a theorem declared in [CSLibExt/Foundations/Unification/Basic.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#size-subst-lt-of-mem).

## Substituting for a variable that does not occur in the substituted term

Let $x$ be a
variable and $t$ a term in which $x$ does not occur. For every term $u$, every variable of the
term obtained from $u$ by replacing each occurrence of $x$ with $t$ is a variable of $u$ or of
$t$, and is different from $x$.

Formalized by `Cslib.Unification.Term.vars_subst_single_subset`, a theorem declared in [CSLibExt/Foundations/Unification/Basic.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#vars-subst-single-subset).

## Composition of substitutions on first-order terms

For substitutions $s$ and $t$,
the composite $s \gg t$ (first $s$, then $t$) sends each variable $x$ to the term obtained
from $s(x)$ by applying $t$ to every variable of $s(x)$.

Formalized by `Cslib.Unification.Subst.comp`, a definition declared in [CSLibExt/Foundations/Unification/Basic.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#comp).

## Single-variable substitution on first-order terms

For a variable $x$ and a term $t$, the
substitution $[x \mapsto t]$ sends $x$ to $t$ and every other variable $y$ to the term $y$.

Formalized by `Cslib.Unification.Subst.single`, a definition declared in [CSLibExt/Foundations/Unification/Basic.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#single).

## Absorbing a single-variable substitution

Let $x$ be a variable, $t$ a term, and
$[x \mapsto t]$ the substitution replacing $x$ by $t$ and fixing every other variable. If a
substitution $\sigma$ satisfies $\sigma(x) = t\sigma$, where $t\sigma$ is the result of applying
$\sigma$ to $t$, then the composite substitution that applies $[x \mapsto t]$ first and
$\sigma$ second equals $\sigma$.

Formalized by `Cslib.Unification.Subst.single_comp_eq`, a theorem declared in [CSLibExt/Foundations/Unification/Basic.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#single-comp-eq).

## A term is fixed by substituting it for a variable it avoids

If the variable $x$ does
not occur in the term $t$, then applying to $t$ the substitution $[x \mapsto t]$, which replaces
$x$ by $t$ and fixes every other variable, leaves $t$ unchanged.

Formalized by `Cslib.Unification.Subst.subst_single_of_not_mem`, a theorem declared in [CSLibExt/Foundations/Unification/Basic.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#subst-single-of-not-mem).

## Lists of equations

A list of equations over constants $C$ is a finite list of pairs
$(t, u)$ of terms over $C$, each pair standing for the equation $t = u$.

Formalized by `Cslib.Unification.Equations`, an abbreviation declared in [CSLibExt/Foundations/Unification/Basic.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#equations).

## Unifier of a list of equations

A substitution $s$ unifies a list $E$ of equations
between terms when, for every equation $(t, u)$ in $E$, applying $s$ to $t$ and applying $s$ to
$u$ give the same term.

Formalized by `Cslib.Unification.Unifies`, a definition declared in [CSLibExt/Foundations/Unification/Basic.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#unifies).

## Most general unifier

A substitution $s$ is a most general unifier of a list of
equations $E$ when $s$ unifies $E$ and every unifier $s'$ of $E$ factors through $s$, that is,
$s' = s \gg r$ for some substitution $r$, where $s \gg r$ applies first $s$ and then $r$.

Formalized by `Cslib.Unification.IsMGU`, a definition declared in [CSLibExt/Foundations/Unification/Basic.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#is-mgu).

## Applying a substitution to a list of equations

For a substitution $\sigma$ and a list
$E$ of equations between terms, the result is the list obtained by replacing each equation
$u = v$ of $E$, in order, by $u\sigma = v\sigma$, where $u\sigma$ is the result of applying
$\sigma$ to $u$.

Formalized by `Cslib.Unification.substEqs`, a definition declared in [CSLibExt/Foundations/Unification/Basic.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#subst-eqs).

## Variables of a list of equations

The variables of a list of equations form the finite
set of all variables that occur on either side of any of its equations.

Formalized by `Cslib.Unification.eqVars`, a definition declared in [CSLibExt/Foundations/Unification/Basic.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#eq-vars).

## Total size of a list of equations

The total size of a list of equations is the sum,
over all its equations, of the sizes of the two sides, where the size of a term is its number
of variable, constant and node symbols.

Formalized by `Cslib.Unification.eqSize`, a definition declared in [CSLibExt/Foundations/Unification/Basic.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#eq-size).

## Eliminating a solved variable lowers the number of variables

Let $x$ be a variable,
$t$ a term in which $x$ does not occur, and $E$ a list of equations. Applying the substitution
that replaces $x$ by $t$ (and fixes every other variable) to both sides of every equation of
$E$ gives a list of equations with strictly fewer distinct variables than the list obtained
by putting the equation $x = t$ in front of $E$.

Formalized by `Cslib.Unification.card_eqVars_elim_lt`, a theorem declared in [CSLibExt/Foundations/Unification/Basic.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#card-eq-vars-elim-lt).

## Martelli–Montanari unification

The algorithm takes a list of equations between terms and
returns a substitution or fails. On the empty list it returns the identity substitution.
Otherwise it looks at the first equation $t = u$ and the remaining list $E$. If $t$ and $u$ are
the same variable, or the same constant, the equation is dropped and the algorithm continues on
$E$; if they are two different constants, it fails. If $t$ is a variable $x$ and $u \ne x$, or
else $u$ is a variable $x$ and $t$ is not a variable, let $v$ be the other side: the algorithm
fails when $x$ occurs in $v$, and otherwise substitutes $v$ for $x$ on both sides of every
equation of $E$ and unifies the result; if that returns $s$, it returns the substitution that
applies first the replacement of $x$ by $v$ and then $s$, and if that fails, it fails. If $t$ and
$u$ are nodes with children $l_1, r_1$ and $l_2, r_2$, it continues on the list $l_1 = l_2$,
$r_1 = r_2$ followed by $E$. If one side is a constant and the other a node, it fails.

Formalized by `Cslib.Unification.unify`, a definition declared in [CSLibExt/Foundations/Unification/Basic.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#unify).

## Specification of a unification result

Let $E$ be a list of equations between terms and
$r$ either a substitution or failure. The specification holds for $E$ and $r$ when, if $r$ is a
substitution $s$, then $s$ unifies $E$ and every substitution $s'$ that unifies $E$ equals the
composite substitution that applies first $s$ and then $s'$; and, if $r$ is failure, then no
substitution unifies $E$.

Formalized by `Cslib.Unification.UnifySpec`, a definition declared in [CSLibExt/Foundations/Unification/Basic.lean, line 404](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L404). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#unify-spec).

## Lists of equations with the same unifiers satisfy the same specification

Let $E$ and
$E'$ be lists of equations such that a substitution unifies $E$ exactly when it unifies $E'$.
If an optional substitution $r$ satisfies the unification specification for $E'$ (a returned
substitution $s$ unifies the list and every unifier $s'$ of it satisfies $s' = s \gg s'$,
where $s \gg s'$ applies first $s$ and then $s'$, and failure means the list has no unifier),
then $r$ satisfies the unification specification for $E$.

Formalized by `Cslib.Unification.UnifySpec.congr`, a theorem declared in [CSLibExt/Foundations/Unification/Basic.lean, line 410](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L410). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#congr).

## Failure is correct when the first equation has no unifier

Let $E$ be a list of
equations between terms and let $u = v$ be a further equation, where $u\sigma$ denotes the
result of applying a substitution $\sigma$ to $u$. If $u\sigma \ne v\sigma$ for every
substitution $\sigma$, then returning no substitution meets the unification specification for
the list obtained by putting $u = v$ in front of $E$: no substitution unifies that list.

Formalized by `Cslib.Unification.UnifySpec.none_of_head`, a theorem declared in [CSLibExt/Foundations/Unification/Basic.lean, line 418](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L418). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#none-of-head).

## The elimination step preserves the unification specification

Let $x$ be a variable,
$t$ a term in which $x$ does not occur, $e$ an equation and $E$ a list of equations. Suppose
that for every substitution $s$, the two sides of $e$ become equal under $s$ exactly when
$s(x)$ equals the result of applying $s$ to $t$. Let $\sigma$ be the substitution that replaces
$x$ by $t$ and fixes every other variable, and let $E'$ be the list obtained by applying
$\sigma$ to both sides of every equation of $E$. Suppose an optional substitution $r$ satisfies
the unification specification for $E'$. Define the result $r'$ by: when $r$ returns a
substitution $s$, $r'$ returns $\sigma \gg s$, the composite that applies first $\sigma$ and
then $s$; when $r$ is failure, $r'$ is failure. Then $r'$ satisfies the unification
specification for the list with head $e$ and tail $E$.

Formalized by `Cslib.Unification.UnifySpec.elim`, a theorem declared in [CSLibExt/Foundations/Unification/Basic.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#elim).

## Soundness of unification

For every list $E$ of equations between terms, if the
Martelli–Montanari algorithm returns a substitution $s$ on $E$, then $s$ unifies $E$: applying
$s$ to the two sides of any equation of $E$ gives the same term.

Formalized by `Cslib.Unification.unifies_unify`, a theorem declared in [CSLibExt/Foundations/Unification/Basic.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#unifies-unify).

## Most generality of unification

For every list $E$ of equations between terms, if the
Martelli–Montanari algorithm returns a substitution $s$ on $E$, then every substitution $s'$
that unifies $E$ equals the composite substitution that applies first $s$ and then $s'$.

Formalized by `Cslib.Unification.unify_eq_some_comp`, a theorem declared in [CSLibExt/Foundations/Unification/Basic.lean, line 506](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L506). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#unify-eq-some-comp).

## Unification returns a most general unifier

If the Martelli-Montanari unification
algorithm, run on a list of equations $E$, returns a substitution $s$, then $s$ is a most
general unifier of $E$.

Formalized by `Cslib.Unification.isMGU_unify`, a theorem declared in [CSLibExt/Foundations/Unification/Basic.lean, line 511](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L511). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#is-mgu-unify).

## Unification returns an idempotent substitution

For every list $E$ of equations between
terms, if the Martelli–Montanari algorithm returns a substitution $s$ on $E$, then $s$ is
idempotent: the composite substitution that applies first $s$ and then $s$ equals $s$.

Formalized by `Cslib.Unification.unify_comp_self`, a theorem declared in [CSLibExt/Foundations/Unification/Basic.lean, line 515](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L515). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#unify-comp-self).

## Completeness of unification

For every list $E$ of equations between terms, the
Martelli–Montanari algorithm fails on $E$ if and only if no substitution unifies $E$.

Formalized by `Cslib.Unification.unify_eq_none_iff`, a theorem declared in [CSLibExt/Foundations/Unification/Basic.lean, line 519](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L519). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#unify-eq-none-iff).

## The elimination step of unification introduces no variables

Write $V(F)$ for the set
of variables of a list $F$ of equations. Let $x_0$ be a variable, $t$ a term in which $x_0$ does
not occur, $e = (e_1, e_2)$ an equation such that every variable of $t$ occurs in $e_1$ or $e_2$,
and $E$ a list of equations, and let $E'$ be obtained from $E$ by substituting $t$ for $x_0$ on
both sides of every equation. Let $s_0$ be a substitution such that, for every variable $x$,
every variable of $s_0(x)$ is $x$ or lies in $V(E')$, and let $\sigma$ be the substitution that
applies first the replacement of $x_0$ by $t$ and then $s_0$. Then for every variable $x$, every
variable of $\sigma(x)$ is $x$, occurs in $e_1$ or $e_2$, or lies in $V(E)$.

Formalized by `Cslib.Unification.vars_single_comp_subset`, a theorem declared in [CSLibExt/Foundations/Unification/Basic.lean, line 533](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L533). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#vars-single-comp-subset).

## Unification introduces no new variables

Let $E$ be a list of equations between terms.
If the unification algorithm succeeds on $E$ and returns the substitution $s$, then for every
variable $x$, each variable of the term $s(x)$ is either $x$ itself or a variable occurring in
some equation of $E$.

Formalized by `Cslib.Unification.vars_unify_subset`, a theorem declared in [CSLibExt/Foundations/Unification/Basic.lean, line 561](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Unification/Basic.lean#L561). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html#vars-unify-subset).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: First-order unification](https://deicyde.github.io/atlas-lean/roadmap/Logic/first-order-logic/first-order-unification/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/first-order-logic/first-order-unification)
