---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.Stlc.Ty.denote, Cslib.Languages.LambdaCalculus.Stlc.Env, Cslib.Languages.LambdaCalculus.Stlc.Env.cons, Cslib.Languages.LambdaCalculus.Stlc.Env.rename, Cslib.Languages.LambdaCalculus.Stlc.Tm.denote, Cslib.Languages.LambdaCalculus.Stlc.Tm.denote_rename, Cslib.Languages.LambdaCalculus.Stlc.Tm.denote_weaken, Cslib.Languages.LambdaCalculus.Stlc.Tm.denoteSub
statement: formalized
proof: formalized
---

# Denotational semantics of the simply typed lambda calculus

43 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html).

## Denotation of simple types

Given an interpretation $I$ assigning a type $I(b)$ to each
base type $b$, the denotation $[\![A]\!]_I$ of a simple type $A$ is defined by recursion on $A$:
a base type $b$ denotes $I(b)$, and a function type $A \Rightarrow B$ denotes the type of all
functions from $[\![A]\!]_I$ to $[\![B]\!]_I$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Ty.denote`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#denote).

## Semantic environments for the denotational semantics of STLC

Given an interpretation $I$
assigning a type to each base type and a typing context $\Gamma$ (a list of simple types), an
environment for $\Gamma$ assigns to every variable $x$ of $\Gamma$, of any simple type $A$, an
element of the denotation $[\![A]\!]_I$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Env`, an abbreviation declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#env).

## Extending a semantic environment in STLC

Given an interpretation $I$ of the base types, a
value $a$ in the denotation of a type $A$ and an environment $\eta$ for a context $\Gamma$, the
extended environment for the context $A :: \Gamma$ sends the newest variable to $a$ and the
successor $\mathrm{succ}\,x$ of each variable $x$ of $\Gamma$ to $\eta(x)$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Env.cons`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#cons).

## Renaming an environment

Given a renaming $\rho$ from context $\Gamma$ to context
$\Delta$ (a type-preserving map from the variables of $\Gamma$ to those of $\Delta$) and an
environment $\eta$ for $\Delta$, the renamed environment for $\Gamma$ sends each variable $x$ of
$\Gamma$ to $\eta(\rho(x))$; that is, it is the composite $\eta \circ \rho$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Env.rename`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#rename).

## Denotation of an STLC term

Given an interpretation $I$ of the base types, the denotation of
a well-typed term $t$ of type $A$ in context $\Gamma$ in an environment $\eta$ for $\Gamma$ is the
element of the denotation of $A$ defined by recursion on $t$: a variable $x$ denotes $\eta(x)$, an
application $f\,a$ denotes the denotation of $f$ applied to the denotation of $a$ (both in
$\eta$), and an abstraction $\lambda.\,b$ denotes the function sending each value $a$ of
its argument type to the denotation of the body $b$ in $\eta$ extended by $a$ for the newest
variable.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Tm.denote`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#denote-2).

## Renaming lemma for STLC denotation

For every interpretation $I$ of the base types, every
type-preserving renaming $\rho$ from context $\Gamma$ to context $\Delta$, every term $t$ in
context $\Gamma$ and every environment $\eta$ for $\Delta$, the denotation in $\eta$ of the term
obtained by renaming the variables of $t$ along $\rho$ equals the denotation of $t$ in the
environment that sends each variable $x$ of $\Gamma$ to $\eta(\rho(x))$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Tm.denote_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#denote-rename).

## Weakening preserves STLC denotation

For every interpretation $I$ of the base types, every
term $t$ of type $A$ in context $\Gamma$, every type $B$, every value $a$ in the denotation of $B$
and every environment $\eta$ for $\Gamma$, the weakening of $t$ to the context $B :: \Gamma$ has,
in the environment that extends $\eta$ by $a$ for the newest variable, the same denotation as $t$
in $\eta$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Tm.denote_weaken`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#denote-weaken).

## Denotation of an STLC substitution

