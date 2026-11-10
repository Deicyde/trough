# Finite étale algebras

> Finite etale subalgebra constructions over fields, spectrum component bounds over separably closed fields, and literal subalgebra reconstruction along finite Galois, separable-closure and purely inseparable field extensions.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/finite-etale-algebras/blob/4627c3ab2479e331c889a374309e62ee1b64a8af/formalization.yaml) of [FormalFrontier/finite-etale-algebras](https://github.com/FormalFrontier/finite-etale-algebras) at commit [4627c3ab](https://github.com/FormalFrontier/finite-etale-algebras/tree/4627c3ab2479e331c889a374309e62ee1b64a8af), Apache-2.0.*

No articles: its formalization.yaml lists no highlights, and none of its 5 headline results links a declaration that the scan finds in the linked file at this commit, so they are quoted below.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/finite-etale-algebras](https://github.com/FormalFrontier/finite-etale-algebras), read at commit [4627c3ab](https://github.com/FormalFrontier/finite-etale-algebras/tree/4627c3ab2479e331c889a374309e62ee1b64a8af) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “agent-reviewed”.
- Review notes: “Mathematical code, public-module clients and later hypothesis generalization received independent non-author agent review. This is not human review, source-author endorsement or a source-coverage decision. Generated API documentation records historical source bindings, not proof certification.”
- Automation: agent; tool setup “Formal Frontier AI agents used Lean and Lake with pinned mathlib, repository tools and independent non-author agent review.”
- Automation notes: “AI-assisted development under human project direction. No model identity, expenditure, elapsed-time total or human mathematical review is asserted.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Algebraic Groups*, James S. Milne, 2017 edition, Propositions 1.29 and 1.30; the separable-closure paragraph in the proof of Proposition 1.30(a) is on printed page 15 (book; background).
- *Original finite-etale subalgebra and embedded descent APIs*, Formal Frontier Agents (original-proof; independently-proves).

## Builds on

No other Formal Frontier library.

## Used by

- [Scheme properties](../../algebraic-geometry/scheme-properties/README.md)


## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/finite-etale-algebras/blob/4627c3ab2479e331c889a374309e62ee1b64a8af/README.md#headline-results) of [FormalFrontier/finite-etale-algebras](https://github.com/FormalFrontier/finite-etale-algebras) at commit [4627c3ab](https://github.com/FormalFrontier/finite-etale-algebras/tree/4627c3ab2479e331c889a374309e62ee1b64a8af), Apache-2.0.*

**Finite etale subalgebras, composites and idempotents.** Over a field `k`,
[surjective images](https://github.com/FormalFrontier/finite-etale-algebras/blob/4627c3ab2479e331c889a374309e62ee1b64a8af/FiniteEtaleAlgebras/MaximalSubalgebra.lean#L44) of finite
etale algebras are finite etale, and
[binary suprema](https://github.com/FormalFrontier/finite-etale-algebras/blob/4627c3ab2479e331c889a374309e62ee1b64a8af/FiniteEtaleAlgebras/MaximalSubalgebra.lean#L129) of finite
etale subalgebras of a commutative `k`-algebra `R` remain finite etale. A
*supplied* uniform natural-number bound on their dimensions yields a
[greatest such subalgebra](https://github.com/FormalFrontier/finite-etale-algebras/blob/4627c3ab2479e331c889a374309e62ee1b64a8af/FiniteEtaleAlgebras/MaximalSubalgebra.lean#L146);
this library does not prove the existence of that bound. Every idempotent
[lies in a finite etale subalgebra](https://github.com/FormalFrontier/finite-etale-algebras/blob/4627c3ab2479e331c889a374309e62ee1b64a8af/FiniteEtaleAlgebras/MaximalSubalgebra.lean#L86),
constructed from `Fin 2 → k` using `e` and `1 - e`.

**Spectrum component counts.** For a finite etale algebra `S` over a
separably closed field `k`, the
[component-count theorem](https://github.com/FormalFrontier/finite-etale-algebras/blob/4627c3ab2479e331c889a374309e62ee1b64a8af/FiniteEtaleAlgebras/SpectrumComponents.lean#L38)
identifies `Nat.card (ConnectedComponents (PrimeSpectrum S))` with
`Module.finrank k S`. A continuous surjection `X → PrimeSpectrum S`
[bounds the dimension](https://github.com/FormalFrontier/finite-etale-algebras/blob/4627c3ab2479e331c889a374309e62ee1b64a8af/FiniteEtaleAlgebras/SpectrumComponents.lean#L68)
by the component count of `X` **when `[Finite (ConnectedComponents X)]`**.
Independent universes, zero algebras and empty-space cases are retained.

**Finite-Galois and separable-closure embedded descent.** For a finite
Galois extension `L/k`, a subalgebra `P` of `L ⊗[k] R` stable under every
[coefficientwise automorphism](https://github.com/FormalFrontier/finite-etale-algebras/blob/4627c3ab2479e331c889a374309e62ee1b64a8af/FiniteEtaleAlgebras/SemilinearDescent.lean)
is reconstructed from its honest preimage under `r ↦ 1 ⊗ r`. The
[reconstruction equivalence](https://github.com/FormalFrontier/finite-etale-algebras/blob/4627c3ab2479e331c889a374309e62ee1b64a8af/FiniteEtaleAlgebras/SemilinearDescent.lean#L420)
and [range equality](https://github.com/FormalFrontier/finite-etale-algebras/blob/4627c3ab2479e331c889a374309e62ee1b64a8af/FiniteEtaleAlgebras/SemilinearDescent.lean#L439)
identify the *literal ambient* scalar extension with `P`; finite etaleness
[descends](https://github.com/FormalFrontier/finite-etale-algebras/blob/4627c3ab2479e331c889a374309e62ee1b64a8af/FiniteEtaleAlgebras/SemilinearDescent.lean#L446) if `P` is finite
etale. For a separable closure `K/k`, the
[finite-data layer](https://github.com/FormalFrontier/finite-etale-algebras/blob/4627c3ab2479e331c889a374309e62ee1b64a8af/FiniteEtaleAlgebras/SeparableClosureDescent.lean)
captures an embedded finite-dimensional algebra over a finite Galois
intermediate field and is coherent under enlargement. Its
[descent package](https://github.com/FormalFrontier/finite-etale-algebras/blob/4627c3ab2479e331c889a374309e62ee1b64a8af/FiniteEtaleAlgebras/SeparableClosureDescent.lean#L479)
reconstructs a finite etale `P` stable under *every* coefficientwise
`k`-automorphism of `K`, including preimage membership and literal ambient
range equality.

**Purely inseparable idempotents and reconstruction.** For a purely
inseparable field extension `K/k`, every idempotent of `K ⊗[k] R` belongs to
the [range of the right-factor inclusion](https://github.com/FormalFrontier/finite-etale-algebras/blob/4627c3ab2479e331c889a374309e62ee1b64a8af/FiniteEtaleAlgebras/PurelyInseparableDescent.lean#L45)
from `R`; [the reversed tensor orientation](https://github.com/FormalFrontier/finite-etale-algebras/blob/4627c3ab2479e331c889a374309e62ee1b64a8af/FiniteEtaleAlgebras/PurelyInseparableDescent.lean#L35)
is also available. If `K` is additionally separably closed, the
[reconstruction package](https://github.com/FormalFrontier/finite-etale-algebras/blob/4627c3ab2479e331c889a374309e62ee1b64a8af/FiniteEtaleAlgebras/PurelyInseparableDescent.lean#L79)
recovers each embedded finite etale `K`-subalgebra from a finite etale
`k`-subalgebra of `R`, with equivalence and
[range equality](https://github.com/FormalFrontier/finite-etale-algebras/blob/4627c3ab2479e331c889a374309e62ee1b64a8af/FiniteEtaleAlgebras/PurelyInseparableDescent.lean#L237)
agreeing with the literal ambient scalar-extension map. No
finite-dimensionality assumption on `K/k` is imposed.

**Conditional point lifting.** Let `R → U → B` be compatible algebra maps
of commutative rings, with `U` finite as an `R`-module and `B = S⁻¹U`
flat over `R`. For `I ⊆ Jac(R)`, the
[point-lifting theorem](https://github.com/FormalFrontier/finite-etale-algebras/blob/4627c3ab2479e331c889a374309e62ee1b64a8af/FiniteEtaleAlgebras/PointLifting.lean#L278) lifts the
specified `R`-algebra map `z : B → R/I` to `s : B → R` with
`(R → R/I) ∘ s = z`, provided a supplied `ebar ∈ U/IU` has an
idempotent lift `ε ∈ U` satisfying `z(β(ε)) = 1` and the following
eigencondition: `ebar · (ubar - rbar) = 0` whenever
`z(β(u)) = r mod I`. Here `β : U → B` is the structural map and
`ubar`, `rbar` are the images of `u`, `r` in `U/IU`.
No etaleness or finite-presentation hypothesis on `B` is required. This
is conditional on the supplied idempotent; it does not assert that every
residue point lifts.

For the finite-etale subalgebra, spectrum and descent results above, the
ambient `R` is a commutative algebra over a field; it need not be
finite-dimensional, finitely generated, reduced or nontrivial (the zero ring
is allowed). The point-lifting theorem instead allows arbitrary commutative
base rings. These are noncomputable mathematical interfaces, not algorithms
for extracting descended algebras or lifted points. This library's
`IsFiniteEtale` predicate combines mathlib's `Module.Finite` and
`Algebra.Etale`; mathlib also supplies the tensor-product, Galois, descent,
spectrum and commutative-algebra infrastructure. This repository develops
the subalgebra, component-count, literal reconstruction and conditional
point-lifting interfaces described here. See the linked modules for full
signatures and the [API reference](https://github.com/FormalFrontier/finite-etale-algebras/blob/4627c3ab2479e331c889a374309e62ee1b64a8af/docs/API.md) for the finite-etale and descent
interfaces it covers; source-specific correspondence and coverage belong in
the respective source repositories, not this reusable library.
