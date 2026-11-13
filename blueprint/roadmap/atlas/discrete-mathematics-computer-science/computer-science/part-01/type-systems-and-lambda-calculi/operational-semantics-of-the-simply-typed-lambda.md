---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.Stlc.Value, Cslib.Languages.LambdaCalculus.Stlc.Step, Cslib.Languages.LambdaCalculus.Stlc.Step.value_irreducible, Cslib.Languages.LambdaCalculus.Stlc.Step.closed_function_value_is_lam, Cslib.Languages.LambdaCalculus.Stlc.Step.progress, Cslib.Languages.LambdaCalculus.Stlc.Step.deterministic, Cslib.Languages.LambdaCalculus.Stlc.Step.NormalForm, Cslib.Languages.LambdaCalculus.Stlc.Step.closed_normalForm_iff_value
statement: formalized
proof: formalized
---

# Operational semantics of the simply typed lambda calculus

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html).

## Values of STLC

A term of type $A$ in a context $\Gamma$ is a value exactly when it is a
lambda abstraction.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Value`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Semantics.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Semantics.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html#value-2).

## Small-step call-by-value reduction in STLC

One-step reduction on terms of type $A$ in a
context $\Gamma$ is the least relation closed under three left-to-right call-by-value rules: if
$f$ reduces to $f'$, then the application $f\,a$ reduces to $f'\,a$; if $f$ is a value and $a$
reduces to $a'$, then $f\,a$ reduces to $f\,a'$; and if $a$ is a value, then the application of
the abstraction of $b$ to $a$ reduces to $b[a]$, the result of substituting $a$ for the newest
free variable of $b$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Step`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Semantics.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Semantics.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html#step).

## Values are irreducible

If a term $t$ of type $A$ in a context $\Gamma$ is a value, then
there is no term $t'$ to which $t$ reduces in one call-by-value step.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Step.value_irreducible`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Semantics.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Semantics.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html#value-irreducible).

## Canonical forms for closed function values

If a term $f$ of function type
$A \Rightarrow B$ in the empty context is a value, then $f$ is a lambda abstraction: there is a
term $b$ of type $B$ in the one-variable context $[A]$ such that $f$ is the abstraction of $b$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Step.closed_function_value_is_lam`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Semantics.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Semantics.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html#closed-function-value-is-lam).

## Progress for closed STLC terms

Every term $t$ of type $A$ in the empty context is
either a value or reduces in one call-by-value step to some term $t'$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Step.progress`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Semantics.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Semantics.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html#progress).

## Small-step call-by-value reduction in STLC is deterministic

For terms $t$, $t_1$,
$t_2$ of type $A$ in a context $\Gamma$, if $t$ reduces in one call-by-value step both to $t_1$
and to $t_2$, then $t_1 = t_2$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Step.deterministic`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Semantics.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Semantics.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html#deterministic-2).

## Normal forms for call-by-value reduction in STLC

A term $t$ of type $A$ in a context
$\Gamma$ is in normal form when there is no term $t'$ such that $t$ reduces to $t'$ in one
call-by-value step.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Step.NormalForm`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Semantics.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Semantics.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html#normal-form).

## Closed normal forms are exactly the values

A term $t$ of type $A$ in the empty context
is in normal form, that is, has no call-by-value reduction step, if and only if it is a value.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Step.closed_normalForm_iff_value`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Semantics.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Semantics.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html#closed-normal-form-iff-value).

## Multi-step call-by-value reduction in STLC

For terms of type $A$ in a context $\Gamma$,
multi-step reduction is the reflexive transitive closure of one-step call-by-value reduction.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Steps`, an abbreviation declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Semantics.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Semantics.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html#steps).

## Big-step call-by-value evaluation in the simply typed lambda calculus

Fix a typing
context $\Gamma$. For terms $t$ and $v$ of the same type in context $\Gamma$, the big-step
evaluation relation $t \Downarrow v$ is the least relation such that every lambda abstraction
$\lambda.\,b$ evaluates to itself, and an application $f\,a$ evaluates to $v$ whenever
$f \Downarrow \lambda.\,b$, $a \Downarrow u$ and $b[u] \Downarrow v$, where $b[u]$ is the body $b$
with its newest free variable replaced by $u$.