Given an interpretation $I$ of the base types, a
type-preserving substitution $\sigma$ mapping each variable of a context $\Gamma$ to a term in a
context $\Delta$, and an environment $\eta$ for $\Delta$, this is the environment for $\Gamma$
that sends each variable $x$ to the denotation of $\sigma(x)$ in $\eta$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Tm.denoteSub`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#denote-sub).

## Substitution lemma for STLC denotation

For every interpretation $I$ of the base types,
every type-preserving substitution $\sigma$ mapping each variable of a context $\Gamma$ to a term
in a context $\Delta$, every term $t$ in context $\Gamma$ and every environment $\eta$ for
$\Delta$, the denotation in $\eta$ of $t$ with $\sigma$ applied simultaneously to its variables
equals the denotation of $t$ in the environment that sends each variable $x$ of $\Gamma$ to the
denotation of $\sigma(x)$ in $\eta$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Tm.denote_subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#denote-subst).

## Denotation of an instantiated STLC body

For every interpretation $I$ of the base types,
every term $b$ of type $B$ in context $A :: \Gamma$, every term $a$ of type $A$ in context $\Gamma$
and every environment $\eta$ for $\Gamma$, the denotation in $\eta$ of $b$ with its newest variable
replaced by $a$ equals the denotation of $b$ in the environment that extends $\eta$ by the
denotation of $a$ in $\eta$ for the newest variable.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Tm.denote_instantiate`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#denote-instantiate).

## One reduction step preserves STLC denotation

For every interpretation $I$ of the base
types, if a term $t$ reduces to $t'$ in one step of call-by-value reduction, then $t$ and $t'$
have the same denotation in every environment $\eta$ for their context.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Step.denote_eq`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#denote-eq).

## Multi-step reduction preserves STLC denotation

For every interpretation $I$ of the base
types, if a term $t$ reduces to $t'$ in zero or more steps of call-by-value reduction, then $t$
and $t'$ have the same denotation in every environment $\eta$ for their context.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Steps.denote_eq`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#denote-eq-2).

## Big-step evaluation preserves STLC denotation

For every interpretation $I$ of the base
types, if a term $t$ evaluates to $v$ under call-by-value big-step evaluation, then $t$ and $v$
have the same denotation in every environment $\eta$ for their context.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Eval.denote_eq`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Denotational.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#denote-eq-3).

## Semantic equality of terms in a model

Fix an interpretation $I$ of the base types as types.
Two terms $t$ and $u$ of the same type $A$ in the same context $\Gamma$ are semantically equal in
$I$ when, for every semantic environment $\eta$ for $\Gamma$, the denotation of $t$ in $I$ at $\eta$
equals the denotation of $u$ in $I$ at $\eta$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SemEq`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#sem-eq-2).

## Semantic equality is reflexive

For every interpretation $I$ of the base types, every
term $t$ is semantically equal to itself in $I$: it has the same denotation as itself in every
environment.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SemEq.refl`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#refl).

## Symmetry of semantic equality of terms

For every interpretation $I$ of the base types and
all terms $t$ and $u$ of the same type in the same context, if $t$ and $u$ are semantically equal
in $I$, then $u$ and $t$ are semantically equal in $I$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SemEq.symm`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#symm).

## Transitivity of semantic equality of terms

For every interpretation $I$ of the base types
and all terms $t$, $u$ and $w$ of the same type in the same context, if $t$ and $u$ are
semantically equal in $I$ and $u$ and $w$ are semantically equal in $I$, then $t$ and $w$ are
semantically equal in $I$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SemEq.trans`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#trans).

## Semantic equality is a congruence for application

Fix an interpretation $I$ of the base
types. If terms $f$ and $g$ of type $A \Rightarrow B$ in a context $\Gamma$ are semantically
equal in $I$ (they have the same denotation in every environment), and terms $a$ and $b$ of type
$A$ in $\Gamma$ are semantically equal in $I$, then the applications $f\,a$ and $g\,b$ are
semantically equal in $I$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SemEq.app`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#app).

## Semantic equality is a congruence for lambda abstraction

