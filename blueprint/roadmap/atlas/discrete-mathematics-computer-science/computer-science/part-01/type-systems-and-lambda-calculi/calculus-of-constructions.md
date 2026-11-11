---
declaration: section
origin: cited
lean: MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.Srt, MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.Tm, MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.lift, MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.subst, MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.Step, MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.Conv, MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.Ax, MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.Rl
statement: formalized
---

# Calculus of constructions

17 results, 11 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/calculus-of-constructions/index.html).

## Sorts of CCω

The sorts are $\mathrm{Prop}$ and $\mathrm{Type}_i$ for every natural number
$i$. In the calculus, $\mathrm{Prop}$ is impredicative and the $\mathrm{Type}_i$ form a
predicative hierarchy.

Formalized by `MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.Srt`, an inductive type declared in [WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/calculus-of-constructions/index.html#srt).

## Terms of the calculus of constructions

A term is a variable $\#i$ with de Bruijn index
$i \in \mathbb{N}$, a sort $s$ (either $\mathrm{Prop}$ or $\mathrm{Type}_i$ for some
$i \in \mathbb{N}$), an application $f\,a$ of a term $f$ to a term $a$, an abstraction
$\lambda (x : A).\, b$ with domain $A$ and body $b$, or a dependent product
$\Pi (x : A).\, B$ with domain $A$ and codomain $B$.

In the body of an abstraction or the codomain of a product, index $0$ refers to the bound
variable and index $i + 1$ to the variable that has index $i$ outside the binder.

Formalized by `MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.Tm`, an inductive type declared in [WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/calculus-of-constructions/index.html#tm).

## Shifting de Bruijn indices

For natural numbers $d$ and $c$, shifting a term $t$ by $d$
above the cutoff $c$ adds $d$ to every variable index $i \ge c$ and leaves every index $i < c$
unchanged. The cutoff goes up by one under each binder, that is, in the body of a $\lambda$ and
in the codomain of a $\Pi$ (not in the type annotation or the domain), and sorts are unchanged.
Thus the free variables of $t$ with index at least $c$ are increased by $d$.

Formalized by `MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.lift`, a definition declared in [WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/calculus-of-constructions/index.html#lift).

## Substitution for a de Bruijn variable

For $k \in \mathbb{N}$ and terms $u$ and $t$, the
term $t[k := u]$ is defined by recursion on $t$. For a variable, $\#i[k := u]$ is $\#i$ if
$i < k$, is $u$ with every free variable raised by $k$ if $i = k$, and is $\#(i - 1)$ if
$i > k$. A sort is unchanged, $(f\,a)[k := u] = f[k := u]\,a[k := u]$,
$(\lambda (x : A).\, b)[k := u] = \lambda (x : A[k := u]).\, b[k + 1 := u]$, and
$(\Pi (x : A).\, B)[k := u] = \Pi (x : A[k := u]).\, B[k + 1 := u]$.

Formalized by `MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.subst`, a definition declared in [WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/calculus-of-constructions/index.html#subst).

## One-step beta reduction

One-step beta reduction is the smallest relation on terms that
contains every beta step $(\lambda (x : A).\, b)\, a \to b[a/x]$, where $b[a/x]$ substitutes $a$
for the bound variable $x$ in $b$, and that is closed under every term former: a step inside the
function or the argument of an application, inside the type annotation or the body of a
$\lambda$, or inside the domain or the codomain of a $\Pi$ is a step of the whole term.

Formalized by `MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.Step`, an inductive type declared in [WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/calculus-of-constructions/index.html#step).

## Beta conversion

Beta conversion is the equivalence closure of one-step beta reduction:
every term is convertible to itself, and if $t$ is convertible to $u$ and $u$ reduces to $v$ in
one step, or $v$ reduces to $u$ in one step, then $t$ is convertible to $v$.

Formalized by `MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.Conv`, an inductive type declared in [WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/calculus-of-constructions/index.html#conv).

## Sort axioms of CCω

The axioms say which sort has which sort as its type: $\mathrm{Prop}$
has type $\mathrm{Type}_0$, and $\mathrm{Type}_i$ has type $\mathrm{Type}_{i+1}$ for every natural
number $i$. No other pair of sorts is related.

Formalized by `MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.Ax`, an inductive type declared in [WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/calculus-of-constructions/index.html#ax).

## Product rules of CCω

The product rules say in which sort $s_3$ a dependent product
$\Pi (x : A).\, B$ lives when $A$ lives in the sort $s_1$ and $B$ lives in the sort $s_2$. There
are exactly three rules: for every sort $s$, a product with domain in $s$ and codomain in
$\mathrm{Prop}$ lives in $\mathrm{Prop}$ (the impredicativity of $\mathrm{Prop}$); for all natural
numbers $i$ and $j$, a product with domain in $\mathrm{Type}_i$ and codomain in $\mathrm{Type}_j$
lives in $\mathrm{Type}_{\max(i, j)}$; and for every natural number $i$, a product with domain in
$\mathrm{Prop}$ and codomain in $\mathrm{Type}_i$ lives in $\mathrm{Type}_i$.

Formalized by `MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.Rl`, an inductive type declared in [WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/calculus-of-constructions/index.html#rl).

## Well-formed contexts

A context is a list of terms whose head is the most recent binding.
Well-formedness of contexts is defined together with the typing judgement
$\Gamma \vdash t : A$ as the least predicate such that the empty context is well formed, and
if $\Gamma$ is well formed and $\Gamma \vdash A : s$ for some sort $s$, then the context
obtained from $\Gamma$ by adding $A$ at the head is well formed.

Formalized by `MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.Wf`, an inductive type declared in [WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/calculus-of-constructions/index.html#wf).

## Typing judgement of the calculus of constructions with universes

A context $\Gamma$ is a
list of terms whose head is the type of the most recent variable; write $\Gamma, A$ for
$\Gamma$ extended by $A$ at the head. The judgement $\Gamma \vdash t : A$ ($t$ has type $A$
in $\Gamma$) is defined together with well-formedness of contexts as the least relation
closed under the following rules.

* Sorts: if $\Gamma$ is well formed and $s : s'$ is an axiom, namely
  $\mathrm{Prop} : \mathrm{Type}_0$ or $\mathrm{Type}_i : \mathrm{Type}_{i+1}$, then
  $\Gamma \vdash s : s'$.
* Variables: if $\Gamma$ is well formed and its entry at position $i$ (counting from $0$ at
  the head) is $A$, then $\Gamma \vdash \#i : A'$, where $A'$ is $A$ with every free variable
  raised by $i + 1$.
* Products: if $\Gamma \vdash A : s_1$, $\Gamma, A \vdash B : s_2$ and $(s_1, s_2, s_3)$ is a
  product rule, namely $(s, \mathrm{Prop}, \mathrm{Prop})$ for a sort $s$,
  $(\mathrm{Type}_i, \mathrm{Type}_j, \mathrm{Type}_{\max(i, j)})$ or
  $(\mathrm{Prop}, \mathrm{Type}_i, \mathrm{Type}_i)$, then
  $\Gamma \vdash \Pi (x : A).\, B : s_3$.
* Abstractions: if $\Gamma \vdash \Pi (x : A).\, B : s$ for some sort $s$ and
  $\Gamma, A \vdash b : B$, then $\Gamma \vdash \lambda (x : A).\, b : \Pi (x : A).\, B$.
* Applications: if $\Gamma \vdash f : \Pi (x : A).\, B$ and $\Gamma \vdash a : A$, then
  $\Gamma \vdash f\,a : B[a]$, where $B[a]$ replaces variable $0$ of $B$ by $a$ and lowers
  the other free variables of $B$ by one.
* Conversion: if $\Gamma \vdash t : A$, $\Gamma \vdash B : s$ for some sort $s$, and $A$ and
  $B$ are beta convertible, then $\Gamma \vdash t : B$.

Formalized by `MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.Typing`, an inductive type declared in [WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/calculus-of-constructions/index.html#typing).

## Strongly normalizing terms

The strongly normalizing terms are defined inductively: a term
$t$ is strongly normalizing when every term to which $t$ reduces in one beta step is strongly
normalizing. Equivalently, classically, there is no infinite chain of one-step beta reductions
starting from $t$.

Formalized by `MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.SN`, a definition declared in [WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/calculus-of-constructions/index.html#sn).

## Typing the polymorphic identity

In the empty context, the polymorphic identity
$\lambda (A : \mathrm{Prop}).\, \lambda (x : A).\, x$ has type
$\Pi (A : \mathrm{Prop}).\, \Pi (x : A).\, A$.

This is typable only because $\mathrm{Prop}$ is impredicative: a product over
$A : \mathrm{Prop}$ whose codomain is a proposition is again a proposition.

## Sources

- Coquand and Huet, 'The calculus of constructions' (1988); Zhaohui Luo, 'An Extended Calculus of Constructions' (1990); Bruno Barras, 'Sets in Coq, Coq in Sets' (2010). Problem `coc_strong_normalization` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.typing_polyId` is written with `theorem_wanted` in [WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/calculus-of-constructions/index.html#typing-poly-id).

## Typing the polymorphic identity applied to falsity

Write $\bot$ for
$\Pi (P : \mathrm{Prop}).\, P$. In the empty context, the application of the polymorphic
identity $\lambda (A : \mathrm{Prop}).\, \lambda (x : A).\, x$ to $\bot$ has type
$\Pi (x : \bot).\, \bot$.

## Sources

- Coquand and Huet, 'The calculus of constructions' (1988); Zhaohui Luo, 'An Extended Calculus of Constructions' (1990); Bruno Barras, 'Sets in Coq, Coq in Sets' (2010). Problem `coc_strong_normalization` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.typing_polyId_app` is written with `theorem_wanted` in [WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/calculus-of-constructions/index.html#typing-poly-id-app).

## Beta step of the applied polymorphic identity

The polymorphic identity
$\lambda (A : \mathrm{Prop}).\, \lambda (x : A).\, x$ applied to
$\bot = \Pi (P : \mathrm{Prop}).\, P$ reduces in one beta step to $\lambda (x : \bot).\, x$.

This is an anti-vacuity guard: it pins down beta reduction and substitution.

## Sources

- Coquand and Huet, 'The calculus of constructions' (1988); Zhaohui Luo, 'An Extended Calculus of Constructions' (1990); Bruno Barras, 'Sets in Coq, Coq in Sets' (2010). Problem `coc_strong_normalization` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.step_polyId_app` is written with `theorem_wanted` in [WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/calculus-of-constructions/index.html#step-poly-id-app).

## Subject reduction

Let $\Gamma$ be a context and $t$, $t'$, $A$ terms of the calculus
of constructions with universes. If $t$ has type $A$ in $\Gamma$, that is
$\Gamma \vdash t : A$, and $t$ reduces to $t'$ in one step of beta reduction (anywhere
inside $t$), then $\Gamma \vdash t' : A$.

## Sources

- Coquand and Huet, 'The calculus of constructions' (1988); Zhaohui Luo, 'An Extended Calculus of Constructions' (1990); Bruno Barras, 'Sets in Coq, Coq in Sets' (2010). Problem `coc_strong_normalization` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.subject_reduction` is written with `theorem_wanted` in [WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/calculus-of-constructions/index.html#subject-reduction).

## Strong normalization of CCω

Every well-typed term is strongly normalizing: if
$\Gamma \vdash t : A$ for some context $\Gamma$ and some term $A$, then $t$ is strongly
normalizing.

## Sources

- Coquand and Huet, 'The calculus of constructions' (1988); Zhaohui Luo, 'An Extended Calculus of Constructions' (1990); Bruno Barras, 'Sets in Coq, Coq in Sets' (2010). Problem `coc_strong_normalization` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.strong_normalization` is written with `theorem_wanted` in [WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/calculus-of-constructions/index.html#strong-normalization).

## Consistency of CCω

No closed term has type $\Pi (P : \mathrm{Prop}).\, P$: there is no term
$t$ with $\vdash t : \Pi (P : \mathrm{Prop}).\, P$ in the empty context.

## Sources

- Coquand and Huet, 'The calculus of constructions' (1988); Zhaohui Luo, 'An Extended Calculus of Constructions' (1990); Bruno Barras, 'Sets in Coq, Coq in Sets' (2010). Problem `coc_strong_normalization` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.TheoryOfComputation.CoCStrongNormalizationWanted.ProgramVerification.CoCStrongNormalization.consistency` is written with `theorem_wanted` in [WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/CoCStrongNormalizationWanted.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/calculus-of-constructions/index.html#consistency).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Calculus of constructions](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/calculus-of-constructions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/calculus-of-constructions)
