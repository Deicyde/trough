---
declaration: section
origin: cited
lean: JaccardLattice.IsModularValuation, JaccardLattice.IsStrictlyPositive, JaccardLattice.GilbertCondition, JaccardLattice.jaccardDist, JaccardLattice.gilbertCondition_iff, JaccardLattice.jaccardDist_eq_div, JaccardLattice.jaccardDist_triangle_of_gilbertCondition, JaccardLattice.jaccardDist_triangle
statement: formalized
proof: formalized
---

# Lattice valuations and the Jaccard distance

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/lattices-boolean-algebras/lattice-valuations-and-the-jaccard-distance/index.html).

## Modular valuation

A function $f \colon L \to \mathbb{R}$ on a lattice $L$, with join
$\vee$ and meet $\wedge$, is a modular valuation when
$f(X) + f(Y) = f(X \vee Y) + f(X \wedge Y)$ for all $X, Y \in L$.

Formalized by `JaccardLattice.IsModularValuation`, a definition declared in [MathlibExt/Combinatorics/JaccardLattice.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/JaccardLattice.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/lattices-boolean-algebras/lattice-valuations-and-the-jaccard-distance/index.html#is-modular-valuation).

## Strictly positive valuation

A function $f \colon L \to \mathbb{R}$ on a lattice
$L$ is strictly positive when $f(X) > 0$ for every $X \in L$.

Formalized by `JaccardLattice.IsStrictlyPositive`, a definition declared in [MathlibExt/Combinatorics/JaccardLattice.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/JaccardLattice.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/lattices-boolean-algebras/lattice-valuations-and-the-jaccard-distance/index.html#is-strictly-positive).

## Gilbert condition

A function $f \colon L \to \mathbb{R}$ on a lattice $L$, with join
$\vee$ and meet $\wedge$, satisfies the Gilbert condition when
$f(X \vee Z) + f(Z \vee Y) + f(X \wedge Y) \ge
f(X \wedge Z) + f(Z \wedge Y) + f(X \vee Y \vee Z)$ for all $X, Y, Z \in L$.

Formalized by `JaccardLattice.GilbertCondition`, a definition declared in [MathlibExt/Combinatorics/JaccardLattice.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/JaccardLattice.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/lattices-boolean-algebras/lattice-valuations-and-the-jaccard-distance/index.html#gilbert-condition).

## Generalized Jaccard distance

For a function $f \colon L \to \mathbb{R}$ on a lattice
$L$ with join $\vee$ and meet $\wedge$, the Jaccard distance of $X, Y \in L$ is
$d_f(X, Y) = 1 - f(X \wedge Y) / f(X \vee Y)$.

Division by zero is taken to give $0$, so $d_f(X, Y) = 1$ when $f(X \vee Y) = 0$.

Formalized by `JaccardLattice.jaccardDist`, a definition declared in [MathlibExt/Combinatorics/JaccardLattice.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/JaccardLattice.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/lattices-boolean-algebras/lattice-valuations-and-the-jaccard-distance/index.html#jaccard-dist).

## Characterization of the Gilbert condition

A function $f \colon L \to \mathbb{R}$
on a lattice $L$ satisfies the Gilbert condition if and only if $f$ is a modular valuation
and is monotone, that is, $X \le Y$ implies $f(X) \le f(Y)$.

Formalized by `JaccardLattice.gilbertCondition_iff`, a theorem declared in [MathlibExt/Combinatorics/JaccardLattice.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/JaccardLattice.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/lattices-boolean-algebras/lattice-valuations-and-the-jaccard-distance/index.html#gilbert-condition-iff).

## Jaccard distance as a single quotient

Let $f \colon L \to \mathbb{R}$ be a strictly
positive function on a lattice $L$, with join $\vee$ and meet $\wedge$. Then for all
$X, Y \in L$ the Jaccard distance of $X$ and $Y$ with respect to $f$ is
$d_f(X, Y) = (f(X \vee Y) - f(X \wedge Y)) / f(X \vee Y)$.

Formalized by `JaccardLattice.jaccardDist_eq_div`, a theorem declared in [MathlibExt/Combinatorics/JaccardLattice.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/JaccardLattice.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/lattices-boolean-algebras/lattice-valuations-and-the-jaccard-distance/index.html#jaccard-dist-eq-div).

## Jaccard triangle inequality under the Gilbert condition

Let
$f \colon L \to \mathbb{R}$ be a strictly positive function on a lattice $L$ that satisfies
the Gilbert condition, and let $d_f$ be the Jaccard distance of $f$. Then
$d_f(U, W) + d_f(W, V) \ge d_f(U, V)$ for all $U, V, W \in L$.

Formalized by `JaccardLattice.jaccardDist_triangle_of_gilbertCondition`, a theorem declared in [MathlibExt/Combinatorics/JaccardLattice.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/JaccardLattice.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/lattices-boolean-algebras/lattice-valuations-and-the-jaccard-distance/index.html#jaccard-dist-triangle-of-gilbert-conditi).

## Triangle inequality for the generalized Jaccard distance

Let
$f \colon L \to \mathbb{R}$ be a strictly positive, monotone modular valuation on a lattice
$L$, and let $d_f$ be the Jaccard distance of $f$. Then
$d_f(U, W) + d_f(W, V) \ge d_f(U, V)$ for all $U, V, W \in L$.

Formalized by `JaccardLattice.jaccardDist_triangle`, a theorem declared in [MathlibExt/Combinatorics/JaccardLattice.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/JaccardLattice.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/lattices-boolean-algebras/lattice-valuations-and-the-jaccard-distance/index.html#jaccard-dist-triangle).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lattice valuations and the Jaccard distance](https://deicyde.github.io/atlas-lean/roadmap/Order/lattices-boolean-algebras/lattice-valuations-and-the-jaccard-distance/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Order/lattices-boolean-algebras/lattice-valuations-and-the-jaccard-distance)
