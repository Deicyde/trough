---
declaration: section
origin: cited
lean: OAI.LipschitzCounterexample.main, OAI.C0Absorption.main_result
statement: formalized
proof: formalized
---

# 324. Lipschitz equivalent Banach spaces need not be linearly isomorphic

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs separable real Banach spaces that are globally bi-Lipschitz equivalent but not linearly isomorphic, resolving the separable Lipschitz-isomorphism problem negatively. Thus even the complete metric structure up to bi-Lipschitz equivalence does not determine a separable Banach space's linear isomorphism class.

## Lipschitz Equivalent Separable Banach Spaces Need Not Be Linearly Isomorphic

There are separable real Banach spaces that are globally bi-Lipschitz equivalent but not linearly isomorphic. This gives a negative answer to the separable Banach-space Lipschitz-isomorphism problem.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## Bi-Lipschitz Absorption of c0 Without a Linear Copy of c0

We construct a separable real Banach space *Z* that contains no linear copy of $c_{0}$, yet is bi-Lipschitz equivalent to $Z\oplus_\infty c_0$. The same space contains a bi-Lipschitz image of every separable metric space.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized counterexample gives separable real Banach spaces $X,Y$ that are bi-Lipschitz equivalent but not linearly isomorphic. The bijection has lower Lipschitz bound $4/21$ and upper bound $76/25$. The linear obstruction is explicit: $X$ contains a linear isometric copy of $c_0(\ell_2)$, whereas $Y$ contains no bounded linear copy of that space.

The formalized result constructs one separable real Banach space $X$ that is bi-Lipschitz equivalent to $X\times c_0$ but contains no closed linear subspace isomorphic to $c_0$. The same space contains a bi-Lipschitz copy of $c_0$, is bi-Lipschitz universal for separable metric spaces, and is not linearly isomorphic to $X\times c_0$. Thus nonlinear absorption of $c_0$ does not force a linear copy of it.

## Lean: Bi-Lipschitz equivalent nonisomorphic Banach spaces

Stated in [LipschitzEquivalence.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/LipschitzEquivalence.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main : MainClaim
```

Proved in [lean/OAI/Analysis/LipschitzEquivalence/Main.lean, line 8](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/LipschitzEquivalence/Main.lean#L8).

## Lean: Bi-Lipschitz absorption of $c_0$

Stated in [C0Absorption.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/C0Absorption.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main_result : MainConclusion
```

Proved in [lean/OAI/Analysis/C0Absorption/Main.lean, line 33](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/C0Absorption/Main.lean#L33).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/324.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/324.md)
