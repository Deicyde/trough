---
declaration: section
origin: cited
lean: Cslib.Languages.LambdaCalculus.Stlc.RawTm, Cslib.Languages.LambdaCalculus.Stlc.RawTm.size, Cslib.Languages.LambdaCalculus.Stlc.RawTm.shift, Cslib.Languages.LambdaCalculus.Stlc.lookupVar, Cslib.Languages.LambdaCalculus.Stlc.Var.toNat, Cslib.Languages.LambdaCalculus.Stlc.lookupVar_toNat, Cslib.Languages.LambdaCalculus.Stlc.lookupVar_result_toNat, Cslib.Languages.LambdaCalculus.Stlc.Tm.erase
statement: formalized
proof: formalized
---

# Type checking for the simply typed lambda calculus

42 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html).

## Raw lambda terms

Raw terms are extrinsic de Bruijn syntax over a given type of base
types: a raw term is either a variable given by a natural-number index $n$, an application
$f\,a$ of two raw terms $f$ and $a$, or a lambda abstraction $\lambda A.\,t$ consisting of a
simple type $A$ over the base types (the parameter type) and a raw term $t$ (the body).
Variables and applications carry no type information.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.RawTm`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#raw-tm).

## Size of a raw term

Writing $|t|$ for the size of a raw term $t$, the size counts the
syntax nodes of $t$: a variable has size $1$, an application $f\,a$ has size $|f| + |a| + 1$,
and a lambda abstraction $\lambda A.\,t$ has size $|t| + 1$, so the type annotation $A$ is
not counted.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.RawTm.size`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#size).

## Shifting raw terms

For natural numbers $k$ (the amount) and $c$ (the cutoff, $0$ by
default), shifting a raw term by $k$ at cutoff $c$ replaces a variable index $n$ by $n + k$ if
$c \le n$ and leaves it unchanged otherwise, shifts both sides of an application by $k$ at
cutoff $c$, and sends $\lambda A.\,t$ to $\lambda A.\,t'$, where $t'$ is $t$ shifted by $k$ at
cutoff $c + 1$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.RawTm.shift`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#shift).

## Variable lookup

Given a context $\Gamma$, a list of types, and a natural number $n$,
looking up the de Bruijn index $n$ in $\Gamma$ either fails or returns a type $A$ together with
an intrinsic variable of type $A$ in $\Gamma$. It is defined by recursion: lookup fails in the
empty context; index $0$ in the context $A :: \Gamma$, obtained by adding $A$ at the front of
$\Gamma$, returns $A$ with the zero variable; and index $n + 1$ in $B :: \Gamma$ looks up $n$ in
$\Gamma$, fails if that fails, and otherwise returns the same type with the successor of the
variable found.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.lookupVar`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#lookup-var).

## Index of a typed variable

For a context $\Gamma$ and a type $A$, a well-typed de Bruijn
variable of type $A$ in $\Gamma$ is sent to its natural-number index, forgetting its type: the
variable for the first entry of the context has index $0$, and the successor of a variable $x$
has the index of $x$ plus $1$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Var.toNat`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#to-nat).

## Lookup recovers an intrinsic variable from its index

For every context $\Gamma$, type
$A$ and intrinsic variable $x$ of type $A$ in $\Gamma$, looking up the de Bruijn index of $x$ in
$\Gamma$ succeeds and returns the type $A$ together with $x$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.lookupVar_toNat`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#lookup-var-to-nat).

## Lookup returns a variable with the queried index

For every context $\Gamma$ and
natural number $n$, if looking up the de Bruijn index $n$ in $\Gamma$ succeeds with a type $A$
and an intrinsic variable $x$ of type $A$ in $\Gamma$, then the de Bruijn index of $x$ is $n$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.lookupVar_result_toNat`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#lookup-var-result-to-nat).

## Erasure of intrinsically typed terms

The erasure of an intrinsically typed term in a
context $\Gamma$ is the raw term defined by recursion: a variable becomes the raw variable whose
index is its position in $\Gamma$ (counting from $0$ at the front); an application of $f$ to $a$
becomes the raw application of the erasure of $f$ to the erasure of $a$; and a lambda with
parameter type $B$ becomes the raw lambda annotated with $B$ whose body is the erasure of its
body. Erasure thus forgets all typing information except the binder annotations.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Tm.erase`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#erase).

## Checked terms

For a context $\Gamma$ of simple types, a checked term in $\Gamma$ is a pair
$(A, t)$ of a simple type $A$ and an intrinsically typed term $t$ of type $A$ in $\Gamma$.

