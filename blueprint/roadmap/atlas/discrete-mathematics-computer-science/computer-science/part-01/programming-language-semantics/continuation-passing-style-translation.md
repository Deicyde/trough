---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.Stlc.CPS.cbnTy, Cslib.Languages.LambdaCalculus.Stlc.CPS.cbnComp, Cslib.Languages.LambdaCalculus.Stlc.CPS.cbnVar, Cslib.Languages.LambdaCalculus.Stlc.CPS.cbn, Cslib.Languages.LambdaCalculus.Stlc.CPS.CbnRel, Cslib.Languages.LambdaCalculus.Stlc.CPS.CbnCompRel, Cslib.Languages.LambdaCalculus.Stlc.CPS.CbnEnvRel, Cslib.Languages.LambdaCalculus.Stlc.CPS.cbn_correct
statement: formalized
proof: formalized
---

# Continuation-passing style translation

42 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html).

## Call-by-name CPS translation of types

Fix an answer type $R$ of the simply typed lambda
calculus. The call-by-name CPS translation $A^\ast$ of a simple type $A$ is defined by recursion
on $A$: a base type is translated to itself, $b^\ast = b$, and a function type is translated by
$(A \to B)^\ast = ((A^\ast \to R) \to R) \to ((B^\ast \to R) \to R)$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cbnTy`, a definition declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByName.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByName.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cbn-ty).

## Computation types of the call-by-name CPS translation

For an answer type $R$ and a simple
type $A$, the type of call-by-name computations of type $A$ is $C(A) = (A^\ast \to R) \to R$,
where $A^\ast$ is the call-by-name CPS translation of $A$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cbnComp`, an abbreviation declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByName.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByName.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cbn-comp).

## Call-by-name CPS translation of variables

Fix an answer type $R$ and write
$C(A) = (A^\ast \to R) \to R$, where $A^\ast$ is the call-by-name CPS translation of a simple
type $A$. A variable of type $A$ in a context $A_1, \dots, A_n$ is translated to the variable at
the same position in the translated context $C(A_1), \dots, C(A_n)$, where it has type $C(A)$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cbnVar`, a definition declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByName.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByName.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cbn-var).

## Call-by-name CPS translation of terms

Fix an answer type $R$ and write
$C(A) = (A^\ast \to R) \to R$, where $A^\ast$ is the call-by-name CPS translation of a simple
type $A$. A term $t$ of type $A$ in a context $A_1, \dots, A_n$ is translated to a term
$\overline{t}$ of type $C(A)$ in the context $C(A_1), \dots, C(A_n)$, by recursion on $t$: a
variable $x$ is translated to the variable at the same position; an abstraction by
$\overline{\lambda x.\, M} = \lambda k.\, k\,(\lambda x.\, \overline{M})$; and an application by
$\overline{M\,N} = \lambda k.\, \overline{M}\,(\lambda m.\, m\,\overline{N}\,k)$, where $k$ and
$m$ are fresh variables.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cbn`, a definition declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByName.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByName.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cbn).

## Logical relation for the call-by-name CPS translation

Fix an answer type $R$ and an
interpretation $I$ of the base types. Write $D(A)$ for the set of values of a simple type $A$
($D(b) = I(b)$ for a base type $b$, and $D(A \to B)$ is the set of functions from $D(A)$ to
$D(B)$), $A^\ast$ for the call-by-name CPS translation of $A$, and
$C(A) = (A^\ast \to R) \to R$. The relation $a \sim_A a'$ between $a \in D(A)$ and
$a' \in D(A^\ast)$ is defined by recursion on $A$. At a base type $b$, $a \sim_b a'$ holds when
$a = a'$. At a function type, $f \sim_{A \to B} g$ holds when for every $a \in D(A)$ and every
$c \in D(C(A))$: if there is $v$ with $a \sim_A v$ and $c\,k = k\,v$ for every
$k \in D(A^\ast \to R)$, then there is $w$ with $f\,a \sim_B w$ and $g\,c\,k = k\,w$ for every
$k \in D(B^\ast \to R)$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.CbnRel`, a definition declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByName.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByName.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cbn-rel).

## Related computations in the call-by-name CPS translation

Fix an answer type $R$ and an
interpretation $I$ of the base types; write $D(A)$ for the set of values of a simple type $A$,
$A^\ast$ for its call-by-name CPS translation, $C(A) = (A^\ast \to R) \to R$, and $\sim_A$ for
the call-by-name logical relation between $D(A)$ and $D(A^\ast)$. A computation $c \in D(C(A))$
is related to a value $a \in D(A)$ when there is $v \in D(A^\ast)$ with $a \sim_A v$ such that
$c\,k = k\,v$ for every continuation $k \in D(A^\ast \to R)$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.CbnCompRel`, a definition declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByName.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByName.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cbn-comp-rel).

