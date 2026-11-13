---
declaration: section
origin: cited
lean: Cslib.HindleyMilner.Expr, Cslib.HindleyMilner.Ty, Cslib.HindleyMilner.Scheme, Cslib.HindleyMilner.toScheme, Cslib.HindleyMilner.Scheme.eval, Cslib.HindleyMilner.Scheme.inst, Cslib.HindleyMilner.Scheme.substTy, Cslib.HindleyMilner.inst_substTy
statement: formalized
proof: formalized
---

# Hindley–Milner type inference

45 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html).

## Expressions of the λ-calculus with let

An expression is a variable $x$, an application
$e_1\,e_2$, an abstraction $\lambda x.\, e$, or a let-binding
$\mathsf{let}\ x = e_1\ \mathsf{in}\ e_2$, where $e$, $e_1$, $e_2$ are expressions and variable
names $x$ are strings.

Formalized by `Cslib.HindleyMilner.Expr`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#expr).

## Monotypes

A monotype over a set $B$ of base types is a term over the constants $B$: a
type variable $\alpha \in \mathbb{N}$, a base type $b \in B$, or an arrow $\tau_1 \to \tau_2$ of
two monotypes (a binary node).

Formalized by `Cslib.HindleyMilner.Ty`, an abbreviation declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#ty).

## Type schemes

A type scheme over base types $B$ is a term over the constant set
$B \oplus \mathbb{N}$: its variables $\alpha \in \mathbb{N}$ are the free type variables, a constant
$\mathrm{inl}\, b$ is the base type $b \in B$, a constant $\mathrm{inr}\, i$ is the bound variable
$i$, and a node of two schemes is an arrow.

Formalized by `Cslib.HindleyMilner.Scheme`, an abbreviation declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#scheme).

## Monotypes as type schemes

Every monotype $\tau$ is read as the type scheme with no bound
variables of the same shape: a type variable stays the same type variable, a base type $b$
becomes the constant $\mathrm{inl}\, b$, and an arrow $\tau_1 \to \tau_2$ becomes the arrow of the
images of $\tau_1$ and $\tau_2$.

Formalized by `Cslib.HindleyMilner.toScheme`, a definition declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#to-scheme).

## Evaluation of a type scheme

Given maps $f$ and $g$ from natural numbers to monotypes
over $B$, a type scheme $\sigma$ over $B$ evaluates to the monotype obtained by replacing each
free type variable $x$ of $\sigma$ by $f(x)$ and each bound variable $i$ by $g(i)$, keeping
every base type $b$ unchanged. An arrow $\sigma_1 \to \sigma_2$ evaluates to the arrow from the
evaluation of $\sigma_1$ to the evaluation of $\sigma_2$.

Formalized by `Cslib.HindleyMilner.Scheme.eval`, a definition declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#eval).

## Instantiation of a type scheme

Given monotypes $(t_i)_{i \in \mathbb{N}}$, the instance of
a scheme $\sigma$ at $(t_i)$ is the monotype obtained from $\sigma$ by replacing each bound
variable $i$ by $t_i$, keeping its free type variables and base types unchanged.

Formalized by `Cslib.HindleyMilner.Scheme.inst`, a definition declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#inst).

## Applying a type substitution to a scheme

For a type substitution $s$ and a type
scheme $\sigma$, $s\sigma$ is the scheme obtained from $\sigma$ by replacing every free type
variable $x$ with the monotype $s(x)$, read as a scheme with no bound variables. The bound
variables of $\sigma$ are left unchanged.

Formalized by `Cslib.HindleyMilner.Scheme.substTy`, a definition declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#subst-ty).

## Instantiation commutes with substitution

For every type substitution $s$, every scheme
$\sigma$ and all monotypes $(t_i)_{i \in \mathbb{N}}$, instantiating each bound variable $i$ of
$s(\sigma)$ by $s(t_i)$ gives $s$ applied to the instance of $\sigma$ at $(t_i)$. Here $s$ acts on
a scheme through its free type variables only.