A successful elaboration returns such a pair: the inferred type together with an intrinsic
term at that type.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Checked`, an abbreviation declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#checked).

## Elaboration of raw STLC terms

Assume equality of base types is decidable. Elaboration in
a context $\Gamma$ of simple types sends a raw term either to failure or to a checked term in
$\Gamma$ (a simple type together with an intrinsically typed term of that type in $\Gamma$), by
recursion on the raw term. A variable with de Bruijn index $n$ elaborates to the variable at
position $n$ of $\Gamma$ (counting from $0$ at the front), with the type stored there, and fails
if $\Gamma$ has at most $n$ entries. A lambda with parameter type $A$ and body $b$ elaborates $b$
in $\Gamma$ extended by $A$ at the front; if that gives type $B$, it returns the lambda at type
$A \to B$, and otherwise it fails. An application of $f$ to $a$ elaborates $f$ and $a$ in
$\Gamma$, and succeeds, returning the application at type $B$, exactly when $f$ gets a function
type $A \to B$ and $a$ gets type $A$; otherwise it fails.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.elaborate`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#elaborate).

## Elaboration inverts erasure

Assume equality of base types is decidable. For every
intrinsically typed term $t$ of type $A$ in context $\Gamma$, elaborating the erasure of $t$ in
$\Gamma$ succeeds and returns exactly the pair $(A, t)$. In other words, erasure is a section of
elaboration.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.elaborate_erase`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#elaborate-erase).

## Elaboration preserves the input syntax

Assume equality of base types is decidable. If
elaborating a raw term $r$ in context $\Gamma$ succeeds with type $A$ and intrinsically typed
term $t$, then the erasure of $t$ is exactly $r$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.elaborate_faithful`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#elaborate-faithful).

## Erasure is injective

For a fixed context $\Gamma$ and type $A$, erasure is injective on
intrinsically typed terms of type $A$ in $\Gamma$: two such terms with the same erasure are
equal.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Tm.erase_injective`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#erase-injective).

## Declarative typing of raw terms

For a context $\Gamma$ (a list of simple types), a
raw term $t$ and a type $A$, the judgment $\Gamma \vdash t : A$ is the least relation closed
under three rules. A variable with de Bruijn index $n$ has type $A$ in $\Gamma$ whenever looking
up $n$ in $\Gamma$ succeeds with the type $A$ and some intrinsic variable of type $A$. If
$\Gamma \vdash f : A \Rightarrow B$ and $\Gamma \vdash a : A$, then the application $f\,a$ has
type $B$ in $\Gamma$. If $A :: \Gamma \vdash b : B$, where $A :: \Gamma$ is $\Gamma$ with $A$
added at the front, then the abstraction $\lambda{:}A.\,b$ with parameter type $A$ has type
$A \Rightarrow B$ in $\Gamma$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.HasType`, an inductive type declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#has-type).

## Erasure preserves typing

For every intrinsically typed term $t$ of type $A$ in context
$\Gamma$, the erasure of $t$ has type $A$ in $\Gamma$ under the declarative typing judgment for
raw terms.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.HasType.erase`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#erase-2).

## Uniqueness of types for raw terms

Let $\Gamma$ be a context of simple types and $r$ a
raw term. If $r$ has type $A$ in $\Gamma$ and $r$ has type $B$ in $\Gamma$ under the declarative
typing judgment for raw terms, then $A = B$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.HasType.unique`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#unique).

## Completeness of elaboration

Assume equality of base types is decidable. If a raw term $r$
has type $A$ in context $\Gamma$ under the declarative typing judgment, then elaborating $r$ in
$\Gamma$ succeeds and returns the type $A$ together with some intrinsically typed term of type
$A$ in $\Gamma$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.HasType.elaborate_complete`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#elaborate-complete).

## Soundness of elaboration

Assume equality of base types is decidable. If elaborating a raw
term $r$ in context $\Gamma$ succeeds with type $A$ (and some intrinsically typed term of type $A$
in $\Gamma$), then $r$ has type $A$ in $\Gamma$ under the declarative typing judgment.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.HasType.elaborate_sound`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#elaborate-sound).

## Declarative typing agrees with elaboration

Assume equality of base types is decidable.
For every context $\Gamma$, raw term $t$ and type $A$, the declarative typing judgment
$\Gamma \vdash t : A$ holds if and only if there is an intrinsically typed term $u$ of type $A$
in context $\Gamma$ such that elaborating $t$ in $\Gamma$ succeeds and returns the type $A$
together with $u$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.HasType.iff_elaborates`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#iff-elaborates).

## Type inference for raw terms

Assume equality of base types is decidable. Given a
context $\Gamma$ and a raw term $t$, type inference elaborates $t$ in $\Gamma$; if elaboration
succeeds, it returns the type component of the result and forgets the intrinsically typed term,
and if elaboration fails, inference fails.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.infer`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#infer).

