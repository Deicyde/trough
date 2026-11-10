---
navigation: transparent
---

# Exactness of dependent… to Irreducible closed rectangles…

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

### Uniform finite generators of dependent reduced products

The [finite-generation module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Finite.lean)
proves two finite-generation criteria.
For the same given semiring, additive and module records, an arbitrary filter `F`,
a naturally finite index type `J` and raw vectors `g : J → (∀ i, M i)`,
`Filter.Product.span_range_coe_eq_top_iff` gives

```text
Submodule.span (F.Product R) (Set.range (fun j => (g j : F.Product M))) = ⊤
  ↔ ∀ᶠ i in F, Submodule.span (R i) (Set.range (fun j => g j i)) = ⊤.
```

The target records are exactly `Product.instSemiring`, `Product.addCommMonoid`
and `Product.module` of the given fibres, even when `R = M`.
`Filter.Product.moduleFinite_iff` gives

```text
Module.Finite (F.Product R) (F.Product M)
  ↔ ∃ n : ℕ, ∀ᶠ i in F, ∃ v : Fin n → M i,
      Submodule.span (R i) (Set.range v) = ⊤.
```

One uniform `n` is essential; eventual pointwise finite generation alone does
not give this condition. No basis or freeness is assumed. All four carrier
universes are independent. Empty `J`, `n = 0`, empty index types, bottom filters
and zero semirings are included, with no properness or nontriviality hypothesis.
These criteria add no new functional data or global instances.

### Uniform finite presentations of dependent reduced products

The [finite-presentation module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/FinitePresentation.lean)
proves the uniform generators-and-relations criterion. For arbitrary `F`,
independently universed ring families `R i`, and given additive
commutative monoids `M i` with their given `R i`-module actions,
`Filter.Product.moduleFinitePresentation_iff` gives

```text
Module.FinitePresentation (F.Product R) (F.Product M)
  ↔ ∃ n m : ℕ, ∀ᶠ i in F,
      ∃ f : (Fin n → R i) →ₗ[R i] M i,
      ∃ g : (Fin m → R i) →ₗ[R i] (Fin n → R i),
        Function.Surjective f ∧ Function.Exact g f.
```

The left side uses exactly `Product.instSemiring` of the ring semiring parents,
`Product.addCommMonoid` of the given vector records, and `Product.module` of the
given actions. Each `f` retains the given target addition and action, even when
`R = M`; only coefficient function spaces use standard self-actions. Exactness
uses the given vector zero. The pair `(n,m)` precedes the eventual quantifier;
eventual individual finite presentation or a generator bound alone is weaker.
Padding generators may require additional relations, so exact fixed sizes must
not be confused with independently padding both sizes at unchanged bounds.

The rings may be noncommutative, and coefficients act on the left. No properness,
nontriviality, freeness, coherence or Noetherian assumption is imposed. Bottom
filters, empty index types, zero rings/modules and zero free sizes are included.
Represented coordinate negation gives additive inverses for the named scalar
semiring; the given module actions give vector inverses without a new group
hypothesis. This is the genuine ring-module presentation scope. Over general
semirings Mathlib's stock class concerns a finitely generated zero kernel, not a
presentation by a finitely generated congruence; no such semiring claim is made.

- [Exactness of dependent reduced-product maps](exactness-of-dependent-reduced-product-maps.md)
- [Coordinate maps and zero-reflection of dependent filter products](coordinate-maps-and-zero-reflection-of-dependent.md)
- [Reindexing dependent filter products](reindexing-dependent-filter-products.md)
- [Small products of dependent filter products](small-products-of-dependent-filter-products.md)
- [Centers of dependent filter products](centers-of-dependent-filter-products.md)
- [Reduced filter germs](reduced-filter-germs.md)
- [Nontrivial dependent reduced products](../../nontrivial-dependent-reduced-products.md)

### Reduced ranges of iterated Frobenius

