---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.ClosureConversion.Source.Value, Cslib.Languages.LambdaCalculus.ClosureConversion.Source.Eval, Cslib.Languages.LambdaCalculus.ClosureConversion.Source.Eval.deterministic, Cslib.Languages.LambdaCalculus.ClosureConversion.Target.Tm, Cslib.Languages.LambdaCalculus.ClosureConversion.Target.Value, Cslib.Languages.LambdaCalculus.ClosureConversion.Target.Tm.Eval, Cslib.Languages.LambdaCalculus.ClosureConversion.Target.Tm.liftRen, Cslib.Languages.LambdaCalculus.ClosureConversion.Target.Tm.rename
statement: formalized
proof: formalized
---

# Closure conversion

43 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html).

## Source values of closure conversion

A source value is a closure of a raw term $b$ (the
body of a lambda) over an environment $\rho$, which is a list of source values.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.Source.Value`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Source.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Source.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#value).

## Big-step semantics of the closure-conversion source

Evaluation
$\rho \vdash t \Downarrow v$ of a raw term $t$ to a source value $v$ in an environment $\rho$ (a
list of source values, where variable $n$ refers to the entry of $\rho$ at index $n$, counting
from $0$) is the least relation closed under the following rules, a call-by-value environment
semantics that ignores the type annotations of lambdas. A variable $n$ evaluates to the entry of
$\rho$ at index $n$, when that entry exists. A lambda $\lambda. b$ evaluates to the closure of $b$
over $\rho$. If $f$ evaluates in $\rho$ to the closure of $b$ over $\rho'$, if
$\rho \vdash a \Downarrow v$, and if $v :: \rho' \vdash b \Downarrow w$, where $v :: \rho'$ is
$\rho'$ with $v$ added at index $0$, then $\rho \vdash f\,a \Downarrow w$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.Source.Eval`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Source.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Source.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#eval).

## Source evaluation is deterministic

For every environment $\rho$ of source values and
every raw term $t$, if $t$ evaluates in $\rho$ to source values $v$ and $w$, then $v = w$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.Source.Eval.deterministic`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Source.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Source.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#deterministic).

## Target terms of closure conversion

The terms of the closure-conversion target language,
with variables as de Bruijn indices, are: a variable $n$ for each natural number $n$; code
$\mathsf{code}\,b$ of one parameter, whose body $b$ is evaluated with only its parameter in scope,
as variable $0$; application $f\,a$ of code to an argument; the unit term $\mathsf{unit}$ (the
empty tuple); pairs $(a, b)$; the projections $\mathsf{fst}\,e$ and $\mathsf{snd}\,e$; and
$\mathsf{let}\ e\ \mathsf{in}\ b$, which binds the value of $e$ as variable $0$ in $b$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.Target.Tm`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Target.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Target.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#tm).

## Target values of closure conversion

A value of the closure-conversion target language is
code $\mathsf{code}\,b$ for a target term $b$, the unit value $\mathsf{unit}$, or a pair $(v, w)$
of values.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.Target.Value`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Target.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Target.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#value-2).

## Big-step semantics of the closure-conversion target

Evaluation $\rho \vdash e \Downarrow v$
of a target term $e$ to a target value $v$ in an environment $\rho$ (a list of values, where
variable $n$ refers to the entry of $\rho$ at index $n$, counting from $0$) is the least relation
closed under the following rules. A variable $n$ evaluates to the entry of $\rho$ at index $n$,
when that entry exists. Code evaluates to itself: $\rho \vdash \mathsf{code}\,b \Downarrow
\mathsf{code}\,b$. If $\rho \vdash f \Downarrow \mathsf{code}\,b$, $\rho \vdash a \Downarrow v$ and
$[v] \vdash b \Downarrow w$, then $\rho \vdash f\,a \Downarrow w$; so a code body runs in the
one-element environment $[v]$ and never sees $\rho$. The unit term evaluates to the unit value.
If $\rho \vdash a \Downarrow v$ and $\rho \vdash b \Downarrow w$, then
$\rho \vdash (a, b) \Downarrow (v, w)$. If $\rho \vdash e \Downarrow (v, w)$, then
$\rho \vdash \mathsf{fst}\,e \Downarrow v$ and $\rho \vdash \mathsf{snd}\,e \Downarrow w$. If
$\rho \vdash e \Downarrow v$ and $v :: \rho \vdash b \Downarrow w$, where $v :: \rho$ is $\rho$
with $v$ added at index $0$, then $\rho \vdash \mathsf{let}\ e\ \mathsf{in}\ b \Downarrow w$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.Target.Tm.Eval`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Target.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Target.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#eval-2).

