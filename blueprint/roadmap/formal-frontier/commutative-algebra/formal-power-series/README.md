# Formal power series

> Integral weighted negative logarithmic derivatives of native formal-power-series units over arbitrary commutative rings, with group laws, naturality and finite coefficient formulas; and coefficientwise ideal-adically restricted native multivariate power series with finite polynomial reductions, regular-principal internal kernels. Polynomial completion over any commutative coefficient ring is the algebra of series over its adic completion with polynomial images at every original quotient precision; coefficient transport recovers the original restricted-series ring equivalence for adically complete coefficients. Ideal-preserving coefficient maps and arbitrary variable maps on these completed-coefficient series give functorial ring maps with finite source-row fiber sums, including infinite fibers. The polynomial-completion comparison is natural in both directions, with completed-scalar compatibility and raw row-kernel containment, without original completeness or finiteness assumptions. The restricted subring also has a coefficient-ring algebra structure, all-level surjective scalar-linear polynomial reductions, and regular-principal module-quotient equivalences, including a separate native-integer API for default module instances. Over adically complete coefficient rings, every polynomial linear endomorphism extends to the restricted series, with finite-level and kernel-preserving uniqueness laws. Independently of completeness, coefficientwise reduction kernels multiply into the kernel at the sum of their levels, including finite-sum laws. For adically complete coefficient rings, units of the restricted subring are detected by the first polynomial reduction or by constant and nonconstant coefficient criteria, with no finite-variable restriction. Over finitely many variables, restrictedness has a degree-cutoff criterion; if the coefficient ideal is finitely generated, every reduction kernel is the intrinsic algebraic image ideal of its corresponding ideal power. Separate restricted-series modules add coefficient content, intrinsic actual-ring leading terms, division under adic/valuation hypotheses and conditional ideal generation by a finite primitive family. A generic support leaf compares cofinal ideal-adic filtrations on arbitrary modules. Change-of-ideal maps and surjective polynomial reduction work for arbitrary ideals and variables. Local-ring polynomial residue is compatible with valuation-domain residue; injective first-variable regrouping has polynomial and finite-variable reindexing interfaces. Intrinsic leading products and singleton division have separate Hausdorff uniqueness and complete primitive-existence interfaces; first-variable division yields finite-polynomial remainders. A supplied division of X₀^d by a divisor with regrouped residue degree d and nonzero scalar top, with actual remainder support below d, gives constant-unit quotient residue; radical equality and completeness reflect it to a unit. With a nonzero principal-adic parameter in the maximal ideal of a commutative valuation domain, radical equality and completeness, a restricted series whose regrouped residue polynomial has degree d and nonzero scalar top coefficient admits a unique unit multiplier and monic first-variable polynomial of degree d, even among competing multipliers not assumed units; coefficient primitivity is derived from the top term.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/formalization.yaml) of [FormalFrontier/formal-power-series](https://github.com/FormalFrontier/formal-power-series) at commit [29bdab8c](https://github.com/FormalFrontier/formal-power-series/tree/29bdab8c1f57472100a579c97a589effaea11987), Apache-2.0.*

No articles: its formalization.yaml lists no highlights, and none of the 9 headline results in its README names a declaration that the linked file declares at this commit, so they are quoted below.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/formal-power-series](https://github.com/FormalFrontier/formal-power-series), read at commit [29bdab8c](https://github.com/FormalFrontier/formal-power-series/tree/29bdab8c1f57472100a579c97a589effaea11987) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “The library's Lean mathematics has received independent review. Source correspondence and coverage are separate decisions.”
- Review notes: “Proofs in the checked Lean sources depend only on propext, Classical.choice and Quot.sound, including private declarations. README.md and API.md describe the public API and its limits.”
- Automation: agent; framework “OpenAI Codex CLI / Formal Frontier Hive”; tool setup “Formal Frontier AI contributors formalized the weighted derivative using mathlib's native power-series APIs and ordinary-import clients. Prism authored the original weighted-derivative proof expression; other contributors adapted its argument, and Folio contributed derivative documentation. Distinct contributors developed the restricted-series carrier, principal kernel, inverse-limit, scalar-linear quotient, linear extension and kernel-filtration proofs; others developed content, selected factorization, leading terms, monic parameters, restricted division, cofinal comparison and conditional primitive ideal generation. The completed-coefficient polynomial comparison reuses the full AdicModules direct-sum completion equivalence and its canonical restriction-of-scalars and completed coefficient-map interfaces. Coefficient change uses Mathlib's coefficientwise power-series maps; arbitrary variable maps use its polynomial renaming and finite dependent direct-sum pushforward, completed through that same whole AdicModules equivalence rather than through the polynomial-completion comparison. Contributors to the finite-variable degree criterion, its infinite-variable counterexample and the finite-generation kernel argument were distinct from those who formalized the results and wrote ordinary-import clients. Further contributors developed and formalized restricted-subring unit detection, using the geometric inverse and kernel-filtration APIs, and wrote its ordinary-import client. The pinned MultivariatePolynomials library supplies polynomial linear-division and monic-lifting algorithms. The antidiagonal multiplication method adapts Jz Pan's Apache-2.0 mathlib argument.”

## Scope

Three independent reusable constructions: the weighted negative logarithmic derivative of power-series units over arbitrary commutative rings; coefficientwise ideal-adically restricted multivariate series; and the rational Artin–Hasse exponential, including its finite Euler-prefix theorem and separate p-integrality module. The rational recurrence holds for 2 ≤ p, including composite p; the Euler-prefix theorem and p-integrality require prime p. The rational core does not import p-adic theory, and p-integrality is proved independently of the Euler identity. The restricted-series family comes with a generic cofinality support leaf. The curated main_results below locate selected restricted-series, completion-map, naturality, scalar-linear quotient, linear-extension, kernel-product, unit, content, cofinality and division interfaces; further declarations are documented in API.md. Generic reductions work for arbitrary ideals; internal division and principal quotients require a regular generator. The completed-coefficient polynomial algebra equivalence has no completeness hypothesis. Its ideal-preserving coefficient and arbitrary-variable naturality holds forward and inverse on all elements, including infinite fibers and precision zero; identity, composition, polynomial, scalar and raw-kernel laws use the original quotient rows. Its original-coefficient specialization and generic linear extension require coefficient adic completeness, and linear-extension uniqueness also assumes all-level kernel preservation. Kernel products are coefficientwise, not intrinsic restricted-ring ideal powers. Unit criteria concern the existing restricted subring over arbitrary variables and ideals when the coefficient ring is I-adically complete; coefficient tests use the quotient by I and the radical of I. For finite variables the degree-cutoff equivalence applies, and with a finitely generated coefficient ideal the kernel is the intrinsic algebraic image ideal at every level, including zero. Neither result asserts arbitrary-variable finite-generation kernels or source coverage. The ideal-generation result assumes, rather than constructs, a finite primitive family with the required actual-R leading-term-ideal equality. These result locators do not assert whole-source coverage. Ideal-change reduction, variable renaming, and first-variable regrouping preserve their coefficient formulas over arbitrary commutative rings and ideals, without completeness, finite-variable, or nontriviality assumptions. The local-ring residue map requires a local ring, hence a nontrivial ring, but no completeness or nonzero-parameter hypothesis. Intrinsic leading-exponent products and singleton uniqueness require Hausdorffness, not completeness. Primitive singleton and first-variable division add the nonzero parameter, radical identity and completeness. Conditional quotient-residue computation starts from a division of the distinguished first-variable monomial X₀^d by a divisor whose regrouped residue has degree d and nonzero scalar top, with an actual remainder supported below d. Radical equality and completeness reflect this to a unit; these results do not construct a division.

*Quoted from the status in [formalization.yaml](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/formalization.yaml) of [FormalFrontier/formal-power-series](https://github.com/FormalFrontier/formal-power-series) at commit [29bdab8c](https://github.com/FormalFrontier/formal-power-series/tree/29bdab8c1f57472100a579c97a589effaea11987), Apache-2.0.*

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *The K-book: An Introduction to Algebraic K-theory*, Charles A. Weibel, Section II.4 and Exercise 4.6 (book; adapts).
- *Foundations of Rigid Geometry I*, Kazuhiro Fujiwara, Fumiharu Kato (book; background).

## Builds on

- [Adic modules](../adic-modules/README.md) (a Lake dependency, pinned at 5fbe4fe9)
- [Coherent modules](../coherent-modules/README.md) (a Lake dependency, pinned at 3ecdd76a)
- [Multivariate polynomials](../multivariate-polynomials/README.md) (a Lake dependency, pinned at 5d58abb9)


## Headline results

**Weighted unit derivative.** Over an arbitrary commutative ring `R`, for a native unit
`f : (PowerSeries R)ˣ`, `negXLogDeriv f = -X * f' * f⁻¹`, weighted by
**negative `X`**. Products become sums, inverses become negatives and integer
powers become integer multiples, naturally under coefficient-ring homomorphisms.
Integral convolution works without normalization; a division-free **forward**
recurrence for derivative coefficients requires constant coefficient one.
Linear factors `1 - C a * X` give signed power sums for finite products,
including inverse factors and the empty family.

This is neither reconstruction nor injectivity: constant units and, under
`[CharP R p]`, `p`-th powers lie in the kernel; even normalized nonidentity
units can do so. No formal logarithm, lambda/Witt structure, splitting extension
or Adams operation is asserted. See the [full formulas and limitations](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/RESULTS.md#weighted-unit-derivative)
and [source](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/UnitLogDerivative.lean).

**Rational Artin–Hasse exponential.** The rational formal construction is defined for every natural `p` and has
constant and linear coefficients one. For `2 ≤ p` (composite `p` allowed), it is
`exp (∑ i ≥ 0, X^(p^i) / p^i)`; the coefficient recurrence together with
`a_0 = 1` determines it uniquely. The recurrence fails at `p = 1`, degree two.

For **prime `p` only**, its degree-`k` coefficient equals that of every finite
Euler product of `(1 - X^n)^(-μ(n)/n)` over positive `n ≤ N` coprime to `p`,
when `k ≤ N`. This is coefficientwise, not an infinite-product or analytic
convergence assertion. Prime `p` also gives coefficient p-integrality
(multiplicative p-adic valuation at most one), by an independent
Dieudonné–Dwork proof using p-adic divided powers, **not** the Euler identity.
The rational core does not import p-adic theory. See [details and examples](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/RESULTS.md#rational-artinhasse-exponential),
the [rational core](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/ArtinHasse.lean),
[Euler product](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/ArtinHasseEulerProduct.lean) and
[separate p-adic module](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/ArtinHasse/Padic.lean).

### Ideal-adically restricted multivariate series

For any family `q : ∀ i, C →+* Q i` of homomorphisms between commutative
semirings, `MvPowerSeries.polynomialReductionSubalgebra σ q` consists of
series whose coefficientwise image under each `q i` is polynomial, equivalently
has finite coefficient support. It uses the usual coefficient-`C` algebra and
needs no compatibility, surjectivity, nonempty index type or finite variable
type. Its polynomial inclusion and finite reductions are homomorphisms;
a surjective row gives a surjective reduction. An empty family gives the whole
series algebra, and one identity row gives precisely the polynomial subalgebra,
with reduction inverse to inclusion.

For arbitrary variable types, commutative coefficient rings and ideals `I`,
restrictedness requires that, at each `k`, only finitely many **monomial indices**
have coefficients outside `I ^ k`. The restricted subring has surjective polynomial reductions, including
`k = 0`, ideal-change maps, and residue maps for parameters in a local ring's
maximal ideal. This subring and its reductions specialize the same construction
to `q k = Ideal.Quotient.mk (I ^ k)`.

**Regrouping and kernels.** First-variable regrouping is injective, not an
equivalence with all iterated restricted series. Finite variables give a
degree-cutoff criterion; with `I.FG` they also identify the intrinsic
algebraic reduction kernel at every level. Regular principal ideals admit
internal division and scalar-linear quotient equivalences. For arbitrary
variables and ideals, coefficientwise reduction kernels multiply from levels
`n`, `k` into level `n + k`, without completeness or finite generation; this
does **not** identify intrinsic ideal powers or give an arbitrary-ideal
intrinsic kernel identity.

**Completion and units.** For arbitrary `R`, `I` and `σ`,
`MvPolynomial.adicCompletionEquiv σ I` identifies polynomial completion with
the algebra of series over `AdicCompletion I R` that become polynomials under
every original quotient evaluation. It uses the named
`AdicCompletion.extendedAlgebra` on the source, not a new global instance.
Under `[IsAdicComplete I R]`, coefficient transport recovers the original
ring equivalence with restricted series over `R`. Neither assertion assumes
intrinsic completeness of arbitrary polynomial completions. Under coefficient
completeness, a restricted series `f` is a unit exactly when `adicReduction I 1 f` is a unit,
equivalently when its constant coefficient is a unit and every other
coefficient lies in `I.radical`.

**Coefficient and variable maps.** For commutative rings `R`, `T`, ideals
`I`, `J`, a homomorphism `f : R →+* T`, `hf : I ≤ J.comap f`, and any variable
map `g : σ → τ`, the completed-coefficient series above admit a ring map
`MvPowerSeries.completedRestrictedMap I J f hf g`. Infinite fibers are
allowed: at each precision its coefficients are finite sums over the source
polynomial reduction's support. Coefficient change is coefficientwise along
`AdicCompletion.mapRingHom I J f hf`; renaming completes a finite direct-sum
pushforward using the whole completion/restricted-product equivalence,
independently of the polynomial-completion comparison. Identity, composition,
polynomial and scalar laws hold, and `MvPolynomial.adicCompletionEquiv`
commutes with these maps in both directions on all elements. No completeness,
separation, finite generation or finite-variable hypothesis is required.
See the [map API](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/API.md#coefficient-change-arbitrary-variable-maps-and-naturality).

**Linear extension.** Under `[IsAdicComplete I R]`, every polynomial
`R`-linear endomorphism extends to an `R`-linear restricted-series operator
with finite-level equations. Uniqueness needs **both** agreement on
polynomials and preservation of **every** coefficientwise reduction kernel;
no ring-homomorphism extension or intrinsic restricted-ring completeness is
asserted. See the [extension guide](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearExtension/README.md).

**Content, leading terms and division.** Separated prevaluation rings give
selected-coefficient content factorization. Over a valuation domain separated
for the principal ideal of a parameter in its maximal ideal, intrinsic
leading terms are polynomials over the actual ring `R`. Any two supplied
divisions by a nonzero singleton divisor with actual-supported remainders
agree; arbitrary-divisor existence is not asserted. Primitive-divisor
existence and conditional ideal generation additionally require a nonzero
parameter, radical equal to the maximal ideal, and adic completeness.
Under those hypotheses, a finite primitive family in a restricted-series
ideal generates it **if** its actual-`R` leading terms generate the full
polynomial leading-term ideal. No standard-basis existence is asserted;
conditional quotient-unit reflection does not construct a division.

**First-variable preparation.** Over a commutative valuation domain complete
for the principal ideal of a nonzero parameter in its maximal ideal, with
that ideal's radical equal to the maximal ideal, let a restricted series `f`
in `Fin (n + 1)` variables have regrouped maximal-ideal residue polynomial
of degree `d` with nonzero scalar top coefficient `C c`. There is a unique
pair consisting of a restricted unit `u` and a monic first-variable polynomial
`G` of exact degree `d` with `polynomialRestrictedFinFirst _ n G = u * f`.
Actual-coefficient primitivity follows; uniqueness even allows competing
multipliers not assumed units. **`n = 0` and `d = 0` are included**. See the
[preparation guide](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariablePreparation/README.md).

**Generic cofinal support.** For any `R`-module, `I ≤ J`, `1 ≤ N` and
`J ^ N ≤ I` equate separation, precompleteness and completeness for the two
filtrations; this separately importable result needs no restricted series.

See the [complete restricted-series results and limitations](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/RESULTS.md#ideal-adically-restricted-multivariate-series)
and [module guide](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/README.md).
These results do not assert norm/radius or variable-adic restrictions, general
base change, standard-basis existence, or source coverage.

For completed-coefficient maps, choose one of these direct imports; paths are
relative to `FormalPowerSeries.MvPowerSeries.IdealAdicRestricted`.

| Module | Use |
| --- | --- |
| [`CompletionMap`](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/CompletionMap.lean) | Canonical map between polynomial completions, quotient squares and completed-scalar compatibility |
| [`CompletedRename`](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/CompletedRename.lean) | Arbitrary variable maps on series over completed coefficients, including infinite fibers |
| [`Naturality`](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Naturality.lean) | Coefficient change, joint maps, functoriality and forward/inverse naturality of the completion comparison |

## Main results

The 96 main results its formalization.yaml lists (`status.main_results`). They are listed here, not made articles: in several Formal Frontier libraries this list is close to the whole API.

| Declaration | Kind | Where | Note |
| --- | --- | --- | --- |
| `MvPowerSeries.restrictedProductEquivPolynomialReduction` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/InverseLimit.lean, line 117](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/InverseLimit.lean#L117) |  |
| `MvPolynomial.adicCompletionMap` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/CompletionMap.lean, line 92](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/CompletionMap.lean#L92) |  |
| `MvPolynomial.adicPolynomialLevelEquiv_evalₐ_adicCompletionMap` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/CompletionMap.lean, line 171](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/CompletionMap.lean#L171) |  |
| `MvPolynomial.adicCompletionMap_comp_completedCoefficient` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/CompletionMap.lean, line 237](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/CompletionMap.lean#L237) |  |
| `MvPowerSeries.completedRestrictedRename` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/CompletedRename.lean, line 230](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/CompletedRename.lean#L230) |  |
| `MvPowerSeries.completedRestrictedCoeffMap` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Naturality.lean, line 76](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Naturality.lean#L76) |  |
| `MvPowerSeries.completedRestrictedMap` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Naturality.lean, line 312](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Naturality.lean#L312) |  |
| `MvPowerSeries.coeff_completedRestrictedMap_eval` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Naturality.lean, line 350](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Naturality.lean#L350) |  |
| `MvPowerSeries.completedRestrictedMap_comp` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Naturality.lean, line 409](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Naturality.lean#L409) |  |
| `MvPowerSeries.completedRestrictedMap_comp_algebraMap` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Naturality.lean, line 508](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Naturality.lean#L508) |  |
| `MvPowerSeries.ker_polynomialReduction_le_comap_completedRestrictedMap` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Naturality.lean, line 566](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Naturality.lean#L566) |  |
| `MvPolynomial.adicCompletionEquiv_naturality` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Naturality.lean, line 687](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Naturality.lean#L687) |  |
| `MvPolynomial.adicCompletionEquiv_symm_naturality` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Naturality.lean, line 816](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Naturality.lean#L816) |  |
| `MvPowerSeries.IsAdicallyRestricted.mono` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/IdealChange.lean, line 29](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/IdealChange.lean#L29) |  |
| `MvPowerSeries.restrictAlongIdeal` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/IdealChange.lean, line 45](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/IdealChange.lean#L45) |  |
| `MvPowerSeries.restrictAlongIdeal_trans` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/IdealChange.lean, line 70](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/IdealChange.lean#L70) |  |
| `MvPowerSeries.reductionAtLargerIdeal` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/IdealChange.lean, line 88](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/IdealChange.lean#L88) |  |
| `MvPowerSeries.reductionAtLargerIdeal_surjective` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/IdealChange.lean, line 113](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/IdealChange.lean#L113) |  |
| `MvPowerSeries.restrictedResidueHom` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/ValuationResidue.lean, line 33](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/ValuationResidue.lean#L33) |  |
| `MvPowerSeries.restrictedResidueHom_apply` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/ValuationResidue.lean, line 64](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/ValuationResidue.lean#L64) |  |
| `MvPowerSeries.restrictedRenameEquiv` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Rename.lean, line 46](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Rename.lean#L46) |  |
| `MvPowerSeries.restrictedFirstRegroup` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableRegrouping.lean, line 76](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableRegrouping.lean#L76) |  |
| `MvPowerSeries.polynomialRestrictedFirst` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableRegrouping.lean, line 199](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableRegrouping.lean#L199) |  |
| `MvPowerSeries.restrictedFirst_actual_support_iff` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableRegrouping.lean, line 244](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableRegrouping.lean#L244) |  |
| `MvPowerSeries.restrictedFinSuccEquiv` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableRegrouping/Fin.lean, line 28](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableRegrouping/Fin.lean#L28) |  |
| `MvPowerSeries.restrictedFinFirst_actual_support_iff` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableRegrouping/Fin.lean, line 140](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableRegrouping/Fin.lean#L140) |  |
| `MvPowerSeries.isUnit_adicallyRestricted_iff_adicReduction_one` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/UnitDetection.lean, line 28](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/UnitDetection.lean#L28) |  |
| `MvPowerSeries.isUnit_adicallyRestricted_iff_coeff_mod_ideal` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/UnitDetection.lean, line 65](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/UnitDetection.lean#L65) |  |
| `MvPowerSeries.isUnit_iff_quotient_of_isAdicComplete` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/UnitDetection.lean, line 77](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/UnitDetection.lean#L77) |  |
| `MvPowerSeries.isUnit_adicallyRestricted_iff_coeff_radical` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/UnitDetection.lean, line 85](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/UnitDetection.lean#L85) |  |
| `MvPowerSeries.isAdicallyRestricted_iff_degree_cutoff` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/DegreeDecay.lean, line 38](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/DegreeDecay.lean#L38) |  |
| `MvPowerSeries.exists_restricted_fg_decomposition` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FinitelyGeneratedKernel.lean, line 30](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FinitelyGeneratedKernel.lean#L30) |  |
| `MvPowerSeries.ker_adicReduction_fg` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FinitelyGeneratedKernel.lean, line 107](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FinitelyGeneratedKernel.lean#L107) |  |
| `MvPowerSeries.adicallyRestrictedAlgebra` | instance | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 30](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L30) |  |
| `MvPowerSeries.algebraMap_adicallyRestricted_coe` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 35](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L35) |  |
| `MvPowerSeries.coe_smul_adicallyRestricted` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 42](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L42) |  |
| `MvPowerSeries.coeff_smul_adicallyRestricted` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 49](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L49) |  |
| `MvPowerSeries.algebraAdicReduction` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 56](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L56) |  |
| `MvPowerSeries.linearAdicReduction` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 63](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L63) |  |
| `MvPowerSeries.linearAdicReduction_apply` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 68](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L68) |  |
| `MvPowerSeries.coeff_linearAdicReduction` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 74](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L74) |  |
| `MvPowerSeries.linearAdicReduction_surjective` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 80](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L80) |  |
| `MvPowerSeries.principalAdicConstant_mul_eq_smul` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 85](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L85) |  |
| `MvPowerSeries.ker_linearAdicReduction_principal` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 95](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L95) |  |
| `MvPowerSeries.principalLinearQuotientEquiv` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 125](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L125) |  |
| `MvPowerSeries.principalLinearQuotientEquiv_mk` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 137](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L137) |  |
| `MvPowerSeries.intLinearAdicReduction` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 144](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L144) |  |
| `MvPowerSeries.intLinearAdicReduction_apply` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 149](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L149) |  |
| `MvPowerSeries.coeff_intLinearAdicReduction` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 155](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L155) |  |
| `MvPowerSeries.intLinearAdicReduction_surjective` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 161](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L161) |  |
| `MvPowerSeries.principalAdicConstant_mul_eq_int_smul` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 166](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L166) |  |
| `MvPowerSeries.ker_intLinearAdicReduction_principal` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 179](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L179) |  |
| `MvPowerSeries.principalIntLinearQuotientEquiv` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 209](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L209) |  |
| `MvPowerSeries.principalIntLinearQuotientEquiv_mk` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean, line 221](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearQuotient.lean#L221) |  |
| `MvPowerSeries.polynomialLinearMapMod` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearExtension.lean, line 28](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearExtension.lean#L28) |  |
| `MvPowerSeries.polynomialLinearMapMod_map` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearExtension.lean, line 45](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearExtension.lean#L45) |  |
| `MvPowerSeries.polynomialLinearMapMod_factorPow` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearExtension.lean, line 60](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearExtension.lean#L60) |  |
| `MvPowerSeries.restrictedLinearExtension` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearExtension.lean, line 163](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearExtension.lean#L163) |  |
| `MvPowerSeries.adicReduction_restrictedLinearExtension` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearExtension.lean, line 186](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearExtension.lean#L186) |  |
| `MvPowerSeries.restrictedLinearExtension_polynomial` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearExtension.lean, line 195](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearExtension.lean#L195) |  |
| `MvPowerSeries.restrictedLinearExtension_preserves_ker` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearExtension.lean, line 207](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearExtension.lean#L207) |  |
| `MvPowerSeries.restrictedLinearExtension_unique` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearExtension.lean, line 218](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LinearExtension.lean#L218) |  |
| `MvPowerSeries.coeff_mul_mem_ideal_mul_ideal` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/KernelFiltration.lean, line 44](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/KernelFiltration.lean#L44) |  |
| `MvPowerSeries.adicReduction_mul_eq_zero` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/KernelFiltration.lean, line 54](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/KernelFiltration.lean#L54) |  |
| `MvPowerSeries.adicReduction_sum_mul_eq_zero` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/KernelFiltration.lean, line 75](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/KernelFiltration.lean#L75) |  |
| `MvPowerSeries.adicReduction_sum_mul_eq_zero_succ` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/KernelFiltration.lean, line 85](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/KernelFiltration.lean#L85) |  |
| `MvPowerSeries.IsAdicallyRestricted.exists_span_range_eq_span_coeff` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Content.lean, line 59](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Content.lean#L59) |  |
| `MvPowerSeries.IsAdicallyRestricted.exists_selected_coeff_factor` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/SelectedFactor.lean, line 68](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/SelectedFactor.lean#L68) |  |
| `MonomialOrder.restrictedLeadingTermIdeal` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LeadingTerm.lean, line 346](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LeadingTerm.lean#L346) |  |
| `MvPowerSeries.exists_common_monic_parameter` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/MonicParameter.lean, line 80](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/MonicParameter.lean#L80) |  |
| `MonomialOrder.restrictedDivisionRemainder` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/PolynomialDivision.lean, line 30](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/PolynomialDivision.lean#L30) |  |
| `MvPowerSeries.restrictedGeometricInverse` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/RestrictedGeometricInverse.lean, line 176](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/RestrictedGeometricInverse.lean#L176) |  |
| `MonomialOrder.restrictedPerturbedDivisionRemainder` | def | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/PerturbedDivision.lean, line 79](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/PerturbedDivision.lean#L79) |  |
| `MonomialOrder.exists_restricted_monic_division` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/MonicDivision.lean, line 30](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/MonicDivision.lean#L30) |  |
| `MvPowerSeries.isAdicallyRestricted_iff_of_cofinal` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Cofinal.lean, line 26](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/Cofinal.lean#L26) |  |
| `isHausdorff_iff_of_cofinal` | theorem | [FormalPowerSeries/AdicCompletion/Cofinal.lean, line 38](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/AdicCompletion/Cofinal.lean#L38) |  |
| `isPrecomplete_iff_of_cofinal` | theorem | [FormalPowerSeries/AdicCompletion/Cofinal.lean, line 51](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/AdicCompletion/Cofinal.lean#L51) |  |
| `isAdicComplete_iff_of_cofinal` | theorem | [FormalPowerSeries/AdicCompletion/Cofinal.lean, line 80](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/AdicCompletion/Cofinal.lean#L80) |  |
| `MonomialOrder.exists_restricted_primitive_division` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/ValuationNormalizedDivision.lean, line 35](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/ValuationNormalizedDivision.lean#L35) |  |
| `MonomialOrder.ideal_eq_span_of_primitive_standardBasis` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/PrimitiveStandardBasis.lean, line 93](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/PrimitiveStandardBasis.lean#L93) |  |
| `MonomialOrder.restrictedLeadingExponent_mul_of_ne_zero` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LeadingTerm/Product.lean, line 34](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/LeadingTerm/Product.lean#L34) |  |
| `MonomialOrder.restricted_singleton_division_unique` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/SingletonDivision.lean, line 35](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/SingletonDivision.lean#L35) |  |
| `MonomialOrder.existsUnique_restricted_primitive_singleton_division` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/SingletonDivision.lean, line 86](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/SingletonDivision.lean#L86) |  |
| `MvPowerSeries.restrictedLeadingExponent_lex_eq_cons_of_scalar_top` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableDivision.lean, line 31](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableDivision.lean#L31) |  |
| `MvPowerSeries.existsUnique_firstVariable_division_of_leadingExponent` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableDivision.lean, line 50](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableDivision.lean#L50) |  |
| `MvPowerSeries.existsUnique_firstVariable_division_of_scalar_top` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableDivision.lean, line 114](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableDivision.lean#L114) |  |
| `MvPowerSeries.exists_firstVariable_monomial_division_of_scalar_top` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableDivision.lean, line 136](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableDivision.lean#L136) |  |
| `MvPowerSeries.isUnit_of_isUnit_restrictedResidueHom` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/UnitDetection/Residue.lean, line 39](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/UnitDetection/Residue.lean#L39) |  |
| `MvPowerSeries.isUnit_of_isUnit_restrictedResidue` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/UnitDetection/Residue.lean, line 72](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/UnitDetection/Residue.lean#L72) |  |
| `MvPowerSeries.finSuccEquiv_restrictedResidueHom_polynomialRestrictedFinFirst` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableUnit.lean, line 38](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableUnit.lean#L38) |  |
| `MvPowerSeries.restrictedResidueHom_quotient_of_restrictedFinFirst_division` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableUnit.lean, line 117](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableUnit.lean#L117) |  |
| `MvPowerSeries.isUnit_quotient_of_restrictedFinFirst_divisionHom` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableUnit.lean, line 181](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableUnit.lean#L181) |  |
| `MvPowerSeries.restrictedResidue_quotient_of_restrictedFinFirst_division` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableUnit.lean, line 210](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableUnit.lean#L210) |  |
| `MvPowerSeries.isUnit_quotient_of_restrictedFinFirst_division` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableUnit.lean, line 234](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariableUnit.lean#L234) |  |
| `MvPowerSeries.existsUnique_firstVariable_preparation_of_scalar_top_of_primitive` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariablePreparation.lean, line 32](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariablePreparation.lean#L32) |  |
| `MvPowerSeries.existsUnique_firstVariable_preparation_of_scalar_top` | theorem | [FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariablePreparation.lean, line 102](https://github.com/FormalFrontier/formal-power-series/blob/29bdab8c1f57472100a579c97a589effaea11987/FormalPowerSeries/MvPowerSeries/IdealAdicRestricted/FirstVariablePreparation.lean#L102) |  |