Fix an interpretation $I$ of
the base types. If two terms of type $B$ in the context $\Gamma$ extended by a newest variable
of type $A$ are semantically equal in $I$ (they have the same denotation in every environment),
then their lambda abstractions, terms of type $A \Rightarrow B$ in $\Gamma$, are semantically
equal in $I$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SemEq.lam`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#lam).

## Renaming preserves semantic equality

Fix an interpretation $I$ of the base types. If
terms $t$ and $u$ of type $A$ in a context $\Gamma$ are semantically equal in $I$ (they have the
same denotation in every environment), then for every type-preserving renaming $\rho$ of the
variables of $\Gamma$ into a context $\Delta$, the renamed terms $\rho(t)$ and $\rho(u)$ are
semantically equal in $I$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SemEq.rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#rename-2).

## Substitution preserves semantic equality

For every interpretation $I$ of the base types,
if two terms $t$ and $u$ of the same type $A$ in a context $\Gamma$ are semantically equal in $I$,
then for every simultaneous substitution $\sigma$ from $\Gamma$ to a context $\Delta$, the result
of applying $\sigma$ to $t$ and the result of applying $\sigma$ to $u$ are semantically equal in
$I$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SemEq.subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#subst).

## Single-step evaluation is a semantic equation

For every interpretation $I$ of the base
types, if a term $t$ reduces to a term $u$ in one call-by-value evaluation step, then $t$ and $u$
are semantically equal in $I$: they have the same denotation in every environment.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SemEq.of_step`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#of-step).

## Multi-step evaluation is a semantic equation

For every interpretation $I$ of the base
types, if a term $t$ reduces to a term $u$ in zero or more call-by-value evaluation steps, then
$t$ and $u$ are semantically equal in $I$: they have the same denotation in every environment.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SemEq.of_steps`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#of-steps).

## Beta is sound for the denotational semantics

For every interpretation $I$ of the base
types, every term $t$ of type $B$ in the context $\Gamma$ extended by a newest variable of type
$A$, and every term $a$ of type $A$ in $\Gamma$, the redex $(\lambda.\,t)\,a$ is semantically
equal in $I$ (has the same denotation in every environment) to the instantiation $t[a]$, which
replaces the newest free variable of $t$ by $a$.

The argument $a$ need not be a value.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SemEq.beta`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#beta-2).

## Eta is sound for the denotational semantics

For every interpretation $I$ of the base
types and every term $f$ of type $A \Rightarrow B$ in a context $\Gamma$, let $f'$ be the
weakening of $f$ to the context $\Gamma$ extended by a newest variable $x$ of type $A$. Then the
term $\lambda x.\, f'\,x$, which binds $x$, is semantically equal to $f$ in $I$ (has the same
denotation in every environment).

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SemEq.eta`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#eta-2).

## Pointwise semantic equality of substitutions

Fix an interpretation $I$ of the base types
as types. Two simultaneous substitutions $\sigma$ and $\tau$ from a context $\Gamma$ to a context
$\Delta$ are pointwise semantically equal in $I$ when, for every variable $x$ of $\Gamma$ (of any
type) and every semantic environment $\eta$ for $\Delta$, the denotation of the term $\sigma(x)$ in
$I$ at $\eta$ equals the denotation of the term $\tau(x)$ in $I$ at $\eta$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SubSemEq`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#sub-sem-eq).

## Pointwise semantic equality of substitutions is reflexive

For every interpretation $I$
of the base types and every simultaneous substitution $\sigma$ that replaces each variable of a
context $\Gamma$ by a term of the same type in a context $\Delta$, $\sigma$ is pointwise
semantically equal to itself in $I$: for every variable $x$ of $\Gamma$, the term $\sigma(x)$
has the same denotation as itself in every environment for $\Delta$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SubSemEq.refl`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#refl-2).

## Symmetry of pointwise semantic equality of substitutions

For every interpretation $I$ of
the base types and all simultaneous substitutions $\sigma$ and $\tau$ from a context $\Gamma$ to a
context $\Delta$, if $\sigma$ and $\tau$ are pointwise semantically equal in $I$, then $\tau$ and
$\sigma$ are pointwise semantically equal in $I$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SubSemEq.symm`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#symm-2).

## Transitivity of pointwise semantic equality of substitutions

