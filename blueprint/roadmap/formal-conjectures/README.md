# Formal Conjectures

[Formal Conjectures](https://github.com/google-deepmind/formal-conjectures), from Google DeepMind, states open and solved mathematical problems in Lean, with a site at https://google-deepmind.github.io/formal-conjectures/. This chapter maps it as read at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6) (2026-11-13), Lean toolchain v4.33.1: a part per source folder of `FormalConjectures/`, an article per problem file and, in it, a card per statement.

Every statement carries one `category` attribute: research open, research solved, textbook, API or test. The articles show the first three, 5,216 statements in 1,837 articles: 1,902 open and stated without proof; 3,065 research solved, 159 of them proved here and 1,116 of the rest with a `formal_proof` link to a proof elsewhere; 249 textbook results, 136 of them proved here. Besides these, 1 definition carries a category attribute; its card says it is not a statement. The 2,692 test and 640 API statements are counted in their problem's article, not shown. 14 problem files state none of the first three and have no article; their folder's page lists them.

A card's status line reads the statement's category, its `formal_proof` links and whether the text of its proof in the file contains `sorry`: “Open: stated without proof.”; “Solved: stated here; a Lean proof is at …” (or “a proof in another system is at …”) when a link gives one, and “Solved: stated here without proof.” when none does; “Textbook result, stated without proof.”; and “Proved here.” or “Textbook result, proved here.” when the proof's text holds no `sorry`, which, like Formal Conjectures' own `hasSorryFreeProof`, says nothing of the statements that proof uses. Formal Conjectures marks a link `formal_conjectures` when the proof fills this statement as written, and `lean4` when the problem is solved in Lean elsewhere, perhaps as an equivalent statement.

No Lean is run for this chapter. Statements, docstrings and attributes are read from the source text: a statement is a named declaration with a category in the `@[...]` list right before it, its Lean statement runs to the `:=` that starts its proof, and its name is read under the namespaces it sits in. A statement with no name, an `example`, or a `private` one is left out, as Formal Conjectures' own site leaves them out. The articles have no dependencies: edges between statements need Lean.

Two indexes link the articles: [by subject](by-subject/README.md), from the `AMS` attributes' top-level classes of the Mathematics Subject Classification (43 subjects), and the [FC100 subsets](fc100-subsets/README.md), Formal Conjectures' benchmark lists.

The docstrings and Lean statements are quoted from [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), under its Apache-2.0 license, with each article naming its file. Formal Conjectures asks that the Erdős problems' docstrings follow erdosproblems.com; the Erdős part says how, and each Erdős article links its problem's page there.

- [Erdős problems](erdos-problems/README.md)
- [OEIS](oeis/README.md)
- [Wikipedia](wikipedia/README.md)
- [Green's open problems](greens-open-problems/README.md)
- [Written on the Wall II](written-on-the-wall-ii/README.md)
- [Papers](papers/README.md)
- [arXiv](arxiv/README.md)
- [MathOverflow](mathoverflow/README.md)
- [Books](books/README.md)
- [Other](other/README.md)
- [Kourovka](kourovka/README.md)
- [Millennium problems](millennium-problems/README.md)
- [Optimization constants](optimization-constants/README.md)
- [Open quantum problems](open-quantum-problems/README.md)
- [Hilbert's problems](hilberts-problems/README.md)
- [Litt's problems](litts-problems/README.md)
- [By subject](by-subject/README.md)
- [FC100 subsets](fc100-subsets/README.md)
