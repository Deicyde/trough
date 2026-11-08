# Adic modules

> Lean theory of ideal-power torsion and adic module and ring completions, with quotient, tensor, finiteness and flatness interfaces. Also covers Henselian pairs and polynomial lifting, valuation-ring completions and localization, submodule closure and p-adic density, comaximal ideal powers and finite Chinese remainders.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/formalization.yaml) of [FormalFrontier/adic-modules](https://github.com/FormalFrontier/adic-modules) at commit [86f9b35e](https://github.com/FormalFrontier/adic-modules/tree/86f9b35ef35af4b77c0f31b148cc8e9685d831db), Apache-2.0.*

1 article: 1 for highlights of its formalization.yaml whose declarations the scan finds. The headline results in its README are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/adic-modules](https://github.com/FormalFrontier/adic-modules), read at commit [86f9b35e](https://github.com/FormalFrontier/adic-modules/tree/86f9b35ef35af4b77c0f31b148cc8e9685d831db) (2026-11-05).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “agent-reviewed”.
- Review notes: “The Lean code has undergone independent review by Formal Frontier AI agents, not human peer review or source-author endorsement. This describes code review, not completeness of correspondence with the mathematical sources.”
- Automation: agent; tool setup “Formal Frontier AI agents using Lean, Lake, Git and Hive for original development, independent agent review, assembly and maintenance.”
- Automation notes: “Original project expression and earlier source-repository adaptations are credited in docs/CREDITS.md. Unverified model identities and costs are omitted.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Adic modules and completions of valuation rings* (folklore; independently-proves).
- [Foundations of Rigid Geometry I](https://arxiv.org/abs/1308.4734v5), Kazuhiro Fujiwara, Fumiharu Kato (book; background).
- *Local Fields and Their Extensions*, Ivan B. Fesenko, Sergei V. Vostokov (book; background).
- [The Stacks Project](https://stacks.math.columbia.edu), The Stacks Project Authors (reference work; background).
- *Commutative Ring Theory*, Hideyuki Matsumura, Theorem 2.1 (Cayley-Hamilton) (book; background).
- *Onto endomorphisms are isomorphisms*, M. Orzech, American Mathematical Monthly 78 (1971), 357-362 (article; background).

## Builds on

- [Coherent modules](../coherent-modules/README.md) (a Lake dependency, pinned at 0bcb335a)
- [Graded rings](../graded-rings/README.md) (a Lake dependency, pinned at 4e0ced75)
- [Group theory](../../group-theory/group-theory/README.md) (a Lake dependency, pinned at 83b7c2f5)
- [Multivariate polynomials](../multivariate-polynomials/README.md) (a Lake dependency, pinned at 5d58abb9)

## Used by

- [Formal power series](../formal-power-series/README.md)
- [General linear groups](../../group-theory/general-linear-groups/README.md)
- [Integral closure](../integral-closure/README.md)
- [Projective modules](../../ring-theory/projective-modules/README.md)
- [Valuation integers](../../number-theory/valuation-integers/README.md)

## Highlights

- [Middle exactness of completion for a Noetherian middle module](middle-exactness-of-completion-for-a-noetherian.md)

## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/README.md#headline-results) of [FormalFrontier/adic-modules](https://github.com/FormalFrontier/adic-modules) at commit [86f9b35e](https://github.com/FormalFrontier/adic-modules/tree/86f9b35ef35af4b77c0f31b148cc8e9685d831db), Apache-2.0.*

Unless stated otherwise, rings are commutative and modules are additive
commutative groups. Write `C = AdicCompletion I R`, `H = AdicCompletion I M`
and `P = C ⊗[R] M`, with its first-factor `C`-action. These results use
Mathlib's raw inverse-limit completion, not a new construction of completion.
The linked [catalogue](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/docs/HeadlineResults.md) contains the full statements,
further result families, examples and boundary cases.

**Finite cotangents of ideal powers.** For any ideal `I`, finite generation of
`I / I²` over `R / I` implies finite generation of `Iⁿ / I²ⁿ` over `R / Iⁿ`
for every `n ≥ 0`, with the canonical quotient-ring action. No finite generation
of `I` or Noetherianity of `R` is required.
See [cotangent modules](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/Ideal/Cotangent.lean).

**Finite modules over complete APf bases.** Suppose `I` has finite-submodule
adic cofinality: the intrinsic filtration on each finitely generated submodule
of each finite module is cofinal with the induced filtration. If original `R`
is intrinsically `I`-adically complete, every finite original `R`-module `M`
is intrinsically complete, and its canonical `M → AdicCompletion I M` is
bijective. More generally, such finite `M` is `I`-Hausdorff whenever
`I ≤ jac(ann_R M)`. No finite generation of `I`, original finite presentation,
Noetherianity, flatness or prior module separation is required; ring and module
universes are independent. See the
[complete-base criteria](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/CompleteBase.lean).

**Intrinsic completeness of arbitrary submodules over complete AP bases.** Full
submodule adic cofinality asks for the same intrinsic/induced filtration comparison
for every submodule of each finite module, without finite generation of the
submodule. Over an intrinsically `I`-adically complete original ring `R`, every
original `R`-submodule `N` of a finite `R`-module is intrinsically `I`-adically
complete. No finite generation of `N` or `I`, Noetherianity, finite presentation,
flatness or additional Jacobson-radical assumption is required. The conclusion
concerns the intrinsic ideal-power topology on `N`, separately from ambient
closedness. See the
[complete-base criteria](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/CompleteBase.lean).

**Adically closed submodules with finite quotient.** If `I` has finite-submodule
adic cofinality and `M / N` is finite over original `R`, then
`I ≤ jac(ann_R(M / N))` makes `N` closed in the canonical `I`-adic module topology
of `M`. Neither ambient `M` nor `N` needs to be finite. No finite generation
of `I`, Noetherianity, completeness or ambient separation is assumed; ring
and module universes are independent. This is a closedness result, not an
intrinsic-completeness assertion for `N`. See
[module-adic topologies](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/Topology/Algebra/Module/AdicTopology.lean).

**Noetherian raw completion.** For any ideal `I`, `C` is Noetherian iff
`R / I` is Noetherian and `I / I²` is finitely generated over `R / I`;
equivalently, iff `R / I^n` is Noetherian for any chosen `n ≥ 2`.
Neither `I.FG` nor Noetherianity of `R` is required.
See [cotangent criteria](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/Cotangent.lean).

**Completion of a Noetherian original module.** For any ideal `I`, a
Noetherian original `R`-module `M` has raw completion `H` Noetherian over `C`
with its canonical action. No Noetherianity of `R` or `R / I`, ideal finiteness,
flatness, faithfulness, separation or completeness is assumed; the converse
fails. See [Noetherian modules](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/Noetherian.lean).

**Faithful completed scalar action.** For any ideal `I`, if original `M` is
Noetherian over `R` and the original `R`-action is faithful, the canonical
`C`-action on `H` is faithful by an automatic `FaithfulSMul` instance. Ring
and module universes are independent; no ideal finiteness, separation or
completeness is assumed. See [faithful actions](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/Annihilator.lean).

**Annihilator of a completed Noetherian original module.** For any ideal `I`
and Noetherian original `R`-module `M`, put `K = ann_R M` and let `q : R → R/K`
be the quotient map. Then `ann_C H` is the kernel of the canonical map
`C → AdicCompletion (I.map q) (R/K)`. No Noetherianity of `R` or `C`, ideal
finiteness, flatness, faithfulness, separation or completeness is assumed.
The effective coefficient ring `C / ann_C H` is canonically isomorphic as an
original-`R` algebra to `AdicCompletion (I.map q) (R/K)`. On every completed
coefficient, the equivalence and its inverse commute with the quotient map.
The annihilator need not be the ideal generated by `K` in `C`. See
[annihilators](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/Annihilator.lean).

**Jacobson criteria under finite-submodule adic cofinality.** If
`I.HasFiniteSubmoduleAdicCofinality`, then `I ≤ jac(0)` iff every finite
original `R`-module is intrinsically `I`-Hausdorff; equivalently every
submodule of every such module is closed in its canonical ambient power
topology. The universal conditions quantify over modules in the ring's
universe; finite-module representatives transport uses to independent
universes with the original action. No ideal finiteness, Noetherianity or
nontriviality is assumed. See
[separation criteria](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/Topology/Algebra/Module/SeparationCriteria.lean).

**Pointwise-cofinal submodule inclusions.** For a submodule `K` of an original
`R`-module `N`, suppose that for each `n` some `m` satisfies
`K ⊓ I^m N ≤ I^n K`, with both sides viewed inside `N`. Then completion of
`K.subtype` is injective and `C`-linear. The source uses the intrinsic `I`-adic
filtration on `K`. No finiteness or Noetherianity of the ring, ideal or modules,
flatness, separation or completeness is assumed; ring and module universes
are independent. See the
[cofinality criterion](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/LinearMap.lean).

**Intrinsic precompleteness of closed cofinal submodules.** If the original
`R`-module `M` is `I`-precomplete, `M / N` is `I`-Hausdorff, and the induced
filtration on `N` is pointwise cofinal with its intrinsic one, then `N` is
intrinsically `I`-precomplete. Ambient separation or completeness is not
needed, and there is no finiteness or Noetherianity assumption on the ring,
ideal or modules. The scalar action remains the original `R`-action. For a
complete ambient module, existing separation inheritance gives completeness
of `N`. See [submodules](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/Submodule.lean).

**Injections into Noetherian original targets.** For every ideal `I`, an
injective original linear map `f : M →ₗ[R] N` induces an injective canonical
map on raw completions if `N` is Noetherian over original `R`. The ring,
source and target universes are independent. No Noetherianity of `R`, finite
generation of `I`, source finiteness, flatness, separation or completeness is
assumed. Module Artin–Rees supplies the pointwise-cofinality bound for the
original range, giving this application of the subtype criterion. See
[completion injectivity](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/Exactness.lean).

**Completion of original images.** For every ideal `I` and original linear
map `f : M →ₗ[R] N`, completion of the original range inclusion has the same
`C`-submodule range as the completed map, without Noetherian hypotheses.
If `K = f.range` satisfies the pointwise-cofinality bound above,
`AdicCompletion I (LinearMap.range f) ≃ₗ[C] LinearMap.range (AdicCompletion.map I f)`
via that completed inclusion. The original range uses its intrinsic `I`-adic
filtration; `M` is arbitrary and `f` need not be injective or surjective.
No finiteness or Noetherianity of the ring, ideal or modules, flatness,
separation or completeness is assumed; all three universes are independent.
For Noetherian original `N`, the original Noetherian-target equivalence agrees
with this comparison for every proof of the bound. See the
[range comparison](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/LinearMap.lean) and
[Noetherian-target application](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/Exactness.lean).

**Middle exactness with a Noetherian original middle module.** For any ideal
`I`, an original exact pair `M →ₗ[R] N →ₗ[R] P` remains middle exact under the
canonical completed maps if `N` is Noetherian over original `R` and the original
last map is surjective. The first source is arbitrary and the first map need
not be injective. No ring Noetherianity, ideal finiteness, flatness, faithfulness,
separation or completeness is assumed; all four universes are independent.
See [completion exactness](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/Exactness.lean).

**Middle exactness from two pointwise range bounds.** For any ideal `I`, an
original exact pair `M →ₗ[R] N →ₗ[R] P` remains middle exact under the canonical
completed maps if, separately for each original range `K` in its ambient module
`X`, every `n` admits some `m` with `K ⊓ I^m X ≤ I^n K`. The two bounds may
have different witnesses. Neither map needs to be injective or surjective.
No finiteness or Noetherianity of the ring, ideal or modules, flatness, separation
or completeness is assumed; all four universes are independent. See
[completion exactness](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/Exactness.lean).

**Middle exactness for Noetherian original pairs.** For any ideal `I`, an
original exact pair `M →ₗ[R] N →ₗ[R] P` remains middle exact under the canonical
completed maps if both original `N` and `P` are Noetherian over original `R`.
The last map need not be surjective, the first map need not be injective, and
`M` is arbitrary. No ring Noetherianity, ideal finiteness, flatness, faithfulness,
separation or completeness is assumed; all four universes are independent.
See [completion exactness](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/Exactness.lean).

**Completion of original kernels.** For every ideal `I` and original linear
map `g : N →ₗ[R] P` with both original modules Noetherian over original `R`,
`AdicCompletion I (LinearMap.ker g) ≃ₗ[C] LinearMap.ker (AdicCompletion.map I g)`.
The forward map is completion of the original kernel inclusion, using the
intrinsic filtration on that kernel. No surjectivity or injectivity of `g`,
ring Noetherianity, ideal finiteness, flatness, faithfulness, separation or
completeness is assumed; ring and module universes are independent. The
inverse gives unique factorization of maps into the completed-map kernel
and agrees with the split comparison on overlap. See
[kernel comparison](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/Exactness.lean).

**Noetherian original module quotients.** For any ideal and `n ≥ 2`, the
original `M / IⁿM` is Noetherian over `R` iff `M / IM` is Noetherian over `R`
and the image of `IM` in `M / I²M` is finitely generated over original `R`.
Neither `R` nor `R / I` need be Noetherian. See the
[original-quotient criterion](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/LinearAlgebra/Quotient/Noetherian.lean).

**Noetherian completed modules.** For any ideal and original module, `H` is
Noetherian over `C` iff the original `M / I²M` is Noetherian over `R`;
equivalently, iff any chosen `M / IⁿM`, `n ≥ 2`, is Noetherian over `R / Iⁿ`
with its canonical action. No Noetherian coefficient ring, finite generation,
original completeness or separation is required. Noetherianity of the original
associated graded module over the quotient Rees algebra also suffices.
See the [module criterion](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/Noetherian.lean).

**Module completion and stationary evaluation.** If the image of `I M` in
the original `M / I² M` is finitely generated over `R`, then `Iⁿ H = ker(evalₙ)`
for every `n ≥ 0` and `H` is intrinsically `I`-adically complete for its original
`R`-action, without assuming `I.FG`. These kernel and completeness conclusions
also hold if `H` is Noetherian over `C`, without Noetherianity of `C`; see the
[module criterion](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/Noetherian.lean).
More generally, if `Iⁿ H = ker(evalₙ)` for all `n`, restriction along `of I M`
gives an `R`-linear Hom equivalence from maps `H →ₗ[R] N` to maps `M →ₗ[R] N`
for every intrinsically `I`-adically complete target `N`, with inverse canonical
extension; `N` needs no `C`-action. Both source hypotheses above, or finite
generation of a positive power of `I`, supply these kernel identities.
See [linear maps](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/LinearMap.lean).
For any ideal and `n ≥ 0`, evaluation at `n` on `H` is injective iff
`I^(n+1) M = I^n M`. Under this equality, `H ≃ₗ[R] M / I^n M`;
equality of ideal powers gives the corresponding `R`-algebra equivalence for `C`.
See [kernels](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/Kernel.lean),
[completeness](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/Completeness.lean) and
[stationary evaluation](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/Stationary.lean).

**Finite presentation and flatness.** If `H` is flat over `C`, then `H` is
finitely presented iff any chosen positive original quotient `M / IⁿM`
is finitely presented over `R / Iⁿ`; when this holds, `H` is finite projective
and every original quotient is finitely presented. If `R / I` is Noetherian,
flat `H` is finitely presented iff it is finite over `C`, and is then projective,
without Noetherianity of `C`. Separately, if `C` is Noetherian,
`H` is flat iff every positive original quotient is flat over `R / Iⁿ`;
in particular, a flat original `M` has flat raw completion.
See [finite presentation](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/FinitePresentation.lean)
and [raw flatness](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/Flat/Noetherian.lean).

**Tensor, exactness and Hom comparisons.** If the original `M / IM` is
finitely generated over `R`, then `H` is finite over `C` and `P → H` is onto.
Projectivity of **`P` over `C`**, not merely of `H`, gives injectivity for every
ideal; together these premises give an equivalence. Short exact sequences
with flat original last module remain short exact after completion.
The completed Hom identifies with the `C`-linear Hom between completions
when the original source is finite projective, or is projective and `I.FG`;
the target is arbitrary. See [tensor](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/TensorProduct.lean),
[exactness](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/Flat.lean) and
[Hom](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/Hom.lean).
If every original-`R` power `IⁿH` is `ker(evalₙ)`, every `R`-linear
`H → AdicCompletion I N` respects the canonical `C`-actions, for arbitrary `N`
without intrinsic completeness of `N` or its raw completion. If original `M`
is also finite projective, the map is uniquely represented by a completed original
Hom element after restricting the comparison's scalars to `R`.

**Finite products of coefficient rings.** For a finite family of commutative
rings, put `A = Π i, R i` and let `I` be any ideal of `A`. Completion of `A`
is canonically `A`-algebra equivalent to the product of the completions at the
coordinate-image ideals. For an arbitrary family of original `R i`-modules,
the corresponding module comparison is `A`-linear and intertwines the completed
coefficient actions. Both comparisons commute with original representatives
and every finite reduction, including precision zero. The index, ring and module
universes are independent; empty products and zero rings are included, without
finite-generation, Noetherianity, completeness or separatedness assumptions.
See [coefficient products](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/CoefficientProduct.lean).

**Maps and changes of ideal.** For every ideal and linear `f : M → N`,
completion of `f` is onto iff the original `M → N / IN` is onto.
Mutual containment of powers gives an `R`-linear equivalence of completions,
including at `I^k` and `I` for positive `k`. Completion at the product of a
finite pairwise-comaximal family is `R`-linearly equivalent to the product
of the completions. Arbitrary dependent products commute with completion
if some given positive power of `I` is finitely generated.
See [maps](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/Surjectivity.lean),
[cofinality](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/ChangeIdeal.lean),
[CRT](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/ChineseRemainderAlgebra.lean) and
[products](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/Pi.lean).
A ring map carrying one ideal into another induces a homomorphism between
their completions. For an `R`-algebra, the completed coefficient map gives
the named, non-global `AdicCompletion.extendedAlgebra`; existing coefficient
algebras are unchanged. See [completed ring maps](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/AdicCompletion/RingHom.lean).

**Henselian lifting.** Over a Henselian pair `(R,I)`, a finite square
polynomial system with unit Jacobian determinant at a root modulo `I`
has a unique root in that residue class. Every specified `R`-algebra map
from an étale algebra to `R/I` lifts uniquely to an `R`-algebra map to `R`.
See [Hensel lifting](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/MvPolynomial/Hensel.lean) and
[étale points](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/RingTheory/HenselianEtale.lean); determinant-
and resultant-square refinements and Henselian-pair criteria are in the
[expanded catalogue](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/docs/HeadlineResults.md).

**Action nilpotence and ideal powers.** For a finitely generated ideal
of a commutative semiring acting on an additive commutative monoid module,
some ideal power annihilates the whole module iff `I ≤ radical(ann M)`;
the module need not be finitely generated. Over a Bézout commutative semiring,
`x ∈ I^n` iff some `t ∈ I` satisfies `t^n ∣ x`, including `n = 0`.
See [torsion](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/BoundedIdealPowerTorsion.lean) and
[powers](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/RingTheory/Ideal/PowerCompression.lean).

**Maximal ideals in the adic topology.** For any ideal `I` of a commutative
ring, a maximal ideal `m` is closed in the `I`-adic topology iff `I ≤ m`.
Thus every maximal ideal is closed iff `I` lies in the Jacobson radical.
No APf, finiteness, Noetherianity, completeness or separation is assumed;
the global criterion includes the zero ring. See
[ideal topologies](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/Topology/Algebra/Ideal.lean).

**Compactness and valuation completeness.** For a given compatible additive
uniformity with `IsAdic I`, a ring is compact iff it is uniformly complete and all
`R/I^n` are finite; under `I.FG`, finiteness of `R/I` suffices.
For valuation integers, a nonzero generator with separated principal powers
identifies adic completeness with completeness for the given valuation
uniformity. See [compactness](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/Topology/Algebra/AdicCompactness.lean)
and [valuation completeness](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/Valuation/Completeness.lean).

**Teichmüller and Witt structure.** For prime `p`, a surjection from a
kernel-adically complete ring to a perfect characteristic-`p` ring has a
unique multiplicative zero-and-one section, whose image is the intersection
of the `p^n`-power ranges. The reduced-residue perfection extension is
described in [results and models](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/docs/Results.md#reduced-residue-teichmüller-image).
Witt vectors form a domain iff the coefficient ring is a domain of
characteristic `p`, and a DVR iff it is a perfect field of characteristic `p`.
See [Teichmüller maps](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/RingTheory/Teichmuller.lean),
[domains](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/RingTheory/WittVector/Domain.lean) and
[DVRs](https://github.com/FormalFrontier/adic-modules/blob/86f9b35ef35af4b77c0f31b148cc8e9685d831db/AdicModules/RingTheory/WittVector/DiscreteValuationRing.lean).