## Related environments for the call-by-name CPS translation

Fix an answer type $R$ and an
interpretation of the base types, and write $C(A) = (A^\ast \to R) \to R$, where $A^\ast$ is the
call-by-name CPS translation of a simple type $A$. Let $\eta$ be an environment for a context
$\Gamma = A_1, \dots, A_n$, assigning to each variable $x$ of type $A$ a value $\eta(x)$ of type
$A$, and let $\eta'$ be an environment for the translated context $C(A_1), \dots, C(A_n)$. Then
$\eta$ and $\eta'$ are related when for every variable $x$ of $\Gamma$, of type $A$ say, the
value that $\eta'$ assigns to the variable at the same position as $x$ in the translated context
is a computation of type $C(A)$ related to $\eta(x)$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.CbnEnvRel`, a definition declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByName.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByName.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cbn-env-rel).

## Denotational correctness of the call-by-name CPS translation

Fix an answer type $R$ and
an interpretation of the base types; write $D(A)$ for the set of values of a simple type $A$,
$A^\ast$ for its call-by-name CPS translation, and $\sim_A$ for the call-by-name logical
relation. Let $t$ be a term of type $A$ in a context $\Gamma$, and let $\eta$ be an environment
for $\Gamma$ and $\eta'$ an environment for the translated context such that $\eta$ and $\eta'$
are related. Let $a \in D(A)$ be the denotation of $t$ in $\eta$, and let $c$ be the denotation
in $\eta'$ of the call-by-name CPS translation $\overline{t}$ of $t$. Then there is
$v \in D(A^\ast)$ with $a \sim_A v$ such that $c\,k = k\,v$ for every continuation
$k \in D(A^\ast \to R)$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cbn_correct`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByName.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByName.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cbn-correct).

## The call-by-name CPS translation at base types

Fix an answer type $R$ and an
interpretation of the base types. Let $t$ be a term of a base type $b$ in a context $\Gamma$, let
$\eta$ be an environment for $\Gamma$, and let $\eta'$ be an environment for the translated
context related to $\eta$. Then for every continuation $k$ from the values of type $b$ to the
values of type $R$, the denotation in $\eta'$ of the call-by-name CPS translation $\overline{t}$
of $t$, applied to $k$, equals $k$ applied to the denotation of $t$ in $\eta$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cbn_denote_base`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByName.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByName.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cbn-denote-base).

## Running the call-by-name CPS translation with the identity continuation

Fix an
interpretation of the base types. Let $t$ be a term of a base type $b$ in a context $\Gamma$, take
the answer type to be $b$, let $\eta$ be an environment for $\Gamma$, and let $\eta'$ be an
environment for the translated context related to $\eta$. Then the denotation in $\eta'$ of the
call-by-name CPS translation $\overline{t}$ of $t$, applied to the identity function on the values
of type $b$, equals the denotation of $t$ in $\eta$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cbn_denote_base_id`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByName.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByName.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cbn-denote-base-id).

## Call-by-value CPS translation of types