Formalized by `Cslib.HindleyMilner.inst_substTy`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#inst-subst-ty).

## Substitution into a scheme depends only on its free variables

If two type
substitutions $s$ and $t$ satisfy $s(x) = t(x)$ for every free type variable $x$ of a type
scheme $\sigma$, then applying $s$ to $\sigma$ gives the same scheme as applying $t$.

Formalized by `Cslib.HindleyMilner.substTy_congr`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#subst-ty-congr).

## Typing context

A typing context over base types $B$ is a finite list of bindings
$(x, \sigma)$, each pairing a name $x$ (a string) with a type scheme $\sigma$ over $B$. A name
may be bound more than once; the first binding of a name in the list is the visible one.

Formalized by `Cslib.HindleyMilner.Ctx`, an abbreviation declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#ctx).

## Context lookup

The lookup of a name $x$ in a typing context $\Gamma$ is the scheme of the
first binding of $x$ in $\Gamma$ (the visible one), or nothing if $\Gamma$ has no binding of $x$.

Formalized by `Cslib.HindleyMilner.Ctx.lookup`, a definition declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#lookup).

## Free type variables of a name's visible scheme

For a typing context $\Gamma$ and a
name $x$, this is the set of free type variables of the scheme that $\Gamma$ binds to $x$ (the
first binding of $x$ in $\Gamma$), or the empty set if $\Gamma$ does not bind $x$.

Formalized by `Cslib.HindleyMilner.Ctx.visibleVars`, a definition declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#visible-vars).

## Free type variables of a context

The free type variables of a typing context $\Gamma$
are the type variables occurring free in the visible scheme of some name bound in $\Gamma$.

A binding shadowed by an earlier binding of the same name does not count, so the free type
variables of $\Gamma$ depend only on the visible scheme of each name.

Formalized by `Cslib.HindleyMilner.Ctx.ftv`, a definition declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#ftv).

## Free type variables depend only on visible bindings

If two typing contexts $\Gamma$ and
$\Gamma'$ give every name $x$ the same visible scheme (or both bind no scheme to $x$), then
$\Gamma$ and $\Gamma'$ have the same free type variables.

Formalized by `Cslib.HindleyMilner.Ctx.ftv_congr`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#ftv-congr).

## Applying a type substitution to a context

For a type substitution $s$ and a typing
context $\Gamma$, $s\Gamma$ is the context obtained by applying $s$ to the scheme of every binding
of $\Gamma$, keeping the names and their order.

Formalized by `Cslib.HindleyMilner.Ctx.subst`, a definition declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#subst).

## Substitutions agreeing on a context give the same lookups

If two type substitutions $s$
and $t$ agree on every free type variable of a context $\Gamma$, then for every name $x$ the
lookups of $x$ in $s(\Gamma)$ and in $t(\Gamma)$ are equal: both give no scheme, or both give the
same scheme.

Formalized by `Cslib.HindleyMilner.Ctx.lookup_subst_congr`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#lookup-subst-congr).

## Generalization of a monotype

Given a typing context $\Gamma$ and a monotype $\tau$, the
generalization of $\tau$ with respect to $\Gamma$ is the type scheme obtained from $\tau$ by
turning each type variable $\alpha$ that is not free in $\Gamma$ into the bound variable with
index $\alpha$, while type variables free in $\Gamma$ stay free.

Formalized by `Cslib.HindleyMilner.gen`, a definition declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#gen).

## Hindley–Milner typing

The syntax-directed Damas–Milner typing relation
$\Gamma \vdash e : \tau$ between a context $\Gamma$, an expression $e$ and a monotype $\tau$ is the
least relation closed under the following rules, where $\Gamma, x : \sigma$ is $\Gamma$ extended
by the binding $x : \sigma$ in front.

- Variable: if the lookup of $x$ in $\Gamma$ gives the scheme $\sigma$, then
  $\Gamma \vdash x : \tau$ for every instance $\tau$ of $\sigma$, obtained by replacing each bound
  variable $i$ of $\sigma$ by a monotype $t_i$.
