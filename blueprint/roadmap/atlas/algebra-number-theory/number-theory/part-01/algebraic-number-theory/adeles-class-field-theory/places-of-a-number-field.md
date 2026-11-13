---
declaration: section
origin: cited
lean: NumberField.FinitePlace.normalizedAbsoluteValue, NumberField.FinitePlace.normalizedAbsoluteValue_apply, NumberField.FinitePlace.normalizedAbsoluteValue_apply_eq_adicAbv, NumberField.InfinitePlace.normalizedAbsoluteValue, NumberField.InfinitePlace.normalizedAbsoluteValue_apply, NumberField.InfinitePlace.normalizedAbsoluteValue_apply_of_isReal, NumberField.InfinitePlace.normalizedAbsoluteValue_apply_of_isComplex, NumberField.Place
statement: formalized
proof: formalized
---

# Places of a number field

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-of-a-number-field/index.html).

## Degree-normalized absolute value at a finite place

Let $K$ be a number field of degree
$d = [K : \mathbb{Q}]$ and let $v$ be a finite place of $K$, with absolute value $|\cdot|_v$. The
degree-normalized absolute value at $v$ is the absolute value $x \mapsto |x|_v^{1/d}$ on $K$.

The finite-place absolute value $|\cdot|_v$ already contains the local-degree factor, so the
remaining normalization exponent is $1/d$.