For a fixed answer type $R$, the translation
$\overline{A}$ of a simple type $A$ is defined by recursion on $A$: $\overline{b} = b$ for a base
type $b$, and $\overline{A \to B} = \overline{A} \to ((\overline{B} \to R) \to R)$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cpsTy`, a definition declared in [CSLibExt/Languages/LambdaCalculus/CPS/Translation.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Translation.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cps-ty).

## CPS computation type

For an answer type $R$ and a simple type $A$, the type of CPS
computations returning a value of type $A$ is $(\overline{A} \to R) \to R$, where $\overline{A}$
is the call-by-value CPS translation of $A$ for answer type $R$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.compTy`, an abbreviation declared in [CSLibExt/Languages/LambdaCalculus/CPS/Translation.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Translation.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#comp-ty).

## CPS translation of variables

Fix an answer type $R$ and write $\overline{A}$ for the
call-by-value CPS translation of a type $A$. A de Bruijn variable of type $A$ in a context
$A_1, \ldots, A_n$ is sent to the variable at the same position in the translated context
$\overline{A_1}, \ldots, \overline{A_n}$, which has type $\overline{A}$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cpsVar`, a definition declared in [CSLibExt/Languages/LambdaCalculus/CPS/Translation.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Translation.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cps-var).

## Call-by-value CPS translation of terms

Fix an answer type $R$ and write $\overline{A}$
for the call-by-value CPS translation of a type $A$ and $\overline{\Gamma}$ for the context
obtained by translating each type of a context $\Gamma$. A term $M$ of type $A$ in context
$\Gamma$ is sent to a term $\overline{M}$ of type $(\overline{A} \to R) \to R$ in context
$\overline{\Gamma}$, defined by recursion on $M$ by $\overline{x} = \lambda k.\,k\,x$,
$\overline{\lambda x.\,M} = \lambda k.\,k\,(\lambda x.\,\overline{M})$ and
$\overline{M\,N} = \lambda k.\,\overline{M}\,(\lambda m.\,\overline{N}\,(\lambda n.\,m\,n\,k))$,
where $k$, $m$ and $n$ are fresh variables.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cps`, a definition declared in [CSLibExt/Languages/LambdaCalculus/CPS/Translation.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Translation.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cps).

## Logical relation for the CPS translation

Fix an answer type $R$ and an interpretation
$I$ of the base types; write $D(A)$ for the set interpreting a simple type $A$ under $I$ and
$\overline{A}$ for the call-by-value CPS translation of $A$. The relation $a \sim_A a'$ between
$a \in D(A)$ and $a' \in D(\overline{A})$ is defined by recursion on $A$: at a base type $b$,
$a \sim_b a'$ means $a = a'$; at a function type, $f \sim_{A \to B} f'$ means that for all
$a \sim_A a'$ there is a $b' \in D(\overline{B})$ with $f(a) \sim_B b'$ and $f'(a')(k) = k(b')$
for every continuation $k \in D(\overline{B} \to R)$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.Rel`, a definition declared in [CSLibExt/Languages/LambdaCalculus/CPS/Translation.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Translation.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#rel).

## Related environments

Fix an answer type $R$ and an interpretation $I$ of the base types,
and write $\overline{\Gamma}$ for the context obtained by translating each type of a context
$\Gamma$ by the call-by-value CPS translation. An environment $\eta$ for $\Gamma$ and an
environment $\eta'$ for $\overline{\Gamma}$ are related when, for every variable $x$ of type $A$
in $\Gamma$, the value $\eta(x)$ is related at type $A$, by the CPS logical relation, to the value
that $\eta'$ assigns to the variable at the same position in $\overline{\Gamma}$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.EnvRel`, a definition declared in [CSLibExt/Languages/LambdaCalculus/CPS/Translation.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Translation.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#env-rel).

## Denotational correctness of the CPS translation (Meyer–Wand)

Fix an answer type $R$
and an interpretation $I$ of the base types; write $D(A)$ for the set interpreting a type $A$,
$\overline{A}$, $\overline{\Gamma}$ and $\overline{t}$ for the call-by-value CPS translations of
types, contexts and terms, and $[t]_\eta$ for the denotation of a term $t$ in an environment
$\eta$. Let $t$ be a term of type $A$ in context $\Gamma$, and let $\eta$ and $\eta'$ be related
environments for $\Gamma$ and $\overline{\Gamma}$. Then there is a value $v' \in D(\overline{A})$,
related to $[t]_\eta$ by the CPS logical relation at $A$, such that $[\overline{t}]_{\eta'}(k) =
k(v')$ for every continuation $k \colon D(\overline{A}) \to D(R)$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cps_correct`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/Translation.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Translation.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cps-correct).

## CPS translation at a base type

Fix an answer type $R$ and an interpretation $I$ of the
base types; write $D(A)$ for the set interpreting a type $A$, $\overline{\Gamma}$ and
$\overline{t}$ for the call-by-value CPS translations of contexts and terms, and $[t]_\eta$ for
the denotation of a term $t$ in an environment $\eta$. Let $t$ be a term of base type $b$ in
context $\Gamma$, and let $\eta$ and $\eta'$ be related environments for $\Gamma$ and
$\overline{\Gamma}$. Then $[\overline{t}]_{\eta'}(k) = k([t]_\eta)$ for every continuation
$k \colon I(b) \to D(R)$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cps_denote_base`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/Translation.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Translation.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cps-denote-base).

## CPS translation at a base type with the identity continuation

Fix an interpretation $I$
of the base types, let $t$ be a term of base type $b$ in context $\Gamma$, and take the answer
type to be $b$; write $\overline{\Gamma}$ and $\overline{t}$ for the call-by-value CPS
translations of $\Gamma$ and $t$, and $[t]_\eta$ for the denotation of $t$ in an environment
$\eta$. If $\eta$ and $\eta'$ are related environments for $\Gamma$ and $\overline{\Gamma}$, then
$[\overline{t}]_{\eta'}(\mathrm{id}) = [t]_\eta$, where $\mathrm{id}$ is the identity on $I(b)$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cps_denote_base_id`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/Translation.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Translation.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cps-denote-base-id).

## Translated renaming

Fix an answer type $R$ and write $\llbracket \Gamma \rrbracket$ for the
context obtained by applying the call-by-value CPS type translation to every entry of $\Gamma$. A
renaming $\rho$ from $\Gamma$ to $\Delta$ induces the renaming from $\llbracket \Gamma \rrbracket$
to $\llbracket \Delta \rrbracket$ that sends the translation of each variable $x$ of $\Gamma$ (the
variable at the same position) to the translation of $\rho(x)$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cpsRen`, a definition declared in [CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cps-ren).

## The call-by-value CPS translation commutes with renaming

Fix an answer type $R$ and
write $\llbracket \cdot \rrbracket$ for the call-by-value CPS translation of types, contexts
(entrywise) and terms. For every renaming $\rho$ from a context $\Gamma$ to a context $\Delta$ and
every term $t$ of type $A$ in $\Gamma$, the translation of the renamed term $t[\rho]$ equals the
renaming of $\llbracket t \rrbracket$ along the translated renaming from
$\llbracket \Gamma \rrbracket$ to $\llbracket \Delta \rrbracket$, which sends the translation of
each variable $x$ of $\Gamma$ to the translation of $\rho(x)$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cps_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cps-rename).

## The CPS translation commutes with weakening

Fix an answer type $R$ and write
$\llbracket \cdot \rrbracket$ for the call-by-value CPS translation of types, contexts (entrywise)
and terms. For every term $t$ of type $A$ in a context $\Gamma$ and every type $B$, the translation
of the weakening of $t$ to the context $B, \Gamma$ is the weakening of $\llbracket t \rrbracket$ to
the context $\llbracket B \rrbracket, \llbracket \Gamma \rrbracket$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cps_weaken`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cps-weaken).

## Plotkin's value translation $\Psi$

Fix an answer type $R$, and write $A^*$ for the
call-by-value CPS translation of a type $A$, $\Gamma^*$ for the context obtained by translating
each type of a context $\Gamma$, and $\overline{M}$ for the CPS translation of a term $M$. The
relation $\Psi$ between terms of type $A$ in context $\Gamma$ and terms of type $A^*$ in context
$\Gamma^*$ holds in exactly two cases: a variable $x$ of $\Gamma$ is related to the variable at
the same position in $\Gamma^*$, and an abstraction $\lambda x.\, N$ is related to
$\lambda x.\, \overline{N}$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.PsiRel`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#psi-rel).

## The CPS translation commutes with substitution of values and variables

Fix an answer
type $R$ and write $\llbracket \cdot \rrbracket$ for the call-by-value CPS translation of types,
contexts (entrywise) and terms; for a variable $x$ of $\Gamma$, $\llbracket x \rrbracket$ is the
variable of $\llbracket \Gamma \rrbracket$ at the same position. Let $\sigma$ be a substitution from
$\Gamma$ to $\Delta$ and $\tau$ a substitution from $\llbracket \Gamma \rrbracket$ to
$\llbracket \Delta \rrbracket$ such that for every variable $x$ of $\Gamma$, the term
$\tau(\llbracket x \rrbracket)$ is related to $\sigma(x)$ by the value translation $\Psi$ (a
variable is related to the corresponding variable, $\lambda y. N$ to
$\lambda y. \llbracket N \rrbracket$). Then for every term $M$ in $\Gamma$, writing $M[\sigma]$
for the result of applying $\sigma$ to $M$, we have
$\llbracket M[\sigma] \rrbracket = \llbracket M \rrbracket[\tau]$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cps_subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cps-subst).

## The CPS translation commutes with instantiation by a value or variable

Fix an answer
type $R$ and write $\llbracket \cdot \rrbracket$ for the call-by-value CPS translation of types,
contexts (entrywise) and terms. Let $N$ be a term of type $B$ in a context $A, \Gamma$, let $v$
be a term of type $A$ in $\Gamma$, and let $p$ be a term of type $\llbracket A \rrbracket$ in
$\llbracket \Gamma \rrbracket$ related to $v$ by the value translation $\Psi$ (a variable is related
to the corresponding variable, $\lambda x. M$ to $\lambda x. \llbracket M \rrbracket$). Writing
$N[u]$ for $N$ with its newest free variable replaced by $u$, we have
$\llbracket N[v] \rrbracket = \llbracket N \rrbracket[p]$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cps_instantiate`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cps-instantiate).

## The value translation preserves values

Fix an answer type $R$. If a term $v$ of type $A$
in context $\Gamma$ is related by Plotkin's value translation $\Psi$ to a term $p$ (of the
translated type in the translated context), and $v$ is a value, that is, a $\lambda$-abstraction,
then $p$ is a value.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.PsiRel.value`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#value).

## A β-redex with a value argument evaluates as its contractum

Let $N$ be a term of type $D$
in a context $C, \Xi$ and let $v$ be a value of type $C$ in $\Xi$. Writing $N[v]$ for $N$ with its
newest free variable replaced by $v$, for every term $w$ of type $D$ the application
$(\lambda x. N)\, v$ evaluates to $w$ under call-by-value big-step evaluation if and only if $N[v]$
evaluates to $w$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.eval_app_lam_iff`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#eval-app-lam-iff).

## Evaluation of an application depends on the function only through its results

Let $F$
and $F'$ be terms of type $C \to D$ in a context $\Xi$ such that, for every term $u$, $F$ evaluates
to $u$ under call-by-value big-step evaluation if and only if $F'$ does. Then for every term $a$ of
type $C$ and every term $w$ of type $D$ in $\Xi$, the application $F\, a$ evaluates to $w$ if and
only if $F'\, a$ evaluates to $w$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.eval_app_congr_fun`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#eval-app-congr-fun).

## Instantiating a return to the continuation

Let $V$ be a term of type $X$ and $K$ a term
of type $X \to Z$ in a context $\Xi$. In the context $X \to Z, \Xi$, let $k$ be the newest
variable (of type $X \to Z$) and $V'$ the weakening of $V$. Replacing $k$ by $K$ in the term
$k\, V'$ gives $K\, V$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.instantiate_ret`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#instantiate-ret).

## Plotkin's simulation theorem, big-step form

Fix an answer type $R$ and write
$\llbracket \cdot \rrbracket$ for the call-by-value CPS translation of types, contexts (entrywise)
and terms. If a term $M$ of type $A$ in a context $\Gamma$ evaluates to $V$ under call-by-value
big-step evaluation, then there is a term $p$ related to $V$ by the value translation $\Psi$ (a
variable is related to the corresponding variable, $\lambda x. N$ to
$\lambda x. \llbracket N \rrbracket$) such that for every value $K$ of type
$\llbracket A \rrbracket \to R$ in $\llbracket \Gamma \rrbracket$ and every term $w$, the
application $\llbracket M \rrbracket\, K$ evaluates to $w$ if and only if $K\, p$ evaluates
to $w$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cps_simulation`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cps-simulation).

## Simulation for terms evaluating to an abstraction

Fix an answer type $R$ and write
$\llbracket \cdot \rrbracket$ for the call-by-value CPS translation of types, contexts (entrywise)
and terms. If a term $M$ of type $A \to B$ in a context $\Gamma$ evaluates to $\lambda x. N$ under
call-by-value big-step evaluation, then for every value $K$ of type
$\llbracket A \to B \rrbracket \to R$ in $\llbracket \Gamma \rrbracket$ and every term $w$ of type
$R$, the application $\llbracket M \rrbracket\, K$ evaluates to $w$ if and only if
$K\, (\lambda x. \llbracket N \rrbracket)$ evaluates to $w$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cps_simulation_lam`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/Simulation.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cps-simulation-lam).