- Application: if $\Gamma \vdash e_1 : \tau_1 \to \tau_2$ and $\Gamma \vdash e_2 : \tau_1$, then
  $\Gamma \vdash e_1\, e_2 : \tau_2$.
- Abstraction: if $\Gamma, x : \tau_1 \vdash e : \tau_2$, with $\tau_1$ bound as a scheme without
  bound variables, then $\Gamma \vdash \lambda x.\, e : \tau_1 \to \tau_2$.
- Let: if $\Gamma \vdash e_1 : \tau_1$ and $\Gamma, x : \mathrm{gen}_\Gamma(\tau_1) \vdash e_2 :
  \tau_2$, then $\Gamma \vdash \mathtt{let}\ x = e_1\ \mathtt{in}\ e_2 : \tau_2$, where
  $\mathrm{gen}_\Gamma(\tau_1)$ binds the type variables of $\tau_1$ that are not free in
  $\Gamma$.

Formalized by `Cslib.HindleyMilner.HasType`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#has-type).

## More general type scheme

A scheme $\sigma'$ is more general than a scheme $\sigma$ when
every instance of $\sigma$ is also an instance of $\sigma'$ and every free type variable of
$\sigma'$ is a free type variable of $\sigma$.

Formalized by `Cslib.HindleyMilner.Scheme.MoreGeneral`, a definition declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#more-general).

## More general context

A context $\Gamma'$ is more general than a context $\Gamma$ when the
same names are visible in both and, for each such name $x$, the visible scheme of $x$ in $\Gamma'$
is more general than its visible scheme in $\Gamma$. Only lookups matter, so shadowed bindings
play no role.

Formalized by `Cslib.HindleyMilner.Ctx.MoreGeneral`, a definition declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#more-general-2).

## Contexts with the same lookups are related by generality

If two typing contexts
$\Gamma'$ and $\Gamma$ give the same lookup result for every name $x$ (the same visible scheme,
or none in both), then $\Gamma'$ is more general than $\Gamma$.

Since the hypothesis is symmetric, $\Gamma$ is then also more general than $\Gamma'$.

Formalized by `Cslib.HindleyMilner.Ctx.MoreGeneral.of_lookup_eq`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#of-lookup-eq).

## Extending more general contexts by a binding

Let $\Gamma'$ and $\Gamma$ be typing
contexts such that $\Gamma'$ is more general than $\Gamma$, let $x$ be a name, and let $\sigma'$
and $\sigma$ be type schemes such that $\sigma'$ is more general than $\sigma$. Then the context
obtained by putting the binding $x : \sigma'$ in front of $\Gamma'$ is more general than the
context obtained by putting the binding $x : \sigma$ in front of $\Gamma$.

Formalized by `Cslib.HindleyMilner.Ctx.MoreGeneral.cons`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#cons).

## Generalizing in a context with fewer free variables

Let $\Gamma'$ and $\Gamma$ be typing
contexts such that every free type variable of $\Gamma'$ is a free type variable of $\Gamma$, and
let $\tau$ be a monotype. Then the generalization of $\tau$ with respect to $\Gamma'$ is more
general than the generalization of $\tau$ with respect to $\Gamma$.

Formalized by `Cslib.HindleyMilner.gen_moreGeneral`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#gen-more-general).

## Typing is preserved in more general contexts

If $\Gamma \vdash e : \tau$ and $\Gamma'$ is
a context more general than $\Gamma$, then $\Gamma' \vdash e : \tau$.

Formalized by `Cslib.HindleyMilner.HasType.mono`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#mono).

## Strict upper bound of a finite set of naturals

For a finite set $S$ of natural numbers,
this is the number $\max S + 1$, where the maximum of the empty set is taken to be $0$. It is
strictly greater than every element of $S$.

Formalized by `Cslib.HindleyMilner.above`, a definition declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 410](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L410). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#above).