For a commutative semiring of exponential characteristic `p`, the original image
of the `n`th Frobenius iterate is reduced exactly when every nilpotent element
has zero `p ^ n`th power. If the semiring is Noetherian and `p` is prime,
all sufficiently high iterates have reduced images. The
[reduced-image API](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Frobenius/Reduced.lean) also gives the
corresponding original subring-range statement for a given commutative ring.
No field, perfectness, or reducedness of the ambient semiring is assumed.

- [No zero divisors in ultrafilter products](no-zero-divisors-in-ultrafilter-products.md)

### Reduced dependent filter products

For an arbitrary filter and an independently universed dependent family of
monoids with zero, the filter product is reduced exactly when its reduced
fibres form a member of the filter. The
[criterion](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Reduced.lean) uses a uniform
square-zero test, not an exchange of a varying nilpotence exponent with
eventual equality. A representative is nilpotent exactly when one uniform
natural-number exponent makes its power zero eventually; the exponent may be
zero. No addition, commutativity, proper-filter or nontriviality hypothesis is
needed.

If the filter contains a finite set, nilpotence of a represented section is
also equivalent to eventual fibrewise nilpotence, by
[`Filter.Product.isNilpotent_coe_iff_of_finite_mem`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Reduced.lean).
The whole index type need not be finite. The same module gives finite-index
and finite-principal criteria; the latter tests exactly the values on the
generating set, including the empty set. These results reuse the
[finite-member exponent bound](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Nilpotent.lean).
For **monoid-with-zero coefficients**, the
[constant-germ specialization](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Germ/Reduced.lean)
uses the existing germ zero and power operations; the earlier germ results
still need only zero and natural-number powers. The
[dependent client](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimesTest/Order/Filter/Product/Nilpotent.lean) gives
a nonzero nilpotent quotient element on an infinite index type with varying
nonadditive fibres.

### Regular elements of dependent filter products

For an arbitrary filter `D` and an independently universed family `K` with only
fibrewise multiplication, a total section represents a left-regular, right-regular,
or regular element of `D.Product K` exactly when its values have that property
eventually. The [criteria](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Regular.lean) require
neither associativity, an identity, nor a proper filter. The existing
[Germ criteria](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Germ/Regular.lean) are their constant-family
specializations. The [varying finite example](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimesTest/Order/Filter/Product/Regular.lean)
separates left and right regularity in noncommutative magmas with no identity.

- [Integral pullback of maximal spectra](integral-pullback-of-maximal-spectra.md)

### Other headline results

The following interfaces are implemented in this library. See the [reader guide](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/docs/Guide.md)
and the linked module documentation for statements, examples, proof ideas and Mathlib dependencies.

**All ideals of products and standard filters**
([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Ideal/PiFilter.lean)). For a dependent family
`K : ι → Type v` of division semirings, `Ideal.piOrderIsoFilter K` identifies
`Ideal (Π i, K i)` with the order dual of `Filter ι`; in particular it applies
to semifields. Its characteristic law is
`{i | f i = 0} ∈ I.piFilter K ↔ f ∈ I`. Both constructors already work for
semirings, but division is used to recover every ideal. The improper filter
gives the whole ideal, a principal filter gives functions vanishing on its
generating set, and the cofinite filter gives finite support. The API includes
germ kernels, singly generated ideals, and compatibility with Mathlib's finite
coordinate-ideal classification. Index and factor universes are independent;
empty products are included without a nontrivial-product assumption.
For arbitrary semiring fibres, coordinate ideals `I i` and a filter `D`,
`Filter.pi_sup_piIdeal_eq_top_iff` says that `Ideal.pi I ⊔ D.piIdeal R` is
the whole ideal exactly when `{i | I i = ⊤} ∈ D`. The properness criterion
`Filter.pi_sup_piIdeal_ne_top_iff` is nonmembership of this set, not membership
of its complement unless `D` is an ultrafilter. Zero fibres and improper
filters are allowed.
([examples](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimesTest/RingTheory/Ideal/PiFilter.lean)).