For every interpretation $I$
of the base types and all simultaneous substitutions $\sigma$, $\tau$ and $\upsilon$ from a context
$\Gamma$ to a context $\Delta$, if $\sigma$ and $\tau$ are pointwise semantically equal in $I$ and
$\tau$ and $\upsilon$ are pointwise semantically equal in $I$, then $\sigma$ and $\upsilon$ are
pointwise semantically equal in $I$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SubSemEq.trans`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#trans-2).

## Semantically equal substitutions give semantically equal results

For every interpretation
$I$ of the base types, every term $t$ of type $A$ in a context $\Gamma$, and all simultaneous
substitutions $\sigma$ and $\tau$ from $\Gamma$ to a context $\Delta$ that are pointwise
semantically equal in $I$, the result of applying $\sigma$ to $t$ and the result of applying $\tau$
to $t$ are semantically equal in $I$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SemEq.subst_congr`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#subst-congr).

## Semantic equality is an equivalence relation

For every interpretation $I$ of the base
types, every context $\Gamma$ and every type $A$, semantic equality in $I$ of terms of type $A$
in $\Gamma$ (having the same denotation in every environment) is reflexive, symmetric and
transitive.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SemEq.equivalence`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Equational.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#equivalence).

## Typed one-hole contexts

Fix simple types over a type of base types. A one-hole context
whose hole has type $A$ in variable context $\Gamma$, and which produces a term of type $B$ in
variable context $\Delta$, is built by four rules. The hole itself is such a context, with
$\Delta = \Gamma$ and $B = A$. If $C$ produces type $S \Rightarrow T$ in $\Delta$ and $a$ is a term
of type $S$ in $\Delta$, then the application $C\,a$ produces type $T$ in $\Delta$. If $f$ is a
term of type $S \Rightarrow T$ in $\Delta$ and $C$ produces type $S$ in $\Delta$, then the
application $f\,C$ produces type $T$ in $\Delta$. If $C$ produces type $T$ in the context
$S :: \Delta$ obtained from $\Delta$ by adding a new leading variable of type $S$, then the
abstraction $\lambda C$ produces type $S \Rightarrow T$ in $\Delta$. In every rule the hole keeps
type $A$ in context $\Gamma$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.TmCtx`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#tm-ctx).

## Plugging a term into an STLC context

Let $E$ be a typed one-hole context whose hole
has type $A$ in variable context $\Gamma$ and which produces a term of type $B$ in variable
context $\Delta$. For a term $t$ of type $A$ in $\Gamma$, the plugged term $E[t]$ of type $B$
in $\Delta$ is defined by recursion on $E$: $[\,][t] = t$, $(E\,a)[t] = E[t]\,a$,
$(f\,E)[t] = f\,E[t]$ and $(\lambda.\,E)[t] = \lambda.\,E[t]$, where $[\,]$ is the bare hole,
$E\,a$ applies $E$ to a term $a$, $f\,E$ applies a term $f$ to $E$, and $\lambda.\,E$ puts $E$
under a lambda. No renaming is applied, so a lambda above the hole may bind free variables
of $t$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.TmCtx.plug`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#plug).

## Composition of STLC contexts

Let $E_2$ be a typed one-hole context whose hole has
type $B$ in variable context $\Delta$ and which produces a term of type $C$ in context
$\Theta$, and let $E_1$ be one whose hole has type $A$ in context $\Gamma$ and which produces
a term of type $B$ in $\Delta$. The composite $E_2 \circ E_1$, with hole of type $A$ in
$\Gamma$ and result of type $C$ in $\Theta$, replaces the hole of $E_2$ by $E_1$; by
recursion on $E_2$: $[\,] \circ E_1 = E_1$, $(E_2\,a) \circ E_1 = (E_2 \circ E_1)\,a$,
$(f\,E_2) \circ E_1 = f\,(E_2 \circ E_1)$ and
$(\lambda.\,E_2) \circ E_1 = \lambda.\,(E_2 \circ E_1)$, where $[\,]$ is the bare hole and
$E\,a$, $f\,E$, $\lambda.\,E$ apply a context $E$ to a term $a$, apply a term $f$ to $E$, and
put $E$ under a lambda.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.TmCtx.comp`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#comp).

## Plugging into a composite STLC context