## Lifting a renaming under a binder, for the closure-conversion target

The lift
$r^{\uparrow}$ of a renaming $r : \mathbb{N} \to \mathbb{N}$ of de Bruijn indices sends $0$ to $0$
and $i + 1$ to $r(i) + 1$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.Target.Tm.liftRen`, a definition declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Target.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Target.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#lift-ren).

## Renaming target terms

For $r : \mathbb{N} \to \mathbb{N}$, the renaming $t[r]$ of a target
term $t$ replaces each variable $i$ by $r(i)$, leaves code $\mathsf{code}\,b$ unchanged (its body
$b$ is not renamed), fixes $\mathsf{unit}$, commutes with application, pairing and the two
projections, and sends $\mathsf{let}\ e\ \mathsf{in}\ b$ to
$\mathsf{let}\ e[r]\ \mathsf{in}\ b[r^{\uparrow}]$, where $r^{\uparrow}$, the lift of $r$ under
one binder, sends $0$ to $0$ and $i + 1$ to $r(i) + 1$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.Target.Tm.rename`, a definition declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Target.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Target.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#rename).

## Shifting a target term

The shift of a target term $e$ is its renaming by the successor map
$i \mapsto i + 1$: every free variable of $e$ goes up by one, and code bodies are left unchanged.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.Target.Tm.shift`, a definition declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Target.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Target.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#shift).

## Evaluation is stable under renaming

Let $\rho$ and $\rho'$ be environments and
$r : \mathbb{N} \to \mathbb{N}$ a renaming such that, for every index $i$ and value $w$, if $\rho$
has entry $w$ at index $i$ then $\rho'$ has entry $w$ at index $r(i)$. If a target term $e$
evaluates to $v$ in $\rho$, then the renaming of $e$ by $r$ evaluates to $v$ in $\rho'$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.Target.Tm.Eval.rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Target.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Target.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#rename-2).

## Evaluation of a shifted term

If a target term $e$ evaluates to $v$ in an environment
$\rho$, then for every value $x$ the shift of $e$ evaluates to $v$ in the environment $x :: \rho$
obtained from $\rho$ by adding $x$ at index $0$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.Target.Tm.Eval.shift`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Target.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Target.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#shift-2).

## Well-scoped target terms

For a natural number $m$, a target term $e$ is scoped in $m$
when every free variable of $e$ is less than $m$ and every code body in $e$ is closed, that is,
scoped in $1$. Inductively: a variable $i$ is scoped in $m$ when $i < m$; $\mathsf{code}\,b$ is
scoped in every $m$ when $b$ is scoped in $1$; $\mathsf{unit}$ is scoped in every $m$; an
application, a pair or a projection is scoped in $m$ when its immediate subterms are; and
$\mathsf{let}\ e\ \mathsf{in}\ b$ is scoped in $m$ when $e$ is scoped in $m$ and $b$ is scoped in
$m + 1$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.Target.Tm.Scoped`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Target.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Target.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#scoped).

## Shifting preserves scoping

If a target term $e$ is scoped in $m$, then its shift is scoped
in $m + 1$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.Target.Tm.Scoped.shift`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Target.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Target.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#shift-3).

## Iterated second projection