**Ultrafilter coordinate-locus criteria**
([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Ideal/PrimePiUltrafilter.lean)). For dependent
semirings `R i` and left ideals `I i`, `Ultrafilter.isPrime_pi_sup_piIdeal_iff`
and `Ultrafilter.isMaximal_pi_sup_piIdeal_iff` characterize the sum
`Ideal.pi I ⊔ (U : Filter ι).piIdeal R` as prime or maximal exactly when the
respective coordinate locus belongs to `U`. The criteria need no commutativity,
nontrivial-factor or subtractivity assumption.

**Prime ideals of arbitrary products of semifields**
([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Ideal/PrimePiUltrafilter.lean)). For any dependent
family `K : ι → Type v` of semifields, `PrimeSpectrum.piEquivUltrafilter K`
identifies every prime ideal of `Π i, K i` with an ultrafilter on `ι`.
A function belongs to the ideal for `U` exactly when `{i | f i = 0} ∈ U`.
Already for **division-semiring** fibres, `Ultrafilter.piIdeal_isMaximal` makes
every such ultrafilter zero-set ideal maximal, via the ideal/filter order isomorphism.
The index universe is independent of `v`, and no additive cancellation, ring,
finite-index or nonempty-index hypothesis is imposed. The forward ideal construction
works already for semiring factors, with evaluation-kernel and constant-family
germ-kernel bridges. Finite products have uniquely labelled coordinate kernels;
the cofinite ultrafilter gives non-coordinate primes on infinite index types.
The [topological extension](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Spectrum/Prime/PiUltrafilter.lean)
`PrimeSpectrum.piHomeomorphUltrafilter K` retains this exact equivalence as a
homeomorphism for the Zariski and existing Stone topologies. Its basis pullback
laws use the nonzero locus and the function one on a subset and zero off it.
Coordinate primes are dense, even when non-coordinate primes occur; the topology
is not in general discrete. For an arbitrary index map `g : κ → ι` and fibrewise
semifield homomorphisms `φ j : K (g j) →+* L j`, spectral pullback along the stock
product homomorphism corresponds to `Ultrafilter.map g`. The API includes the
inverse square, index precomposition and same-index family-map specializations;
the index and fibre universes are independent, with no injectivity or finiteness assumption.

**Residue fields of dependent products of fields**
([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Ideal/ResidueFieldPiUltrafilter.lean)). For a
dependent family `K : ι → Type v` of fields and `U : Ultrafilter ι`,
`Ultrafilter.residueFieldProductEquiv K U` canonically identifies
`(U.piIdeal K).ResidueField` with the existing `(U : Filter ι).Product K`.
This is a ring equivalence over the section ring `R = Π i, K i`: for **every
section** `r`, it sends `algebraMap R (U.piIdeal K).ResidueField r` to the
reduced-product class of `r`. The API includes the inverse equation, uniqueness
from this property and its equality-of-homomorphisms form. Fibrewise field
homomorphisms give a commuting square with `Ideal.ResidueField.map` and
`Filter.Product.mapRingHom`. Index and fibre universes are independent; no
common characteristic, finite-index or nonempty-index hypothesis, or global
field instance on the Product, is required. The
[examples](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimesTest/ResidueFieldPiUltrafilter.lean) check the principal
coordinate kernel and a dependent `ZMod 2`/`ZMod 3` family with distinct residue
characteristics and opposite-characteristic nonzero controls.

**Minimal primes of finite products**
([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Ideal/MinimalPrimePi.lean)). For commutative
semirings `R i` and a finite index type, `Ideal.mem_minimalPrimes_pi_iff`
identifies minimal primes over any ideal of the product with unique labelled coordinate
minimal primes. `Ideal.minimalPrimesPiEquiv` gives the corresponding equivalence
with the dependent sum of the minimal primes over `Ideal.piOrderIso I i`.
Its inverse is evaluation comap, with forward/comap and evaluation-image laws.
The transport theorem `Ideal.comap_eval_mem_minimalPrimes_iff` works even for
infinite index types; it does not classify all primes of an infinite product.
No nonempty-index, nontrivial-factor, proper-base-ideal or ring assumptions
are needed. Equal factors retain distinct coordinate labels.

