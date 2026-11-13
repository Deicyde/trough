---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.Stlc.Sem, Cslib.Languages.LambdaCalculus.Stlc.Sem.rename, Cslib.Languages.LambdaCalculus.Stlc.SemEnv, Cslib.Languages.LambdaCalculus.Stlc.SemEnv.rename, Cslib.Languages.LambdaCalculus.Stlc.SemEnv.cons, Cslib.Languages.LambdaCalculus.Stlc.SemEnv.identity, Cslib.Languages.LambdaCalculus.Stlc.nbeEval, Cslib.Languages.LambdaCalculus.Stlc.normalizeNf
statement: formalized
proof: formalized
---

# Normalization by evaluation

35 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html).

## Kripke semantic values

For a context $\Gamma$, the semantic values of a simple type in
$\Gamma$ are defined by recursion on the type. At a base type $b$ they are the neutral terms of
type $b$ in $\Gamma$ (variables applied to zero or more normal arguments). At an arrow type
$A \Rightarrow B$ a semantic value is a family that, for every context $\Delta$ and every
renaming from $\Gamma$ to $\Delta$, maps semantic values of type $A$ in $\Delta$ to semantic
values of type $B$ in $\Delta$.

Because a semantic function acts after every renaming into a later context, reification under a
binder needs no untyped weakening operation.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Sem`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Nbe.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Nbe.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#sem).

## Renaming a semantic value

Given a renaming $\rho$ from a context $\Gamma$ to a context
$\Delta$, a simple type $A$ and a semantic value $v$ of type $A$ in $\Gamma$, the renamed value is
the semantic value of type $A$ in $\Delta$ defined by cases on $A$. At a base type it is the
neutral term $v$ with its free variables renamed by $\rho$. At an arrow type
$A = B \Rightarrow C$ it sends a renaming $\sigma$ from $\Delta$ to a context $\Theta$ and a
semantic value $a$ of type $B$ in $\Theta$ to the semantic value of type $C$ in $\Theta$ that $v$
assigns to the composite renaming ($\rho$ followed by $\sigma$) and $a$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Sem.rename`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Nbe.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Nbe.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#rename).

## Semantic environments for normalization by evaluation

For contexts $\Delta$ and
$\Gamma$, a semantic environment for $\Gamma$ in $\Delta$ assigns to every variable of $\Gamma$,
of any type $A$, a Kripke semantic value of type $A$ in $\Delta$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SemEnv`, an abbreviation declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Nbe.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Nbe.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#sem-env).

## Renaming a semantic environment

Given a renaming $\rho$ from a context $\Delta$ to a
context $\Theta$ and a semantic environment $\eta$ for $\Gamma$ in $\Delta$, the renamed
environment is the semantic environment for $\Gamma$ in $\Theta$ that sends each variable $x$ of
type $A$ to the semantic value $\eta(x)$ renamed along $\rho$ at type $A$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SemEnv.rename`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Nbe.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Nbe.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#rename-2).

## Extending a semantic environment by one variable

