---
declaration: section
origin: cited
lean: MathlibExt.Algebra.Lie.LandmarkWanted.ado, MathlibExt.GroupTheory.AdoIwasawaWanted.RepresentationTheory.AdoIwasawa.adoIwasawa
statement: formalized
---

# Ado's theorem

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/ado-s-theorem/index.html).

## Ado's theorem

Every finite-dimensional Lie algebra $L$ over a field $K$ of
characteristic zero has a faithful finite-dimensional representation: there are a natural
number $n$ and an injective homomorphism of Lie algebras over $K$ from $L$ into the Lie algebra
of $K$-linear endomorphisms of $K^n$ with the commutator bracket.

Proof: Following Tao's 2011 route, the nilpotent and solvable cases are proved by induction using
finite-dimensional quotients of universal enveloping algebras. The general case uses the Levi
decomposition and combines the resulting radical representation with the adjoint representation.

## Sources

- I. D. Ado, Bull. Soc. Phys.-Math. Kazan 7 (1935) and 1947 char-zero theorem; Bourbaki, Lie Groups and Lie Algebras; Lean states char-zero finite-dimensional version while modern theorem extends to arbitrary fields.

Formalized by `MathlibExt.Algebra.Lie.LandmarkWanted.ado`, a theorem declared in [MathlibExt/Algebra/Lie/Ado.lean, line 2120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Lie/Ado.lean#L2120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/ado-s-theorem/index.html#ado).

## Ado–Iwasawa theorem

Let $K$ be a field and let $L$ be a finite-dimensional Lie algebra
over $K$. Then $L$ has a faithful finite-dimensional representation: there are a
finite-dimensional vector space $V$ over $K$ and an injective homomorphism of Lie algebras over
$K$ from $L$ to the Lie algebra of $K$-linear endomorphisms of $V$ with the commutator bracket.

## Sources

- K. Iwasawa, On the representation of Lie algebras, Japanese Journal of Mathematics 19 (1948), 405–426. See also the Tau Ceti Ado–Iwasawa roadmap, https://github.com/TauCetiProject/TauCetiRoadmap/pull/102. Problem `adoIwasawa` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.AdoIwasawaWanted.RepresentationTheory.AdoIwasawa.adoIwasawa` is written with `theorem_wanted` in [WantedExt/GroupTheory/AdoIwasawaWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AdoIwasawaWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/ado-s-theorem/index.html#ado-iwasawa).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ado's theorem](https://deicyde.github.io/atlas-lean/roadmap/Algebra/nonassociative-algebras/ado-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/nonassociative-algebras/ado-s-theorem)