**Minimal primes and radical membership detected by localization**
([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Ideal/MinimalPrimeLocalization.lean)).
In a commutative semiring `R`, an element belongs to `I.radical` exactly when its
canonical image belongs to the radical of the extension of `I` in
`Localization.AtPrime q` for every minimal prime `q` over `I`
(`Ideal.mem_radical_iff_forall_minimalPrimes_localization`). The unit ideal is included.
The [natural-number client](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimesTest/RingTheory/Ideal/MinimalPrimeLocalization.lean)
shows that `2` passes these tests for `(4)` despite not belonging to `(4)`, while `1` fails.
For commutative semirings `R`, `A` with `[Algebra R A]`, a prime ideal `q`
and `[IsLocalization.AtPrime A q]`, any ideal `I` also satisfies
`(I.map (algebraMap R A)).radical = q.map (algebraMap R A)` iff `q ∈ I.minimalPrimes`.
No separate `I ≤ q` is needed. Mathlib supplies the implication from minimality.

**Multipliers outside a minimal prime** ([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Ideal/MinimalPrimeMultipliers.lean)).
For ideals `I`, `q` in a commutative semiring, `q ∈ I.minimalPrimes` and `x ∈ q`
imply `∃ s ∉ q, s * x ∈ I.radical`. Over the zero ideal, the product is nilpotent.

**Ideal contraction and positive powers in the image**
([ideals](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Ideal/PositivePowerRange.lean),
[prime spectra](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Spectrum/Prime/PositivePowerRange.lean)).
For a homomorphism from a semiring `R` to a commutative semiring `S`, suppose
every `x : S` has some positive power in `Set.range f`. Then
`I.comap f ≤ J.comap f ↔ I ≤ J` for arbitrary `I` and radical `J`.
For every target ideal `I`,
`Ideal.radical_map_comap_of_pos_pow_mem_range` also gives
`(Ideal.map f (Ideal.comap f I)).radical = I.radical`.
The map may have any type with `FunLike` and `RingHomClass` instances, in an
independent universe. No surjectivity, uniform exponent or radicality of `I`
is assumed. For commutative semirings on both sides and a bundled homomorphism,
`PrimeSpectrum.isEmbedding_comap_of_pos_pow_mem_range` proves that the existing
`PrimeSpectrum.comap f` is a topological embedding, with independent source and
target universes. Its image need not be closed or the whole spectrum.

**Dimension under field extension.** For fields `K` and `L`, a given
`[Algebra K L]`, and a commutative `K`-algebra `A` with
`[Algebra.FiniteType K A]`, the
[field-extension leaf](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/KrullDimension/FieldExtension.lean)
proves `Algebra.ringKrullDim_tensorProduct_of_finiteType`:
`ringKrullDim (A ⊗[K] L) = ringKrullDim A`. All three types may lie in
independent universes. The extension need not be algebraic, and `A` need not
be a domain, reduced or nontrivial. Dimension takes values in `WithBot ℕ∞`;
the zero algebra has dimension `⊥`.

**Dimension under integral maps** ([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/KrullDimension/Integral.lean)).
For integral maps `f : R →+* S` of commutative rings, target Krull dimension is
at most source dimension, with equality if `f` is injective. Without injectivity,
`ringKrullDim S = ringKrullDim (R ⧸ RingHom.ker f)`. A faithful integral algebra
has equal source and target dimensions using its given algebra structure.
Dimensions lie in `WithBot ℕ∞`, including zero rings and infinite dimension.

