# Ideal completion

> Ideal completions of bounded distributive lattices: the injective principal bounded lattice homomorphism, finite-join witnesses for arbitrary suprema, frame structure, compact-principal characterization and compact generation, and a prime-order-ideal/Boolean-map equivalence for bounded lattices.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/ideal-completion/blob/e316d02a1c0814b130a7085a112c142542b7019d/formalization.yaml) of [FormalFrontier/ideal-completion](https://github.com/FormalFrontier/ideal-completion) at commit [e316d02a](https://github.com/FormalFrontier/ideal-completion/tree/e316d02a1c0814b130a7085a112c142542b7019d), Apache-2.0.*

2 articles: 2 for headline results in its README whose declaration link names a declaration the scan finds in the linked file. Its other headline results are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/ideal-completion](https://github.com/FormalFrontier/ideal-completion), read at commit [e316d02a](https://github.com/FormalFrontier/ideal-completion/tree/e316d02a1c0814b130a7085a112c142542b7019d) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “other: independent AI-agent review”.
- Review notes: “Independent AI agents reviewed the mathematical core and module/example contributions.”
- Automation: agent; tool setup “Formal Frontier AI agents using Lean, Lake and Git for formalization, documentation and maintenance, with separate independent agent review.”
- Automation notes: “The mathematical core, reference adapter and packaging were prepared by the Anchor AI agent; another AI contributor prepared the modules and examples. Independent AI agents reviewed the formalization. No human peer review or source-author endorsement is implied.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Ideal completion of a bounded distributive lattice* (folklore; independently-proves).
- [Foundations of Rigid Geometry I](https://arxiv.org/abs/1308.4734v5), Kazuhiro Fujiwara, Fumiharu Kato, Chapter 0, section 2.2(b), paragraph after Definition 2.2.6, printed page 38 (book; background).

## Builds on

No other Formal Frontier library.

## Used by

- [Spectral Stone duality](../spectral-stone-duality/README.md)

## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/ideal-completion/blob/e316d02a1c0814b130a7085a112c142542b7019d/README.md#headline-results) of [FormalFrontier/ideal-completion](https://github.com/FormalFrontier/ideal-completion) at commit [e316d02a](https://github.com/FormalFrontier/ideal-completion/tree/e316d02a1c0814b130a7085a112c142542b7019d), Apache-2.0.*

- [Principal embedding](principal-embedding.md)

**Frame and arbitrary suprema.** The
[`Order.Frame` instance](https://github.com/FormalFrontier/ideal-completion/blob/e316d02a1c0814b130a7085a112c142542b7019d/IdealCompletion/OrderIdeal.lean#L96) makes the ideal
completion a complete Heyting algebra. The
[`mem_sSup_iff` theorem](https://github.com/FormalFrontier/ideal-completion/blob/e316d02a1c0814b130a7085a112c142542b7019d/IdealCompletion/OrderIdeal.lean#L77) characterizes
`x ∈ sSup S` by a finite set of elements, each in some ideal of the *arbitrary*
family `S`, whose join is **at least** `x`. This includes the empty-family and
bottom cases; it is not restricted to directed families.

**Compact generation.** Every principal ideal is
[compact](https://github.com/FormalFrontier/ideal-completion/blob/e316d02a1c0814b130a7085a112c142542b7019d/IdealCompletion/OrderIdeal.lean#L116), and
[`isCompactElement_iff_eq_principal`](https://github.com/FormalFrontier/ideal-completion/blob/e316d02a1c0814b130a7085a112c142542b7019d/IdealCompletion/OrderIdeal.lean#L141)
identifies **all** compact ideals as principal. The
[`IsCompactlyGenerated` instance](https://github.com/FormalFrontier/ideal-completion/blob/e316d02a1c0814b130a7085a112c142542b7019d/IdealCompletion/OrderIdeal.lean#L168)
expresses every ideal as a supremum of compact ideals. Compactness here is
order-theoretic, not finiteness of the ideal's underlying set.

- [Prime ideals and Boolean-valued maps](prime-ideals-and-boolean-valued-maps.md)

These constructions and proofs build on mathlib's existing ideal, lattice and
compactness infrastructure. They do not establish prime-ideal existence,
spectra, Stone duality, a universal extension property, or generic partial-order
completion.

The [generated API reference](https://github.com/FormalFrontier/ideal-completion/blob/e316d02a1c0814b130a7085a112c142542b7019d/docs/API.md) is bound to an earlier seven-declaration
ideal-completion revision and does **not** cover the new prime-ideal module or
the current aggregate import. See the [prime-ideal API guide](https://github.com/FormalFrontier/ideal-completion/blob/e316d02a1c0814b130a7085a112c142542b7019d/docs/PrimeIdeals.md)
for the new declarations, and [reference scope and generation](https://github.com/FormalFrontier/ideal-completion/blob/e316d02a1c0814b130a7085a112c142542b7019d/docs/README.md)
for the historical native signatures and exact source binding.
