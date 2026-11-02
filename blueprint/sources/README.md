# Sources

Trough reads these sources. The catalog of libraries is `catalog/libraries.toml`.

## Mathlib's curated lists

- `data/mathlib/yaml/`: docs/overview.yaml, docs/undergrad.yaml, docs/100.yaml and docs/1000.yaml from [leanprover-community/mathlib4 at 1b1ccf4b](https://github.com/leanprover-community/mathlib4/tree/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs), Apache-2.0.
- `data/mathlib/concept-deps.json`: each listed declaration's kind, docstring, signature and nearest listed dependencies, written by `lean/ConceptDeps.lean` in GitHub Actions.
- `data/thousand-plus.json`: subject classification and Wikipedia pages of the 1000+ theorems, from [1000-plus/1000-plus.github.io](https://github.com/1000-plus/1000-plus.github.io) at 8e04b97d, released into the public domain.

## Libraries

### Core library

- [Mathlib](https://github.com/leanprover-community/mathlib4) at 1b1ccf4b088b: General-purpose Lean 4 mathematics library: algebra, analysis, topology, category theory, number theory, measure/probability, and more.

### AI-written libraries

- [Tau Ceti](https://github.com/TauCetiProject/TauCeti) at 36bbd8632db6: An AI-written library downstream of Mathlib covering all areas. Humans write the roadmaps and review rubrics (TauCetiReview repo).
- [ATLAS](https://github.com/facebookresearch/atlas-lean) at c905cd2490ed: Autoformalized textbook mathematics. v2 root: MathlibExt (reusable Mathlib extensions), CSLibExt, WantedExt (established results with deferred proofs). Archived v1/ (2653 files, own lakefile) and Atlas/ developments (StatisticalMechanics 6971, CPythonListsort, FC) are outside the root build.

### Research projects with blueprints

- [Fermat's Last Theorem (Imperial)](https://github.com/ImperialCollegeLondon/FLT) at a3210204ad88: Ongoing formalization of the Wiles/Taylor-Wiles proof of Fermat's Last Theorem, reduced to 1980s-known results (FLT/KnownIn1980s, Assumptions).
- [PNT+](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd) at 127b50e33f60: Prime Number Theorem and extensions: Wiener-Ikehara, medium/strong error terms, IEANTN (126 files), zero-free regions, explicit estimates.
- [Polynomial Freiman-Ruzsa](https://github.com/teorth/pfr) at 7e7fadf0c4d0: Polynomial Freiman-Ruzsa conjecture (Gowers-Green-Manners-Tao) and related results: entropy and Ruzsa distance, torsion and integer versions, improved exponents.
- [Equational Theories](https://github.com/teorth/equational_theories) at 2ddb16c4c4c0: The implication graph between equational laws of magmas (crowdsourced and automated).
- [Strong PNT (Math Inc)](https://github.com/math-inc/strongpnt) at 2f5835c32231: Strong Prime Number Theorem with classical de la Vallee Poussin error term, produced by Math Inc's Gauss agent.

### Libraries

- [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) at d995ef5d3066: Statements (mostly sorry'd) of open conjectures: ErdosProblems 1000 files, OEIS 250, Wikipedia 184, WrittenOnTheWallII 64, GreensOpenProblems 61, Paper 52, Arxiv 41, MathOverflow, Kourovka, Books.
- [Physlib](https://github.com/leanprover-community/physlib) at 3d3ec913681f: Physics (formerly HepLean/PhysLean): relativity, particles, QFT, quantum mechanics, classical mechanics, electromagnetism, condensed matter, plus quantum information (QuantumInfo lib).
- [CSLib](https://github.com/leanprover/cslib) at 52897fc2059b: Computer science foundations: computability (110), foundations (82), languages and semantics (45), logics, algorithms, crypto, ML.
- [Foundation](https://github.com/FormalizedFormalLogic/Foundation) at c3eb37ae896d: Mathematical logic: first-order arithmetic and incompleteness (FirstOrder 177), provability logic (58), propositional and modal logic, second-order.
- [Analysis I companion](https://github.com/teorth/analysis) at a19a5bfadc61: Lean companion to Tao's Analysis I textbook (section-by-section exercises), plus measure theory.

### Large corpora

- [Fermat's Last Theorem (Anthropic)](https://github.com/anthropics/fermats-last-theorem) at 6e837e753555: A complete machine-checked proof of FLT via Frey-Serre-Ribet-Wiles-Taylor-Wiles, from the three standard axioms; checked by comparator and the nanoda kernel.
- [OpenAI Math](https://github.com/openai/math) at 4eaee8754825: Lean proofs of results from about 721 model-generated research manuscripts (README says ~42% of top-line results are formalized). Includes Hodge for CM abelian varieties, BSD cases, and counterexamples (Hadwiger, Kaplansky).
- [Classification of Finite Simple Groups (Axiom)](https://github.com/AxiomMath/CFSG) at 69cb972f587a: A sorry-free proof of the Classification of Finite Simple Groups, mostly first-generation, using TauCeti's ClassificationStatement; produced by AxiomProver.
- [Lean Pool](https://github.com/LeanPool/lean-pool) at 01db1d7049cf: A pool of 289 permissively licensed Lean projects outside Mathlib's scope (README: about 9.9M lines), e.g. Navier-Stokes, CKN, Davis-Kahan, Conway-Soifer, Zeta5Irrational, MovingSofa.

### Formal Frontier libraries

- [adic-modules](https://github.com/FormalFrontier/adic-modules) at f8b67c787f71: Ideal-power torsion, adic completions, Henselian pairs and Hensel lifting, valuation-ring completions; background: Fujiwara-Kato, Fesenko-Vostokov, Stacks, Matsumura
- [algebraic-direct-limits](https://github.com/FormalFrontier/algebraic-direct-limits) at 70dfb18292c4: Directed/filtered limits of modules and rings, tensor products, Mittag-Leffler inverse systems, spectra and Krull dimension of filtered colimits (Stacks 10.86.3 background)
- [algebraic-groups](https://github.com/FormalFrontier/algebraic-groups) at d9fc50596a5d: Matrix point groups, finite algebraic group schemes, coordinate Hopf algebras, unitriangular groups (background: Milne Algebraic Groups, Hopf algebras)
- [coherent-modules](https://github.com/FormalFrontier/coherent-modules) at 96b2ee42795b: Coherent rings and modules, finite-presentation criteria, localization/descent, Noetherian ascent (folklore; Fujiwara-Kato background)
- [complex-analysis](https://github.com/FormalFrontier/complex-analysis) at ec0323f84c5b: Complex Frechet-differentiable maps on finite-dim spaces are analytic, via polydisc Cauchy formula (folklore)
- [continuous-group-cohomology](https://github.com/FormalFrontier/continuous-group-cohomology) at 61e5e2616b25: Low-degree continuous group cohomology, Tate deflation, compact-group norm-limit sequences; adapts Neukirch-Schmidt-Wingberg Cohomology of Number Fields
- [dedekind-ideal-arithmetic](https://github.com/FormalFrontier/dedekind-ideal-arithmetic) at 3c83ef9dc8a8: Six results on ideal absolute norms, principal primes from norms, class groups of Dedekind localizations (Weibel K-book background)
- [finite-etale-algebras](https://github.com/FormalFrontier/finite-etale-algebras) at edb115c15526: Finite etale subalgebras over fields, Galois/separable/purely inseparable descent (Milne Algebraic Groups background)
- [finite-group-tate-cohomology](https://github.com/FormalFrontier/finite-group-tate-cohomology) at 96ce4463091a: Norms, exceptional Tate degrees, cyclic period-two comparisons for finite-group representations (folklore)
- [formal-power-series](https://github.com/FormalFrontier/formal-power-series) at d8d03bb6d7fd: Logarithmic derivatives of power-series units, restricted (adic) multivariate power series; adapts Weibel K-book
- [fundamental-groupoids](https://github.com/FormalFrontier/fundamental-groupoids) at b28cd19d48b4: Fundamental groupoids, descent along open covers, van Kampen for two-open covers; adapts May's Concise Course
- [general-linear-groups](https://github.com/FormalFrontier/general-linear-groups) at a9b20bb169ee: GL_n over (non)commutative rings: elementary matrices, commutators, Whitehead lemma, Steinberg relations; adapts Weibel K-book, Fesenko-Vostokov
- [graded-rings](https://github.com/FormalFrontier/graded-rings) at 02b76f2240ac: Graded quotients/localizations, homogeneous primes, symmetric algebras; Vakil Rising Sea 7.4.F-H background
- [group-rings](https://github.com/FormalFrontier/group-rings) at 14cc9186ae16: Group algebras of free abelian groups as Laurent polynomial algebras, etc.; adapts Weibel K-book
- [group-theory](https://github.com/FormalFrontier/group-theory) at d8187797d516: Shared topological/algebraic group API (continuous homs, open subgroups, profinite characters); cites May, Neukirch-Schmidt-Wingberg plus many original proofs
- [homological-algebra](https://github.com/FormalFrontier/homological-algebra) at 6c7f755cf87e: Euler invariants, cochain constructions, double-complex totals; adapts Weibel K-book and Cohomology of Number Fields
- [ideal-completion](https://github.com/FormalFrontier/ideal-completion) at 7fb1aca4010f: Ideal completions of bounded distributive lattices as coherent frames (folklore; Fujiwara-Kato background)
- [integral-closure](https://github.com/FormalFrontier/integral-closure) at 8162fe19a81e: Integral-closure and normality descent along retractions and field scalar extensions (original; Rising Sea background)
- [iwasawa-modules](https://github.com/FormalFrontier/iwasawa-modules) at 887cda208486: Pseudo-null/pseudo-isomorphism calculus and completed group algebras (Cohomology of Number Fields background)
- [metrization](https://github.com/FormalFrontier/metrization) at 9ecc20de2856: Nagata-Smirnov metrization theorem and its converse, metrizability from locally finite metrizable covers (adapts Nagata 1950 and Smirnov 1951 papers)
- [minimal-primes](https://github.com/FormalFrontier/minimal-primes) at db21a0ac3837: Minimal primes over principal ideals in UFD semirings, irreducible components (Rising Sea background)
- [morphism-properties](https://github.com/FormalFrontier/morphism-properties) at 031b99e7900b: Category theory: morphism properties under pullback, over-category transport, density under slicing
- [multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at 616945c1c06d: Infinite-variable ideals, evaluation ideals, block substitution, Taylor expansion of MvPolynomial (mostly original; Rising Sea/Fujiwara-Kato background)
- [norm-forms](https://github.com/FormalFrontier/norm-forms) at c3d1a3a7c81c: Field and spectral norms over complete ultrametric fields, norm forms, nontrivial zeros of forms, Chevalley-Warning; formalizes parts of Fesenko-Vostokov; BGR background
- [polynomial-root-stability](https://github.com/FormalFrontier/polynomial-root-stability) at fe1ff972e445: Krasner-type stability of root fields, Newton lifting (Neukirch-Schmidt-Wingberg, Fesenko-Vostokov background)
- [profinite-groups](https://github.com/FormalFrontier/profinite-groups) at 83b3b2eee8ac: Profinite groups: finite-stage limits, Sylow families, closed subgroups (Cohomology of Number Fields background)
- [projective-modules](https://github.com/FormalFrontier/projective-modules) at 51a40ea06a9a: Projective modules, Baer criterion and linear systems, K-theory foundations; adapts Weibel K-book
- [projective-space](https://github.com/FormalFrontier/projective-space) at e9d6d913dd45: Proj of graded rings, standard charts, projective space (original; Rising Sea background)
- [quadratic-algebras](https://github.com/FormalFrontier/quadratic-algebras) at a36cd9d5b5f3: Quadratic algebras, integral closure criteria, class number of Q(sqrt(-5)) (original)
- [restricted-product-duality](https://github.com/FormalFrontier/restricted-product-duality) at 2353cdd535d2: Topology of cofinite restricted products, path components, compactness (Cohomology of Number Fields, May background)
- [ringed-spaces](https://github.com/FormalFrontier/ringed-spaces) at 052015f070ef: Ringed-space restriction and gluing, module presheaf/sheaf scalar extension and inverse image (original; adapts Mathlib)
- [scheme-properties](https://github.com/FormalFrontier/scheme-properties) at 6391288bf75a: Scheme properties, rational maps and function fields, birational geometry; Rising Sea background, adapts Milne Algebraic Groups and Weibel
- [sequence-growth](https://github.com/FormalFrontier/sequence-growth) at c472750a1f13: Growth bounds for natural-division lower recurrences (original)
- [sheaf-cohomology](https://github.com/FormalFrontier/sheaf-cohomology) at 66b27c46e97d: Sheaf cohomology, quasi-flasque acyclicity, derived pushforward, sheafed-space limits (folklore; Fujiwara-Kato background)
- [simplicial-objects](https://github.com/FormalFrontier/simplicial-objects) at e85333e5a0b0: Decalage of simplicial objects, chain transfers and homology maps (folklore; May background)
- [simplicial-rings](https://github.com/FormalFrontier/simplicial-rings) at 034080a40765: Central polynomial simplices and simplicial homotopy (Weibel K-book background)
- [smooth-regularity](https://github.com/FormalFrontier/smooth-regularity) at 760c430ad076: Conormal/Jacobian criteria, smooth implies regular over fields (Stacks background)
- [spectral-stone-duality](https://github.com/FormalFrontier/spectral-stone-duality) at 582201dc239a: Stone duality between bounded distributive lattices and spectral spaces, cofiltered spectral limits (folklore; Fujiwara-Kato)
- [sphere-topology](https://github.com/FormalFrontier/sphere-topology) at 3c24c77cbb55: Singular homology of spheres, Brouwer fixed point for the disk, non-retraction (May, Weibel background)
- [stable-range](https://github.com/FormalFrontier/stable-range) at b3c9bc562219: Bass stable range, cancellation, unimodular rows; adapts Weibel K-book
- [supernatural-numbers](https://github.com/FormalFrontier/supernatural-numbers) at 6b3cd7604fb5: Supernatural numbers, profinite orders and indices; adapts Neukirch-Schmidt-Wingberg
- [toric-ideals](https://github.com/FormalFrontier/toric-ideals) at 8b8e3ff3934c: Toric/binomial ideals, fiber normalization, monoid-algebra kernels; adapts Vakil Rising Sea
- [valuation-integers](https://github.com/FormalFrontier/valuation-integers) at db743a475a4d: Integers of rank-one valuations: power divisibility, Krull dimension bounds; adapts Fesenko-Vostokov
- [vector-bundles](https://github.com/FormalFrontier/vector-bundles) at c0d03404c969: Hermitian/real fiber metrics, orthogonal subbundles, local coordinates; adapts Hatcher's Vector Bundles and K-Theory
