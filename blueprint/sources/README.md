# Sources

Trough reads these sources. The catalog of libraries is `catalog/libraries.toml`.

## Mathlib's curated lists

- `data/mathlib/yaml/`: docs/overview.yaml, docs/undergrad.yaml, docs/100.yaml and docs/1000.yaml from [leanprover-community/mathlib4 at 9bac2d06](https://github.com/leanprover-community/mathlib4/tree/9bac2d0692944a775113f7c130fd5e5b4608a854/docs), Apache-2.0.
- `data/mathlib/concept-deps.json`: each listed declaration's kind, docstring, signature and nearest listed dependencies, written by `lean/ConceptDeps.lean` in GitHub Actions.
- `data/thousand-plus.json`: subject classification and Wikipedia pages of the 1000+ theorems, from [1000-plus/1000-plus.github.io](https://github.com/1000-plus/1000-plus.github.io) at 8e04b97d, released into the public domain.

## Blueprints

- `data/blueprints/flt/`: the TeX of [Fermat's Last Theorem (Imperial)'s blueprint](https://github.com/ImperialCollegeLondon/FLT), pinned in its source.json, Apache-2.0; the license is copied beside it.
- `data/blueprints/pnt-plus/`: the TeX of [PNT+'s blueprint](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd), pinned in its source.json, Apache-2.0; the license is copied beside it.
- `data/blueprints/pfr/`: the TeX of [Polynomial Freiman-Ruzsa's blueprint](https://github.com/teorth/pfr), pinned in its source.json, Apache-2.0; the license is copied beside it.
- `data/blueprints/equational-theories/`: the TeX of [Equational Theories's blueprint](https://github.com/teorth/equational_theories), pinned in its source.json, Apache-2.0; the license is copied beside it.
- `data/blueprints/strongpnt/structure.json`: the titles, labels, Lean names, marks and places of [Strong PNT (Math Inc)'s blueprint](https://github.com/math-inc/strongpnt); it gives no license, so its text is not copied.

## Tau Ceti

- `data/tauceti/roadmaps.json`: each roadmap's title and the declarations its STATUS.md names under its named results and notable definitions, from [TauCetiProject/TauCetiRoadmap at 9f7c032a](https://github.com/TauCetiProject/TauCetiRoadmap/tree/9f7c032adaf1b838e8183d63ff3cfa886d061cb3), Apache-2.0.
- `data/tauceti/deps.json`: each named declaration's kind, docstring, signature and nearest named dependencies in [TauCetiProject/TauCeti at a6027b1d](https://github.com/TauCetiProject/TauCeti/tree/a6027b1d24fcb935c53bd5b50d11b40991cda418), Apache-2.0, written by `lean/tauceti/TauCetiDeps.lean` in GitHub Actions.

## Formal Frontier

- `data/ff/<name>.json`: for each of the 44 Formal Frontier libraries, the facts, highlights and main results of its formalization.yaml and the headline results of its README, read at the commit the file records, with the line and kind of each named declaration its file declares, from [FormalFrontier](https://github.com/FormalFrontier), Apache-2.0. The declarations are read from the source text, without Lean.

## Formal Conjectures

- `data/formal-conjectures/problems.json`: each problem file's title and module docstring, its research and textbook statements with their categories, subjects, proof links, docstrings and Lean statements, and its counts of test and API statements, with the FC100 lists, from [google-deepmind/formal-conjectures at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0. They are read from the source text, without Lean.

## Lean Pool

- `data/lean-pool/projects.json`: the title, summary, authors, sources, license, provenance, MSC2020 codes and main results of each project card in [LeanPool/lean-pool at 2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0, with the note, its copyright line or a remark about it, that its NOTICE.extra.yml keeps for a project published under MIT, and the module, line and kind of each main result's declaration, read from the source text without Lean. `data/lean-pool/source.json` records the commit, its Lean toolchain and Mathlib.

## Fermat's Last Theorem (Anthropic)

- `data/anthropic-flt/source.json` and `landmarks.json`: the facts of the formalization.yaml, the steps of PROOF-PATH.md, and the landmark theorems of [anthropics/fermats-last-theorem at 6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), each with its route stage, aliases and nearest landmarks from html/data/meta.js and html/data/edges.js and its Lean statement from its file under Theorems/, Apache-2.0. Nothing is read with Lean.

## Classification of Finite Simple Groups (Axiom)

- `data/cfsg/proof.json`: the top theorem, the reduction and the theorem its proof gives for each case, each milestone module's declarations, with their Lean statements and lines, the case and milestone files each such file imports, directly or not, through no other, the main results, facts and README opening, and the files and theorems of each folder, from [AxiomMath/CFSG at 69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0. They are read from the source text, without Lean. `data/cfsg/source.json` records the commit, its Lean toolchain, Mathlib and Tau Ceti.

## The Stacks Project in Lean (Axiom)

- `data/stacks/tags/`: each Stacks tag's declarations, with their tiers, attribute comments, docstrings, Lean statements and EGA and SGA references, and the declarations registered for it, from [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7), Apache-2.0. They are read from the source text, without Lean.
- `data/stacks/structure.json`: the parts, chapters and sections of the [Stacks Project](https://github.com/stacks/stacks-project), their numbers and titles, and the section each tag is in, at the commit the file records. The Stacks Project is under the GNU Free Documentation License; none of its text is copied beyond these titles.

## ATLAS (Meta)

- `data/atlas/articles/`: each result of ATLAS's vault, its title, statement and Lean declaration, and where the repository's Lean declares it, read from the source text without Lean; `data/atlas/structure.json`: the vault's areas, subjects and containers, with their titles and prose. From [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d), the `wiki/autoform-blueprint` branch, Apache-2.0. The archived `v1/`, under a non-commercial license, is not read.

## OpenAI Math

- `data/openai-math/families/`: each result family's description, its manuscripts' titles, PDFs and abstracts, and its Lean page, with each formalized result's statements as the statement file writes them and where the repository's Lean proves them, read from the source text without Lean; `data/openai-math/structure.json`: the subjects and their families. From [openai/math at 4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae), Apache-2.0.

## Libraries

### Core library

- [Mathlib](https://github.com/leanprover-community/mathlib4) at 1b1ccf4b088b: General-purpose Lean 4 mathematics library: algebra, analysis, topology, category theory, number theory, measure/probability, and more.

### AI-written libraries

- [Tau Ceti](https://github.com/TauCetiProject/TauCeti) at ace60277c4c5: An AI-written library downstream of Mathlib covering all areas. Humans write the roadmaps and review rubrics (TauCetiReview repo).
- [ATLAS](https://github.com/facebookresearch/atlas-lean) at c905cd2490ed: Autoformalized textbook mathematics. v2 root: MathlibExt (reusable Mathlib extensions), CSLibExt, WantedExt (established results with deferred proofs). Archived v1/ (2653 files, own lakefile) and Atlas/ developments (StatisticalMechanics 6971, CPythonListsort, FC) are outside the root build.

### Research projects with blueprints

- [Fermat's Last Theorem (Imperial)](https://github.com/ImperialCollegeLondon/FLT) at a3210204ad88: Ongoing formalization of the Wiles/Taylor-Wiles proof of Fermat's Last Theorem, reduced to 1980s-known results (FLT/KnownIn1980s, Assumptions).
- [PNT+](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd) at 127b50e33f60: Prime Number Theorem and extensions: Wiener-Ikehara, medium/strong error terms, IEANTN (126 files), zero-free regions, explicit estimates.
- [Polynomial Freiman-Ruzsa](https://github.com/teorth/pfr) at 7e7fadf0c4d0: Polynomial Freiman-Ruzsa conjecture (Gowers-Green-Manners-Tao) and related results: entropy and Ruzsa distance, torsion and integer versions, improved exponents.
- [Equational Theories](https://github.com/teorth/equational_theories) at 2ddb16c4c4c0: The implication graph between equational laws of magmas (crowdsourced and automated).
- [Strong PNT (Math Inc)](https://github.com/math-inc/strongpnt) at 2f5835c32231: Strong Prime Number Theorem with classical de la Vallee Poussin error term, produced by Math Inc's Gauss agent.

### Libraries

- [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) at 2055e5adadae: Statements, mostly without proof, of open and solved problems, a file per problem in a folder per source: the Erdős problems, OEIS, Wikipedia, Green's open problems, Written on the Wall II, papers, arXiv, MathOverflow, books and smaller ones.
- [Physlib](https://github.com/leanprover-community/physlib) at 3d3ec913681f: Physics (formerly HepLean/PhysLean): relativity, particles, QFT, quantum mechanics, classical mechanics, electromagnetism, condensed matter, plus quantum information (QuantumInfo lib).
- [CSLib](https://github.com/leanprover/cslib) at 52897fc2059b: Computer science foundations: computability (110), foundations (82), languages and semantics (45), logics, algorithms, crypto, ML.
- [Foundation](https://github.com/FormalizedFormalLogic/Foundation) at c3eb37ae896d: Mathematical logic: first-order arithmetic and incompleteness (FirstOrder 177), provability logic (58), propositional and modal logic, second-order.
- [Analysis I companion](https://github.com/teorth/analysis) at a19a5bfadc61: Lean companion to Tao's Analysis I textbook (section-by-section exercises), plus measure theory.

### Large corpora

- [Fermat's Last Theorem (Anthropic)](https://github.com/anthropics/fermats-last-theorem) at 6e837e753555: Its README states that it is a complete, machine-checked proof of FLT via Frey, Serre, Ribet, Wiles and Taylor-Wiles, from the three standard axioms, checked by comparator and the nanoda kernel.
- [OpenAI Math](https://github.com/openai/math) at 4eaee8754825: Lean proofs of results from about 721 model-generated research manuscripts (README says ~42% of top-line results are formalized). Includes Hodge for CM abelian varieties, BSD cases, and counterexamples (Hadwiger, Kaplansky).
- [Classification of Finite Simple Groups (Axiom)](https://github.com/AxiomMath/CFSG) at 69cb972f587a: A sorry-free proof of the Classification of Finite Simple Groups, mostly first-generation, using TauCeti's ClassificationStatement; produced by AxiomProver.
- [Lean Pool](https://github.com/LeanPool/lean-pool) at 2b205bf90401: A pool of permissively licensed Lean projects outside Mathlib's scope, e.g. Navier-Stokes, CKN, Davis-Kahan, Conway-Soifer, Zeta5Irrational, MovingSofa.
- [The Stacks Project in Lean (Axiom)](https://github.com/AxiomMath/Stacks) at 5ed82d14634e: A formalization of the Stacks Project, indexed by Stacks tag, in two tiers: StacksCore, human-reviewed, and StacksFrontier, drafted with AxiomProver and not yet reviewed. Declarations also carry the EGA and SGA items they prove.

### Formal Frontier libraries

- [Adic modules](https://github.com/FormalFrontier/adic-modules) at 86f9b35ef35a: Ideal-power torsion, adic completions, Henselian pairs and Hensel lifting, valuation-ring completions; background: Fujiwara-Kato, Fesenko-Vostokov, Stacks, Matsumura
- [Algebraic direct limits](https://github.com/FormalFrontier/algebraic-direct-limits) at e5d0dea1697c: Directed/filtered limits of modules and rings, tensor products, Mittag-Leffler inverse systems, spectra and Krull dimension of filtered colimits (Stacks 10.86.3 background)
- [Algebraic groups](https://github.com/FormalFrontier/algebraic-groups) at cad2dc41da14: Matrix point groups, finite algebraic group schemes, coordinate Hopf algebras, unitriangular groups (background: Milne Algebraic Groups, Hopf algebras)
- [Coherent modules](https://github.com/FormalFrontier/coherent-modules) at b670b34e8741: Coherent rings and modules, finite-presentation criteria, localization/descent, Noetherian ascent (folklore; Fujiwara-Kato background)
- [Complex analysis](https://github.com/FormalFrontier/complex-analysis) at c22c803e257c: Complex Frechet-differentiable maps on finite-dim spaces are analytic, via polydisc Cauchy formula (folklore)
- [Continuous group cohomology](https://github.com/FormalFrontier/continuous-group-cohomology) at 4434e3f21530: Low-degree continuous group cohomology, Tate deflation, compact-group norm-limit sequences; adapts Neukirch-Schmidt-Wingberg Cohomology of Number Fields
- [Dedekind ideal arithmetic](https://github.com/FormalFrontier/dedekind-ideal-arithmetic) at c76307595a11: Six results on ideal absolute norms, principal primes from norms, class groups of Dedekind localizations (Weibel K-book background)
- [Finite étale algebras](https://github.com/FormalFrontier/finite-etale-algebras) at 4627c3ab2479: Finite etale subalgebras over fields, Galois/separable/purely inseparable descent (Milne Algebraic Groups background)
- [Finite-group Tate cohomology](https://github.com/FormalFrontier/finite-group-tate-cohomology) at c0c9d563d45a: Norms, exceptional Tate degrees, cyclic period-two comparisons for finite-group representations (folklore)
- [Formal power series](https://github.com/FormalFrontier/formal-power-series) at 29bdab8c1f57: Logarithmic derivatives of power-series units, restricted (adic) multivariate power series; adapts Weibel K-book
- [Fundamental groupoids](https://github.com/FormalFrontier/fundamental-groupoids) at ce38a38faef1: Fundamental groupoids, descent along open covers, van Kampen for two-open covers; adapts May's Concise Course
- [General linear groups](https://github.com/FormalFrontier/general-linear-groups) at a2199cf0d02b: GL_n over (non)commutative rings: elementary matrices, commutators, Whitehead lemma, Steinberg relations; adapts Weibel K-book, Fesenko-Vostokov
- [Graded rings](https://github.com/FormalFrontier/graded-rings) at 6a459e8e4d20: Graded quotients/localizations, homogeneous primes, symmetric algebras; Vakil Rising Sea 7.4.F-H background
- [Group rings](https://github.com/FormalFrontier/group-rings) at 8e90e6563300: Group algebras of free abelian groups as Laurent polynomial algebras, etc.; adapts Weibel K-book
- [Group theory](https://github.com/FormalFrontier/group-theory) at cad97f1a1920: Shared topological/algebraic group API (continuous homs, open subgroups, profinite characters); cites May, Neukirch-Schmidt-Wingberg plus many original proofs
- [Homological algebra](https://github.com/FormalFrontier/homological-algebra) at 8bcaebe913c5: Euler invariants, cochain constructions, double-complex totals; adapts Weibel K-book and Cohomology of Number Fields
- [Ideal completion](https://github.com/FormalFrontier/ideal-completion) at e316d02a1c08: Ideal completions of bounded distributive lattices as coherent frames (folklore; Fujiwara-Kato background)
- [Integral closure](https://github.com/FormalFrontier/integral-closure) at 8f0b15a513bb: Integral-closure and normality descent along retractions and field scalar extensions (original; Rising Sea background)
- [Iwasawa modules](https://github.com/FormalFrontier/iwasawa-modules) at e71db96b779b: Pseudo-null/pseudo-isomorphism calculus and completed group algebras (Cohomology of Number Fields background)
- [Metrization](https://github.com/FormalFrontier/metrization) at 9c7cf0d82ab3: Nagata-Smirnov metrization theorem and its converse, metrizability from locally finite metrizable covers (adapts Nagata 1950 and Smirnov 1951 papers)
- [Minimal primes](https://github.com/FormalFrontier/minimal-primes) at 45952e34e2da: Minimal primes over principal ideals in UFD semirings, irreducible components (Rising Sea background)
- [Morphism properties](https://github.com/FormalFrontier/morphism-properties) at 1666ed81a5c4: Category theory: morphism properties under pullback, over-category transport, density under slicing
- [Multivariate polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at 724d9804aa6e: Infinite-variable ideals, evaluation ideals, block substitution, Taylor expansion of MvPolynomial (mostly original; Rising Sea/Fujiwara-Kato background)
- [Norm forms](https://github.com/FormalFrontier/norm-forms) at 4b2893fb313b: Field and spectral norms over complete ultrametric fields, norm forms, nontrivial zeros of forms, Chevalley-Warning; formalizes parts of Fesenko-Vostokov; BGR background
- [Polynomial root stability](https://github.com/FormalFrontier/polynomial-root-stability) at efade497a4cf: Krasner-type stability of root fields, Newton lifting (Neukirch-Schmidt-Wingberg, Fesenko-Vostokov background)
- [Profinite groups](https://github.com/FormalFrontier/profinite-groups) at bf258c54ddbe: Profinite groups: finite-stage limits, Sylow families, closed subgroups (Cohomology of Number Fields background)
- [Projective modules](https://github.com/FormalFrontier/projective-modules) at 27f95a8b2a06: Projective modules, Baer criterion and linear systems, K-theory foundations; adapts Weibel K-book
- [Projective space](https://github.com/FormalFrontier/projective-space) at 9dbd208f4275: Proj of graded rings, standard charts, projective space (original; Rising Sea background)
- [Quadratic algebras](https://github.com/FormalFrontier/quadratic-algebras) at 16a5b4c54c45: Quadratic algebras, integral closure criteria, class number of Q(sqrt(-5)) (original)
- [Restricted-product duality](https://github.com/FormalFrontier/restricted-product-duality) at df6cc0bb4483: Topology of cofinite restricted products, path components, compactness (Cohomology of Number Fields, May background)
- [Ringed spaces](https://github.com/FormalFrontier/ringed-spaces) at 052015f070ef: Ringed-space restriction and gluing, module presheaf/sheaf scalar extension and inverse image (original; adapts Mathlib)
- [Scheme properties](https://github.com/FormalFrontier/scheme-properties) at 09db7d881a2f: Scheme properties, rational maps and function fields, birational geometry; Rising Sea background, adapts Milne Algebraic Groups and Weibel
- [Sequence growth](https://github.com/FormalFrontier/sequence-growth) at ccf81c7190cb: Growth bounds for natural-division lower recurrences (original)
- [Sheaf cohomology](https://github.com/FormalFrontier/sheaf-cohomology) at 85cf087ff3e2: Sheaf cohomology, quasi-flasque acyclicity, derived pushforward, sheafed-space limits (folklore; Fujiwara-Kato background)
- [Simplicial objects](https://github.com/FormalFrontier/simplicial-objects) at e210890fdc17: Decalage of simplicial objects, chain transfers and homology maps (folklore; May background)
- [Simplicial rings](https://github.com/FormalFrontier/simplicial-rings) at 728785746bd0: Central polynomial simplices and simplicial homotopy (Weibel K-book background)
- [Smooth regularity](https://github.com/FormalFrontier/smooth-regularity) at fbc0ee825697: Conormal/Jacobian criteria, smooth implies regular over fields (Stacks background)
- [Spectral Stone duality](https://github.com/FormalFrontier/spectral-stone-duality) at 3d9e22b25e63: Stone duality between bounded distributive lattices and spectral spaces, cofiltered spectral limits (folklore; Fujiwara-Kato)
- [Sphere topology](https://github.com/FormalFrontier/sphere-topology) at 672d46f90cf5: Singular homology of spheres, Brouwer fixed point for the disk, non-retraction (May, Weibel background)
- [Stable range](https://github.com/FormalFrontier/stable-range) at 4d01f17954ba: Bass stable range, cancellation, unimodular rows; adapts Weibel K-book
- [Supernatural numbers](https://github.com/FormalFrontier/supernatural-numbers) at cb444a4051e5: Supernatural numbers, profinite orders and indices; adapts Neukirch-Schmidt-Wingberg
- [Toric ideals](https://github.com/FormalFrontier/toric-ideals) at 593116e0783d: Toric/binomial ideals, fiber normalization, monoid-algebra kernels; adapts Vakil Rising Sea
- [Valuation integers](https://github.com/FormalFrontier/valuation-integers) at 212f1a045abb: Integers of rank-one valuations: power divisibility, Krull dimension bounds; adapts Fesenko-Vostokov
- [Vector bundles](https://github.com/FormalFrontier/vector-bundles) at e3fb9de334c8: Hermitian/real fiber metrics, orthogonal subbundles, local coordinates; adapts Hatcher's Vector Bundles and K-Theory