Let $E_2$ be a typed one-hole context whose
hole has type $B$ in variable context $\Delta$ and which produces a term of type $C$ in
context $\Theta$, and let $E_1$ be one whose hole has type $A$ in context $\Gamma$ and which
produces a term of type $B$ in $\Delta$. Then for every term $t$ of type $A$ in $\Gamma$,
$(E_2 \circ E_1)[t] = E_2[E_1[t]]$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.TmCtx.plug_comp`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#plug-comp).

## Associativity of composition of STLC contexts

Let $E_1$ be a typed one-hole context
whose hole has type $A$ in variable context $\Gamma$ and which produces a term of type $B$ in
context $\Delta$, $E_2$ one with hole of type $B$ in $\Delta$ producing type $C$ in $\Theta$,
and $E_3$ one with hole of type $C$ in $\Theta$ producing type $D$ in $\Xi$. Then
$(E_3 \circ E_2) \circ E_1 = E_3 \circ (E_2 \circ E_1)$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.TmCtx.comp_assoc`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#comp-assoc).

## Semantic equality is a congruence for typed contexts

Fix an interpretation $I$ of the
base types. Let $t$ and $u$ be terms of type $A$ in variable context $\Gamma$ that denote the same
value in $I$ under every semantic environment. Then for every typed one-hole context $C$ whose
hole has type $A$ in context $\Gamma$ and which produces a term of type $B$ in context $\Delta$, the
terms $C[t]$ and $C[u]$ obtained by plugging $t$ and $u$ into the hole also denote the same value
in $I$ under every semantic environment.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.TmCtx.semEq`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#sem-eq).

## Model equality of STLC terms

Two terms $t$ and $u$ of type $A$ in variable
context $\Gamma$ are model-equal when, for every interpretation $I$ of the base types by types
in the same universe as the type of base types, they are semantically equal in $I$: with
function types interpreted as full function spaces, the denotations of $t$ and $u$ agree at
every semantic environment for $\Gamma$.

Unlike semantic equality in a fixed interpretation, this relation does not choose a particular
model.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.ModelEq`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#model-eq).

## Model equality is a congruence for STLC contexts

Let $E$ be a typed one-hole context
whose hole has type $A$ in variable context $\Gamma$ and which produces a term of type $B$ in
context $\Delta$. If two terms $t$ and $u$ of type $A$ in $\Gamma$ are model-equal, then
$E[t]$ and $E[u]$ are model-equal.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.ModelEq.context`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#context).

## Model-independent beta equality

For every term $b$ of type $B$ in the variable
context $\Gamma$ extended by a newest variable of type $A$, and every term $a$ of type $A$ in
$\Gamma$, the application $(\lambda.\,b)\,a$ is model-equal to $b[a]$, the result of
substituting $a$ for the newest variable of $b$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.ModelEq.beta`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#beta).

## Model-independent eta equality

For every term $f$ of type $A \Rightarrow B$ in
variable context $\Gamma$, the term $\lambda.\,(f^{\uparrow}\,x_0)$ is model-equal to $f$,
where $f^{\uparrow}$ is $f$ weakened by a newest variable of type $A$ and $x_0$ is that
variable.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.ModelEq.eta`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#eta).

## Beta equality inside an STLC context

Let $E$ be a typed one-hole context whose hole
has type $B$ in variable context $\Gamma$ and which produces a term of type $C$ in context
$\Delta$. For every term $b$ of type $B$ in $\Gamma$ extended by a newest variable of type
$A$, and every term $a$ of type $A$ in $\Gamma$, the term $E[(\lambda.\,b)\,a]$ is
model-equal to $E[b[a]]$, where $b[a]$ is the result of substituting $a$ for the newest
variable of $b$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.ModelEq.context_beta`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#context-beta).

## Eta equality inside an STLC context

Let $E$ be a typed one-hole context whose hole
has type $A \Rightarrow B$ in variable context $\Gamma$ and which produces a term of type $C$
in context $\Delta$. For every term $f$ of type $A \Rightarrow B$ in $\Gamma$, the term
$E[\lambda.\,(f^{\uparrow}\,x_0)]$ is model-equal to $E[f]$, where $f^{\uparrow}$ is $f$
weakened by a newest variable of type $A$ and $x_0$ is that variable.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.ModelEq.context_eta`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Contextual.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html#context-eta).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Denotational semantics of the simply typed lambda calculus](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/denotational-semantics-of-the-simply-typed-lambd)
