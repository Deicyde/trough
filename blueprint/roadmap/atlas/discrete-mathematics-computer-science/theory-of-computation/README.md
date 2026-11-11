# Theory of Computation

5,667 results of ATLAS's vault, 5,437 proved and 230 stated but not proved, in this subject's topics.

The mathematical study of what can be computed and at what cost: machine models, computability and undecidability, automata and formal languages, and computational complexity.

[NP-completeness](part-01/np-completeness/README.md) is the largest field, with over two fifths of the subject's articles. It
starts from the [Cook–Levin theorem](part-01/np-completeness/cook-levin/README.md), that SAT is in NP and every problem in NP
reduces to it by a polynomial-time many-one reduction, and establishes NP-completeness problem by problem, from
variants of [satisfiability](part-01/np-completeness/satisfiability/README.md) to Hamiltonian cycles, clique, graph coloring
and subset sum. [Complexity classes](part-01/complexity-classes/README.md) has Savitch's theorem, the Immerman–Szelepcsényi
theorem $\mathrm{NL} = \mathrm{coNL}$ and Ladner's theorem, and
[hierarchy theorems and barriers](part-01/hierarchy-theorems-and-barriers/README.md) has the time hierarchy theorem and the
Baker–Gill–Solovay [oracles](part-01/hierarchy-theorems-and-barriers/relativization-and-oracle-separations.md) relative
to which P and NP differ or coincide.

In [regular languages](part-01/regular-languages/README.md), Kleene's theorem identifies the languages of finite automata with
those of regular expressions, and [minimization](part-01/regular-languages/minimization/README.md) rests on the Myhill–Nerode
theorem. [Context-free languages](part-01/context-free-languages/README.md) has normal forms, CYK and Earley recognizers, the
equivalence of grammars with [pushdown automata](part-01/context-free-languages/grammars-and-pushdown-automata/README.md), and
the pumping and Ogden lemmas, and [decision procedures](part-01/decision-procedures/README.md) decide emptiness and
equivalence of finite automata and emptiness of context-free grammars.

[Turing machines](part-01/turing-machines/README.md), from single-tape and multi-tape machines to universal ones, compute
exactly the recursive functions ([equivalence of models](part-01/equivalence-of-models/README.md)).
[Computability](part-01/computability/README.md) has Rice's theorem and the
[undecidability of the halting problem](part-01/computability/halting-problem-and-rice-s-theorem.md), Kleene's
[recursion theorem](part-01/computability/kleene-s-recursion-theorem.md) and the
[Busy Beaver](part-01/computability/busy-beaver.md) value $\Sigma(5) = 4098$, and
[undecidable problems](part-01/undecidable-problems/README.md) include the
[Post correspondence problem](part-01/undecidable-problems/post-correspondence-problem.md) and
[Hilbert's tenth problem](part-01/undecidable-problems/diophantine-sets-and-hilbert-s-tenth-problem.md), by the theorem
of Davis, Putnam, Robinson and Matiyasevich that the recursively enumerable sets are the Diophantine ones.

## [Turing machines to NP-completeness](part-01/README.md)

- [Turing machines](part-01/turing-machines/README.md)
- [Equivalence of models of computation](part-01/equivalence-of-models/README.md)
- [Computability and undecidability](part-01/computability/README.md)
- [Degrees of unsolvability and the arithmetical hierarchy](part-01/degrees-and-hierarchies/README.md)
- [Undecidable problems](part-01/undecidable-problems/README.md)
- [Decision procedures for automata, grammars and strings](part-01/decision-procedures/README.md)
- [Finite automata and regular languages](part-01/regular-languages/README.md)
- [Automata on infinite words and infinite games](part-01/omega-automata-and-games/README.md)
- [Context-free languages](part-01/context-free-languages/README.md)
- [Context-sensitive languages](part-01/context-sensitive-languages/README.md)
- [Complexity classes](part-01/complexity-classes/README.md)
- [Hierarchy theorems and proof barriers](part-01/hierarchy-theorems-and-barriers/README.md)
- [Randomized, interactive and quantum complexity](part-01/randomized-and-quantum-complexity/README.md)
- [Counting complexity](part-01/counting-complexity/README.md)
- [Pseudorandomness and one-way functions](part-01/pseudorandomness-and-one-way-functions/README.md)
- [Boolean circuit complexity](part-01/circuit-complexity/README.md)
- [Algebraic complexity](part-01/algebraic-complexity/README.md)
- [Descriptive complexity](part-01/descriptive-complexity/README.md)
- [Kolmogorov complexity](part-01/kolmogorov-complexity/README.md)
- [NP-completeness](part-01/np-completeness/README.md)

## [Probabilistically checkable… to Fine-grained and…](part-02/README.md)

- [Probabilistically checkable proofs and inapproximability](part-02/pcp-and-inapproximability/README.md)
- [Completeness for other complexity classes](part-02/completeness-other-classes/README.md)
- [Problems solvable in polynomial time](part-02/polynomial-time-problems/README.md)
- [Fine-grained and exponential-time complexity](part-02/fine-grained-complexity/README.md)
