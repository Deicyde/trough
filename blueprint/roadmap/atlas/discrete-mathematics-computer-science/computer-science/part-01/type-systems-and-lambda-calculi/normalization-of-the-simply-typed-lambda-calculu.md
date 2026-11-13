---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.Stlc.Steps.appFun, Cslib.Languages.LambdaCalculus.Stlc.Steps.appArg, Cslib.Languages.LambdaCalculus.Stlc.Steps.suffix_of_value, Cslib.Languages.LambdaCalculus.Stlc.Terminates, Cslib.Languages.LambdaCalculus.Stlc.Terminates.of_value, Cslib.Languages.LambdaCalculus.Stlc.Terminates.anti, Cslib.Languages.LambdaCalculus.Stlc.Terminates.forward, Cslib.Languages.LambdaCalculus.Stlc.Reducible
statement: formalized
proof: formalized
---

# Normalization of the simply typed lambda calculus

35 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html).

## Multi-step evaluation is a congruence in function position

Let $f$ and $f'$ be terms
of type $A \Rightarrow B$ and let $a$ be a term of type $A$, all in the same context. If $f$
evaluates to $f'$ in zero or more call-by-value steps, then the application $f\,a$ evaluates
to $f'\,a$ in zero or more steps.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Steps.appFun`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#app-fun).

## Evaluating the argument of a value function is a multi-step congruence

Let $f$ be a term
of type $A \Rightarrow B$ and let $a$, $a'$ be terms of type $A$, all in the same context. If $f$
is a value and $a$ evaluates to $a'$ in zero or more call-by-value steps, then the application
$f\,a$ evaluates to $f\,a'$ in zero or more steps.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Steps.appArg`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#app-arg).

## Evaluation to a value passes through every reduct

Let $t$, $t'$ and $v$ be terms of the
same type in the same context, with $v$ a value. If $t$ evaluates to $v$ and $t$ evaluates to
$t'$, each in finitely many call-by-value steps, then $t'$ evaluates to $v$ in finitely many
steps.

The value endpoint makes the first evaluation maximal, so every other finite
evaluation is one of its prefixes.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Steps.suffix_of_value`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#suffix-of-value).

## Termination of closed terms

A closed term $t$ terminates when it evaluates, in
finitely many call-by-value steps, to a value.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Terminates`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#terminates).

## Values terminate

Every closed term of the simply typed lambda calculus that is a value
terminates.

No evaluation step is needed: the value itself is the value reached.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Terminates.of_value`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#of-value).

## Termination is closed under backward evaluation

Let $t$ and $t'$ be closed terms of
the same type. If $t$ evaluates to $t'$ in zero or more call-by-value steps and $t'$
terminates, then $t$ terminates.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Terminates.anti`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#anti).

## Termination is closed under forward evaluation

Let $t$ and $t'$ be closed terms of
the same type. If $t$ terminates and $t$ evaluates to $t'$ in zero or more call-by-value
steps, then $t'$ terminates.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Terminates.forward`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#forward).

## Tait reducibility for closed terms

Reducibility of a closed term $t$ is defined by
recursion on its simple type. At a base type, $t$ is reducible when it terminates. At a function
type $A \Rightarrow B$, $t$ is reducible when it terminates and, for every reducible closed term
$a$ of type $A$, the application $t\,a$ is reducible.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Reducible`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#reducible).

## Reducible terms terminate

Every reducible closed term of the simply typed lambda
calculus terminates.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Reducible.terminates`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#terminates-2).

## Reducibility is closed under forward evaluation

Let $t$ and $t'$ be closed terms of
the same type. If $t$ is reducible and $t$ evaluates to $t'$ in zero or more call-by-value
steps, then $t'$ is reducible.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Reducible.forward`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#forward-2).

## Reducibility is closed under backward evaluation

Let $t$ and $t'$ be closed terms of
the same type. If $t$ evaluates to $t'$ in zero or more call-by-value steps and $t'$ is
reducible, then $t$ is reducible.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Reducible.anti`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#anti-2).

## Reducibility is invariant under evaluation

Let $t$ and $t'$ be closed terms of the
same type. If $t$ evaluates to $t'$ in zero or more call-by-value steps, then $t$ is reducible
if and only if $t'$ is reducible.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Reducible.iff_of_steps`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#iff-of-steps).

## Reducible substitutions

A substitution $\sigma$ that replaces each variable of a
context $\Gamma$ by a closed term of the same type is reducible when $\sigma(x)$ is reducible
for every variable $x$ of $\Gamma$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.ReducibleSub`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#reducible-sub).

## Substitutions on the empty context are reducible

Every substitution from the empty
context to closed terms is reducible, since the empty context has no variables.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.ReducibleSub.empty`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#empty).

## Extending a reducible substitution by a reducible term keeps it reducible

