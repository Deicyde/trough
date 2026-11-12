---
declaration: section
origin: cited
lean: OAI.KadisonKastler.universal_strong_stability
statement: formalized
proof: formalized
---

# 289. Strong Kadison–Kastler stability and its spatial boundaries

3 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that sufficiently close unital von Neumann algebras on the same Hilbert space are conjugate by a unitary arbitrarily close to the identity, with a universal tolerance in the operator-norm distance between unit balls. Counterexamples show that near-identity conjugacy fails for one-sided near inclusions, and that arbitrarily close norm-separable $C^{∗}$-algebras need not be ambiently unitarily conjugate.

## Universal strong Kadison–Kastler stability

We prove that sufficiently close unital von Neumann algebras are conjugate by a unitary arbitrarily close to the identity. The tolerance depends only on the prescribed distance of that unitary from the identity, uniformly over all algebras, representations, and Hilbert spaces. This resolves the strong Kadison–Kastler conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## Near Inclusions of von Neumann Algebras Without Small Spatial Embeddings

We give a negative answer to the unrestricted small-spatial-embedding problem for one-sided near inclusions of von Neumann algebras. On separable complex Hilbert spaces, we construct pairs of unital von Neumann algebras with common identity whose one-sided gaps tend to zero. Spatial embeddings of the source into the target exist, but every implementing unitary stays a fixed positive distance from the identity. The obstruction therefore concerns small implementing unitaries, rather than the existence of spatial embeddings.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Near-Inclusions-of-von-Neumann-Algebras-Without-Small-Spatial-Embeddings-October-5-2026/near-inclusions.pdf).

## Close Separable C*-Algebras Without Spatial Conjugacy

We disprove the separable $C^{∗}$-algebraic spatial form of the Kadison–Kastler conjecture. For every *ε* > 0, we construct unital, norm-separable $C^{∗}$-algebras on a common separable complex Hilbert space, with the same identity and Kadison–Kastler distance less than *ε*, that are not conjugate by any unitary. The two algebras have the same von Neumann closure.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Close-Separable-Cstar-Algebras-Without-Spatial-Conjugacy-October-5-2026/paper.pdf).

## The Lean formalization

The formalization proves the strong Kadison–Kastler conjecture uniformly. For every $\varepsilon>0$, there is a $\delta>0$ such that any two unital von Neumann algebras on the same complex Hilbert space at Kadison–Kastler distance below $\delta$ are conjugate by a unitary $u$ with $\lVert u-1\rVert<\varepsilon$. The tolerance depends only on $\varepsilon$, uniformly over the algebras, their representations, and the Hilbert space.

## Lean: Universal near-identity unitary conjugacy for close von Neumann algebras

Stated in [StrongKadisonKastler.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/StrongKadisonKastler.lean).

```lean
theorem universal_strong_stability : UniversalStrongStability.{u}
```

Proved in [lean/OAI/Analysis/KadisonKastler/UnconditionalStability.lean, line 41](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/KadisonKastler/UnconditionalStability.lean#L41).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/289.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/289.md)