Formalized by `NumberField.FinitePlace.normalizedAbsoluteValue`, a definition declared in [MathlibExt/NumberTheory/NumberField/NormalizedPlace.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/NormalizedPlace.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-of-a-number-field/index.html#normalized-absolute-value).

## Value of the degree-normalized absolute value at a finite place

Let $K$ be a number field
of degree $d = [K : \mathbb{Q}]$ and let $v$ be a finite place of $K$, with absolute value
$|\cdot|_v$. For every $x \in K$, the degree-normalized absolute value of $x$ at $v$ equals
$|x|_v^{1/d}$.

Formalized by `NumberField.FinitePlace.normalizedAbsoluteValue_apply`, a theorem declared in [MathlibExt/NumberTheory/NumberField/NormalizedPlace.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/NormalizedPlace.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-of-a-number-field/index.html#normalized-absolute-value-apply).

## Degree-normalized finite absolute value through the prime ideal

Let $K$ be a number
field of degree $d = [K : \mathbb{Q}]$, let $v$ be a finite place of $K$, and let $\mathfrak{p}$
be the nonzero prime ideal of the ring of integers of $K$ that defines $v$. For every $x \in K$,
the degree-normalized absolute value of $x$ at $v$ equals $|x|_{\mathfrak{p}}^{1/d}$, where
$|x|_{\mathfrak{p}} = N(\mathfrak{p})^{-v_{\mathfrak{p}}(x)}$ for $x \neq 0$ and
$|0|_{\mathfrak{p}} = 0$, with $N(\mathfrak{p})$ the absolute norm of $\mathfrak{p}$ and
$v_{\mathfrak{p}}$ the $\mathfrak{p}$-adic valuation.

Formalized by `NumberField.FinitePlace.normalizedAbsoluteValue_apply_eq_adicAbv`, a theorem declared in [MathlibExt/NumberTheory/NumberField/NormalizedPlace.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/NormalizedPlace.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-of-a-number-field/index.html#normalized-absolute-value-apply-eq-adic).

## Degree-normalized absolute value at an infinite place

Let $K$ be a number field of degree
$d = [K : \mathbb{Q}]$ and let $v$ be an infinite place of $K$, with absolute value $|\cdot|_v$
and multiplicity $m_v$, equal to $1$ if $v$ is real and $2$ if $v$ is complex. The
degree-normalized absolute value at $v$ is the absolute value $x \mapsto |x|_v^{m_v/d}$ on $K$.

Formalized by `NumberField.InfinitePlace.normalizedAbsoluteValue`, a definition declared in [MathlibExt/NumberTheory/NumberField/NormalizedPlace.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/NormalizedPlace.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-of-a-number-field/index.html#normalized-absolute-value-2).

## Value of the degree-normalized absolute value at an infinite place

Let $K$ be a number
field of degree $d = [K : \mathbb{Q}]$ and let $v$ be an infinite place of $K$, with absolute
value $|\cdot|_v$ and multiplicity $m_v$, equal to $1$ if $v$ is real and $2$ if $v$ is complex.
For every $x \in K$, the degree-normalized absolute value of $x$ at $v$ equals $|x|_v^{m_v/d}$.

Formalized by `NumberField.InfinitePlace.normalizedAbsoluteValue_apply`, a theorem declared in [MathlibExt/NumberTheory/NumberField/NormalizedPlace.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/NormalizedPlace.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-of-a-number-field/index.html#normalized-absolute-value-apply-2).

## Degree-normalized absolute value at a real place

Let $K$ be a number field of degree
$d = [K : \mathbb{Q}]$ and let $v$ be a real infinite place of $K$, with absolute value
$|\cdot|_v$. For every $x \in K$, the degree-normalized absolute value of $x$ at $v$ equals
$|x|_v^{1/d}$.

Formalized by `NumberField.InfinitePlace.normalizedAbsoluteValue_apply_of_isReal`, a theorem declared in [MathlibExt/NumberTheory/NumberField/NormalizedPlace.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/NormalizedPlace.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-of-a-number-field/index.html#normalized-absolute-value-apply-of-is-re).

## Degree-normalized absolute value at a complex place

Let $K$ be a number field of degree
$d = [K : \mathbb{Q}]$ and let $v$ be a complex infinite place of $K$, with absolute value
$|\cdot|_v$. For every $x \in K$, the degree-normalized absolute value of $x$ at $v$ equals
$|x|_v^{2/d}$.

Formalized by `NumberField.InfinitePlace.normalizedAbsoluteValue_apply_of_isComplex`, a theorem declared in [MathlibExt/NumberTheory/NumberField/NormalizedPlace.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/NormalizedPlace.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-of-a-number-field/index.html#normalized-absolute-value-apply-of-is-co).

## Places of a number field

For a number field $K$, the places of $K$ form the disjoint union
of the infinite places of $K$ (the absolute values coming from complex embeddings of $K$) and the
finite places of $K$ (the absolute values coming from nonzero prime ideals of the ring of
integers $\mathcal{O}_K$).

Formalized by `NumberField.Place`, a definition declared in [MathlibExt/NumberTheory/NumberField/Place.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Place.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-of-a-number-field/index.html#place).

## Infinite places as places

For a number field $K$, each infinite place $v$ of $K$ is
regarded as a place of $K$ via the inclusion of the infinite places into the disjoint union of the
infinite and finite places of $K$.

Formalized by `NumberField.Place.infinitePlace`, a definition declared in [MathlibExt/NumberTheory/NumberField/Place.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Place.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-of-a-number-field/index.html#infinite-place).

## Finite places as places

For a number field $K$, each finite place $v$ of $K$ is regarded
as a place of $K$ via the inclusion of the finite places into the disjoint union of the infinite
and finite places of $K$.

Formalized by `NumberField.Place.finitePlace`, a definition declared in [MathlibExt/NumberTheory/NumberField/Place.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Place.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-of-a-number-field/index.html#finite-place).

## Residue norm of a finite place

Let $v$ be a finite place of a number field $K$ and
$\mathfrak{p}_v$ the corresponding nonzero prime ideal of the ring of integers $\mathcal{O}_K$. The
residue norm $N(v)$ is the absolute norm $|\mathcal{O}_K / \mathfrak{p}_v|$ of $\mathfrak{p}_v$, the
cardinality of the residue field at $v$, regarded as a real number.

Formalized by `NumberField.FinitePlace.residueNorm`, a definition declared in [MathlibExt/NumberTheory/NumberField/Place.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Place.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-of-a-number-field/index.html#residue-norm).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Places of a number field](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-of-a-number-field/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/places-of-a-number-field)