## Call-by-name big-step evaluation

Call-by-name big-step evaluation $M \Downarrow_n V$
of the simply typed $\lambda$-calculus relates two terms of the same type in the same context
$\Gamma$. It is the least relation closed under two rules: every abstraction $\lambda x.\,N$
evaluates to itself, and if $f \Downarrow_n \lambda x.\,N$ and $N[a/x] \Downarrow_n v$, then
$f\,a \Downarrow_n v$. The argument $a$ is substituted for $x$ without being evaluated.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.EvalN`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#eval-n).

## The call-by-name CPS translation of a renaming

Fix an answer type $R$. The translation
of a context $\Gamma$ replaces each type $A$ in it by the computation type $(A^* \to R) \to R$,
where $A^*$ is the call-by-name translation of $A$, and a variable $x$ of $\Gamma$ becomes the
variable $\overline{x}$ at the same position of the translated context. A renaming $\rho$ from
$\Gamma$ to $\Delta$, a type-preserving map from the variables of $\Gamma$ to those of $\Delta$,
is transported to the renaming $\overline{\rho}$ of the translated contexts with
$\overline{\rho}(\overline{x}) = \overline{\rho(x)}$ for every variable $x$ of $\Gamma$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cbnRen`, a definition declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cbn-ren).

## The call-by-name CPS translation commutes with renaming