## Type inference is sound and complete

Assume equality of base types is decidable. For
every context $\Gamma$, raw term $t$ and type $A$, type inference for $t$ in $\Gamma$ returns
$A$ if and only if the declarative typing judgment $\Gamma \vdash t : A$ holds.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.infer_eq_some_iff`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#infer-eq-some-iff).

## Type checking for raw STLC terms

Assume equality of base types is decidable. Given a
context $\Gamma$ (a list of simple types), a raw term $r$ and a simple type $A$, the type checker
returns true exactly when type inference for $r$ in $\Gamma$ returns the type $A$, and false
otherwise.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.check`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#check).

## Normalization of raw terms

Let the base types have decidable equality. Given a context
$\Gamma$ of simple types and a raw term $r$, raw normalization elaborates $r$ in $\Gamma$. If
elaboration fails, raw normalization fails. If elaboration returns a type $A$ and an
intrinsically typed term $t$ of type $A$, raw normalization returns $A$ together with the
erasure to a raw term of the normal form of $t$ computed by normalization by evaluation.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.normalizeRaw`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#normalize-raw).

## Raw normalization of an erased term

Assume equality of base types is decidable. For
every intrinsically typed term $t$ of type $A$ in context $\Gamma$, raw normalization of the
erasure of $t$ in $\Gamma$ succeeds and returns the type $A$ together with the erasure of the
normal form of $t$ computed by normalization by evaluation.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.normalizeRaw_erase`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#normalize-raw-erase).

## Raw normalization reports the inferred type

Let the base types have decidable
equality, let $\Gamma$ be a context of simple types and let $r$ be a raw term. If normalizing
$r$ in $\Gamma$ succeeds and returns a type $A$ together with a raw term, then type inference
for $r$ in $\Gamma$ returns $A$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.normalizeRaw_type`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 408](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L408). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#normalize-raw-type).

## Raw normalization produces well-typed terms

Assume equality of base types is
decidable. For every context $\Gamma$ and raw term $t$, if raw normalization of $t$ in $\Gamma$
succeeds with a type $A$ and a raw term $t'$, then the declarative typing judgment
$\Gamma \vdash t' : A$ holds.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.normalizeRaw_hasType`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#normalize-raw-has-type).

## Raw normalization is idempotent

Assume equality of base types is decidable. For every
context $\Gamma$ and raw term $t$, if raw normalization of $t$ in $\Gamma$ succeeds with a type
$A$ and a raw term $t'$, then raw normalization of $t'$ in $\Gamma$ succeeds with the same type
$A$ and the same term $t'$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.normalizeRaw_idempotent`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/Elaboration.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#normalize-raw-idempotent).

## Lifting a numerical renaming

Given a renaming $\rho : \mathbb{N} \to \mathbb{N}$ of
de Bruijn indices, its lift through one binder is the map $\mathbb{N} \to \mathbb{N}$ sending
$0$ to $0$ and $n + 1$ to $\rho(n) + 1$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.RawTm.liftRen`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#lift-ren).

## Renaming of raw terms

Given a map $\rho : \mathbb{N} \to \mathbb{N}$ on de Bruijn indices,
renaming a raw term by $\rho$ replaces each variable $n$ by $\rho(n)$, renames both parts of an
application by $\rho$, and renames the body of a lambda abstraction, keeping its parameter type,
by the lifted map $\rho'$ given by $\rho'(0) = 0$ and $\rho'(n + 1) = \rho(n) + 1$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.RawTm.rename`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#rename).

## Lifting commutes with composition of numerical renamings

For maps
$\rho, \sigma : \mathbb{N} \to \mathbb{N}$, the lift of $\sigma \circ \rho$ through one binder
equals the lift of $\sigma$ composed after the lift of $\rho$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.RawTm.liftRen_comp`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#lift-ren-comp).

## Composition of renamings of raw terms

For all maps
$\rho, \sigma : \mathbb{N} \to \mathbb{N}$ and every raw term $t$, renaming $t$ by $\rho$ and then
renaming the result by $\sigma$ gives the same raw term as renaming $t$ by the composite
$\sigma \circ \rho$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.RawTm.rename_comp`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#rename-comp).

## Renaming preserves the size of a raw term

For every map $\rho : \mathbb{N} \to \mathbb{N}$
and every raw term $t$, the renaming of $t$ by $\rho$ has the same number of syntax nodes as $t$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.RawTm.size_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#size-rename).

