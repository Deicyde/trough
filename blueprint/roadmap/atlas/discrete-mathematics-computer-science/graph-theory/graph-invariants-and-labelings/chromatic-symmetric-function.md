---
declaration: section
origin: cited
lean: SimpleGraph.chromaticProfileCount, SimpleGraph.SameChromaticSymmetricFunction, SimpleGraph.SameChromaticSymmetricFunction.refl, SimpleGraph.SameChromaticSymmetricFunction.symm, SimpleGraph.SameChromaticSymmetricFunction.trans, SimpleGraph.SameChromaticSymmetricFunction.of_iso
statement: formalized
proof: formalized
---

# Chromatic symmetric function

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/chromatic-symmetric-function/index.html).

## Chromatic profile count

Let $G$ be a simple graph on a finite vertex set $V$, let $k$ be
a natural number and let $m : \{0, \dots, k-1\} \to \mathbb{N}$. The chromatic profile count of
$G$ at $k$ and $m$ is the number of proper colorings $c : V \to \{0, \dots, k-1\}$ of $G$ such
that for every color $i$, exactly $m(i)$ vertices $v$ satisfy $c(v) = i$.

These counts are the coefficients of the chromatic symmetric function.

Formalized by `SimpleGraph.chromaticProfileCount`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/ChromaticSymmetric.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/ChromaticSymmetric.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/chromatic-symmetric-function/index.html#chromatic-profile-count).

## Graphs with the same chromatic symmetric function

Let $G$ and $H$ be simple graphs on
finite vertex sets. We say that $G$ and $H$ have the same chromatic symmetric function when, for
every natural number $k$ and every $m : \{0, \dots, k-1\} \to \mathbb{N}$, the chromatic profile
count of $G$ at $k$ and $m$ equals that of $H$: both graphs have equally many proper colorings
with colors $\{0, \dots, k-1\}$ in which each color $i$ is used on exactly $m(i)$ vertices.

This is equality of chromatic symmetric functions, expressed through their coefficients.

Formalized by `SimpleGraph.SameChromaticSymmetricFunction`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/ChromaticSymmetric.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/ChromaticSymmetric.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/chromatic-symmetric-function/index.html#same-chromatic-symmetric-function).

## Reflexivity of having the same chromatic symmetric function

Every simple graph on a
finite vertex set has the same chromatic symmetric function as itself.

Formalized by `SimpleGraph.SameChromaticSymmetricFunction.refl`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/ChromaticSymmetric.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/ChromaticSymmetric.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/chromatic-symmetric-function/index.html#refl).

## Symmetry of having the same chromatic symmetric function

Let $G$ and $H$ be simple
graphs on finite vertex sets. If $G$ has the same chromatic symmetric function as $H$, then $H$
has the same chromatic symmetric function as $G$.

Formalized by `SimpleGraph.SameChromaticSymmetricFunction.symm`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/ChromaticSymmetric.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/ChromaticSymmetric.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/chromatic-symmetric-function/index.html#symm).

## Transitivity of having the same chromatic symmetric function

Let $G$, $H$ and $K$ be
simple graphs on finite vertex sets. If $G$ has the same chromatic symmetric function as $H$, and
$H$ has the same chromatic symmetric function as $K$, then $G$ has the same chromatic symmetric
function as $K$.

Formalized by `SimpleGraph.SameChromaticSymmetricFunction.trans`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/ChromaticSymmetric.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/ChromaticSymmetric.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/chromatic-symmetric-function/index.html#trans).

## Isomorphic graphs have the same chromatic symmetric function

If $G$ and $H$ are
isomorphic simple graphs on finite vertex sets, then $G$ and $H$ have the same chromatic
symmetric function.

The proof transports colorings and their color classes along the isomorphism.

Formalized by `SimpleGraph.SameChromaticSymmetricFunction.of_iso`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/ChromaticSymmetric.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/ChromaticSymmetric.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/chromatic-symmetric-function/index.html#of-iso).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Chromatic symmetric function](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/chromatic-symmetric-function/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/graph-invariants-and-labelings/chromatic-symmetric-function)
