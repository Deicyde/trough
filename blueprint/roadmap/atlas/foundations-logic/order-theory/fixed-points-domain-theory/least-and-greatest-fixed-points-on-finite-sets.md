---
declaration: section
origin: cited
lean: Finset.lfpFin, Finset.gfpFin, Finset.lfpFin_fixed, Finset.gfpFin_fixed, Finset.lfpFin_le, Finset.le_gfpFin, Finset.mem_finset_iterate_iff, Finset.mem_finset_iterate_univ_iff
statement: formalized
proof: formalized
---

# Least and greatest fixed points on finite sets

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/least-and-greatest-fixed-points-on-finite-sets/index.html).

## Finite Iteration

## Least fixed point of a finset map by finite iteration

Let $\alpha$ be a finite type with
$|\alpha|$ elements, let $f$ map subsets of $\alpha$ to subsets of $\alpha$, and write $f^n$ for the
$n$-fold iterate of $f$. Then $\mathrm{lfp}_{\mathrm{fin}}(f)$ is the set $f^{|\alpha|}(\emptyset)$,
obtained by applying $f$ to the empty set $|\alpha|$ times.

For monotone $f$ the iteration has stabilized after $|\alpha|$ steps, and the result is the least
fixed point of $f$.

Formalized by `Finset.lfpFin`, a definition declared in [MathlibExt/Order/FixedPoints/Finset.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/FixedPoints/Finset.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/least-and-greatest-fixed-points-on-finite-sets/index.html#lfp-fin).

## Greatest fixed point of a finset map by finite iteration

Let $\alpha$ be a finite type
with $|\alpha|$ elements, let $f$ map subsets of $\alpha$ to subsets of $\alpha$, and write $f^n$
for the $n$-fold iterate of $f$. Then $\mathrm{gfp}_{\mathrm{fin}}(f)$ is the set
$f^{|\alpha|}(\alpha)$, obtained by applying $f$ to the whole of $\alpha$ $|\alpha|$ times.

For monotone $f$ the iteration has stabilized after $|\alpha|$ steps, and the result is the
greatest fixed point of $f$.

Formalized by `Finset.gfpFin`, a definition declared in [MathlibExt/Order/FixedPoints/Finset.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/FixedPoints/Finset.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/least-and-greatest-fixed-points-on-finite-sets/index.html#gfp-fin).

## Finite iteration from the empty set reaches a fixed point

Let $\alpha$ be a finite type
with $|\alpha|$ elements, let $f$ be a map from subsets of $\alpha$ to subsets of $\alpha$ that is
monotone for inclusion, and let $\mathrm{lfp}_{\mathrm{fin}}(f) = f^{|\alpha|}(\emptyset)$ be the
result of applying $f$ to $\emptyset$ $|\alpha|$ times. Then $\mathrm{lfp}_{\mathrm{fin}}(f)$ is a
fixed point of $f$, that is, $f(\mathrm{lfp}_{\mathrm{fin}}(f)) = \mathrm{lfp}_{\mathrm{fin}}(f)$.

The iterates of $f$ from $\emptyset$ form an increasing chain, and until it stabilizes each step
strictly increases the cardinality, which is bounded by $|\alpha|$.

Formalized by `Finset.lfpFin_fixed`, a theorem declared in [MathlibExt/Order/FixedPoints/Finset.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/FixedPoints/Finset.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/least-and-greatest-fixed-points-on-finite-sets/index.html#lfp-fin-fixed).

## Finite iteration from the whole type reaches a fixed point

Let $\alpha$ be a finite type
with $|\alpha|$ elements, let $f$ be a map from subsets of $\alpha$ to subsets of $\alpha$ that is
monotone for inclusion, and let $\mathrm{gfp}_{\mathrm{fin}}(f) = f^{|\alpha|}(\alpha)$ be the
result of applying $f$ to $\alpha$ $|\alpha|$ times. Then $\mathrm{gfp}_{\mathrm{fin}}(f)$ is a
fixed point of $f$, that is, $f(\mathrm{gfp}_{\mathrm{fin}}(f)) = \mathrm{gfp}_{\mathrm{fin}}(f)$.

The iterates of $f$ from $\alpha$ form a decreasing chain, and until it stabilizes each step
strictly decreases the cardinality.

Formalized by `Finset.gfpFin_fixed`, a theorem declared in [MathlibExt/Order/FixedPoints/Finset.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/FixedPoints/Finset.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/least-and-greatest-fixed-points-on-finite-sets/index.html#gfp-fin-fixed).

## The finite least fixed point lies in every pre-fixed point

Let $\alpha$ be a finite type
with $|\alpha|$ elements, let $f$ be a map from subsets of $\alpha$ to subsets of $\alpha$ that is
monotone for inclusion, and let $\mathrm{lfp}_{\mathrm{fin}}(f) = f^{|\alpha|}(\emptyset)$ be the
result of applying $f$ to $\emptyset$ $|\alpha|$ times. If $Z \subseteq \alpha$ satisfies
$f(Z) \subseteq Z$, then $\mathrm{lfp}_{\mathrm{fin}}(f) \subseteq Z$.

Every iterate of $f$ from $\emptyset$ is contained in $Z$, by induction.

Formalized by `Finset.lfpFin_le`, a theorem declared in [MathlibExt/Order/FixedPoints/Finset.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/FixedPoints/Finset.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/least-and-greatest-fixed-points-on-finite-sets/index.html#lfp-fin-le).

## Every post-fixed point lies in the finite greatest fixed point

Let $\alpha$ be a finite
type with $|\alpha|$ elements, let $f$ be a map from subsets of $\alpha$ to subsets of $\alpha$
that is monotone for inclusion, and let $\mathrm{gfp}_{\mathrm{fin}}(f) = f^{|\alpha|}(\alpha)$ be
the result of applying $f$ to $\alpha$ $|\alpha|$ times. If $Z \subseteq \alpha$ satisfies
$Z \subseteq f(Z)$, then $Z \subseteq \mathrm{gfp}_{\mathrm{fin}}(f)$.

$Z$ is contained in every iterate of $f$ from $\alpha$, by induction.

Formalized by `Finset.le_gfpFin`, a theorem declared in [MathlibExt/Order/FixedPoints/Finset.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/FixedPoints/Finset.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/least-and-greatest-fixed-points-on-finite-sets/index.html#le-gfp-fin).

## Finset and predicate iterations from the bottom agree

Let $\alpha$ be a type, let $f$ map
finite subsets of $\alpha$ to finite subsets of $\alpha$, and let $F$ map predicates on $\alpha$
to predicates on $\alpha$. For a finite set $Z \subseteq \alpha$ write $P_Z$ for the predicate
$t \mapsto t \in Z$, and suppose that for every finite $Z \subseteq \alpha$ and every
$s \in \alpha$, $s \in f(Z)$ if and only if $F(P_Z)(s)$ holds. Write $f^n$ and $F^n$ for the
$n$-fold iterates and $\bot$ for the predicate that is false everywhere. Then for every
$n \in \mathbb{N}$ and every $s \in \alpha$, $s \in f^n(\emptyset)$ if and only if $F^n(\bot)(s)$
holds.

Formalized by `Finset.mem_finset_iterate_iff`, a theorem declared in [MathlibExt/Order/FixedPoints/Finset.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/FixedPoints/Finset.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/least-and-greatest-fixed-points-on-finite-sets/index.html#mem-finset-iterate-iff).

## Finset and predicate iterations from the top agree

Let $\alpha$ be a finite type, let $f$
map subsets of $\alpha$ to subsets of $\alpha$, and let $F$ map predicates on $\alpha$ to
predicates on $\alpha$. For $Z \subseteq \alpha$ write $P_Z$ for the predicate
$t \mapsto t \in Z$, and suppose that for every $Z \subseteq \alpha$ and every $s \in \alpha$,
$s \in f(Z)$ if and only if $F(P_Z)(s)$ holds. Write $f^n$ and $F^n$ for the $n$-fold iterates
and $\top$ for the predicate that is true everywhere. Then for every $n \in \mathbb{N}$ and every
$s \in \alpha$, $s \in f^n(\alpha)$ if and only if $F^n(\top)(s)$ holds.

Formalized by `Finset.mem_finset_iterate_univ_iff`, a theorem declared in [MathlibExt/Order/FixedPoints/Finset.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/FixedPoints/Finset.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/least-and-greatest-fixed-points-on-finite-sets/index.html#mem-finset-iterate-univ-iff).

## Finite iteration computes the least fixed point

Let $\alpha$ be a finite type with
$|\alpha|$ elements, let $f$ be a map from subsets of $\alpha$ to subsets of $\alpha$ that is
monotone for inclusion, and let $\mathrm{lfp}_{\mathrm{fin}}(f) = f^{|\alpha|}(\emptyset)$ be the
result of applying $f$ to $\emptyset$ $|\alpha|$ times. Let $F$ be a map from predicates on $\alpha$
to predicates on $\alpha$ that is monotone for the pointwise order. For $Z \subseteq \alpha$
write $P_Z$ for the predicate $t \mapsto t \in Z$, and suppose that for every $Z \subseteq \alpha$
and every $s \in \alpha$, $s \in f(Z)$ if and only if $F(P_Z)(s)$ holds. Then for every
$s \in \alpha$, $s \in \mathrm{lfp}_{\mathrm{fin}}(f)$ if and only if $s$ satisfies the least
fixed point of $F$ in the complete lattice of predicates on $\alpha$.

One inclusion is iteration into the fixed point; the other is Park induction: the
$|\alpha|$-th iterate of $F$ from the everywhere-false predicate is pre-fixed because the
corresponding iterate of $f$ has stabilized, transported through the hypothesis relating $f$
and $F$.

Formalized by `Finset.mem_lfpFin_iff_lfp`, a theorem declared in [MathlibExt/Order/FixedPoints/Finset.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/FixedPoints/Finset.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/least-and-greatest-fixed-points-on-finite-sets/index.html#mem-lfp-fin-iff-lfp).

## Finite iteration computes the greatest fixed point

Let $\alpha$ be a finite type with
$|\alpha|$ elements, let $f$ be a map from subsets of $\alpha$ to subsets of $\alpha$ that is
monotone for inclusion, and let $\mathrm{gfp}_{\mathrm{fin}}(f) = f^{|\alpha|}(\alpha)$ be the
result of applying $f$ to $\alpha$ $|\alpha|$ times. Let $F$ be a map from predicates on $\alpha$
to predicates on $\alpha$ that is monotone for the pointwise order. For $Z \subseteq \alpha$
write $P_Z$ for the predicate $t \mapsto t \in Z$, and suppose that for every $Z \subseteq \alpha$
and every $s \in \alpha$, $s \in f(Z)$ if and only if $F(P_Z)(s)$ holds. Then for every
$s \in \alpha$, $s \in \mathrm{gfp}_{\mathrm{fin}}(f)$ if and only if $s$ satisfies the greatest
fixed point of $F$ in the complete lattice of predicates on $\alpha$.

This is dual to the corresponding statement for least fixed points.

Formalized by `Finset.mem_gfpFin_iff_gfp`, a theorem declared in [MathlibExt/Order/FixedPoints/Finset.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/FixedPoints/Finset.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/least-and-greatest-fixed-points-on-finite-sets/index.html#mem-gfp-fin-iff-gfp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Least and greatest fixed points on finite sets](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/least-and-greatest-fixed-points-on-finite-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Order/fixed-points-domain-theory/least-and-greatest-fixed-points-on-finite-sets)
