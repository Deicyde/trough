---
declaration: section
origin: cited
lean: OAI.KLInvariance.combinatorial_invariance
statement: formalized
proof: formalized
---

# 168. Combinatorial invariance of Kazhdan–Lusztig polynomials

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the full combinatorial invariance conjecture: isomorphic Bruhat intervals in arbitrary Coxeter systems have identical equal-parameter Kazhdan–Lusztig polynomials. Thus the abstract order of the interval determines the polynomial, even across different Coxeter systems.

## Combinatorial invariance of Kazhdan–Lusztig polynomials

We prove that an isomorphism of Bruhat intervals in arbitrary Coxeter systems preserves their equal-parameter Kazhdan–Lusztig polynomials. This resolves the full combinatorial invariance conjecture positively.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Combinatorial-Invariance-of-Kazhdan-Lusztig-Polynomials-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The combinatorial invariance conjecture asks whether a Kazhdan–Lusztig polynomial depends only on its Bruhat interval as an ordered set. The formalization proves that every order isomorphism between Bruhat intervals in arbitrary Coxeter systems preserves the corresponding equal-parameter Kazhdan–Lusztig polynomial. The two intervals may come from different Coxeter systems.

## Lean: Combinatorial invariance of Kazhdan–Lusztig polynomials

```lean
theorem combinatorial_invariance
    {B' : Type u'} {W' : Type v'} [Group W'] {M' : CoxeterMatrix B'}
    (cs : CoxeterSystem M W) (cs' : CoxeterSystem M' W')
    {u b : W} {u' b' : W'}
    (hub : BruhatLE cs u b) (hub' : BruhatLE cs' u' b')
    (ι : Interval cs u b ≃o Interval cs' u' b') :
    klPolynomial cs u b = klPolynomial cs' u' b'
```

Stated in [KLInvariance.lean, line 88](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/KLInvariance.lean#L88). Proved in [lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean, line 547](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/RepresentationTheory/KazhdanLusztig/Invariance.lean#L547).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/168.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/168.md)
