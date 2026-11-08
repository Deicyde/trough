# Dedekind ideal arithmetic

> Reusable ideal arithmetic, module indices and intrinsic heights of normed invertible modules over rings of integers. Ideal-norm comparisons, principal-prime extraction and class-group localization sit alongside finite section quotients, common scalar multiples, integral-section heights and normalized logarithmic heights, with tensor-product, positive metric-rescaling and equivalence-pullback formulas. Rational frames evaluate the same intrinsic height through coefficient-ideal norms and weighted archimedean products. Nonzero fractional-ideal norms factor as finite-support prime-norm products with signed exponents; over number fields, negative coefficient-ideal exponents give the finite-place numerator of height. Supplied frames extend to linear coordinates over semiring algebras. Over an infinite Dedekind domain with finite quotients, invertible modules have canonical definite ultrametric seminorms on their adic fibres, characterized in every rational frame by the residue cardinality raised to the signed coefficient-ideal count, times the coordinate norm. Principal fractional-ideal counts determine scalar adic valuations and residue-cardinality completion norms. Rank-one seminorm scalar extension, relative-degree formulas for weighted infinite-place products, fractional-ideal norm extension and isometric completion maps supply further interfaces.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/formalization.yaml) of [FormalFrontier/dedekind-ideal-arithmetic](https://github.com/FormalFrontier/dedekind-ideal-arithmetic) at commit [c7630759](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/tree/c76307595a1151abc42eacc9a815cb2d1bba6dc8), Apache-2.0.*

5 articles: 5 for highlights of its formalization.yaml whose declarations the scan finds. The headline results in its README are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/dedekind-ideal-arithmetic](https://github.com/FormalFrontier/dedekind-ideal-arithmetic), read at commit [c7630759](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/tree/c76307595a1151abc42eacc9a815cb2d1bba6dc8) (2026-11-05).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “agent-reviewed”.
- Review notes: “AI agents reviewed the ideal-norm, principal-prime and localization results; no human review is claimed.”
- Automation: agent; framework “AI agents using Lean and Lake”; tool setup “AI agents composed Lean proofs using mathlib APIs and ordinary tactics such as rw, simp, constructor, congr, by_cases and typeclass inference. Toolchain and dependency revisions are pinned by the repository's Lean/Lake files.”
- Automation notes: “AI agents authored the Lean proofs and documentation. AI involvement does not itself establish origin, correctness or rights.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- [The K-book: An Introduction to Algebraic K-theory](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.pdf), Charles A. Weibel, Complete-book build dated 2013-08-29, Chapter I, section 3 (book; background).
- *Ideal class groups under localization of Dedekind domains* (folklore; independently-proves).
- *Abelian Varieties*, J. S. Milne, IV section 6, 6.2–6.3 (book; background).

## Builds on

No other Formal Frontier library.

## Highlights

- [Ideal norms, factorization and principal primes](ideal-norms-factorization-and-principal-primes.md)
- [Class groups under localization](class-groups-under-localization.md)
- [Section indices and rational-frame coordinates](section-indices-and-rational-frame-coordinates.md)
- [Intrinsic heights of normed invertible modules](intrinsic-heights-of-normed-invertible-modules.md)
- [Adic fibre seminorms and integral spans](adic-fibre-seminorms-and-integral-spans.md)

## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/README.md#headline-results) of [FormalFrontier/dedekind-ideal-arithmetic](https://github.com/FormalFrontier/dedekind-ideal-arithmetic) at commit [c7630759](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/tree/c76307595a1151abc42eacc9a815cb2d1bba6dc8), Apache-2.0.*

**Norm detects strict ideal inclusion and equality.** In an infinite
commutative Dedekind domain with finite quotients, `I < J` and `I ≠ ⊥`
imply `J.absNorm < I.absNorm`. If `I ≤ J` and the norms agree, `I = J`,
including zero ideals. No finite-free presentation over `ℤ` is needed.
See [strict comparison](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Ideal/AbsNorm.lean#L29)
and [equality](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Ideal/AbsNorm.lean#L42).

**A supplied prime-norm element yields a principal prime.** In an infinite
Dedekind domain finite free over `ℤ`, a natural prime `p` and a supplied
`α` with `(Algebra.norm ℤ α).natAbs = p` give a principal prime above
`(p)`. This is conditional existence, not a search for `α`, a class-number
computation or a witness assertion for every prime. See
[principal-prime extraction](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Ideal/PrincipalPrime.lean#L27).

**Localization can kill the class group and give a PID/UFD.** For Dedekind
domains `A, B` in possibly different universes, an `A`-algebra `B`
torsion-free over `A`, and
`IsLocalization M B`, extension `Cl(A) → Cl(B)` is
[surjective](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/ClassGroup/Localization.lean#L37).
If every source class is an integral power of a supplied `g` and `g`
extends to one, the library gives a
[PID](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/ClassGroup/Localization.lean#L59) and hence a
[UFD](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/ClassGroup/Localization.lean#L81).
Surjectivity needs no generator; neither class group need be finite.

**Section indices and common multiples.** Over a domain, scaling a
nonzero section of a torsion-free module multiplies its quotient index by
the principal left-ideal index, including zero scalars and infinite quotients.
Invertible modules over commutative domains with finite quotients have finite
quotients by nonzero sections; over any commutative domain their nonzero
sections admit common nonzero scalar multiples. See
[module indices](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/Index.lean).

**Intrinsic heights of normed invertible modules.** Over `𝓞 K` for a number
field `K`, definite seminorms on all archimedean fibres give a positive,
section-independent height: quotient index divided by the weighted norm
product. Invertibility, not integral freeness, is assumed. Tensor products,
positive rescaling and integral-equivalence pullback obey the expected
multiplicative and logarithmic laws. The normalized logarithmic height can
be negative. See [module heights](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/NumberField/ModuleHeight.lean)
and the [height guide](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/docs/RationalFrameHeight.md#intrinsic-height-and-sections).

**Rational-frame and finite-place height formulas.** Every rational frame
evaluates this same intrinsic height as `1 / (N(I) * archimedeanProduct)`.
Nonzero fractional-ideal norms factor into prime norms with signed exponents
over Dedekind domains finite free over `ℤ`, without a number-field structure
on the fraction field. For number fields the height numerator uses residue
cardinalities with **negative** coefficient-ideal counts. See
[fractional norms](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Ideal/FractionalNorm.lean) and
[finite-place height factors](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/NumberField/FinitePlaceHeight.lean).

**Principal exponents determine scalar completion norms.** Over a Dedekind
domain and fraction field, a nonzero scalar has adic valuation equal to the
exponential of its negative principal-ideal count. For an infinite base with
finite quotients, its completion norm is the residue cardinality to that
negative count. No norm on bare `K` is chosen. See
[adic norms](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Ideal/AdicNorm.lean).

**Sharp signed fractional-ideal exponents.** At each fixed height-one prime
of any Dedekind domain, a nonzero fractional ideal contains a nonzero element
attaining its signed count. Together with Mathlib's `count_mono`, this is an
attained minimum. The witness may depend on the prime; no principality,
infinite-ring, finite-residue or `ℤ`-freeness hypothesis is needed. See
[count attainment](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Ideal/CountAttainment.lean).

**Algebraic integral spans in adic fibres.** For any `R`-module `M` over a
Dedekind domain with fraction field `K` and height-one prime `p`, the span of
`1 ⊗ m` over the valuation integers in `F ⊗[R] M`,
`F = p.adicCompletion K`, is the image of
`O ⊗[R] M`, `O = p.adicCompletionIntegers K`. It is finite over `O` if
`M` is finite, and spans the whole fibre over `F`; flatness makes the image
map an equivalence onto the span. For `M = R`, the whole span corresponds
exactly to `O`. No finite-residue or infinite-ring hypothesis is used. See
[integral spans](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/AdicIntegralSpan.lean).

**Canonical ultrametric seminorms on adic fibres.** For an infinite Dedekind
domain `R` with finite quotients, fraction field `K`, height-one prime `p`
and invertible `M`, the fibre `F ⊗[R] M` has a canonical definite
`F`-seminorm. In every rational frame, on every vector, it is the coordinate
norm times the residue cardinality raised to the signed coefficient-ideal
count, with a **plus** sign; negative counts are included. It is
frame-independent and characterized by its rational-unit-vector weight.
The supplied-frame constructor only needs finite `M` and a frame,
allowing torsion. For `M = R` the whole seminorm is the completion norm
pulled back along tensor right-unit equivalence. See
[adic seminorms](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/AdicSeminorm.lean).

## Main results

Its formalization.yaml lists 44 main results, and the scan finds 44 of them declared in the file the yaml gives; they are on their own page, not made articles.

- [Main results](main-results/README.md)