Let $\sigma$
be a substitution that sends each variable of a context $\Gamma$ to a closed term of the same
type, and let $a$ be a closed term of type $A$. If $\sigma$ and $a$ are reducible, then so is
the substitution on the context $A, \Gamma$ that sends the newest variable to $a$ and each
older variable $x$ to $\sigma(x)$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.ReducibleSub.cons`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#cons).

## Fundamental theorem of the reducibility relation

Let $t$ be a term of type $A$ in a
context $\Gamma$, and let $\sigma$ be a reducible substitution sending each variable of $\Gamma$
to a closed term of the same type. Then the closed term obtained by applying $\sigma$ to $t$ is
reducible.

The lambda case is the key: evaluate an arbitrary reducible
argument to a value, cross the beta step, and invoke the induction hypothesis
under the extended substitution.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.fundamental`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#fundamental).

## Closed terms are reducible

Every closed well-typed term of the simply typed lambda
calculus is reducible.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.reducible_closed`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#reducible-closed).

## Termination of the call-by-value simply typed lambda calculus

Every closed well-typed
term evaluates, in finitely many call-by-value steps, to a value.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.terminates_closed`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/LogicalRelation.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#terminates-closed).

## Values reduce only to themselves

Let $v$ and $t$ be terms of the same type in the same
context. If $v$ is a value and $v$ reduces to $t$ in zero or more call-by-value steps, then
$v = t$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Steps.eq_of_value_source`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#eq-of-value-source).

## Uniqueness of the value reached by evaluation

Let $t$ be a term in any context. If $t$
reduces in zero or more call-by-value steps to a value $v$ and also to a value $w$, then
$v = w$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Steps.value_unique`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#value-unique).

## Normalizing closed terms

A closed term $t$ of the simply typed lambda calculus normalizes
when it reduces, in zero or more call-by-value steps, to a term in normal form, that is, a term
with no further call-by-value reduction step.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Normalizes`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#normalizes).

## Normalization and termination coincide

A closed well-typed term $t$ normalizes, that is,
reduces in zero or more call-by-value steps to a normal form (a term with no further reduction
step), if and only if it terminates, that is, reduces in zero or more call-by-value steps to a
value.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Normalizes.iff_terminates`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#iff-terminates).

## Normalization of closed terms

Every closed well-typed term normalizes: it reduces in
zero or more call-by-value steps to a normal form.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.normalizes_closed`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#normalizes-closed).

## Uniqueness of normal forms

If a closed term $t$ reduces in zero or more call-by-value
steps to a normal form $n$ and also to a normal form $m$, then $n = m$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.normalForm_unique`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#normal-form-unique).

## Closed functions evaluate to lambda abstractions

For every closed term $f$ of a function
type $A \Rightarrow B$ there is a term $b$ of type $B$ in the context with a single variable of
type $A$ such that $f$ reduces, in zero or more call-by-value steps, to the lambda abstraction
with body $b$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.closed_function_evaluates_to_lam`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#closed-function-evaluates-to-lam).

## No closed terms of base type

In the pure, constant-free calculus there is no closed
term whose type is a base type.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.no_closed_base`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#no-closed-base).

## Closed terms with the same result

Two closed terms $t$ and $u$ of the same type have the
same result when there is a value $v$ such that both $t$ and $u$ reduce to $v$ in zero or more
call-by-value steps.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SameResult`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#same-result).

## Reflexivity of having the same result

Every closed term has the same result as
itself.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SameResult.refl`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#refl).

## Symmetry of having the same result

If closed terms $t$ and $u$ have the same result,
then $u$ and $t$ have the same result.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SameResult.symm`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#symm).

## Transitivity of having the same result

If closed terms $t$ and $u$ have the same result,
and $u$ and a closed term $v$ have the same result, then $t$ and $v$ have the same result.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SameResult.trans`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#trans).

## Evaluation preserves the result of a closed term

If a closed term $t$ reduces to a
term $u$ in zero or more call-by-value steps, then $t$ and $u$ have the same result.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SameResult.of_steps`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#of-steps).

## Left expansion preserves having the same result

Let $t$, $t'$ and $u$ be closed terms of
the same type. If $t$ reduces to $t'$ in zero or more call-by-value steps, and $t'$ and $u$ have
the same result, then $t$ and $u$ have the same result.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SameResult.anti_left`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#anti-left).

## Right expansion preserves having the same result

Let $t$, $u$ and $u'$ be closed terms
of the same type. If $u$ reduces to $u'$ in zero or more call-by-value steps, and $t$ and $u'$
have the same result, then $t$ and $u$ have the same result.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SameResult.anti_right`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#anti-right).

## Application preserves having the same result

Let $f$ and $g$ be closed terms of a
function type $A \Rightarrow B$, and let $a$ and $b$ be closed terms of type $A$. If $f$ and $g$
have the same result and $a$ and $b$ have the same result, then the applications $f\,a$ and
$g\,b$ have the same result.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.SameResult.app`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#app).

## Having the same result is an equivalence relation

For every simple type $A$, the
relation of having the same result is an equivalence relation on the closed terms of type $A$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.sameResult_equivalence`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Normalization.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html#same-result-equivalence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Normalization of the simply typed lambda calculus](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/normalization-of-the-simply-typed-lambda-calculu)