The application rule fixes a left-to-right order: first the function, then the argument, then
the instantiated body.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Eval`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html#eval).

## Big-step evaluation produces values

In the call-by-value simply typed lambda calculus,
if a term $t$ of type $A$ in context $\Gamma$ evaluates by big-step evaluation to a term $v$,
written $t \Downarrow v$, then $v$ is a value, that is, a lambda abstraction.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Eval.value`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html#value).

## Values evaluate to themselves

Every value $v$, that is, every lambda abstraction, of any
type in any typing context evaluates to itself in the big-step semantics: $v \Downarrow v$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Eval.value_self`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html#value-self).

## Big-step evaluation implies small-step evaluation

Let $t$ and $v$ be terms of the same
type in the same typing context. If $t$ evaluates to $v$ in the big-step semantics, written
$t \Downarrow v$, then $t$ reduces to $v$ in finitely many (possibly zero) left-to-right
call-by-value steps.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Eval.to_steps`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html#to-steps).

## Big-step evaluation is closed under backward reduction steps

Let $t$, $t'$ and $v$ be
terms of the same type $A$ in the same typing context $\Gamma$. If $t$ reduces to $t'$ in one
left-to-right call-by-value step and $t'$ evaluates to $v$ in the big-step semantics, written
$t' \Downarrow v$, then $t \Downarrow v$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Eval.anti_step`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html#anti-step).

## Big-step evaluation is closed under backward multi-step reduction

Let $t$, $t'$ and $v$
be terms of the same type $A$ in the same typing context $\Gamma$. If $t$ reduces to $t'$ in
finitely many (possibly zero) left-to-right call-by-value steps and $t'$ evaluates to $v$ in the
big-step semantics, written $t' \Downarrow v$, then $t \Downarrow v$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Eval.anti_steps`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html#anti-steps).

## Small-step evaluation to a value implies big-step evaluation

Let $t$ and $v$ be terms of
the same type in the same typing context. If $t$ reduces to $v$ in finitely many (possibly zero)
left-to-right call-by-value steps and $v$ is a value, then $t$ evaluates to $v$ in the big-step
semantics, written $t \Downarrow v$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Eval.of_steps`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html#of-steps).

## Big-step evaluation is small-step evaluation to a value

For terms $t$ and $v$ of the
same type in the same typing context, $t$ evaluates to $v$ in the big-step semantics, written
$t \Downarrow v$, if and only if $t$ reduces to $v$ in finitely many (possibly zero)
left-to-right call-by-value steps and $v$ is a value, that is, a lambda abstraction.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Eval.iff_steps_value`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html#iff-steps-value).

## Determinism of big-step evaluation in the simply typed lambda calculus

For every typing
context $\Gamma$ and type $A$, if a term $t$ of type $A$ in context $\Gamma$ evaluates in the
big-step call-by-value semantics both to $v$ and to $w$, written $t \Downarrow v$ and
$t \Downarrow w$, then $v = w$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Eval.deterministic`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html#deterministic).

## Closed simply typed terms have a big-step evaluation

For every type $A$ and every closed
term $t$ of type $A$, that is, a term in the empty typing context, there is a term $v$ such that
$t$ evaluates to $v$ in the big-step call-by-value semantics, written $t \Downarrow v$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Eval.exists_closed`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html#exists-closed).

## Termination in terms of big-step evaluation

For every closed term $t$ of type $A$, that
is, a term in the empty typing context, $t$ terminates (it reduces to a value in finitely many
left-to-right call-by-value steps) if and only if there is a term $v$ such that $t$ evaluates to
$v$ in the big-step semantics, written $t \Downarrow v$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.terminates_iff_eval`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/BigStep.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html#terminates-iff-eval).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Operational semantics of the simply typed lambda calculus](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/operational-semantics-of-the-simply-typed-lambda)
