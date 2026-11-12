---
declaration: section
origin: cited
lean: OAI.ComplexCancellation.main
statement: formalized
proof: formalized
---

# 047. Zariski cancellation and affine fibrations over the complex numbers

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs an integral complex affine fourfold $X\not\cong\mathbb A^4$ with $X\times\mathbb A^1\cong\mathbb A^5$, disproving affine-space cancellation over ℂ in dimension four. It also disproves the Dolgachev–Weisfeiler affine-fibration conjecture: smooth surjections $X\to\mathbb A^1$ and $\mathbb A^5\to\mathbb A^2$ have every residue-field fiber isomorphic to affine three-space but are not Zariski-locally trivial.

## An explicit failure of complex affine-space cancellation

We construct an explicit integral complex affine fourfold *X* with $X\times\mathbb A^1\cong\mathbb A^5$ but $X\not\cong\mathbb A^4$. This gives a negative answer to Zariski's affine-space cancellation problem over ℂ in dimension four. The same construction disproves the Stable Coordinate Conjecture in ambient dimension five and yields smooth 𝔸$^{3}$-fibrations over 𝔸$^{1}$ and 𝔸$^{2}$ that are not Zariski-locally trivial. These fibrations disprove the Dolgachev–Weisfeiler affine-fibration conjecture over these bases.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Affine-space cancellation asks whether $X\times\mathbb A^1\cong\mathbb A^{n+1}$ forces $X\cong\mathbb A^n$. The formalized result gives an explicit finite-type complex domain $A$ of Krull dimension four with $A[w]\cong\mathbb C[x_1,\ldots,x_5]$ but $A\not\cong\mathbb C[x_1,\ldots,x_4]$. Thus adjoining one variable erases a genuine algebraic distinction.

The separate stable-coordinate and general line-bundle lifting consequences are not included.

## Lean: Complex affine-space cancellation counterexample

Stated in [ComplexCancellation.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ComplexCancellation.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main : MainStatement
```

Proved in [lean/OAI/Algebra/AffineCancellation/Main.lean, line 32](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Algebra/AffineCancellation/Main.lean#L32).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/047.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/047.md)