Fix an answer type $R$ and write
$\overline{t}$ for the call-by-name CPS translation of a term $t$. For a renaming $\rho$ from a
context $\Gamma$ to a context $\Delta$, let $\overline{\rho}$ be the renaming of the translated
contexts that sends the translation of each variable $x$ of $\Gamma$ to the translation of
$\rho(x)$. Then for every term $t$ in context $\Gamma$, the translation of the renamed term
$t[\rho]$ is the renaming of $\overline{t}$ by $\overline{\rho}$:
$\overline{t[\rho]} = \overline{t}[\overline{\rho}]$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cbn_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cbn-rename).

## The call-by-name CPS translation commutes with weakening

Fix an answer type $R$ and write
$\overline{t}$ for the call-by-name CPS translation of a term $t$. For every term $t$ in a context
$\Gamma$ and every type $B$, translating the weakening of $t$ to the context $B, \Gamma$ (which
adds a fresh newest variable of type $B$) gives the weakening of $\overline{t}$ to the translated
context, which adds a fresh newest variable of the translated type
$(B^* \to R) \to R$, where $B^*$ is the call-by-name translation of $B$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cbn_weaken`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cbn-weaken).

## The call-by-name CPS translation commutes with substitution

Fix an answer type $R$ and
write $\overline{t}$ for the call-by-name CPS translation of a term $t$ and $\overline{x}$ for the
translation of a variable $x$, the variable at the same position of the translated context. Let
$\sigma$ be a substitution from a context $\Gamma$ to a context $\Delta$ (assigning to each
variable of $\Gamma$ a term of the same type in context $\Delta$), and let $\tau$ be a
substitution from the translated context of $\Gamma$ to that of $\Delta$ such that
$\tau(\overline{x}) = \overline{\sigma(x)}$ for every variable $x$ of $\Gamma$. Then for every
term $t$ in context $\Gamma$, $\overline{t[\sigma]} = \overline{t}[\tau]$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cbn_subst`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cbn-subst).