Given a semantic value $a$ of type $A$
in a context $\Delta$ and a semantic environment $\eta$ for $\Gamma$ in $\Delta$, the extended
environment is the semantic environment for the context $A :: \Gamma$ (the context $\Gamma$ with a
new innermost variable of type $A$) in $\Delta$ that sends the new innermost variable to $a$ and
sends the successor of each variable $x$ of $\Gamma$ to $\eta(x)$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SemEnv.cons`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Nbe.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Nbe.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#cons).

## The identity semantic environment

For a context $\Gamma$, the identity environment is the
semantic environment for $\Gamma$ in $\Gamma$ that sends each variable $x$ of type $A$ to the
reflection at type $A$ of the neutral term $x$. Reflection turns a neutral term into a semantic
value of the same type in the same context.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SemEnv.identity`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Nbe.lean, line 333](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Nbe.lean#L333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#identity).

## Evaluation into the Kripke semantic domain

Let $t$ be a term of type $T$ in context
$\Gamma$ and let $\eta$ be a semantic environment interpreting every variable of $\Gamma$ as a
semantic value in context $\Delta$. The evaluation $\operatorname{ev}(t, \eta)$ is the semantic
value of type $T$ in context $\Delta$ defined by recursion on $t$: a variable $x$ evaluates to
$\eta(x)$; an application $f\,a$ evaluates to the semantic function $\operatorname{ev}(f, \eta)$
applied, along the identity renaming of $\Delta$, to $\operatorname{ev}(a, \eta)$; and an
abstraction $\lambda b$ of type $A \to B$, whose body $b$ lies in the context $\Gamma$ extended
by $A$, evaluates to the semantic function that sends a renaming $\rho$ from $\Delta$ to a context
$\Theta$ and a semantic value $a$ of type $A$ in $\Theta$ to $\operatorname{ev}(b, \eta')$, where
$\eta'$ sends the new variable to $a$ and each variable $x$ of $\Gamma$ to $\eta(x)$ renamed along
$\rho$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.nbeEval`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeEvaluation.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeEvaluation.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#nbe-eval).

## Normalization by evaluation

For a term $t$ of type $A$ in context $\Gamma$, its normal
form is the beta-normal, eta-long term of type $A$ in context $\Gamma$ obtained by reifying, at
type $A$, the evaluation of $t$ in the identity semantic environment of $\Gamma$, which interprets
each variable as the reflection of that variable.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.normalizeNf`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeEvaluation.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeEvaluation.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#normalize-nf).

## Normalization of terms

For a term $t$ of type $A$ in context $\Gamma$, its normalized term
is the term of type $A$ in context $\Gamma$ underlying the beta-normal, eta-long normal form of $t$
computed by normalization by evaluation.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.normalizeTm`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeEvaluation.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeEvaluation.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#normalize-tm).

## Reflection commutes with renaming

For every type $A$, every renaming $\rho$ from a
context $\Gamma$ to a context $\Delta$, and every neutral term $n$ of type $A$ in context
$\Gamma$, transporting the semantic value obtained by reflecting $n$ at type $A$ along $\rho$
gives the reflection at type $A$ of the neutral term $n$ renamed by $\rho$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.reflect_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#reflect-rename).

## The identity environment under a binder

Let $\Gamma$ be a context, $A$ a type, and
$\Gamma, A$ the context $\Gamma$ extended by a newest variable of type $A$. Transport the identity
semantic environment of $\Gamma$ (which reflects each variable as a neutral value) along the
weakening renaming from $\Gamma$ to $\Gamma, A$ that sends each variable to its successor, and
extend the result by the reflection at type $A$ of the newest variable of $\Gamma, A$. The
resulting semantic environment equals the identity semantic environment of $\Gamma, A$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SemEnv.cons_reflect_rename_identity`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#cons-reflect-rename-identity).

## Evaluation respects pointwise equal environments

Let $t$ be a term of type $A$ in
context $\Gamma$, and let $\xi$ and $\zeta$ be semantic environments interpreting the variables of
$\Gamma$ in a context $\Delta$. If $\xi(x) = \zeta(x)$ for every variable $x$ of $\Gamma$, of any
type, then evaluating $t$ in $\xi$ and evaluating $t$ in $\zeta$ give the same semantic value.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.nbeEval_congr`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#nbe-eval-congr).

## Evaluating a neutral term reflects it

For every neutral term $n$ of type $A$ in context
$\Gamma$, evaluating the underlying term of $n$ in the identity semantic environment of $\Gamma$
gives the reflection of $n$ at type $A$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.nbeEval_ne_toTm`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#nbe-eval-ne-to-tm).

## Normal forms are fixed points of normalization

For every beta-normal, eta-long normal
form $n$ of type $A$ in context $\Gamma$, normalizing the underlying term of $n$ by evaluation
returns the normal form $n$ itself.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.normalizeNf_toTm`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#normalize-nf-to-tm).

## Renormalizing a computed normal form

For every term $t$ of type $A$ in context
$\Gamma$, normalizing the underlying term of the normal form that normalization by evaluation
computes from $t$ gives the same term as normalizing $t$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.normalizeTm_normalizeNf`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#normalize-tm-normalize-nf).

## Normalization by evaluation is idempotent

For every term $t$ of type $A$ in context
$\Gamma$, normalizing the normalized term of $t$ by evaluation gives the normalized term of $t$
again.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.normalizeTm_idem`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#normalize-tm-idem).

## Normalization fixes the terms of normal forms

For every eta-long normal form $n$ of
type $A$ in context $\Gamma$, normalizing the underlying term of $n$ returns that term
unchanged.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.normalizeTm_toTm`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#normalize-tm-to-tm).

## Erasing normal forms is injective

For every context $\Gamma$ and type $A$, two
eta-long normal forms of type $A$ in context $\Gamma$ with the same underlying term are equal.

NbE gives an explicit left inverse, so no separate syntactic injectivity argument is
needed.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Nf.toTm_injective`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#to-tm-injective).

## Canonical terms

A term $t$ of type $A$ in context $\Gamma$ is canonical when it is the
underlying term of some beta-normal, eta-long normal form of type $A$ in context $\Gamma$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.IsCanonical`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#is-canonical).

## Canonical terms are the fixed points of normalization

A term $t$ of type $A$ in context
$\Gamma$ is canonical if and only if normalization by evaluation maps $t$ to itself, that is, the
term underlying the normal form computed for $t$ is $t$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.isCanonical_iff_normalizeTm_eq`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#is-canonical-iff-normalize-tm-eq).

## Normalized terms are canonical

For every term $t$ of type $A$ in context $\Gamma$, the
term obtained by normalizing $t$ by evaluation is canonical.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.isCanonical_normalizeTm`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#is-canonical-normalize-tm).

## Renaming preserves canonical terms

If a term $t$ of type $A$ in context $\Gamma$ is
canonical, then for every renaming $\rho$ from $\Gamma$ to a context $\Delta$, the term
obtained by renaming $t$ along $\rho$ is canonical.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.IsCanonical.rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#rename-3).

## Certified canonical terms

For a context $\Gamma$ and a type $A$, a certified canonical
term of type $A$ in context $\Gamma$ is a term $t$ of type $A$ in context $\Gamma$ together with a
proof that $t$ is a fixed point of normalization by evaluation: the term underlying the normal
form computed for $t$ is $t$ itself.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CanonicalTm`, an abbreviation declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#canonical-tm).

## Normal forms as canonical terms

The canonical term of an eta-long normal form $n$ of
type $A$ in context $\Gamma$ is the underlying term of $n$, certified to be a fixed point of
normalization.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Nf.toCanonicalTm`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#to-canonical-tm).

## The normal form of a canonical term

For a canonical term $t$ of type $A$ in context
$\Gamma$, that is, a term that normalization returns unchanged, its normal form is the
eta-long normal form that normalization by evaluation computes from $t$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CanonicalTm.toNf`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#to-nf).

## Canonical terms have a unique normal form

Let $t$ be a term of type $A$ in context
$\Gamma$. If $t$ is canonical, then there is exactly one beta-normal, eta-long normal form of type
$A$ in context $\Gamma$ whose underlying term is $t$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.isCanonical_existsUniqueNf`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCanonical.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#is-canonical-exists-unique-nf).

## Kripke realization relation for NbE

Fix an interpretation $I$ of the base types. For a
context $\Gamma$, an environment $\eta$ for $\Gamma$ in $I$, a type $A$, a Kripke semantic value
$v$ of type $A$ in $\Gamma$ and an element $d$ of the denotation of $A$ under $I$, the relation
"$v$ realizes $d$ at $\eta$" is defined by recursion on $A$. At a base type, $v$ is a neutral
term, and $v$ realizes $d$ when the denotation of $v$, read as a term, in $\eta$ equals $d$. At a
function type $A \Rightarrow B$, $v$ realizes $d$ when for every context $\Delta$, every renaming
$\rho : \Gamma \to \Delta$, every environment $\theta$ for $\Delta$ with $\theta \circ \rho = \eta$,
every semantic value $a$ of type $A$ in $\Delta$ and every element $e$ of the denotation of $A$
such that $a$ realizes $e$ at $\theta$, the semantic value $v(\rho, a)$ realizes $d(e)$ at
$\theta$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.NbeRelated`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCorrectness.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCorrectness.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#nbe-related).

## Realization is stable under renaming

Fix an interpretation $I$ of the base types. Let
$v$ be a Kripke semantic value of type $A$ in context $\Gamma$ that realizes an element $d$ of
the denotation of $A$ at an environment $\eta$ for $\Gamma$. If $\rho : \Gamma \to \Delta$ is a
renaming and $\theta$ is an environment for $\Delta$ with $\theta \circ \rho = \eta$, then the
transport of $v$ along $\rho$ realizes $d$ at $\theta$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.NbeRelated.rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCorrectness.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCorrectness.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#rename-4).

## Realization of environments

Fix an interpretation $I$ of the base types, contexts
$\Delta$ and $\Gamma$, an environment $\theta$ for $\Delta$ in $I$, a Kripke semantic environment
$\xi$ assigning to each variable of $\Gamma$ a semantic value in $\Delta$, and an environment
$\eta$ for $\Gamma$ in $I$. Then $\xi$ realizes $\eta$ at $\theta$ when for every type $A$ and
every variable $x$ of type $A$ in $\Gamma$, the semantic value $\xi(x)$ realizes $\eta(x)$ at
$\theta$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.NbeEnvRelated`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCorrectness.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCorrectness.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#nbe-env-related).

## Fundamental lemma for NbE evaluation

Fix an interpretation $I$ of the base types.
Let $t$ be a term of type $A$ in context $\Gamma$, let $\xi$ be a Kripke semantic environment
assigning to each variable of $\Gamma$ a semantic value in context $\Delta$, and let $\eta$ and
$\theta$ be environments in $I$ for $\Gamma$ and $\Delta$. If $\xi$ realizes $\eta$ at $\theta$,
then the NbE evaluation of $t$ in $\xi$ realizes the denotation of $t$ in $\eta$ at $\theta$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.nbeEval_related`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCorrectness.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCorrectness.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#nbe-eval-related).

## The identity semantic environment realizes every environment

Fix an interpretation $I$
of the base types and an environment $\eta$ for a context $\Gamma$ in $I$. Then the identity
Kripke semantic environment on $\Gamma$, which reflects each variable as a neutral value,
realizes $\eta$ at $\eta$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.identity_related`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCorrectness.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCorrectness.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#identity-related).

## NbE preserves denotation

For every interpretation $I$ of the base types, every term $t$
of type $A$ in context $\Gamma$ and every environment $\eta$ for $\Gamma$ in $I$, the NbE normal
form of $t$ has the same denotation in $\eta$ as $t$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.normalizeTm_denote`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCorrectness.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCorrectness.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#normalize-tm-denote).

## Every term is semantically equal to its NbE normal form in each model

For every
interpretation $I$ of the base types and every term $t$ of type $A$ in context $\Gamma$, $t$ and
its NbE normal form are semantically equal in $I$: they have the same denotation in every
environment for $\Gamma$ in $I$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.normalizeTm_semEq`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCorrectness.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCorrectness.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#normalize-tm-sem-eq).

## Every term is model-equal to its NbE normal form

Every term $t$ of type $A$ in context
$\Gamma$ is model-equal to its NbE normal form.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.normalizeTm_modelEq`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCorrectness.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCorrectness.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#normalize-tm-model-eq).

## Equal NbE normal forms imply model equality

If two terms $t$ and $u$ of type $A$ in
context $\Gamma$ have the same NbE normal form, then $t$ and $u$ are model-equal.

Equality of computed normal forms is thus a sound test for model equality; no converse is
claimed.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.modelEq_of_normalizeTm_eq`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCorrectness.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/NbeCorrectness.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html#model-eq-of-normalize-tm-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Normalization by evaluation](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-by-evaluation)
