---
declaration: section
origin: cited
lean: Algebra.Etale.of_isSemisimpleRing_tensorProduct, Algebra.trace_pi, Algebra.traceForm_pi, Algebra.traceForm_apply_of_algEquiv, Algebra.traceForm_apply_eq_zero_of_isNilpotent, Algebra.isReduced_of_traceForm_nondegenerate, Algebra.traceForm_nondegenerate_iff_etale, Algebra.discr_ne_zero_iff_traceForm_nondegenerate
statement: formalized
proof: formalized
---

# Étale algebras and the trace form

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/tale-algebras-and-the-trace-form/index.html).

## Étale criterion via semisimple base change

Let $K$ be a field, $\Omega$ an
algebraically closed field extension of $K$, and $A$ a commutative $K$-algebra that is
finite-dimensional over $K$. If the ring $\Omega \otimes_K A$ is semisimple, then $A$ is étale
over $K$.

Formalized by `Algebra.Etale.of_isSemisimpleRing_tensorProduct`, a theorem declared in [MathlibExt/RingTheory/Etale/SemisimpleBaseChange.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Etale/SemisimpleBaseChange.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/tale-algebras-and-the-trace-form/index.html#of-is-semisimple-ring-tensor-product).

## Trace on a finite product of algebras

Let $K$ be a field, and for a finite-dimensional
commutative $K$-algebra $A$ and $z \in A$ write $\operatorname{Tr}_{A/K}(z)$ for the trace of the
$K$-linear map given by multiplication by $z$. Let $(A_i)_{i \in I}$ be a family of
finite-dimensional commutative $K$-algebras indexed by a finite set $I$, and let
$P = \prod_{i \in I} A_i$. Then for every $x = (x_i)_{i \in I}$ in $P$,
$\operatorname{Tr}_{P/K}(x) = \sum_{i \in I} \operatorname{Tr}_{A_i/K}(x_i)$.

Formalized by `Algebra.trace_pi`, a theorem declared in [MathlibExt/RingTheory/Etale/TraceForm.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Etale/TraceForm.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/tale-algebras-and-the-trace-form/index.html#trace-pi).

## Trace form of a finite product of algebras

Let $K$ be a field, and for a
finite-dimensional commutative $K$-algebra $A$ and $z \in A$ write $\operatorname{Tr}_{A/K}(z)$
for the trace of the $K$-linear map given by multiplication by $z$. Let $(A_i)_{i \in I}$ be a
family of finite-dimensional commutative $K$-algebras indexed by a finite set $I$, and let
$P = \prod_{i \in I} A_i$. Then for all $x = (x_i)_{i \in I}$ and $y = (y_i)_{i \in I}$ in $P$,
$\operatorname{Tr}_{P/K}(xy) = \sum_{i \in I} \operatorname{Tr}_{A_i/K}(x_i y_i)$, that is, the
trace form of $P$ over $K$ is the sum of the trace forms of the factors.

Formalized by `Algebra.traceForm_pi`, a theorem declared in [MathlibExt/RingTheory/Etale/TraceForm.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Etale/TraceForm.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/tale-algebras-and-the-trace-form/index.html#trace-form-pi).

## The trace form is invariant under algebra isomorphisms

For a commutative algebra $A$
over a field $K$ and $z \in A$, write $\operatorname{Tr}_{A/K}(z)$ for the trace of the $K$-linear
map given by multiplication by $z$, taken to be $0$ when $A$ is infinite-dimensional over $K$. Let
$R$ and $S$ be commutative algebras over $K$ and let $e : R \to S$ be an isomorphism of
$K$-algebras. Then for all $x, y \in R$ we have
$\operatorname{Tr}_{S/K}(e(x)\,e(y)) = \operatorname{Tr}_{R/K}(xy)$, that is, $e$ carries the
trace form of $R$ over $K$ to the trace form of $S$ over $K$.

Formalized by `Algebra.traceForm_apply_of_algEquiv`, a theorem declared in [MathlibExt/RingTheory/Etale/TraceForm.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Etale/TraceForm.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/tale-algebras-and-the-trace-form/index.html#trace-form-apply-of-alg-equiv).

## Nilpotent elements pair to zero under the trace form

Let $R$ be a commutative algebra
over a field $K$, and for $z \in R$ write $\operatorname{Tr}_{R/K}(z)$ for the trace of the
$K$-linear map given by multiplication by $z$, taken to be $0$ when $R$ is infinite-dimensional
over $K$. If $x, y \in R$ and $x$ is nilpotent, then the trace form of $R$ over $K$ vanishes at
$(x, y)$, that is, $\operatorname{Tr}_{R/K}(xy) = 0$.

Multiplication by a nilpotent element is a nilpotent endomorphism, whose trace vanishes.

Formalized by `Algebra.traceForm_apply_eq_zero_of_isNilpotent`, a theorem declared in [MathlibExt/RingTheory/Etale/TraceForm.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Etale/TraceForm.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/tale-algebras-and-the-trace-form/index.html#trace-form-apply-eq-zero-of-is-nilpotent).

## A nondegenerate trace form forces the algebra to be reduced

Let $R$ be a commutative
algebra over a field $K$. For $z \in R$ write $\operatorname{Tr}_{R/K}(z)$ for the trace of the
$K$-linear map given by multiplication by $z$, taken to be $0$ when $R$ is infinite-dimensional
over $K$. If the trace form $(x, y) \mapsto \operatorname{Tr}_{R/K}(xy)$ of $R$ over $K$ is
nondegenerate, then $R$ is reduced, that is, its only nilpotent element is $0$.

Every nilpotent element lies in the kernel of the trace form, hence is zero.

Formalized by `Algebra.isReduced_of_traceForm_nondegenerate`, a theorem declared in [MathlibExt/RingTheory/Etale/TraceForm.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Etale/TraceForm.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/tale-algebras-and-the-trace-form/index.html#is-reduced-of-trace-form-nondegenerate).

## Trace form criterion for étale algebras

Let $R$ be a finite-dimensional commutative
algebra over a field $K$, and for $z \in R$ write $\operatorname{Tr}_{R/K}(z)$ for the trace of
the $K$-linear map given by multiplication by $z$. Then the trace form
$(x, y) \mapsto \operatorname{Tr}_{R/K}(xy)$ of $R$ over $K$ is nondegenerate if and only if $R$
is étale over $K$.

## Sources

- ATLAS NumberTheoryI Theorem 5.20.

Formalized by `Algebra.traceForm_nondegenerate_iff_etale`, a theorem declared in [MathlibExt/RingTheory/Etale/TraceForm.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Etale/TraceForm.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/tale-algebras-and-the-trace-form/index.html#trace-form-nondegenerate-iff-etale).

## Discriminant and nondegeneracy of the trace form

Let $R$ be a commutative algebra over a
field $K$ and let $b$ be a $K$-basis of $R$ indexed by a finite set. For $z \in R$ write
$\operatorname{Tr}_{R/K}(z)$ for the trace of the $K$-linear map given by multiplication by $z$.
Then the discriminant of $b$ over $K$ is nonzero if and only if the trace form
$(x, y) \mapsto \operatorname{Tr}_{R/K}(xy)$ of $R$ over $K$ is nondegenerate.

Formalized by `Algebra.discr_ne_zero_iff_traceForm_nondegenerate`, a theorem declared in [MathlibExt/RingTheory/Etale/TraceForm.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Etale/TraceForm.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/tale-algebras-and-the-trace-form/index.html#discr-ne-zero-iff-trace-form-nondegenera).

## Étale algebras are detected by the discriminant

Let $R$ be a commutative algebra over a
field $K$ and let $b$ be a $K$-basis of $R$ indexed by a finite set. Then the discriminant of $b$
over $K$ is nonzero if and only if $R$ is étale over $K$.

## Sources

- ATLAS NumberTheoryI Lemma 12.18.

Formalized by `Algebra.discr_ne_zero_iff_etale`, a theorem declared in [MathlibExt/RingTheory/Etale/TraceForm.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Etale/TraceForm.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/tale-algebras-and-the-trace-form/index.html#discr-ne-zero-iff-etale).

## Étale algebras have nonzero discriminant

Let $R$ be a commutative algebra over a field
$K$ that is étale over $K$. Then for every $K$-basis $b$ of $R$ indexed by a finite set, the
discriminant of $b$ over $K$ is nonzero.

## Sources

- ATLAS NumberTheoryI Lemma 12.18, one direction.

Formalized by `Algebra.discr_ne_zero_of_etale`, a theorem declared in [MathlibExt/RingTheory/Etale/TraceForm.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Etale/TraceForm.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/tale-algebras-and-the-trace-form/index.html#discr-ne-zero-of-etale).

## A nonzero discriminant forces étaleness

Let $R$ be a commutative algebra over a field
$K$ and let $b$ be a $K$-basis of $R$ indexed by a finite set. If the discriminant of $b$ over
$K$ is nonzero, then $R$ is étale over $K$.

## Sources

- ATLAS NumberTheoryI Lemma 12.18, one direction.

Formalized by `Algebra.etale_of_discr_ne_zero`, a theorem declared in [MathlibExt/RingTheory/Etale/TraceForm.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Etale/TraceForm.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/tale-algebras-and-the-trace-form/index.html#etale-of-discr-ne-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Étale algebras and the trace form](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/tale-algebras-and-the-trace-form/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/algebras-and-differentials/tale-algebras-and-the-trace-form)