For a natural number $k$ and a target term $e$, the term
$\mathsf{snd}^k\,e$ applies the second projection $k$ times to $e$: $\mathsf{snd}^0\,e = e$ and
$\mathsf{snd}^{k+1}\,e = \mathsf{snd}\,(\mathsf{snd}^k\,e)$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.snds`, a definition declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#snds).

## Environment-packing term

For a map $\mathit{acc}$ from natural numbers to target terms
and a natural number $n$, the environment-packing term of $\mathit{acc}$ and $n$ is the target
term $(\mathit{acc}(0), (\mathit{acc}(1), \dots (\mathit{acc}(n - 1), \mathsf{unit})\dots))$
packing $\mathit{acc}(0), \dots, \mathit{acc}(n - 1)$ as nested pairs ending in $\mathsf{unit}$.
Recursively, it is $\mathsf{unit}$ for $n = 0$, and for $n + 1$ it is the pair of
$\mathit{acc}(0)$ and the environment-packing term of $i \mapsto \mathit{acc}(i + 1)$ and $n$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.envOf`, a definition declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#env-of).

## Accessors inside converted code

Write $\#0$ for the target variable $0$ and
$\mathsf{snd}^i$ for $i$ applications of the second projection. The code accessor for index $0$
is $\mathsf{fst}\,\#0$, and the code accessor for index $i + 1$ is
$\mathsf{fst}\,(\mathsf{snd}^i\,(\mathsf{snd}\,\#0))$. When the code parameter $\#0$ is the pair
of the argument and an environment encoded as nested pairs, accessor $0$ fetches the argument and
accessor $i + 1$ fetches entry $i$ of the environment.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.codeAcc`, a definition declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#code-acc).

## Closure conversion with accessors

Let $\mathit{acc}$ be a family of target terms indexed
by the natural numbers (accessor $i$ fetches source variable $i$) and $n$ a natural number (the
number of source variables in scope). The conversion $\mathcal{C}(\mathit{acc}, n, t)$ of a
source term $t$ is defined by recursion on $t$. A variable $i$ converts to $\mathit{acc}(i)$. A
lambda with body $b$ (whatever its parameter type) converts to the pair of
$\mathsf{code}\,\mathcal{C}(c, n + 1, b)$, where $c$ is the family of code accessors, and the
target term packing $\mathit{acc}(0), \dots, \mathit{acc}(n - 1)$ as nested pairs ending in
$\mathsf{unit}$. An application $f\,a$ converts to
$\mathsf{let}\ \mathcal{C}(\mathit{acc}, n, f)\ \mathsf{in}\ (\mathsf{fst}\,\#0)\,
(\mathcal{C}(\mathit{acc}', n, a), \mathsf{snd}\,\#0)$, where $\#0$ is the target variable $0$
and $\mathit{acc}'(i)$ is the shift of $\mathit{acc}(i)$ for every $i$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.convert`, a definition declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#convert).

## Closure conversion of a program

The closure conversion of a source term $t$ is the
conversion of $t$ in a scope of $0$ variables with the accessors that send each index $i$ to the
target variable $i$. It is intended for closed terms.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.closureConvert`, a definition declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#closure-convert).

## Encoding a list of target values

The encoding of a list of target values as nested pairs
sends the empty list to the unit value and a list with head $w$ and tail $ws$ to the pair of $w$
and the encoding of $ws$. Thus $[w_0, \dots, w_{k-1}]$ is encoded as
$(w_0, (w_1, \dots (w_{k-1}, \mathsf{unit})))$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.encodeEnv`, a definition declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#encode-env).

## Value relation for closure conversion

The relation between source values and target
values of closure conversion is the least relation such that, for every source lambda body $b$,
every list $\rho$ of source values and every list $ws$ of target values with $|\rho| = |ws|$
and $\rho_i$ related to $ws_i$ for every $i < |\rho|$, the source closure of $b$ over $\rho$ is
related to the target pair $(\mathsf{code}\,c, E)$. Here $c$ is the closure conversion of $b$ in
a scope of $|\rho| + 1$ variables with the code accessors, which read variable $0$ as
$\mathsf{fst}\,\#0$ and variable $i + 1$ as $\mathsf{fst}\,(\mathsf{snd}^i\,(\mathsf{snd}\,\#0))$,
where $\#0$ is the code parameter and $\mathsf{snd}^i$ applies the second projection $i$ times;
and $E$ is the encoding of $ws$ as nested pairs ending in the unit value.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.ValRel`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#val-rel).

## Accessors implementing a source environment

Let $\rho$ be a list of source values,
$\rho_t$ a list of target values and $\mathit{acc}$ a family of target terms indexed by the
natural numbers. The accessors $\mathit{acc}$ implement $\rho$ in $\rho_t$ when, for every index
$i$ less than the length of $\rho$, there is a target value $w$ such that $\mathit{acc}(i)$
evaluates to $w$ in the environment $\rho_t$ and the entry of $\rho$ at index $i$ is related to
$w$ by the value relation of closure conversion.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.AccRel`, a definition declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#acc-rel).

## Packed accessors evaluate to an encoded related environment

Let $\rho$ be a list of
source values, $\rho_t$ a list of target values and $\mathit{acc}$ a map from natural numbers
to target terms, and suppose the accessors $\mathit{acc}$ implement $\rho$ in $\rho_t$: for
every $i < |\rho|$, the term $\mathit{acc}(i)$ evaluates in $\rho_t$ to a target value related
to $\rho_i$ by the value relation. Then there is a list $ws$ of target values with
$|ws| = |\rho|$ and $\rho_i$ related to $ws_i$ for every $i < |\rho|$, such that the target
term packing $\mathit{acc}(0), \dots, \mathit{acc}(|\rho| - 1)$ as nested pairs ending in
$\mathsf{unit}$ evaluates in $\rho_t$ to the encoding of $ws$ as nested pairs ending in the
unit value.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.AccRel.envOf`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#env-of-2).

## Iterated second projections of an encoded environment

Let $\rho$ be a list of target
values, $e$ a target term and $ws = [w_0, \dots, w_{m-1}]$ a list of target values, and suppose
$e$ evaluates in $\rho$ to the encoding of $ws$, the nested pairs
$(w_0, (w_1, \dots (w_{m-1}, \mathsf{unit})\dots))$. Then for every natural number $k \le m$, the
term obtained by applying the second projection $k$ times to $e$ evaluates in $\rho$ to the
encoding of $[w_k, \dots, w_{m-1}]$, the list $ws$ with its first $k$ entries dropped.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.eval_snds`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#eval-snds).

## Code accessors implement the extended closure environment

Let $v$ be a source value
related to a target value $w$ by the value relation of closure conversion, and let $\rho$ and $ws$
be lists of source and target values of the same length such that, for every index $i$ below that
length, the entry of $\rho$ at $i$ is related to the entry of $ws$ at $i$. Then the code accessors
implement the source environment $v :: \rho$ ($\rho$ with $v$ added at index $0$) in the
one-element target environment whose entry is the pair of $w$ and the encoding of $ws$ as nested
pairs ending in $\mathsf{unit}$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.accRel_codeAcc`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#acc-rel-code-acc).

## Correctness of closure conversion

Let $\rho$ be a list of source values, $\ell$ its
length, and $t$ a source term that evaluates to a source value $v$ in the environment $\rho$. Let
$\rho_t$ be a list of target values and $\mathit{acc}$ a family of target terms indexed by the
natural numbers that implement $\rho$ in $\rho_t$. Then there is a target value $w$ such that the
conversion of $t$ in a scope of $\ell$ variables with accessors $\mathit{acc}$ evaluates to $w$
in the environment $\rho_t$, and $v$ is related to $w$ by the value relation of closure
conversion.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.convert_correct`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#convert-correct).

## Correctness of closure conversion in the empty environment

If a source term $t$
evaluates to a source value $v$ in the empty environment, then there is a target value $w$ such
that the closure conversion of $t$ evaluates to $w$ in the empty environment and $v$ is related to
$w$ by the value relation of closure conversion.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.closureConvert_correct`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#closure-convert-correct).

## Converted terms are well scoped

Let $m$ and $n$ be natural numbers and $t$ a source term
whose list of free indices at binder depth $n$ is empty, that is, $t$ is scoped in $n$ variables.
If $\mathit{acc}$ is a family of target terms indexed by the natural numbers such that
$\mathit{acc}(i)$ is scoped in $m$ for every $i < n$, then the conversion of $t$ in a scope of
$n$ variables with accessors $\mathit{acc}$ is scoped in $m$; in particular, every code body it
contains is scoped in $1$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.convert_scoped`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#convert-scoped).

## Closure conversion of a closed term is well scoped

If a source term $t$ is closed (it
has no free variables), then its closure conversion is scoped in $0$: it has no free variables,
and every code body in it is scoped in $1$, so refers only to its parameter.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.closureConvert_scoped`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Correctness.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#closure-convert-scoped).

## Free variables one binder deeper

For every raw term $t$ and natural numbers $d$ and $j$,
$j$ is a free index of $t$ at binder depth $d + 1$ if and only if $j + 1$ is a free index of $t$
at binder depth $d$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.mem_freeIndices_succ`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#mem-free-indices-succ).

## Variables captured by a lambda

For a raw term $b$, the captured variables of $b$ form
the list of free indices of $b$ at binder depth $1$ with duplicates removed: the de Bruijn
indices $j$ such that variable $j + 1$ occurs free in $b$, that is, the free variables of the
abstraction $\lambda.\,b$, each listed once.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.captured`, a definition declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#captured).

## Flat closure environment

For a map $\mathrm{acc}$ from natural numbers to target terms
and a list $i_1, \dots, i_n$ of natural numbers, the flat environment is the target term
$(\mathrm{acc}(i_1), (\mathrm{acc}(i_2), \dots, (\mathrm{acc}(i_n), \mathsf{unit})\dots))$, which
packs $\mathrm{acc}(i)$ for each $i$ in the list, in order, as nested pairs ending in
$\mathsf{unit}$; the empty list gives $\mathsf{unit}$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.envFlat`, a definition declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#env-flat).

## Accessors inside flat code

For a list $L$ of natural numbers, the flat accessors for $L$
assign a target term to each variable: variable $0$ is sent to $\mathsf{fst}\,\#0$, and variable
$j + 1$ is sent to $\mathsf{fst}\,(\mathsf{snd}^k\,(\mathsf{snd}\,\#0))$. Here $\#0$ is target
variable $0$, $\mathsf{snd}^k$ applies the second projection $k$ times, and $k$ is the index of the
first occurrence of $j$ in $L$, or the length of $L$ if $j$ does not occur in $L$.

Inside flat code the parameter $\#0$ is the pair of the argument and the environment, so variable
$0$ is the argument and variable $j + 1$ is the entry of the environment at the position of $j$
in $L$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.flatAcc`, a definition declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#flat-acc).

## Flat closure conversion

Given accessors $\mathrm{acc}$, a map from natural numbers to
target terms, the flat conversion $C_{\mathrm{acc}}(t)$ of a raw term $t$ is defined by recursion
on $t$. A variable $i$ becomes $\mathrm{acc}(i)$. A lambda $\lambda.\,b$, whose parameter type is
ignored, becomes the pair $(\mathsf{code}\,C_{\mathrm{acc}'}(b), e)$. Here $i_1, \dots, i_n$ are
the captured variables of $b$, the environment $e$ is
$(\mathrm{acc}(i_1), (\mathrm{acc}(i_2), \dots, (\mathrm{acc}(i_n), \mathsf{unit})\dots))$, and
$\mathrm{acc}'$ sends $0$ to $\mathsf{fst}\,(\mathsf{var}\,0)$ and $j + 1$ to
$\mathsf{fst}\,(\mathsf{snd}^{k+1}\,(\mathsf{var}\,0))$, where $k$ is the position of $j$ in that
list, counting from $0$ (the length $n$ if $j$ does not occur). An application $f\,a$ becomes
$\mathsf{let}\ C_{\mathrm{acc}}(f)\ \mathsf{in}\ (\mathsf{fst}\,(\mathsf{var}\,0))\,
(C_{\mathrm{acc}^{+}}(a), \mathsf{snd}\,(\mathsf{var}\,0))$, where $\mathsf{var}\,0$ is the
variable bound by the $\mathsf{let}$ and $\mathrm{acc}^{+}(i)$ is the shift of $\mathrm{acc}(i)$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.convertFlat`, a definition declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#convert-flat).

## Flat closure conversion of a program

The flat closure conversion of a raw term $t$ is
the flat conversion of $t$ with the accessors $i \mapsto \mathsf{var}\,i$, which send each free
variable $i$ of $t$ to the target variable $i$. It is meant for closed terms.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.closureConvertFlat`, a definition declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#closure-convert-flat).

## Flat value relation

The flat value relation between source values and target values is
the least relation with the following property. Let $b$ be a raw term, $\rho$ a list of source
values of length $|\rho|$, $c = (c_0, \dots, c_{m-1})$ the list of variables captured by
$\lambda. b$, and $w_0, \dots, w_{m-1}$ target values, as many as there are captured variables. If,
for every $k < m$, $c_k < |\rho|$ and the entry of $\rho$ at index $c_k$ (counting from $0$) is
related to $w_k$, then the source closure of $b$ over $\rho$ is related to the target value
$(\mathsf{code}\,B, \mathrm{enc}(w_0, \dots, w_{m-1}))$, where $B$ is the flat closure conversion
of $b$ with the flat accessors for $c$, and $\mathrm{enc}$ encodes a list of target values as
nested pairs ending in $\mathsf{unit}$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.FlatValRel`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#flat-val-rel).

## Accessors implementing the free variables of a term

Let $\rho$ be a list of source
values of length $|\rho|$, $\rho_t$ a list of target values, $\mathrm{acc}$ a map assigning a target
term to each natural number, and $t$ a raw term. The accessors $\mathrm{acc}$ implement $t$ for
$\rho$ in $\rho_t$ when, for every free variable $i$ of $t$, $i < |\rho|$ and $\mathrm{acc}(i)$
evaluates in the target environment $\rho_t$ to a target value that is related, by the flat value
relation, to the entry of $\rho$ at index $i$ (counting from $0$).

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.FlatAccRel`, a definition declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#flat-acc-rel).

## Evaluating a flat environment

Let $\rho$ be a source environment, $\rho_t$ a target
environment, $\mathrm{acc}$ a map from natural numbers to target terms, and $i_1, \dots, i_n$ a
list of natural numbers. Write $\rho_i$ for the entry of $\rho$ at index $i$, counting from $0$.
Suppose every $i$ in the list is less than the length of $\rho$ and $\mathrm{acc}(i)$ evaluates
in $\rho_t$ to a target value related to $\rho_i$ by the flat value relation. Then there are
target values $w_1, \dots, w_n$ such that the flat environment
$(\mathrm{acc}(i_1), (\dots, (\mathrm{acc}(i_n), \mathsf{unit})\dots))$ evaluates in $\rho_t$ to
$(w_1, (\dots, (w_n, \mathsf{unit})\dots))$, and for each $k$ the index $i_k$ is less than the
length of $\rho$ and $w_k$ is related to $\rho_{i_k}$ by the flat value relation.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.eval_envFlat`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#eval-env-flat).

## Length of an evaluated flat environment

Let $\mathrm{acc}$ be a map from natural numbers
to target terms and $i_1, \dots, i_n$ a list of natural numbers. If the flat environment
$(\mathrm{acc}(i_1), (\dots, (\mathrm{acc}(i_n), \mathsf{unit})\dots))$ evaluates in some target
environment to the encoding $(w_1, (\dots, (w_k, \mathsf{unit})\dots))$ of a list of target values
$w_1, \dots, w_k$, then $k = n$.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.envFlat_length`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#env-flat-length).

## Flat accessors implement the variables of a closure body

Let $b$ be a raw term, let
$c = (c_0, \dots, c_{m-1})$ be the list of variables captured by $\lambda. b$, let $\rho$ be a list
of source values of length $|\rho|$, write $\rho_n$ for the entry of $\rho$ at index $n$ (counting
from $0$), and let $w_0, \dots, w_{m-1}$ be target values such that $c_k < |\rho|$ and $\rho_{c_k}$
is related to $w_k$ by the flat value relation for every $k < m$. If a source value $v$ is related
to a target value $w$ by the flat value relation, then the flat accessors for $c$ implement the
free variables of $b$ for the source environment $v :: \rho$ (the list $\rho$ with $v$ added at
index $0$) in the one-entry target environment $[(w, \mathrm{enc}(w_0, \dots, w_{m-1}))]$, where
$\mathrm{enc}$ encodes a list of target values as nested pairs ending in $\mathsf{unit}$. That is,
for every free variable $i$ of $b$, $i < |\rho| + 1$ and the flat accessor for $i$ evaluates in
that target environment to a target value related to the entry of $v :: \rho$ at index $i$ by the
flat value relation.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.flatAccRel_flatAcc`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#flat-acc-rel-flat-acc).

## Correctness of flat closure conversion

Let $\rho$ be a source environment, $\rho_t$ a
target environment, $\mathrm{acc}$ a map from natural numbers to target terms, and $t$ a raw term
that evaluates to a source value $v$ in $\rho$. Suppose that for every free variable $i$ of $t$,
$i$ is less than the length of $\rho$ and $\mathrm{acc}(i)$ evaluates in $\rho_t$ to a target
value related by the flat value relation to the entry $\rho_i$ of $\rho$ at index $i$ (counting
from $0$). Then the flat conversion of $t$ with accessors $\mathrm{acc}$ evaluates in $\rho_t$ to
some target value related to $v$ by the flat value relation.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.convertFlat_correct`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#convert-flat-correct).

## Correctness of flat closure conversion for closed programs

Let $t$ be a closed raw
term, that is, one with no free variables. If $t$ evaluates to a source value $v$ in the empty
environment, then the flat closure conversion of $t$ evaluates in the empty target environment
to some target value $w$ related to $v$ by the flat value relation.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.closureConvertFlat_correct`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#closure-convert-flat-correct).

## Flat closure conversion preserves scoping

Let $t$ be a raw term, $m$ a natural number
and $\mathrm{acc}$ a map from natural numbers to target terms. If $\mathrm{acc}(i)$ is scoped in
$m$ for every free variable $i$ of $t$, then the flat conversion of $t$ with accessors
$\mathrm{acc}$ is scoped in $m$. In particular every code body it contains is scoped in $1$, so
refers only to its parameter.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.convertFlat_scoped`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#convert-flat-scoped).

## Flat closure conversion of a closed term is well scoped

If a raw term $t$ is closed,
then its flat closure conversion is scoped in $0$: it has no free variables, and every code
body in it is scoped in $1$, so refers only to its parameter.

Formalized by `Cslib.Languages.LambdaCalculus.ClosureConversion.closureConvertFlat_scoped`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/LambdaCalculus/ClosureConversion/Flat.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html#closure-convert-flat-scoped).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Closure conversion](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/programming-language-semantics/closure-conversion/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/programming-language-semantics/closure-conversion)
