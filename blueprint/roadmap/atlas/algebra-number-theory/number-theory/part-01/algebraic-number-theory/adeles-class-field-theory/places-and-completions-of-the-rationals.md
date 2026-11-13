---
declaration: section
origin: cited
lean: Rat.Place, Rat.Place.absoluteValue, Rat.Place.CompletedFieldBundle, Rat.Place.bundle, Rat.Place.CompletedField, Rat.Place.embedding, Rat.Place.absoluteValue_infinite_apply, Rat.Place.absoluteValue_finite_apply
statement: formalized
proof: formalized
---

# Places and completions of the rationals

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-and-completions-of-the-rationals/index.html).

## Place

## Places of $\mathbb{Q}$

The set $M_{\mathbb{Q}}$ of places of $\mathbb{Q}$, which indexes
the inequivalent normalised absolute values on $\mathbb{Q}$. It consists of one infinite place,
corresponding to the ordinary archimedean absolute value, and one finite place for each prime
number $p$, corresponding to the $p$-adic absolute value.

Formalized by `Rat.Place`, an inductive type declared in [MathlibExt/NumberTheory/Rat/Place.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Rat/Place.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-and-completions-of-the-rationals/index.html#place).

## Absolute value at a rational place

For a place $v$ of $\mathbb{Q}$, the absolute value
$|\cdot|_v : \mathbb{Q} \to \mathbb{R}$ sends $q \in \mathbb{Q}$ to the ordinary absolute value
$|q|$ when $v$ is the infinite place. When $v$ is the finite place at a prime $p$, it sends $q$ to
the normalised $p$-adic absolute value $|q|_p$, where $|0|_p = 0$ and $|q|_p = p^{-v_p(q)}$ for
$q \neq 0$, with $v_p(q)$ the $p$-adic valuation of $q$.

Formalized by `Rat.Place.absoluteValue`, a definition declared in [MathlibExt/NumberTheory/Rat/Place.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Rat/Place.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-and-completions-of-the-rationals/index.html#absolute-value).

## Bundled complete normed field

A complete normed field bundled with its structure: a type
$K$ together with a normed field structure on $K$ for which $K$ is complete with respect to the
metric induced by the norm. It is used to package the completed fields $\mathbb{Q}_v$ of
$\mathbb{Q}$ at its places $v$.

Formalized by `Rat.Place.CompletedFieldBundle`, a structure declared in [MathlibExt/NumberTheory/Rat/Place.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Rat/Place.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-and-completions-of-the-rationals/index.html#completed-field-bundle).

## Bundled completed field at a rational place

To each place $v$ of $\mathbb{Q}$ this assigns
a complete normed field: the real numbers $\mathbb{R}$ with the usual absolute value when $v$ is the
infinite place, and, when $v$ is the finite place at a prime $p$, the field $\mathbb{Q}_p$ of
$p$-adic numbers with the $p$-adic norm.

Formalized by `Rat.Place.bundle`, an abbreviation declared in [MathlibExt/NumberTheory/Rat/Place.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Rat/Place.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-and-completions-of-the-rationals/index.html#bundle).

## Completed field at a rational place

For a place $v$ of $\mathbb{Q}$, the completed field
$\mathbb{Q}_v$ is the field $\mathbb{R}$ of real numbers when $v$ is the infinite place and, when
$v$ is the finite place at a prime $p$, the field $\mathbb{Q}_p$ of $p$-adic numbers.

It is a complete normed field, with the usual absolute value on $\mathbb{R}$ and the $p$-adic norm
on $\mathbb{Q}_p$.

Formalized by `Rat.Place.CompletedField`, an abbreviation declared in [MathlibExt/NumberTheory/Rat/Place.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Rat/Place.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-and-completions-of-the-rationals/index.html#completed-field).

## Embedding of the rationals into a completion

For a place $v$ of $\mathbb{Q}$ with
completed field $\mathbb{Q}_v$, the canonical ring homomorphism $\mathbb{Q} \to \mathbb{Q}_v$ sends
each rational number to itself, viewed as a real number when $v$ is the infinite place and as a
$p$-adic number when $v$ is the finite place at a prime $p$.

Formalized by `Rat.Place.embedding`, a definition declared in [MathlibExt/NumberTheory/Rat/Place.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Rat/Place.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-and-completions-of-the-rationals/index.html#embedding).

## Absolute value at the infinite rational place

For every $q \in \mathbb{Q}$, the absolute
value attached to the infinite place of $\mathbb{Q}$, evaluated at $q$, equals the ordinary absolute
value $|q|$ of $q$ viewed as a real number.

Formalized by `Rat.Place.absoluteValue_infinite_apply`, a theorem declared in [MathlibExt/NumberTheory/Rat/Place.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Rat/Place.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-and-completions-of-the-rationals/index.html#absolute-value-infinite-apply).

## Absolute value at a finite rational place

For every prime $p$ and every $q \in \mathbb{Q}$,
the absolute value attached to the finite place of $\mathbb{Q}$ at $p$, evaluated at $q$, equals the
$p$-adic absolute value $|q|_p$ of $q$. Here $|0|_p = 0$, and $|q|_p = p^{-v_p(q)}$ for $q \neq 0$,
where $v_p(q)$ is the $p$-adic valuation of $q$.

Formalized by `Rat.Place.absoluteValue_finite_apply`, a theorem declared in [MathlibExt/NumberTheory/Rat/Place.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Rat/Place.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-and-completions-of-the-rationals/index.html#absolute-value-finite-apply).

## Norm of a rational in a completion

For every place $v$ of $\mathbb{Q}$ and every
$q \in \mathbb{Q}$, the norm in the completed field $\mathbb{Q}_v$ of the image of $q$ under the
canonical embedding $\mathbb{Q} \to \mathbb{Q}_v$ equals $|q|_v$, the absolute value attached to $v$
evaluated at $q$.

Formalized by `Rat.Place.embedding_norm_eq_absoluteValue`, a theorem declared in [MathlibExt/NumberTheory/Rat/Place.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Rat/Place.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-and-completions-of-the-rationals/index.html#embedding-norm-eq-absolute-value).

## The rationals are dense in each completion

For every place $v$ of $\mathbb{Q}$, with
completed field $\mathbb{Q}_v$, the image of $\mathbb{Q}$ under the canonical embedding
$\mathbb{Q} \to \mathbb{Q}_v$ is dense in $\mathbb{Q}_v$.

Formalized by `Rat.Place.denseRange_embedding`, a theorem declared in [MathlibExt/NumberTheory/Rat/Place.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Rat/Place.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-and-completions-of-the-rationals/index.html#dense-range-embedding).

## Every nontrivial absolute value on $\mathbb{Q}$ is equivalent to that of a place

Let $f$
be a real-valued absolute value on $\mathbb{Q}$ that is nontrivial, that is, $f(x) \ne 1$ for some
$x \ne 0$. Then there is a place $v$ of $\mathbb{Q}$ such that $f$ is equivalent to the absolute
value $|\cdot|_v$ attached to $v$ (the ordinary absolute value at the infinite place, the
$p$-adic absolute value at the prime $p$).

Here two absolute values $f$ and $g$ on $\mathbb{Q}$ are equivalent when $f(x) \le f(y)$ holds
exactly when $g(x) \le g(y)$, for all $x, y \in \mathbb{Q}$.

Formalized by `Rat.Place.exists_place_equiv`, a theorem declared in [MathlibExt/NumberTheory/Rat/Place.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Rat/Place.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-and-completions-of-the-rationals/index.html#exists-place-equiv).

## Ostrowski's theorem for $\mathbb{Q}$, indexed by places

Let $f$ be a real-valued absolute
value on $\mathbb{Q}$ that is nontrivial, that is, $f(x) \ne 1$ for some $x \ne 0$. Then there is
exactly one place $v$ of $\mathbb{Q}$ such that $f$ is equivalent to the absolute value
$|\cdot|_v$ attached to $v$ (the ordinary absolute value at the infinite place, the $p$-adic
absolute value at the prime $p$).

Here two absolute values $f$ and $g$ on $\mathbb{Q}$ are equivalent when $f(x) \le f(y)$ holds
exactly when $g(x) \le g(y)$, for all $x, y \in \mathbb{Q}$.

Formalized by `Rat.Place.exists_unique_place_equiv`, a theorem declared in [MathlibExt/NumberTheory/Rat/Place.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Rat/Place.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-and-completions-of-the-rationals/index.html#exists-unique-place-equiv).

## Embedding of $\mathbb{Q}$, normed by a place, into its completion

For a place $v$ of
$\mathbb{Q}$, the ring homomorphism from $\mathbb{Q}$, equipped with the absolute value $|\cdot|_v$
attached to $v$ as its norm, into the completed field $\mathbb{Q}_v$ given by the canonical
embedding of $\mathbb{Q}$ ($\mathbb{Q}_v = \mathbb{R}$ at the infinite place and
$\mathbb{Q}_v = \mathbb{Q}_p$ at a prime $p$).

Formalized by `Rat.Place.withAbsEmbedding`, a definition declared in [MathlibExt/NumberTheory/Rat/Place.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Rat/Place.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-and-completions-of-the-rationals/index.html#with-abs-embedding).

## The embedding of $\mathbb{Q}$ into its completion at a place is an isometry

Let $v$ be a
place of $\mathbb{Q}$, let $|\cdot|_v$ be the absolute value attached to $v$, and let
$\mathbb{Q}_v$ be the completed field at $v$. The canonical embedding of $\mathbb{Q}$, equipped
with the metric $d(x, y) = |x - y|_v$, into $\mathbb{Q}_v$ is an isometry: for all
$x, y \in \mathbb{Q}$, the distance between the images of $x$ and $y$ in $\mathbb{Q}_v$ equals
$|x - y|_v$.

Formalized by `Rat.Place.withAbsEmbedding_isometry`, a theorem declared in [MathlibExt/NumberTheory/Rat/Place.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Rat/Place.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-and-completions-of-the-rationals/index.html#with-abs-embedding-isometry).

## Density of the rationals with a place's absolute value in the completion

Let $v$ be a
place of $\mathbb{Q}$, let $|\cdot|_v$ be the absolute value attached to $v$, let $\mathbb{Q}_v$ be
the completed field at $v$, and write $(\mathbb{Q}, |\cdot|_v)$ for the field $\mathbb{Q}$ equipped
with $|\cdot|_v$. The image of the canonical ring homomorphism
$(\mathbb{Q}, |\cdot|_v) \to \mathbb{Q}_v$, which sends each rational number to itself, is dense
in $\mathbb{Q}_v$.

Formalized by `Rat.Place.denseRange_withAbsEmbedding`, a theorem declared in [MathlibExt/NumberTheory/Rat/Place.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Rat/Place.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-and-completions-of-the-rationals/index.html#dense-range-with-abs-embedding).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Places and completions of the rationals](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-and-completions-of-the-rationals/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-and-completions-of-the-rationals)