## Renaming step of the substitution lemma

Let $\Gamma$ be a typing context, $\tau$ a
monotype and $s$ a type substitution. Write $s\Gamma$ for the context obtained by applying $s$ to
every scheme of $\Gamma$, and let $N$ be one more than the largest free type variable of
$s\Gamma$, with $N = 1$ if $s\Gamma$ has none. Let $\rho$ be the substitution sending a type
variable $y$ to $s(y)$ if $y$ is free in $\Gamma$, and to the type variable $y + N$ otherwise.
Then the generalization of $\rho(\tau)$ with respect to $s\Gamma$ is more general than the scheme
obtained by applying $s$ to the free type variables of the generalization of $\tau$ with respect
to $\Gamma$.

Formalized by `Cslib.HindleyMilner.gen_subst_moreGeneral`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#gen-subst-more-general).

## Hindley–Milner typing is stable under type substitution

Let $\Gamma$ be a typing
context, $e$ an expression and $\tau$ a monotype with $\Gamma \vdash e : \tau$. Then for every
type substitution $s$, $s\Gamma \vdash e : s\tau$, where $s\Gamma$ applies $s$ to every scheme of
$\Gamma$ and $s\tau$ applies $s$ to $\tau$.

Formalized by `Cslib.HindleyMilner.HasType.subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 447](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L447). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#subst-2).

## Typing inversion for variables

Let $\Gamma$ be a typing context, $x$ a name and $\tau$ a
monotype. Then $\Gamma \vdash x : \tau$ holds for the variable expression $x$ if and only if
there are a type scheme $\sigma$ and monotypes $(t_i)_{i \in \mathbb{N}}$ such that the lookup of
$x$ in $\Gamma$ gives $\sigma$ and $\tau$ is the instance of $\sigma$ at $(t_i)$.

Formalized by `Cslib.HindleyMilner.hasType_var_iff`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 476](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L476). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#has-type-var-iff).

## No monotype is an arrow out of itself

For all monotypes $\tau_1$ and $\tau_2$,
$\tau_1 \ne (\tau_1 \to \tau_2)$.

Formalized by `Cslib.HindleyMilner.ne_node_self_left`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 517](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L517). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#ne-node-self-left).

## The abstraction $\lambda f.\, f\, f$ has no type

For every typing context $\Gamma$,
every variable name $f$ and every monotype $\tau$, the judgment
$\Gamma \vdash \lambda f.\, f\, f : \tau$ does not hold.

The λ-bound variable $f$ is monomorphic, so it cannot be applied to itself.

Formalized by `Cslib.HindleyMilner.not_hasType_lam_self_app`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 523](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L523). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#not-has-type-lam-self-app).

## `let` generalizes

For every typing context $\Gamma$, all variable names $f$ and $x$, and
every type variable $\alpha$, the expression $\mathtt{let}\ f = \lambda x.\, x\ \mathtt{in}\ f\, f$
has type $\alpha \to \alpha$ in $\Gamma$.

Formalized by `Cslib.HindleyMilner.hasType_let_id_app_id`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean, line 537](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Typing.lean#L537). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#has-type-let-id-app-id).

## The let rule under a type substitution

Let $\Gamma$ be a typing context, $s$ a type
substitution, $x$ a variable name, $e_1, e_2$ expressions and $\tau_1, \tau_2$ monotypes, and
write $s\Gamma$ for the context obtained by applying $s$ to every type scheme of $\Gamma$.
Suppose $e_1$ has type $\tau_1$ in $\Gamma$, and $e_2$ has type $\tau_2$ in the context
obtained from $s\Gamma$ by binding $x$, in front, to the type scheme that results from
applying $s$ to the generalization of $\tau_1$ in $\Gamma$. Then
$\mathtt{let}\ x = e_1\ \mathtt{in}\ e_2$ has type $\tau_2$ in $s\Gamma$.

Formalized by `Cslib.HindleyMilner.HasType.let_substTy`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/AlgorithmW.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/AlgorithmW.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#let-subst-ty).

## Bound-variable supremum of a type scheme

The bound-variable supremum of a type scheme
$\sigma$ is one more than the largest index $i$ of a bound variable occurring in $\sigma$, and
$0$ if no bound variable occurs in $\sigma$.

Formalized by `Cslib.HindleyMilner.Scheme.boundSup`, a definition declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/AlgorithmW.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/AlgorithmW.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#bound-sup).

## Algorithm W

Given a typing context $\Gamma$, an expression $e$ and a counter $n$,
Algorithm W either fails or returns a substitution, a monotype and a new counter; type variables
$\alpha_m$ with $m \ge n$ serve as fresh. Write $\tau_1 \to \tau_2$ for the arrow type, $s\Gamma$
for $\Gamma$ with the substitution $s$ applied to every type scheme, and $s(\tau)$ for $s$
applied to a monotype $\tau$. Algorithm W is defined by recursion on $e$, and fails as soon
as a recursive call or a unification fails:

- For a variable $x$: if $x$ is unbound in $\Gamma$, W fails; otherwise, with $\sigma$ the
  visible type scheme of $x$, W returns the identity substitution, the instance of $\sigma$
  that replaces each bound variable $i$ by $\alpha_{n+i}$, and the counter $n + k$, where $k$
  is one more than the largest bound-variable index of $\sigma$ ($0$ if it has none).
- For $\lambda x.\, e'$: W runs on the context $\Gamma$ with $x$ bound in front to the
  monotype $\alpha_n$, the body $e'$ and the counter $n + 1$; if this returns
  $(s, \tau, n')$, W returns $(s, s(\alpha_n) \to \tau, n')$.
- For an application $e_1\, e_2$: W runs on $\Gamma$, $e_1$, $n$, giving
  $(s_1, \tau_1, n_1)$, then on $s_1\Gamma$, $e_2$, $n_1$, giving $(s_2, \tau_2, n_2)$, then
  runs unification on the single equation $s_2(\tau_1) = \tau_2 \to \alpha_{n_2}$, giving
  $s_3$; it returns the composite substitution applying $s_1$, then $s_2$, then $s_3$, the
  type $s_3(\alpha_{n_2})$ and the counter $n_2 + 1$.
- For $\mathtt{let}\ x = e_1\ \mathtt{in}\ e_2$: W runs on $\Gamma$, $e_1$, $n$, giving
  $(s_1, \tau_1, n_1)$, then on the context $s_1\Gamma$ with $x$ bound in front to the
  generalization of $\tau_1$ in $s_1\Gamma$, $e_2$ and $n_1$, giving $(s_2, \tau_2, n_2)$;
  it returns the composite substitution applying $s_1$ then $s_2$, the type $\tau_2$ and the
  counter $n_2$.

Formalized by `Cslib.HindleyMilner.W`, a definition declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/AlgorithmW.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/AlgorithmW.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#w).

## Type inference for closed expressions

Type inference on an expression $e$ runs
Algorithm W on $e$ in the empty context with fresh-variable counter $0$. If W succeeds with a
substitution $s$, a monotype $\tau$ and a counter $n'$, the inferred type of $e$ is $\tau$;
if W fails, $e$ has no inferred type.

Formalized by `Cslib.HindleyMilner.infer`, a definition declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/AlgorithmW.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/AlgorithmW.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#infer).

## Soundness of Algorithm W

Let $\Gamma$ be a typing context, $e$ an expression and $n$ a
natural number. If Algorithm W, run on $\Gamma$ and $e$ with fresh-variable counter $n$,
succeeds and returns a substitution $s$, a monotype $\tau$ and a counter $n'$, then $e$ has
type $\tau$ in the context $s\Gamma$ obtained by applying $s$ to every type scheme of
$\Gamma$.

Formalized by `Cslib.HindleyMilner.hasType_of_W_eq_some`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/AlgorithmW.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/AlgorithmW.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#has-type-of-w-eq-some).

## Soundness of type inference for closed expressions

For every expression $e$ and
monotype $\tau$, if type inference for closed expressions returns $\tau$ on $e$, then $e$ has
type $\tau$ in the empty context.

Formalized by `Cslib.HindleyMilner.hasType_of_infer_eq_some`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/AlgorithmW.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/AlgorithmW.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#has-type-of-infer-eq-some).

## Variables below a bound

A term $t$ has all its variables below $n$ when every variable
$z$ occurring in $t$ satisfies $z < n$.

Formalized by `Cslib.HindleyMilner.VarsBelow`, a definition declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Completeness.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Completeness.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#vars-below).

## Freshness invariants of Algorithm W

Let $\Gamma$ be a typing context and $n$ a
natural number such that every free type variable of $\Gamma$ is less than $n$. If Algorithm W
succeeds on $\Gamma$ and an expression $e$ with counter $n$, returning a substitution $s$, a
monotype $\tau$ and a new counter $n'$, then $n \le n'$, every type variable of $\tau$ is less
than $n'$, and for every type variable $x < n$ every type variable of $s(x)$ is less than
$n'$.

Formalized by `Cslib.HindleyMilner.W_fresh`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Completeness.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Completeness.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#w-fresh).

## Substituting into a generalization is more general

For a typing context $\Gamma$, a
monotype $\tau$ and a type substitution $r$, the scheme obtained by applying $r$ to the free
type variables of the generalization of $\tau$ in $\Gamma$ is more general than the
generalization of $r(\tau)$ in $r(\Gamma)$: every instance of the latter is an instance of the
former, and every free type variable of the former is a free type variable of the latter.

Formalized by `Cslib.HindleyMilner.substTy_gen_moreGeneral`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Completeness.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Completeness.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#subst-ty-gen-more-general).

## Generalization depends only on the free variables of the context

If two typing
contexts $\Gamma$ and $\Gamma'$ have the same free type variables, then for every monotype
$\tau$ the generalization of $\tau$ in $\Gamma$ equals the generalization of $\tau$ in
$\Gamma'$.

Formalized by `Cslib.HindleyMilner.gen_congr`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Completeness.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Completeness.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#gen-congr).

## Completeness of Algorithm W

Let $\Gamma$ be a typing context and $n$ a natural number
such that every free type variable of $\Gamma$ is less than $n$. If, for some type substitution
$u$, an expression $e$ has a monotype $\tau'$ in the context $u(\Gamma)$, then Algorithm W
succeeds on $\Gamma$ and $e$ with counter $n$, returning a substitution $s$, a monotype $\tau$
and a new counter $n'$, and there is a type substitution $r$ such that $u(x) = r(s(x))$ for
every type variable $x < n$, and $\tau' = r(\tau)$.

This is the completeness theorem of Damas and Milner.

Formalized by `Cslib.HindleyMilner.W_complete`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Completeness.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Completeness.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#w-complete).

## Completeness of type inference for closed expressions

If an expression $e$ has a
monotype $\tau'$ in the empty context, then type inference succeeds on $e$ and returns a
monotype $\tau$ of which $\tau'$ is a substitution instance: $\tau' = r(\tau)$ for some type
substitution $r$.

Formalized by `Cslib.HindleyMilner.infer_complete`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Completeness.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Completeness.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#infer-complete).

## Type inference succeeds exactly on typable closed expressions

Type inference succeeds
on an expression $e$ if and only if $e$ has some monotype in the empty context.

Formalized by `Cslib.HindleyMilner.infer_isSome_iff`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Completeness.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Completeness.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#infer-is-some-iff).

## Principal types

The inferred type of a closed expression is one of its types, and
every type of it is an instance of the inferred one.

Formalized by `Cslib.HindleyMilner.infer_principal`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/HindleyMilner/Completeness.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/HindleyMilner/Completeness.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html#infer-principal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hindley–Milner type inference](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/hindley-milner-type-inference)