**Closed-locus dimension bound for ideals containing a non-zero-divisor**
([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/KrullDimension/Basic.lean)). For a commutative
semiring `R`, `PrimeSpectrum.krullDim_zeroLocus_add_one_le_of_exists_mem_nonZeroDivisors`
states that `Order.krullDim (PrimeSpectrum.zeroLocus (J : Set R)) + 1 ≤ ringKrullDim R`
whenever `∃ a ∈ J, a ∈ nonZeroDivisors R`. Addition is in `WithBot ℕ∞`, so empty loci
retain dimension bottom and infinite dimensions are included. The finite-bound API
`PrimeSpectrum.krullDimLE_zeroLocus_of_exists_mem_nonZeroDivisors` also gives dimension
at most `n` under `[Ring.KrullDimLE (n + 1) R]`. The canonical closed locus carries the
inherited spectrum order. No prime element, principal or prime ideal, domain, unique
factorization, ring, Noetherian, properness or nonempty-locus assumption is imposed.
Neither form asserts equality or exact dimension subtraction.
For commutative rings, Mathlib's quotient-spectrum order isomorphism identifies
the same locus with the spectrum of `R ⧸ J`; arbitrary semiring ideal quotients
are not asserted.

**Dimension from irreducible generators of prime ideals**
([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/KrullDimension/Basic.lean)). In any commutative
semiring, if every nonzero nonmaximal prime ideal is generated by an irreducible
element, `Ring.krullDimLE_two_of_forall_exists_irreducible_span_eq` gives
`Ring.KrullDimLE 2 R`. No domain, unique factorization, ring or Noetherian
assumption is required, and irreducible elements need not be prime.

**Height and dimension of pointwise products**
([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean)). In arbitrary preorders,
`Order.height_pi` and `Order.coheight_pi` express the ranks of a section of a
finite dependent product as sums of its coordinate ranks in `ℕ∞`, including
infinite ranks and rank zero for an empty index. For arbitrary dependent products,
`Order.height_pi_eq_iSup_finset` and `Order.coheight_pi_eq_iSup_finset` give the
supremum of finite coordinate-rank sums, with no finite-support hypothesis.
`Order.krullDim_pi_eq_iSup_range_restrict` expresses the dimension of an arbitrary
dependent product as the supremum of its finite restriction-image dimensions,
retaining empty images when the full product is empty.
The binary formulas are
`Order.height_prod` and `Order.coheight_prod`.
`Order.krullDim_prod` and `Order.krullDim_pi` give the dimension of binary
and finite dependent products as the sum of the factor dimensions in `WithBot ℕ∞`.
Empty factors give bottom even alongside infinite dimension; an empty-index
product has dimension zero. No nonemptiness, finite-dimension or antisymmetry
hypothesis is required. These concern canonical pointwise orders, not lexicographic
or topological products.

**All-dimension bounds after deleting boundary points**
([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean)). For any preorder `α : Type u`,
`Order.krullDim_not_isMin_add_one_le` states
`Order.krullDim {x : α // ¬ IsMin x} + 1 ≤ Order.krullDim α`.
The dual `Order.krullDim_not_isMax_add_one_le` gives the same bound for the
nonmaximal locus. The original-interior bound
`Order.krullDim_not_isMin_not_isMax_add_two_le` states
`Order.krullDim {x : α // ¬ IsMin x ∧ ¬ IsMax x} + 2 ≤ Order.krullDim α`.
Both predicates are tested in the **original preorder**, with canonical inherited
subtype orders. Dimensions and addition lie in `WithBot ℕ∞`: `⊥ + k = ⊥` and
`⊤ + k = ⊤` for the finite shifts. There is no antisymmetry, inhabitation,
finite-dimension, finite-carrier or chain-condition assumption. The shifts are
sharp on two- and three-point chains. Empty types and antichains show why these
are not unconditional equalities; infinite dimension precludes a strict-drop
assertion. This generic order API is a Mathlib-upstream candidate.

