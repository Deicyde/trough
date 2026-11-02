# Generating laws from equations

The invariants defined in this chapter are properties of the *syntax* of the equations being considered. In other words, they are properties of the laws associated with the equations, rather than of the equations themselves. Proving non-implications using invariants requires a way to operate on the syntax of the equations and then translate the reasoning back to results about the original equations.

A magma law can be generated from an equation by accessing the syntax used in its definition and converting it to a declaration representing a magma law through metaprogramming. There is a choice in the variable set of the magma law – one one hand, it can be a finite set whose size matches the number of variables, and on the other hand, it can be the set of natural numbers. The advantage of the former is that one can generate proofs that the satisfiability of the magma law is equivalent to the satisfiability of the original equation (this only needs to be done for variable sets of size up to six, since that is the maximum size currently being considered in the project; it's convenient to prove individual lemmata for each variable set size establishing this equivalence). The advantage of the latter is that it bypasses the need to cast between various finite sets while constructing a model as a counter-example.

One approach is to generate both forms of the law, using the first to establish the equisatisfiability of the law and the equation and then transporting this result to the second form of the law. The conversion from the first form to the second is summarised in the lemma below.

- [compatibility-between-magma-laws](compatibility-between-magma-laws.md)