## Shifting preserves the size of a raw term

For all natural numbers $k$ and $c$ and every
raw term $t$, shifting $t$ by $k$ at cutoff $c$ (adding $k$ to each variable index that is at
least the cutoff, which grows by one under each binder) gives a raw term with the same number
of syntax nodes as $t$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.RawTm.size_shift`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#size-shift).

## Indices occurring in a raw term

The list of de Bruijn indices of a raw term, read
from left to right with repetitions: a variable with index $n$ gives $[n]$, an application
gives the indices of the function followed by those of the argument, and a lambda abstraction
gives the indices of its body, unshifted.

Bound occurrences are intentionally included, so this list is useful for diagnostics rather
than for scoping.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.RawTm.indices`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#indices).

## Free indices of a raw term

For a binder depth $d$ and a raw term $t$, the free
indices of $t$ at depth $d$ form a list defined by recursion on $t$: a variable with index $n$
contributes $[n - d]$ if $d \le n$ and the empty list otherwise; an application contributes
the free indices of the function followed by those of the argument, both at depth $d$; and a
lambda abstraction contributes the free indices of its body at depth $d + 1$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.RawTm.freeIndices`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#free-indices).

## Closed raw terms

A raw term $t$ is closed when its list of free indices at binder
depth $0$ is empty.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.RawTm.Closed`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#closed).

## Agreement of a typed and a numerical renaming

A typed renaming $\rho$ from context
$\Gamma$ to context $\Delta$ agrees with a map $r : \mathbb{N} \to \mathbb{N}$ when, for every
type $A$ and every variable $x$ of type $A$ in $\Gamma$, the de Bruijn index of $\rho(x)$
equals $r$ applied to the de Bruijn index of $x$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.RenAgrees`, a definition declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#ren-agrees).

## Agreement of renamings is preserved by lifting

Let $\rho$ be a typed renaming from
context $\Gamma$ to $\Delta$ and let $r : \mathbb{N} \to \mathbb{N}$ be a numerical renaming
that agrees with $\rho$. Then for every type $A$, the lift of $\rho$ under a binder of type
$A$ agrees with the lift of $r$ through one binder.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.RenAgrees.lift`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#lift).

## Agreement of renamings is preserved by composition

Let $\rho$ be a typed renaming
from context $\Gamma$ to $\Delta$, let $\sigma$ be a typed renaming from $\Delta$ to $\Xi$,
and let $r, s : \mathbb{N} \to \mathbb{N}$. If $\rho$ agrees with $r$ and $\sigma$ agrees with
$s$, then the composite renaming that applies $\rho$ and then $\sigma$ agrees with
$s \circ r$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.RenAgrees.comp`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#comp).

## Erasure commutes with renaming

Let $\rho$ be a typed renaming from context $\Gamma$
to $\Delta$ and let $r : \mathbb{N} \to \mathbb{N}$ be a numerical renaming that agrees with
$\rho$. Then for every intrinsically typed term $t$ of type $A$ in context $\Gamma$, the
erasure of the renamed term $\rho(t)$ equals the raw renaming by $r$ (lifted at every binder)
of the erasure of $t$.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Tm.erase_rename`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#erase-rename).

## Erasure of a weakened term

For every intrinsically typed term $t$ in context $\Gamma$
and every type $B$, the erasure of the weakening of $t$ to the context $\Gamma$ extended by
$B$ equals the raw renaming by the successor map $n \mapsto n + 1$ (lifted at every binder)
of the erasure of $t$. Thus every free index is incremented by one.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.Tm.erase_weaken`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#erase-weaken).

## Agreeing numerical renamings coincide on erased terms

Let $\rho$ be a type-preserving
renaming of variables from context $\Gamma$ to context $\Delta$, and let
$r, s : \mathbb{N} \to \mathbb{N}$ both agree with $\rho$: for every variable $x$ of $\Gamma$, the
de Bruijn index of $\rho(x)$ is the image of the index of $x$ under $r$, and also under $s$. Then
for every intrinsically typed term $t$ of type $A$ in context $\Gamma$, renaming the erasure of $t$
by $r$ and renaming it by $s$ give the same raw term.

Formalized by `Cslib.Languages.LambdaCalculus.Stlc.RawTm.rename_eq_on_erase`, a theorem declared in [CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/LambdaCalculus/DeBruijn/Stlc/ElaborationStructural.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html#rename-eq-on-erase).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Type checking for the simply typed lambda calculus](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/type-systems-and-lambda-calculi/type-checking-for-the-simply-typed-lambda-calcul)