**Finite dimension bounds after deleting boundary points**
([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean)). For any preorder `α : Type u`
and `n : ℕ`, `Order.krullDimLE_succ_iff_not_isMin` states
`Order.KrullDimLE (n + 1) α ↔ Order.KrullDimLE n {x : α // ¬ IsMin x}`.
The dual theorem `Order.krullDimLE_succ_iff_not_isMax` gives the same equivalence
after deleting maximal points. Their composition,
`Order.krullDimLE_add_two_iff_not_isMin_not_isMax`, states
`Order.KrullDimLE (n + 2) α ↔
Order.KrullDimLE n {x : α // ¬ IsMin x ∧ ¬ IsMax x}`.
Both predicates refer to the **original preorder**, and the subtypes carry its
inherited order. No antisymmetry, inhabitation, bottom, top, finite-carrier or
chain-condition assumption is needed. These are finite-bound equivalences,
not unconditional exact dimension subtraction; empty types and antichains are included.

**Comparison in dimension at most two**
([order](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean),
[prime ideals](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/KrullDimension/Basic.lean)). In a preorder
with `[Order.KrullDimLE 2 α]`, if `x ≤ y`, `¬ IsMin x` and `¬ IsMax y`, then
`y ≤ x`; equality needs antisymmetry. In a commutative semiring with
`[Ring.KrullDimLE 2 R]`, a nonmaximal prime ideal `I` containing a prime element
`a ∈ nonZeroDivisors R` equals `Ideal.span {a}`. No unique factorization, global
no-zero-divisors, ring or Noetherian hypothesis is required.

**Prime ideals in dimension-two unique factorization semirings**
([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/KrullDimension/UniqueFactorizationDomain.lean)).
In a commutative semiring with `[UniqueFactorizationMonoid R]` and
`[Ring.KrullDimLE 2 R]`, every nonzero nonmaximal prime ideal is the span of
an irreducible element. Every prime is therefore zero, irreducible-principal,
or maximal; the alternatives may overlap. No ring, Noetherian, normalization
or global nontriviality hypothesis is required.

**When a prime localization is a field** ([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Localization/AtPrime.lean)).
For commutative semirings `R`, `A` with their given `R`-algebra structure,
any prime `q` and `[IsLocalization.AtPrime A q]` satisfy
`IsField A ↔ q ∈ minimalPrimes R ∧ IsReduced A`.
Reducedness of `R` gives the reduced-base corollary: arbitrary localization
preserves reducedness. For semirings `IsField` includes semifields.

**Principal prime witnesses and contraction** ([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Principal.lean)).
In a commutative semiring, a proper principal ideal avoids at least one of two
relatively prime (`IsRelPrime`) elements.
In a commutative semiring with unique factorization, every nonunit, including
zero, belongs to a principal prime ideal with this disjunctive avoidance.
No normalization or nonzero assumption is needed. Contraction from any semiring
gives a prime two-sided source ideal, not necessarily a principal ideal.

**Minimal primes of a principal ideal** ([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Principal.lean)).
For `[CommSemiring R]`, `[UniqueFactorizationMonoid R]`, the caller's
`[NormalizationMonoid R]` and `f ≠ 0`, the minimal primes over `(f)` are exactly
the principal ideals generated by normalized irreducible factor values.
Their factor equivalence sends `p` to `span {p}`; multiplicities do not add primes.

**Irreducible components of a principal zero locus** ([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/IrreducibleComponents.lean)).
Under those same semiring, factorization, normalization and nonzero hypotheses,
the factor values are equivalent to the **order-dual subtype** of irreducible
components of the subspace `V((f))` in `PrimeSpectrum R`. This is an `Equiv`,
not an order-equivalence or homeomorphism, and does not classify arbitrary ideals.

**Associated primes of a principal quotient** ([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/AssociatedPrincipal.lean)).
For every `f` in a commutative ring with unique factorization,
`associatedPrimes R (R ⧸ Ideal.span {f}) = (Ideal.span {f}).minimalPrimes`,
using base-ring `R` scalars. No normalization, nonzero or Noetherian hypothesis
is needed; the zero ring is included.

**Scalar restriction and quotient points** ([scalar restriction](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/AssociatedRestrictScalars.lean),
[quotients](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/AssociatedPrincipal.lean)). Colon ideals of arbitrary
submodules contract under compatible algebra/module towers with commutative
source and semiring target. Associated primes of a compatible module contract
along algebra maps of commutative semirings and reflect along surjective ones.
For every principal quotient
of a commutative ring with unique factorization, quotient-spectrum associated
points and exact singleton-annihilator criteria correspond by ideal comap to
minimal primes over the generator.

