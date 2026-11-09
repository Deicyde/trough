# Formal Conjectures

[Formal Conjectures](https://github.com/google-deepmind/formal-conjectures), from Google DeepMind, states open and solved mathematical problems in Lean, with a site at https://google-deepmind.github.io/formal-conjectures/. This chapter maps it as read at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0) (2026-11-06), Lean toolchain v4.33.1: a part per source folder of `FormalConjectures/`, an article per problem file and, in it, a card per statement.

Every statement carries one `category` attribute: research open, research solved, textbook, API or test. The articles show the first three, 5,133 statements in 1,814 articles: 1,873 open and stated without proof, 2,861 solved (1,099 of them with a `formal_proof` link to a proof elsewhere), 247 textbook results, and 283 of these proved here. 1 definition carrying a category attribute is shown as such. The 2,673 test and 630 API statements are counted in their problem's article, not shown. 14 problem files state none of the first three and have no article; their folder's page lists them.

A card's status line reads the statement's category, its `formal_proof` links and whether the text of its proof in the file contains `sorry`: “Open: stated without proof.”; “Solved: stated here; a Lean proof is at …” when a link gives one, and “Solved: stated here without proof.” when none does; “Proved here.” when the proof's text holds no `sorry`, which, like Formal Conjectures' own `hasSorryFreeProof`, says nothing of the statements that proof uses. Formal Conjectures marks a link `formal_conjectures` when the proof fills this statement as written, and `lean4` when the problem is solved in Lean elsewhere, perhaps as an equivalent statement.

No Lean is run for this chapter. Statements, docstrings and attributes are read from the source text: a statement is a named declaration with a category in the `@[...]` list right before it, its Lean statement runs to the `:=` that starts its proof, and its name is read under the namespaces it sits in. A statement with no name, an `example`, or a `private` one is left out, as Formal Conjectures' own site leaves them out. The articles have no dependencies: the problems form a flat collection, and edges between statements need Lean.

Two indexes link the articles: [by subject](by-subject/README.md), from the `AMS` attributes' top-level classes of the Mathematics Subject Classification (43 subjects), and the [FC100 subsets](fc100-subsets/README.md), Formal Conjectures' benchmark lists.

The docstrings and Lean statements are quoted from [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), under its Apache-2.0 license, with each article naming its file. Formal Conjectures asks that the Erdős problems' docstrings follow erdosproblems.com; the Erdős part says how, and each Erdős article links its problem's page there.

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