## The call-by-name CPS translation commutes with instantiation

Fix an answer type $R$ and
write $\overline{t}$ for the call-by-name CPS translation of a term $t$. Let $N$ be a term of type
$B$ in a context $A, \Gamma$ whose newest variable $x$ has type $A$, and let $a$ be a term of type
$A$ in context $\Gamma$. Then translating the instantiation $N[a/x]$ of $x$ by $a$ gives the
instantiation of the newest variable of $\overline{N}$ by $\overline{a}$:
$\overline{N[a/x]} = \overline{N}[\overline{a}/x]$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cbn_instantiate`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cbn-instantiate).

## The translation of a closed term is a value

Fix an answer type $R$. For every closed term
$t$, the call-by-name CPS translation of $t$ is a value, that is, a $\lambda$-abstraction.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cbn_value`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cbn-value).

## Administrative step of the call-by-name translation of an application

Let $\Xi$ be a
context and $W$, $V$, $Z$ types, and write $t^{\uparrow}$ for the weakening of a term $t$ by one
new newest variable. Let $F$ be a term of type
$((W \Rightarrow ((V \Rightarrow Z) \Rightarrow Z)) \Rightarrow Z) \Rightarrow Z$, $N$ a term of
type $W$ and $K$ a term of type $V \Rightarrow Z$, all in context $\Xi$. In the context $\Xi$
extended by a newest variable $k$ of type $V \Rightarrow Z$, consider the term
$F^{\uparrow}\,(\lambda p.\; p\; N^{\uparrow\uparrow}\; k)$. Here $p$ is the bound variable, of type
$W \Rightarrow ((V \Rightarrow Z) \Rightarrow Z)$, with de Bruijn index $0$, and $k$ has index $1$
under the binder. Instantiating $k$ with $K$ in this term gives
$F\,(\lambda p.\; p\; N^{\uparrow}\; K^{\uparrow})$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.instantiate_cbnApp₁`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#instantiate-cbn-app).

## The translation of an abstraction passes the translated function to its continuation

Fix an answer type $R$, and write $\overline{t}$ for the call-by-name CPS translation of a term
$t$, $T^*$ for the translation of a type $T$, and $\Gamma^*$ for the context obtained from
$\Gamma$ by replacing each type $C$ with $(C^* \to R) \to R$. Let $N$ be a term of type $B$ in
context $A, \Gamma$, let $K$ be a value of type $(A \to B)^* \to R$ in context $\Gamma^*$, and
let $w$ be a term of type $R$ in context $\Gamma^*$. Then $\overline{\lambda x.\,N}\,K$
evaluates to $w$ under call-by-value big-step evaluation if and only if
$K\,(\lambda x.\,\overline{N})$ does.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.eval_cbn_lam_iff`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#eval-cbn-lam-iff).