**Height of a principal prime** ([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Ideal/PrincipalPrimeHeight.lean)).
In a commutative ring with `[WfDvdMonoid R]` and `Prime p`, `span {p}` has height
at most one. Its height is one if `p ∈ nonZeroDivisors R`, in particular in a domain.
This uses well-founded strict divisibility, not a Noetherian or UFM assumption,
and concerns prime generators, not arbitrary principal ideals.

**Descending prime chains at finite initial height**
([order](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/FiniteHeightChain.lean), [prime chains](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Ideal/FiniteHeightChain.lean)).
In a preorder, finite ambient height of `x` makes the strict order on `Set.Iic x`
well-founded. An antitone spectrum sequence over a commutative semiring with
finite initial ambient height stabilizes. So does an antitone ideal sequence
over a commutative ring when **every term is prime** and the initial ideal has
`Ideal.FiniteHeight`. One common index gives both tail constancy and the
**all-index** ideal infimum; no global dimension or chain-condition hypothesis
is added. Spectrum height is not height in the full lattice of ideals.

**Zero-dimensional Zariski spectra** ([module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Spectrum/Prime/ZeroDimensional.lean)).
For any commutative semiring, T₁ and Hausdorffness of `PrimeSpectrum R` are each
equivalent to `Ring.KrullDimLE 0 R`, including the empty spectrum; under this
bound all basic opens are clopen. Mathlib supplies total separation and total
disconnectedness from the Hausdorff spectrum. For a **reduced, nontrivial
commutative ring**, this bound and preconnectedness of its spectrum imply `IsField R`.

### Non-zero-divisor loci of germs

For an arbitrary filter `D` and a monoid with zero `M`, the
[non-zero-divisor criteria](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Germ/NonZeroDivisors.lean)
identify intrinsic left, right and two-sided non-zero-divisors of `Filter.Germ D M`
with eventual coordinate membership in the corresponding submonoids of `M`.
The index and coefficient universes are independent; improper filters, empty indices
and trivial monoids are included. These are zero-annihilator criteria, not full
multiplicative cancellation criteria. The generic API is a Mathlib-upstream candidate.

- [Irreducible closed rectangles and topological product dimensions](irreducible-closed-rectangles-and-topological-pr.md)

### Topological dimension under inducing maps and covers

The [inducing-map and open-cover module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Topology/KrullDimension/OpenCover.lean)
proves `Topology.IsInducing.topologicalKrullDim_eq`: an inducing surjection between
independently universed spaces with their given topologies preserves dimension in
`WithBot ℕ∞`. The map need not be injective, and no separation, sobriety, finiteness
or nonemptiness assumption is needed.

The same module proves
`topologicalKrullDim_eq_iSup_of_isOpenEmbedding_cover`: the dimension of a space is
the supremum of the dimensions of any jointly surjective family of open-embedding
charts, with independent universes for the space, index type and chart domains.
Its open-subspace form, `topologicalKrullDim_eq_iSup_of_isOpen_cover`, applies to
any family of open sets whose union is the whole space, with their induced topologies.
Both equalities use `WithBot ℕ∞`, including bottom for an empty-index cover of the
empty space and infinite or unbounded dimensions. No separation, sobriety,
Noetherianity, quasi-compactness, finiteness or nonemptiness assumption is needed.

For `ι : Type u`, `X : Type v`, `Y : ι → Type w`, and `I : Finset ι`,
`topologicalKrullDim_le_iSup_of_isInducing_finset_cover` states

```lean
topologicalKrullDim X ≤
  ⨆ J ∈ I.powerset, ⨆ (_ : J.Nonempty),
    (∑ i ∈ J, topologicalKrullDim (Y i)) + ((J.card - 1 : ℕ) : WithBot ℕ∞)
```

