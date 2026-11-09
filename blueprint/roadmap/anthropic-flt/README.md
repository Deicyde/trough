# Fermat's Last Theorem (Anthropic)

[anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem), by Anthropic, read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2) (2026-09-24). The repository states that it proves Fermat's Last Theorem in Lean 4 along the route of Frey, Serre, Ribet, Wiles and Taylor-Wiles. This chapter runs no Lean and checks none of it: what it says about the proof is what the repository states. Its formalization.yaml describes the project so:

> A complete, machine-checked Lean 4 proof of Fermat's Last Theorem, built on Mathlib: for every natural number n >= 3 there are no positive natural numbers a, b, c with a^n + b^n = c^n (declaration fermat_last_theorem). The default build target also derives Mathlib's own statement FermatLastTheorem. The argument is that of Frey, Serre, Ribet, Wiles and Taylor-Wiles; the named classical inputs (irreducibility of the Frey representation, Langlands-Tunnell, modularity lifting, modularity of semistable curves, level lowering) are proved within the development, in the strength the argument needs, rather than assumed.

*Quoted from the project description in [formalization.yaml](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/formalization.yaml) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0.*

Its PROOF-PATH.md, “The route of the proof”, opens:

> The argument is that of Frey, Serre, Ribet, Wiles and Taylor-Wiles, largely as in Darmon, Diamond and Taylor,
> run as a proof by contradiction. A theorem `X.y` is stated in `Theorems/Thm_X_y.lean` and proved in
> `P2M/Sol/S_X_y.lean`, whose `import Theorems.Thm_…` lines are exactly the theorems it cites. Where this prose and the
> Lean differ, the Lean is right. Named classical theorems are proved in the strength the argument needs; the last
> section says exactly what that is.

*Quoted from [PROOF-PATH.md](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/PROOF-PATH.md) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0.*

> Portions derive from the Imperial College London FLT project led by Kevin Buzzard, from flt-regular and from Mathlib, all released under the Apache License 2.0; see NOTICE and ATTRIBUTION.md.

*Quoted from the acknowledgements in [formalization.yaml](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/formalization.yaml) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0.*

The repository's web pages list 29,511 theorems, a theorem `X.y` stated in its own file `Theorems/Thm_X_y.lean`, and mark 49 of them as landmarks. This chapter maps the 49 landmarks, one article each, in a part for each of the 6 steps of PROOF-PATH.md, as the web pages place them, and quotes its other sections; the other 29,462 theorems are counted, not mapped. An article quotes its theorem's Lean statement, from the end of the file's imports and `attribute` lines to the top-level `:=`, lists the aliases the web pages give it, and links its line in the repository at the commit above. A theorem that opens a step of PROOF-PATH.md, as the theorem carrying it, takes the step's name as its title; any other has its Lean name.

The repository's citation graph has 106,853 edges: the `import Theorems.Thm_…` lines of each proof module, which the repository documents as exactly the theorems the proof cites. Under *Proof depends on*, an article lists the landmarks its proof reaches through theorems that are not landmarks, 76 edges in all.

Where a landmark's name, or another declaration its statement file makes, is also the Lean name of an article in the [Imperial FLT chapter](../flt/README.md), the landmark's article says so and links it. The names are compared as written, so a match says only that the names agree. At this commit none does.

The repository's documentation website, https://tianyipeng.github.io/fermats-last-theorem/, has a page for each theorem, and each article links it; the data workflow checks that the site serves those pages before it links them.

The web pages also give each theorem an English title and summary, and suggested references. The repository says the English text is generated automatically from the Lean source, with the Lean statement authoritative, and that the references have not been individually verified, so this chapter leaves them out. PROOF-PATH.md, the formalization.yaml and the Lean statements are quoted as written, under the repository's Apache-2.0 license, with the repository and commit named where they are quoted.

## The route

- [1. Reduction to a prime p ≥ 5](1-reduction-to-a-prime-p-5/README.md)
- [2. Frey package](2-frey-package/README.md)
- [3. Irreducibility](3-irreducibility/README.md)
- [4. Modularity](4-modularity/README.md)
- [5. Level lowering](5-level-lowering/README.md)
- [6. S₂(Γ₀(2)) = 0](6-s2-0-2-0/README.md)
- [Exact strength of the named steps](exact-strength-of-the-named-steps/README.md)

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem), read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2) (2026-09-24).
- Lean toolchain v4.33.1, Mathlib at [db584cd6](https://github.com/leanprover-community/mathlib4/tree/db584cd6d46c92f209a44c0f1c829460d327499d).
- License: Apache-2.0.
- Authors: Anthropic.
- Review status: “self-assessed”.
- Review notes: “The proof is machine-checked: by the Lean kernel in a from-scratch build whose default target fails unless fermat_last_theorem depends on exactly propext, Classical.choice and Quot.sound; by leanprover/comparator against the Mathlib-only challenge statement in verification/comparator/Challenge.lean (statement and constants identical, no other axiom, full kernel replay including Mathlib); and by the independent kernel nanoda, which accepted every declaration of the exported environment. See README.md, "How it was verified".”
- Automation: agent
- Scope, as its status states: “The full statement of Fermat's Last Theorem for natural-number exponents n >= 3, proved from Lean's three standard axioms with every intermediate result proved in the development or taken from Mathlib; nothing is assumed from the literature.”

## Main results

The main results its formalization.yaml lists, with the sorry count and axioms it gives for each, and where the source text declares them.

- `fermat_last_theorem`, stated in [Theorems/Thm_fermat_last_theorem.lean, line 128](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_fermat_last_theorem.lean#L128); its article: [fermat_last_theorem](1-reduction-to-a-prime-p-5/fermat-last-theorem.md); sorry count 0; axioms `propext`, `Classical.choice`, `Quot.sound`.
- `flt_mathlib`, stated in [FinalCheck.lean, line 7](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/FinalCheck.lean#L7); sorry count 0; axioms `propext`, `Classical.choice`, `Quot.sound`.

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Modular elliptic curves and Fermat's Last Theorem*, Andrew Wiles, Annals of Mathematics 141 (1995), 443-551 (article; adapts).
- *Ring-theoretic properties of certain Hecke algebras*, Richard Taylor, Andrew Wiles, Annals of Mathematics 141 (1995), 553-572 (article; adapts).
- *Fermat's Last Theorem*, Henri Darmon, Fred Diamond, Richard Taylor (article; adapts).