## Call-by-name evaluation is preserved by the CPS translation

Fix an answer type $R$,
and write $\overline{M}$ for the call-by-name CPS translation of a term $M$ and $T^*$ for the
translation of a type $T$. Let $M$ and $V$ be closed terms of type $T$ such that $M$ evaluates
to $V$ under call-by-name big-step evaluation. Then for every closed value $K$ of type
$T^* \to R$ and every closed term $w$ of type $R$, the application $\overline{M}\,K$ evaluates to
$w$ under call-by-value big-step evaluation if and only if $\overline{V}\,K$ does.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cbn_evalN`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cbn-eval-n).

## Plotkin's simulation theorem for the call-by-name CPS translation

Fix an answer type
$R$, and write $\overline{M}$ for the call-by-name CPS translation of a term $M$ and $T^*$ for
the translation of a type $T$. Let $M$ be a closed term of type $A \to B$ that evaluates to
$\lambda x.\,N$ under call-by-name big-step evaluation. Then for every closed value $K$ of type
$(A \to B)^* \to R$ and every closed term $w$ of type $R$, the application $\overline{M}\,K$
evaluates to $w$ under call-by-value big-step evaluation if and only if
$K\,(\lambda x.\,\overline{N})$ does.

This is the big-step form of the theorem, for the simply typed calculus.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.CPS.cbn_simulation`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/CPS/CallByNameSimulation.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html#cbn-simulation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Continuation-passing style translation](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/programming-language-semantics/continuation-passing-style-translation)