The hypotheses are `∀ i ∈ I, Topology.IsInducing (f i)` and
`∀ x : X, ∃ i ∈ I, ∃ y : Y i, f i y = x` for `f : ∀ i, Y i → X`.
All original topologies are retained, with independent index, ambient and domain
universes. No global finiteness of the index, injectivity, separation, sobriety,
Noetherianity, nonemptiness, finite dimension or attaining chain is assumed.
Empty families give bottom, and mixed empty pieces are handled by the supremum
over subfamilies. Subtraction is in `ℕ` before casting. The two point subspaces of
Sierpiński space show that a maximum bound is false and the additive penalty is sharp.
The order-theoretic finite-cover bound supplies the powerset expression.

The characteristic lemmas
`TopologicalSpace.IrreducibleCloseds.map_le_map_iff_of_isInducing` and
`TopologicalSpace.IrreducibleCloseds.mem_range_map_iff_of_isInducing` concern Mathlib's
existing closure-image map, not a different map. For inducing `f`, it reflects
inclusion, and an ambient irreducible closed `Z` belongs to its range exactly when
`closure ((Z : Set X) ∩ Set.range f) = (Z : Set X)`. These properties apply to
noninjective maps and identify the chart orders used in the finite-cover bound.

### Topological dimension on closed covers, components and point closures

The [closed-cover leaf](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Topology/KrullDimension/ClosedCover.lean) proves
`topologicalKrullDim_eq_iSup_of_isClosedEmbedding_cover`: the dimension is the
supremum of the dimensions of the given domains of a jointly surjective family of
closed embeddings, provided the original indexed family of images is locally finite.
The ambient, index and domain universes are independent. Its closed-subspace form,
`topologicalKrullDim_eq_iSup_of_locallyFinite_isClosed_cover`, uses the ordinary
membership subtypes with their induced topologies. Both equalities are in
`WithBot ℕ∞`, including empty covers and unbounded dimensions, without separation,
sobriety, Noetherianity, quasi-compactness, nonemptiness or attainment assumptions.

The same module proves `topologicalKrullDim_eq_iSup_irreducibleComponents`: for any
given topological space `X`, its dimension equals
`⨆ C : irreducibleComponents X, topologicalKrullDim (C : Set X)`.
The index is the membership subtype of Mathlib's canonical set of components; each
component carries its ordinary induced subspace topology. No local finiteness,
Noetherianity, separation or sobriety assumption is imposed. The empty space has
dimension `⊥`, and the supremum can be unbounded without being attained.

For any `X : Type u` with `[TopologicalSpace X] [QuasiSober X]`, the same module proves
`topologicalKrullDim_eq_iSup_closure_singleton`:
`topologicalKrullDim X = ⨆ x : X, topologicalKrullDim (closure ({x} : Set X))`.
The index is every original point; each closure uses the original topology and its
induced subspace topology. No T0 separation, Noetherianity, nonemptiness or local
finiteness is assumed. The `WithBot ℕ∞` supremum is bottom for the empty space and
includes infinite and unbounded dimensions without requiring attainment.

The same module proves `topologicalKrullDim_eq_iSup_connectedComponents`: for arbitrary
`X : Type u` with its given topology, its dimension equals
`⨆ C : ConnectedComponents X,
  topologicalKrullDim ((ConnectedComponents.mk : X → ConnectedComponents X) ⁻¹' {C})`.
The index is Mathlib's canonical quotient of connected components. Each fibre is a
membership subspace of the original `X`, with its induced topology, not a subspace
of the quotient. Connected components partition the points, unlike irreducible
components, which may intersect. No local finiteness, local connectedness or discrete
quotient is assumed; empty spaces give `⊥`, and unbounded suprema need not be attained.

The supporting containment theorem applies to any irreducible set, not necessarily
closed. The characteristic range theorem for the existing `IrreducibleCloseds.map`
and closed-embedding height invariance use the canonical inclusion orders. Mathlib
supplies canonical components, their closedness and whole-irreducible-set extension.
